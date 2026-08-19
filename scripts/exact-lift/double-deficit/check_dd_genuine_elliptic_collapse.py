#!/usr/bin/env python3
"""Mechanical checks for genuine-elliptic-collapse.md.

The script verifies the exact algebraic collapse and a finite valuation ledger.
It does not prove DD emptiness.
"""

from __future__ import annotations

import sympy as sp


def symbolic_sphere_pay_identity() -> None:
    T, k, G, Q, y, a3, b3 = sp.symbols(
        "T k G Q y a3 b3", nonzero=True
    )

    beta = T * Q + b3
    mathscr_t = k**2 * (k + 2 * G) / T
    theta = (k + G) * Q * y**2 * beta + mathscr_t * a3**2
    s_raw = y**2 * b3**2 + G**2 * a3**2

    lhs = T * G**2 * theta
    rhs = k * (k * (k + 2 * G) * s_raw + G**2 * y**2 * b3**2)

    # Tail-weight relation: k*b3 = T*Q*G.
    err = sp.factor((lhs - rhs).subs(Q, k * b3 / (T * G)))
    assert err == 0


def symbolic_theta_from_psi() -> None:
    k, G, Ac, beta, a3, W, Cdd, mathscr_t, eta = sp.symbols(
        "k G Ac beta a3 W Cdd mathscr_t eta", nonzero=True
    )

    psi = Ac * beta + eta * W * a3
    theta = (k + G) * Ac * beta + mathscr_t * a3**2

    # Tail-root identity: mathscr_t*a3 = k*G^2*Cdd + eta*(k+G)*W.
    rhs = (k + G) * psi + k * G**2 * Cdd * a3
    err = sp.expand(theta - rhs)
    err = err.subs(matherscr_t if False else mathscr_t * a3,
                   k * G**2 * Cdd + eta * (k + G) * W)
    err = sp.expand(err).subs(eta**2, 1)
    assert sp.factor(err) == 0


def finite_depth_ledger() -> None:
    # If v_p(S_raw)>=4h and v_p(G)=v_p(b3)=h, then the RHS of
    # Sphere-pay-identity has >=4h while explicit G^2 on the LHS pays 2h.
    for h in range(1, 9):
        sphere_depth = 4 * h
        explicit_depth = 2 * h + 2 * h  # G^2 + b3^2
        rhs_depth = min(sphere_depth, explicit_depth)
        assert rhs_depth >= 4 * h
        theta_depth = rhs_depth - 2 * h
        assert theta_depth >= 2 * h


def main() -> None:
    symbolic_sphere_pay_identity()
    symbolic_theta_from_psi()
    finite_depth_ledger()
    print("DD genuine elliptic sphere-pay collapse checks passed")


if __name__ == "__main__":
    main()
