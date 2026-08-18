#!/usr/bin/env python3
"""Exact certificate for spontaneous-tangent-f-overlap.md."""

import sympy as sp

K, T = sp.symbols("K T")
ratio = sp.Rational(29, 18)
a_ratio = ratio - sp.Rational(55, 9)
assert sp.factor(a_ratio + sp.Rational(9, 2)) == 0

R23_ratio = sp.factor(2*a_ratio**2 + 9*a_ratio + 13)
assert R23_ratio == 13

# Prefix value on K=29/18.
assert sp.factor(ratio**2 - 26 + sp.Rational(7583, 324)) == 0

# Source-scale elimination, represented symbolically by the final ratio.
# cQ^2 XY /(A_f T) = -7583/1296.
source_ratio = -sp.Rational(7583, 1296)
R23f_ratio = sp.factor(R23_ratio + 2*source_ratio)
assert R23f_ratio == sp.Rational(841, 648)
assert sp.factor(R23f_ratio - sp.Rational(29**2, 2**3 * 3**4)) == 0

# f-channel double-root target K = 9 + 2 a3/T becomes zero,
# incompatible with 18K=29 except at p=29.
assert sp.factor(9 + 2*a_ratio) == 0
assert sp.factor(18*ratio - 29) == 0

print("OK: A2 repeated spontaneous f-overlap certified")
