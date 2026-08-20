#!/usr/bin/env python3
"""Mechanical checks for tail-root-kappa-plus-g-crt-nogo.md."""

from __future__ import annotations

import sympy as sp


def symbolic_coefficient_collapse() -> None:
    gamma, F, U, V, B, T3 = sp.symbols(
        "gamma F U V B T3", nonzero=True
    )
    k = 2 * gamma * F * U
    G = gamma * V
    MT = k**2 * (k + 2 * G) / T3

    expr = MT * B * V - U * k * G**2
    expr = sp.factor(expr.subs(B, T3 / (2 * F)))
    target = U * k * G * (k + G)
    assert sp.factor(expr - target) == 0


def symbolic_sunit_factors() -> None:
    gamma, F, U, V = sp.symbols("gamma F U V", nonzero=True)
    k = 2 * gamma * F * U
    G = gamma * V
    Sigma = V + 2 * F * U
    X = V + F * U

    assert sp.expand(k + G - gamma * Sigma) == 0
    assert sp.expand(k + 2 * G - 2 * gamma * X) == 0


def candidate_congruence_loses_a12() -> None:
    g0, D, U, k, G, A12, MT, Sigma, R0, eta, W = sp.symbols(
        "g0 D U k G A12 MT Sigma R0 eta W", nonzero=True
    )
    # After coefficient collapse the exact candidate has the form below.
    lhs = g0 * D * U * k * G * (k + G) * A12 - MT * Sigma * R0
    rhs = eta * g0 * U * (k + G) * W
    # Mod (k+G), both A12 and W terms vanish, leaving only MT*Sigma*R0.
    modulus = k + G
    lhs_mod = sp.rem(sp.Poly(lhs, A12), sp.Poly(modulus, A12)) if False else None
    # Symbolic modular statement is represented by direct factor removal:
    assert sp.factor(lhs - rhs + MT * Sigma * R0) == (
        U * g0 * (k + G) * (A12 * D * G * k - W * eta)
    )


def main() -> None:
    symbolic_coefficient_collapse()
    symbolic_sunit_factors()
    candidate_congruence_loses_a12()
    print("DD kappa-plus-G CRT collapse checks passed")


if __name__ == "__main__":
    main()
