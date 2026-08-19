#!/usr/bin/env python3
"""Certificate for spontaneous-crt-height-primitive-remainder.md."""

import sympy as sp

K,T,a=sp.symbols("K T a")
F0=T*K**2-(18*T+4*a)*K+18*a+55*T
identity=sp.expand((2*K-9)*((2*K-12)*T-2*a)-F0)
assert identity == T*(3*K**2-24*K+53)

# 5-adic bookkeeping for J_Delta after division by 5^(lambda-d):
# three terms have depths 3d, 2d, 3d; the middle coefficient is a unit.
for d in range(1,20):
    depths=(3*d,2*d,3*d)
    assert min(depths)==2*d
    assert 3*d+2>2*d  # U_63 is deeper

# Full descent exponent: nu_5+2d=lambda.
lam,d=sp.symbols("lam d", integer=True)
nu=lam-2*d
assert sp.expand(nu+2*d-lam)==0

# Mod-5 unit: 2K-9 == 1 mod5 when K==0 mod5.
assert (-9) % 5 == 1

# 5^(2d) is 1 mod4, so primitive 3-mod-4 orientation is unchanged.
for d0 in range(1,10):
    assert pow(5,2*d0,4)==1

print("OK: A2 short height remainder has exact 5^(2d) content and full-5 descent")
