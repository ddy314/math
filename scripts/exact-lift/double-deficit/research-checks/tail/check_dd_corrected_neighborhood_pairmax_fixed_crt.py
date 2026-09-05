#!/usr/bin/env python3
"""Mechanical audits for dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md.

Checks exact algebra and the local valuation ledger after retaining the low
pair-max baseline r.  This is not a proof assistant and does not certify the
asymptotic DD hypotheses.
"""

from __future__ import annotations

from math import isclose
import sympy as sp


def check_generic_carry() -> None:
    L, omega, F5, V, D10, A12 = sp.symbols(
        "L omega F5 V D10 A12", nonzero=True
    )
    U, a3, Q1, w, a0, eps, Sigma = sp.symbols(
        "U a3 Q1 w a0 eps Sigma", nonzero=True
    )

    # B=L*omega/(2*F5), L*Q1=2*F5*U,
    # eps*w=Sigma, and V*omega*A12*D10-a3*Q1=w*a0.
    B = L * omega / (2 * F5)
    expr = B * V * D10 * A12 - U * a3
    expr = sp.expand(expr.subs(U, L * Q1 / (2 * F5)))
    expr = sp.factor(expr)

    target = L * (V * omega * D10 * A12 - a3 * Q1) / (2 * F5)
    assert sp.simplify(expr - target) == 0

    target2 = L * w * a0 / (2 * F5)
    assert sp.simplify(target.subs(V * omega * D10 * A12 - a3 * Q1, w * a0) - target2) == 0

    target3 = Sigma * L * a0 / (2 * F5 * eps)
    assert sp.simplify(target2.subs(w, Sigma / eps) - target3) == 0


def check_carry_square_expansion() -> None:
    g0, U, kappa, G, Ac, beta, MT = sp.symbols(
        "g0 U kappa G Ac beta MT", nonzero=True
    )
    a3, B, D10, V, A12, Sigma, R0 = sp.symbols(
        "a3 B D10 V A12 Sigma R0", nonzero=True
    )

    theta = (kappa + G) * Ac * beta + MT * a3**2
    carry = g0 * B * D10 * V * A12 - Sigma * R0
    lhs = sp.expand(g0**2 * U**2 * theta).subs(g0**2 * U**2 * a3**2, carry**2)
    lhs = sp.expand(lhs)

    constant = g0**2 * U**2 * (kappa + G) * Ac * beta + MT * Sigma**2 * R0**2
    rhs = (
        constant
        - 2 * MT * g0 * B * D10 * V * Sigma * R0 * A12
        + MT * g0**2 * B**2 * D10**2 * V**2 * A12**2
    )
    assert sp.factor(lhs - rhs) == 0


def check_pairmax_depth_ledger(bound: int = 20) -> None:
    states = 0
    for r in range(bound + 1):
        for h in range(1, bound + 1):
            # Exact/base valuations established in the proof.
            v_kappa = 2 * r
            v_kplusg = 2 * r
            v_kplus2g = 2 * r
            v_G = 2 * r + h
            v_Q = r
            v_y = r
            v_beta = r
            v_b3 = r + h
            v_Ac = v_Q + 2 * v_y
            v_MT = 2 * v_kappa + v_kplus2g
            v_Sraw = 4 * r + 4 * h

            # Sphere-pay RHS bracket terms.
            term1 = v_kappa + v_kplus2g + v_Sraw
            term2 = 2 * v_G + 2 * v_y + 2 * v_b3
            assert term1 >= 8 * r + 4 * h
            assert term2 == 8 * r + 4 * h

            rhs_depth = v_kappa + min(term1, term2)
            lhs_explicit = 2 * v_G
            theta_depth = rhs_depth - lhs_explicit
            assert theta_depth >= 6 * r + 2 * h

            # Both raw Theta summands have the common 6r baseline.
            assert v_kplusg + v_Ac + v_beta == 6 * r
            assert v_MT == 6 * r

            # Carry-square terms after the same baseline.
            linear = v_MT + h
            quadratic = v_MT + 2 * h
            assert linear == 6 * r + h
            assert quadratic == 6 * r + 2 * h

            # After dividing 6r, then one h, the linear coefficient is a unit
            # and the quadratic term still vanishes mod p^h.
            assert linear - 6 * r - h == 0
            assert quadratic - 6 * r - h >= h
            assert theta_depth - 6 * r - h >= h
            states += 1

    print(f"pair-max baseline states checked: {states}")


def check_capacity_constant() -> None:
    zstar = 0.308883577618031
    c_one = 2.335049992773302
    threshold = 2 * zstar / (2 + c_one)
    assert isclose(threshold, 0.1425051974639056, rel_tol=0, abs_tol=1e-15)
    print(f"fixed-fiber uniqueness threshold: {threshold:.15f}")


def main() -> None:
    check_generic_carry()
    check_carry_square_expansion()
    check_pairmax_depth_ledger()
    check_capacity_constant()
    print("DD corrected neighborhood pair-max fixed CRT audits passed")


if __name__ == "__main__":
    main()
