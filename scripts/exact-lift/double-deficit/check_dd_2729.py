"""Finish the S_12=4 boundary by checking m_3=15,...,21.

The exact primitive denominator-tail kernel is empty for m_3=22,...,26;
this is checked separately after the seven discriminant slices.  Use
``--m3`` to rerun one slice while developing or auditing the certificate.
Without that option the script checks the complete remaining range.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction

from check_dd_2716 import bounded_divisors, valuation
from check_dd_2726 import Counts, check_quadratic_ranges, check_slice


S = 4
N_3 = 31
FINITE_M3 = tuple(range(15, 22))
EMPTY_M3 = tuple(range(22, 27))
EXPECTED_SHAPES = {
    15: (28, 5, 23),
    16: (38, 3, 35),
    17: (45, 0, 45),
    18: (45, 0, 45),
    19: (45, 0, 45),
    20: (45, 0, 45),
    21: (45, 0, 45),
}
EXPECTED_STRUCTURAL_COUNTS = {
    15: (171086, 159257, 19964, 152597),
    16: (94053, 90486, 17354, 202178),
    17: (27472, 25791, 8998, 134970),
    18: (9078, 7935, 4348, 65220),
    19: (1336, 1283, 821, 12315),
    20: (188, 179, 150, 2250),
    21: (9, 9, 9, 135),
}
EXPECTED_POSITIONS = {
    15: Counter({"b3-unique": 171075, "all-odd": 9, "prefix-or-tie": 2}),
    **{
        m_3: Counter({"b3-unique": tail_rows})
        for m_3, tail_rows in zip(
            range(16, 22), (94053, 27472, 9078, 1336, 188, 9), strict=True
        )
    },
}
EXPECTED_UNFILTERED_COUNTS = {
    15: Counts(
        tail_rows=171086,
        eligible_tail_rows=159257,
        denominator_pairs=19964,
        shape_denominator_pairs=152597,
        digit_pairs=57299353506,
        coprime_pairs=21911817780,
        squarefree_pairs=10139813772,
        valuation_tail_pairs=14150484,
        modular_square_pairs=1614629,
        nonnegative_discriminants=1614629,
        square_discriminants=0,
    ),
    20: Counts(
        tail_rows=188,
        eligible_tail_rows=179,
        denominator_pairs=150,
        shape_denominator_pairs=2250,
        digit_pairs=660000150,
        coprime_pairs=158999184,
        squarefree_pairs=158999184,
        valuation_tail_pairs=1887,
        modular_square_pairs=34,
        nonnegative_discriminants=34,
        square_discriminants=0,
    ),
    21: Counts(
        tail_rows=9,
        eligible_tail_rows=9,
        denominator_pairs=9,
        shape_denominator_pairs=135,
        digit_pairs=39600009,
        coprime_pairs=10813386,
        squarefree_pairs=10813386,
        valuation_tail_pairs=0,
        modular_square_pairs=0,
        nonnegative_discriminants=0,
        square_discriminants=0,
    ),
}


def power_of_ten(exponent: int) -> Fraction:
    if exponent >= 0:
        return Fraction(10**exponent)
    return Fraction(1, 10 ** (-exponent))


def digit_shapes(
    m_3: int,
) -> tuple[
    set[tuple[int, int, int, int]],
    set[tuple[int, int, int, int]],
    dict[tuple[int, int], tuple[tuple[int, int], ...]],
]:
    """Return coarse, size-killed, and surviving ordered digit shapes."""

    d_3 = N_3 - m_3
    coarse: set[tuple[int, int, int, int]] = set()
    killed: set[tuple[int, int, int, int]] = set()
    survivors: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for m_1 in range(1, S):
        m_2 = S - m_1
        for n_1 in range(1, S + 2):
            for n_2 in range(1, S + 3 - n_1):
                s_1 = n_1 - m_1
                s_2 = n_2 - m_2
                if d_3 > 3 * S + abs(s_1 - s_2) + 2:
                    continue
                row = (m_1, m_2, n_1, n_2)
                coarse.add(row)
                ratio_upper = power_of_ten(
                    n_1 + 2 * m_2 - n_2
                ) + power_of_ten(n_2 + 2 * m_1)
                if 40 * 10 ** (2 * S) * ratio_upper < 10**d_3:
                    killed.add(row)
                    continue
                survivors.setdefault((m_1, m_2), []).append((n_1, n_2))
    return (
        coarse,
        killed,
        {key: tuple(values) for key, values in survivors.items()},
    )


def check_one_slice(m_3: int, *, use_prefilters: bool = True) -> None:
    assert m_3 in FINITE_M3
    coarse, killed, shapes = digit_shapes(m_3)
    counts, positions = check_slice(
        m_3,
        N_3 - m_3,
        shapes,
        use_corner_gap=use_prefilters,
        use_valuation_box=use_prefilters,
        use_general_divisor=use_prefilters,
    )
    shape_summary = (
        len(coarse), len(killed), sum(map(len, shapes.values()))
    )
    assert shape_summary == EXPECTED_SHAPES[m_3]
    assert (
        counts.tail_rows,
        counts.eligible_tail_rows,
        counts.denominator_pairs,
        counts.shape_denominator_pairs,
    ) == EXPECTED_STRUCTURAL_COUNTS[m_3]
    assert positions == EXPECTED_POSITIONS[m_3]
    if not use_prefilters and m_3 in EXPECTED_UNFILTERED_COUNTS:
        assert counts == EXPECTED_UNFILTERED_COUNTS[m_3]
    if use_prefilters and m_3 <= 20:
        assert counts.valuation_tail_pairs > 0
    if use_prefilters and m_3 in {15, 16, 17, 18, 20}:
        assert counts.modular_square_pairs > 0
    assert counts.square_discriminants == 0
    print(
        f"m_3={m_3}: coarse-shapes={shape_summary[0]}, "
        f"size-killed={shape_summary[1]}, surviving-shapes={shape_summary[2]}"
    )
    print(f"  tail positions = {dict(positions)}")
    print(f"  {counts}")


def check_empty_high_tails() -> None:
    """Enumerate divisors once per denominator and prove m_3=22,...,26 empty."""

    counts: Counter[int] = Counter()
    maximum_m_3 = max(EMPTY_M3)
    for m_1 in range(1, S):
        m_2 = S - m_1
        for b_1 in range(10 ** (m_1 - 1), 10**m_1):
            for b_2 in range(10 ** (m_2 - 1), 10**m_2):
                Q = b_1 * 10**m_2 + b_2
                G = b_1 * b_2
                QG = Q * G
                qg_2 = valuation(QG, 2)
                qg_5 = valuation(QG, 5)
                for kappa in bounded_divisors(QG, maximum_m_3, 10 * QG):
                    if kappa <= QG:
                        continue
                    kappa_2 = valuation(kappa, 2)
                    kappa_5 = valuation(kappa, 5)
                    lower = max(
                        min(EMPTY_M3),
                        kappa_2 - qg_2,
                        kappa_5 - qg_5,
                    )
                    upper = min(
                        maximum_m_3,
                        2 * kappa_2 + valuation(kappa + 2 * G, 2),
                        2 * kappa_5 + valuation(kappa + 2 * G, 5),
                    )
                    for m_3 in range(lower, upper + 1):
                        counts[m_3] += 1
    assert all(counts[m_3] == 0 for m_3 in EMPTY_M3)
    print("m_3=22,...,26 primitive denominator-tail rows = 0")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--m3", type=int, choices=FINITE_M3)
    group.add_argument("--empty-high-only", action="store_true")
    parser.add_argument(
        "--unfiltered",
        action="store_true",
        help="disable optional Python prefilters for baseline cross-checks",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    check_quadratic_ranges()
    print("exact positive-quadratic interval solver: OK")
    if args.empty_high_only:
        if args.unfiltered:
            raise SystemExit("--unfiltered requires --m3")
        check_empty_high_tails()
        return
    if args.m3 is not None:
        check_one_slice(args.m3, use_prefilters=not args.unfiltered)
        return
    if args.unfiltered:
        raise SystemExit("--unfiltered requires --m3")
    for m_3 in FINITE_M3:
        check_one_slice(m_3)
    check_empty_high_tails()
    print("DD 27.28 S=4 boundary certificate: OK")


if __name__ == "__main__":
    main()
