#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-source-tail-nogo.md."""

import sympy as sp

# Source split and source triangle imply the theta identities exactly.
cQ,q,Mpow,D0,cu,g,omega,lam_pow,two_m=sp.symbols(
    "cQ q Mpow D0 cu g omega lam_pow two_m"
)
# Mpow = 5^M, lam_pow = 5^lambda, D0 = 2^m g, two_m=2^m.

# Substitute cQ*q = Mpow + D0*cu and g*omega = lam_pow*q + cu.
expr = sp.expand(g*cQ*omega - (Mpow*lam_pow + cQ*cu + lam_pow*D0*cu))
expr = expr.subs(g*omega, lam_pow*q + cu)
expr = sp.expand(expr.subs(cQ*q, Mpow + D0*cu))
assert expr == 0

# theta := cQ*omega - 2^m*5^lambda*cu.
theta = cQ*omega-two_m*lam_pow*cu
expr2 = sp.expand(g*theta-(Mpow*lam_pow+cQ*cu))
expr2 = sp.expand(expr2.subs(g*omega,lam_pow*q+cu))
expr2 = sp.expand(expr2.subs(cQ*q,Mpow+D0*cu))
expr2 = sp.expand(expr2.subs(D0,two_m*g))
assert expr2==0

# Converse: theta equations + source triangle recover source split.
# g*theta = 5^(M+lambda)+cQ*cu and cQ*omega-theta=2^m*5^lambda*cu
# imply lam_pow*(cQ*q-D0*cu-Mpow)=0.
recover = sp.expand(
    cQ*(lam_pow*q+cu)
    -g*two_m*lam_pow*cu
    -(Mpow*lam_pow+cQ*cu)
)
recover = sp.expand(recover.subs(g*two_m,D0))
assert sp.factor(recover)==lam_pow*(cQ*q-D0*cu-Mpow)

# Normalized 23^h tail bridge is just Q=2^(M+1)cQ*q plus rho=q*5^lambda/cu.
Qtilde,ctilde,two_M1,rho=sp.symbols("Qtilde ctilde two_M1 rho")
# Qtilde = two_M1*(cQ/23^h)*q, ctilde=(cQ/23^h)*cu.
cbar=sp.symbols("cbar")
bridge=sp.expand(lam_pow*(two_M1*cbar*q)-two_M1*(q*lam_pow/cu)*(cbar*cu))
assert bridge==0

print("OK: A2 pure-cQ theta/tail equations are algebraically dependent on source split and source triangle")
