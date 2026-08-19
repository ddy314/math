#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-decimal-tropical-identity.md."""

import sympy as sp

K,T,Q,b3,cu,c,D,U = sp.symbols("K T Q b3 cu c D U", nonzero=True)
P=6*K**2-36*K+55
FH=5*K**2-36*K+55
beta=c*D
z=cu*T*Q/b3
AH=cu*beta/b3
f=AH+cu
BW=cu**2*FH+z**2*K**2
Rplus=D*P-K*U
LJB=2*D*AH*K-f*U
Eplus=c*Rplus
Lambda=b3*c*LJB/cu
Bdec=b3**2*FH+T**2*Q**2*K**2
Fdec=T*Q+2*b3

# B_W decimal reader.
assert sp.factor(b3**2*BW-cu**2*Bdec) == 0

# f decimal reader, under the actual beta=TQ+b3 relation.
expr=sp.expand(b3*f-cu*Fdec)
expr=sp.factor(expr.subs(D,(T*Q+b3)/c))
assert expr == 0

# Full source Bezout itself.
source=cu**2*f*Rplus-(D*f*BW-D*z*AH**2*K**2+K*cu**2*LJB)
# It becomes exact after U=DK-N; introduce N through U relation for the check.
N=sp.symbols("N")
source=sp.factor(source.subs(U,D*K-N))
assert source == 0

# Fully-decimal identity.  Substitute actual beta=TQ+b3 by D=(TQ+b3)/c.
identity=(
    b3**2*Fdec*Eplus
    - beta*Fdec*Bdec
    + beta**3*T*Q*K**2
    - K*b3**2*Lambda
)
identity=sp.factor(sp.together(identity.subs(D,(T*Q+b3)/c)))
assert identity == 0

# Abstract valuation ledger used by the theorem.
# After extracting p^(2h), RHS residual depths are exactly rB,h,rho.
for h in range(1,6):
    for rB in range(1,6):
        for rho in range(1,6):
            depths=(2*h+rB,3*h,2*h+rho)
            assert min(depths)==2*h+min(rB,h,rho)
            m=min(rB,h,rho)
            if sum(v==m for v in (rB,h,rho))==1:
                assert sum(v==min(depths) for v in depths)==1

print("OK: A2 B_W residual and R+/tail tropical balance are fully decimalized")
