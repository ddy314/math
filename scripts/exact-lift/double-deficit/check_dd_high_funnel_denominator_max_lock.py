#!/usr/bin/env python3
"""Mechanical valuation checks for high-funnel-denominator-max-lock.md."""

from __future__ import annotations


def finite_ledger() -> None:
    # Enumerate abstract high-funnel valuations satisfying exact resonance.
    for m in range(1, 60):
        for q in range(0, 15):
            for g in range(0, 15):
                for n5 in range(0, 20):
                    num = m + q + 2 * g - n5
                    if num % 3:
                        continue
                    B = num // 3
                    if B < 0 or B >= m:
                        continue
                    D = m + 2 * q + 2 * g - 2 * B

                    # b3-max branch formula from sphere balance.
                    # Require D = 2(B-g)+n5 and solve locks.
                    if D != 2 * (B - g) + n5:
                        continue
                    assert B == q + 2 * g
                    assert m == 2 * q + 4 * g + n5
                    assert D == m - 2 * g

                    k = m + q + g - B
                    T = k - g
                    assert T == m - 2 * g
                    assert D == T

                    x = (5 * q + 4 * g + n5 - m)
                    assert x % 3 == 0
                    assert x // 3 == q


def nonmax_implies_six() -> None:
    # If D<=n5 and 3D=m+4q+2g+2n5, then A5=2q+g+n5>=m.
    for m in range(1, 40):
        for q in range(0, 10):
            for g in range(0, 10):
                for n5 in range(0, 20):
                    rhs = m + 4 * q + 2 * g + 2 * n5
                    if rhs % 3:
                        continue
                    D = rhs // 3
                    if D <= n5:
                        assert 2 * q + g + n5 >= m


def main() -> None:
    finite_ledger()
    nonmax_implies_six()
    print("DD high-funnel denominator-max lock checks passed")


if __name__ == "__main__":
    main()
