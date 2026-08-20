#!/usr/bin/env python3
"""Certificate for spontaneous-crt-height-descent-overlap.md."""

import sympy as sp

K,u,z,c = sp.symbols("K u z c")
GD = 11*K**2 - 240*K + 432
FH = 5*K**2 - 36*K + 55
BW = FH + u*K**2

res_u = sp.factor(sp.resultant(GD, BW, K))
assert res_u == 186624*u**2 + 779040*u + 527017

# z=0 branch.
res0 = sp.factor(sp.resultant(GD, FH, K))
assert res0 == 527017
assert sp.factorint(res0) == {17: 1, 29: 1, 1069: 1}
assert all(p % 4 == 1 for p in (17,29,1069))

H67 = 186624*z**4 + 779040*z**2*c**2 + 527017*c**4
completion = (1296*z**2 + 2705*c**2)**2 - 67*(196*c**2)**2
assert sp.expand(9*H67 - completion) == 0
assert 2705**2 - 67*196**2 == 9*527017

# Ramified 67 value is u=63, which is a non-square.
p = 67
u67 = (-2705 * pow(1296, -1, p)) % p
assert u67 == 63
assert pow(u67, (p-1)//2, p) == p-1

# Triple source-common/height/descent overlap.
LS = 18*K - 55
resS = sp.factor(sp.resultant(GD, LS, K))
assert resS == -64357
assert sp.factorint(abs(int(resS))) == {139: 1, 463: 1}
for p,root in [(139,88),(463,286)]:
    assert p % 4 == 3
    assert int(GD.subs(K,root)) % p == 0
    assert int(LS.subs(K,root)) % p == 0

print("OK: height/descent common support carries fixed-67 orientation; 67 ramified branch is empty")
