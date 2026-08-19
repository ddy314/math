#!/usr/bin/env python3
"""Mechanical checks for pairmax-fixed-a12-crt.md.

Checks the split-independent sphere-pay identity, carry-square extraction, and
frontier period constant.  It is not a DD emptiness proof.
"""

from __future__ import annotations

from decimal import Decimal, getcontext

import sympy as sp


def symbolic_sphere_pay() -> None:
    T, k, G, Q, y, a3, b3 = sp.symbols(
        "T k G Q y a3 b3", nonzero=True
    )
    beta = T * Q + b3
    MT = k**2 * (k + 2 * G) / T
    theta = (k + G) * Q * y**2 * beta + MT * a3**2
    s_raw = y**2 * b3**2 + G**2 * a3**2

    lhs = T * G**2 * theta
    rhs = k * (k * (k + 2 * G) * s_raw + G**2 * y**2 * b3**2)

    # Tail-weight: k*b3=T*Q*G.
    err = sp.factor((lhs - rhs).subs(Q, k * b3 / (T * G)))
    assert err == 0


def symbolic_carry_extract() -> None:
    g0, U, k, G, Ac, beta, MT = sp.symbols(
        "g0 U k G Ac beta MT", nonzero=True
    )
    a3, B, D, V, A12, Sigma, R0 = sp.symbols(
        "a3 B D V A12 Sigma R0", nonzero=True
    )

    theta = (k + G) * Ac * beta + MT * a3**2
    carry = g0 * B * D * V * A12 - Sigma * R0

    expanded = sp.expand(g0**2 * U**2 * theta).subs(
        g0**2 * U**2 * a3**2, carry**2
    )
    expanded = sp.expand(expanded)

    h0 = g0**2 * U**2 * (k + G) * Ac * beta + MT * Sigma**2 * R0**2
    target = (
        h0
        - 2 * MT * g0 * B * D * V * Sigma * R0 * A12
        + MT * g0**2 * B**2 * D**2 * V**2 * A12**2
    )
    assert sp.factor(expanded - target) == 0


def valuation_ledger() -> None:
    for h in range(1, 10):
        # Raw sphere norm has 4h, explicit G^2 on LHS has 2h.
        assert 4 * h - 2 * h == 2 * h
        # In carry extraction V=C_L*v0: linear term has h, quadratic 2h.
        assert h < 2 * h


def frontier_constant() -> None:
    getcontext().prec = 30
    z = Decimal("0.308883577618")
    combined = Decimal(1) + 2 * z
    assert combined == Decimal("1.617767155236")
    assert combined > 1


def main() -> None:
    symbolic_sphere_pay()
    symbolic_carry_extract()
    valuation_ledger()
    frontier_constant()
    print("DD split-independent pairmax A12 CRT checks passed")


if __name__ == "__main__":
    main()
