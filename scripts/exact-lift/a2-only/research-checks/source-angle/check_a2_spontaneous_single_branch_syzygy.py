#!/usr/bin/env python3
"""Exact checks for spontaneous-single-branch-syzygy.md."""

import sympy as sp

x,y,t,z=sp.symbols("x y t z")
s=9+y
c=(x+2)**2*(2025*x**2+y**2)/(100*x**2)
L=55*t**2+18*(z-s)*t+s**2-4*s*z-c
Cstar=sp.expand(164025*x**4+656100*x**3+2381*x**2*y**2+41400*x**2*y+842400*x**2+324*x*y**2+324*y**2)

rhs=100*x**2*(9*t-2*s)*(495*t+162*z-52*s)-8100*x**2*L
assert sp.cancel(Cstar-rhs)==0

D=sp.discriminant(L,t)
assert sp.cancel(405*x**2*D-(20*x**2*(81*z+29*s)**2+11*Cstar))==0
assert sp.cancel(23*s**2+81*c-Cstar/(100*x**2))==0

critical=sp.Rational(9,55)*(s-z)
U=81*z+29*s
assert sp.cancel((9*critical-2*s)+U/55)==0
assert sp.expand((495*critical+162*z-52*s)-U)==0
assert sp.cancel((100*x**2*(9*critical-2*s)*(495*critical+162*z-52*s)) + sp.Rational(20,11)*x**2*U**2)==0

print("OK: A2 spontaneous single-branch syzygy certified")
