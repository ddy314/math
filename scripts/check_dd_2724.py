"""Finite certificate for n_3 = 8S_12-1 at S_12 = 2 and 3.

Section 27.23 proves that the whole boundary is dominant and has S_12 <= 17.
This script closes its two smallest sizes by reusing the exact denominator-tail,
p-adic-state, overflow-safe squarefree-gap, and discriminant machinery from
Section 27.22.  It does not cover 4 <= S_12 <= 17.
"""

from __future__ import annotations

from collections import Counter

from check_dd_2722 import (
    PrefixCounts,
    check_dominant_prefixes,
    check_product_comparison,
    position,
    state_signature,
    tail_kernel,
)


EXPECTED = {
    2: {
        "dominant": 2665,
        "positions": {
            "b3-unique": 2422,
            "prefix-or-tie": 155,
            "all-odd": 88,
        },
        "eligible": 1929,
        "denominator_pairs": 74,
        "prefix_counts": PrefixCounts(
            digit_pairs=1_924_074,
            coprime_pairs=817_860,
            squarefree_pairs=983_949,
            valuation_tail_pairs=24_396,
            nonnegative_discriminants=24_396,
            square_discriminants=0,
        ),
    },
    3: {
        "dominant": 126669,
        "positions": {
            "b3-unique": 119948,
            "prefix-or-tie": 4766,
            "all-odd": 1955,
        },
        "eligible": 108434,
        "denominator_pairs": 1619,
        "prefix_counts": PrefixCounts(
            digit_pairs=566_651_619,
            coprime_pairs=228_937_308,
            squarefree_pairs=275_830_547,
            valuation_tail_pairs=1_582_338,
            nonnegative_discriminants=1_582_338,
            square_discriminants=0,
        ),
    },
}


def check_slice(S: int) -> None:
    n_3 = 8 * S - 1
    all_tails = tail_kernel(S, range(1, 6 * S + 4))
    nondominant = [tail for tail in all_tails if tail.m_3 >= n_3 - S]
    dominant = [tail for tail in all_tails if tail.m_3 >= n_3 - 5 * S]
    positions = Counter(position(tail) for tail in dominant)
    eligible = [
        tail
        for tail in dominant
        if state_signature(tail, S, n_3) != ("impossible",)
    ]
    denominator_pairs = len(
        {(tail.m_1, tail.m_2, tail.b_1, tail.b_2) for tail in eligible}
    )

    expected = EXPECTED[S]
    assert nondominant == []
    assert len(dominant) == expected["dominant"]
    assert dict(positions) == expected["positions"]
    assert len(eligible) == expected["eligible"]
    assert denominator_pairs == expected["denominator_pairs"]

    prefix_counts, squares = check_dominant_prefixes(S, dominant, n_3)
    assert prefix_counts == expected["prefix_counts"]
    assert squares == []
    print(
        f"S={S}: non-dominant=0, dominant={len(dominant)}, "
        f"eligible={len(eligible)}, "
        f"valuation-discriminants={prefix_counts.valuation_tail_pairs}, "
        "squares=0"
    )


def main() -> None:
    check_product_comparison()
    print("exact limb product comparison: OK")
    check_slice(2)
    check_slice(3)
    print("DD 27.24 small 8S-1 certificate: OK")


if __name__ == "__main__":
    main()
