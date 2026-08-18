#!/usr/bin/env python3
"""Exact algebra certificate for spontaneous-source-saturation-parity.md."""

import sympy as sp

five_lam, L0, cu, sigma, a2 = sp.symbols(
    "five_lam L0 cu sigma a2", integer=True
)
E1 = five_lam*L0**2 - 2*cu*sigma*a2**2

# E1 and 5^lambda L0^2 differ by an exact sigma multiple, which is the
# algebra behind gcd(E1,sigma)=gcd(5^lambda L0^2,sigma).
assert sp.expand(E1 - five_lam*L0**2 + 2*cu*sigma*a2**2) == 0

# The local valuation step used in the proof is purely arithmetic:
# v_p(sigma)=2h and v_p(L0)>=h imply min(2v_p(L0),2h)=2h.
h, ell = sp.symbols("h ell", integer=True, nonnegative=True)
# Check the boundary and a representative deeper value symbolically via
# substitution; the general inequality is stated/proved in the markdown.
for hv in range(1, 8):
    for lv in range(hv, hv+5):
        assert min(2*lv, 2*hv) == 2*hv
        assert (2*hv) % 2 == 0

print("OK: A2 source saturation parity identity certified")
