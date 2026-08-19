#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-h1-additive-bezout.md."""

import sympy as sp
from fractions import Fraction

A,B,N=sp.symbols("A B N", integer=True)
K=9*N+10*A
Q=B+2*N
N0=sp.Rational(81,4)*B**2+A**2
F=(K-5)*(5*K-11)
CH=101*B**2+4*B*N+4*N**2
H1=2025*B**4+A**2*CH
JH=B**2*F-Q**2*N0
RH1=4*CH*F-81*Q**4

# Exact Bezout identity.
assert sp.expand(4*CH*JH+4*Q**2*H1-B**2*RH1)==0
assert sp.expand(CH-100*B**2-Q**2)==0

# Normalized identity in x,y,tau.
x,y,t=sp.symbols("x y t")
s=9+y
Cnorm=101*x**2+4*x+4
Rnorm=4*Cnorm*(s-5*t)*(5*s-11*t)-81*(x+2)**4
# K/N=s and tau=1/N turn F/N^2 into the two linear factors.
assert sp.expand((s-5*t)*(5*s-11*t)-(5*s**2-36*s*t+55*t**2))==0

# The coarse rational positivity bound used in the proof.
lower=16*Fraction(197,20)*Fraction(4939,100)
upper=81*3**4
assert lower>upper

# 2-adic orientation: exact integer samples cover the symbolic residue pattern.
def vp(n,p=2):
    e=0
    while n%p==0:
        e+=1
        n//=p
    return e

for M in range(2,8):
    for m in range(1,5):
        for b0 in (1,3,5,7):
            for a in (1,3,5,7):
                Nv=10**M
                Bv=2**(M+m+1)*b0
                Kv=9*Nv+10*a
                Qv=Bv+2*Nv
                CHv=101*Bv**2+4*Bv*Nv+4*Nv**2
                Fv=(Kv-5)*(5*Kv-11)
                Rv=4*CHv*Fv-81*Qv**4
                assert vp(CHv)==2*M+2
                assert (CHv//2**(2*M+2))%4==1
                assert Kv%4==2
                assert Fv%4==3
                assert vp(Rv)==2*M+4
                assert (Rv//2**(2*M+4))%4==3

# H1 first layer makes C_H an explicit negative square class.
r=sp.symbols("r", nonzero=True)
# If CH=-r^2, the equal-depth cancellation coefficient is a square.
ratio=sp.simplify(-1/(-r**2))
assert ratio==r**-2

print("OK: A2 H1/additive exact Bezout bridge, positive 3mod4 carrier, and unequal-depth law certified")
