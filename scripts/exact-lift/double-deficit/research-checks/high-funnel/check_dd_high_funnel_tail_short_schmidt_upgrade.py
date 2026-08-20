#!/usr/bin/env python3
"""Mechanical checks for high-funnel-tail-short-schmidt-upgrade.md."""

from __future__ import annotations

import math
import sympy as sp


def dual_certificate() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    lam = 2 / (1 + a)
    mu = 4 * a / (3 * (1 + a))

    assert sp.simplify(lam * A - mu - sp.Rational(4, 3)) == 0
    assert sp.simplify(lam * b / 3 + mu - sp.Rational(2, 3)) == 0

    q_slack = sp.simplify(lam * 2 * b / 3 + 5 * mu - sp.Rational(4, 3))
    g_slack = sp.simplify(lam * 4 * b / 3 + 4 * mu - sp.Rational(5, 3))
    assert sp.simplify(q_slack - 4 * a / (1 + a)) == 0
    assert sp.simplify(g_slack - 1) == 0

    bound = sp.simplify(3 * lam)
    assert sp.simplify(bound - 6 / (1 + a)) == 0


def equality_geometry() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    M = 3 / (1 + a)
    N = M
    # At Q=G=0 and N=M both constraints saturate.
    assert sp.simplify(A * M + b * N / 3 - 3) == 0
    assert sp.simpl(-M + N) == 0
    objective = sp.simplify(sp.Rational(4, 3) * M + sp.Rational(2, 3) * N)
    assert sp.simplify(objective - 6 / (1 + a)) == 0


def numeric_constant() -> None:
    a = math.log10(2)
    bound = 6 / (1 + a)
    assert abs(bound - 4.611730721041445) < 1e-12
    assert bound < 5
    assert bound < 6
    assert bound < 6.215109404735


def branch_objective_sanity() -> None:
    # Finite rational ledger: if M>=5Q+4G+N then tail objective <=2M.
    for M in range(1, 30):
        for Q in range(0, 8):
            for G in range(0, 8):
                for N in range(0, 15):
                    if M < 5 * Q + 4 * G + N:
                        continue
                    lhs3 = 4 * M + 4 * Q + 5 * G + 2 * N
                    assert lhs3 <= 6 * M


def main() -> None:
    dual_certificate()
    equality_geometry()
    numeric_constant()
    branch_objective_sanity()
    print("DD Tail-short recovered-Schmidt upgrade checks passed")


if __name__ == "__main__":
    main()
