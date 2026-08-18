#!/usr/bin/env python3
"""Exact arithmetic checks for decimal-prefix-bridge.md."""

from math import isqrt


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    x = pow(a, (p - 1) // 2, p)
    return 1 if x == 1 else -1


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    p = 2
    while p <= isqrt(n):
        if n % p == 0:
            return False
        p += 1
    return True


def check_height_square() -> None:
    # Algebraic identity after substituting
    # b3/b2 = 5^d cQ/g, N0=5^(lambda-2d)XY,
    # H0^2-g^2 a3^2=5^lambda cQ^2 XY.
    for g in range(1, 8):
        for b2base in range(1, 6):
            b2 = g * b2base
            for d in range(0, 4):
                for cQ in range(1, 5):
                    b3 = b2base * (5**d) * cQ
                    for nu in range(0, 4):
                        lam = nu + 2 * d
                        for X in range(1, 5):
                            for Y in range(1, 5):
                                N0 = 5**nu * X * Y
                                rhs_prod = 5**lam * cQ * cQ * X * Y
                                for a3 in range(1, 5):
                                    Hsq = g * g * a3 * a3 + rhs_prod
                                    H0 = isqrt(Hsq)
                                    if H0 * H0 != Hsq:
                                        continue
                                    lhs = b3 * b3 * N0 + b2 * b2 * a3 * a3
                                    rhs = (b2 * H0 // g) ** 2
                                    assert lhs == rhs


def check_resultant_identities() -> None:
    for b2 in range(1, 12):
        for b3 in range(1, 12):
            for Q in range(1, 9):
                for T in range(1, 9):
                    for N0 in range(1, 12):
                        for a3 in range(-8, 9):
                            H = b3 * b3 * N0 + b2 * b2 * a3 * a3
                            D = 55 * T * T * Q * Q - 49 * b3 * b3
                            RN = 324 * Q * Q * N0 + 2695 * b2 * b2
                            rhs = (
                                324 * Q * Q * H
                                - 55 * b2 * b2 * D
                                + b2 * b2 * Q * Q * (55 * T - 18 * a3) * (55 * T + 18 * a3)
                            )
                            assert b3 * b3 * RN == rhs

    for b2 in range(1, 12):
        for Q in range(1, 9):
            for N0 in range(1, 12):
                for K in range(-20, 21):
                    psi = b2 * b2 * (K * K - 26) - Q * Q * N0
                    RN = 324 * Q * Q * N0 + 2695 * b2 * b2
                    assert 324 * psi + 2704 * b2 * b2 == b2 * b2 * (18 * K - 55) * (18 * K + 55) - RN
                    F = 5 * K * K - 36 * K + 55
                    assert 324 * F + 2695 == (18 * K - 55) * (90 * K - 373)
                    assert 324 * (K * K - 26) + 5399 == (18 * K - 55) * (18 * K + 55)


def check_5399_gate() -> None:
    assert is_prime_trial(5399)
    assert 5399 % 4 == 3
    assert 5399 % 5 == 4
    assert 5399 % 11 == 9
    assert legendre(55, 5399) == -1


def check_negative_square_class() -> None:
    # At the double-root first layer: Psi_f = -(26*b2/9)^2 mod p.
    # Verify for representative 3 mod 4 primes away from denominators.
    primes = (7, 19, 23, 31, 43, 47, 59, 67, 71, 79)
    for p in primes:
        if p in (3, 13):
            continue
        if p % 4 != 3:
            continue
        inv9 = pow(9, -1, p)
        for b2 in range(1, p):
            x = (26 * b2 * inv9) % p
            val = (-x * x) % p
            assert val != 0
            assert legendre(val, p) == -1


def main() -> None:
    check_height_square()
    check_resultant_identities()
    check_5399_gate()
    check_negative_square_class()
    print("A2 decimal-prefix bridge certificate: OK")


if __name__ == "__main__":
    main()
