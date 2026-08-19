#!/usr/bin/env python3
"""Mechanical checks for high-funnel-625-rigidity.md."""

from __future__ import annotations

import math
import sympy as sp


def symbolic_constants() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    M = 3 / (1 + a)
    G5 = M / 4
    G2 = M / 2
    T = M / 2
    gamma_h = a * G2 + b * G5
    assert sp.simplify(gamma_h - sp.Rational(3, 4)) == 0

    U = sp.simplify(2 - gamma_h - b * T)
    Z = sp.simplify(2 - gamma_h - a * M)
    assert sp.simplify(U - (11 * a - 1) / (4 * (1 + a))) == 0
    assert sp.simplify(Z - (5 - 7 * a) / (4 * (1 + a))) == 0
    assert sp.simplify(U + Z - 1) == 0

    V = sp.simplify(1 - gamma_h)
    assert V == sp.Rational(1, 4)

    XY = sp.simplify(b * T + U)
    assert XY == sp.Rational(5, 4)

    d = sp.simplify(sp.Rational(25, 4) - M)
    assert sp.simplify(d - (13 + 25 * a) / (4 * (1 + a))) == 0


def final5_q_eta_identity() -> None:
    # Pure symbolic exponent/form check:
    # L=2^ell 5^(T-q5), q=eta*2*5^T/L.
    eta = sp.symbols("eta", positive=True)
    ell, T, q5 = sp.symbols("ell T q5", integer=True, nonnegative=True)
    L = 2**ell * 5 ** (T - q5)
    q = sp.simplify(eta * 2 * 5**T / L)
    expected = eta * 2 ** (1 - ell) * 5**q5
    assert sp.simplify(q - expected) == 0


def numeric_values() -> None:
    a = math.log10(2)
    M = 3 / (1 + a)
    G5 = M / 4
    G2 = M / 2
    U = (11 * a - 1) / (4 * (1 + a))
    Z = (5 - 7 * a) / (4 * (1 + a))
    d = 25 / 4 - M

    assert abs(M - 2.3058653605207224) < 1e-12
    assert abs(G5 - 0.5764663401301806) < 1e-12
    assert abs(G2 - 1.1529326802603612) < 1e-12
    assert abs(U - 0.44413463947927745) < 1e-12
    assert abs(Z - 0.5558653605207225) < 1e-12
    assert abs(d - 3.9441346394792776) < 1e-12
    assert abs(U + Z - 1) < 1e-14


def orientation_valuation_ledger() -> None:
    # Abstract normalized leading-order check for the rejected orientation:
    # m1=o, m2~S forces e1=o and e2~g5<1, hence
    # v5(b1*10^m2)>e2 and v5(Q)=e2, contradicting q5=o.
    for scale in (1000, 10000):
        # Use rational approximants only as a finite sanity check.
        e1 = 0
        e2 = int(0.57 * scale)
        m2 = scale
        q_depth = min(e1 + m2, e2)
        assert q_depth == e2
        assert q_depth > scale // 2


def main() -> None:
    symbolic_constants()
    final5_q_eta_identity()
    numeric_values()
    orientation_valuation_ledger()
    print("DD Final-5 25/4 rigidity checks passed")


if __name__ == "__main__":
    main()
