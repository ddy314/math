#!/usr/bin/env python3
"""Certificate for spontaneous-crt-dual-gap-mobius.md."""

import sympy as sp
from fractions import Fraction as F

D,C,K,q,W = sp.symbols("D C K q W")
As = 2*q*W-2*D-C
Bs = 2*q*W-4*D-C
source_rel = {q*W: D*K-(3*D-C)}
assert sp.expand(As.subs(source_rel) - (2*D*(K-4)+C)) == 0
assert sp.expand(Bs.subs(source_rel) - (2*D*(K-5)+C)) == 0
assert sp.expand((As-Bs).subs(source_rel) - 2*D) == 0

# Full-5 residues differ by curvature -4 D c_u^2 a_3.
cu,a = sp.symbols("cu a")
Rp = cu**2*a*(D*(20-4*K)-2*C)
Rm = cu**2*a*(D*(16-4*K)-2*C)
assert sp.expand(Rm-Rp) == -4*D*cu**2*a
assert sp.expand(Rm + 2*cu**2*a*As.subs(source_rel)) == 0
assert sp.expand(Rp + 2*cu**2*a*Bs.subs(source_rel)) == 0

# Safe Archimedean inequalities. It suffices to check their algebraic thresholds.
# 30(2K-15)/K^2 > 59/K iff K>450.
assert sp.expand(30*(2*K-15)-59*K) == K-450
# 59/K - 1/(K-5) > 57/K iff K>10.
# Cross-multiplying positive K(K-5): 2(K-5)>K.
assert sp.expand(2*(K-5)-K) == K-10

# Cross determinant factorization.
Dm,Dp,A,B = sp.symbols("Dm Dp A B")
E = Dm*B-Dp*A
ratio_form = sp.factor(E - Dp*B*(Dm/Dp-A/B))
assert ratio_form == 0

# The coarse (6,10) window follows from rational constants, with K huge.
# Lower coefficient before (1-5/K): 114/17 > 6.
assert F(114,17) > 6
# Upper coefficient before (1-4/K): 136/15 < 10.
assert F(136,15) < 10

print("OK: A2 dual gaps synchronize with the source Mobius ratio modulo full 5-depth")
