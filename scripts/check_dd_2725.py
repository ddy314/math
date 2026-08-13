"""Finite certificate for the lowest S_12=4 row on n_3=8S_12-1.

Section 27.24 leaves 4 <= S_12 <= 17 on the highest allowed DD layer.
For S_12=4 the squarefree-gap bound forces m_3 >= 11.  This script
checks the complete m_3=11 slice.  It first proves the two possible digit
shapes, enumerates every exact primitive denominator tail, applies the full
2/5-adic state disjunction, and tests the unified discriminant with Python
big integers.

The numerator scan is exact but interval-driven: for fixed a_1 the
squarefree-gap inequality is an upward quadratic in a_2, so its positive
integer intervals are found by binary search.  A randomized brute-force
cross-check protects this optimization.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cache
from math import gcd, isqrt
from random import Random

import numpy as np

from check_dd_2716 import bounded_divisors, valuation_array
from check_dd_2722 import (
    Tail,
    position,
    signature_accepts,
    state_signature,
)


S = 4
N_3 = 31
M_3 = 11
D_3 = 20


@dataclass
class Counts:
    tail_rows: int = 0
    eligible_tail_rows: int = 0
    denominator_pairs: int = 0
    digit_pairs: int = 0
    coprime_pairs: int = 0
    squarefree_pairs: int = 0
    valuation_tail_pairs: int = 0
    nonnegative_discriminants: int = 0
    square_discriminants: int = 0


EXPECTED_COUNTS = Counts(
    tail_rows=382086,
    eligible_tail_rows=345643,
    denominator_pairs=8092,
    digit_pairs=6554520000,
    coprime_pairs=2745307606,
    squarefree_pairs=20178838,
    valuation_tail_pairs=694825,
    nonnegative_discriminants=694825,
    square_discriminants=0,
)
EXPECTED_POSITIONS = Counter(
    {"b3-unique": 359063, "prefix-or-tie": 17171, "all-odd": 5852}
)


@cache
def coprime_second_count(denominator: int) -> int:
    """Count five-digit integers coprime to one one-digit denominator."""

    return sum(
        gcd(value, denominator) == 1 for value in range(10000, 100000)
    )


def positive_quadratic_ranges(
    quadratic: int,
    linear: int,
    constant: int,
    lower: int,
    upper: int,
) -> list[tuple[int, int]]:
    """Return all integer intervals where ax^2-bx+c is positive."""

    assert quadratic > 0
    assert lower <= upper

    def value(x: int) -> int:
        return quadratic * x * x - linear * x + constant

    # The integer minimum is attained at one of the two integers adjacent to
    # linear/(2*quadratic).  On either side the quadratic is monotone.
    vertex_floor = linear // (2 * quadratic)
    left_end = min(upper, max(lower, vertex_floor))
    right_start = max(lower, min(upper, vertex_floor + 1))
    ranges: list[tuple[int, int]] = []

    if value(lower) > 0:
        if value(left_end) > 0:
            ranges.append((lower, left_end))
        else:
            lo, hi = lower, left_end
            while lo < hi:
                middle = (lo + hi + 1) // 2
                if value(middle) > 0:
                    lo = middle
                else:
                    hi = middle - 1
            ranges.append((lower, lo))

    if value(upper) > 0:
        if value(right_start) > 0:
            candidate = (right_start, upper)
        else:
            lo, hi = right_start, upper
            while lo < hi:
                middle = (lo + hi) // 2
                if value(middle) > 0:
                    hi = middle
                else:
                    lo = middle + 1
            candidate = (lo, upper)
        if ranges and candidate[0] <= ranges[-1][1] + 1:
            ranges[-1] = (ranges[-1][0], candidate[1])
        else:
            ranges.append(candidate)

    return ranges


def check_quadratic_ranges() -> None:
    """Cross-check the interval solver against direct integer evaluation."""

    random = Random(2725)
    for _ in range(2000):
        quadratic = random.randrange(1, 1000)
        linear = random.randrange(0, 10000)
        constant = random.randrange(-100000, 100001)
        lower = random.randrange(-100, 101)
        upper = lower + random.randrange(0, 300)
        actual = {
            value
            for interval_lower, interval_upper in positive_quadratic_ranges(
                quadratic, linear, constant, lower, upper
            )
            for value in range(interval_lower, interval_upper + 1)
        }
        expected = {
            value
            for value in range(lower, upper + 1)
            if quadratic * value * value - linear * value + constant > 0
        }
        assert actual == expected


def check_digit_kernel() -> None:
    shapes: set[tuple[int, int, int, int]] = set()
    for m_1 in range(1, S):
        m_2 = S - m_1
        for n_1 in range(1, S + 2):
            for n_2 in range(1, S + 3 - n_1):
                s_1 = n_1 - m_1
                s_2 = n_2 - m_2
                if D_3 <= 3 * S + abs(s_1 - s_2) + 2:
                    shapes.add((m_1, m_2, n_1, n_2))
    assert shapes == {(1, 3, 5, 1), (3, 1, 1, 5)}
    assert 4 * 10**19 + 4 * 10**12 < 10**20


def numerator_rows(
    b_1: int,
    b_2: int,
) -> tuple[np.ndarray, np.ndarray, int, int]:
    """Return all coprime rows satisfying the exact squarefree-gap bound."""

    # The m_3=3S-1 extremal gap has two ordered digit shapes.  The shape
    # (m_1,m_2,n_1,n_2)=(1,3,5,1) is ruled out in the proof by a uniform
    # strict estimate.  This routine handles the other shape (3,1,1,5).
    Q = b_1 * 10 + b_2
    concatenation_scale = 10**5
    digit_pairs = 9 * 90000
    coprime_pairs = 0
    first_values: list[np.ndarray] = []
    second_values: list[np.ndarray] = []

    for a_1 in range(1, 10):
        if gcd(a_1, b_1) != 1:
            continue
        coprime_pairs += coprime_second_count(b_2)

        # 10^D_3 A_12 < 40 Q^2 N_12 becomes
        #
        #   (40 Q^2 b_1^2) a_2^2 - 10^D_3 a_2
        #   + 40 Q^2 (a_1 b_2)^2 - 10^D_3 10^5 a_1 > 0.
        quadratic = 40 * Q * Q * b_1 * b_1
        linear = 10**D_3
        constant = (
            40 * Q * Q * (a_1 * b_2) ** 2
            - 10**D_3 * concatenation_scale * a_1
        )
        for lower, upper in positive_quadratic_ranges(
            quadratic, linear, constant, 10000, 99999
        ):
            values = np.arange(lower, upper + 1, dtype=np.int64)
            values = values[np.gcd(values, b_2) == 1]
            if values.size:
                first_values.append(
                    np.full(values.size, a_1, dtype=np.int64)
                )
                second_values.append(values)

    if not first_values:
        empty = np.array([], dtype=np.int64)
        return empty, empty, digit_pairs, coprime_pairs
    return (
        np.concatenate(first_values),
        np.concatenate(second_values),
        digit_pairs,
        coprime_pairs,
    )


def tail_groups(
    b_1: int,
    b_2: int,
) -> tuple[
    int,
    Counter[str],
    dict[tuple[int | str, ...], list[Tail]],
]:
    """Build every exact m_3=11 tail for one ordered denominator pair."""

    Q = b_1 * 10 + b_2
    G = b_1 * b_2
    QG = Q * G
    total = 0
    positions: Counter[str] = Counter()
    groups: dict[tuple[int | str, ...], list[Tail]] = defaultdict(list)
    for kappa in bounded_divisors(QG, M_3, 10 * QG):
        if kappa <= QG:
            continue
        if kappa * kappa * (kappa + 2 * G) % 10**M_3:
            continue
        tail = Tail(3, 1, b_1, b_2, M_3, kappa)
        total += 1
        positions[position(tail)] += 1
        signature = state_signature(tail, S, N_3)
        if signature != ("impossible",):
            groups[signature].append(tail)
    return total, positions, groups


def check_slice() -> tuple[Counts, Counter[str]]:
    """Enumerate the remaining ordered digit shape and test every tail pair."""

    counts = Counts()
    positions: Counter[str] = Counter()
    processed = 0

    for b_1 in range(100, 1000):
        for b_2 in range(1, 10):
            tail_count, local_positions, groups = tail_groups(b_1, b_2)
            counts.tail_rows += tail_count
            positions.update(local_positions)
            counts.eligible_tail_rows += sum(map(len, groups.values()))
            if not groups:
                continue

            counts.denominator_pairs += 1
            a_1, a_2, digit_pairs, coprime_pairs = numerator_rows(b_1, b_2)
            counts.digit_pairs += digit_pairs
            counts.coprime_pairs += coprime_pairs
            counts.squarefree_pairs += a_1.size
            if a_1.size == 0:
                continue

            Q = b_1 * 10 + b_2
            G = b_1 * b_2
            A_12 = a_1 * 10**5 + a_2
            N_12 = (a_1 * b_2) ** 2 + (a_2 * b_1) ** 2
            n_2 = valuation_array(N_12, 2)
            a_2_valuation = valuation_array(A_12, 2)
            n_5 = valuation_array(N_12, 5)
            a_5_valuation = valuation_array(A_12, 5)

            for signature, tails in groups.items():
                accepted = np.flatnonzero(
                    signature_accepts(
                        signature,
                        n_2,
                        a_2_valuation,
                        n_5,
                        a_5_valuation,
                    )
                )
                counts.valuation_tail_pairs += accepted.size * len(tails)
                if accepted.size == 0:
                    continue

                for tail in tails:
                    leading = tail.kappa * G * 10**D_3
                    norm_coefficient = (
                        tail.kappa
                        * (tail.kappa + 2 * G)
                        * Q
                        * Q
                    )
                    for index in accepted:
                        discriminant = (
                            leading * int(A_12[index])
                        ) ** 2 - norm_coefficient * int(N_12[index])
                        if discriminant < 0:
                            continue
                        counts.nonnegative_discriminants += 1
                        root = isqrt(discriminant)
                        if root * root == discriminant:
                            counts.square_discriminants += 1

            processed += 1
            if processed % 1000 == 0:
                print(
                    f"  checked {processed} denominator pairs; "
                    f"valuation-tail pairs={counts.valuation_tail_pairs}"
                )

    return counts, positions


def main() -> None:
    check_quadratic_ranges()
    print("exact positive-quadratic interval solver: OK")
    check_digit_kernel()
    print("m_3=11 digit kernel and one-sided size exclusion: OK")
    counts, positions = check_slice()
    assert positions == EXPECTED_POSITIONS
    assert counts == EXPECTED_COUNTS
    print(f"tail positions = {dict(positions)}")
    print(counts)
    print("DD 27.25 S=4, m_3=11 certificate: OK")


if __name__ == "__main__":
    main()
