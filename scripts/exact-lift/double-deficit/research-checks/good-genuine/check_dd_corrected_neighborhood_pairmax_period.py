#!/usr/bin/env python3
"""Mechanical checks for dd-corrected-neighborhood-pairmax-period-2026-08-22.md.

This script checks only symbolic identities, valuation bookkeeping, and the
reported numerical threshold.  It is not a DD emptiness proof.
"""

from __future__ import annotations

from decimal import Decimal, getcontext

import sympy as sp


def check_generic_carry() -> None:
    L, omega, V, A12, D10, a3, Q1, w, a0 = sp.symbols(
        "L omega V A12 D10 a3 Q1 w a0", nonzero=True
    )
    eps, Sigma, fiveT2 = sp.symbols(
        "eps Sigma fiveT2", nonzero=True
    )

    # fiveT2 abbreviates 2*5^T.  Use the exact canonical definitions
    # B=L*omega/fiveT2 and U=L*Q1/fiveT2.
    B = L * omega / fiveT2
    U = L * Q1 / fiveT2

    source_residual = V * omega * A12 * D10 - a3 * Q1 - w * a0
    carry_left = B * V * A12 * D10 - U * a3

    # Clearing fiveT2 shows that the carry identity is exactly the source
    # elimination multiplied by L.
    cleared = sp.factor(fiveT2 * carry_left - L * w * a0)
    assert sp.simplify(cleared - L * source_residual) == 0

    # With Sigma=eps*w, the R0/g0 parent is the same identity.
    sigma_parent = sp.expand(
        eps * fiveT2 * carry_left - Sigma * L * a0
    ).subs(Sigma, eps * w)
    assert sp.simplify(sigma_parent - eps * L * source_residual) == 0


def check_pairmax_depths() -> None:
    # r = common denominator baseline; h = moving pair-max excess.
    for r in range(0, 9):
        for h in range(1, 9):
            b1 = r
            b2 = r + h
            b3 = r + h
            qlcm = r + h
            Q = r
            V = h
            G = b1 + b2
            gamma = G - V
            kappa = gamma
            kplus = gamma
            kplus2 = gamma
            beta = r
            Ac = Q + 2 * b1
            Tcal = 2 * kappa + kplus2

            assert G == 2 * r + h
            assert gamma == 2 * r
            assert kappa == 2 * r
            assert kplus == 2 * r
            assert kplus2 == 2 * r
            assert beta == r
            assert Ac == 3 * r
            assert Tcal == 6 * r

            # Pair-max sphere supplies 2h beyond the explicit raw baseline.
            Sraw = 2 * b1 + 2 * (b2 + b3 - qlcm) + 2 * h
            assert Sraw == 4 * r + 4 * h

            bracket1 = kappa + kplus2 + Sraw
            bracket2 = 2 * G + 2 * b1 + 2 * b3
            assert bracket1 == 8 * r + 4 * h
            assert bracket2 == 8 * r + 4 * h

            rhs = kappa + min(bracket1, bracket2)
            lhs_explicit = 2 * G
            theta_lower = rhs - lhs_explicit
            assert theta_lower == 6 * r + 2 * h

            linear = Tcal + V
            quadratic = Tcal + 2 * V
            assert linear == 6 * r + h
            assert quadratic == 6 * r + 2 * h

            # After dividing by p^(6r+h), old r=0 shape reappears.
            assert theta_lower - (6 * r + h) >= h
            assert linear - (6 * r + h) == 0
            assert quadratic - (6 * r + h) == h


def check_threshold() -> None:
    getcontext().prec = 50
    a = Decimal(2).ln() / Decimal(10).ln()
    z_star = Decimal("0.308883577618031")
    c_one = Decimal(1) + Decimal(5) * (Decimal(1) + 2 * a) / Decimal(6)
    c_total = Decimal(2) + c_one
    delta_crt = 2 * z_star / c_total

    expected_c_one = Decimal("2.335049992773302")
    expected_delta = Decimal("0.142505197463905")

    assert abs(c_one - expected_c_one) < Decimal("1e-15")
    assert abs(delta_crt - expected_delta) < Decimal("1e-15")

    # At the threshold the normalized joint period equals 1.
    joint = Decimal(1) + 2 * z_star - c_total * delta_crt
    assert abs(joint - Decimal(1)) < Decimal("1e-45")


def main() -> None:
    check_generic_carry()
    check_pairmax_depths()
    check_threshold()
    print("DD corrected neighborhood pairmax period checks passed")


if __name__ == "__main__":
    main()
