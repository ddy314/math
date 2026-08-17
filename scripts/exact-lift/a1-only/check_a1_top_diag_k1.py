#!/usr/bin/env python3
"""Exact finite certificate for A1: d=2, r=s=1, k=g=1.

The prefix box comes from the six minimal-surplus types and the exact half-gap
windows.  The third-block enumeration uses the same proved denominator supply,
decade strip, resonance lines, and primitive cross-corridor bounds as the k=2
certificate.

Expected result:
    prefixes=79
    tail_states=113015
    rational_square_contacts=0

Run:
    uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k1.py --jobs 4
"""

from __future__ import annotations

import argparse
import math
import multiprocessing as mp
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

import sympy as sp


K = 1
GSHIFT = 1
LOW_RHO = Fraction(1)
HIGH_RHO = Fraction(10)
SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))

EXPECTED_PREFIXES = 79
EXPECTED_STATES = 113_015


@dataclass(frozen=True)
class Prefix:
    z: int
    w: int
    U1: int
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
        raise ValueError("vp(0,p) is not used")
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


def divisors_of(n: int) -> list[int]:
    factors = sp.factorint(n)
    ds = [1]
    for p, e in factors.items():
        ds = [d * p**j for d in ds for j in range(e + 1)]
    return sorted(ds)


def ppow(p: int, e: int) -> Fraction:
    return Fraction(p**e) if e >= 0 else Fraction(1, p ** (-e))


def rho_value(h: int, x: int, y: int) -> Fraction:
    return Fraction(h) * ppow(2, x) * ppow(5, y)


def rat_sqrt(q: Fraction) -> Fraction | None:
    if q < 0:
        return None
    a = isqrt(q.numerator)
    b = isqrt(q.denominator)
    if a * a == q.numerator and b * b == q.denominator:
        return Fraction(a, b)
    return None


def min_exp_ge(p: int, coeff: Fraction, target: Fraction) -> int:
    e = 0
    v = coeff
    if v >= target:
        while v / p >= target:
            v /= p
            e -= 1
    else:
        while v < target:
            v *= p
            e += 1
    return e


def max_exp_lt(p: int, coeff: Fraction, target: Fraction) -> int:
    e = 0
    v = coeff
    if v < target:
        while v * p < target:
            v *= p
            e += 1
    else:
        while v >= target:
            v /= p
            e -= 1
    return e


def strict_integer_interval(lo: Fraction, hi: Fraction) -> range:
    first = lo.numerator // lo.denominator + 1
    last = (hi.numerator - 1) // hi.denominator
    return range(first, last + 1)


def build_prefixes() -> list[Prefix]:
    out: list[Prefix] = []
    k = g = 1
    b2 = 1
    n2 = 3

    for z, w in SIX_TYPES:
        b1 = 10**3 - w
        a2 = 10**3 - z

        # For k=g=1, H0=10 and phi1=U1/b1.
        if z == 1:
            lo, hi = Fraction(2, 5), Fraction(217, 500)
        else:
            lo, hi = Fraction(1, 5), Fraction(117, 500)

        for U1 in strict_integer_interval(lo * b1, hi * b1):
            x = U1 - 100 * w
            if x < 0:
                continue

            a1 = 10**5 + x
            if math.gcd(a1, b1) != 1:
                continue

            Q = 10 * b1 + 1
            G = b1
            C = a1 * 10**n2 + a2
            N = a1 * a1 + (a2 * b1) ** 2
            D = 10 * Q
            Kdef = G * G * C * C - D * D * N
            if Kdef <= 0:
                continue

            out.append(Prefix(z, w, U1, a1, b1, a2, b2, Q, G, C, N, D, Kdef))

    return out


def padic_data(p: Prefix) -> PadicData:
    k2, k5 = vp(p.Kdef, 2), vp(p.Kdef, 5)
    d2, d5 = vp(p.D, 2), vp(p.D, 5)
    g2, g5 = vp(p.G, 2), vp(p.G, 5)
    c2, c5 = vp(p.C, 2), vp(p.C, 5)
    n2, n5 = vp(p.N, 2), vp(p.N, 5)
    xs = k2 - (1 + d2 + n2)
    ys = k5 - (d5 + n5)

    if k2 % 2 == 0:
        X0 = max(0, d2, d2 + k2 // 2 - g2 - c2, d2 + g2 - k2 // 2)
    else:
        X0 = xs

    if k5 % 2 == 0:
        Y0 = max(0, d5, d5 + k5 // 2 - g5 - c5, d5 + g5 - k5 // 2)
    else:
        Y0 = ys

    return PadicData(k2, k5, d2, d5, g2, g5, c2, c5, n2, n5, xs, ys, X0, Y0)


def h_divisors(p: Prefix) -> list[int]:
    return divisors_of(remove_2_5(p.Q * p.Q * p.G))


def finite_xy_box(h: int, pd: PadicData) -> tuple[int, int, int, int]:
    xs, ys = pd.x_star, pd.y_star

    if pd.k2 % 2:
        xmax = xs
    else:
        xmax = max(pd.X0, max_exp_lt(2, Fraction(h) * ppow(5, ys), HIGH_RHO))
    xmin = min_exp_ge(2, Fraction(h) * ppow(5, max(ys, pd.Y0)), LOW_RHO)

    if pd.k5 % 2:
        ymax = ys
    else:
        ymax = max(pd.Y0, max_exp_lt(5, Fraction(h) * ppow(2, xs), HIGH_RHO))
    ymin = min_exp_ge(5, Fraction(h) * ppow(2, max(xs, pd.X0)), LOW_RHO)

    return xmin, xmax, ymin, ymax


def sector_possible(x: int, y: int, pd: PadicData) -> bool:
    if x > pd.x_star and pd.k2 % 2:
        return False
    if y > pd.y_star and pd.k5 % 2:
        return False
    if x > pd.x_star and y < pd.y_star and x > pd.X0:
        return False
    if x < pd.x_star and y > pd.y_star and y > pd.Y0:
        return False
    return True


def check_prefix(item: tuple[int, Prefix]) -> tuple[int, int, int, int, int]:
    idx, p = item
    pd = padic_data(p)
    P = Fraction(p.C, p.D)
    S = Fraction(p.N, p.G * p.G)

    states = squares = positive_roots = exact_hits = 0

    for h in h_divisors(p):
        xmin, xmax, ymin, ymax = finite_xy_box(h, pd)
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                rho = rho_value(h, x, y)
                if not (LOW_RHO <= rho < HIGH_RHO):
                    continue
                if not sector_possible(x, y, pd):
                    continue

                states += 1
                theta = rho / p.D
                Xi = P * P - (1 + 2 * theta) * S
                root = rat_sqrt(Xi)
                if root is None:
                    continue

                squares += 1
                den = 1 + 2 * theta
                for sign in (1, -1):
                    r3 = (theta * P + sign * (1 + theta) * root) / den
                    if r3 <= 0:
                        continue
                    positive_roots += 1

                    a3, b3 = r3.numerator, r3.denominator
                    ell = len(str(a3))
                    if len(str(b3)) != 1 + ell:
                        continue
                    if Fraction(b3, 10**ell) != rho:
                        continue

                    alpha = p.a1 * 10 ** (3 + ell) + p.a2 * 10**ell + a3
                    m3 = len(str(b3))
                    beta = p.b1 * 10 ** (1 + m3) + 10**m3 + b3
                    rhs = (
                        Fraction(p.a1 * p.a1, p.b1 * p.b1)
                        + Fraction(p.a2 * p.a2)
                        + Fraction(a3 * a3, b3 * b3)
                    )
                    if Fraction(alpha * alpha, beta * beta) == rhs:
                        exact_hits += 1

    return idx, states, squares, positive_roots, exact_hits


def run(jobs: int) -> None:
    prefixes = build_prefixes()
    if len(prefixes) != EXPECTED_PREFIXES:
        raise AssertionError(f"prefixes={len(prefixes)} != {EXPECTED_PREFIXES}")

    items = list(enumerate(prefixes))
    if jobs == 1:
        results = [check_prefix(x) for x in items]
    else:
        with mp.get_context("fork").Pool(jobs) as pool:
            results = pool.map(check_prefix, items)

    total_states = sum(r[1] for r in results)
    total_squares = sum(r[2] for r in results)
    total_roots = sum(r[3] for r in results)
    total_hits = sum(r[4] for r in results)

    by_type: dict[tuple[int, int], list[int]] = {}
    for p, result in zip(prefixes, results):
        acc = by_type.setdefault((p.z, p.w), [0, 0, 0])
        acc[0] += 1
        acc[1] += result[1]
        acc[2] += result[2]

    print(f"prefixes={len(prefixes)}")
    for typ in SIX_TYPES:
        n, states, squares = by_type.get(typ, [0, 0, 0])
        print(f"type z={typ[0]},w={typ[1]}: prefixes={n}, states={states}, squares={squares}")
    print(f"tail_states={total_states}")
    print(f"rational_square_contacts={total_squares}")
    print(f"positive_r3_roots={total_roots}")
    print(f"exact_hits={total_hits}")

    if total_states != EXPECTED_STATES:
        raise AssertionError(f"tail_states={total_states} != {EXPECTED_STATES}")
    if total_squares != 0 or total_roots != 0 or total_hits != 0:
        raise AssertionError("unexpected candidate found")

    print("CERTIFICATE OK: k=g=1, r=s=1 diagonal slice is empty.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=1)
    args = ap.parse_args()
    if args.jobs < 1:
        ap.error("--jobs must be >= 1")
    run(args.jobs)


if __name__ == "__main__":
    main()
