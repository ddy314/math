#!/usr/bin/env python3
"""Exact checks for spontaneous-cstar-audit.md."""

import sympy as sp

N,A,B=sp.symbols("N A B", nonzero=True)
x,y=sp.symbols("x y")
Q=2*N+B
K=9*N+10*A
N0=sp.Rational(81,4)*B**2+A**2
Cint=23*B**2*K**2+81*Q**2*N0
Cstar=sp.expand(164025*x**4+656100*x**3+2381*x**2*y**2+41400*x**2*y+842400*x**2+324*x*y**2+324*y**2)
assert sp.expand(N**4*Cstar.subs({x:B/N,y:10*A/N})-100*Cint)==0

RN=324*Q**2*N0+2695*B**2
assert sp.expand(4*Cint-(RN+B**2*(92*K**2-2695)))==0

center=sp.factor((sp.Rational(1,4))*(92*sp.Rational(55,18)**2-2695))
assert center == -sp.Rational(37180,81)
assert sp.factorint(37180)=={2:2,5:1,11:1,13:2}

print("OK: A2 C-star character shadow certified")
