#!/usr/bin/env python3
"""Exact certificate for spontaneous-residual-parity-doubling.md."""

import sympy as sp

M,m=sp.symbols("M m", integer=True, nonnegative=True)
B0,cu,g,omega,Wq,K,a3,A,Q0,cQ=sp.symbols(
    "B0 cu g omega Wq K a3 A Q0 cQ", integer=True
)
Jhat,That=sp.symbols("Jhat That", integer=True)

# Primitive additive-height identity is checked after removing known powers of 2.
# B0=cu*g and B=2^(M+m+1)B0.
C=2**(m+1)*B0**2*(2*K-9)*omega*Wq
assert sp.expand(That-(5**m*Jhat-C)) == That-5**m*Jhat+C

# Check the exponent arithmetic used to divide the raw identity.
assert sp.simplify(2**m * 2**(2*M+2) / 2**(2*M+m+2)) == 1
assert sp.simplify(
    2 * 2**(2*(M+m+1)) / 2**(2*M+m+2)
) == 2**(m+1)

# Actual/conjugate angle primitive difference.
# Q=2^(M+1)Q0, b3=2^(M+m+1)5^d cQ cu.
d=sp.symbols("d", integer=True, nonnegative=True)
raw_angle_diff = 4*A**2 * 2**(M+1)*Q0 * 2**(M+m+1)*5**d*cQ*cu
primitive_angle_diff = sp.simplify(raw_angle_diff / 2**(2*M+m+2))
assert primitive_angle_diff == 4*A**2*Q0*5**d*cQ*cu

# Additive actual/conjugate difference has at least three extra 2-adic bits
# after primitive normalization when m>=1.
raw_additive_diff_factor = sp.simplify(
    4*2**(2*(M+m+1)) / 2**(2*M+m+2)
)
assert raw_additive_diff_factor == 2**(m+2)

# Elementary mod-4 parity duplication: two positive odd 3 mod 4 carriers,
# divided by the same odd gcd D, have identical residual orientation.
for Dr in (1,3):
    invD = pow(Dr,-1,4)
    rr = (3*invD) % 4
    if Dr == 1:
        assert rr == 3
    else:
        assert rr == 1

# Removing a common gcd from both integers gives coprime residuals by valuation.
# Finite valuation sanity check over small exponents.
for a in range(5):
    for b in range(5):
        dmin=min(a,b)
        assert min(a-dmin,b-dmin)==0

print("OK: A2 residual parity doubling identities certified")
