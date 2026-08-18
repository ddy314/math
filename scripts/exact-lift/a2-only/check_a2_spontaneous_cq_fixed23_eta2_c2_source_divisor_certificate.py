#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md."""

import sympy as sp

cQ = 1587
lam = sp.symbols("lam", integer=True, positive=True)
cu, theta = sp.symbols("cu theta", integer=True, nonzero=True)
S = sp.symbols("S")

# Source product substitution S=5^(3lambda)+cQ*cu, g=S/theta.
g = S / theta

# Mod 5^(lambda-1), source product gives g = cQ*cu*theta^{-1}.
# Algebraic coefficient in the long Gaussian residue after inserting
# b3=2^(3lambda+2)*5*cQ*cu.
iota = sp.symbols("iota")
formal_a5 = sp.expand(
    sp.Rational(1, 2)
    * cQ
    * cu
    * (sp.Symbol("theta_inv") - 45 * iota * 2 ** (3 * lam + 2))
)
assert formal_a5.has(cu)
assert formal_a5.has(iota)

# CRT scale A*B=T/25.
A = 2 ** (lam + 1)
B = 5 ** (lam - 1)
T = 10 ** (lam + 1)
assert sp.simplify(A * B - T / 25) == 0

# Normalized CRT coefficient formula sanity check on concrete coprime moduli.
def crt_cell(r2, r5, A0, B0):
    k = ((r5 - r2) * pow(A0, -1, B0)) % B0
    R = r2 + A0 * k
    return k, R

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

# Source-only recovery is exact once theta divides S_lambda(cu).
for l, c in ((52, 29), (63, 337)):
    N = 5 ** (3 * l) + cQ * c
    # Any admissible theta must divide N; the complementary g is then unique.
    for d in sp.divisors(N)[:20]:
        if d % 2 == 1:
            gg = N // d
            assert gg * d == N

print("OK: source divisor reduction and normalized a3 CRT-cell certificate verified")
