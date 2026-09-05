#!/usr/bin/env python3
"""Arithmetic audit for the w=1 fixed-pair branch (u,v)=(27,23).

Assume the strict endpoint reduction already proved in the A1 README:

    54*beta - 23*alpha = 5**d,
    5**(d+1)*s + beta = 23*2**c*n0,

with d>=1, c>=3, alpha,beta,n0 all coprime to 10, and
s=(10**(2*k+1)-1)/27.  The first equation has the complete
parameterization

    alpha = 7*5**d + 54*m,
    beta  = 3*5**d + 23*m.

The second equation and 23 | Q force

    R := (5*s+3)/23 = (5*10**(2*k+1)+76)/621,
    5**d*R + m = 2**c*n0.

Since v2(R)=2 and c>=3, necessarily v2(m)=2.  This in turn gives
r10=alpha*beta == 1 (mod 8).  Since 5 does not divide m,
r10 is always a quadratic non-residue modulo 5.

This file checks the short residue algebra and the numerical scale bounds.
It is a research audit, not a replacement for the written unbounded proof.
"""

from __future__ import annotations

from fractions import Fraction


def vp(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def ab(d: int, m: int) -> tuple[int, int]:
    return 7 * 5**d + 54 * m, 3 * 5**d + 23 * m


def main() -> None:
    # The two k classes from the previous endpoint-period audit.
    for k in (52, 118):
        # k=52 represents the 52 mod 99 class; k=118 represents 19 mod 99
        # while staying in the active k>=32 range.
        b1 = 10 ** (2 * k + 1) - 1
        q_big = 10 ** (2 * k + 2) - 9
        assert b1 % 27 == 0
        assert q_big % 23 == 0
        s = b1 // 27
        assert s % 23 == 4
        r_aux = (5 * s + 3) // 23
        assert 23 * r_aux == 5 * s + 3
        assert vp(r_aux, 2) == 2

    # If m == 4 mod 8 and 5 does not divide m, the parameterized factors
    # have the claimed local residues for either parity of d.
    for d in range(1, 9):
        for m in range(4, 200, 8):
            if m % 5 == 0:
                continue
            alpha, beta = ab(d, m)
            assert 54 * beta - 23 * alpha == 5**d
            assert alpha % 5 != 0 and beta % 5 != 0
            r10 = alpha * beta
            assert r10 % 8 == 1
            assert r10 % 5 in (2, 3)  # Legendre symbol -1 modulo 5.

    # Endpoint scale: alpha*beta/25**d = (7+54x)(3+23x), x=m/5**d.
    # delta>=12 and xi>196000 force the product above 11760; the global
    # delta and xi upper bounds keep it below about 1.226e6.  Hence x is
    # positive and, safely, 2 < x < 32.
    lower = Fraction(12 * 196_000, 200)
    upper = Fraction(10_001 * 15_214_000, 621 * 200)

    def product_at(x: int) -> int:
        return (7 + 54 * x) * (3 + 23 * x)

    assert product_at(0) < lower
    assert product_at(2) < lower
    assert product_at(32) > upper

    print("w=1 fixed-pair local-lock audit: OK")
    print("normalized product interval:", float(lower), float(upper))
    print("safe parameter strip: 2 < m/5^d < 32")
    print("forced residues: v2(m)=2, r10=1 mod 8, (r10|5)=-1")


if __name__ == "__main__":
    main()
