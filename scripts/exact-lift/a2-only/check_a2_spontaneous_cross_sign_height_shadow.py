#!/usr/bin/env python3
"""Exact certificate for spontaneous-cross-sign-height-shadow.md."""

import sympy as sp

x,y=sp.symbols("x y")
P=101*x**2+4*x+4
H1=202500*x**4+P*y**2
H2=(
    410062500*x**6-402975*x**4*y**2-7290000*x**4*y
    +8100*x**3*y**2+101*x**2*y**4+3600*x**2*y**3
    +40500*x**2*y**2+4*x*y**4+4*y**4
)
X=(
    205031250*x**6+2025*x**4*y**2-1822500*x**4*y
    +8100*x**3*y**2-99*x**2*y**4-1800*x**2*y**3
    +4050*x**2*y**2+4*x*y**4+4*y**4
)

R1sq=20250*x**3*(9*x-2)*(11*x+2)-90*x*y*P
expr=sp.factor(P**2*(-2*X)-R1sq**2)
assert sp.rem(expr,H1,y)==0

D2=2025*x**2-2*y**2-27*y
assert sp.expand((-2*X)-((-2*H2)+(10*x*D2)**2))==0

Q1=9801*x**4-792*x**3-372*x**2+48*x+32
res1=sp.factor(sp.resultant(H1,R1sq,y))
assert res1==410062500*x**6*P*Q1
assert sp.factor(sp.discriminant(Q1,x))==2**18*3**7*5**2*11**2*3677363
assert sp.factorint(3677363)=={3677363:1}

Q2=10609*x**4+2472*x**3+3052*x**2+432*x+288
res2=sp.factor(sp.resultant(H2,D2,y))
assert res2==672605015625*x**6*(25*x**2+1)*Q2
assert sp.factor(sp.discriminant(Q2,x))==2**18*3**2*5**2*61*103**2*2671*6659

# Finite repeated-root checks.
def repeated_root(poly,p):
    g=sp.gcd(sp.Poly(poly,x,modulus=p),sp.Poly(sp.diff(poly,x),x,modulus=p))
    return g
assert repeated_root(Q1,11).degree()==0
r=repeated_root(Q1,3677363)
assert r.degree()==1
assert int(r.eval(1336107))%3677363==0
assert repeated_root(Q2,103).degree()==0
r2671=repeated_root(Q2,2671)
assert r2671.degree()==1 and int(r2671.eval(2615))%2671==0
r6659=repeated_root(Q2,6659)
assert r6659.degree()==1 and int(r6659.eval(654))%6659==0

# p^2 linearized compatibility helper.
def audit(F,G,p,x0,y0):
    vals=[int(F.subs({x:x0,y:y0})),int(G.subs({x:x0,y:y0}))]
    assert vals[0]%p==0 and vals[1]%p==0
    rhs=[(-vals[0]//p)%p,(-vals[1]//p)%p]
    J=[[int(sp.diff(F,v).subs({x:x0,y:y0}))%p for v in (x,y)],
       [int(sp.diff(G,v).subs({x:x0,y:y0}))%p for v in (x,y)]]
    det=(J[0][0]*J[1][1]-J[0][1]*J[1][0])%p
    assert det==0
    compat=((J[0][0]*rhs[1]-J[1][0]*rhs[0])%p==0 and
            (J[0][1]*rhs[1]-J[1][1]*rhs[0])%p==0)
    return rhs,compat

rhs,compat=audit(H1,R1sq,3677363,1336107,2340128)
assert rhs==[482973,1688419] and not compat
rhs,compat=audit(H2,D2,2671,2615,601)
assert rhs==[1437,335] and not compat
rhs,compat=audit(H2,D2,6659,654,2478)
assert rhs==[4424,4966] and not compat

print("OK: A2 cross-sign height shadows and singular audits certified")
