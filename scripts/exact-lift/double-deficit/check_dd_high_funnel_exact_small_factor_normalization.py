#!/usr/bin/env python3
"""Mechanical checks for high-funnel-exact-small-factor-normalization.md.

This script is a ledger/algebra checker, not a proof searcher.
"""

from __future__ import annotations

import sympy as sp


def symbolic_checks() -> None:
    r0, s, U, qred, V, X = sp.symbols(
        "r0 s U qred V X", nonzero=True
    )
    a_gap, gstar = sp.symbols("a_gap gstar", nonzero=True)

    q = s * qred
    L = r0 / s
    tau = qred * V
    Q = U * q

    # In the t2=1 phase: X = 5^T U + V = r0*U/2 + V,
    # since r0=2*5^T.
    X_phase = r0 * U / 2 + V

    # Tail reduction gives the exact simplification of LQ+2 tau.
    assert sp.simplify(L * Q + 2 * tau - 2 * qred * X_phase) == 0

    # Section 35 small-factor factorization.
    F35 = a_gap * gstar * L * (L * Q + 2 * tau) / tau
    target = 2 * a_gap * gstar * L * X_phase / V
    assert sp.simplify(F35 - target) == 0

    # Replacing L=r0/s gives the normalized quotient a*(g*/V).
    target2 = 2 * r0 * X_phase / s * a_gap * gstar / V
    assert sp.simplify(F35 - target2) == 0


def smooth_gcd_ledger() -> None:
    # r0 = 2 * 5^T.  q may share some 2/5 depth with r0.
    # After s=(r0,q), reduced r=r0/s and q_red=q/s are coprime.
    for T in range(0, 20):
        for q2 in range(0, 8):
            for q5 in range(0, 25):
                s2 = min(1, q2)
                s5 = min(T, q5)

                r2 = 1 - s2
                r5 = T - s5
                qr2 = q2 - s2
                qr5 = q5 - s5

                assert min(r2, qr2) == 0
                assert min(r5, qr5) == 0
                assert s2 <= 1
                assert s5 <= T


def final_five_consistency() -> None:
    # On Final-5-lock:
    #   m=2 q5+4 g5+n5,
    #   T=m-2g5,
    #   v5(a)=q5,
    # and b3 is the 5-adic maximum, so v5(g*/V)=g5.
    # The exact factorization must reproduce v5(F_-)=k5=m-g5.
    for q5 in range(0, 20):
        for g5 in range(0, 20):
            for n5 in range(0, 20):
                m = 2 * q5 + 4 * g5 + n5
                T = m - 2 * g5
                k5 = m - g5

                assert T >= q5
                s5 = min(T, q5)
                v5_R = q5 + g5
                v5_F = (T - s5) + v5_R
                assert v5_F == k5


def main() -> None:
    symbolic_checks()
    smooth_gcd_ledger()
    final_five_consistency()
    print("DD exact small-factor normalization checks passed")


if __name__ == "__main__":
    main()
