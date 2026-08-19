#!/usr/bin/env python3
"""Certificate for spontaneous-crt-source-descent-overlap.md."""

from fractions import Fraction as F
import sympy as sp

K,T,g,a,C,Lam = sp.symbols("K T g a C Lam")
F63 = (
    16*(2*K-9)*(g*((2*K-12)*T-2*a)+Lam*C)
    -63*g*T*K**2
)
LS = 18*K-55
H = 102383*g*T - 29952*g*a + 14976*C*Lam

# Exact linear resultant.
assert sp.factor(sp.resultant(F63, LS, K)) == -H

# Coefficient factorizations.
assert sp.factorint(14976) == {2: 7, 3: 2, 13: 1}
assert sp.factorint(29952) == {2: 8, 3: 2, 13: 1}
assert sp.factorint(102383) == {43: 1, 2381: 1}
assert 102383 % 13 == 8

# Endpoint normalized interval for H/(gT).
zeta_hi = F(251,250)
delta_hi = F(3,250)
lo = F(102383) - F(29952)*zeta_hi
hi = F(102383) - F(29952) + F(14976)*delta_hi
assert lo == F(9038899,125)
assert hi == F(9076339,125)
assert F(72311) < lo < hi < F(72611)

# Source sheet length bound follows from 0<K<10N.
# Here just certify the coefficient arithmetic used for 18K-55<180N.
assert 18*10 == 180

print("OK: source/descent overlap lies on short H_S63 carrier and fixed 13 is excluded")
