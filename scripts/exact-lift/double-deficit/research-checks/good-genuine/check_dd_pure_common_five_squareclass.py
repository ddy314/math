#!/usr/bin/env python3
"""Mechanical checks for pure-common-five-squareclass-nogo.md."""

from __future__ import annotations

import math


def valuation_ledger() -> None:
    # Pure branch: m=4g, T=2g, B5=2g.
    for g in range(1, 20):
        m = 4 * g
        T = 2 * g
        omega = 2 * g
        L = m - omega
        r = g
        assert L == 2 * g

        # Cleared SFQ valuations.
        leading = L + 2 * r
        middle = L + 2 * r + 1 + 0 + 0 + 0  # omit d and omega for the moment
        constant = 0
        # After multiplying by omega^2:
        leading_cleared = leading
        constant_cleared = constant + 2 * omega
        assert leading_cleared == 4 * g
        assert constant_cleared == 4 * g

        for d in (1, 3, 9):
            middle_cleared = L + 2 * r + d + omega
            assert middle_cleared == d + 6 * g
            assert middle_cleared - 4 * g == d + 2 * g

        assert m - T == 2 * g


def unit_square_lifting() -> None:
    # For p=5, verify on small powers that a unit is a square mod 5^k
    # iff its mod-5 class is a square. This is only a finite sanity check;
    # the proof in the note is ordinary Hensel lifting.
    for k in range(1, 6):
        mod = 5**k
        squares = {x * x % mod for x in range(mod) if x % 5}
        for u in range(1, mod):
            if u % 5 == 0:
                continue
            mod5_square = (u % 5) in {1, 4}
            assert (u in squares) == mod5_square


def squareclass_substitution() -> None:
    # Check the formal non-square coefficient reduction:
    # -Q1/[L'(LQ1+2v)] -> -Q1^2/[2^(H+2) U Z]
    # using L'Q1=2U and LQ1+2v=2^(H+1)Z.
    # Numerical rational instances are enough to catch factor-of-two errors.
    from fractions import Fraction

    for Q1 in (1, 3, 7, 11):
        for U in (3, 9, 15):
            if 2 * U % Q1:
                continue
            Lp = Fraction(2 * U, Q1)
            for H in (1, 2, 5):
                for Z in (1, 3, 7):
                    lhs = -Fraction(Q1, 1) / (Lp * (2 ** (H + 1) * Z))
                    rhs = -Fraction(Q1 * Q1, (2 ** (H + 2)) * U * Z)
                    assert lhs == rhs


def main() -> None:
    valuation_ledger()
    unit_square_lifting()
    squareclass_substitution()
    print("DD pure-common five squareclass checks passed")


if __name__ == "__main__":
    main()
