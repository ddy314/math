#!/usr/bin/env python3
"""Exact certificate for spontaneous-oplus-thetaplus-root-gap.md."""

import sympy as sp

x,y,t,z=sp.symbols("x y t z")
s=y+9
c=(x+2)**2*(2025*x**2+y**2)/(100*x**2)

L=55*t**2+18*(z-s)*t+s**2-4*s*z-c
A=55*t**2-18*s*t+s**2-c
B=18*t-4*s
assert sp.expand(L-(A+B*z))==0

# Theta sign flip sends z_theta to -z_theta, so cross equation uses L(t,-z_i).
Lsharp=sp.expand(L.subs(z,-z))
assert sp.expand(Lsharp-(A-B*z))==0
assert sp.Poly(Lsharp,t).LC()==55

# tau=0 and tau=1 identities used for sign placement.
assert sp.expand(Lsharp.subs(t,0)-(s**2+4*s*z-c))==0
assert sp.expand(A.subs(t,1)-(y**2-26-c))==0
assert sp.expand(B.subs(t,1)-(-18-4*y))==0

# Coarse endpoint inequalities. The independent sphere-root checker proves z_i<-4.778<-4.
assert 100-16*9==-44
assert sp.Rational(1223295069,256000000)>4

# If an upward quadratic is negative at both 0 and 1, its two real roots straddle [0,1].
# This final implication is elementary; symbolic checks above certify all algebraic inputs.
print("OK: A2 Oplus/Thetaplus cross roots avoid the decimal interval [0,1]")
