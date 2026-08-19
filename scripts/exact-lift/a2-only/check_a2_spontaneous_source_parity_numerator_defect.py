#!/usr/bin/env python3
"""Certificate for spontaneous-source-parity-numerator-defect.md."""

import sympy as sp
N,e=sp.symbols("N e", integer=True)
a2=N/sp.Integer(10)-e
K=9*N+10*a2
assert sp.expand(K-10*(N-e))==0

# If N=10e mod r and 18K-55=0, the residual is 5(324e-11).
expr=sp.expand((18*K-55).subs(N,10*e))
assert expr==5*(324*e-11)

# Constant conversion.
assert sp.Rational(324,2500)==sp.Rational(81,625)
assert float(sp.Rational(81,625))<0.13

print("OK: A2 source parity numerator-angle reuse collapses to 324e-11")
