#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-resonance.md."""

import sympy as sp

N,z,cu,D,K,q,W,g,omega,alpha=sp.symbols(
    "N z cu D K q W g omega alpha"
)
AH=z+cu
BH=D*K-N
L=2*N*AH+z*BH

# Canonical identifications A_H=g*omega and B_H=qW.
assert sp.expand(AH.subs(z,g*omega-cu)-g*omega)==0
assert sp.expand(BH.subs(N,D*K-q*W)-q*W)==0

# L_JB = DzK + fN with f=z+2cu.
f=z+2*cu
L_original=D*z*K+f*N
assert sp.expand(L_original-L)==0

# Product identity A_H B_H = g q alpha after alpha=omega W.
prod=sp.expand(
    (AH*BH).subs({z:g*omega-cu,N:D*K-q*W,alpha:omega*W})
    -g*q*alpha.subs(alpha,omega*W)
)
assert prod==0

# Exact quadratic identity and square discriminant.
quad=2*N*AH**2-L*AH+z*g*q*alpha
quad_sub=sp.expand(
    quad.subs({z:g*omega-cu,N:D*K-q*W,alpha:omega*W})
)
assert sp.factor(quad_sub)==0

M=2*N*AH-z*BH
disc=sp.expand(L**2-8*N*z*AH*BH)
assert sp.expand(disc-M**2)==0

# Replacing AH*BH by g*q*alpha gives the documented form.
disc_alpha=sp.expand(L**2-8*N*z*g*q*alpha)
disc_alpha_sub=sp.expand(
    disc_alpha.subs({z:g*omega-cu,N:D*K-q*W,alpha:omega*W})
)
M_sub=sp.expand(M.subs({z:g*omega-cu,N:D*K-q*W}))
assert sp.factor(disc_alpha_sub-M_sub**2)==0

print("OK: A2 equal-depth omega-height resonance reduces to a square-shadow unit ratio")
