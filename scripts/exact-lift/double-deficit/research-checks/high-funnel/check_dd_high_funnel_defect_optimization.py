#!/usr/bin/env python3
"""Mechanical checks for high-funnel-defect-optimization.md."""

from __future__ import annotations

import sympy as sp


def symbolic_stability() -> None:
    a, b, m, S = sp.symbols("a b m S", positive=True)
    q2, n2, A5, n = sp.symbols("q2 n2 A5 n", nonnegative=True)

    lower = (2 * a + 4 * b / 3) * m - 2 * S - 1 - a + 2 * a * q2 + a * n2 + 2 * b * A5 / 3
    upper = 4 * S + 2 * m - n + 4 + a

    # lower < upper => n < target
    target = 6 * S + 2 * b * m / 3 - 2 * a * q2 - a * n2 - 2 * b * A5 / 3 + 5 + 2 * a
    expr = sp.expand((upper - lower).subs(b, 1 - a))
    assert sp.factor(expr - (target - n)) == 0


def dual_certificate() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    lam = 7 / (5 * a + 3)
    mu = 2 * (4 * a + 1) / (3 * (5 * a + 3))

    # Combined constraint coefficients: A*M + b/3*(2Q+G+N) <= 4
    # Branch closure: -M+5Q+4G+N <= 0
    coeff_M = sp.simplify(lam * A - mu)
    coeff_Q = sp.simplify(lam * (2 * b / 3) + 5 * mu)
    coeff_G = sp.simplify(lam * (b / 3) + 4 * mu)
    coeff_N = sp.simplify(lam * (b / 3) + mu)

    assert sp.simplify(coeff_M - sp.Rational(4, 3)) == 0
    assert sp.simplify(coeff_G - sp.Rational(5, 3)) == 0

    extra_Q = sp.factor(coeff_Q - sp.Rational(4, 3))
    extra_N = sp.factor(coeff_N - sp.Rational(2, 3))
    assert sp.simplify(extra_Q - 2 * (a + 2) / (5 * a + 3)) == 0
    assert sp.simplify(extra_N - (1 - 3 * a) / (5 * a + 3)) == 0


def numerical_constant() -> None:
    import math

    a = math.log10(2)
    bound = 28 / (3 + 5 * a)
    assert abs(bound - 6.215109404735) < 2e-12
    assert a < 1 / 3
    assert bound < 6.308883577618


def main() -> None:
    symbolic_stability()
    dual_certificate()
    numerical_constant()
    print("DD high-funnel defect optimization checks passed")


if __name__ == "__main__":
    main()
