#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-angle-additive-norm-bridge.md."""

import sympy as sp

A,B,N=sp.symbols("A B N", integer=True)
K=9*N+10*A
Q=B+2*N
N0=sp.Rational(81,4)*B**2+A**2
U=(45*B**2-2*A*N)**2-A**2*B*(99*B-4*N)
F=(K-5)*(5*K-11)
JH=B**2*F-Q**2*N0
HO=N0*U**2+4*A**4*B**2*Q**2*K**2
RHO=F*U**2+4*A**4*Q**4*K**2

# Exact universal identity.
assert sp.expand(Q**2*HO+U**2*JH-B**2*RHO)==0


def vp(n,p=2):
    e=0
    while n%p==0:
        e+=1
        n//=p
    return e

# 2-adic orientation. M>=2 is already enough to see the terminal pattern.
for M in range(2,8):
    for m in range(1,5):
        for b0 in (1,3,5):
            for a in (1,3,5):
                Nv=10**M
                Bv=2**(M+m+1)*b0
                Kv=9*Nv+10*a
                Qv=Bv+2*Nv
                Uv=(45*Bv**2-2*a*Nv)**2-a*a*Bv*(99*Bv-4*Nv)
                Fv=(Kv-5)*(5*Kv-11)
                Rv=Fv*Uv*Uv+4*a**4*Qv**4*Kv**2
                assert vp(Uv)==2*M+2
                assert (Uv//2**(2*M+2))%4==1
                assert Kv%4==2
                assert Fv%4==3
                assert vp(Qv)==M+1
                assert vp(Rv)==4*M+4
                assert (Rv//2**(4*M+4))%4==3
                assert Rv>0

# Equal-depth cancellation coefficient is -square, hence nonsquare at p=3 mod4.
for p in list(sp.primerange(7,200)):
    if p%4!=3 or p in (3,5):
        continue
    for u in (1,2,3,5):
        if u%p:
            value=(-u*u)%p
            assert pow(value,(p-1)//2,p)==p-1

print("OK: A2 moving height angle-norm/additive exact bridge and relative nonsquare law certified")
