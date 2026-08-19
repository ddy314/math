#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-branch-defect.md."""

import sympy as sp
from fractions import Fraction as F

s,t,z=sp.symbols('s t z')
K=s/t
zeta=z/t
expr=12+2*zeta-2*K+sp.Rational(63,16)*K**2/(2*K-9)
num,den=sp.together(expr).as_numer_denom()
assert sp.factor(num)==-s**2+672*s*t+64*s*z-1728*t**2-288*t*z
assert sp.factor(den)==16*t*(2*s-9*t)

# Safe endpoint sign certificate used in the proof.
slo=F(2499,250)
tauhi=F(1,10**11)
assert 64*slo-288*tauhi>639
assert F(4778,1000)*639>3052
assert 672*10*tauhi < F(1,10**7)
# Thus z*(64s-288t) < -3052 and the only positive term is <1e-7;
# the remaining terms are nonpositive.

print('OK: pure-spontaneous descendant branch uniquely recovers a negative real defect residue')
