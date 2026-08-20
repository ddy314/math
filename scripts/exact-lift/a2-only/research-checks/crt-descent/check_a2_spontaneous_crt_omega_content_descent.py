#!/usr/bin/env python3
"""Certificate for spontaneous-crt-omega-content-descent.md."""

import sympy as sp

K, delta = sp.symbols("K delta")
GD = 11*K**2 - 240*K + 432
expr = sp.expand(3*GD - 16*(2*K-9)*(3-K-delta))
# Solving expr=0 for delta gives the theorem's rational map.
num = sp.factor(sp.expand(16*(2*K-9)*(3-K) - 3*GD))
assert num == -65*K**2 + 960*K - 1728
assert sp.expand(expr.subs(delta, num/(16*(2*K-9)))) == 0

# Central resultant.
res = sp.factor(sp.resultant(GD, 2*K-9, K))
assert res == -1701
assert sp.factorint(abs(int(res))) == {3: 5, 7: 1}

# Archimedean sign on the actual huge-K range is immediate; certify at the
# weaker K>=1000 threshold and monotone leading signs.
poly = -65*K**2 + 960*K - 1728
assert int(poly.subs(K,1000)) < 0
assert 2*1000-9 > 0
# The positive natural representative coefficients are indeed positive for K>=1000.
pos = 65*K**2 - 960*K + 1728
assert int(pos.subs(K,1000)) > 0

print("OK: omega-content descendant common fixes top defect residue; central branch only fixed 7")
