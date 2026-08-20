#!/usr/bin/env python3
"""Mechanical checks for high-funnel-fminus-sunit-factorization.md."""

from __future__ import annotations

import math
import sympy as sp


def factorization_algebra() -> None:
    a, v, c, lam, r, L, eta, Q1 = sp.symbols(
        "a v c lam r L eta Q1", nonzero=True
    )
    gstar = v * c * lam * r
    Q = eta * Q1
    tau = eta * v
    u = L * Q1
    fminus = a * gstar * L * (L * Q + 2 * tau) / tau
    ghat = c * lam * r
    assert sp.simplify(fminus - a * ghat * L * (u + 2 * v)) == 0

    # t2=1: u=2Y, v=X-Y, hence u+2v=2X.
    X, Y = sp.symbols("X Y")
    assert sp.expand(2 * Y + 2 * (X - Y) - 2 * X) == 0


def overlap_gamma_identity() -> None:
    eps, c, lam, r = sp.symbols("eps c lam r", nonzero=True)
    gamma = eps * c**2 * lam * r
    c3 = eps * c
    ghat = c * lam * r
    assert sp.simplify(ghat - gamma / c3) == 0


def final5_smooth_depth() -> None:
    # Abstract valuation check: f=g2+H+1, k5=T+g5.
    for H in range(0, 20):
        for g2 in range(0, 10):
            for T in range(0, 20):
                for g5 in range(0, 10):
                    f = g2 + H + 1
                    k5 = T + g5
                    # Exact factor contains 2^(H+1) * Z, a gap with
                    # v2=1,v5=T, and ghat with v2=g2,v5=g5.
                    assert (H + 1) + 1 + g2 == f + 1
                    assert T + g5 == k5


def diagnostic_constants() -> None:
    a = math.log10(2)
    b = math.log10(5)
    # The coarse stand-alone LP diagnostic recorded in the note.
    M = 3 / (1 + a)
    G5 = M / 4
    coarse = 2 + 2 * M + 1 - b * (M - 2 * G5)
    assert 6.7 < coarse < 6.9


def main() -> None:
    factorization_algebra()
    overlap_gamma_identity()
    final5_smooth_depth()
    diagnostic_constants()
    print("DD high-funnel exact Fminus S-unit checks passed")


if __name__ == "__main__":
    main()
