#!/usr/bin/env python3
"""Finite certificate for small-S t2=1 resonance at n3 = 8S.

Section 27.19 first derives a bounded size/valuation box for 4 <= S <= 10.
This script checks that box, the simultaneous F_- factor bound, the exact
cofactor intervals, and the real denominator block equations.  One
denominator-tail core remains and is killed by the displayed mod-3
near-square contradiction.

The script covers only the b3-dominant, t2 = 1, five-adic resonance state.  It
does not certify the five-adic non-resonance states or all remaining small-S
2-adic positions.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from check_dd_2717 import (
    coprime_cofactor_count,
    interval_contains_odd_multiple,
    valuation_tuples,
)


EXPECTED_BY_S: dict[int, list[int]] = {
    4: list(range(12, 18)),
    5: list(range(15, 22)),
    6: list(range(18, 25)),
    7: list(range(21, 29)),
    8: list(range(24, 33)),
    9: list(range(27, 37)),
    10: list(range(31, 40)),
}

EXPECTED_VALUATION_TOTALS = {
    4: 2754,
    5: 4452,
    6: 7916,
    7: 11634,
    8: 18692,
    9: 28857,
    10: 23388,
}

EXPECTED_FMINUS_TOTALS = {
    4: 661,
    5: 603,
    6: 568,
    7: 408,
    8: 352,
    9: 311,
    10: 218,
}

EXPECTED_COFACTOR_COUNTS = {
    (4, 12): 56,
    (5, 15): 32,
    (5, 16): 1,
    (6, 18): 14,
    (7, 21): 6,
    (8, 24): 3,
    (9, 27): 1,
}

EXPECTED_FINAL_CORE = (
    5,
    16,
    (0, 0, 1, 8, 21, 11),
    1,
    3,
    2,
    768,
    97,
    76897,
    74496,
    25000000000,
    1,
)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def rational_kernel() -> list[tuple[int, int]]:
    kernel: list[tuple[int, int]] = []
    for S in range(4, 11):
        lower = Fraction(1000 * S - 2801, 233)
        upper = Fraction(1000 * S + 661, 267)
        for m3 in range(3 * S, 6 * S + 4):
            if lower < m3 < upper:
                kernel.append((S, m3))
    return kernel


def denominator_splits(
    G: int,
    S: int,
    extreme_shape: bool,
) -> list[tuple[int, int, int, int]]:
    """Return digit-compatible ordered (m1,m2,b1,b2) factorizations."""

    shapes = (
        ((1, S - 1), (S - 1, 1))
        if extreme_shape
        else tuple((m1, S - m1) for m1 in range(1, S))
    )
    result: list[tuple[int, int, int, int]] = []
    for m1, m2 in shapes:
        lower = max(10 ** (m1 - 1), (G + 10**m2 - 1) // 10**m2)
        upper = min(10**m1 - 1, G // 10 ** (m2 - 1))
        for b1 in range(lower, upper + 1):
            if G % b1:
                continue
            b2 = G // b1
            if 10 ** (m2 - 1) <= b2 < 10**m2:
                result.append((m1, m2, b1, b2))
    return result


def exact_denominator_cores(
    S: int,
    m3: int,
    tuples: list[tuple[int, int, int, int, int, int]],
) -> tuple[int, list[tuple[object, ...]]]:
    """Enumerate only the cofactor/odd-G values surviving exact intervals."""

    extreme_shape = m3 == 3 * S
    G_max = 9 * (10 ** (S - 1) - 1) if extreme_shape else 10**S - 1
    kappa_max = 10 * (10**S - 1) * G_max
    cofactor_count = 0
    cores: list[tuple[object, ...]] = []

    for item in tuples:
        q2, n2, A5, g2, f2, k5 = item
        h2 = f2 - g2 - 1
        if h2 < 1:
            continue
        base = 2 ** (g2 + 1) * 5**k5
        bound = kappa_max // base
        interval_length = G_max // 2**g2
        row_count = coprime_cofactor_count(
            bound,
            k5,
            h2,
            interval_length,
        )
        cofactor_count += row_count
        if row_count == 0:
            continue

        found = 0
        for cofactor in range(1, bound + 1):
            if gcd(cofactor, 10) != 1:
                continue
            lo = 5**k5 * cofactor + 1
            hi = 5**k5 * cofactor + interval_length
            if not interval_contains_odd_multiple(lo, hi, 2**h2):
                continue
            found += 1

            odd_multiplier = (lo + 2**h2 - 1) // 2**h2
            if odd_multiplier % 2 == 0:
                odd_multiplier += 1
            while odd_multiplier * 2**h2 <= hi:
                G_odd = odd_multiplier * 2**h2 - 5**k5 * cofactor
                odd_multiplier += 2
                if G_odd % 2 == 0:
                    continue

                G = 2**g2 * G_odd
                kappa = base * cofactor
                for m1, m2, b1, b2 in denominator_splits(
                    G,
                    S,
                    extreme_shape,
                ):
                    Q = b1 * 10**m2 + b2
                    q5 = valuation(Q, 5)
                    g5 = valuation(G, 5)
                    if valuation(Q, 2) != q2:
                        continue
                    if 2 * q5 + g5 > A5:
                        continue
                    if not Q * G < kappa <= 10 * Q * G:
                        continue
                    cores.append(
                        (
                            S,
                            m3,
                            item,
                            cofactor,
                            m1,
                            m2,
                            b1,
                            b2,
                            Q,
                            G,
                            kappa,
                            A5 - 2 * q5 - g5,
                        )
                    )
        assert found == row_count

    return cofactor_count, cores


def main() -> None:
    expected_kernel = [
        (S, m3)
        for S, values in EXPECTED_BY_S.items()
        for m3 in values
    ]
    kernel = rational_kernel()
    assert kernel == expected_kernel
    assert len(kernel) == 56

    valuation_totals = {S: 0 for S in EXPECTED_BY_S}
    fminus_totals = {S: 0 for S in EXPECTED_BY_S}
    cofactor_counts: dict[tuple[int, int], int] = {}
    final_cores: list[tuple[object, ...]] = []

    for S, m3 in kernel:
        tuples = valuation_tuples(S, m3)
        valuation_totals[S] += len(tuples)

        # From v2(F_-)=f2+1, v5(F_-)=k5 and
        # F_- < 2*10^(2*m3-4*S+4).
        fminus_tuples = [
            item
            for item in tuples
            if 2 ** item[4] * 5 ** item[5] < 10 ** (2 * m3 - 4 * S + 4)
        ]
        fminus_totals[S] += len(fminus_tuples)

        count, cores = exact_denominator_cores(S, m3, fminus_tuples)
        if count:
            cofactor_counts[(S, m3)] = count
        final_cores.extend(cores)

    assert valuation_totals == EXPECTED_VALUATION_TOTALS
    assert sum(valuation_totals.values()) == 97693
    assert fminus_totals == EXPECTED_FMINUS_TOTALS
    assert sum(fminus_totals.values()) == 3121
    assert cofactor_counts == EXPECTED_COFACTOR_COUNTS
    assert sum(cofactor_counts.values()) == 113
    assert final_cores == [EXPECTED_FINAL_CORE]

    # The sole core is the same denominator-tail core as in Section 27.15.
    *_, Q, G, kappa, required_n5 = EXPECTED_FINAL_CORE
    b3 = 10**16 * Q * G // kappa
    assert b3 == 2291407564800000
    assert required_n5 == 1
    assert G % 3 == 0
    assert Q % 3 == 1
    assert b3 % 3 == 0
    assert 10**16 % 3 == 1
    assert all(square % 3 != 2 for square in (value * value for value in range(3)))

    print(f"small-S size pairs = {len(kernel)}")
    print(f"valuation rows = {sum(valuation_totals.values())}")
    print(f"rows after the simultaneous F_- bound = {sum(fminus_totals.values())}")
    print(f"cofactor pairs after exact intervals = {sum(cofactor_counts.values())}")
    print(f"real denominator-tail cores = {final_cores}")
    print("sole core near-square residue = 2 mod 3")
    print("DD 27.19 finite resonance certificate: OK")


if __name__ == "__main__":
    main()
