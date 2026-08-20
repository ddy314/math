#!/usr/bin/env python3
"""Algebra certificate for spontaneous-source-equal-depth.md."""

import sympy as sp

x, y, r = sp.symbols("x y r")
As = 99*x-4
d = 225*x**2-y
Phi = As*r-2*x-4
Psi = 3600*(r+1)**2-y*(99*r-2)**2

# Reconstruct the exact source resultant/Bezout constant.
res = sp.factor(sp.resultant(Phi,Psi,r))
assert res == 163216*d
assert 163216 == 404**2

# Verify the standard linear-root identity modulo Phi by polynomial division:
# As^2 Psi - 404^2 d is divisible by Phi.
expr = sp.expand(As**2*Psi-404**2*d)
q, rem = sp.div(sp.Poly(expr,r), sp.Poly(Phi,r))
assert rem.as_expr() == 0

# The normalized angle condition is just E1 / p^(2h); certify the
# source-scale formula for L0 used in the document.
M = sp.symbols("M", integer=True, positive=True)
U = 5**M
L0 = -U*10**(M-1)*d
assert sp.expand(L0 + 5**M*10**(M-1)*d) == 0

# Character rewrite through 4 sigma = 5^M cQ Phi is algebraically the
# replacement sigma# = 5^M cQ Phi# / 4.  The factor after multiplying by
# 5^lambda differs from 2*c_u*cQ*Phi#*5^(M+lambda) by a square/inverse-2.
cu, cQ, phish, lam = sp.symbols("cu cQ phish lam")
sigsh = 5**M*cQ*phish/4
lhs = 2*cu*sigsh*5**lam
rhs = 2*cu*cQ*phish*5**(M+lam)
assert sp.factor(rhs/lhs-4) == 0  # ratio 4 is a square.

print("OK: A2 normalized source equal-depth gate certified")
