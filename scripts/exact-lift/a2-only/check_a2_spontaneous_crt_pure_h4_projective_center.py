#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-h4-projective-center.md."""

import sympy as sp
from fractions import Fraction as F

t,s,z,c,u,v=sp.symbols('t s z c u v')
K,zz=sp.symbols('K zz')

U=2*K-9
Lk=K**2-576*K+1296
A0=5*K**2+144*K-324
B2=381*K**4-78048*K**3-277520*K**2+2392704*K-3074112
B1=189*K**4-126720*K**3+132784*K**2+1359360*K-2218752
B0=63*K**4-54432*K**3+136672*K**2+239616*K-539136
E63=sp.expand(98304*U**3*A0*zz**3-1024*U**2*B2*zz**2+32*U*Lk*B1*zz-Lk**2*B0)
Et=sp.Poly(sp.expand(E63.subs({K:s/t,zz:z/t})*t**8),t)
L=sp.Poly(55*t**2+18*(z-s)*t+s**2-4*s*z-c,t)
num,_=sp.together(sp.rem(Et,L).as_expr()).as_numer_denom()
pr=sp.Poly(num,t)
A=pr.coeff_monomial(t)
B=pr.coeff_monomial(1)

a=sp.expand(A.subs({s:1,z:u,c:v}))
b=sp.expand(B.subs({s:1,z:u,c:v}))
sub=sp.subresultants(a,b,v)
S1=sp.Poly(sub[-2],v)
h4=sp.Poly(-29520930816*u**4-46902675456*u**3+90353275489*u**2+114775877404*u+31476144004,u)
av=sp.rem(sp.Poly(S1.coeff_monomial(v),u),h4).as_expr()
b0=sp.rem(sp.Poly(S1.coeff_monomial(1),u),h4).as_expr()
assert sp.rem(sp.Poly(1296*b0+3097*av,u),h4).is_zero
C4=sp.primitive(sp.Poly(sp.together(av).as_numer_denom()[0],u).as_expr(),u)[1]
assert sp.degree(C4,u)==3
E4=int(sp.resultant(h4.as_expr(),C4,u))
assert E4 != 0
assert len(str(abs(E4)))==315

# Known small-prime content of E4.
R=abs(E4)
known={2:84,3:83,5:13,7:11,11:12,13:40,29:2}
for p,e in known.items():
    got=0
    while R%p==0:
        R//=p; got+=1
    assert got==e
assert len(str(R))==171

# Exact specialization: v=3097/1296 makes both coefficient equations carry h4.
vr=sp.Rational(3097,1296)
As=sp.factor(A.subs(c,vr*s**2))
Bs=sp.factor(B.subs(c,vr*s**2))
H4s=(31476144004*s**4+114775877404*s**3*z+90353275489*s**2*z**2-46902675456*s*z**3-29520930816*z**4)
assert sp.rem(sp.Poly(sp.together(As).as_numer_denom()[0],z),sp.Poly(H4s,z)).is_zero
assert sp.rem(sp.Poly(sp.together(Bs).as_numer_denom()[0],z),sp.Poly(H4s,z)).is_zero

# Endpoint v upper bound.
upper=(F(40,19)**2*(F(8461,361)))/(F(2499,250)**2)
assert upper==F(846100000000,813854775321)
assert upper < F(21,20)
assert F(3097,1296)>F(119,50)
assert F(119,50)-F(21,20)==F(133,100)

print('OK: generic h4 singularity fixes c/s^2=3097/1296, far above the real endpoint window')
