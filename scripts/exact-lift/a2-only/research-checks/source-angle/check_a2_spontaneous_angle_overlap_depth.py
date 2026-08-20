#!/usr/bin/env python3
"""Exact polynomial certificate for spontaneous-angle-overlap-depth.md."""

import sympy as sp

x, y, r = sp.symbols("x y r")
d = 225*x**2-y
Delta = 2025*x**2-18*y-y**2
Phi = (99*x-4)*r-2*x-4
Asp = 4*d**2-x*y**2*(99*x-4)
Omega = sp.expand(Asp*r+2*x*y**2*(x+2))
Ff = r*(x+2)+2*x

# Source decomposition.
assert sp.expand(Omega-(4*r*d**2-x*y**2*Phi)) == 0

# f-line Bezout identity.
assert sp.factor((x+2)*Omega-Asp*Ff+200*x**3*Delta) == 0

# q-line Euclidean identity.
Jq = sp.expand(
    202500*r*x**3-405000*r*x**2-99*r*x*y**2-1800*r*x*y
    +202*r*y**2+3600*r*y+2*x*y**2
)
assert sp.expand(Omega-400*r*Delta-(x+2)*Jq) == 0

# On x=-2 and Delta=0, J_q=-4y^2.  Verify with polynomial reduction.
J_at = sp.expand(Jq.subs(x,-2))
Delta_at = sp.expand(Delta.subs(x,-2))
rem = sp.rem(sp.Poly(J_at+4*y**2,y), sp.Poly(Delta_at,y)).as_expr()
assert sp.expand(rem) == 0

# The old first-layer resultant formulas are recovered exactly.
assert sp.factor(sp.resultant(Ff,Omega,r)+200*x**3*Delta) == 0
assert sp.factor(Omega.subs(x,-2)-400*r*Delta.subs(x,-2)) == 0
assert sp.factor(sp.resultant(Phi,Omega,r)-8*(x+2)*d**2) == 0

print("OK: A2 spontaneous overlap depth identities certified")
