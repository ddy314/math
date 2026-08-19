#!/usr/bin/env python3
"""Uniform exact certificate closing the full A1 minimal diagonal k=g=6.

This script is independent of the third-block digit length ell.  It combines:
  * complete odd-prime h supply,
  * exact maxima of v2(N), v5(N) over all integer centers N0,
  * the proved cross-corridor exclusions,
  * the one-sided near-integer gap.

See:
  docs/proofs/exact-lift/branches/a1-only/k6-uniform-tail-certificate.md
"""

from __future__ import annotations

import math
from fractions import Fraction

import sympy as sp


K = 6
SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))

LOW_GAP = Fraction(509, 100_000_000)   # 5.09 * 10^-6
HIGH_GAP = Fraction(5045, 100_000_000) # 50.45 * 10^-6

EXPECTED_H_COUNTS = {1: 64, 2: 32, 3: 2, 4: 8}
EXPECTED_VMAX = {
    (1, 1): (1, 9),
    (1, 2): (3, 8),
    (1, 3): (1, 8),
    (1, 4): (5, 9),
    (3, 1): (1, 8),
    (3, 2): (3, 9),
}
EXPECTED_XSTAR_FLOOR = -8
EXPECTED_YSTAR_FLOOR = -15
EXPECTED_BOX = (-77, 54, -29, 12)
EXPECTED_DECADE_STATES = 8679
EXPECTED_NEAR_HITS = 0


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("vp(0,p) is not used")
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def ppow(p: int, e: int) -> Fraction:
    if e >= 0:
        return Fraction(p**e)
    return Fraction(1, p ** (-e))


def all_divisors(factors: dict[int, int]) -> list[int]:
    out = [1]
    for p, e in sorted(factors.items()):
        out = [d * p**j for d in out for j in range(e + 1)]
    return sorted(out)


def odd_prime_supply(w: int) -> list[int]:
    b1 = 10 ** (2 * K + 1) - w
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

    hs = sorted({q * s for q in q_divisors for s in selectors})
    if len(hs) != EXPECTED_H_COUNTS[w]:
        raise AssertionError(
            f"w={w}: h supply changed: {len(hs)} != {EXPECTED_H_COUNTS[w]}"
        )
    return hs


def prefix_N(z: int, w: int, N0: int) -> int:
    j = N0 + 10**K - 1
    a1 = 10 ** (3 * K + 2) + (5 - z - w) * 10 ** (K + 1) + j
    b1 = 10 ** (2 * K + 1) - w
    a2 = 10 ** (2 * K + 1) - z
    return a1 * a1 + (a2 * b1) ** 2


def valuation_maxima() -> dict[tuple[int, int], tuple[int, int]]:
    """Scan the full center superset 10^(k-1) <= N0 <= 10^k exactly."""
    out: dict[tuple[int, int], tuple[int, int]] = {}
    for z, w in SIX_TYPES:
        max2 = 0
        max5 = 0
        for N0 in range(10 ** (K - 1), 10**K + 1):
            N = prefix_N(z, w, N0)
            max2 = max(max2, vp(N, 2))
            max5 = max(max5, vp(N, 5))
        out[(z, w)] = (max2, max5)
    return out


def derive_box(hmax: int, xstar_floor: int, ystar_floor: int) -> tuple[int, int, int, int]:
    """Derive a safe global exponent box from decade + universal corridors."""
    low = 10 ** (K - 1)
    high = 10**K

    # x upper: x>K forces y>=ystar_floor, and h>=1.
    x_hi = K
    while ppow(2, x_hi + 1) * ppow(5, ystar_floor) < high:
        x_hi += 1

    # x lower: x<xstar_floor forces y<=K; use h<=hmax.
    x_lo = xstar_floor
    while Fraction(hmax) * ppow(2, x_lo - 1) * ppow(5, K) >= low:
        x_lo -= 1

    # y upper: y>K forces x>=xstar_floor, and h>=1.
    y_hi = K
    while ppow(2, xstar_floor) * ppow(5, y_hi + 1) < high:
        y_hi += 1

    # y lower: y<ystar_floor forces x<=K; use h<=hmax.
    y_lo = ystar_floor
    while Fraction(hmax) * ppow(2, K) * ppow(5, y_lo - 1) >= low:
        y_lo -= 1

    return x_lo, x_hi, y_lo, y_hi


def run() -> None:
    vmax = valuation_maxima()
    if vmax != EXPECTED_VMAX:
        raise AssertionError(f"valuation maxima changed: {vmax} != {EXPECTED_VMAX}")

    xstar_floor = min(
        2 * vp(w, 2) - 1 - K - max2
        for (z, w), (max2, max5) in vmax.items()
    )
    ystar_floor = min(-K - max5 for max2, max5 in vmax.values())

    if xstar_floor != EXPECTED_XSTAR_FLOOR:
        raise AssertionError(
            f"x* floor changed: {xstar_floor} != {EXPECTED_XSTAR_FLOOR}"
        )
    if ystar_floor != EXPECTED_YSTAR_FLOOR:
        raise AssertionError(
            f"y* floor changed: {ystar_floor} != {EXPECTED_YSTAR_FLOOR}"
        )

    hs_by_w = {w: odd_prime_supply(w) for w in (1, 2, 3, 4)}
    hmax = max(max(hs) for hs in hs_by_w.values())

    box = derive_box(hmax, xstar_floor, ystar_floor)
    if box != EXPECTED_BOX:
        raise AssertionError(f"exponent box changed: {box} != {EXPECTED_BOX}")
    x_lo, x_hi, y_lo, y_hi = box

    decade_states = 0
    near_hits = 0

    for w, hs in hs_by_w.items():
        for h in hs:
            for x in range(x_lo, x_hi + 1):
                for y in range(y_lo, y_hi + 1):
                    # Universal safe consequences of cross-corridor:
                    # x>K, y<y*_floor is impossible;
                    # y>K, x<x*_floor is impossible.
                    if x > K and y < ystar_floor:
                        continue
                    if y > K and x < xstar_floor:
                        continue

                    rho = Fraction(h) * ppow(2, x) * ppow(5, y)
                    if not (10 ** (K - 1) <= rho < 10**K):
                        continue

                    decade_states += 1
                    N0 = (rho.numerator + rho.denominator - 1) // rho.denominator
                    gap = Fraction(N0) - rho

                    if LOW_GAP < gap < HIGH_GAP:
                        near_hits += 1
                        print(
                            "NEAR HIT "
                            f"w={w} h={h} x={x} y={y} "
                            f"N0={N0} gap={gap}"
                        )

    if decade_states != EXPECTED_DECADE_STATES:
        raise AssertionError(
            f"decade-state count changed: {decade_states} != {EXPECTED_DECADE_STATES}"
        )
    if near_hits != EXPECTED_NEAR_HITS:
        raise AssertionError(
            f"near-hit count changed: {near_hits} != {EXPECTED_NEAR_HITS}"
        )

    print("valuation_maxima=", vmax)
    print(f"xstar_floor={xstar_floor} ystar_floor={ystar_floor}")
    print(f"hmax={hmax}")
    print(f"box=x[{x_lo},{x_hi}] y[{y_lo},{y_hi}]")
    print(f"decade_states={decade_states}")
    print(f"near_hits={near_hits}")
    print("CERTIFICATE OK: the full A1 minimal diagonal k=g=6 is empty.")


if __name__ == "__main__":
    run()
