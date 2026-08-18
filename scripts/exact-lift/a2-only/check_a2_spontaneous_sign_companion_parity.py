#!/usr/bin/env python3
"""Exact certificate for spontaneous-sign-companion-parity.md."""

import sympy as sp

M,m=sp.symbols("M m", integer=True, nonnegative=True)
A,Q0,cQ,cu,g,K,a3=sp.symbols("A Q0 cQ cu g K a3", integer=True)

# Angle primitive difference exponent arithmetic.
raw_angle = (
    4*A**2
    * 2**(M+1)*Q0
    * 2**(M+m+1)*5**sp.Symbol("d", integer=True, nonnegative=True)*cQ*cu
)
d=sp.Symbol("d", integer=True, nonnegative=True)
raw_angle = 4*A**2*2**(M+1)*Q0*2**(M+m+1)*5**d*cQ*cu
prim_angle=sp.simplify(raw_angle/2**(2*M+m+2))
assert prim_angle == 4*A**2*Q0*5**d*cQ*cu

# Additive sign-pair difference.
B=2**(M+m+1)*cu*g
raw_add=4*B**2*(2*K-9)*a3
prim_add=sp.simplify(raw_add/2**(2*M+m+2))
assert prim_add == 2**(m+2)*(cu*g)**2*(2*K-9)*a3

# The additive correction is at least 8 times an integer for m>=1.
for mm in range(1,8):
    assert 2**(mm+2) % 8 == 0

# Common mod-4 orientation after removing same odd gcd.
for D in (1,3):
    r=(3*pow(D,-1,4))%4
    assert r==(3 if D==1 else 1)

print("OK: A2 angle/additive sign-companion parity identities certified")
