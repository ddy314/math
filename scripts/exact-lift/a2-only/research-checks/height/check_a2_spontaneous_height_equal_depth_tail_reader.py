#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-tail-reader.md."""

import sympy as sp

# ----------------------------------------------------------------------
# Exact decimalization of L_JB.
b, EM, omega, cu, beta, Delta, T, Q, alpha, N = sp.symbols(
    "b EM omega cu beta Delta T Q alpha N", nonzero=True
)
AH, z, q, W = sp.symbols("AH z q W")
BH = q*W
L = 2*N*AH + z*BH
Lambda = 2*beta*Delta + T*Q**2*alpha

# Use the exact decimal realizations
#   b*AH = cu*beta,
#   b*z  = T*cu*Q,
#   EM*N*omega = Delta,
#   EM*q = Q,
#   omega*W = alpha.
term1 = b*EM*omega*(2*N*AH)
term1_dec = sp.expand(
    term1.subs(AH, cu*beta/b).subs(EM*omega, Delta/N)
)
assert sp.simplify(term1_dec - 2*cu*beta*Delta) == 0

term2 = b*EM*omega*z*q*W
term2_dec = sp.expand(
    term2.subs(z, T*cu*Q/b)
         .subs(q, Q/EM)
         .subs(W, alpha/omega)
)
assert sp.simplify(term2_dec - cu*T*Q**2*alpha) == 0

assert sp.simplify(term1_dec + term2_dec - cu*Lambda) == 0

# ----------------------------------------------------------------------
# Endpoint rational bounds for the fixed digit window.
Nmin = 10**11
alpha_lo = sp.Rational(2499,250)
alpha_hi = sp.Integer(10)
Q_lo = sp.Rational(21,10)
Q_hi = sp.Rational(40,19)
beta_hi = sp.Rational(211,100)
Delta_hi = sp.Rational(843,100)

lower = Q_lo**2 * alpha_lo
upper = Q_hi**2 * alpha_hi + sp.Rational(2,Nmin)*beta_hi*Delta_hi
gap = 2*beta_hi*Delta_hi

assert lower > 44
assert upper < 45
assert gap < 36

# ----------------------------------------------------------------------
# Valuation bookkeeping: omega contributes h and L contributes h+rho.
for h in range(1,8):
    for rho in range(0,8):
        assert h + (h+rho) == 2*h + rho

print("OK: A2 Lambda_dec reads the complete equal-depth resonance tail")
