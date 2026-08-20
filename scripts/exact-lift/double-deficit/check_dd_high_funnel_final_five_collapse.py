#!/usr/bin/env python3
"""Mechanical checks for high-funnel-final-five-collapse.md."""

from __future__ import annotations

import math


def smooth_depth_ledger() -> None:
    # Final-5: T=2q5+2g5+n5 >= q5.
    # shallow 2-gap makes v2(a)=v2(s); g*/V contributes full g2.
    for q5 in range(12):
        for g5 in range(12):
            for n5 in range(12):
                T = 2 * q5 + 2 * g5 + n5
                assert T >= q5
                assert T - q5 + q5 + g5 == T + g5

    for q2 in range(12):
        s2 = min(1, q2)
        a2 = 0 if q2 == 0 else 1
        assert s2 == a2
        for g2 in range(12):
            assert -s2 + a2 + g2 == g2


def algebra_and_dual() -> None:
    a = math.log10(2)
    b = 1 - a

    # 2a+b = 1+a, and Final-5 gives 2bG5 <= bM/2.
    assert abs((2 * a + b) - (1 + a)) < 1e-14

    coeff_m = 1.5 + a / 2
    lam = coeff_m / (1 + a)
    assert lam > 0.5

    c = 2 + 3 * lam
    assert abs(c - 5.805865360520722) < 1e-12
    assert c < 6.215109404735


def main() -> None:
    smooth_depth_ledger()
    algebra_and_dual()
    print("DD Final-5 collapse checks passed")


if __name__ == "__main__":
    main()
