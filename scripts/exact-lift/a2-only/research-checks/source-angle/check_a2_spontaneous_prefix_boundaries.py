#!/usr/bin/env python3
"""Exact checks for spontaneous-prefix-boundaries.md."""

import sympy as sp

x, y, t, z = sp.symbols("x y t z")
d = 225*x**2-y
Asp = sp.expand(4*d**2-x*y**2*(99*x-4))
Delta0 = 2025*x**2-18*y-y**2
Nbar = 2025*x**2+y**2
wbar = -Asp/(2*y**2*(x+2))

sphere = sp.cancel(
    x**2*wbar**2*(9+y+z)**2
    -(x+2+wbar)**2*(Nbar*wbar**2/100+x**2*z**2)
)
num, _ = sp.fraction(sphere)
P = sp.Poly(sp.expand(num), z)
a2,a1,a0 = [sp.factor(c) for c in P.all_coeffs()]
assert sp.cancel(a2/(160000*x**4*y**6*(x+2)**4*Delta0)) == 1

Hlin = sp.expand(202500*x**4-99*x**2*y**2-1800*x**2*y+4*x*y**2+4*y**2)
assert sp.cancel(a1/(800*x**2*y**4*(x+2)**2*(y+9)*Hlin**2)) == 1
R = sp.factor(sp.resultant(Hlin,Delta0,y))
assert R == 3**8*5**4*x**4*(x+2)**4
assert sp.expand(Nbar-(2*y*(y+9)-Delta0)) == 0

# Q2 / Delta0 projective boundary resultant.
Aplus = sp.expand(202500*x**4+99*x**2*y**2-4*x*y**2-4*y**2)
G = sp.expand(
    410062500*x**6-407025*x**4*y**2-7290000*x**4*y-8100*x**3*y**2
    +99*x**2*y**4+3600*x**2*y**3+24300*x**2*y**2-4*x*y**4-4*y**4
)
z2 = Asp*G/(400*x**2*y**3*(x+2)**2*Delta0)
ztheta = (
    x**2*((9+y)**2-18*(9+y)*t+55*t**2)-(x+2)**2*Nbar/100
)/(2*x**2*(2*(9+y)-9*t))
n2,_ = sp.fraction(sp.cancel(ztheta-z2))
q2 = sp.primitive(sp.Poly(-n2,t,x,y))[1].as_expr()
res = sp.factor(sp.resultant(q2,Delta0,y))
const, factors = sp.factor_list(res)
expected_factors = {
    sp.Poly(x,x).as_expr():10,
    sp.Poly(x+2,x).as_expr():8,
    25*x**2+1:1,
    100*x**2+4-t**2:1,
}
for f,e in factors:
    assert expected_factors.get(sp.expand(f)) == e
assert len(factors) == 4
assert sp.expand(81*(25*x**2+1)-(y+9)**2+Delta0) == 0

print("OK: A2 spontaneous prefix boundaries certified")
