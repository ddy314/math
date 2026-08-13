#!/usr/bin/env python3
"""Check the constant arithmetic in DD Section 27.18.

Section 27.18 proves an unbounded divisor contradiction for the eight
constant cores left by Section 27.17.  This helper checks the core valuation
table, the corresponding gcd caps, and the final uniform numerical gap.  It
does not prove the algebraic divisibility and does not enumerate DD blocks.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


EXPECTED: dict[int, tuple[int, int, int, int, int, int, int]] = {
    # c: (u, v, w, A2, A5, gcd cap, possible rho rows)
    1: (0, 0, 1, 1, 0, 2, 4000),
    2: (1, 0, 1, 4, 0, 16, 2000),
    3: (0, 0, 3, 1, 0, 6, 4000),
    4: (2, 0, 1, 7, 0, 128, 1000),
    5: (0, 1, 1, 1, 3, 250, 800),
    6: (1, 0, 3, 4, 0, 48, 2000),
    7: (0, 0, 7, 1, 0, 14, 4000),
    8: (3, 0, 1, 10, 0, 1024, 500),
}


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def core_row(c: int) -> tuple[int, int, int, int, int, int, int]:
    u = valuation(c, 2)
    v = valuation(c, 5)
    w = c // (2**u * 5**v)
    A2 = 1 + 3 * u
    A5 = 3 * v
    gcd_cap = 2**A2 * 5**A5 * w

    rho_base = 2 ** (u + 1) * 5**v
    z_cap = 19999 // rho_base
    rho_count = z_cap - z_cap // 2 - z_cap // 5 + z_cap // 10
    return u, v, w, A2, A5, gcd_cap, rho_count


def main() -> None:
    actual = {c: core_row(c) for c in range(1, 9)}
    assert actual == EXPECTED

    # If H/D divides rho*Q, then H/D <= rho*Q.  The proof gives
    # H/D > c*10^(2S)/D and rho*Q < 20000*10^S, hence the necessary
    # inequality 10^S < 20000*(D/c).
    largest_gcd_ratio = max(
        Fraction(row[5], c)
        for c, row in actual.items()
    )
    assert largest_gcd_ratio == 128
    assert 20_000 * largest_gcd_ratio == 2_560_000
    assert 2_560_000 < 10**7 < 10**11

    assert sum(row[6] for row in actual.values()) == 18_300
    assert all(gcd(row[2], 10) == 1 for row in actual.values())

    print(f"core rows = {actual}")
    print("possible (c, rho) rows across the eight cores = 18300")
    print(f"max(D/c) = {largest_gcd_ratio}")
    print("uniform divisor threshold = 2560000 < 10^7")
    print("DD 27.18 constant-core checks: OK")


if __name__ == "__main__":
    main()
