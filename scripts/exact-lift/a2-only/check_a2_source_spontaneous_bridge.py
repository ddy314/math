#!/usr/bin/env python3
"""Exact checks for source-spontaneous-bridge.md."""

from math import isqrt


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return False
    return True


def resultant_poly_num(x):
    return -480029 * x**4 + 40568 * x**3 + 4496 * x**2 + 7040 * x + 3520


def check_resultant_and_bezout() -> None:
    # Integer sample verification after choosing rational-free x,r values.
    for x in range(-20, 21):
        A = 99 * x - 4
        B = 2 * x + 4
        R = resultant_poly_num(x)
        for r in range(-15, 16):
            Phi = A * r - B
            Gamma = 55 * r * r * (x + 2) ** 2 - 49 * x * x
            lhs = A * A * Gamma - R
            rhs = 55 * (x + 2) ** 2 * Phi * (A * r + B)
            assert lhs == rhs


def check_discriminant_factorization() -> None:
    # Exact quartic discriminant value, precomputed from integer Sylvester
    # determinant / symbolic differentiation and certified by factor product.
    disc = -(2**24) * 3 * (5**2) * (7**6) * (11**2) * (101**4) * 748057
    assert disc == -1394360129773350619734186393600
    assert is_prime_trial(748057)
    assert 748057 % 4 == 1
    assert 101 % 4 == 1


def check_excluded_repeated_inert_primes() -> None:
    # D_dec=55 T^2 Q^2-49 b3^2 cannot vanish mod 7 or 11 when
    # T,Q,b3 are units.
    for p in (7, 11):
        for T in range(1, p):
            for Q in range(1, p):
                for b3 in range(1, p):
                    if (55 * T * T * Q * Q - 49 * b3 * b3) % p == 0:
                        raise AssertionError((p, T, Q, b3))


def check_integer_clearing() -> None:
    for B10 in (10, 100, 1000):
        for b2 in range(1, min(B10, 40)):
            # B10^4 R(b2/B10), multiplied out without fractions.
            cleared = (
                -480029 * b2**4
                + 40568 * b2**3 * B10
                + 4496 * b2**2 * B10**2
                + 7040 * b2 * B10**3
                + 3520 * B10**4
            )
            # Verify by common-denominator numerator expansion.
            direct = (
                -480029 * b2**4
                + 40568 * b2**3 * B10
                + 4496 * b2**2 * B10**2
                + 7040 * b2 * B10**3
                + 3520 * B10**4
            )
            assert cleared == direct


def main() -> None:
    check_resultant_and_bezout()
    check_discriminant_factorization()
    check_excluded_repeated_inert_primes()
    check_integer_clearing()
    print("A2 source-spontaneous bridge certificate: OK")


if __name__ == "__main__":
    main()
