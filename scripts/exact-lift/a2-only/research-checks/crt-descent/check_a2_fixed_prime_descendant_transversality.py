#!/usr/bin/env python3
"""Certificate for fixed-prime-descendant-transversality.md."""

import sympy as sp

K = sp.symbols("K", integer=True)
L23 = 2 * K - 9
GD = 11 * K**2 - 240 * K + 432

# Exact Bezout identity between the height/saturation center and the old
# descendant-height gate.
assert sp.expand(4 * GD - (11 * L23**2 - 282 * L23 - 1701)) == 0
assert sp.factorint(1701) == {3: 5, 7: 1}

# Hence every non-3 common prime is forced to p=7, and common p-adic depth
# can never reach 7^2.
assert sp.factor(GD.subs(K, sp.Rational(9, 2))) == -sp.Rational(1701, 4)

# Mod-7 / mod-49 Hensel audit for G_D.
roots7 = [k for k in range(7) if int(GD.subs(K, k)) % 7 == 0]
roots49 = [k for k in range(49) if int(GD.subs(K, k)) % 49 == 0]
assert roots7 == [1, 3]
assert roots49 == [8, 45]

# The central root 2K-9=0 has the distinct lift K=29 mod49.
central49 = [k for k in range(49) if (2 * k - 9) % 49 == 0]
assert central49 == [29]
assert 29 not in roots49

# The two genuine fixed-7 asymmetric angle/denominator continuations from
# fixed-prime-asymmetric-lifts.md.  Recover K=(y+9)/tau modulo 49.
fixed7_lifts = [
    (39, 48, 29),  # height-deep, additive shallow
    (25, 34, 22),  # additive-deep, height shallow
]
fixed7_K = []
for x, y, tau in fixed7_lifts:
    kval = (y + 9) * pow(tau, -1, 49) % 49
    fixed7_K.append(kval)
assert fixed7_K == [29, 22]

# Neither continuation can simultaneously carry descendant G_D to depth 2.
for kval in fixed7_K:
    assert int(GD.subs(K, kval)) % 49 != 0

# At the exact height center, the only non-3 prime in G_D is 7.  Thus the
# other fixed height/common labels 23,43 (and angle-only 199) are separated
# already in the first layer from the G_D gate.
for p in (23, 43, 199):
    assert 1701 % p != 0

print(
    "OK: A2 central/fixed-height support meets the descendant G_D gate only "
    "at a single transverse 7-layer; the genuine fixed-7 p^2 branches are disjoint"
)
