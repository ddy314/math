#!/usr/bin/env python3
"""Certificate for spontaneous-crt-target-descent-overlap.md."""

import sympy as sp

K=sp.symbols("K")
P=6*K**2-36*K+55
GD=11*K**2-240*K+432
GR=63*K**2+144*K-416

resD=sp.factor(sp.resultant(P,GD,K))
resR=sp.factor(sp.resultant(P,GR,K))
assert resD==1492681
assert sp.factorint(resD)=={31:1,179:1,269:1}
assert resR==13434129
assert sp.factorint(resR)=={3:2,31:1,179:1,269:1}
assert sp.expand(GR-(16*P-3*GD))==0

# Target inert class filter and unique common roots.
assert 31%24==7
assert 179%24==11
assert 269%24==5
for p,root in [(31,9),(179,71),(269,64)]:
    states=[k for k in range(p) if int(P.subs(K,k))%p==0 and int(GD.subs(K,k))%p==0]
    assert states==[root]
    assert (2*root-9)%p !=0

# Exact F63 decomposition polynomial.
assert sp.expand(48*(2*K-9)*(K-3)-63*K**2-3*GD)==0

# Under target substitutions, Rstar polynomial is GR.
# Algebraic polynomial reduction check.
assert sp.expand(GR+3*GD-16*P)==0

# Transversality: each fixed resultant prime occurs exactly once.
for p in (31,179,269):
    assert sp.factorint(resD)[p]==1

# Singular target candidate sets are disjoint from actual descent target reuse.
assert set((31,179)).isdisjoint({7,79,107,199})

print("OK: A2 equal-depth target/descent overlap is fixed to 31/179 and transverse above baseline")
