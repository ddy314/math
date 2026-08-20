#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-gaussian-unit.md."""

import sympy as sp

# k_h=1 and delta in {0,1}: N(G_5)=1/3^delta can be an integer only for delta=0.
valid_delta = [delta for delta in (0, 1) if 1 % (3**delta) == 0]
assert valid_delta == [0]

# Norm-one Gaussian integers are the four units in a small exhaustive box.
units = []
for a in range(-2, 3):
    for b in range(-2, 3):
        if a * a + b * b == 1:
            units.append((a, b))
assert sorted(units) == [(-1, 0), (0, -1), (0, 1), (1, 0)]

# Explicit Gaussian factorization coordinates.
rm, rp, R3, R1 = sp.symbols("rm rp R3 R1")
real = sp.expand(rm * rp - R3 * R1)
imag = sp.expand(rm * R1 + rp * R3)
assert sp.expand((rm + sp.I * R3) * (rp + sp.I * R1) - (real + sp.I * imag)) == 0

# Norm multiplicativity of the explicit factorization.
lhs_norm = sp.expand(real**2 + imag**2)
rhs_norm = sp.expand((rm**2 + R3**2) * (rp**2 + R1**2))
assert sp.expand(lhs_norm - rhs_norm) == 0

# In the fixed type d=1, nu_5=lambda-2, so the Gaussian modulus has norm 5^lambda.
lam = sp.symbols("lam", integer=True, positive=True)
d = 1
nu = lam - 2
assert sp.expand(d + (nu + d) - lam) == 0

print("OK: A2 fixed-23 eta=2 c=2 has delta=0, Gaussian-unit quotient, and explicit two-factor prefix decomposition")
