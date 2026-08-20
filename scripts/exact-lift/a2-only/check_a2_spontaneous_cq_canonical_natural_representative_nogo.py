#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-canonical-natural-representative-nogo.md."""

import sympy as sp

# Symbols for the endpoint natural representative identity.
g, T, a3, eps, a2, cQ, p5d, kh = sp.symbols(
    "g T a3 eps a2 cQ p5d kh"
)
Y2 = a2*cQ*p5d
A3 = a3 + 3*T
high = g**2*kh/2

# Minus canonical residue: 5^lambda C = 3 g T modulo p^(2c).
minus_reduced = sp.expand(g*A3 + eps*Y2 - high - 3*g*T)
minus_target = sp.expand(g*a3 + eps*Y2 - high)
assert sp.expand(minus_reduced - minus_target) == 0

# Plus canonical residue: 5^lambda C = g(3T+2a3) modulo p^(2c).
plus_reduced = sp.expand(g*A3 + eps*Y2 - high - g*(3*T + 2*a3))
plus_target = sp.expand(-g*a3 + eps*Y2 - high)
assert sp.expand(plus_reduced - plus_target) == 0

# These are exactly high-2 equality after H0 = +/- ga3 modulo p^(2c).
Hminus = g*a3
Hplus = -g*a3
assert sp.expand((Hminus + eps*Y2 - high) - minus_target) == 0
assert sp.expand((Hplus + eps*Y2 - high) - plus_target) == 0

# Fixed 23 overlap: a3/T = 7, hence directed roots are +/-7T.
p = 23
assert (-16) % p == 7
assert (-7) % p == 16

print("OK: canonical C residue plus endpoint natural representative reduces to the existing high-2 directed root lock")
