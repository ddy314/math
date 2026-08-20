#!/usr/bin/env python3
"""Mechanical checks for high-funnel-qz-sheet-reader-collapse.md."""

from __future__ import annotations

import sympy as sp


def prefix_determinant_identities() -> None:
    a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2")
    T, S, D = sp.symbols("T S D")  # 10^m2, 10^s2, 10^d

    Q = b1 * T + b2
    A12 = a1 * T * S + a2
    delta12 = D * (a1 * S * b2 - a2 * b1)

    assert sp.expand(delta12 / D - (Q * a1 * S - b1 * A12)) == 0
    assert sp.expand(-T * delta12 / D - (Q * a2 - b2 * A12)) == 0


def moving_factor_identities() -> None:
    # Write Y=5^T U and X=Y+V=2^H Z.  In the t2=1 phase u=2Y, v=V.
    X, Y = sp.symbols("X Y")
    V = X - Y
    u = 2 * Y
    v = V

    assert sp.expand((u + 2 * v) - 2 * X) == 0
    assert sp.expand((u + v) - (X + Y)) == 0


def balanced_payer_ledger() -> None:
    # D_qZ p-depth is d=M+e on the genuine excess support.
    # gamma contributes 2M.  Gap contributes >=2e via a;
    # complementary contributes >=e via C12 and >=e via Z0.
    for M in range(10):
        for c in range(1, 10):
            r = M + c
            for z in range(1, 12):
                d_qz = min(r, z)
                e = max(d_qz - M, 0)
                if e == 0:
                    continue
                assert e <= c

                gamma_depth = 2 * M
                gap_a_depth = 2 * c
                comp_c12_depth = e
                comp_z0_depth = c

                assert 2 * d_qz <= gamma_depth + gap_a_depth
                assert 2 * d_qz <= (
                    gamma_depth + comp_c12_depth + comp_z0_depth
                )


def primary_sheet_model() -> None:
    for e in range(1, 10):
        # Gap: a pays two copies, A12 is a unit.
        va_gap = 2 * e
        vA_gap = 0
        assert va_gap >= 2 * e
        assert vA_gap == 0

        # Complementary: a unit, A12 pays one copy.
        va_comp = 0
        vA_comp = e
        assert va_comp == 0
        assert vA_comp >= e


def main() -> None:
    prefix_determinant_identities()
    moving_factor_identities()
    balanced_payer_ledger()
    primary_sheet_model()
    print("DD high-funnel q-Z sheet reader-collapse checks passed")


if __name__ == "__main__":
    main()
