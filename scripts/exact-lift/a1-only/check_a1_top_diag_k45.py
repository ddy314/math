#!/usr/bin/env python3
"""Exact finite certificates for A1 minimal diagonal k=g=4 and k=g=5.

See:
    docs/proofs/exact-lift/branches/a1-only/k4-k5-certificates.md

The implementation is the generic k>=3 certificate used after the proved
near-integer tail theorem.  Every exponent box is theorem-derived; all
rational arithmetic is exact; the final partial-data square sieve uses integer
square-root tests on Fraction numerator/denominator.
"""

from __future__ import annotations

import bisect
import math
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

import sympy as sp


SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))

EXPECTED = {
    4: {
        "h": {1: 24, 2: 48, 3: 32, 4: 16},
        "prefix": {
            (1, 1): 5839,
            (1, 2): 4494,
            (1, 3): 8868,
            (1, 4): 3001,
            (3, 1): 5838,
            (3, 2): 4495,
        },
        "states": {
            (1, 1): 37,
            (1, 2): 66,
            (1, 3): 65,
            (1, 4): 25,
            (3, 1): 38,
            (3, 2): 66,
        },
        "total_prefix": 32535,
        "total_states": 297,
        "squares": 0,
    },
    5: {
        "h": {1: 16, 2: 24, 3: 32, 4: 16},
        "prefix": {
            (1, 1): 59997,
            (1, 2): 43449,
            (1, 3): 84707,
            (1, 4): 27691,
            (3, 1): 59997,
            (3, 2): 43449,
        },
        "states": {
            (1, 1): 30,
            (1, 2): 110,
            (1, 3): 151,
            (1, 4): 34,
            (3, 1): 28,
            (3, 2): 112,
        },
        "total_prefix": 319290,
        "total_states": 465,
        "squares": 0,
    },
}


@dataclass(frozen=True)
class Prefix:
    z: int
    w: int
    j: int
    a1: int
    b1: int
    a2: int
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


@dataclass(frozen=True)
class TailState:
    h: int
    x: int
    y: int
    rho: Fraction


def vp(n: int, p: int) -> int:
    n = abs(n)
    if n == 0:
        raise ValueError("vp(0,p) is not used")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def ppow(p: int, e: int) -> Fraction:
    return Fraction(p**e) if e >= 0 else Fraction(1, p ** (-e))


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


def all_divisors(factors: dict[int, int]) -> list[int]:
    out = [1]
    for p, e in sorted(factors.items()):
        out = [d * p**j for d in out for j in range(e + 1)]
    return sorted(out)


def min_exp_ge(p: int, coeff: Fraction, target: Fraction) -> int:
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


def build_prefixes(k: int) -> list[Prefix]:
    """Complete prefix box from the integer N0 window 10^(k-1)<=N0<=10^k."""
    out: list[Prefix] = []
    n2_digits = 2 * k + 1

    for z, w in SIX_TYPES:
        c = 5 - z
        b1 = 10 ** (2 * k + 1) - w
        a2 = 10 ** (2 * k + 1) - z
        Q = 10 * b1 + 1
        G = b1
        D = 10**k * Q

        for N0 in range(10 ** (k - 1), 10**k + 1):
            j = N0 + 10**k - 1
            a1 = 10 ** (3 * k + 2) + (c - w) * 10 ** (k + 1) + j

            if math.gcd(a1, b1) != 1:
                continue

            C = a1 * 10**n2_digits + a2
            N = a1 * a1 + (a2 * b1) ** 2
            Kdef = G * G * C * C - D * D * N
            if Kdef <= 0:
                continue

            out.append(Prefix(z, w, j, a1, b1, a2, Q, G, C, N, D, Kdef))

    return out


def odd_prime_supply(k: int, w: int) -> list[int]:
    """Exact h supply from Q divisors and whole 1 mod 4 blocks of b1."""
    b1 = 10 ** (2 * k + 1) - w
    Q = 10 * b1 + 1
    q_divisors = all_divisors(sp.factorint(Q))

    blocks = [
        p**e
        for p, e in sp.factorint(b1).items()
        if p not in (2, 5) and p % 4 == 1
    ]
    selectors = [1]
    for block in blocks:
        selectors += [s * block for s in selectors]

    hs = sorted(q * s for q in q_divisors for s in selectors)
    if len(hs) != len(set(hs)):
        raise AssertionError("duplicate h in prime supply")
    return hs


def padic_data(p: Prefix, k: int) -> PadicData:
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

    if k5 != 0 or k2 != 2 * vp(p.w, 2):
        raise AssertionError("K valuation normal form failed")
    if (d2, d5) != (k, k) or (c2, c5) != (0, 0):
        raise AssertionError("D/C valuation normal form failed")

    x_star = k2 - (1 + d2 + n2)
    y_star = k5 - (d5 + n5)

    X0 = max(
        0,
        d2,
        d2 + k2 // 2 - g2 - c2,
        d2 + g2 - k2 // 2,
    )
    Y0 = max(
        0,
        d5,
        d5 + k5 // 2 - g5 - c5,
        d5 + g5 - k5 // 2,
    )

    if X0 != k or Y0 != k:
        raise AssertionError(f"cross-corridor cap failed: {(X0, Y0)} != {(k, k)}")

    return PadicData(
        k2, k5, d2, d5, g2, g5, c2, c5, n2, n5,
        x_star, y_star, X0, Y0,
    )


def finite_xy_box(
    h: int,
    pd: PadicData,
    low_rho: Fraction,
    high_rho: Fraction,
) -> tuple[int, int, int, int]:
    xs = pd.x_star
    ys = pd.y_star

    xmax = max(
        pd.X0,
        max_exp_lt(2, Fraction(h) * ppow(5, ys), high_rho),
    )
    xmin = min_exp_ge(
        2,
        Fraction(h) * ppow(5, max(ys, pd.Y0)),
        low_rho,
    )
    ymax = max(
        pd.Y0,
        max_exp_lt(5, Fraction(h) * ppow(2, xs), high_rho),
    )
    ymin = min_exp_ge(
        5,
        Fraction(h) * ppow(2, max(xs, pd.X0)),
        low_rho,
    )
    return xmin, xmax, ymin, ymax


def sector_is_possible(x: int, y: int, pd: PadicData) -> bool:
    if x > pd.x_star and y < pd.y_star and x > pd.X0:
        return False
    if x < pd.x_star and y > pd.y_star and y > pd.Y0:
        return False
    return True


def tail_candidates(
    pd: PadicData,
    hs: list[int],
    low_rho: Fraction,
    high_rho: Fraction,
) -> list[TailState]:
    out: list[TailState] = []
    for h in hs:
        xmin, xmax, ymin, ymax = finite_xy_box(h, pd, low_rho, high_rho)
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                rho = rho_value(h, x, y)
                if not (low_rho <= rho < high_rho):
                    continue
                if not sector_is_possible(x, y, pd):
                    continue
                out.append(TailState(h, x, y, rho))
    out.sort(key=lambda state: state.rho)
    return out


def certify(k: int) -> None:
    expected = EXPECTED[k]
    prefixes = build_prefixes(k)

    prefix_by_type: dict[tuple[int, int], int] = defaultdict(int)
    for p in prefixes:
        prefix_by_type[(p.z, p.w)] += 1

    if len(prefixes) != expected["total_prefix"]:
        raise AssertionError(
            f"k={k} prefix total changed: {len(prefixes)} != {expected['total_prefix']}"
        )
    if dict(prefix_by_type) != expected["prefix"]:
        raise AssertionError(f"k={k} prefix type counts changed")

    h_by_w = {w: odd_prime_supply(k, w) for w in (1, 2, 3, 4)}
    if {w: len(hs) for w, hs in h_by_w.items()} != expected["h"]:
        raise AssertionError(f"k={k} odd-prime supply counts changed")

    prefix_padic: list[PadicData] = []
    representatives: dict[tuple[int, int, int], PadicData] = {}
    for p in prefixes:
        pd = padic_data(p, k)
        prefix_padic.append(pd)
        representatives.setdefault((p.w, pd.n2, pd.n5), pd)

    low_rho = Fraction(10 ** (k - 1))
    high_rho = Fraction(10**k)

    tails_by_signature: dict[tuple[int, int, int], list[TailState]] = {}
    rho_by_signature: dict[tuple[int, int, int], list[Fraction]] = {}
    for key, pd in representatives.items():
        states = tail_candidates(pd, h_by_w[key[0]], low_rho, high_rho)
        tails_by_signature[key] = states
        rho_by_signature[key] = [state.rho for state in states]

    # From -17.425*10^-k < N0-rho < 50.45*10^-k:
    lower_margin = Fraction(1009, 20 * 10**k)  # rho > N0 - margin
    upper_margin = Fraction(697, 40 * 10**k)   # rho < N0 + margin

    states_by_type: dict[tuple[int, int], int] = defaultdict(int)
    squares_by_type: dict[tuple[int, int], int] = defaultdict(int)
    total_states = 0
    total_squares = 0

    for p, pd in zip(prefixes, prefix_padic):
        key = (p.w, pd.n2, pd.n5)
        tails = tails_by_signature[key]
        rhos = rho_by_signature[key]
        N0 = Fraction(p.j - 10**k + 1)

        lo = bisect.bisect_right(rhos, N0 - lower_margin)
        hi = bisect.bisect_left(rhos, N0 + upper_margin)
        surviving = tails[lo:hi]

        typ = (p.z, p.w)
        states_by_type[typ] += len(surviving)
        total_states += len(surviving)

        if not surviving:
            continue

        P = Fraction(p.C, p.D)
        S = Fraction(p.N, p.G * p.G)
        for state in surviving:
            theta = state.rho / p.D
            Xi = P * P - (1 + 2 * theta) * S
            if rational_square_root(Xi) is not None:
                squares_by_type[typ] += 1
                total_squares += 1

    if total_states != expected["total_states"]:
        raise AssertionError(
            f"k={k} tail total changed: {total_states} != {expected['total_states']}"
        )
    if dict(states_by_type) != expected["states"]:
        raise AssertionError(f"k={k} tail type counts changed")
    if total_squares != expected["squares"]:
        raise AssertionError(
            f"k={k} square total changed: {total_squares} != {expected['squares']}"
        )

    print(f"k={k}")
    print(f"prefixes={len(prefixes)}")
    print("h_supply=" + ",".join(f"w{w}:{len(h_by_w[w])}" for w in (1, 2, 3, 4)))
    for typ in SIX_TYPES:
        print(
            f"type={typ} prefixes={prefix_by_type[typ]} "
            f"tail_states={states_by_type[typ]} "
            f"rational_square_contacts={squares_by_type[typ]}"
        )
    print(f"tail_states={total_states}")
    print(f"rational_square_contacts={total_squares}")
    print(f"CERTIFICATE OK: k=g={k} minimal diagonal slice is empty.")
    print()


def main() -> None:
    certify(4)
    certify(5)


if __name__ == "__main__":
    main()
