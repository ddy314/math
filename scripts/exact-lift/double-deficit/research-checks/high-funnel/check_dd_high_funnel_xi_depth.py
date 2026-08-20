#!/usr/bin/env python3
"""Mechanical checks for high-funnel-xi-depth.md."""

from __future__ import annotations


def valuation_identities() -> None:
    # Enumerate finite high-funnel valuation tuples satisfying the exact 5-resonance.
    for m in range(1, 50):
        for q in range(0, 15):
            for g in range(0, 15):
                for n5 in range(0, 25):
                    num = 2 * m + 2 * q + g + n5
                    if num % 3:
                        continue
                    k = num // 3
                    if k <= g:
                        continue
                    B = m + q + g - k
                    if B < 0:
                        continue
                    assert 3 * B == m + q + 2 * g - n5

                    if B >= m:
                        assert 2 * m + n5 <= q + 2 * g
                        assert m <= 2 * q + g + n5
                    else:
                        x = 2 * k - 2 * m + B
                        assert 3 * x == 5 * q + 4 * g + n5 - m
                        assert x == 2 * q + 2 * g - B
                        assert x >= 0


def main() -> None:
    valuation_identities()
    print("DD high-funnel Xi-depth checks passed")


if __name__ == "__main__":
    main()
