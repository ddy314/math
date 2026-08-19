#!/usr/bin/env python3
"""Certificate for spontaneous-crt-f-descent-separation.md."""

import sympy as sp

K = sp.symbols("K")
Pf = 3*K**2 - 36*K + 26
GD = 11*K**2 - 240*K + 432

# Saturated f-allocation substituted into the descendant equation.
expr = sp.expand(32*(K-6)*K - 144*(K-6) + K**2 - 384*K + 432)
assert sp.factor(expr) == 3*GD

res = sp.factor(sp.resultant(Pf, GD, K))
assert res == -1996988
assert sp.factorint(abs(int(res))) == {2: 2, 7: 1, 73: 1, 977: 1}
assert 7 % 4 == 3
assert 73 % 4 == 1
assert 977 % 4 == 1

roots7 = [k for k in range(7) if int(Pf.subs(K,k)) % 7 == 0 and int(GD.subs(K,k)) % 7 == 0]
assert roots7 == [1]

# At K=1, delta=K-6=-5=2 mod7; hence N/D=3-delta=1 and DK-N=0 mod7.
assert (1 - 6) % 7 == 2
assert (3 - 2) % 7 == 1
assert (1*1 - 1) % 7 == 0

print("OK: saturated f-denominator descendant overlap reduces to a single transverse height-7 label")
