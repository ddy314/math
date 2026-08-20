#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-four-sheet-split.md."""

import sympy as sp

K,D,N,T,a3=sp.symbols("K D N T a3", integer=True)
P=6*K**2-36*K+55
U=D*K-N
LD=D*(K-6)+N
RPD=55*D**2-36*D*N+6*N**2
alpha=T*K+a3
L3=T*(K-6)-a3
R3=6*(a3+3*T)**2+T**2

# Parallel source/third exact sheet identities.
assert sp.expand(D**2*P-RPD-6*U*LD)==0
assert sp.expand(T**2*P-R3-6*alpha*L3)==0
assert sp.expand(U+LD-2*D*(K-3))==0
assert sp.expand(alpha+L3-2*T*(K-3))==0
assert sp.expand(P-(6*(K-3)**2+1))==0

# Finite orientation sanity over sample primes and all P-roots.
for p in list(sp.primerange(7,300)):
    if p in (2,3,5):
        continue
    roots=[k for k in range(p) if int(P.subs(K,k))%p==0]
    for k in roots:
        if k%p==0 or (k-6)%p==0:
            continue
        xp=6*(k-3)%p
        # source minus U=0 -> D/N=1/K
        dminus=pow(k,-1,p)
        xdminus=(55*dminus-18)%p
        assert xdminus==(-xp)%p
        # source plus LD=0 -> D/N=-1/(K-6)
        dplus=(-pow((k-6)%p,-1,p))%p
        xdplus=(55*dplus-18)%p
        assert xdplus==xp%p
        # third minus alpha=0 -> a3/T=-K
        x3minus=6*((-k+3)%p)%p
        assert x3minus==(-xp)%p
        # third plus L3=0 -> a3/T=K-6
        x3plus=6*((k-6+3)%p)%p
        assert x3plus==xp%p

print("OK: A2 P/R_PD/R_3 common roots split into four canonical source/third sheets")
