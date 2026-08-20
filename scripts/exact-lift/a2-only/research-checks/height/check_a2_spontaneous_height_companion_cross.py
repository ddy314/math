#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-companion-cross.md."""

import sympy as sp

K,D,N,cu,z,f=sp.symbols("K D N cu z f")
AW=5*cu**2+z**2
BW=sp.expand(AW*K**2-36*cu**2*K+55*cu**2)
L=D*z*K+f*N
R=sp.expand(55*D**2*cu**2*z**2+36*D*N*cu**2*f*z+N**2*f**2*AW)

assert sp.factor(sp.resultant(BW,L,K)-R)==0

completion=sp.expand(AW*R-(AW*f*N+18*D*cu**2*z)**2-D**2*cu**2*z**2*(55*z**2-49*cu**2))
assert completion==0

assert sp.factor(sp.discriminant(sp.Poly(R,N))) == -4*D**2*cu**2*f**2*z**2*(55*z**2-49*cu**2)

# Linearization of the J/B difference bracket.
g,omega,W,q,u,s,v=sp.symbols("g omega W q u s v")
T=u*s*v
Dexpr=g*u*s
zexpr=q*v
fexpr=g*omega+cu
br=(g**2*omega**2-cu**2)*W-2*g**2*omega*T*K
expr=sp.expand(q*br+zexpr*(Dexpr*zexpr*K+fexpr*N))
expr=sp.expand(expr.subs(W,(Dexpr*K-N)/q))
expr=sp.factor(expr.subs(g**2*omega**2-cu**2,(g*omega-cu)*(g*omega+cu)))
assert expr==0

print("OK: A2 J/B cross linear gate and positive norm certified")
