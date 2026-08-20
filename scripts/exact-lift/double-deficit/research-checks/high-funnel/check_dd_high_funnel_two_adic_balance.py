#!/usr/bin/env python3
"""Mechanical checks for high-funnel-two-adic-balance.md.

This is an algebra/valuation checker, not a proof assistant and not an
enumeration of Exact Lift candidates.
"""

from __future__ import annotations

import math


def shallow_gap_algebra() -> None:
    """Check the scale-free quadratic valuation cancellation identities."""
    for m in range(2, 18):
        for q in range(0, 7):
            ell = 1 if q == 0 else 0
            B = m + q - 1
            for g in range(0, min(B, 8) + 1):
                for n in range(0, 9):
                    R = 2 * (B - g) + n
                    if R < 2:
                        continue

                    # Test only the hypothetical deep orientation D_-=R-1>1.
                    Dminus = R - 1
                    if Dminus <= 1:
                        continue
                    A2 = Dminus - ell
                    if A2 < 0:
                        continue

                    V1 = 2 * q + n + 3 * ell - 3 + 2 * A2
                    V3 = 2 * q + n - 1 + ell
                    assert V1 - V3 == 2 * (Dminus - 1)
                    assert V1 > V3

                    # v2(A12) and d are arbitrary nonnegative / positive here.
                    for d in (1, 2, 5, 11):
                        for a12 in (0, 1, 4):
                            V2 = d - m + 1 + 2 * ell + 2 * g + a12 + A2
                            assert V2 - V3 == d + m - 1 + a12
                            assert V2 > V3


def tail_root_dichotomy_algebra() -> None:
    """Check the exact equality branch in the 2-adic tail-root ledger."""
    for m in range(2, 25):
        for q in range(0, 8):
            ell = 1 if q == 0 else 0
            for n in range(0, 10):
                for g in range(0, 16):
                    r2 = m + 2 * q + n + g - 1
                    A = 2 * m + 3 * q + n - 2 * g - 3
                    rhs_depth = g + ell + A
                    if rhs_depth == r2:
                        assert 2 * g == m + q + ell - 2

                    # Conversely, the balanced equation makes the two depths equal.
                    if 2 * g == m + q + ell - 2:
                        assert rhs_depth == r2


def uz_height_coefficients() -> None:
    """Check coefficient-by-coefficient expansion of U+Z height."""
    # Represent a linear form as coefficients of
    # (S,m,q2,n2,g2,q5,g5,n5,R0) plus an O(1) constant.
    # Start from 4S - 2 log(gamma) - a H - b T.
    a = math.log10(2.0)
    b = 1.0 - a

    # gamma = a*g2 + b*g5 + R0
    # H = 2m + 2q2 + n2 - 2g2 + O(1)
    # T = (2m + 2q5 - 2g5 + n5)/3
    coeff = {
        "S": 4.0,
        "m": -2.0 * a - 2.0 * b / 3.0,
        "q2": -2.0 * a,
        "n2": -a,
        "g2": -2.0 * a + 2.0 * a,
        "q5": -2.0 * b / 3.0,
        "g5": -2.0 * b + 2.0 * b / 3.0,
        "n5": -b / 3.0,
        "R0": -2.0,
    }

    assert abs(coeff["g2"]) < 1e-12
    assert abs(coeff["m"] + 2.0 * (1.0 + 2.0 * a) / 3.0) < 1e-12
    assert abs(coeff["g5"] + 4.0 * b / 3.0) < 1e-12

    # On Final-5, 2 q5 + 4 g5 + n5 = m.
    final_m_coeff = 2.0 * (1.0 + 2.0 * a) / 3.0 + b / 3.0
    assert abs(final_m_coeff - (1.0 + a)) < 1e-12


def sector_constants() -> None:
    a = math.log10(2.0)
    b = 1.0 - a

    final5 = 5.0 + 3.0 * b / (1.0 + a)
    final5_closed = (8.0 + 2.0 * a) / (1.0 + a)
    assert abs(final5 - final5_closed) < 1e-12
    assert abs(final5 - 6.611730721041445) < 1e-12

    balanced = 4.0 + 3.0 * (5.0 - 3.0 * a) / (4.0 * (1.0 + a))
    balanced_closed = (31.0 + 7.0 * a) / (4.0 * (1.0 + a))
    assert abs(balanced - balanced_closed) < 1e-12
    assert abs(balanced - 6.361730721041445) < 1e-12

    # These diagnostics are deliberately weaker than the already established
    # global strict limsup < 6.308883..., so the script must never advertise
    # them as global improvements.
    assert balanced > 6.308883577618
    assert final5 > balanced


def pure_common_shape() -> None:
    # m=4g5, T=2g5.  From b3=2^(m-1) 5^(m-T) qV,
    # log10(qV)=b*T+O(1); check coefficient identity only.
    a = math.log10(2.0)
    b = 1.0 - a
    for g5 in range(1, 20):
        m = 4 * g5
        T = 2 * g5
        assert m - T == 2 * g5
        assert abs(b * T - (b / 2.0) * m) < 1e-12


def main() -> None:
    shallow_gap_algebra()
    tail_root_dichotomy_algebra()
    uz_height_coefficients()
    sector_constants()
    pure_common_shape()
    print("DD high-funnel two-adic balance checks passed")


if __name__ == "__main__":
    main()
