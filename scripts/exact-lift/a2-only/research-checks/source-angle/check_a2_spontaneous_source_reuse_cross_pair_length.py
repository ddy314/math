#!/usr/bin/env python3
"""Certificate for spontaneous-source-reuse-cross-pair-length.md."""

import sympy as sp

B,N=sp.symbols("B N", integer=True)
K=sp.Rational(55,18)
A=(K-9*N)/10
Q=B+2*N
N0=(sp.Rational(9,2)*B)**2+A**2
FH=5*K**2-36*K+55
J=sp.Poly(B**2*FH-Q**2*N0,B,N).clear_denoms()[1].as_expr()
U=(45*B**2-2*A*N)**2-A**2*B*(99*B-4*N)
X=sp.Poly(49*U**2-220*A**4*Q**4,B,N).clear_denoms()[1].as_expr()

Phi1=(
152356364573249030359104*N**8-4097103068832023796480*N**7
+31384125262928360244960*N**6+18803025591118547565600*N**5
+2075376150266128766100*N**4+1943181330646900509000*N**3
+675406005318781110000*N**2-26358539660104162500*N
+244063541277015625)
Phi2=(
40095472108377374070575040576*N**8+30284848824599488024870272000*N**7
+13738744691885641990863011040*N**6+4454752959867937104210016800*N**5
+1029832152338324301433146900*N**4+174239977384696722571611000*N**3
+19756759606772961743190000*N**2+621005812442557377412500*N
+5763793275102412515625)
C=132849458140481700073021440000000000000000

res=sp.resultant(J,X,B)
assert sp.expand(res-C*N**8*(162*N-55)**8*Phi1*Phi2)==0
assert sp.factorint(C)=={2:28,3:38,5:16,7:4}

# Positive t=162N-55 transforms.
t=sp.symbols("t")
for Phi in (Phi1,Phi2):
    num=sp.fraction(sp.together(Phi.subs(N,(t+55)/162)))[0]
    _,prim=sp.Poly(num,t).primitive()
    assert all(c>0 for c in prim.all_coeffs())

# Repeated candidate states quoted in the proof.
def gcd_bn(p,n):
    return sp.gcd(sp.Poly(J.subs(N,n),B,modulus=p),sp.Poly(X.subs(N,n),B,modulus=p))
assert gcd_bn(19,15).monic().as_expr()==B**2
assert sp.gcd(sp.Poly(Phi1,N,modulus=23),sp.Poly(Phi1,N,modulus=23).diff()).degree()==2
assert all(int(sp.gcd(sp.Poly(Phi1,N,modulus=23),sp.Poly(Phi1,N,modulus=23).diff()).eval(i))%23 for i in range(23))

# p=67 has two full simple states.
det=sp.diff(J,B)*sp.diff(X,N)-sp.diff(J,N)*sp.diff(X,B)
for b,dv in ((53,57),(37,46)):
    assert int(J.subs({B:b,N:1}))%67==0
    assert int(X.subs({B:b,N:1}))%67==0
    assert int(det.subs({B:b,N:1}))%67==dv

# Three genuine singular projection states fail p^2 compatibility.
states=[
(8971,8433,8743,[(5124,6911,3110),(7124,6240,5864)]),
(102251,35831,90859,[(53480,77070,90010),(18723,47191,56760)]),
(630451,242244,110422,[(143149,160161,311616),(279823,277602,522614)]),
]
def rankmod(rows,p):
    a=[[x%p for x in row] for row in rows]
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        q=next((i for i in range(r,m) if a[i][c]),None)
        if q is None: continue
        a[r],a[q]=a[q],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[(x*inv)%p for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                f=a[i][c]
                a[i]=[(a[i][j]-f*a[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r
for p,b,n,quoted in states:
    rows=[]
    for F in (J,X):
        F0=int(F.subs({B:b,N:n}))
        assert F0%p==0
        rows.append((int(sp.diff(F,B).subs({B:b,N:n}))%p,
                     int(sp.diff(F,N).subs({B:b,N:n}))%p,
                     (-F0//p)%p))
    assert rows==quoted
    assert rankmod([r[:2] for r in rows],p)==1
    assert rankmod(rows,p)==2

# Large repeated root is outside the decimal subgroup.
p=136776907; n=93550173
ord10=7598717
assert pow(10,ord10,p)==1
assert pow(n,ord10,p)!=1

print("OK: A2 source-reuse O/J cross-pair projects to two simple pure-length octic orbits")
