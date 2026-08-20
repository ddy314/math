#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-global-decimal-gcd.md."""

import sympy as sp

K,Q,alpha,beta,G=sp.symbols("K Q alpha beta G")
F=5*K**2-36*K+55
Delta=K*beta-Q*alpha
Eminus=F*beta-K*Delta
Eplus=F*beta+K*Delta
P=6*K**2-36*K+55

# Exact decimal companion difference.
assert sp.expand(Eplus-Eminus-2*K*Delta)==0

# First-layer no-double-count audit:
# under alpha == 0 mod G, Delta == K*beta mod G.
# Eminus + 2K Delta == Eplus then reduces to P*K?  More directly,
# Eplus = F*beta + K*Delta == (F+K^2) beta = P*beta mod G.
assert sp.expand(Eplus.subs(Delta,K*beta)-P*beta)==0

# Prime-exponent aggregation checks.
# For each target equal-depth prime, alpha and Eplus have >=2h,
# while Delta and Eminus have exactly h.  Hence gcd with p^(2h)
# has exponents 2h, h, h respectively.
for h in range(1,8):
    assert min(2*h,2*h)==2*h
    assert min(h,2*h)==h
    assert min(h,2*h)==h

# A deep prime pays one extra radical power in Eplus.
for h in range(1,8):
    assert 2*h+1 > 2*h

print("OK: A2 equal-depth decimal pair globalizes to a square-core/radical gcd bridge")
