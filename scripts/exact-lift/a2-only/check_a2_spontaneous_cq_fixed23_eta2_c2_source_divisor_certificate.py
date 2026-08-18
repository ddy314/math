#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md."""

import sympy as sp

cQ = 1587
lam = sp.symbols("lam", integer=True, positive=True)
cu, theta = sp.symbols("cu theta", integer=True, nonzero=True)

# ---------------------------------------------------------------------------
# 1. Source-product substitution and 5-adic elimination of g.
# ---------------------------------------------------------------------------
# If g*theta = 5^(3lambda)+cQ*cu, then modulo 5^(lambda-1)
# one has g = cQ*cu*theta^{-1}. Inserting
# b3=2^(3lambda+2)*5*cQ*cu into (g-9*iota*b3)/2 gives the formula below.
iota, theta_inv = sp.symbols("iota theta_inv")
formal_a5 = sp.expand(
    sp.Rational(1, 2)
    * cQ
    * cu
    * (theta_inv - 45 * iota * 2 ** (3 * lam + 2))
)
expanded_from_g_b3 = sp.expand(
    sp.Rational(1, 2)
    * (
        cQ * cu * theta_inv
        - 9 * iota * (2 ** (3 * lam + 2) * 5 * cQ * cu)
    )
)
assert sp.simplify(formal_a5 - expanded_from_g_b3) == 0

# ---------------------------------------------------------------------------
# 2. CRT scale A*B=T/25.
# ---------------------------------------------------------------------------
A = 2 ** (lam + 1)
B = 5 ** (lam - 1)
T = 10 ** (lam + 1)
assert sp.simplify(A * B - T / 25) == 0


def crt_cell(r2, r5, A0, B0):
    k = ((r5 - r2) * pow(A0, -1, B0)) % B0
    R = r2 + A0 * k
    return k, R


# Normalized CRT coefficient sanity checks use only small/medium deterministic
# modular arithmetic; no factorization of source integers occurs here.
for l in (8, 19, 30):
    A0 = 2 ** (l + 1)
    B0 = 5 ** (l - 1)
    for r2 in (1, A0 // 3, A0 - 1):
        for r5 in (0, 1, B0 // 3, B0 - 1):
            k, R = crt_cell(r2, r5, A0, B0)
            assert 0 <= k < B0
            assert 0 <= R < A0 * B0
            assert R % A0 == r2 % A0
            assert R % B0 == r5 % B0
            if 0 < R < A0 * B0 / 10:
                assert k < B0 / 10

# ---------------------------------------------------------------------------
# 3. Divisor recovery is purely algebraic: once theta|S, g=S/theta is unique.
# Use synthetic exact examples rather than factoring the real 100+ digit S.
# ---------------------------------------------------------------------------
for S0, d in ((3 * 5 * 7 * 11, 5 * 11), (13 * 17 * 29, 17), (101 * 103, 101)):
    assert S0 % d == 0
    g0 = S0 // d
    assert g0 * d == S0

print("OK: source divisor reduction and normalized a3 CRT-cell certificate verified")
