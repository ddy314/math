#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-h4-short-carrier.md."""

import sympy as sp
from fractions import Fraction as F

x,y=sp.symbols('x y')
d=225*x**2-y
Asp=4*d**2-x*y**2*(99*x-4)
Aminus=Asp-2*y**2*(x+2)**2
Aplus=202500*x**4+99*x**2*y**2-4*x*y**2-4*y**2
Delta0=2025*x**2-18*y-y**2
Cstar=(164025*x**4+656100*x**3+2381*x**2*y**2+41400*x**2*y
       +842400*x**2+324*x*y**2+324*y**2)

raw=sp.expand(1296*(x+2)**2*(2025*x**2+y**2)-309700*x**2*(9+y)**2)
V4=sp.expand(raw/4)
expected=(656100*x**4+2624400*x**3-77101*x**2*y**2-1393650*x**2*y
          -3647025*x**2+1296*x*y**2+1296*y**2)
assert sp.expand(V4-expected)==0
P=sp.Poly(V4,x,y)
assert P.total_degree()==4
assert len(P.terms())==7
fl=sp.factor_list(V4,x,y)
assert fl[0] in (1,-1)
assert len(fl[1])==1 and fl[1][0][1]==1
assert sp.Poly(fl[1][0][0],x,y).total_degree()==4
for old in (d,Asp,Aminus,Aplus,Delta0,Cstar):
    assert sp.gcd(P,sp.Poly(old,x,y)).total_degree()==0

# V4 = 25 x^2 s^2 (1296 c/s^2 - 3097).
s=9+y
c=(x+2)**2*(2025*x**2+y**2)/(100*x**2)
assert sp.simplify(V4-25*x**2*s**2*(1296*c/s**2-3097))==0

lower=25*F(1,100)*F(2499,250)**2*(F(3097)-F(1296)*F(21,20))
upper=25*F(4,361)*100*F(3097)
assert lower==F(54212853681,1250000) and lower>43000
assert upper==F(1630000,19) and upper<86000

# Integer clearing coefficients.
B,A,N=sp.symbols('B A N')
cleared=sp.expand(N**4*V4.subs({x:B/N,y:10*A/N}))
expected_int=(656100*B**4+2624400*B**3*N-7710100*B**2*A**2
              -13936500*B**2*A*N-3647025*B**2*N**2
              +129600*B*A**2*N+129600*A**2*N**2)
assert sp.expand(cleared-expected_int)==0

print('OK: generic h4 singularity is read by an irreducible 7-term degree-4 prefix carrier with fixed negative window')
