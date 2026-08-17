#!/usr/bin/env python3
"""Exact finite certificate for the A1 top-layer diagonal slice k=g=2, r=s=1.

This script implements only already-proved necessary conditions from the A1
proof tree.  It is intentionally exact: all rational arithmetic uses
fractions.Fraction, all square tests use integer square roots, and the finite
(x,y) box is derived from the proved decade/resonance/cross-corridor bounds.

Target slice
------------
    d = s1-g = 2,
    r = m1-2k = 1,
    s = m2+g-k = 1,
    k = g = 2.

Expected certificate
--------------------
    admissible prefixes:          333
    exact (h,x,y) tail states: 2,592,393
    rational-square contacts:       0

Run from the repository root, for example:
    uv run python scripts/check_a1_top_diag_k2.py --jobs 4
"""

from __future__ import annotations

import argparse
import math
import multiprocessing as mp
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Iterable

import sympy as sp


K = 2
GSHIFT = 2
LOW_RHO = Fraction(10)
HIGH_RHO = Fraction(100)
SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))

EXPECTED_PREFIXES = 333
EXPECTED_STATES = 2_592_393
EXPECTED_SQUARES = 0


@dataclass(frozen=True)
class Prefix:
    z: int
    w: int
    j: int
    a1: int
    b1: int
    a2: int
    b2: int
    Q: int
    G: int
    C: int
    N: int
    D: int
    Kdef: int


@dataclass(frozen=True)
class PadicData:
    k2: int
    k5: int
    d2: int
    d5: int
    g2: int
    g5: int
    c2: int
    c5: int
    n2: int
    n5: int
    x_star: int
    y_star: int
    X0: int
    Y0: int


def vp(n: int, p: int) -> int:
    n = abs(n)
    if n == 0:
        raise ValueError("vp(0,p) is not used in this certificate")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def remove_2_5(n: int) -> int:
    n = abs(n)
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n


def all_divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for p, e in factors.items():
        divisors = [d * p**j for d in divisors for j in range(e + 1)]
    return sorted(divisors)


def ppow(p: int, e: int) -> Fraction:
    if e >= 0:
        return Fraction(p**e)
    return Fraction(1, p ** (-e))


def rho_value(h: int, x: int, y: int) -> Fraction:
    return Fraction(h) * ppow(2, x) * ppow(5, y)


def rational_square_root(q: Fraction) -> Fraction | None:
    if q < 0:
        return None
    sn = isqrt(q.numerator)
    sd = isqrt(q.denominator)
    if sn * sn == q.numerator and sd * sd == q.denominator:
        return Fraction(sn, sd)
    return None


def min_exp_ge(p: int, coeff: Fraction, target: Fraction) -> int:
    """Least integer e for which coeff*p**e >= target, exactly."""
    e = 0
    value = coeff
    if value >= target:
        while value / p >= target:
            value /= p
            e -= 1
    else:
        while value < target:
            value *= p
            e += 1
    return e


def max_exp_lt(p: int, coeff: Fraction, target: Fraction) -> int:
    """Greatest integer e for which coeff*p**e < target, exactly."""
    e = 0
    value = coeff
    if value < target:
        while value * p < target:
            value *= p
            e += 1
    else:
        while value >= target:
            value /= p
            e -= 1
    return e


def build_prefixes() -> list[Prefix]:
    """Build the complete prefix list from the proved diagonal kernel.

    The diagonal significand lock gives
        1.079 < j/10^k < 2.02.
    At k=2 this is exactly j in {108,...,201}.
    The minimal-surplus theorem supplies the six (z,w) types.
    We then retain the original coprimality and the necessary Kdef>0 contact
    condition.
    """
    out: list[Prefix] = []
    k = K
    g = GSHIFT
    b2 = 1
    n2 = 5

    for z, w in SIX_TYPES:
        c = 5 - z
        b1 = 10 ** (2 * k + 1) - w
        a2 = 10 ** (2 * k + 1) - z

        for j in range(108, 202):
            x_prefix = (c - w) * 10 ** (k + 1) + j
            a1 = 10 ** (3 * k + 2) + x_prefix

            if math.gcd(a1, b1) != 1:
                continue

            Q = 10 * b1 + b2
            G = b1 * b2
            C = a1 * 10**n2 + a2
            N = (a1 * b2) ** 2 + (a2 * b1) ** 2
            D = 10**g * Q
            Kdef = G * G * C * C - D * D * N

            # Exact lift has P>R>sqrt(N/G^2), hence Kdef>0.
            if Kdef <= 0:
                continue

            out.append(
                Prefix(z, w, j, a1, b1, a2, b2, Q, G, C, N, D, Kdef)
            )

    return out


def padic_data(p: Prefix) -> PadicData:
    k2 = vp(p.Kdef, 2)
    k5 = vp(p.Kdef, 5)
    d2 = vp(p.D, 2)
    d5 = vp(p.D, 5)
    g2 = vp(p.G, 2)
    g5 = vp(p.G, 5)
    c2 = vp(p.C, 2)
    c5 = vp(p.C, 5)
    n2 = vp(p.N, 2)
    n5 = vp(p.N, 5)

    # Resonance lines for rho = h*2^x*5^y in
    # V^2 = Kdef - 2*rho*D*N.
    x_star = k2 - (1 + d2 + n2)
    y_star = k5 - (d5 + n5)

    # Primitive cross-corridor bounds from
    # a1-cross-corridor-primitive-collapse-2026-08-16.md.
    # If k_p is odd, the K-dominant high side is impossible because a square
    # cannot have odd p-adic valuation; setting the effective bound to the
    # resonance line is then conservative and exact for coverage.
    if k2 % 2 == 0:
        X0 = max(
            0,
            d2,
            d2 + k2 // 2 - g2 - c2,
            d2 + g2 - k2 // 2,
        )
    else:
        X0 = x_star

    if k5 % 2 == 0:
        Y0 = max(
            0,
            d5,
            d5 + k5 // 2 - g5 - c5,
            d5 + g5 - k5 // 2,
        )
    else:
        Y0 = y_star

    return PadicData(
        k2,
        k5,
        d2,
        d5,
        g2,
        g5,
        c2,
        c5,
        n2,
        n5,
        x_star,
        y_star,
        X0,
        Y0,
    )


def h_divisors(p: Prefix) -> list[int]:
    # The universal denominator certificate is
    #     b3 | 10^(2m3) Q^2 G.
    # Therefore the exact 2/5-free part h of b3 divides the 2/5-free part of
    # Q^2 G.  Enumerating all such divisors is complete (and deliberately may
    # include values that later fail other necessary conditions).
    odd_supply = remove_2_5(p.Q * p.Q * p.G)
    return all_divisors_from_factorization(sp.factorint(odd_supply))


def finite_xy_box(h: int, pd: PadicData) -> tuple[int, int, int, int]:
    """Return a conservative but proved-complete finite (x,y) rectangle.

    Feasible pairs satisfy the decade strip
        10 <= h*2^x*5^y < 100.

    Split by the resonance lines x=x*, y=y*.

    * If x>x* and y<y*, primitive reduction gives x<=X0.
    * If x<x* and y>y*, primitive reduction gives y<=Y0.
    * In the ++/-- and resonance sectors, the decade strip bounds the other
      exponent once one exponent is bounded by its resonance line.
    * If v_p(Kdef) is odd, the strict K-dominant p-high side is impossible.

    The formulas below simply take the worst endpoint among those sectors;
    every feasible pair is therefore inside the returned rectangle.
    """
    xs = pd.x_star
    ys = pd.y_star

    if pd.k2 % 2:
        xmax = xs
    else:
        xmax = max(
            pd.X0,
            max_exp_lt(2, Fraction(h) * ppow(5, ys), HIGH_RHO),
        )

    y_cap_when_x_low = max(ys, pd.Y0)
    xmin = min_exp_ge(
        2,
        Fraction(h) * ppow(5, y_cap_when_x_low),
        LOW_RHO,
    )

    if pd.k5 % 2:
        ymax = ys
    else:
        ymax = max(
            pd.Y0,
            max_exp_lt(5, Fraction(h) * ppow(2, xs), HIGH_RHO),
        )

    x_cap_when_y_low = max(xs, pd.X0)
    ymin = min_exp_ge(
        5,
        Fraction(h) * ppow(2, x_cap_when_y_low),
        LOW_RHO,
    )

    return xmin, xmax, ymin, ymax


def sector_is_possible(x: int, y: int, pd: PadicData) -> bool:
    # Strict K-dominant high side with odd valuation cannot be a square.
    if x > pd.x_star and pd.k2 % 2:
        return False
    if y > pd.y_star and pd.k5 % 2:
        return False

    # Primitive bounds on the two cross corridors.
    if x > pd.x_star and y < pd.y_star and x > pd.X0:
        return False
    if x < pd.x_star and y > pd.y_star and y > pd.Y0:
        return False

    return True


def exact_original_check(p: Prefix, a3: int, b3: int) -> bool:
    ell = len(str(a3))
    m3 = len(str(b3))

    # Here n2=5 and m2=1 throughout this finite slice.
    alpha = p.a1 * 10 ** (5 + ell) + p.a2 * 10**ell + a3
    beta = p.b1 * 10 ** (1 + m3) + p.b2 * 10**m3 + b3

    rhs = (
        Fraction(p.a1 * p.a1, p.b1 * p.b1)
        + Fraction(p.a2 * p.a2, p.b2 * p.b2)
        + Fraction(a3 * a3, b3 * b3)
    )
    return Fraction(alpha * alpha, beta * beta) == rhs


def check_prefix(index_and_prefix: tuple[int, Prefix]) -> tuple[int, int, int, int, int, int]:
    index, p = index_and_prefix
    pd = padic_data(p)
    hs = h_divisors(p)

    P = Fraction(p.C, p.D)
    S = Fraction(p.N, p.G * p.G)

    state_count = 0
    square_count = 0
    positive_root_count = 0
    exact_hit_count = 0

    for h in hs:
        xmin, xmax, ymin, ymax = finite_xy_box(h, pd)
        if xmin > xmax or ymin > ymax:
            continue

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                rho = rho_value(h, x, y)
                if not (LOW_RHO <= rho < HIGH_RHO):
                    continue
                if not sector_is_possible(x, y, pd):
                    continue

                state_count += 1

                # Partial-data rational-contact sieve.  The discriminant audit
                # explicitly permits this use: with (P,S,theta) fixed but r3
                # not yet constructed, rational r3 requires Xi to be a
                # nonnegative rational square.
                theta = rho / p.D
                Xi = P * P - (1 + 2 * theta) * S
                sqrt_Xi = rational_square_root(Xi)
                if sqrt_Xi is None:
                    continue

                square_count += 1
                denominator = 1 + 2 * theta

                for sign in (1, -1):
                    r3 = (
                        theta * P + sign * (1 + theta) * sqrt_Xi
                    ) / denominator
                    if r3 <= 0:
                        continue

                    positive_root_count += 1
                    a3 = r3.numerator
                    b3 = r3.denominator
                    ell = len(str(a3))

                    # A1 requires n3=ell and m3=g+ell, and rho=b3/10^ell.
                    if len(str(b3)) != GSHIFT + ell:
                        continue
                    if Fraction(b3, 10**ell) != rho:
                        continue

                    if exact_original_check(p, a3, b3):
                        exact_hit_count += 1

    return (
        index,
        state_count,
        square_count,
        positive_root_count,
        exact_hit_count,
        len(hs),
    )


def run(jobs: int) -> None:
    prefixes = build_prefixes()
    if len(prefixes) != EXPECTED_PREFIXES:
        raise AssertionError(
            f"prefix count changed: {len(prefixes)} != {EXPECTED_PREFIXES}"
        )

    indexed = list(enumerate(prefixes))
    if jobs == 1:
        results = [check_prefix(item) for item in indexed]
    else:
        ctx = mp.get_context("fork")
        with ctx.Pool(jobs) as pool:
            results = pool.map(check_prefix, indexed)

    total_states = sum(row[1] for row in results)
    total_squares = sum(row[2] for row in results)
    total_roots = sum(row[3] for row in results)
    total_hits = sum(row[4] for row in results)

    by_type: dict[tuple[int, int], list[int]] = {}
    for p, row in zip(prefixes, results):
        key = (p.z, p.w)
        acc = by_type.setdefault(key, [0, 0, 0])
        acc[0] += 1
        acc[1] += row[1]
        acc[2] += row[2]

    print(f"prefixes={len(prefixes)}")
    for key in SIX_TYPES:
        pref_count, states, squares = by_type.get(key, [0, 0, 0])
        print(
            f"type z={key[0]},w={key[1]}: "
            f"prefixes={pref_count}, states={states}, squares={squares}"
        )
    print(f"tail_states={total_states}")
    print(f"rational_square_contacts={total_squares}")
    print(f"positive_r3_roots={total_roots}")
    print(f"exact_hits={total_hits}")

    if total_states != EXPECTED_STATES:
        raise AssertionError(
            f"state count changed: {total_states} != {EXPECTED_STATES}"
        )
    if total_squares != EXPECTED_SQUARES:
        raise AssertionError(
            f"square contacts changed: {total_squares} != {EXPECTED_SQUARES}"
        )
    if total_roots != 0 or total_hits != 0:
        raise AssertionError("unexpected rational root / exact lift found")

    print("CERTIFICATE OK: k=g=2, r=s=1 diagonal slice is empty.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--jobs",
        type=int,
        default=1,
        help="worker processes (use e.g. --jobs 4 on a multicore machine)",
    )
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be >=1")
    run(args.jobs)


if __name__ == "__main__":
    main()
