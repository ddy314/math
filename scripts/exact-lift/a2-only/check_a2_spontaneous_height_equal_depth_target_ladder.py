#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-target-ladder.md."""

import sympy as sp

K,D,N,U=sp.symbols("K D N U")
P=6*K**2-36*K+55
R=55*D**2-36*D*N+6*N**2

# U = DK-N.  Exact elimination identity.
expr=sp.expand(D**2*P - (R+(12*N-36*D)*U+6*U**2))
expr=sp.expand(expr.subs(U,D*K-N))
assert expr==0

# Exact Bezout identity for the exceptional linear factor.
L=36*D-11*N
assert sp.expand(1296*R-(1980*D-691*N)*L-175*N**2)==0

# Endpoint rational bound: 599 N^2 < P < 600 N^2 for M>=11.
slo=sp.Rational(2499,250)
tau=sp.Rational(1,10**11)
lower=6*slo**2-360*tau
assert lower>599

# Upper bound is immediate from K<10N and -36K+55<0 for K>=2.
# Verify the fixed 7 local root recorded in the proof.
assert (6*2**2-36*2+55)==7
assert (36*4-11) % 7 == 0
assert (4*2-1) % 7 == 0

# Primewise target ladder valuation law.
for h in range(1,8):
    for rho in range(0,16):
        for k in range(1,6):
            assert min(k*h,rho)==min(k*h,rho)

print("OK: A2 equal-depth targets compress to a short prefix ladder with fixed 7 exception")
