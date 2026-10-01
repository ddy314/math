#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0262; see history/sources.json.
"""

from fractions import Fraction
from math import gcd, isqrt


def ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def certify() -> dict[str, int]:
    e = delta = 2
    E = M = 100
    C, Q0 = 10_000_000, 1001
    q_prefix = E * Q0
    xi = Fraction(q_prefix, q_prefix + 1)
    lam = Fraction(1, Q0)
    tail_lo, tail_hi = 100_000, 999_999
    counts = {key: 0 for key in ("prefix", "J", "square_discriminant", "root", "solution")}

    for d in (0, 1):
        k_values = range(1, 8) if d == 0 else (1,)
        for k in k_values:
            Z = 10**k
            # Necessary xi*P<R, P>(1-lambda)Z r1,
            # R^2<r1^2+100Z^2+100. Strict upper bound on a1^2.
            contact_cap = Fraction(E * E * (100 * Z * Z + 100), 1) / (
                xi * xi * (1 - lam) ** 2 * Z * Z - 1
            )
            assert contact_cap > 0
            a1_cap = isqrt((contact_cap.numerator - 1) // contact_cap.denominator)
            a1_lo = 10 ** (e + d)
            a1_hi = min(10 ** (e + d + 1) - 1, a1_cap)
            for j in (11, 91):
                assert Q0 % j == 0
                q = 10_000 * j
                F0 = 1 + M * M * (Q0 // j)
                quadratic_a = F0 * F0 - 1
                for a1 in range(a1_lo, a1_hi + 1):
                    if gcd(a1, 10) != 1:
                        continue
                    counts["prefix"] += 1
                    # V=q(R-r2)>0 is integer; r3<10 and r2>=Z imply
                    # V<q(r1^2+100)/(2Z). Clear strict rational bound.
                    v_cap = Fraction(q * (a1 * a1 + 100 * E * E), 2 * E * E * Z)
                    v_max = (v_cap.numerator - 1) // v_cap.denominator
                    denominator = M * (C + j)
                    base = M * j * Z * a1
                    # Original word: a3=base-denominator*J+F0*V.
                    # These are inclusive bounds from a3 digits and 1<=V<=v_max.
                    j_lo = max(
                        1,
                        Z * a1 - (10 ** (e + k + 1) - 1),
                        ceil_div(base - tail_hi + F0, denominator),
                    )
                    j_hi = min(
                        Z * a1 - 10 ** (e + k),
                        (base - tail_lo + F0 * v_max) // denominator,
                    )
                    for J in range(j_lo, j_hi + 1):
                        a2 = Z * a1 - J
                        if gcd(a2, 10) != 1:
                            continue
                        counts["J"] += 1
                        B = base - denominator * J
                        quadratic_b = F0 * B - j * M * a2
                        quadratic_c = B * B + j * j * M * M * a1 * a1
                        # A V^2+2 b V+c=0. An integer V forces
                        # D=b^2-Ac=(A V+b)^2 to be a perfect square.
                        discriminant = quadratic_b**2 - quadratic_a * quadratic_c
                        if discriminant < 0:
                            continue
                        root_d = isqrt(discriminant)
                        if root_d * root_d != discriminant:
                            continue
                        counts["square_discriminant"] += 1
                        for numerator in set((-quadratic_b + root_d, -quadratic_b - root_d)):
                            if numerator % quadratic_a:
                                continue
                            V = numerator // quadratic_a
                            if not 1 <= V <= v_max:
                                continue
                            a3 = B + F0 * V
                            if not tail_lo <= a3 <= tail_hi:
                                continue
                            counts["root"] += 1
                            if gcd(a3, q) != 1:
                                continue
                            H = j * M * a2 + V
                            alpha = (a1 * 10 ** (e + 1 + k) + a2) * 10**6 + a3
                            assert H * H == (j * M * a1) ** 2 + (j * M * a2) ** 2 + a3 * a3
                            assert alpha == H * F0
                            counts["solution"] += 1

    assert counts == {
        "prefix": 5050,
        "J": 219101,
        "square_discriminant": 0,
        "root": 0,
        "solution": 0,
    }
    return counts


if __name__ == "__main__":
    print(certify())
    print("PASS: complete finite endpoint certificate for g=0,b1=b2=100,balanced b3")
    print("No claim for other prefix depths or for the whole A1 branch.")
