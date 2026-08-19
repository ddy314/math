#!/usr/bin/env python3
"""Certificate for spontaneous-crt-q-descent-separation.md."""

import sympy as sp

K, delta = sp.symbols("K delta")
Fq = 32*delta*K - 144*delta + K**2 - 384*K + 432
reduced = sp.factor(Fq.subs(delta, 3-K))
assert reduced == -K*(31*K+144)

res = sp.factor(sp.resultant(K**2-26, 31*K+144, K))
assert res == -4250
assert sp.factorint(abs(int(res))) == {2: 1, 5: 3, 17: 1}
assert 17 % 4 == 1
assert 4250 % 11 != 0
assert 4250 % 23 != 0

print("OK: saturated q-denominator inert support is disjoint from descendant common support")
