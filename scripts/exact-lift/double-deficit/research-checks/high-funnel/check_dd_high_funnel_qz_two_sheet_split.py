#!/usr/bin/env python3
"""Mechanical checks for high-funnel-qz-two-sheet-split.md.

This script checks only finite algebra / valuation ledgers.  It is not a
proof of the global DD branch.
"""

from __future__ import annotations

import sympy as sp


def symbolic_identities() -> None:
    a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3")
    T, S, D = sp.symbols("T S D")

    # T=10^m2, S=10^s2, D=10^d.
    Q = b1 * T + b2
    A12 = a1 * T * S + a2

    delta12 = D * (a1 * S * b2 - a2 * b1)
    delta13 = D * a1 * S * b3 - a3 * b1
    delta23 = D * a2 * b3 - a3 * b2
    E = b3 * A12 * D - a3 * Q

    assert sp.expand(E - (T * delta13 + delta23)) == 0
    assert sp.expand(delta12 / D - (Q * a1 * S - b1 * A12)) == 0
    assert sp.expand(b1 * delta23 - b2 * delta13 + b3 * delta12) == 0


def denominator_excess_ledger() -> None:
    # Abstract odd non-decimal p-adic ledger from the q-Z allocation theorem.
    # If e1!=e2 then v_p(Q)=min(e1,e2).  If e1=e2=M, cancellation may
    # raise v_p(Q)=r to any r>=M.  For p|D_qZ let d=min(r,z).
    for e1 in range(12):
        for e2 in range(12):
            rs = [min(e1, e2)] if e1 != e2 else range(e1, 12)
            for r in rs:
                gamma_depth = e1 + e2
                for z in range(1, 12):
                    d_qz = min(r, z)
                    e = max(d_qz - gamma_depth // 2, 0)
                    if e == 0:
                        continue

                    # Positive D_ex depth forces the unique third-exclusive
                    # pattern e1=e2=M<e3=r.
                    assert e1 == e2
                    M = e1
                    assert gamma_depth == 2 * M
                    assert r > M
                    c = r - M
                    assert e == d_qz - M
                    assert 0 < e <= c
                    assert z >= M + e

                    # Sharpened payer exponent: gamma pays 2M and either
                    # gap a or Z0^2 pays at least 2e.
                    assert 2 * d_qz <= gamma_depth + 2 * e


def sheet_valuation_model() -> None:
    # Pure valuation consequences used by the two sheets.
    for M in range(0, 8):
        for c in range(1, 8):
            r = M + c
            for e in range(1, c + 1):
                # Gap sheet:
                vE_gap = r + e
                vTheta_gap = 0
                assert vE_gap - r >= e
                assert vTheta_gap == 0

                # Complementary sheet:
                vE_comp = r
                vTheta_comp = e
                assert vE_comp - r == 0
                assert vTheta_comp >= e

                # Sphere/projective payer depths.
                va_gap = 2 * c
                vZ0_comp = c
                assert va_gap >= 2 * e
                assert vZ0_comp >= e


def main() -> None:
    symbolic_identities()
    denominator_excess_ledger()
    sheet_valuation_model()
    print("DD high-funnel q-Z two-sheet split checks passed")


if __name__ == "__main__":
    main()
