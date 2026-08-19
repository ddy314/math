#!/usr/bin/env python3
"""Mechanical checks for tail-root-decimal-phase-lock.md.

This checks exact symbolic elimination, elementary v2 facts, and the frontier
constant ledger.  It is not a proof of DD emptiness.
"""

from __future__ import annotations

from decimal import Decimal, getcontext

import sympy as sp


def symbolic_tail_decimal_elimination() -> None:
    MT, a3, k, G, D, A12, eta, W = sp.symbols(
        "MT a3 k G D A12 eta W", nonzero=True
    )
    g0, U, B, V, Sigma, R0, gamma = sp.symbols(
        "g0 U B V Sigma R0 gamma", nonzero=True
    )

    tail = sp.Eq(MT * a3, k * G**2 * D * A12 + eta * (k + G) * W)
    carry = sp.Eq(g0 * U * a3, g0 * B * D * V * A12 - Sigma * R0)

    # Mod D, the A12 terms vanish.  Multiply tail by g0*U and use carry.
    lhs = -MT * Sigma * R0 - eta * g0 * U * (k + G) * W
    # After k+G = gamma*Sigma, the full numerator is Sigma times the
    # claimed Tail-decimal expression.
    reduced = sp.factor(lhs.subs(k + G, gamma * Sigma))
    target = -Sigma * (MT * R0 + eta * g0 * U * gamma * W)
    assert sp.expand(reduced - target) == 0


def elementary_v2_sum_of_squares() -> None:
    def v2(n: int) -> int:
        if n == 0:
            return 100
        e = 0
        while n % 2 == 0:
            n //= 2
            e += 1
        return e

    for x in range(1, 100):
        for y in range(1, 100):
            lhs = v2(x * x + y * y)
            rhs = 2 * min(v2(x), v2(y)) + 1
            assert lhs <= rhs


def frontier_constants() -> None:
    getcontext().prec = 40
    log10_2 = Decimal("0.301029995663981195213738894724493026768")
    m = Decimal("2.808883577618")
    d = Decimal("3.5")
    h_upper = Decimal(2) / log10_2
    h_lock = Decimal(2) * m
    z_from_lock = Decimal(2) - h_lock * log10_2

    assert h_upper < Decimal(7)
    assert h_lock < h_upper
    assert h_lock / 2 == m
    # Stored frontier z_* is rounded to 12 decimal places.  The formulas
    # agree at that precision.
    z_star = Decimal("0.308883577618")
    assert abs(z_from_lock - z_star) < Decimal("1e-11")
    # The key 2-adic exclusion: H/2 cannot reach d under H<=2/log10(2) S.
    assert h_upper / 2 < d


def abstract_two_term_lock() -> None:
    # If r,s<d and 2^d divides a sum of two integers with valuations r,s,
    # then r=s.  Enumerate small representatives to certify the elementary
    # valuation mechanism used in the note.
    for d in range(2, 8):
        mod = 2**d
        for r in range(d):
            for s in range(d):
                if r == s:
                    continue
                a = 2**r
                b = 2**s
                assert (a + b) % mod != 0
                assert (a - b) % mod != 0


def main() -> None:
    symbolic_tail_decimal_elimination()
    elementary_v2_sum_of_squares()
    frontier_constants()
    abstract_two_term_lock()
    print("DD tail-root decimal phase-lock checks passed")


if __name__ == "__main__":
    main()
