#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0266; see history/sources.json.
"""

from fractions import Fraction
from math import gcd, isqrt

import sympy as sp


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def check_funnel_and_corners() -> None:
    a1, a2, J, V, Z = sp.symbols("a1 a2 J V Z")
    H = 10100 * a2 + V
    alpha = (a1 * 1000 * Z + a2) * 100000 + sp.Symbol("a3")
    recovery = 910100 * Z * a1 - 100910100 * J + 10001 * V
    assert sp.expand((alpha - 10001 * H).subs(a2, Z * a1 - J)).subs(sp.Symbol("a3"), recovery) == 0
    allowed = []
    for e in (1, 2, 3):
        Q0 = 10 ** (e + 1) + 1
        for j in sp.divisors(Q0):
            if len(str(j)) == 4 - e and j % 20 in (1, 9):
                allowed.append((e, j))
    assert allowed == [(1, 101), (3, 1)]
    # e=3,j=1 means all three denominators are powers of ten: global D9.
    assert 1**2 + 1**2 + 1**2 != 0 % 9
    assert Fraction(101000 * (1000**2 + 1), 20 * 10**10) < 1
    # All-g d2 pure equal-prefix contact: R/(Zr1)^2<201/10000.
    assert Fraction(201, 10000) < Fraction(5, 6) ** 2


def certify() -> dict[str, int]:
    check_funnel_and_corners()
    E, M, j, F0, q = 10, 100, 101, 10001, 101000
    xi, lam = Fraction(1010, 1011), Fraction(1, 101)
    tail_lo, tail_hi, den = 10000, 99999, 100910100
    counts = {key: 0 for key in ("prefix", "J", "square_discriminant", "root", "solution")}
    square_points = []
    for d in (0, 1):
        for k in (range(1, 8) if d == 0 else range(1, 10)):
            Z = 10**k
            contact_cap = Fraction(E * E * (10000 * Z * Z + 1), 1) / (
                xi * xi * (1 - lam) ** 2 * Z * Z - 1
            )
            a1_hi = min(10 ** (3 + d) - 1, isqrt((contact_cap.numerator - 1) // contact_cap.denominator))
            for a1 in range(10 ** (2 + d), a1_hi + 1):
                if gcd(a1, E) != 1:
                    continue
                counts["prefix"] += 1
                # r2>=10Z, r3<1, r1=a1/E.
                cap = Fraction(q * (a1 * a1 + E * E), 20 * E * E * Z)
                vmax = (cap.numerator - 1) // cap.denominator
                base = 910100 * Z * a1
                Jlo = max(1, Z * a1 - (10 ** (k + 3) - 1), ceil_div(base - tail_hi + F0, den))
                Jhi = min(Z * a1 - 10 ** (k + 2), (base - tail_lo + F0 * vmax) // den)
                for J in range(Jlo, Jhi + 1):
                    a2 = Z * a1 - J
                    if gcd(a2, E) != 1:
                        continue
                    counts["J"] += 1
                    B, qa = base - den * J, F0 * F0 - 1
                    lin = F0 * B - j * M * a2
                    qc = B * B + j * j * M * M * a1 * a1
                    D = lin * lin - qa * qc
                    if D < 0:
                        continue
                    rd = isqrt(D)
                    if rd * rd != D:
                        continue
                    counts["square_discriminant"] += 1
                    square_points.append((d, k, a1, J, rd, -lin + rd, -lin - rd))
                    for numerator in set((-lin + rd, -lin - rd)):
                        if numerator % qa:
                            continue
                        V = numerator // qa
                        if not 1 <= V <= vmax:
                            continue
                        a3 = B + F0 * V
                        if not tail_lo <= a3 <= tail_hi:
                            continue
                        counts["root"] += 1
                        if gcd(a3, q) != 1:
                            continue
                        H = j * M * a2 + V
                        alpha = (a1 * 10 ** (k + 3) + a2) * 100000 + a3
                        assert H * H == (j * M * a1) ** 2 + (j * M * a2) ** 2 + a3 * a3
                        assert alpha == F0 * H
                        counts["solution"] += 1
    assert square_points == [(0, 1, 981, 489, 260616360000, 404470706460000, 403949473740000)]
    assert Fraction(404470706460000, 100020000) == Fraction(6741178441, 1667)
    assert 403949473740000 // 100020000 == 4038687
    assert 910100 * 10 * 981 - den * 489 + F0 * 4038687 == -26049213
    print(f"square projection points: {square_points}")
    assert counts == {"prefix": 2566, "J": 30923, "square_discriminant": 1, "root": 0, "solution": 0}
    return counts


if __name__ == "__main__":
    print(certify())
    print("PASS: complete g=1,delta=2 pure equal-prefix balanced-tail certificate")
    print("No claim for delta>=3, general unit prefixes, or the whole A1 branch.")
