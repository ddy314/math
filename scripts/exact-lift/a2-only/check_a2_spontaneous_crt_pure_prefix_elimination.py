#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-prefix-elimination.md."""

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
E63=sp.expand(
    98304*U**3*A0*zz**3
    -1024*U**2*B2*zz**2
    +32*U*Lk*B1*zz
    -Lk**2*B0
)

Et=sp.Poly(sp.expand(E63.subs({K:s/t,zz:z/t})*t**8),t)
assert Et.degree()==8
L=sp.Poly(55*t**2+18*(z-s)*t+s**2-4*s*z-c,t)
rem=sp.rem(Et,L).as_expr()
num,den=sp.together(rem).as_numer_denom()
pr=sp.Poly(num,t)
assert pr.degree()==1
A=sp.factor(pr.coeff_monomial(t))
B=sp.factor(pr.coeff_monomial(1))
assert sp.Poly(A,s,z,c).total_degree()==7
assert sp.Poly(B,s,z,c).total_degree()==8
assert len(sp.Poly(A,s,z,c).terms())==20
assert len(sp.Poly(B,s,z,c).terms())==24

# The tau-resultant of the compact quadratic and the linear remainder.
X=sp.expand(55*B**2-18*(z-s)*A*B+(s**2-4*s*z-c)*A**2)
# Verify it agrees with the direct resultant exactly (up to the quadratic's
# leading coefficient convention already captured by the explicit formula).
res=sp.expand(sp.resultant(L.as_expr(),A*t+B,t))
assert sp.expand(X-res)==0

PX=sp.Poly(X,s,z,c)
content=0
for coeff in PX.coeffs():
    content=math.gcd(content,abs(int(coeff)))
assert content==5**7*11**7
Xprim=sp.Poly(sp.expand(X/content),s,z,c)
assert Xprim.total_degree()==16
assert len(Xprim.terms())==59

print('OK: universal descendant cubic reduces branchwise to linear tau and a primitive degree-16 prefix resultant')
