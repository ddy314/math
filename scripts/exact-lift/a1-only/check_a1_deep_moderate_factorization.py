#!/usr/bin/env python3
"""Symbolic audit for deep-moderate-factorization.md.

Checks the normalized supply quadratic, its discriminant, the natural-square
rewriting, and the exact factor-pair identity.  This is an algebra audit, not a
finite-k search.
"""

import sympy as sp


def main() -> None:
    w, D, N, g, T, u, r = sp.symbols("w D N g T u r")
    C0 = w * (10*w - 1)
    c2 = 10 * (1 - 20*w)
    u0 = 10 * g * (20*w - 1)

    q = (
        C0 * D**2 * N**2
        - D*u*T*N
        + 1000*g**2*T**2
        + g*u
        + c2*g**2
    )

    disc = sp.factor(sp.discriminant(q, N) / D**2)
    expected = (
        T**2 * (u**2 - 4000*C0*g**2)
        - 4*C0*g*(u-u0)
    )
    assert sp.expand(disc - expected) == 0

    factored = (
        (w*D*N - 10*g*T)
        * ((10*w - 1)*D*N - 100*g*T)
        - D*r*(D*T*N - g)
    )
    assert sp.expand(q.subs(u, u0 + D*r) - factored) == 0

    # Natural square point.
    v0 = 10*g
    assert sp.expand(u0**2 - v0**2 - 4000*C0*g**2) == 0

    print("A1 moderate deep factorization symbolic audit OK")


if __name__ == "__main__":
    main()
