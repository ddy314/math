#!/usr/bin/env python3
"""Mechanical checks for the scale-free secondary norm/prefix no-go theorem.

The checks cover the exact norm/phase/prefix algebra and one semantically valid
decimal toy.  They do not prove any asymptotic DD emptiness statement.
"""

from __future__ import annotations


def check_toy() -> None:
    # Same valid toy used by the secondary-carrier audit.
    v2 = 13
    v1 = 1
    m = 3
    T = 2
    H = 5
    U = 139
    Z = 109
    qV = 10
    b1V = 1
    m2 = 3
    tau2 = 30
    g0 = 1
    a2 = 1
    R0 = 8

    assert 2**H * Z - 5**T * U == v1 * v2
    assert U * qV == b1V * 10**m2 + v2 * tau2
    assert v2 * tau2 < 10**m2

    A = g0 * a2 * v1
    B = R0 * tau2
    real = A * 2 ** (m - 2) * qV
    imag = B * 5 ** (2 * T - m)

    # pi=3+2i divides real-i*imag; quotient is -180-280i.
    dr, di = -180, -280
    assert 3 * dr - 2 * di == real
    assert 2 * dr + 3 * di == -imag
    n_delta = dr * dr + di * di
    assert v2 * n_delta == real * real + imag * imag

    d2 = H - (2 * m - 4)
    d5 = 3 * T - 2 * m
    d2p, d2m = max(d2, 0), max(-d2, 0)
    d5p, d5m = max(d5, 0), max(-d5, 0)

    cU = A * A * 2**d2m * 5**d5m
    cZ = B * B * 2**d2p * 5**d5p

    C = cU * qV * qV * U + cZ * Z
    assert C % v2 == 0
    K = C // v2

    cross = cU * qV * b1V * 10**m2 + cZ * Z
    assert cross % v2 == 0
    J = cross // v2

    assert K == cU * qV * tau2 + J
    assert J > cU * b1V * tau2 * qV
    assert J > qV
    assert K > J > qV

    # Concrete values make accidental sign/normalization errors easy to catch.
    assert cU == 1
    assert cZ == 460800
    assert K == 3_864_700
    assert J == 3_864_400


def main() -> None:
    check_toy()
    print("DD corrected scale-free secondary norm/prefix no-go checks passed")


if __name__ == "__main__":
    main()
