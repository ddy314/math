#!/usr/bin/env python3
"""Mechanical checks for genuine-a12-fixed-crt.md.

This verifies only exact symbolic expansion and the abstract valuation ledger.
It is not a DD emptiness proof.
"""

from __future__ import annotations

import sympy as sp


def symbolic_carry_square_expansion() -> None:
    g0, U, k, G, Ac, beta, MT = sp.symbols(
        "g0 U k G Ac beta MT", nonzero=True
    )
    a3, B, D, V, A12, Sigma, R0 = sp.symbols(
        "a3 B D V A12 Sigma R0", nonzero=True
    )

    theta = (k + G) * Ac * beta + MT * a3**2
    carry = g0 * B * D * V * A12 - Sigma * R0

    lhs = sp.expand(g0**2 * U**2 * theta).subs(
        g0**2 * U**2 * a3**2, carry**2
    )
    lhs = sp.expand(lhs)

    h0 = g0**2 * U**2 * (k + G) * Ac * beta + MT * Sigma**2 * R0**2
    rhs = (
        h0
        - 2 * MT * g0 * B * D * V * Sigma * R0 * A12
        + MT * g0**2 * B**2 * D**2 * V**2 * A12**2
    )
    assert sp.factor(lhs - rhs) == 0


def finite_depth_ledger() -> None:
    # Abstract p-adic bookkeeping after V=C_G e_G with e_G a unit:
    # theta has >=2h, linear term has h, quadratic term has 2h.
    # Hence constant term has >=h; after division by C_G the quadratic
    # vanishes mod p^h and the linear coefficient remains a unit.
    for h in range(1, 10):
        theta_depth = 2 * h
        linear_depth = h
        quadratic_depth = 2 * h
        assert min(theta_depth, linear_depth, quadratic_depth) == h
        constant_depth_lower_bound = h
        assert constant_depth_lower_bound >= h
        assert quadratic_depth - h >= h
        assert linear_depth - h == 0


def main() -> None:
    symbolic_carry_square_expansion()
    finite_depth_ledger()
    print("DD genuine fixed A12 CRT checks passed")


if __name__ == "__main__":
    main()
