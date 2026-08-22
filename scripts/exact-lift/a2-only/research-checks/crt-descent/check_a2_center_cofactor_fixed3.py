#!/usr/bin/env python3
"""Certificate for center-cofactor-fixed3.md.

In the dangerous Z=1 orientation, the odd-3 allocation has two channels.
The reduced numerator W_q=alpha_0 has exact v_3=1.  Combining its two exact
source equations with the rational-root equation shows the center cofactor
Xi_C has exact v_3=3 in both channels.

This is a fixed-prime local certificate, not an A2 closure certificate.
"""

import itertools
import sympy as sp

K, zeta, delta, R, J = sp.symbols("K zeta delta R J")
k, s, c, r = sp.symbols("k s c r")

Phi = sp.expand(
    J * (J + 2*zeta) * (K - J)**2
    - R * (J + zeta)**2
)

# The actual root is J0=3-delta, delta=C/D.  Since Phi(J0)=0,
# Phi(3)/delta equals this polynomial difference quotient.
Phi3 = sp.expand(Phi.subs(J, 3))
Phi0 = sp.expand(Phi.subs(J, 3-delta))
Qcenter = sp.factor((Phi3-Phi0)/delta)
expected = (
    -K**2*delta + 2*K**2*zeta + 6*K**2
    -2*K*delta**2 + 4*K*delta*zeta + 18*K*delta
    -24*K*zeta -54*K
    +R*delta -2*R*zeta -6*R
    -delta**3 +2*delta**2*zeta +12*delta**2
    -18*delta*zeta -54*delta +54*zeta +108
)
assert sp.expand(Qcenter-expected) == 0

# In Z=1: K,zeta,delta are divisible by 3 and R is divisible by 9.
subs = {K:3*k, zeta:3*s, delta:3*c, R:9*r}
Qscaled = sp.expand(Qcenter.subs(subs))
assert all(int(a) % 27 == 0 for a in sp.Poly(Qscaled,k,s,c,r).coeffs())
P = sp.Poly(Qscaled/27, k,s,c,r, modulus=3)

# The actual-root equation starts at 3^4 in the same normalization.
rootscaled = sp.expand(Phi0.subs(subs))
assert all(int(a) % 81 == 0 for a in sp.Poly(rootscaled,k,s,c,r).coeffs())
Root = sp.Poly(rootscaled/81, k,s,c,r, modulus=3)


def ev(poly, cv, kv, sv, rv):
    return int(poly.eval({c:cv,k:kv,s:sv,r:rv})) % 3

# Exact v3(W_q)=1 gives two source unit conditions after division by 3:
#   W_q q/D = k-1+c,
#   W_q c_u/g = s+1-c.
# Both RHS must therefore be nonzero mod 3.
def source_units(cv, kv, sv):
    return (kv-1+cv) % 3 != 0 and (sv+1-cv) % 3 != 0

# Channel A: v3(a3)=1, v3(a2)>=2.
# Then k=0, s is a unit, and v3(R)>=4 so r=0 mod3.
A=[]
for cv in range(3):
    for sv in (1,2):
        if source_units(cv,0,sv) and ev(Root,cv,0,sv,0)==0:
            A.append((cv,0,sv,0,ev(P,cv,0,sv,0)))
assert A == [(0,0,1,0,1),(2,0,2,0,1)]

# Channel B: v3(a2)=1, v3(a3)>=2.
# Then s=0, k is a unit, v3(N0)=2, and Q/b2 is a 3-unit square,
# hence R/9=1 mod3.
B=[]
for cv in range(3):
    for kv in (1,2):
        if source_units(cv,kv,0) and ev(Root,cv,kv,0,1)==0:
            B.append((cv,kv,0,1,ev(P,cv,kv,0,1)))
assert B == [(0,2,0,1,1),(2,1,0,1,1)]

# Every admissible first-layer state has Qcenter/27 a 3-unit.
assert all(row[-1] != 0 for row in A+B)

print("OK: in Z=1 the center rational-root cofactor has exact v3=3")
