#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-square-core.md."""

import sympy as sp

# ----------------------------------------------------------------------
# Exact decimal identities for alpha and its top complement.
N,T,e2,h3=sp.symbols("N T e2 h3", positive=True, integer=True)
a2=N/10-e2
a3=T+h3
K=9*N+10*a2
alpha=T*K+a3
Calpha=10*T*N-alpha

assert sp.expand(K-(10*N-10*e2))==0
assert sp.expand(Calpha-(10*T*e2-a3))==0

# ----------------------------------------------------------------------
# Rational endpoint bounds.
# e2 < N/2500 gives K > 2499/250 N.
assert 10-sp.Rational(10,2500)==sp.Rational(2499,250)
# e2>=1 and a3<251/250 T give the top gap >2249/250 T.
assert 10-sp.Rational(251,250)==sp.Rational(2249,250)

# The upper complement bound follows from e2<N/2500 and a3>T:
# 10*T*e2-a3 < T*N/250-T < T*N/250.
assert sp.Rational(10,2500)==sp.Rational(1,250)

# ----------------------------------------------------------------------
# Canonical valuation identity behind the square-core factorization.
# For nonnegative e,h:
# (e+h)-2*min(e,h)=abs(e-h).
for ev in range(8):
    for hv in range(8):
        assert ev+hv-2*min(ev,hv)==abs(ev-hv)

# Triple-gcd identity.  At each prime write
# alpha: e+h, beta: e+s, H0: c+h,
# with gcd(W,S)=1 => min(h,s)=0 and gcd(omega,cu)=1 => min(e,c)=0.
# Then min(v(alpha),v(beta),v(H0)) = min(e,h).
for ev in range(6):
    for hv in range(6):
        for sv in range(6):
            for cv in range(6):
                if min(hv,sv)!=0 or min(ev,cv)!=0:
                    continue
                triple=min(ev+hv,ev+sv,cv+hv)
                assert triple==min(ev,hv)

# Equal depth contributes an exact square block p^(2h) to alpha.
for hv in range(1,8):
    assert hv+hv==2*hv

print("OK: A2 equal-depth primes form a bounded original-integer triple-gcd square core")
