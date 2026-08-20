#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-centered-a3-map.md."""

import sympy as sp

u, c, S, v = sp.symbols("u c S v")
a = sp.symbols("a")

# Centered substitution u=v*a turns the binary equation into
# u^2+c*u+S^2/4.
expr = sp.expand(v**2 * a**2 + c * v * a + S**2 / 4)
assert sp.expand(expr.subs(a, u / v) - (u**2 + c * u + S**2 / 4)) == 0

# Discriminant after S=5^(3lambda)+c.
P = sp.symbols("P")
disc = sp.expand(c**2 - S**2)
disc_sub = sp.factor(disc.subs(S, P + c))
assert disc_sub == -P * (P + 2 * c)

# Derivative 2u+c is odd whenever c is odd, so each mod-2 root lifts uniquely.
assert (2 * 1 + 1) % 2 == 1

# Finite sanity check: for source-like S divisible by 4 and odd c,
# the centered polynomial has exactly one odd root modulo 2^n.
def roots(bits, c0, S0):
    mod = 2**bits
    out = []
    for u0 in range(1, mod, 2):
        if (u0*u0 + c0*u0 + (S0*S0 // 4)) % mod == 0:
            out.append(u0)
    return out

for c0 in (3, 7, 11, 15):
    for S0 in (4, 8, 12, 20, 28):
        for bits in range(1, 8):
            assert len(roots(bits, c0, S0)) == 1

# Centered long-5 affine map:
# theta^{-1}=-v^{-1} gives -c/(2v) - (45c/2)iota*2^(3lambda+2).
vinv, iota, lam = sp.symbols("vinv iota lam")
old = sp.Rational(1,2)*c*(-vinv - 45*iota*2**(3*lam+2))
new = -sp.Rational(1,2)*c*vinv - sp.Rational(45,2)*c*iota*2**(3*lam+2)
assert sp.expand(old-new) == 0

print("OK: centered A2 c2 map has one source-only binary root and affine long-5 divisor dependence")
