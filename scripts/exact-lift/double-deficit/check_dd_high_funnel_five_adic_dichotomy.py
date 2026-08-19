#!/usr/bin/env python3
"""Mechanical algebra for high-funnel-five-adic-dichotomy.md.

Checks exact linear identities between the valuation variables and the two
branches of the dichotomy.  It is not a global DD emptiness proof.
"""

from __future__ import annotations


def check_grid() -> None:
    # Variables are nonnegative integer valuations satisfying:
    # k = m+q+g-B,  3k=2m+2q+g+n, and k>g.
    for m in range(1, 40):
        for q in range(0, 12):
            for g in range(0, 12):
                for n in range(0, 20):
                    numer = 2 * m + 2 * q + g + n
                    if numer % 3:
                        continue
                    k = numer // 3
                    if k <= g:
                        continue
                    B = m + q + g - k
                    if B < 0:
                        continue

                    assert 3 * B == m + q + 2 * g - n

                    r = 2 * k + g - m
                    assert 3 * r == m + 4 * q + 5 * g + 2 * n

                    defect_heavy = m <= 5 * q + 4 * g + n
                    deep_denominator = B > 2 * q + 2 * g
                    assert defect_heavy == (not deep_denominator)

                    if deep_denominator:
                        assert B < m
                        s_lower = m + g - B
                        assert s_lower - r == B - 2 * q - 2 * g
                        assert s_lower > r


def frontier_specialization() -> None:
    # In the old extremal frontier q,g,n=o(S), the tail-short branch becomes
    # 3d<=m+o(S).  Compare the leading constants.
    m = 2.808883577618
    d = 3.5
    assert 3 * d > m
    assert 3 * d - m > 7.6


def main() -> None:
    check_grid()
    frontier_specialization()
    print("DD high-funnel five-adic dichotomy checks passed")


if __name__ == "__main__":
    main()
