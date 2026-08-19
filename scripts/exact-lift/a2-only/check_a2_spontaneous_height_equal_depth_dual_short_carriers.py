#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-dual-short-carriers.md."""

import math
import sympy as sp

K,T,a3=sp.symbols("K T a3", integer=True)
P=6*K**2-36*K+55
R3=6*(a3+3*T)**2+T**2
alpha=T*K+a3
L3=T*(K-6)-a3

# Exact two-sheet identity and its sum relation.
assert sp.expand(T**2*P-R3-6*alpha*L3)==0
assert sp.expand(alpha+L3-2*T*(K-3))==0
assert sp.expand(P-(6*(K-3)**2+1))==0

# Tight endpoint bound for 1<a3/T<251/250.
upper=6*sp.Rational(1001,250)**2+1
assert upper==sp.Rational(3037253,31250)
assert upper<98
assert 6*4**2+1==97

# Primitive orientations.
# K=10*r with r odd => K == 10 mod 20.
for r in range(1,40,2):
    kval=10*r
    pval=int(P.subs(K,kval))
    assert pval%20==15
    assert (pval//5)%4==3

# a3 odd and T divisible by 8 => R3 == 6 mod 8.
for t in (8,16,40,200):
    for aval in range(1,20,2):
        rval=int(R3.subs({T:t,a3:aval}))
        assert rval%8==6
        assert (rval//2)%4==3

# Finite valuation sanity for the exact gcd sheet factorization.
# Actual endpoint primitive reduction gives 5∤alpha, and T is divisible by 5,
# hence 5∤a3.  Enforce that real hypothesis here; otherwise the fixed prime 5
# can pollute both sheet gcds even though it never belongs to gcd(P,R3) in the
# actual target sector.
for kval in range(10,250,20):
    for tval in (40,200,1000):
        for aval in range(1,60,2):
            if aval%5==0:
                continue
            pval=int(P.subs(K,kval))
            rval=int(R3.subs({T:tval,a3:aval}))
            alphaval=tval*kval+aval
            lval=tval*(kval-6)-aval
            lhs=math.gcd(pval,rval)
            rhs=math.gcd(pval,alphaval)*math.gcd(pval,lval)
            assert lhs==rhs
            assert math.gcd(math.gcd(pval,alphaval),math.gcd(pval,lval))==1

print("OK: A2 target baseline splits into coprime numerator/conjugate short-carrier sheets")
