"""Finite certificate for S_12=4, m_3=12 on n_3=8S_12-1.

The squarefree-gap digit bound leaves three ordered prefix shapes.  For each
shape this script scans the longer numerator block through the exact positive
intervals of the squarefree-gap quadratic, then applies the complete p-adic
state disjunction and the unified discriminant.  No a_3 values are enumerated.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cache
from itertools import combinations
from math import gcd, isqrt, prod

import numpy as np
from sympy import factorint

from check_dd_2716 import (
    bounded_divisors,
    maximum_valuation_below,
    valuation_array,
)
from check_dd_2722 import (
    Tail,
    position,
    signature_accepts,
    state_signature,
)
from check_dd_2725 import check_quadratic_ranges, positive_quadratic_ranges


S = 4
N_3 = 31
M_3 = 12
D_3 = 19
SQUARE_MODULUS = 64 * 9 * 5 * 7 * 11 * 13
SHAPES = {
    (1, 3): ((5, 1),),
    (3, 1): ((1, 4), (1, 5)),
}
COARSE_SHAPES = {
    (1, 3, 4, 1),
    (1, 3, 5, 1),
    (3, 1, 1, 4),
    (3, 1, 1, 5),
}


@dataclass
class Counts:
    tail_rows: int = 0
    eligible_tail_rows: int = 0
    denominator_pairs: int = 0
    shape_denominator_pairs: int = 0
    corner_gap_killed_tail_shape_rows: int = 0
    valuation_box_killed_tail_shape_rows: int = 0
    large_divisor_killed_tail_shape_rows: int = 0
    digit_pairs: int = 0
    coprime_pairs: int = 0
    squarefree_pairs: int = 0
    valuation_tail_pairs: int = 0
    modular_square_pairs: int = 0
    nonnegative_discriminants: int = 0
    square_discriminants: int = 0


EXPECTED_COUNTS = Counts(
    tail_rows=613218,
    eligible_tail_rows=562830,
    denominator_pairs=16186,
    shape_denominator_pairs=24278,
    digit_pairs=13766112000,
    coprime_pairs=5765369400,
    squarefree_pairs=834231374,
    valuation_tail_pairs=138352740,
    modular_square_pairs=10987773,
    nonnegative_discriminants=10987773,
    square_discriminants=0,
)
EXPECTED_POSITIONS = Counter(
    {"b3-unique": 594016, "all-odd": 6192, "prefix-or-tie": 13010}
)


def square_residue_table() -> np.ndarray:
    values = np.arange(SQUARE_MODULUS, dtype=np.int64)
    table = np.zeros(SQUARE_MODULUS, dtype=bool)
    table[(values * values) % SQUARE_MODULUS] = True
    return table


SQUARE_RESIDUES = square_residue_table()


def signature_fits_valuation_box(
    signature: tuple[int | str, ...],
    max_n_2: int,
    max_a_2: int,
    max_n_5: int,
    max_a_5: int,
) -> bool:
    """Test whether each p-adic state disjunction meets a height box."""

    if signature[0] == "b3-unique":
        two_possible = (
            0 <= int(signature[1]) <= max_n_2
            or -max_a_2 <= int(signature[2]) <= max_n_2
            or 0 <= int(signature[3]) <= max_a_2
        )
        five_offset = 4
    else:
        assert signature[0] == "all-odd"
        two_possible = int(signature[1]) <= max_n_2
        five_offset = 2
    if not two_possible:
        return False
    if signature[five_offset] == "five-unit":
        return True
    assert signature[five_offset] == "five-locked"
    return (
        0 <= int(signature[five_offset + 1]) <= max_n_5
        or -max_a_5 <= int(signature[five_offset + 2]) <= max_n_5
        or 0 <= int(signature[five_offset + 3]) <= max_a_5
    )


@cache
def coprime_count(lower: int, upper: int, denominator: int) -> int:
    """Count integers in one closed interval coprime to denominator."""

    primes = tuple(factorint(denominator))
    total = upper - lower + 1
    for size in range(1, len(primes) + 1):
        sign = -1 if size % 2 else 1
        for selected in combinations(primes, size):
            divisor = prod(selected)
            multiples = upper // divisor - (lower - 1) // divisor
            total += sign * multiples
    return total


def digit_interval(digits: int) -> tuple[int, int]:
    return 10 ** (digits - 1), 10**digits - 1


def corner_gap_possible(
    m_2: int,
    n_1: int,
    n_2: int,
    b_1: int,
    b_2: int,
    d_3: int,
) -> bool:
    """Test the exact four-corner maximum necessary for squarefree gap.

    The ratio N_12/A_12 is separately strictly convex in a_1 and a_2,
    so its maximum on the closed digit rectangle occurs at a corner.
    """

    Q = b_1 * 10**m_2 + b_2
    for a_1 in digit_interval(n_1):
        for a_2 in digit_interval(n_2):
            A_12 = a_1 * 10**n_2 + a_2
            N_12 = (a_1 * b_2) ** 2 + (a_2 * b_1) ** 2
            if 10**d_3 * A_12 < 40 * Q * Q * N_12:
                return True
    return False


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
    assert shapes == COARSE_SHAPES
    assert 4 * 10**18 + 4 * 10**12 < 10**19


def numerator_rows(
    m_1: int,
    m_2: int,
    n_1: int,
    n_2: int,
    b_1: int,
    b_2: int,
    d_3: int,
) -> tuple[np.ndarray, np.ndarray, int, int]:
    """Enumerate exactly the coprime rows inside the squarefree gap."""

    Q = b_1 * 10**m_2 + b_2
    a_1_lower, a_1_upper = digit_interval(n_1)
    a_2_lower, a_2_upper = digit_interval(n_2)
    scale = 10**n_2
    digit_pairs = (
        (a_1_upper - a_1_lower + 1) * (a_2_upper - a_2_lower + 1)
    )
    first_rows: list[np.ndarray] = []
    second_rows: list[np.ndarray] = []
    coprime_pairs = 0

    if n_1 <= n_2:
        for a_1 in range(a_1_lower, a_1_upper + 1):
            if gcd(a_1, b_1) != 1:
                continue
            coprime_pairs += coprime_count(a_2_lower, a_2_upper, b_2)
            quadratic = 40 * Q * Q * b_1 * b_1
            linear = 10**d_3
            constant = (
                40 * Q * Q * (a_1 * b_2) ** 2
                - 10**d_3 * scale * a_1
            )
            for lower, upper in positive_quadratic_ranges(
                quadratic, linear, constant, a_2_lower, a_2_upper
            ):
                values = np.arange(lower, upper + 1, dtype=np.int64)
                values = values[np.gcd(values, b_2) == 1]
                if values.size:
                    first_rows.append(
                        np.full(values.size, a_1, dtype=np.int64)
                    )
                    second_rows.append(values)
    else:
        for a_2 in range(a_2_lower, a_2_upper + 1):
            if gcd(a_2, b_2) != 1:
                continue
            coprime_pairs += coprime_count(a_1_lower, a_1_upper, b_1)
            quadratic = 40 * Q * Q * b_2 * b_2
            linear = 10**d_3 * scale
            constant = (
                40 * Q * Q * (a_2 * b_1) ** 2 - 10**d_3 * a_2
            )
            for lower, upper in positive_quadratic_ranges(
                quadratic, linear, constant, a_1_lower, a_1_upper
            ):
                values = np.arange(lower, upper + 1, dtype=np.int64)
                values = values[np.gcd(values, b_1) == 1]
                if values.size:
                    first_rows.append(values)
                    second_rows.append(
                        np.full(values.size, a_2, dtype=np.int64)
                    )

    if not first_rows:
        empty = np.array([], dtype=np.int64)
        return empty, empty, digit_pairs, coprime_pairs
    return (
        np.concatenate(first_rows),
        np.concatenate(second_rows),
        digit_pairs,
        coprime_pairs,
    )


def tail_groups(
    m_1: int,
    m_2: int,
    b_1: int,
    b_2: int,
    m_3: int,
    n_3: int,
) -> tuple[int, Counter[str], dict[tuple[int | str, ...], list[Tail]]]:
    Q = b_1 * 10**m_2 + b_2
    G = b_1 * b_2
    QG = Q * G
    total = 0
    positions: Counter[str] = Counter()
    groups: dict[tuple[int | str, ...], list[Tail]] = defaultdict(list)
    for kappa in bounded_divisors(QG, m_3, 10 * QG):
        if kappa <= QG:
            continue
        if kappa * kappa * (kappa + 2 * G) % 10**m_3:
            continue
        tail = Tail(m_1, m_2, b_1, b_2, m_3, kappa)
        total += 1
        positions[position(tail)] += 1
        signature = state_signature(tail, S, n_3)
        if signature != ("impossible",):
            groups[signature].append(tail)
    return total, positions, groups


def check_slice(
    m_3: int,
    d_3: int,
    shapes_by_denominator: dict[tuple[int, int], tuple[tuple[int, int], ...]],
    use_corner_gap: bool = False,
    use_valuation_box: bool = False,
    use_general_divisor: bool = False,
) -> tuple[Counts, Counter[str]]:
    counts = Counts()
    positions: Counter[str] = Counter()
    processed = 0

    for (m_1, m_2), shapes in shapes_by_denominator.items():
        for b_1 in range(10 ** (m_1 - 1), 10**m_1):
            for b_2 in range(10 ** (m_2 - 1), 10**m_2):
                tail_count, local_positions, groups = tail_groups(
                    m_1, m_2, b_1, b_2, m_3, N_3
                )
                counts.tail_rows += tail_count
                positions.update(local_positions)
                counts.eligible_tail_rows += sum(map(len, groups.values()))
                if not groups:
                    continue
                counts.denominator_pairs += 1

                Q = b_1 * 10**m_2 + b_2
                G = b_1 * b_2
                for n_1, n_2 in shapes:
                    counts.shape_denominator_pairs += 1
                    if use_corner_gap and not corner_gap_possible(
                        m_2, n_1, n_2, b_1, b_2, d_3
                    ):
                        counts.corner_gap_killed_tail_shape_rows += sum(
                            map(len, groups.values())
                        )
                        continue
                    max_a_2 = maximum_valuation_below(
                        10 ** (n_1 + n_2), 2
                    )
                    max_a_5 = maximum_valuation_below(
                        10 ** (n_1 + n_2), 5
                    )
                    norm_bound = (
                        10 ** (2 * (n_1 + m_2))
                        + 10 ** (2 * (n_2 + m_1))
                    )
                    max_n_2 = maximum_valuation_below(norm_bound, 2)
                    max_n_5 = maximum_valuation_below(norm_bound, 5)
                    local_groups: dict[
                        tuple[int | str, ...], list[Tail]
                    ] = defaultdict(list)
                    for signature, tails in groups.items():
                        if not use_valuation_box or signature_fits_valuation_box(
                            signature,
                            max_n_2,
                            max_a_2,
                            max_n_5,
                            max_a_5,
                        ):
                            local_groups[signature].extend(tails)
                        else:
                            counts.valuation_box_killed_tail_shape_rows += len(
                                tails
                            )
                    if not local_groups:
                        continue
                    if use_general_divisor:
                        s_1 = n_1 - m_1
                        s_2 = n_2 - m_2
                        exponent = (
                            2 * S
                            + s_1
                            + s_2
                            + abs(s_1 - s_2)
                            + 2 * m_3
                            - N_3
                            + 4
                        )
                        assert exponent >= 0
                        f_minus_upper = 2 * 10**exponent
                        divisor_groups: dict[
                            tuple[int | str, ...], list[Tail]
                        ] = defaultdict(list)
                        for signature, tails in local_groups.items():
                            for tail in tails:
                                numerator = tail.kappa * (tail.kappa + 2 * G)
                                primitive = numerator // gcd(
                                    numerator, tail.kappa + G
                                )
                                large_divisor = primitive // gcd(primitive, Q)
                                if large_divisor < f_minus_upper:
                                    divisor_groups[signature].append(tail)
                                else:
                                    counts.large_divisor_killed_tail_shape_rows += 1
                        local_groups = divisor_groups
                        if not local_groups:
                            continue
                    a_1, a_2, digit_pairs, coprime_pairs = numerator_rows(
                        m_1, m_2, n_1, n_2, b_1, b_2, d_3
                    )
                    counts.digit_pairs += digit_pairs
                    counts.coprime_pairs += coprime_pairs
                    counts.squarefree_pairs += a_1.size
                    if a_1.size == 0:
                        continue

                    A_12 = a_1 * 10**n_2 + a_2
                    N_12 = (a_1 * b_2) ** 2 + (a_2 * b_1) ** 2
                    n_2_valuation = valuation_array(N_12, 2)
                    a_2_valuation = valuation_array(A_12, 2)
                    n_5_valuation = valuation_array(N_12, 5)
                    a_5_valuation = valuation_array(A_12, 5)

                    for signature, tails in local_groups.items():
                        accepted = np.flatnonzero(
                            signature_accepts(
                                signature,
                                n_2_valuation,
                                a_2_valuation,
                                n_5_valuation,
                                a_5_valuation,
                            )
                        )
                        counts.valuation_tail_pairs += (
                            accepted.size * len(tails)
                        )
                        for tail in tails:
                            leading = tail.kappa * G * 10**d_3
                            norm_coefficient = (
                                tail.kappa
                                * (tail.kappa + 2 * G)
                                * Q
                                * Q
                            )
                            local_a = A_12[accepted] % SQUARE_MODULUS
                            local_n = N_12[accepted] % SQUARE_MODULUS
                            leading_square = (
                                (leading % SQUARE_MODULUS) ** 2
                            ) % SQUARE_MODULUS
                            residue = (
                                leading_square
                                * ((local_a * local_a) % SQUARE_MODULUS)
                                - (norm_coefficient % SQUARE_MODULUS) * local_n
                            ) % SQUARE_MODULUS
                            modular = accepted[
                                np.flatnonzero(SQUARE_RESIDUES[residue])
                            ]
                            counts.modular_square_pairs += modular.size
                            for index in modular:
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
                if processed % 2000 == 0:
                    print(
                        f"  checked {processed} denominator pairs; "
                        f"valuation-tail pairs={counts.valuation_tail_pairs}"
                    )

    return counts, positions


def main() -> None:
    check_quadratic_ranges()
    print("exact positive-quadratic interval solver: OK")
    check_digit_kernel()
    print("m_3=12 digit kernel and one-sided size exclusion: OK")
    counts, positions = check_slice(M_3, D_3, SHAPES)
    assert positions == EXPECTED_POSITIONS
    assert counts == EXPECTED_COUNTS
    print(f"tail positions = {dict(positions)}")
    print(counts)
    print("DD 27.26 S=4, m_3=12 certificate: OK")


if __name__ == "__main__":
    main()
