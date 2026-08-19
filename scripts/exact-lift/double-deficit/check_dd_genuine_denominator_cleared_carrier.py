#!/usr/bin/env python3
"""Mechanical checks for genuine-denominator-cleared-carrier.md."""

from __future__ import annotations

from sympy import simplify, symbols


def vp(n: int, p: int) -> int:
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def check_clear_identity() -> None:
    b2, b3, q, Omega, a2, a3, W = symbols(
        "b2 b3 q Omega a2 a3 W", nonzero=True
    )
    y2 = a2 * q / b2
    y3 = a3 * q / b3

    theta_minus = Omega * y2 - W * y3
    phi_minus = Omega * a2 * b3 - W * a3 * b2
    theta_plus = Omega * y2 + W * y3
    phi_plus = Omega * a2 * b3 + W * a3 * b2

    assert simplify(b2 * b3 * theta_minus - q * phi_minus) == 0
    assert simplify(b2 * b3 * theta_plus - q * phi_plus) == 0


def check_cube_depth_ledger() -> None:
    # v_p(b2)=v_p(b3)=v_p(q)=h and v_p(theta)>=2h imply
    # v_p(phi)>=3h from b2*b3*theta=q*phi.
    for h in range(1, 8):
        vb2 = vb3 = vq = h
        for vtheta in range(2 * h, 4 * h + 1):
            vphi = vb2 + vb3 + vtheta - vq
            assert vphi >= 3 * h
            assert vphi - h >= 2 * h


def check_digit_expansion() -> None:
    Q, a2, b1, b3, kappa, G, W, a3, b2 = symbols(
        "Q a2 b1 b3 kappa G W a3 b2"
    )
    Omega = Q * (a2 * b1) * (kappa + G)
    phi_minus = Omega * a2 * b3 - W * a3 * b2
    phi_plus = Omega * a2 * b3 + W * a3 * b2

    expected_minus = Q * a2**2 * b1 * b3 * (kappa + G) - W * a3 * b2
    expected_plus = Q * a2**2 * b1 * b3 * (kappa + G) + W * a3 * b2
    assert simplify(phi_minus - expected_minus) == 0
    assert simplify(phi_plus - expected_plus) == 0


def main() -> None:
    check_clear_identity()
    check_cube_depth_ledger()
    check_digit_expansion()
    print("DD genuine denominator-cleared carrier checks passed")


if __name__ == "__main__":
    main()
