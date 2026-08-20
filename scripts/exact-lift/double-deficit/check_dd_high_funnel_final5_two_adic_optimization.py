#!/usr/bin/env python3
"""Mechanical algebra checks for high-funnel-final5-two-adic-optimization.md.

This checks the symbolic reductions and numerical constants.  The mathematical
sector coverage comes from the proof notes, not from finite enumeration here.
"""

from __future__ import annotations

import math
import sympy as sp


def symbolic_final5_reduction() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    M, Q5, G5, N5, Q2, N2, G2, R = sp.symbols(
        "M Q5 G5 N5 Q2 N2 G2 R", nonnegative=True
    )

    # Z-defect stability after using z=2-Gamma-aH.
    gamma_height = a * G2 + b * G5 + R
    H = 2 * M + 2 * Q2 + N2 - 2 * G2
    z = 2 - gamma_height - a * H
    expr = (
        6
        + 2 * b * M / 3
        - 2 * a * Q2
        - a * N2
        - 2 * b * (2 * Q5 + G5 + N5) / 3
        - z
    )

    # Final-5: M=2Q5+4G5+N5.
    g5_sol = (M - 2 * Q5 - N5) / 4
    reduced = sp.factor(sp.expand(expr.subs(G5, g5_sol)))
    expected = (
        4
        + (5 * a + 3) * M / 4
        - a * G2
        + R
        - 3 * b * Q5 / 2
        - 3 * b * N5 / 4
    )
    assert sp.simplify(reduced - expected) == 0


def short_closed_form() -> None:
    a = sp.symbols("a", positive=True)
    c = (5 * a + 3) / 4
    theta = 1 / (1 + a)
    # Convex combination: theta*Zstab + (1-theta)*2-short.
    m_coeff = sp.simplify(theta * c + (1 - theta) * 2)
    assert sp.simplify(m_coeff - (13 * a + 3) / (4 * (1 + a))) == 0

    after_budget_m = sp.simplify(m_coeff - 1)
    assert sp.simplify(after_budget_m - (9 * a - 1) / (4 * (1 + a))) == 0

    final = sp.simplify(
        7 / (1 + a)
        + 3 * (9 * a - 1) / (4 * (1 + a) ** 2)
    )
    target = 5 * (5 + 11 * a) / (4 * (1 + a) ** 2)
    assert sp.simplify(final - target) == 0


def balanced_closed_form() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    M, Q5, N5, Q2, N2, R = sp.symbols(
        "M Q5 N5 Q2 N2 R", nonnegative=True
    )
    c = (5 * a + 3) / 4
    G2 = (M + Q2) / 2
    zstab = 4 + c * M - a * G2 + R - 3 * b * Q5 / 2 - 3 * b * N5 / 4
    reduced = sp.expand(zstab)
    expected = (
        4
        + 3 * (1 + a) * M / 4
        - a * Q2 / 2
        + R
        - 3 * b * Q5 / 2
        - 3 * b * N5 / 4
    )
    assert sp.simplify(reduced - expected) == 0

    # Substitute R <= (3-(1+a)M-2aQ2-aN2)/2.
    with_budget = sp.expand(
        expected.subs(R, (3 - (1 + a) * M - 2 * a * Q2 - a * N2) / 2)
    )
    target = (
        sp.Rational(11, 2)
        + (1 + a) * M / 4
        - 3 * a * Q2 / 2
        - a * N2 / 2
        - 3 * b * Q5 / 2
        - 3 * b * N5 / 4
    )
    assert sp.simplify(with_budget - target) == 0


def numerical_constants() -> None:
    a = math.log10(2)
    short = 5 * (5 + 11 * a) / (4 * (1 + a) ** 2)
    balanced = 25 / 4
    assert abs(short - 6.137703685012176) < 1e-12
    assert abs(balanced - 6.25) < 1e-15
    assert short < 6.215109404735
    assert balanced < 6.308883577618


def main() -> None:
    symbolic_final5_reduction()
    short_closed_form()
    balanced_closed_form()
    numerical_constants()
    print("DD Final-5 Z-enhanced two-adic optimization checks passed")


if __name__ == "__main__":
    main()
