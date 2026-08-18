#!/usr/bin/env python3
"""Exact checks for spontaneous-single-branch.md."""

import sympy as sp

x, y, t, z = sp.symbols("x y t z")
s = 9 + y
Nbar = 2025*x**2 + y**2
c = (x+2)**2*Nbar/(100*x**2)

ztheta = (
    x**2*(s**2 - 18*s*t + 55*t**2)
    -(x+2)**2*Nbar/100
)/(2*x**2*(2*s-9*t))
L = 55*t**2 + 18*(z-s)*t + s**2 - 4*s*z - c
assert sp.cancel((ztheta-z) - L/(2*(2*s-9*t))) == 0

D = sp.factor(sp.discriminant(L,t))
expected = 324*z**2 + 232*s*z + 104*s**2 + 220*c
assert sp.cancel(D-expected) == 0
complete = 324*(z+sp.Rational(29,81)*s)**2 + sp.Rational(5060,81)*s**2 + 220*c
assert sp.cancel(D-complete) == 0

critical = sp.solve(sp.diff(L,t), t)[0]
assert critical == sp.Rational(9,55)*(s-z)
assert sp.factor(L.subs(t,critical) + D/220) == 0

lower = sp.factor(sp.Rational(9,55)*(sp.Rational(2499,250)+sp.Rational(1223295069,256000000)))
assert lower == sp.Rational(34040439621,14080000000)
assert lower > sp.Rational(12,5)

print("OK: A2 spontaneous single branch certified")
