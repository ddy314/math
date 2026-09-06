#!/usr/bin/env python3
"""Mechanical audit for the circular-failure no-residual F_- continuation.

Checks only the local exponent bookkeeping and the final 7/8 constant.  The
asymptotic theorem itself is proved in the companion markdown file.
"""

from __future__ import annotations


def check_soft_escape() -> None:
    for E in range(0, 7):
        for j in range(0, 7):
            M = max(E, j)
            for t in range(0, 5):
                for alpha in range(0, 5):
                    for eN in range(1, 7):
                        if j > E:
                            for e3 in range(0, j - E + 1):
                                x = t + alpha + eN + e3
                                c = x + j + E
                                rE = max(c - M - t, 0)
                                assert rE == alpha + eN + e3 + E
                                assert rE >= eN
                        else:
                            e3 = 0
                            x = t + alpha + eN
                            c = x + 2 * j
                            rE = max(c - M - t, 0)
                            escape = eN - min(eN, rE)
                            assert escape <= max(E - 2 * j - alpha, 0)
                            assert escape <= E


def check_hard_coverage() -> None:
    for h in range(1, 8):
        for t in range(0, 5):
            for n0 in range(0, 5):
                for j in range(0, 5):
                    rE = h + t + n0 + j
                    assert h + n0 <= rE


def check_final_constant() -> None:
    # Circular failure gives 4 f >= 4 S-r, and r<=m2/2<=S/2.
    for S in range(1, 200):
        for m2 in range(1, S + 1):
            r_upper = m2 / 2
            f_lower = S - r_upper / 4
            assert f_lower >= 7 * S / 8


def main() -> None:
    check_soft_escape()
    check_hard_coverage()
    check_final_constant()
    print("DD circular failure no-residual Fminus checks passed")


if __name__ == "__main__":
    main()
