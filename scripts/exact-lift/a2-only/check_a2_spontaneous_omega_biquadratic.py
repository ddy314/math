#!/usr/bin/env python3
"""Exact certificate for spontaneous-omega-biquadratic.md."""

import sympy as sp

x,y,t,r=sp.symbols("x y t r")
P=101*x**2+4*x+4
R=101*x**2+4*x+8
Am=sp.expand(202500*x**4-P*y**2-1800*x**2*y)

# First quadratic layer.
assert sp.factor(sp.discriminant(Am,y)-(900*x**2)**2*R)==0
yplus=450*x**2/(2+r)
yminus=450*x**2/(2-r)
# Verify each root in the quotient r^2=R.
def reduce_r(expr):
    num,den=sp.fraction(sp.together(expr))
    rem=sp.rem(sp.Poly(sp.expand(num),r),sp.Poly(r**2-R,r),domain=sp.QQ[x]).as_expr()
    return sp.factor(rem),sp.factor(den)
for yy in (yplus,yminus):
    rem,den=reduce_r(Am.subs(y,yy))
    assert rem==0

# Additive quadratic and its discriminant.
s=y+9
J=sp.expand(
    100*x**2*(5*s**2-36*s*t+55*t**2)
    -(x+2)**2*(2025*x**2+y**2)
)
D=sp.expand(
    22275*x**4+89100*x**3+991*x**2*y**2+17640*x**2*y
    +168480*x**2+44*x*y**2+44*y**2
)
assert sp.factor(sp.discriminant(J,t)-2000*x**2*D)==0

AL=501055*x**4+44440*x**3+104756*x**2+4304*x+4992
BL=4*(4955*x**2+220*x+416)
Lp=AL+r*BL
Lm=AL-r*BL

# On y+ sheet, D = 405*x^2/(r+2)^2 * L+ modulo r^2=R.
expr_plus=sp.together(D.subs(y,yplus)-405*x**2*Lp/(r+2)**2)
rem,_=reduce_r(expr_plus)
assert rem==0
expr_minus=sp.together(D.subs(y,yminus)-405*x**2*Lm/(2-r)**2)
rem,_=reduce_r(expr_minus)
assert rem==0

# Hence tau discriminants are square prefactors times L+/-.
disc=sp.discriminant(J,t)
expr_plus=sp.together(disc.subs(y,yplus)-(900*x**2/(r+2))**2*Lp)
rem,_=reduce_r(expr_plus)
assert rem==0
expr_minus=sp.together(disc.subs(y,yminus)-(900*x**2/(2-r))**2*Lm)
rem,_=reduce_r(expr_minus)
assert rem==0

# The old degree-8 eliminant is exactly the quadratic norm.
Qomega=sp.expand(
    251056113025*x**8+44533768400*x**7+67275876360*x**6
    +8529261920*x**5+6336428816*x**4+503628928*x**3
    +239152384*x**2+8466432*x+2768896
)
norm=sp.expand(AL**2-R*BL**2)
assert sp.expand(norm-Qomega)==0
assert sp.factor(sp.resultant(Am,D,y)-164025*x**4*Qomega)==0

# Source collision r=0 gives y=225*x^2.
assert sp.factor(yplus.subs(r,0)-225*x**2)==0
assert sp.factor(yminus.subs(r,0)-225*x**2)==0

# Real separation bounds.
assert R.subs(x,sp.Rational(1,10))==sp.Rational(941,100)
assert sp.Rational(941,100) > sp.Rational(301,100)**2
upper=sp.Rational(450)*sp.Rational(4,361)/sp.Rational(501,100)
assert upper==sp.Rational(60000,60287)
assert upper < sp.Rational(249,250)

print("OK: A2 omega-content biquadratic tower certified")
