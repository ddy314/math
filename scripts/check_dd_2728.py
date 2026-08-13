"""Finite certificate for S_12=4, m_3=14 on n_3=8S_12-1."""

from __future__ import annotations

from fractions import Fraction

from collections import Counter

from check_dd_2726 import Counts, check_quadratic_ranges, check_slice


S = 4
N_3 = 31
M_3 = 14
D_3 = N_3 - M_3
COARSE_SHAPES = {
    (1, 3, 2, 1),
    (1, 3, 3, 1),
    (1, 3, 3, 2),
    (1, 3, 4, 1),
    (1, 3, 4, 2),
    (1, 3, 5, 1),
    (2, 2, 1, 4),
    (2, 2, 1, 5),
    (2, 2, 4, 1),
    (2, 2, 5, 1),
    (3, 1, 1, 2),
    (3, 1, 1, 3),
    (3, 1, 1, 4),
    (3, 1, 1, 5),
    (3, 1, 2, 3),
    (3, 1, 2, 4),
}
KILLED_SHAPES = {
    (1, 3, 2, 1),
    (1, 3, 3, 2),
    (2, 2, 4, 1),
}
SHAPES = {
    (1, 3): ((3, 1), (4, 1), (4, 2), (5, 1)),
    (2, 2): ((1, 4), (1, 5), (5, 1)),
    (3, 1): ((1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4)),
}
EXPECTED_COUNTS = Counts(
    tail_rows=379935,
    eligible_tail_rows=361023,
    denominator_pairs=23355,
    shape_denominator_pairs=101112,
    digit_pairs=40488912720,
    coprime_pairs=15952005956,
    squarefree_pairs=6322749453,
    valuation_tail_pairs=1077887,
    modular_square_pairs=99342,
    nonnegative_discriminants=99342,
    square_discriminants=0,
)
EXPECTED_POSITIONS = Counter(
    {"b3-unique": 379590, "all-odd": 174, "prefix-or-tie": 171}
)


def power_of_ten(exponent: int) -> Fraction:
    if exponent >= 0:
        return Fraction(10**exponent)
    return Fraction(1, 10 ** (-exponent))


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

    for m_1, m_2, n_1, n_2 in KILLED_SHAPES:
        ratio_upper = power_of_ten(
            n_1 + 2 * m_2 - n_2
        ) + power_of_ten(n_2 + 2 * m_1)
        assert 40 * 10 ** (2 * S) * ratio_upper < 10**D_3


def main() -> None:
    check_quadratic_ranges()
    print("exact positive-quadratic interval solver: OK")
    check_digit_kernel()
    print("m_3=14 digit kernel and three size exclusions: OK")
    counts, positions = check_slice(M_3, D_3, SHAPES)
    assert positions == EXPECTED_POSITIONS
    assert counts == EXPECTED_COUNTS
    print(f"tail positions = {dict(positions)}")
    print(counts)
    print("DD 27.28 S=4, m_3=14 certificate: OK")


if __name__ == "__main__":
    main()
