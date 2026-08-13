#!/usr/bin/env python3
"""Mechanically check the bounded arithmetic in DD Section 27.13.

The Markdown text proves the unbounded reductions.  This helper checks the
logarithm certificates, the residual (S, m3) size kernel, and the final
cofactor-interval certificate.  It does not enumerate original DD candidates;
instead it exhausts the explicitly bounded necessary valuation data.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def valuation_tuples(S: int, m3: int) -> list[tuple[int, int, int, int, int, int]]:
    """Return all valuation tuples surviving the exact height inequalities."""

    tuples: list[tuple[int, int, int, int, int, int]] = []
    combined_rhs = 2**6 * 11**3 * 10 ** (12 * S + 3)

    # Q,G < 10^S imply q,g < 4S.  Under the extreme digit shape,
    # N12 < 2*10^(4S), hence n < 14S for S >= 2.  The k5 height bound
    # and m3 >= 3S+1 imply A5 <= 3S+1, so range(3S+2) is ample.
    for q2 in range(4 * S):
        if 2**q2 >= 10**S:
            continue
        for n2 in range(14 * S + 1):
            if 2**n2 >= 2 * 10 ** (4 * S):
                continue
            for A5 in range(3 * S + 2):
                if (2 * m3 + A5) % 3:
                    continue

                combined_lhs = (
                    10 ** (2 * m3)
                    * 2 ** (4 * m3 + 6 * q2 + 3 * n2)
                    * 5**A5
                )
                if combined_lhs >= combined_rhs:
                    continue

                k5 = (2 * m3 + A5) // 3
                for g2 in range(4 * S):
                    if 2**g2 >= 10**S:
                        continue
                    f2 = 2 * m3 + 2 * q2 + n2 - g2 - 3
                    if f2 < 0:
                        continue
                    if 2 ** (g2 + 1) * 5**k5 >= 10 ** (2 * S + 1):
                        continue
                    if 2**f2 >= 11 * 10 ** (2 * S):
                        continue
                    tuples.append((q2, n2, A5, g2, f2, k5))

    return tuples


def interval_contains_odd_multiple(lo: int, hi: int, modulus: int) -> bool:
    """Whether [lo, hi] contains modulus times an odd positive integer."""

    first_quotient = (lo + modulus - 1) // modulus
    if first_quotient % 2 == 0:
        first_quotient += 1
    return first_quotient * modulus <= hi


def cofactor_survivors(
    S: int,
    tuples: list[tuple[int, int, int, int, int, int]],
) -> list[tuple[tuple[int, int, int, int, int, int], int]]:
    """Return valuation/cofactor pairs not killed by the v2 interval."""

    G_max = 9 * (10 ** (S - 1) - 1)
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
    # Logarithm certificates used in the text.
    assert 10**2 < 5**3
    assert 10**3 < 2**10
    assert 10**301 < 2**1000 < 10**302
    assert 11**500 < 10**521

    # If Xi < 20 and A2 - A5 == 1 (mod 3), then Xi is 2 or 16.
    assert 2**5 >= 20
    assert 5**2 >= 20
    xi_values = {
        2**a2 * 5**a5
        for a2 in range(5)
        for a5 in range(2)
        if 2**a2 * 5**a5 < 20 and (a2 - a5) % 3 == 1
    }
    assert xi_values == {2, 16}

    # The non-b3 2-adic positions cannot reach n3 = 8S + 4.
    assert Fraction(29, 4) * 4 + Fraction(20, 3) < 8 * 4 + 4
    assert Fraction(150, 23) < 3 * 2 + 4
    assert Fraction(210, 23) < 3 * 3 + 4

    # Rational consequences of 301/1000 < log10(2) and
    # log10(11) < 521/500 in the t2 = 1 branch.
    lower_slope = Fraction(1000, 233)
    lower_constant = Fraction(-801, 233)
    upper_slope = Fraction(1000, 267)
    upper_constant = Fraction(661, 267)
    compatibility_cap = Fraction(541, 50)
    assert compatibility_cap < 11

    initial_kernel: list[tuple[int, int]] = []
    for S in range(2, 11):
        for m3 in range(3 * S + 4, 6 * S + 4):
            if (
                Fraction(m3) > lower_slope * S + lower_constant
                and Fraction(m3) < upper_slope * S + upper_constant
            ):
                initial_kernel.append((S, m3))

    assert initial_kernel == [
        (3, 13),
        (4, 16),
        (4, 17),
        (5, 19),
        (5, 20),
        (5, 21),
        (6, 23),
        (6, 24),
        (7, 27),
        (7, 28),
        (8, 31),
        (8, 32),
        (9, 36),
    ]

    # For every residual size, the surplus lower bound is greater than
    # 2S - 2.  Since s + Ds is even and at most 2S, it must equal 2S.
    assert all(30 * S + 6 > 7 * m3 for S, m3 in initial_kernel)

    # Section 27.12 already excludes the first two cases below once the same
    # extreme digit shape has been forced.  The S=8 case is new here.
    reused_height_contradictions = {(4, 17), (5, 21)}
    s8_case = (8, 32)
    residual_kernel = [
        item
        for item in initial_kernel
        if item not in reused_height_contradictions and item != s8_case
    ]
    assert residual_kernel == [
        (3, 13),
        (4, 16),
        (5, 19),
        (5, 20),
        (6, 23),
        (6, 24),
        (7, 27),
        (7, 28),
        (8, 31),
        (9, 36),
    ]

    # At (S,m3)=(8,32), A5 == 2 (mod 3).  After its minimum value is
    # removed, the combined height budget is < log10(2), forcing q=n=0
    # and A5=2.  Then k5=22 and no v2(G) can satisfy both height bounds.
    slack_upper = Fraction(11) + Fraction(521, 500) - 40 * Fraction(301, 1000)
    assert slack_upper == Fraction(1, 500)
    assert slack_upper < Fraction(301, 1000)
    assert 2**6 * 5**22 > 10**17
    assert 2**57 > 11 * 10**16
    possible_g = [
        g
        for g in range(62)
        if 2 ** (g + 1) * 5**22 < 10**17
        and 2 ** (61 - g) < 11 * 10**16
    ]
    assert possible_g == []

    # Exact finite certificate for the ten remaining sizes.  The combined
    # logarithmic height inequality is exponentiated to an integer inequality
    #
    # 10^(2m) 2^(4m+6q+3n) 5^A5
    #   < 2^6 11^3 10^(12S+3).
    #
    # For every surviving valuation tuple, write
    # kappa = 2^(g+1) 5^k5 u and G = 2^g G_odd.  Exact f then requires
    # 5^k5 u + G_odd to be 2^h times an odd integer.  The possible interval
    # for that sum contains no such multiple.
    expected_tuple_counts = {
        (3, 13): 3,
        (4, 16): 27,
        (5, 19): 72,
        (5, 20): 7,
        (6, 23): 42,
        (6, 24): 14,
        (7, 27): 42,
        (7, 28): 1,
        (8, 31): 16,
        (9, 36): 1,
    }
    tuple_counts: dict[tuple[int, int], int] = {}
    for item in residual_kernel:
        tuples = valuation_tuples(*item)
        tuple_counts[item] = len(tuples)
        assert len(tuples) == expected_tuple_counts[item]
        assert cofactor_survivors(item[0], tuples) == []
    assert sum(tuple_counts.values()) == 225

    print(f"initial top-layer size kernel = {initial_kernel}")
    print(f"residual top-layer size kernel = {residual_kernel}")
    print("possible v2(G) at (S,m3)=(8,32) = []")
    print(f"exact valuation tuple counts = {tuple_counts}")
    print("cofactor-interval survivors = []")
    print("DD 27.13 arithmetic checks: OK")


if __name__ == "__main__":
    main()
