#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-coefficient-singular.md."""

import math
import sympy as sp

t,s,z,c=sp.symbols('t s z c')
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
assert sp.Poly(A,c).degree()==3
assert sp.Poly(B,c).degree()==4

R=sp.resultant(A,B,c)
content,prim=sp.primitive(sp.Poly(R,s,z).as_expr(),s,z)
assert sp.factorint(abs(int(content)))=={2:72,3:32,5:9,11:9}
fl=sp.factor_list(prim,s,z)
assert fl[0]==1
assert [(sp.Poly(f,s,z).total_degree(),e,len(sp.Poly(f,s,z).terms())) for f,e in fl[1]]==[(4,1,5),(24,1,25)]
H4=fl[1][0][0]
assert sp.expand(H4-(31476144004*s**4+114775877404*s**3*z+90353275489*s**2*z**2-46902675456*s*z**3-29520930816*z**4))==0

u=sp.symbols('u')
h4=sp.Poly(H4.subs({s:1,z:u}),u)
disc=sp.factorint(abs(int(sp.discriminant(h4.as_expr(),u))))
assert disc=={2:21,3:13,5:13,7:6,11:12,13:3,19:1,29:2,163:1,6661944924691447:1}

print('OK: pure descendant coefficient singularity reduces to homogeneous degree-4/24 ratio gates')
