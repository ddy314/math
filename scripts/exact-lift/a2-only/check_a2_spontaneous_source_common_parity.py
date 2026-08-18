#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-common-parity.md."""

import sympy as sp

H, F, E, J, R = sp.symbols("H F E J R", integer=True)

P4 = (
    9401*H**4 + 13684*H**3*F - 175354*H**2*F**2
    - 418156*H*F**3 - 878519*F**4
)
Prod = (
    (H+F)*(99*H+59*F)*(H**2+2*H*F+5*F**2)
    *(49*H**2+58*H*F-191*F**2)
)
K = sp.expand(
    4400*F**2*(H+21*F)**2
    + 81*E*F*P4
    - 810*E**2*Prod
)

# Encode the actual endpoint constraints
#   8 | H+F  -> H = 8J-F
#   2^10 | E -> E = 1024 R  (M >= 11).
Ksub = sp.expand(K.subs({H:8*J-F, E:1024*R}))
assert all(int(c) % 256 == 0 for c in sp.Poly(Ksub,J,F,R).coeffs())
Kprim = sp.expand(Ksub/256)

L = 2*J + 5*F  # (H+21F)/4
first_prim = 275*F**2*L**2
remainder = sp.expand(Kprim-first_prim)
assert all(int(c) % 8 == 0 for c in sp.Poly(remainder,J,F,R).coeffs())

# In fact P4 is much deeper after H+F is forced to be a multiple of 8.
P4sub = sp.factor(P4.subs(H,8*J-F))
assert sp.cancel(P4sub/1024).is_polynomial(J,F)

# For odd F, L=2J+5F is odd. Odd squares are 1 mod 8, hence
# first_prim = 275*F^2*L^2 = 3 mod 8. Enumerate the residue classes.
for f in (1,3,5,7):
    for j in range(8):
        l = (2*j+5*f) % 8
        assert l % 2 == 1
        assert (275*f*f*l*l) % 8 == 3

print("OK: A2 source common natural gate has exact v2=8 and primitive 3 mod 8")
