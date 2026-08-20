#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-third-order-balance.md."""

import math
import sympy as sp


def bernstein_coefficients(poly_expr, xvar, yvar, xr, yr):
    X0,Y0=sp.symbols('X0 Y0')
    xa,xb=xr; ya,yb=yr
    expr=sp.expand(poly_expr.subs({xvar:xa+(xb-xa)*X0,yvar:ya+(yb-ya)*Y0}))
    P=sp.Poly(expr,X0,Y0,domain=sp.QQ)
    m=P.degree(X0); n=P.degree(Y0)
    power={(i,j):P.coeff_monomial(X0**i*Y0**j) for i in range(m+1) for j in range(n+1)}
    out=[]
    for k in range(m+1):
        for ell in range(n+1):
            val=sp.Rational(0)
            for i in range(k+1):
                for j in range(ell+1):
                    a=power[(i,j)]
                    if a:
                        val += a*sp.Rational(math.comb(k,i),math.comb(m,i))*sp.Rational(math.comb(ell,j),math.comb(n,j))
            out.append(val)
    return out

K,zeta,J,R=sp.symbols('K zeta J R')
F,Lerr=sp.symbols('F Lerr')
X,Y=sp.symbols('X Y')
r,u,v=sp.symbols('r u v')
U=2*K-9

Lk=K**2-576*K+1296
A0=5*K**2+144*K-324
B2=381*K**4-78048*K**3-277520*K**2+2392704*K-3074112
B1=189*K**4-126720*K**3+132784*K**2+1359360*K-2218752
B0=63*K**4-54432*K**3+136672*K**2+239616*K-539136
E63=sp.expand(98304*U**3*A0*zeta**3-1024*U**2*B2*zeta**2+32*U*Lk*B1*zeta-Lk**2*B0)
R0=K**2-(18+4*zeta)*K+18*zeta+55
J0=(K**2-64*K*zeta-576*K+288*zeta+1296)/(16*U)

Phi=J*(J+2*zeta)*(K-J)**2-R*(J+zeta)**2
PhiJ=sp.diff(Phi,J)
PhiJ0=sp.factor(PhiJ.subs({J:J0,R:R0}))
Ctr=sp.Rational(65536)*U**4/K**8

Eproj=sp.Poly(sp.expand(E63.subs({K:1/r,zeta:u/r})*r**8),r)
Lproj=sp.Poly(55*r**2+18*(u-1)*r+1-4*u-v,r)
Qproj,_=sp.div(Eproj,Lproj)
Qact=sp.factor(Qproj.as_expr().subs({r:1/K,u:zeta/K,v:R0/K**2-Lerr}))
Q0=sp.factor(Qproj.as_expr().subs({r:1/K,u:zeta/K,v:R0/K**2}))

transport=sp.expand(Ctr*(Phi.subs({J:J0+F/U,R:R0+K**2*Lerr})-Phi.subs({J:J0,R:R0})))
M=sp.factor(transport-Qact*Lerr)
PM=sp.Poly(M,F,Lerr)
assert PM.total_degree()==4

# First-order gates and geometric parent ratio.
C_lt=sp.factor(-sp.Rational(65536)*U**4*(J0+zeta)**2/K**6)
C_gt=sp.factor(sp.Rational(65536)*U**3/K**6*(PhiJ0-U*(J0+zeta)**2))
num_lt,den_lt=sp.together(C_lt-Q0).as_numer_denom()
num_gt,den_gt=sp.together(C_gt-Q0).as_numer_denom()
c_lt,Glt_expr=sp.primitive(sp.Poly(sp.expand(num_lt),K,zeta).as_expr(),K,zeta)
c_gt,Ggt_expr=sp.primitive(sp.Poly(sp.expand(num_gt),K,zeta).as_expr(),K,zeta)
assert c_lt==5184 and c_gt==128
assert sp.factor(den_lt)==5**7*11**7*K**6
assert sp.factor(den_gt)==5**7*11**7*K**6
Glt=sp.Poly(Glt_expr,K,zeta,domain=sp.ZZ)
Ggt=sp.Poly(Ggt_expr,K,zeta,domain=sp.ZZ)
chi=sp.factor(-sp.Rational(2)*Ggt.as_expr()/(81*Glt.as_expr()))

# Cubic homogeneous block.
M3=sp.Integer(0)
for (ef,el),cc in PM.terms():
    if ef+el==3:
        M3 += cc*F**ef*Lerr**el
H3rat=sp.factor(M3.subs({F:K**2*Y,Lerr:X+Y}))
num3,den3=sp.together(H3rat).as_numer_denom()
cont3,H3expr=sp.primitive(sp.Poly(sp.expand(num3),X,Y,K,zeta).as_expr(),X,Y,K,zeta)
assert cont3==8192
assert sp.factor(den3)==5**5*11**5*K**2
H3=sp.Poly(H3expr,X,Y,K,zeta,domain=sp.ZZ)
assert len(H3.terms())==24 and H3.degree(zeta)==2

# Evaluate at the geometric recycling ratio.
H3chi=sp.factor(H3rat.subs({X:chi,Y:1}))
numS,denS=sp.together(H3chi).as_numer_denom()
content,S3expr=sp.primitive(sp.Poly(sp.expand(numS),K,zeta).as_expr(),K,zeta)
S3=sp.Poly(S3expr,K,zeta,domain=sp.ZZ)
assert content==2**13
assert sp.factor(denS)==81*K**2*Glt.as_expr()**3
assert S3.total_degree()==20
assert S3.degree(zeta)==19
assert len(S3.terms())==230

# Exact resultant: central, old G_D, and one irreducible degree-148 gate.
res=sp.resultant(E63,S3.as_expr(),zeta)
fl=sp.factor_list(res,K)
assert sp.factorint(abs(int(fl[0])))=={2:174,3:10}
assert [(sp.Poly(f,K).degree(),e) for f,e in fl[1]]==[(1,3),(2,2),(148,1)]
assert sp.expand(fl[1][0][0]-U)==0
GD=11*K**2-240*K+432
assert sp.expand(fl[1][1][0]-GD)==0
P148=sp.Poly(fl[1][2][0],K,domain=sp.ZZ)
assert P148.is_irreducible
assert P148.degree()==148
assert len(P148.terms())==149

# Real projective sign: all 420 Bernstein coefficients are negative.
S3proj=sp.Poly(sp.expand(S3.as_expr().subs({K:1/r,zeta:u/r})*r**20),r,u)
assert S3proj.degree(r)==20 and S3proj.degree(u)==19
assert len(S3proj.terms())==230
box=(sp.Rational(0),sp.Rational(1,1000))
b=bernstein_coefficients(S3proj.as_expr(),r,u,box,box)
assert len(b)==420
assert min(b)==-sp.Rational(
    110643494138140653988416850451597394424139780430491531767088006331095359222500626733242735149107,
    29103830456733703613281250000000000000000000000000,
)
assert max(b)==-sp.Integer(2741384670235465948046260545341682788232526505)
assert max(b)<0

print('OK: strict second-tail overdepth at third order is fixed by central/G_D/P148; generic resonance remains only at sigma=h')
