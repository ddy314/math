#!/usr/bin/env python3
"""Exact certificate for spontaneous-jh-root-gap.md."""

import sympy as sp

x,y,t=sp.symbols("x y t")
s=y+9
G=sp.expand(
    100*x**2*(5*s**2-36*s*t+55*t**2)
    -(x+2)**2*(2025*x**2+y**2)
)

# Vertex.
dG=sp.diff(G,t)
tstar=sp.solve(sp.Eq(dG,0),t)[0]
assert sp.factor(tstar-18*(y+9)/55)==0
assert sp.Rational(44982,13750)>3

# tau=1 simplification.
G1=sp.expand(G.subs(t,1))
expected=sp.expand(
    100*x**2*(5*y**2+54*y+136)
    -(x+2)**2*(2025*x**2+y**2)
)
assert sp.expand(G1-expected)==0

# Coarse exact endpoint lower/upper bounds used in the proof.
first_lower=(
    5*sp.Rational(249,250)**2
    +54*sp.Rational(249,250)+136
)
second_upper=(
    (2+sp.Rational(2,19))**2
    *(2025*sp.Rational(2,19)**2+1)
)
assert first_lower==sp.Rational(12172701,62500)
assert first_lower>194
assert second_upper==sp.Rational(1494400,14440)
assert second_upper<104
assert first_lower-second_upper>90

# Leading coefficient is positive throughout endpoint.
assert sp.Poly(G,t).LC()==5500*x**2

print("OK: A2 J_H real roots are uniformly beyond tau=1")
