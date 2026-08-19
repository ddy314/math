#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-triple-orientation.md."""

import sympy as sp

K,D,N,T,a3=sp.symbols("K D N T a3", integer=True)
P=6*K**2-36*K+55
RPD=55*D**2-36*D*N+6*N**2
R3=6*(a3+3*T)**2+T**2
U=D*K-N
alpha=T*K+a3
Rplus=D*P-K*U
LD3=55*T*D-36*T*N-6*N*a3

# Three sqrt(-6) completions / orientation identities.
assert sp.expand(P-(6*(K-3)**2+1))==0
assert sp.expand(55*RPD-((55*D-18*N)**2+6*N**2))==0
assert sp.expand(R3-(6*(a3+3*T)**2+T**2))==0

# Exact cross-orientation identity.
assert sp.expand(LD3-(T*Rplus+T*(36-5*K)*U-6*N*alpha))==0

# Fixed-exception Bezout identity.
assert sp.expand(25*P-(30*K+36)*(5*K-36))==2671
assert sp.isprime(2671)
assert 2671%24==7
assert (36*pow(5,-1,2671))%2671==2144

# First-layer orientation sanity for all allowed roots modulo sample primes.
for p in list(sp.primerange(7,400)):
    if p in (2,3,5):
        continue
    roots=[k for k in range(p) if (6*k*k-36*k+55)%p==0]
    for k in roots:
        assert k%p!=0
        d=pow(k,-1,p)
        xp=(6*(k-3))%p
        xd=(55*d-18)%p
        assert xd==(-xp)%p
        assert xp*xp%p==(-6)%p

print("OK: A2 deep target has a fixed-2671 source/third orientation exception")
