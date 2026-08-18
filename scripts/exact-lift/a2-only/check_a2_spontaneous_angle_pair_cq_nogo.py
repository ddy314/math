#!/usr/bin/env python3
"""Exact certificate for spontaneous-angle-pair-cq-nogo.md."""

import sympy as sp

x,y=sp.symbols("x y")
Delta=2025*x**2-18*y-y**2
Dx=sp.diff(Delta,x)
Dy=sp.diff(Delta,y)

assert sp.expand(Dx-4050*x)==0
assert sp.expand(Dy+18+2*y)==0
assert int(Dx.subs(x,-2))==-8100

conic=sp.expand(Delta.subs(x,-2))
assert sp.expand(conic-(8181-(y+9)**2))==0
assert sp.factorint(8181)=={3:4,101:1}
assert 101%4==1

# The only simultaneous root of conic and d/dy conic away from 3 is p=101.
res=sp.resultant(conic,sp.diff(conic,y),y)
assert abs(int(res))==4*8181

# Symbolic first-order perturbation around a smooth branch Delta(x,y0)=0.
eps,eta=sp.symbols("eps eta")
y0=sp.symbols("y0")
expr=sp.expand(Delta.subs(y,y0+eps*eta)-Delta.subs(y,y0))
coeff=sp.expand(expr.coeff(eps,1))
assert coeff==eta*(-18-2*y0)

print("OK: A2 pure-cQ unsaturated angle-pair depth is locally smooth")
