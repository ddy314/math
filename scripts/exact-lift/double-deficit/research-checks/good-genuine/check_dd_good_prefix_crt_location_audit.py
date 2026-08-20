#!/usr/bin/env python3
"""Mechanical checks for good-prefix-crt-location-audit.md.

Only exact algebraic rearrangements are checked here.  The script does not
certify any asymptotic statement or DD emptiness.
"""

from __future__ import annotations

from sympy import I, simplify, symbols


def check_prefix_q_exact() -> None:
    g0, B, D, V, t, a1, a2 = symbols("g0 B D V t a1 a2")
    Sigma, U, a3, X, F, R0 = symbols("Sigma U a3 X F R0")
    q2L = symbols("q2L")

    # R0-A12 after A12=t*a1+a2.
    prefix_main = Sigma * R0 + g0 * U * a3 - g0 * B * D * V * a2
    H_Q = X * R0 - g0 * B * D * V * a2

    diff = simplify(prefix_main - H_Q)
    diff = simplify(diff.subs(Sigma, X + F * U))
    assert simplify(diff - U * (g0 * a3 + F * R0)) == 0
    assert simplify(diff.subs(g0 * a3 + F * R0, q2L) - U * q2L) == 0


def check_q_parent_equivalence() -> None:
    g0, B, D, V, A12 = symbols("g0 B D V A12")
    Sigma, U, a3, X, F, R0 = symbols("Sigma U a3 X F R0")

    # QCRT-exact with q^2 L replaced by Source-a3.
    lhs = Sigma * (g0 * a3 + F * R0)
    rhs = g0 * (F * B * D * V * A12 + X * a3)
    reduced = simplify((lhs - rhs).subs(Sigma, X + F * U) / F)

    # This must be exactly the negative of R0-A12 residual.
    reconstruction = Sigma * R0 - g0 * (B * D * V * A12 - U * a3)
    reconstruction = simplify(reconstruction.subs(Sigma, X + F * U))
    assert simplify(reduced - reconstruction) == 0


def check_prefix_qg_compatibility() -> None:
    Gamma, HG, HQ = symbols("Gamma HG HQ")
    main = symbols("main")
    U, q2L = symbols("U q2L")

    # -i Gamma H_G is the same prefix main term as Q-side.
    rel_g = -I * Gamma * HG - main
    rel_q = main - HQ - U * q2L

    # Eliminating main gives the compatibility identity.
    combined = simplify(rel_g + rel_q)
    assert simplify(combined - (-I * Gamma * HG - HQ - U * q2L)) == 0


def main() -> None:
    check_prefix_q_exact()
    check_q_parent_equivalence()
    check_prefix_qg_compatibility()
    print("DD Good prefix CRT location-audit checks passed")


if __name__ == "__main__":
    main()
