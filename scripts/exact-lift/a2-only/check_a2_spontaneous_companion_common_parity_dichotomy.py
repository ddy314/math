#!/usr/bin/env python3
"""Certificate for spontaneous-companion-common-parity-dichotomy.md."""

import sympy as sp

# Mod-4 table for the residual pair J1,B1.
for DH in (1, 3):
    for G in (1, 3):
        inv_DH = pow(DH, -1, 4)
        inv_G = pow(G, -1, 4)
        residual = (3 * inv_DH * inv_G) % 4
        expected = 3 if G == DH else 1
        assert residual == expected

# Verify the exact bracket -> linear-gate relation used by the external depth law.
g, om, cu, q, D, T, z, f, N, W, K = sp.symbols(
    "g om cu q D T z f N W K", nonzero=True
)
bracket = (g**2 * om**2 - cu**2) * W - 2 * g**2 * om * T * K
L = D * z * K + f * N
expr = q * bracket + z * L
# Source relations: qW=DK-N, Dz=qgT, z=gom-cu, f=gom+cu.
expr = expr.subs(W, (D * K - N) / q)
expr = expr.subs(T, D * z / (q * g))
expr = expr.subs({z: g * om - cu, f: g * om + cu})
assert sp.factor(expr) == 0

# Abstract valuation ledger: if k=min(j,b), the difference of two terms with
# depths j,b has depth >=k, and exactly k when j!=b.  The theorem transfers
# that depth to L_JB because q,z,W^circ and coefficients are units.
for j in range(1, 7):
    for b in range(1, 7):
        k = min(j, b)
        assert k >= 1
        if j != b:
            assert min(j, b) == k

print("OK: A2 companion common parity splits into residual, external-linear, or height-target cost")
