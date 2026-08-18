#!/usr/bin/env python3
"""Exact arithmetic checks for docs/proofs/exact-lift/branches/a2-only/height-cofactor.md.

This is a certificate for fixed polynomial identities, binary-form rewrites,
resultant constants, and the residue table for the surviving f-height primes.
It is not a search for A2 solutions and not a global proof.
"""

from fractions import Fraction


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    x = pow(a, (p - 1) // 2, p)
    return 1 if x == 1 else -1


def f_w(k):
    return 5 * k * k - 36 * k + 55


def g_w(k):
    return 9 * k * k - 36 * k + 55


def check_polynomial_identities() -> None:
    for k in range(-100, 101):
        assert f_w(k) == (k - 5) * (5 * k - 11)
        assert g_w(k) == f_w(k) + 4 * k * k
        assert 4 * f_w(k) + 23 == (2 * k - 9) * (10 * k - 27)
        assert 4 * g_w(k) - 301 == (2 * k - 9) * (18 * k + 9)


def check_binary_forms() -> None:
    for t in range(1, 31):
        for a in range(-40, 41):
            k = Fraction(-a, t)
            lhs_q = t * t * f_w(k)
            rhs_q = (a + 5 * t) * (5 * a + 11 * t)
            assert lhs_q == rhs_q

            lhs_f = t * t * g_w(k)
            rhs_f = (3 * a + 6 * t) ** 2 + 19 * t * t
            assert lhs_f == rhs_f


def check_saturation_resultants() -> None:
    # On 2a+9T=0, the q/f binary forms become -23*T^2/4 and
    # 301*T^2/4 respectively.  Multiplying by 4 gives the exact
    # resultant constants because T is a unit at every odd carrier prime.
    for t in range(1, 50):
        a = Fraction(-9 * t, 2)
        h_q = (a + 5 * t) * (5 * a + 11 * t)
        h_f = (3 * a + 6 * t) ** 2 + 19 * t * t
        assert h_q == Fraction(-23 * t * t, 4)
        assert h_f == Fraction(301 * t * t, 4)

    assert 301 == 7 * 43
    assert 23 % (23 * 23) != 0
    assert 301 % (7 * 7) != 0
    assert 301 % (43 * 43) != 0


def check_external_discriminant() -> None:
    # B_W(K)=(5u^2+z^2)K^2-36u^2 K+55u^2 has discriminant
    # 4u^2(49u^2-55z^2).
    for u in range(1, 20):
        for z in range(-20, 21):
            a = 5 * u * u + z * z
            b = -36 * u * u
            c = 55 * u * u
            disc = b * b - 4 * a * c
            assert disc == 4 * u * u * (49 * u * u - 55 * z * z)


def check_surviving_prime_characters() -> None:
    expected = {
        7: (-1, 1, 1),
        43: (-1, 1, 1),
    }
    for p, target in expected.items():
        got = (
            legendre(p, 23),
            legendre(p, 5) * legendre(p, 11),
            legendre(p, 19),
        )
        assert got == target, (p, got, target)


def main() -> None:
    check_polynomial_identities()
    check_binary_forms()
    check_saturation_resultants()
    check_external_discriminant()
    check_surviving_prime_characters()
    print("A2 height-cofactor certificate: OK")


if __name__ == "__main__":
    main()
