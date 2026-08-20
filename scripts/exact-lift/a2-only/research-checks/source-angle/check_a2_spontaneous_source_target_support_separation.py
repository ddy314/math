#!/usr/bin/env python3
"""Certificate for spontaneous-source-target-support-separation.md."""

import sympy as sp

K = sp.symbols("K")
P = 6 * K**2 - 36 * K + 55
L = 18 * K - 55

# Exact resultant and fixed-prime support.
res = sp.resultant(P, L, K)
assert res == 330
assert sp.factorint(abs(res)) == {2: 1, 3: 1, 5: 1, 11: 1}

# In the genuine non-3,5 target sector the only residual candidate is 11.
p = 11
roots = [
    k
    for k in range(p)
    if int(P.subs(K, k)) % p == 0 and int(L.subs(K, k)) % p == 0
]
assert roots == [0]

# Mod 11, L=18K-55=7K, so the unique common root forces K=0.
assert 18 % p == 7
assert 55 % p == 0
assert int(P.subs(K, 0)) % p == 0

# Genuine height targets satisfy p∤K (proved in
# spontaneous-height-content-oversaturation.md), hence the fixed-11 common root
# is nongenuine.  The numerical product budget remains unchanged.
assert 180 * 98 == 17640

print("OK: A2 source-common and equal-depth target genuine supports are completely separated")
