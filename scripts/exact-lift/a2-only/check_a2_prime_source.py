#!/usr/bin/env python3
"""Exact finite checks for the A2 prime-source continuation.

This script certifies the purely finite modular statement in
`docs/proofs/exact-lift/branches/a2-only/prime-source.md`, §4.
It uses only Python integer arithmetic.
"""

P = 23


def legendre_symbol(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    x = pow(a, (p - 1) // 2, p)
    return 1 if x == 1 else -1


def multiplicative_order(a: int, p: int) -> int:
    x = 1
    for n in range(1, p):
        x = (x * a) % p
        if x == 1:
            return n
    raise AssertionError("order not found")


def main() -> None:
    assert multiplicative_order(10, P) == 22
    assert legendre_symbol(17, P) == -1

    allowed_exponents = []
    rows = []

    # t = 10^(M-1) mod 23.  Since ord_23(10)=22, it is enough to
    # inspect M-1 modulo 22.
    for exponent in range(22):
        t = pow(10, exponent, P)

        # From 2K == 9 (mod 23), K=10P_prefix and
        # P_prefix=9*10^(M-1)+a2:
        a2 = (20 - 9 * t) % P

        # From Q0 == 0 (mod 23) and the reflection source split:
        C0 = (2 * t) % P

        n0_direct = (C0 * C0 + a2 * a2) % P
        n0_poly = (16 * t * t + 8 * t + 9) % P
        assert n0_direct == n0_poly
        assert n0_poly != 0

        chi = legendre_symbol(n0_poly, P)
        if chi == -1:
            allowed_exponents.append(exponent)
        rows.append((exponent, t, a2, C0, n0_poly, chi))

    expected_exponents = [0, 1, 7, 8, 9, 11, 12, 14, 16, 18, 19, 21]
    assert allowed_exponents == expected_exponents

    allowed_M = sorted({(exponent + 1) % 22 for exponent in allowed_exponents})
    expected_M = [0, 1, 2, 8, 9, 10, 12, 13, 15, 17, 19, 20]
    assert allowed_M == expected_M

    print("ord_23(10) = 22")
    print("allowed (M-1) mod 22:", expected_exponents)
    print("allowed M mod 22:", expected_M)
    print("checked rows:")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
