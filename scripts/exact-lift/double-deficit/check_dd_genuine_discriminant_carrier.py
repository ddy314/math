#!/usr/bin/env python3
"""Mechanical checks for genuine-discriminant-carrier.md.

The script verifies the exact polynomial identities and finite valuation logic
behind the new discriminant carrier.  It does not prove the frontier
asymptotics or DD emptiness.
"""

from __future__ import annotations

from sympy import I, simplify, symbols


def vp(n: int, p: int) -> int:
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def check_square_approx_identity() -> None:
    x, y, kappa, G = symbols("x y kappa G")
    N12 = x**2 + y**2
    lhs = N12 * kappa * (kappa + 2 * G) - y**2 * (kappa + G) ** 2
    rhs = x**2 * kappa * (kappa + 2 * G) - y**2 * G**2
    assert simplify(lhs - rhs) == 0


def check_disc_rearrangement() -> None:
    kappa, G, C, Q, N12 = symbols("kappa G C Q N12")
    W2 = kappa * (
        kappa * (G**2 * C**2 - Q**2 * N12) - 2 * G * Q**2 * N12
    )
    target = (kappa * G * C) ** 2 - Q**2 * N12 * kappa * (kappa + 2 * G)
    assert simplify(W2 - target) == 0


def check_cross_combinations() -> None:
    Omega, y2, y3, W = symbols("Omega y2 y3 W")
    same = Omega * (y2 + I * y3) - y3 * (W + I * Omega)
    opp = Omega * (y2 + I * y3) + y3 * (W - I * Omega)
    assert simplify(same - (Omega * y2 - W * y3)) == 0
    assert simplify(opp - (Omega * y2 + W * y3)) == 0


def check_local_divisibility_samples() -> None:
    """If p^h divides x and G, the square-approx error has p^(2h)."""

    for p in (3, 5, 7, 11, 13):
        for h in range(1, 4):
            ph = p**h
            x = ph * 2
            G = ph * 3
            y = 1
            kappa = 2
            if kappa % p == 0:
                kappa += 1
            err = x * x * kappa * (kappa + 2 * G) - y * y * G * G
            assert vp(err, p) >= 2 * h


def main() -> None:
    check_square_approx_identity()
    check_disc_rearrangement()
    check_cross_combinations()
    check_local_divisibility_samples()
    print("DD genuine discriminant-carrier checks passed")


if __name__ == "__main__":
    main()
