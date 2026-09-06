#!/usr/bin/env python3
"""Mechanical checks for dd-corrected-scale-free-secondary-carrier-2026-09-06.md.

This script checks only algebra/constants/toy divisibility.  It does not certify
asymptotic DD emptiness or a strict slope gap.
"""

from __future__ import annotations

from math import isclose, log10


def check_constants() -> None:
    a = log10(2)
    lam = (2 + a) / (1 + 2 * a)
    A = 2 * (1 + 2 * a) / 3
    M_star = 3 / A
    C_T = (lam + 1) / (lam - 1)
    threshold = M_star / C_T
    margin_half = (M_star - C_T / 2) / 3

    assert isclose(lam, 1.436294525872677, rel_tol=0, abs_tol=1e-12)
    assert isclose(M_star, 2.808883577618032, rel_tol=0, abs_tol=1e-12)
    assert isclose(C_T, 5.58405934844036, rel_tol=0, abs_tol=1e-12)
    assert isclose(threshold, 0.503018217097309, rel_tol=0, abs_tol=1e-12)
    assert threshold > 0.5
    assert isclose(margin_half, 0.00561796779928, rel_tol=0, abs_tol=1e-12)
    assert margin_half > 0


def check_scale_free_secondary_toy() -> None:
    # A semantically valid toy: p=13, iota=5 since 5^2 == -1 mod 13.
    # It also obeys a genuine decimal prefix with m2=3:
    #   U*q_V = 139*10 = 1000 + 13*30.
    p = 13
    iota = 5
    m = 3
    T = 2
    H = 5
    U = 139
    Z = 109
    v1 = 1
    v2 = p
    qV = 10
    b1V = 1
    m2 = 3
    tau2 = 30
    g0 = 1
    a2 = 1
    R0 = 8

    assert (iota * iota + 1) % p == 0
    assert 2 * T > m
    assert (2**H) * Z - (5**T) * U == v1 * v2
    assert U * qV == b1V * (10**m2) + v2 * tau2
    assert v2 * tau2 < 10**m2

    # Raw scale-free pair-max/source congruence.
    B = 10**m // (2 * 5**T)
    raw_lhs = g0 * a2 * B * v1 * qV
    raw_rhs = 2 * 5**T * iota * R0 * tau2
    assert (raw_lhs - raw_rhs) % p == 0

    # Secondary-normalized congruence.
    sec_lhs = g0 * a2 * v1 * 2 ** (m - 2) * qV
    sec_rhs = iota * R0 * tau2 * 5 ** (2 * T - m)
    assert (sec_lhs - sec_rhs) % p == 0

    # Chosen Gaussian prime pi=3+2i has i -> 5 mod 13.
    # Numerator is 20 - 1200 i, quotient should be -180 - 280 i.
    real = sec_lhs
    imag = R0 * tau2 * 5 ** (2 * T - m)
    qr = -180
    qi = -280
    assert 3 * qr - 2 * qi == real
    assert 2 * qr + 3 * qi == -imag
    assert real * real + imag * imag == p * (qr * qr + qi * qi)


def main() -> None:
    check_constants()
    check_scale_free_secondary_toy()
    print("DD corrected scale-free secondary carrier checks passed")


if __name__ == "__main__":
    main()
