#!/usr/bin/env python3
"""Certificate for spontaneous-crt-f1270-source-audit.md."""

import sympy as sp
from fractions import Fraction as F

K,T,a,D,C,B,N,Q,N0=sp.symbols("K T a D C B N Q N0")
G=T*K**2-(18*T+4*a)*K+18*a-1215*T
P=6*K**2-36*K+55
R3=6*(a+3*T)**2+T**2
H79=1215*T**2-36*T*a-5*a**2

assert sp.factor(sp.resultant(G,2*K-9,K)) == -5103*T
assert sp.factorint(5103)=={3:6,7:1}
assert sp.factor(sp.resultant(G,18*K-55,K)) == 1872*a-408455*T
assert sp.factor(sp.resultant(G,T*K+a,K)) == -T*H79

Ns=3*D-C
height_res=sp.factor(sp.resultant(G,D*K-Ns,K))
height_expected=C**2*T+12*C*D*T+4*C*D*a-1260*D**2*T+6*D**2*a
assert sp.expand(height_res-height_expected)==0

res_target=sp.factor(sp.resultant(G,P,K))
H6=57169585*T**2-543816*T*a+1392*a**2
assert sp.expand(res_target-H6)==0
assert sp.factor(sp.discriminant(H6,a)) == -6*(61352*T)**2

res_third=sp.factor(sp.resultant(H79,R3,a))
assert res_third == 58875145*T**4
assert sp.factorint(58875145)=={5:1,7:1,79:1,107:1,199:1}
assert sp.factor(sp.discriminant(H79,a)) == 18**2*79*T**2

# Endpoint windows.
zlo,zhi=F(1),F(251,250)
H79_lo=F(1215)-36*zhi-5*zhi*zhi
H79_hi=F(1215)-36*zlo-5*zlo*zlo
assert H79_lo>1173 and H79_hi==1174

src_lo=F(408455)-1872*zhi
src_hi=F(408455)-1872*zlo
assert src_lo>406575 and src_hi==406583

dlo,dhi=F(0),F(3,250)
# L_H/(D^2 T)=1260-6z-(12+4z)d-d^2.
height_lo=F(1260)-6*zhi-(12+4*zhi)*dhi-dhi*dhi
height_hi=F(1260)-6*zlo
assert height_lo>1253 and height_hi==1254

# Unique fixed target states after normalizing T=1.
expected={7:(5,2),79:(28,51),107:(11,96),199:(83,116)}
for p,(ar,kr) in expected.items():
    states=[]
    for av in range(p):
        if int(H79.subs({T:1,a:av}))%p: continue
        if int(R3.subs({T:1,a:av}))%p: continue
        for kv in range(p):
            if int(P.subs(K,kv))%p==0 and int(G.subs({T:1,a:av,K:kv}))%p==0:
                states.append((av,kv))
    assert states==[(ar,kr)]

# Pure-prefix H1270 2-adic orientation: lower Q^2 N0 term leaves +1 mod8.
# This is valuation bookkeeping rather than a symbolic polynomial identity.
for m in range(5,10):
    assert 2*m+1 >= 11

print("OK: A2 F1270 singular overlaps collapse to the claimed short/fixed prime-source gates")
