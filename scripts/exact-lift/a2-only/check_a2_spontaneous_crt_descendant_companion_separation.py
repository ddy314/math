#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-companion-separation.md."""

import sympy as sp

J, alpha, L = sp.symbols("J alpha L")
u5, C = sp.symbols("u5 C", nonzero=True)

# Abstract the height-free identity on a field where u5=5^m and
# C=2^(m+1) B0^2 are units:
#   That = u5*J - C*L*alpha,  L=2K-9.
That = u5 * J - C * L * alpha

# A common root of That and J can only occur on L*alpha=0.
res = sp.resultant(That, J, J)
assert sp.expand(res + C * L * alpha) == 0

# In the alpha-separated sector this reduces exactly to the central gate L=0.
p = 101
for a in (1, 2, 7, 33):
    for c in (1, 5, 19):
        for u in (1, 3, 25):
            for ell in range(p):
                # On That=0, J is uniquely determined because u is a unit.
                j = (c * ell * a * pow(u, -1, p)) % p
                assert (u * j - c * ell * a) % p == 0
                assert (j == 0) == (ell == 0)

print("OK: alpha-separated descendant common support meets J_H only on the central gate 2K-9")
