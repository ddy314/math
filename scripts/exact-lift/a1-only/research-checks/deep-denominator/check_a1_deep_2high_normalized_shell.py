#!/usr/bin/env python3
"""Exact constant audit for the A1 full-2-high normalized complement shell.

This script does not certify the full 2-high branch.  It only checks the exact
rational inequalities and leading-slot bounds recorded in
`deep-2high-normalized-complement-shell.md`.
"""

from fractions import Fraction
from math import isqrt


TYPE_DATA = [
    # (z,w), strict xi lower, moderate r upper, exact lower square root
    ((1, 1), Fraction(973_439_975, 1000), 10_885_221, 6240),
    ((1, 2), Fraction(734_409_975, 1000), 8_400_003, 5420),
    ((1, 3), Fraction(528_999_975, 1000), 6_236_387, 4600),
    ((1, 4), Fraction(357_209_975, 1000), 4_394_372, 3780),
    ((3, 1), Fraction(519_839_975, 1000), 15_204_352, 4560),
    ((3, 2), Fraction(428_489_975, 1000), 13_677_244, 4140),
]

EXPECTED_UPPER_SLOTS = {
    (1, 1): 65_988,
    (1, 2): 57_968,
    (1, 3): 49_948,
    (1, 4): 41_927,
    (3, 1): 77_989,
    (3, 2): 73_969,
}

EXPECTED_COUNTS = {
    (1, 1): 59_749,
    (1, 2): 52_549,
    (1, 3): 45_349,
    (1, 4): 38_148,
    (3, 1): 73_430,
    (3, 2): 69_830,
}


def floor_sqrt_fraction(x: Fraction) -> int:
    """Return floor(sqrt(x)) exactly for x >= 0."""
    q = isqrt(x.numerator // x.denominator)
    while Fraction((q + 1) ** 2, 1) <= x:
        q += 1
    while Fraction(q * q, 1) > x:
        q -= 1
    return q


def main() -> None:
    # Full-master lower endpoint: the weakest typewise xi lower is (1,4).
    weakest = Fraction(357_209_975, 1000)
    lower_rad = 1 + 40 * weakest
    assert lower_rad == 3780**2

    # Full-master universal upper endpoint.
    universal_upper_rad = 1 + Fraction(10001 * 15_214_000, 25)
    assert universal_upper_rad == 6_086_208_561
    assert universal_upper_rad < 78_015**2
    assert 78_014**2 < universal_upper_rad

    # Therefore m=floor(R/5^d) has exactly these absolute slots.
    assert 78_014 - 3780 + 1 == 74_235

    total = 0
    print("type      lower_m  upper_m  slots")
    for typ, xi_lower, r_upper, lower_m in TYPE_DATA:
        # Strict lower shell is an exact perfect square.
        lower_rad = 1 + 40 * xi_lower
        assert lower_rad == lower_m**2

        # In moderate HL, xi=r and mu<10001.
        upper_rad = 1 + Fraction(10001 * r_upper, 25)
        upper_m = floor_sqrt_fraction(upper_rad)

        # None of the six upper radicands is itself a square, so strictness
        # leaves floor(sqrt(upper_rad)) as the largest possible leading slot.
        assert Fraction(upper_m**2, 1) < upper_rad
        assert Fraction((upper_m + 1) ** 2, 1) > upper_rad
        assert upper_m == EXPECTED_UPPER_SLOTS[typ]

        count = upper_m - lower_m + 1
        assert count == EXPECTED_COUNTS[typ]
        total += count
        print(f"{typ!s:8}  {lower_m:7d}  {upper_m:7d}  {count:5d}")

    assert total == 339_055
    print(f"total typewise slot incidences = {total}")
    print("CERTIFICATE CONSTANT AUDIT OK")


if __name__ == "__main__":
    main()
