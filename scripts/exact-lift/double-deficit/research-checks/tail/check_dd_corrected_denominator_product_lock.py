#!/usr/bin/env python3
"""Mechanical audits for dd-corrected-denominator-product-lock-2026-09-06.md.

Checks the quantitative qZ-v2 separation constant, the exact modular
elimination behind the product congruence, and a small exact toy instance.
This is not a proof assistant and does not certify asymptotic DD coverage.
"""

from __future__ import annotations

from math import gcd, log10


def constants() -> None:
    a = log10(2)
    lam = (2 + a) / (1 + 2 * a)
    u_star = 0.691116422381969
    z_star = 1 - u_star
    c_z = 2 * a + 0.5 + 1 / (2 * lam)
    c_qz = (1 + a) + c_z
    c_one = 1 + 5 * (1 + 2 * a) / 6
    delta_qz = (1 - 2 * z_star) / (c_one + c_qz)

    assert abs(c_z - 1.450178006813822) < 1e-12
    assert abs(c_qz - 2.751208002477803) < 1e-12
    assert abs(c_one - 2.335049992773302) < 1e-12
    assert abs(delta_qz - 0.075150109396892) < 1e-12
    assert 0 < delta_qz < 0.238062349248111

    # At the threshold the upper/lower exponents meet exactly.
    lhs = 2 * z_star + c_qz * delta_qz
    rhs = 1 - c_one * delta_qz
    assert abs(lhs - rhs) < 1e-12


def exact_product_congruence() -> None:
    # A fully integral toy instance satisfying the decimal-length convention:
    #   Q = U*q = b1*10^m2 + b2,
    #   2^H*Z - 5^T*U = V = v1*v2,
    #   v2 | b2,
    # together with q*Z < v2.
    H = 6
    T = 1
    U = 37
    Z = 3
    v1 = 1
    v2 = 7
    m2 = 1
    b1 = 3
    q = 1
    b2 = 7

    V = v1 * v2
    Q = U * q

    assert 10 ** (m2 - 1) <= b2 < 10**m2
    assert gcd(U * V * Z, 10) == 1
    assert gcd(U, V) == gcd(U, Z) == gcd(V, Z) == 1
    assert gcd(v2, 2) == 1
    assert Q == b1 * 10**m2 + b2
    assert 2**H * Z - 5**T * U == V
    assert b2 % v2 == 0

    left = (2**H * q * Z) % v2
    right = (5**T * b1 * 10**m2) % v2
    assert left == right

    rho = (pow(2**H, -1, v2) * 5**T * b1 * 10**m2) % v2
    assert 0 < q * Z < v2
    assert q * Z % v2 == rho
    assert q * Z == rho


def residue_lock_sanity() -> None:
    # Exhaustively check the elementary last step for small odd moduli:
    # if 0 < x < M and x == rho (mod M), with rho in [0,M), then x=rho.
    for modulus in range(3, 200, 2):
        for x in range(1, modulus):
            rho = x % modulus
            assert 0 <= rho < modulus
            assert x == rho


def main() -> None:
    constants()
    exact_product_congruence()
    residue_lock_sanity()
    print("DD corrected denominator qZ product-lock audit passed")


if __name__ == "__main__":
    main()
