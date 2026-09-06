#!/usr/bin/env python3
"""Mechanical audit for dd-global-sixfold-decimal-folding-source-lock-2026-09-06.md.

Checks the universal block-folding algebra for several k and the sixfold
least-residue mechanism on finite integer toys.  It does not prove DD emptiness
or any asymptotic statement by finite computation.
"""

from __future__ import annotations

from math import gcd

import sympy as sp


def check_symbolic_block_folding() -> None:
    b1, b2, t, u, w = sp.symbols("b1 b2 t u w")
    ql, A, H, b3, a3, v = sp.symbols("ql A H b3 a3 v")
    Q = b1 * t + b2

    for k in range(1, 9):
        alpha = A * (u * t) ** k * w + a3
        beta = Q * v + b3
        exact_error = ql * alpha - H * beta

        folded = (
            ql * A * (-b2) ** k * u**k * w
            - b1**k * (H * b3 - ql * a3)
        )

        # folded - b1^k*(exact lift error) must be a polynomial multiple of Q.
        diff = sp.expand(folded - b1**k * exact_error)
        quotient, remainder = sp.div(diff, Q, t)
        assert sp.expand(remainder) == 0
        assert sp.expand(diff - Q * quotient) == 0


def inv_mod(a: int, m: int) -> int:
    return pow(a, -1, m)


def check_sixfold_residue_toy() -> None:
    # Pure modular toy for the theorem.  S=m1+m2=2, n=13=6S+1.
    # Q=13 from b1*10^m2+b2 = 1*10+3.
    m1 = 1
    m2 = 1
    S = m1 + m2
    n = 13
    e = n - 6 * S
    assert e == 1

    b1 = 1
    b2 = 3
    Q = 13
    ql = 2
    A12 = 5

    # Pick D3 so that the sixfold congruence holds with 10^e=10.
    C6 = ql * A12 * b2**6 * 10 ** (6 * m1)
    D3 = (C6 * 10**e * inv_mod(b1**6, Q)) % Q

    assert gcd(C6, Q) == 1
    assert (C6 * 10**e - b1**6 * D3) % Q == 0

    rho = (b1**6 * D3 * inv_mod(C6, Q)) % Q
    assert 0 < 10**e < Q
    assert rho == 10**e


def check_height_margin() -> None:
    z_star = 0.308883577618031
    U_star = 1 - z_star
    assert U_star > 0
    # If log10 X/S -> 1 and e/S <= z_star+o(1), the leading gap is U_star.
    assert abs(U_star - 0.691116422381969) < 1e-12


def main() -> None:
    check_symbolic_block_folding()
    check_sixfold_residue_toy()
    check_height_margin()
    print("DD global sixfold decimal folding/source-lock checks passed")


if __name__ == "__main__":
    main()
