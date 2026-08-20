#!/usr/bin/env python3
"""Exact certificate for spontaneous-tangent-psif-overlap.md."""

import sympy as sp

ratio = sp.Rational(29, 18)
a_ratio = ratio - sp.Rational(55, 9)
assert a_ratio == -sp.Rational(9, 2)
assert sp.factor(ratio**2 - 26 + sp.Rational(7583, 324)) == 0
assert sp.factor(9 + 2*a_ratio) == 0

R23_ratio = sp.factor(2*a_ratio**2 + 9*a_ratio + 13)
assert R23_ratio == 13

source_ratio = -sp.Rational(7583, 1296)  # c_Q^2 XY / (A_f T)
R23f_ratio = sp.factor(R23_ratio + 2*source_ratio)
assert R23f_ratio == sp.Rational(841, 648)
assert R23f_ratio == sp.Rational(29**2, 2**3 * 3**4)

# Pure-channel alpha residue on 18K-29=0.
assert sp.factor((18*ratio-55) + 26) == 0

print("OK: A2 repeated spontaneous Psi_f overlap certified")
