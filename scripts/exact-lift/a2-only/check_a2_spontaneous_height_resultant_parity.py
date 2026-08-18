#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-resultant-parity.md."""

import sympy as sp

K,cu,q,z,g,omega,W,T=sp.symbols("K cu q z g omega W T")
u,s=sp.symbols("u s")  # u=2^m, s=5^d
F=5*K**2-36*K+55
BW=cu**2*F+z**2*K**2

# B_W mod 8: K=2 mod4, cu,z odd.
for kr in (2,6):
    for cr in (1,3,5,7):
        for zr in (1,3,5,7):
            assert int(BW.subs({K:kr,cu:cr,z:zr}))%8==7

# Primitive J_H bridge reconstructed in source variables.
# 5^(2d) Jhat = u^2 s^2 cu^2 g^2 F - q^2(cu^2 W^2-g^2 a3^2)
a3=omega*W-T*K
Jscaled=sp.expand(u**2*s**2*cu**2*g**2*F-q**2*(cu**2*W**2-g**2*a3**2))
# T=u*s*z/q because z=q*5^lambda and T=u*s*5^lambda.
# Avoid division: verify after substituting q*T=u*s*z.
expr=sp.expand(Jscaled-u**2*s**2*g**2*BW-q**2*W*((g**2*omega**2-cu**2)*W-2*g**2*omega*T))
# Replace z^2 using q^2*T^2/(u^2*s^2), equivalently clear u^2 s^2.
cleared=sp.expand(u**2*s**2*expr)
cleared=sp.expand(cleared.subs(z**2,q**2*T**2/(u**2*s**2)))
assert sp.cancel(cleared)==0

# The bracket linearizes using z=g*omega-cu, f=g*omega+cu and qW=DK-N.
D,N,f=sp.symbols("D N f")
R=(g**2*omega**2-cu**2)*W-2*g**2*omega*T*K
# qR + z(D z K + fN)=0 under qW=DK-N, z=q*5^lambda,
# D=g*u*s, T=u*s*5^lambda and f=g omega+cu.
v=sp.symbols("v") # 5^lambda
lin=sp.expand(q*R + z*(D*z*K+f*N))
lin=lin.subs({W:(D*K-N)/q,z:q*v,D:g*u*s,T:u*s*v,f:g*omega+cu})
assert sp.factor(lin)==0

print("OK: A2 height-resultant parity pair and J/B bridge certified")
