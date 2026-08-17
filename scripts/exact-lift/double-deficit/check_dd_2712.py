#!/usr/bin/env python3
"""Mechanically check the bounded arithmetic in DD Section 27.12.

The unbounded reductions are proved in the Markdown text. This helper checks
the exact logarithm certificates, the residual (S, m3) list, and the final
integer height comparisons; it does not enumerate original DD candidates.
"""

from __future__ import annotations

from fractions import Fraction


def main() -> None:
    assert 10**3 < 2**10
    assert 2**3 < 10
    assert 11**20 < 10**21
    assert 10**301 < 2**1000 < 10**302
    assert 11**500 < 10**521

    coarse_lower_slope = Fraction(30, 7)
    coarse_lower_constant = Fraction(-10, 7)
    coarse_upper_slope = Fraction(15, 4)
    coarse_upper_constant = Fraction(163, 64)
    compatibility_cap = Fraction(1781, 240)
    assert compatibility_cap < 8
    assert coarse_lower_slope * 7 + coarse_lower_constant == Fraction(200, 7)
    assert coarse_upper_slope * 7 + coarse_upper_constant == Fraction(1843, 64)
    assert Fraction(1843, 64) < 29

    sharp_upper_slope = Fraction(1000, 267)
    sharp_upper_constant = Fraction(441, 178)
    size_candidates: list[tuple[int, int]] = []
    for S in range(2, 7):
        for m3 in range(3 * S + 5, 6 * S + 4):
            if Fraction(m3) < sharp_upper_slope * S + sharp_upper_constant:
                size_candidates.append((S, m3))
    assert size_candidates == [(4, 17), (5, 20), (5, 21), (6, 23), (6, 24)]

    rejected_by_surplus = []
    for S, m3 in size_candidates:
        if 3 * S > Fraction(7, 10) * m3 + Fraction(9, 10):
            rejected_by_surplus.append((S, m3))
    assert rejected_by_surplus == [(5, 20), (6, 23), (6, 24)]
    survivors = [item for item in size_candidates if item not in rejected_by_surplus]
    assert survivors == [(4, 17), (5, 21)]

    possible_g_4 = [
        g
        for g in range(20)
        if 2 ** (g + 1) * 5**12 < 10**9 and 2 ** (31 - g) < 11 * 10**8
    ]
    possible_g_5 = [
        g
        for g in range(20)
        if 2 ** (g + 1) * 5**14 < 10**11 and 2 ** (39 - g) < 11 * 10**10
    ]
    assert possible_g_4 == [1]
    assert possible_g_5 == [3]

    lower_kappa_4 = 2**2 * 5**12
    upper_kappa_4 = 10 * 10**4 * (9 * 999)
    lower_kappa_5 = 2**4 * 5**14
    upper_kappa_5 = 10 * 10**5 * (9 * 9999)
    assert lower_kappa_4 > upper_kappa_4
    assert lower_kappa_5 > upper_kappa_5

    print(f"residual size candidates = {size_candidates}")
    print(f"survivors after surplus height = {survivors}")
    print(f"possible v2(G): S=4 -> {possible_g_4}, S=5 -> {possible_g_5}")
    print(f"final S=4 heights: {lower_kappa_4} > {upper_kappa_4}")
    print(f"final S=5 heights: {lower_kappa_5} > {upper_kappa_5}")
    print("DD 27.12 arithmetic checks: OK")


if __name__ == "__main__":
    main()
