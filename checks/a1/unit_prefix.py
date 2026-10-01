#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0265; see history/sources.json.
"""

from fractions import Fraction
from math import gcd, isqrt

import sympy as sp


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def check_identity() -> None:
    a1, a2, J, V, Z, W = sp.symbols("a1 a2 J V Z W")
    q, den = 11 * W, 1011 * W
    recovery = q * Z * a1 - den * J + 101 * V
    alpha = (10 * Z * a1 + a2) * 100 * W + recovery
    H = q * a2 + V
    assert sp.expand((alpha - 101 * H).subs(a2, Z * a1 - J)) == 0
    assert sp.divisors(11) == [1, 11]


def certify() -> dict[str, int]:
    check_identity()
    counts = {key: 0 for key in ("prefix", "J", "square_discriminant", "root", "solution")}
    square_points = []
    for c in (0, 1):
        q, den, qa = 11 * 10**c, 1011 * 10**c, 10200
        tail_lo, tail_hi = 10 ** (c + 1), 10 ** (c + 2) - 1
        for d in (0, 1):
            for k in range(1, (2 + c if d == 0 else 4 + c) + 1):
                Z = 10**k
                for a1 in range(10**d, 10 ** (d + 1)):
                    counts["prefix"] += 1
                    cap = Fraction(q * (a1 * a1 + 100), 2 * Z)
                    vmax = (cap.numerator - 1) // cap.denominator
                    base = q * Z * a1
                    Jlo = max(1, Z * a1 - (10 * Z - 1), ceil_div(base - tail_hi + 101, den))
                    Jhi = min(Z * a1 - Z, (base - tail_lo + 101 * vmax) // den)
                    for J in range(Jlo, Jhi + 1):
                        a2, B = Z * a1 - J, base - den * J
                        counts["J"] += 1
                        lin, qc = 101 * B - q * a2, B * B + q * q * a1 * a1
                        D = lin * lin - qa * qc
                        if D < 0:
                            continue
                        rd = isqrt(D)
                        if rd * rd != D:
                            continue
                        counts["square_discriminant"] += 1
                        square_points.append((c, d, k, a1, J))
                        for numerator in set((-lin + rd, -lin - rd)):
                            if numerator % qa:
                                continue
                            V = numerator // qa
                            if not 1 <= V <= vmax:
                                continue
                            a3 = B + 101 * V
                            if not tail_lo <= a3 <= tail_hi:
                                continue
                            counts["root"] += 1
                            if gcd(a3, q) != 1:
                                continue
                            H = q * a2 + V
                            alpha = (a1 * 10 * Z + a2) * 10 ** (c + 2) + a3
                            assert H * H == q * q * (a1 * a1 + a2 * a2) + a3 * a3
                            assert alpha == 101 * H
                            counts["solution"] += 1
    print(f"square projection points: {square_points}")
    assert square_points == []
    assert counts == {"prefix": 855, "J": 161, "square_discriminant": 0, "root": 0, "solution": 0}
    return counts


if __name__ == "__main__":
    print(certify())
    print("PASS: complete g=0,b1=b2=1,balanced b3 certificate")
    print("No claim for arbitrary prefixes or unbalanced b3.")
