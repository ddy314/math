#!/usr/bin/env python3
"""Mechanical checks for good-prefix-polarization.md.

This checks only exact digit-count/algebra patterns and the numerical leading
CRT constant.  The asymptotic o(S) inputs are proved in the proof notes.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


def digits(n: int) -> int:
    assert n > 0
    return len(str(n))


def check_concat_digit_identity() -> None:
    """A12=a1*10^n2+a2 has n1+n2 digits for positive digit blocks."""

    for n1 in range(1, 6):
        for n2 in range(1, 6):
            lo1, hi1 = 10 ** (n1 - 1), 10**n1 - 1
            lo2, hi2 = 10 ** (n2 - 1), 10**n2 - 1
            for a1 in (lo1, hi1):
                for a2 in (lo2, hi2):
                    A12 = a1 * 10**n2 + a2
                    assert digits(A12) == n1 + n2
                    assert A12 % (10**n2) == a2
                    assert (A12 - a2) // (10**n2) == a1


def check_affine_residue_pushdown() -> None:
    """Check the generic affine substitution A12=t*a1+a2 modulo M."""

    # Use many coprime toy moduli.  This is the exact algebra behind pushing
    # QCRT/GCRT rational periods from A12 down to a1 when gcd(t,M)=1.
    for M in (7, 11, 13, 17, 19, 23, 29):
        for t in (10, 100, 1000):
            tinv = pow(t, -1, M)
            for a2 in range(M):
                for rho in range(M):
                    a1_res = ((rho - a2) * tinv) % M
                    for k in range(3):
                        a1 = a1_res + k * M
                        A12 = t * a1 + a2
                        assert A12 % M == rho


def check_leading_constant() -> None:
    getcontext().prec = 30
    z_star = Decimal("0.308883577618")
    combined = Decimal(2) * z_star + Decimal(1)
    assert combined == Decimal("1.617767155236")
    assert combined > Decimal(1)


def main() -> None:
    check_concat_digit_identity()
    check_affine_residue_pushdown()
    check_leading_constant()
    print("DD Good prefix-polarization checks passed")


if __name__ == "__main__":
    main()
