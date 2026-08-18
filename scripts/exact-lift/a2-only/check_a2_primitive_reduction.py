#!/usr/bin/env python3
"""Finite arithmetic checks for A2 primitive-reduction.md.

The proof in the markdown file is algebraic.  This script only certifies the
fixed rational coefficients and the quadratic-reciprocity simplifications used
in the q/f-height channel separation.
"""

from fractions import Fraction


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    x = pow(a, (p - 1) // 2, p)
    return 1 if x == 1 else -1


def primes_upto(n: int):
    out = []
    for x in range(2, n + 1):
        if all(x % q for q in range(2, int(x**0.5) + 1)):
            out.append(x)
    return out


def main() -> None:
    # Under saturation a3/T = -9/2.
    a = Fraction(-9, 2)
    r23_coeff = 2 * a * a + 9 * a + 13
    assert r23_coeff == 13

    # After also imposing H0 == 0 mod p, the f-curvature companion is
    # (-55/2) * g^2*T^3/5^lambda modulo p.
    r23f_coeff = Fraction(13, 1) - Fraction(81, 2)
    assert r23f_coeff == Fraction(-55, 2)

    # For p == 3 mod 4, (-23/p) == (p/23).
    # Also (-55/p) == (p/5)(p/11).
    for p in primes_upto(5000):
        if p in {2, 3, 5, 11, 23} or p % 4 != 3:
            continue
        assert legendre(-23, p) == legendre(p, 23)
        assert legendre(-55, p) == legendre(p, 5) * legendre(p, 11)

    # q-height intersection: K == 9/2 and K^2 == 26 imply p | 23.
    # Clearing the denominator leaves the exact integer difference 104-81.
    assert 4 * 26 - 9 * 9 == 23

    print("R23 saturation coefficient:", r23_coeff)
    print("R23,f height+saturation coefficient:", r23f_coeff)
    print("quadratic reciprocity checks: OK")
    print("q-height resultant 4*26-9^2 =", 4 * 26 - 9 * 9)


if __name__ == "__main__":
    main()
