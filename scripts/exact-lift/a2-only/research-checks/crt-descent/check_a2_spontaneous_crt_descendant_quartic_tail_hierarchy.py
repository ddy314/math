#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-quartic-tail-hierarchy.md."""

import math
import sympy as sp


def v2(n: int) -> int:
    n=abs(int(n)); assert n
    return (n & -n).bit_length()-1


def bernstein_nd(poly_expr, vars_, intervals):
    q=sp.symbols('q0:%d'%len(vars_))
    expr=sp.expand(poly_expr.subs({x:a+(b-a)*qq for x,qq,(a,b) in zip(vars_,q,intervals)}))
    P=sp.Poly(expr,*q,domain=sp.QQ)
    degs=[P.degree(qq) for qq in q]
    power=dict(P.terms())
    import itertools
    out=[]
    for ks in itertools.product(*[range(d+1) for d in degs]):
        val=sp.Rational(0)
        for ii in itertools.product(*[range(k+1) for k in ks]):
            aa=power.get(tuple(ii),0)
            if not aa: continue
            mult=sp.Rational(1)
            for k,i,d in zip(ks,ii,degs):
                mult*=sp.Rational(math.comb(k,i),math.comb(d,i))
            val+=aa*mult
        out.append(val)
    return degs,out

K,zeta,J,R=sp.symbols('K zeta J R')
F,Lerr=sp.symbols('F Lerr')
X,Y,chi=sp.symbols('X Y chi')
r,u,v=sp.symbols('r u v')
U=2*K-9

# Universal cubic and exact first-layer point.
Lk=K**2-576*K+1296
A0=5*K**2+144*K-324
B2=381*K**4-78048*K**3-277520*K**2+2392704*K-3074112
B1=189*K**4-126720*K**3+132784*K**2+1359360*K-2218752
B0=63*K**4-54432*K**3+136672*K**2+239616*K-539136
E63=sp.expand(98304*U**3*A0*zeta**3-1024*U**2*B2*zeta**2+32*U*Lk*B1*zeta-Lk**2*B0)
R0=K**2-(18+4*zeta)*K+18*zeta+55
J0=(K**2-64*K*zeta-576*K+288*zeta+1296)/(16*U)

Phi=J*(J+2*zeta)*(K-J)**2-R*(J+zeta)**2
Ctr=sp.Rational(65536)*U**4/K**8

# Exact Euclidean quotient Q(r,u,v).
Eproj=sp.Poly(sp.expand(E63.subs({K:1/r,zeta:u/r})*r**8),r)
Lproj=sp.Poly(55*r**2+18*(u-1)*r+1-4*u-v,r)
Qproj,_=sp.div(Eproj,Lproj)
Qact=sp.factor(Qproj.as_expr().subs({r:1/K,u:zeta/K,v:R0/K**2-Lerr}))

transport=sp.expand(Ctr*(Phi.subs({J:J0+F/U,R:R0+K**2*Lerr})-Phi.subs({J:J0,R:R0})))
M=sp.factor(transport-Qact*Lerr)
PM=sp.Poly(M,F,Lerr)
assert PM.total_degree()==4
assert {mon for mon,c in PM.terms()} == {
    (1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(0,3),(4,0),(0,4)
}

# Homogeneous parent forms after F=K^2 sL Y, L=sL(X+Y).
Hrat={}
for n in range(1,5):
    e=sp.Integer(0)
    for (ef,el),cc in PM.terms():
        if ef+el==n:
            e += cc*F**ef*Lerr**el
    Hrat[n]=sp.factor(e.subs({F:K**2*Y,Lerr:X+Y}))

expected_den={
    1:5**7*11**7*K**6,
    2:5**5*11**6*K**4,
    3:5**5*11**5*K**2,
    4:5**4*11**4,
}
expected_content={1:64,2:256,3:8192,4:65536}
Hprim={}
for n in range(1,5):
    num,den=sp.together(Hrat[n]).as_numer_denom()
    assert sp.factor(den)==expected_den[n]
    cont,prim=sp.primitive(sp.Poly(sp.expand(num),X,Y,K,zeta).as_expr(),X,Y,K,zeta)
    assert cont==expected_content[n]
    Hprim[n]=sp.Poly(prim,X,Y,K,zeta,domain=sp.ZZ)

H3=Hprim[3]; H4=Hprim[4]
assert len(H3.terms())==24
assert H3.degree(zeta)==2
assert all(ix+iy==3 for (ix,iy,ik,iz),c in H3.terms())
assert len(H4.terms())==5
assert all(ix+iy==4 and ik==iz==0 for (ix,iy,ik,iz),c in H4.terms())
H4_expected=2*3**12*13*(X+Y)**4+5**4*11**4*Y**4
assert sp.expand(H4.as_expr()-H4_expected)==0

# Projective positivity of H3 for actual parent ratio chi.
h3proj=sp.expand(H3.as_expr().subs({X:chi,Y:1,K:1/r,zeta:u/r})*r**2)
degs,b3=bernstein_nd(h3proj,(r,u,chi),((0,sp.Rational(1,1000)),(0,sp.Rational(1,1000)),(0,sp.Rational(1,23))))
assert degs==[2,2,3]
assert len(b3)==36
assert min(b3)==77742383923
assert max(b3)==sp.Rational(70017378306520823817,760437500)
assert min(b3)>0

# First-order coefficient lower bound for the sign proof.
h1=sp.factor(Hrat[1].subs({X:chi,Y:1}))
h1proj=sp.factor(h1.subs({K:1/r,zeta:u/r}))
nh1,dh1=sp.together(h1proj).as_numer_denom()
assert dh1==5**7*11**7
_,b1=bernstein_nd(nh1,(r,u,chi),((0,sp.Rational(1,1000)),(0,sp.Rational(1,1000)),(0,sp.Rational(1,23))))
assert max(b1)==-545871046771800704
h1_abs=sp.Rational(545871046771800704,5**7*11**7)
assert h1_abs>350000

# H2 is strictly negative on the same parent box.
h2=sp.factor(Hrat[2].subs({X:chi,Y:1}))
h2proj=sp.factor(h2.subs({K:1/r,zeta:u/r}))
nh2,dh2=sp.together(h2proj).as_numer_denom()
assert dh2==5**5*11**6
_,b2c=bernstein_nd(nh2,(r,u,chi),((0,sp.Rational(1,1000)),(0,sp.Rational(1,1000)),(0,sp.Rational(1,23))))
assert max(b2c)<0

h3_upper=sp.Rational(max(b3)*8192,5**5*11**5)
assert h3_upper<1500000
h4_upper=sp.Rational(65536,5**4*11**4)*(2*3**12*13*sp.Rational(24,23)**4+5**4*11**4)
assert h4_upper<183000
wmax=sp.Rational(8,125)
assert -350000+wmax**2*1500000<0
assert -350000+wmax**2*1500000+wmax**3*183000<0

# 2-adic cubic ledger after T^6 clearing.
def ledger(poly,m,t,degT=6):
    yv=m+t-1
    vals=[]
    for (ix,iy,ik,iz),cc in poly.terms():
        vals.append((v2(int(cc))+iy*yv+ik+m*(degT-iz),(ix,iy,ik,iz),int(cc)))
    return sorted(vals)

v3=ledger(H3,5,3)
assert v3[0][0:2]==(23,(3,0,0,2))
assert v3[1][0]>=29
c3=H3.coeff_monomial(X**3*zeta**2)
assert c3==-8800610472
assert sp.factorint(abs(c3))=={2:3,3:8,107:1,1567:1}
# relative slopes vs baseline 4m+3 are nonnegative
for (ix,iy,ik,iz),cc in H3.terms():
    assert iy+2-iz>=0
    assert iy>=0

# N3 primitive coefficient is 3*X mod8; since X=3 mod4, N3 is 1 mod4.
assert ((c3//2**3)*(5**2*11**2))%8==3
for xmod in (3,7):
    assert (3*xmod)%4==1
    assert (-3*xmod)%4==3

# Quartic ledger: X^4 is unique shallowest.
v4=ledger(H4,5,3)
assert v4[0][0:2]==(31,(4,0,0,0))  # 6m + v2(2*3^12*13) = 31
assert v4[1][0]>31
c4=H4.coeff_monomial(X**4)
assert c4==2*3**12*13
assert ((c4//2)*(5**3*11**3))%8==3

# Abstract finite valuation resolution.
def vp(n,p):
    n=abs(int(n))
    if n==0: return 10**9
    k=0
    while n%p==0:
        n//=p; k+=1
    return k

p=101
for h in range(1,4):
    # stop in first, second, third layer
    for rho in range(h):
        assert vp(p**(h+rho)+p**(2*h)+p**(3*h)+p**(4*h),p)==h+rho
    for sigma in range(h):
        assert vp(p**(2*h+sigma)+p**(3*h)+p**(4*h),p)==2*h+sigma
    for tau in range(h):
        assert vp(p**(3*h+tau)+p**(4*h),p)==3*h+tau
    # terminal tail can carry arbitrary residual depth kappa.
    for kappa in range(0,4):
        assert vp(p**(4*h+kappa),p)==4*h+kappa

print('OK: descendant recycling terminates in a four-tail exact hierarchy; third parent tail carries 3 mod4 parity')
