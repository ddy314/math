#!/usr/bin/env python3
"""Check the S>=4 part of the DD layer n3=8S+1.

The script verifies the rational size kernel, the general cofactor-interval
reduction, and the final mod-3 contradiction for its unique survivor.  The
small entrance-boundary cases S=2,3 are intentionally outside this certificate.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from check_dd_2713 import interval_contains_odd_multiple, valuation_tuples
from check_dd_2714 import general_cofactor_survivors


EXPECTED_BY_S: dict[int, list[int]] = {
    4: [13, 14, 15, 16, 17],
    5: [16, 17, 18, 19, 20, 21],
    6: [19, 20, 21, 22, 23, 24],
    7: [22, 23, 24, 25, 26, 27, 28],
    8: [25, 26, 27, 28, 29, 30, 31, 32],
    9: [29, 30, 31, 32, 33, 34, 35, 36],
    10: [34, 35, 36, 37, 38, 39],
    11: [38, 39, 40, 41, 42, 43],
    12: [42, 43, 44, 45, 46, 47],
    13: [46, 47, 48, 49, 50, 51],
    14: [51, 52, 53, 54],
    15: [55, 56, 57, 58],
    16: [59, 60, 61, 62],
    17: [64, 65, 66],
    18: [68, 69],
    19: [72, 73],
    20: [76, 77],
    21: [81],
}


def expected_kernel() -> list[tuple[int, int]]:
    return [(S, m3) for S, values in EXPECTED_BY_S.items() for m3 in values]


def rational_kernel() -> list[tuple[int, int]]:
    kernel: list[tuple[int, int]] = []
    for S in range(4, 23):
        lower = Fraction(1000 * S - 2301, 233)
        upper = Fraction(1000 * S + 661, 267)
        for m3 in range(3 * S + 1, 6 * S + 4):
            if lower < m3 < upper:
                kernel.append((S, m3))
    return kernel


def exact_G_odd_values(
    S: int,
    item: tuple[int, int, int, int, int, int],
    cofactor: int,
) -> list[int]:
    """List exact odd G-parts allowed by v2(kappa+2G)."""

    _, _, _, g2, f2, k5 = item
    h2 = f2 - g2 - 1
    G_odd_max = (10**S - 1) // 2**g2
    lo = 5**k5 * cofactor + 1
    hi = 5**k5 * cofactor + G_odd_max
    modulus = 2**h2
    first = (lo + modulus - 1) // modulus
    if first % 2 == 0:
        first += 1
    values: list[int] = []
    for odd_quotient in range(first, hi // modulus + 1, 2):
        values.append(odd_quotient * modulus - 5**k5 * cofactor)
    return values


def main() -> None:
    assert 10**9 < 5**13
    assert 10**301 < 2**1000 < 10**302
    assert 11**500 < 10**521

    # The other 2-adic positions cannot reach 8S+1.
    assert Fraction(29, 4) * 8 + Fraction(20, 3) < 8 * 8 + 1
    assert all(
        Fraction(10 * (6 * S + 3), 23) < 3 * S + 1
        for S in range(4, 8)
    )
    assert Fraction(38419, 1700) < 23

    kernel = rational_kernel()
    assert kernel == expected_kernel()
    assert len(kernel) == 86

    survivors: list[
        tuple[
            tuple[int, int],
            tuple[int, int, int, int, int, int],
            int,
        ]
    ] = []
    valuation_count = 0
    for size in kernel:
        tuples = valuation_tuples(*size)
        valuation_count += len(tuples)
        for item, cofactor in general_cofactor_survivors(size[0], tuples):
            survivors.append((size, item, cofactor))

    assert valuation_count == 48808
    assert survivors == [
        ((5, 16), (0, 0, 1, 8, 21, 11), 1),
    ]

    size, item, cofactor = survivors[0]
    S, m3 = size
    q2, n2, A5, g2, f2, k5 = item
    assert (q2, n2, A5, g2, f2, k5, cofactor) == (0, 0, 1, 8, 21, 11, 1)
    assert interval_contains_odd_multiple(
        5**k5 + 1,
        5**k5 + (10**S - 1) // 2**g2,
        2 ** (f2 - g2 - 1),
    )
    assert exact_G_odd_values(S, item, cofactor) == [291]

    G = 2**g2 * 291
    assert G == 74496

    # q2=0 makes Q odd, hence b2 odd.  Exhausting factor pairs with
    # m1+m2=S leaves one ordered denominator pair.
    denominator_pairs: list[tuple[int, int, int, int]] = []
    for m1 in range(1, S):
        m2 = S - m1
        for b1 in range(10 ** (m1 - 1), 10**m1):
            if G % b1:
                continue
            b2 = G // b1
            if not 10 ** (m2 - 1) <= b2 < 10**m2:
                continue
            Q = b1 * 10**m2 + b2
            if Q % 2 == 1:
                denominator_pairs.append((m1, m2, b1, b2))
    assert denominator_pairs == [(3, 2, 768, 97)]

    # The surplus lower bound gives max(s1,s2)>=4.  Together with
    # s1+s2<=2, |s1-s2|<=8 and positive numerator blocks, only one
    # ordered surplus pair remains.
    m1, m2, b1, b2 = denominator_pairs[0]
    surplus_pairs = [
        (s1, s2)
        for s1 in range(1 - m1, 26)
        for s2 in range(1 - m2, 26)
        if s1 + s2 <= 2
        and abs(s1 - s2) <= 2 * S - 2
        and max(s1, s2) >= 4
    ]
    assert surplus_pairs == [(-2, 4)]

    n1, numerator_n2 = m1 - 2, m2 + 4
    assert (n1, numerator_n2) == (1, 6)

    Q = b1 * 10**m2 + b2
    kappa = 2 ** (g2 + 1) * 5**k5
    b3_numerator = 10**m3 * Q * G
    assert b3_numerator % kappa == 0
    b3 = b3_numerator // kappa
    assert b3 == 2291407564800000

    # In the near-square discriminant, X is divisible by 3, while
    # N12*TQ*(TQ+2b3) is 1 mod 3 for every admissible a1,a2.
    assert G % 3 == 0
    assert Q % 3 == 1
    assert b3 % 3 == 0
    T = 10**m3
    assert T * Q * (T * Q + 2 * b3) % 3 == 1
    admissible_a1 = [a1 for a1 in range(1, 10) if gcd(a1, b1) == 1]
    assert admissible_a1 == [1, 5, 7]
    assert all((a1 * b2) ** 2 % 3 == 1 for a1 in admissible_a1)
    assert 2 not in {x * x % 3 for x in range(3)}

    print(f"S>=4 size kernel = {len(kernel)} pairs")
    print(f"exact valuation tuples = {valuation_count}")
    print(f"cofactor survivors = {survivors}")
    print(f"forced denominators = {(b1, b2)}, forced surpluses = {surplus_pairs[0]}")
    print("near-square discriminant mod 3 = 2 (non-square)")
    print("DD 27.15 S>=4 certificate: OK")


if __name__ == "__main__":
    main()
