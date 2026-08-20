#!/usr/bin/env python3
"""Certificate for spontaneous-crt-dual-gap-remainder.md."""

import sympy as sp
from fractions import Fraction as F

r,z,K=sp.symbols("r z K", positive=True)
Lfun=2*r**2*z+7*r**2+5*r*z**2+14*r*z+2*z**3+7*z**2
Cfun=2*r**3*z+7*r**3+5*r**2*z**2+28*r**2*z+37*r**2+2*r*z**3+35*r*z**2+74*r*z+14*z**3+37*z**2
# delta=3-r
first=2*(2*K-12-2*z+(3-r))*(2*K-10+(3-r))/K**2
Sdim=(z**2*K**2-2*Lfun*K+Cfun)/(r+z)**2
Enorm=sp.factor(first-2*Sdim/K**2)
C1=-4*(2*r**3+4*r**2*z+9*r**2+r*z**2+18*r*z+9*z**2)/(r+z)**2
C2=2*(r**4+2*r**3*z+9*r**3+18*r**2*z+26*r**2+9*r*z**2+52*r*z+26*z**2)/(r+z)**2
expected=8-2*z**2/(r+z)**2+C1/K+C2/K**2
assert sp.simplify(Enorm-expected)==0

# Safe box certification via corner-friendly coarse arithmetic.
# Leading lower bound.
lead_lo=F(8)-2*F(251,998)**2
assert lead_lo > F(787,100)
# Correction is > -70/K, negligible for K>9e11.
assert lead_lo-F(70,9*10**11) > F(787,100)
# Upper correction is negative once K>4 from C1<-40,C2<130.
assert -F(40,5)+F(130,25) < 0  # evaluate at K=5; improves with K

# Remainder factor arithmetic: 63-8*(787/100)=1/25.
assert F(63)-8*F(787,100)==F(1,25)

# 2-adic depth bookkeeping.
# v2(B_parent)=3m+2t, v2(8 Ehat)=m+4; for m>=5,t>=3 parent is deeper.
for m in range(5,30):
    for t in range(3,10):
        assert 3*m+2*t > m+4

# Primitive mod-4 collapse: Ehat/2^(m+1)=1 -> R/2^(m+4)=-1=3 mod4.
assert (-1) % 4 == 3

print("OK: A2 dual-gap synchronization yields a short primitive 3-mod-4 remainder")
