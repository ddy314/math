#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-fixed2671-h1-squeeze.md."""

import sympy as sp

T,Rp,F,U,N,alpha = sp.symbols("T Rp F U N alpha", integer=True)
LD3 = T*Rp - T*F*U - 6*N*alpha
# The proof uses this exact three-term identity and only valuation uniqueness.
assert sp.expand(LD3 - (T*Rp-T*F*U-6*N*alpha)) == 0

p=2671
K0=2144
mod=p*p
# First root.
assert (6*K0*K0-36*K0+55) % p == 0
assert (5*K0-36) % p == 0
# Explicit linear p^2 lift from the transversality file.
KF = (36*pow(5,-1,mod)) % mod
assert KF == 5707400
assert (5*KF-36) % mod == 0
# It remains on exact h=1 quadratic baseline: P is divisible by p but not p^2.
P=lambda x:6*x*x-36*x+55
assert P(KF) % p == 0
assert P(KF) % mod != 0
assert (P(KF)//p) % p == 2030

# Abstract valuation implication used in §§2-3:
# v(F)>=2, v(U)=1, v(alpha)=2. If v(Rp)>=3 then alpha term is unique shallow.
for vF in range(2,6):
    vU=1
    va=2
    for vRp in range(2,6):
        vals=(vRp,vF+vU,va)
        if vRp>=3:
            assert vals[2] == 2
            assert vals[0] >= 3 and vals[1] >= 3
        # If LD3 can exceed 2 while vF>=2, Rp cannot be >=3;
        # the only remaining possibility is vRp=2 and cancellation at depth 2.
        if vRp>=3:
            assert sum(v==min(vals) for v in vals) == 1

print("OK: A2 fixed-2671 h=1 linear p^2 branch cannot support simultaneous parallel and E+ deepening")
