#!/usr/bin/env python3
"""Check the finite certificates for DD layers n3=8S+3 and n3=8S+2.

The unbounded reductions and all range bounds are proved in Section 27.14.
This script uses only integer arithmetic after the rational size reduction.
It exhausts necessary valuation/cofactor data, not original DD numerators and
denominators.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from check_dd_2713 import interval_contains_odd_multiple, valuation_tuples


EXPECTED_BY_LAYER: dict[int, dict[int, list[int]]] = {
    3: {
        2: [9],
        3: [12, 13],
        4: [15, 16, 17],
        5: [18, 19, 20, 21],
        6: [21, 22, 23, 24],
        7: [25, 26, 27, 28],
        8: [29, 30, 31, 32],
        9: [34, 35, 36],
        10: [38, 39],
        11: [42, 43],
        12: [46, 47],
        13: [51],
    },
    2: {
        2: [8, 9],
        3: [11, 12, 13],
        4: [14, 15, 16, 17],
        5: [17, 18, 19, 20, 21],
        6: [20, 21, 22, 23, 24],
        7: [23, 24, 25, 26, 27, 28],
        8: [27, 28, 29, 30, 31, 32],
        9: [31, 32, 33, 34, 35, 36],
        10: [36, 37, 38, 39],
        11: [40, 41, 42, 43],
        12: [44, 45, 46, 47],
        13: [49, 50, 51],
        14: [53, 54],
        15: [57, 58],
        16: [61, 62],
        17: [66],
    },
}

EXPECTED_VALUATION_COUNTS: dict[int, list[int]] = {
    3: [
        6,
        41,
        3,
        146,
        27,
        1,
        291,
        72,
        7,
        1,
        643,
        212,
        42,
        14,
        392,
        100,
        42,
        1,
        274,
        145,
        16,
        0,
        79,
        8,
        1,
        29,
        8,
        48,
        3,
        25,
        0,
        0,
    ],
    2: [
        15,
        6,
        78,
        41,
        3,
        240,
        146,
        27,
        1,
        454,
        291,
        72,
        7,
        1,
        930,
        643,
        212,
        42,
        14,
        1469,
        1044,
        392,
        100,
        42,
        1,
        1878,
        818,
        274,
        145,
        16,
        0,
        1523,
        612,
        373,
        79,
        8,
        1,
        630,
        170,
        29,
        8,
        428,
        112,
        48,
        3,
        306,
        161,
        25,
        0,
        66,
        3,
        0,
        30,
        8,
        50,
        3,
        16,
        0,
        1,
    ],
}


def expected_kernel(layer: int) -> list[tuple[int, int]]:
    return [
        (S, m3)
        for S, values in EXPECTED_BY_LAYER[layer].items()
        for m3 in values
    ]


def rational_kernel(layer: int) -> list[tuple[int, int]]:
    """Apply the rational m3 window proved in Section 27.14."""

    cap = {3: 14, 2: 18}[layer]
    kernel: list[tuple[int, int]] = []
    for S in range(2, cap + 1):
        upper = Fraction(1000 * S + 661, 267)
        # For layer 2 at S=2 we deliberately omit the surplus lower bound,
        # obtaining a safe (slightly enlarged) finite kernel.
        lower = (
            None
            if layer == 2 and S == 2
            else Fraction(1000 * S + 500 * layer - 2801, 233)
        )
        for m3 in range(3 * S + layer, 6 * S + 4):
            if Fraction(m3) >= upper:
                continue
            if lower is not None and Fraction(m3) <= lower:
                continue
            kernel.append((S, m3))
    return kernel


def general_cofactor_survivors(
    S: int,
    tuples: list[tuple[int, int, int, int, int, int]],
) -> list[tuple[tuple[int, int, int, int, int, int], int]]:
    """Test the cofactor interval using only the general bound G<10^S."""

    G_max = 10**S - 1
    kappa_max = 10 * (10**S - 1) * G_max
    survivors: list[tuple[tuple[int, int, int, int, int, int], int]] = []

    for item in tuples:
        _, _, _, g2, f2, k5 = item
        h2 = f2 - g2 - 1
        if h2 < 1:
            continue

        base = 2 ** (g2 + 1) * 5**k5
        G_odd_max = G_max // 2**g2
        for cofactor in range(1, kappa_max // base + 1):
            if gcd(cofactor, 10) != 1:
                continue
            lo = 5**k5 * cofactor + 1
            hi = 5**k5 * cofactor + G_odd_max
            if interval_contains_odd_multiple(lo, hi, 2**h2):
                survivors.append((item, cofactor))

    return survivors


def main() -> None:
    assert 10**2 < 5**3
    assert 10**301 < 2**1000 < 10**302
    assert 11**500 < 10**521

    # Other 2-adic positions: the n3 bound handles large S and the m3
    # bound handles the listed small S.
    assert Fraction(29, 4) * 5 + Fraction(20, 3) < 8 * 5 + 3
    assert all(
        Fraction(10 * (6 * S + 3), 23) < 3 * S + 3
        for S in range(2, 5)
    )
    assert Fraction(29, 4) * 7 + Fraction(20, 3) < 8 * 7 + 2
    assert all(
        Fraction(10 * (6 * S + 3), 23) < 3 * S + 2
        for S in range(2, 7)
    )

    assert Fraction(25069, 1700) < 15
    assert Fraction(7936, 425) < 19

    layer_summaries: dict[int, tuple[int, int]] = {}
    for layer in (3, 2):
        kernel = rational_kernel(layer)
        assert kernel == expected_kernel(layer)

        counts: list[int] = []
        for S, m3 in kernel:
            tuples = valuation_tuples(S, m3)
            counts.append(len(tuples))
            assert general_cofactor_survivors(S, tuples) == []

        assert counts == EXPECTED_VALUATION_COUNTS[layer]
        layer_summaries[layer] = (len(kernel), sum(counts))

    assert layer_summaries == {3: (32, 2677), 2: (59, 14095)}
    print(f"layer summaries (size pairs, valuation tuples) = {layer_summaries}")
    print("general cofactor-interval survivors = []")
    print("DD 27.14 finite certificates: OK")


if __name__ == "__main__":
    main()
