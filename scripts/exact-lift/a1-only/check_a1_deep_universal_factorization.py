#!/usr/bin/env python3
"""Symbolic audit for deep-universal-factorization.md."""

import sympy as sp


def main() -> None:
    w, D, N, g, T, lam, t = sp.symbols("w D N g T lam t")
    C0 = w * (10*w - 1)
    c2 = 10 * (1 - 20*w)
    u0 = 10 * lam * g * (20*w - 1)
    u = u0 + t

    q = (
        C0*lam*D**2*N**2
        - D*u*T*N
        + 1000*lam*g**2*T**2
        + g*u
        + c2*lam*g**2
    )

    factor_form = (
        lam
        * (w*D*N - 10*g*T)
        * ((10*w - 1)*D*N - 100*g*T)
        - lam*t*(D*T*N - g)
    )

    assert sp.expand(q - factor_form) == 0

    print("A1 universal deep factorization symbolic audit OK")


if __name__ == "__main__":
    main()
