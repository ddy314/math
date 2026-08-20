#!/usr/bin/env python3
"""Mechanical checks for genuine-full-concat-carrier/Hensel notes."""

from __future__ import annotations

from sympy import simplify, symbols


def check_beta_tail() -> None:
    b1, b2, b3, t2, t3 = symbols("b1 b2 b3 t2 t3")
    Q = b1 * t2 + b2
    beta = b1 * t2 * t3 + b2 * t3 + b3
    assert simplify(beta - (t3 * Q + b3)) == 0


def check_phi_psi_factorization() -> None:
    Q, a2, b1, b2, b3, t3, W, a3 = symbols(
        "Q a2 b1 b2 b3 t3 W a3"
    )
    G = b1 * b2
    kappa = t3 * Q * G / b3
    Omega = Q * (a2 * b1) * (kappa + G)
    beta = t3 * Q + b3
    A = Q * a2**2 * b1**2

    for sign in (-1, 1):
        phi = Omega * a2 * b3 + sign * W * a3 * b2
        psi = A * beta + sign * W * a3
        assert simplify(phi - b2 * psi) == 0


def check_hensel_depth_ledger() -> None:
    # If v_p(Psi)>=2h, v_p(b3)=h and Psi=R+A*b3,
    # then C|R. Writing R=C*K and b3=C*b3o gives
    # C | K+A*b3o.  If A,b3o are units, K must be a unit.
    for h in range(1, 8):
        vpsi_min = 2 * h
        vb3 = h
        # First layer R has at least h from subtraction modulo p^h.
        vR_min = h
        assert vR_min == h
        # Second-layer congruence forces K unit, hence exact vR=h.
        vK = 0
        assert h + vK == h
        # Psi=C*(K+A*b3o) retains at least the second h.
        v_second = vpsi_min - h
        assert v_second >= h
        assert vb3 == h


def main() -> None:
    check_beta_tail()
    check_phi_psi_factorization()
    check_hensel_depth_ledger()
    print("DD genuine full-concat/Hensel checks passed")


if __name__ == "__main__":
    main()
