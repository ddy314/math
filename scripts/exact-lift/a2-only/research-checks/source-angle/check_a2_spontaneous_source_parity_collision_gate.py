#!/usr/bin/env python3
"""Certificate for spontaneous-source-parity-collision-gate.md."""

import sympy as sp

K,cu,z=sp.symbols("K cu z")
FH=5*K**2-36*K+55
BW=cu**2*FH+z**2*K**2
DW=55*z**2-49*cu**2
P=6*K**2-36*K+55

assert sp.expand(55*BW-K**2*DW-cu**2*(18*K-55)**2)==0
assert sp.expand((18*K-55)-9*(2*K-9)-26)==0
assert sp.factor(sp.resultant(P,18*K-55,K))==330
assert sp.factor((18**2)*P.subs(K,sp.Rational(55,18)))==330

# Only odd divisor of 26 is 13, and it is split mod 4.
assert sp.factorint(26)=={2:1,13:1}
assert 13%4==1

print("OK: A2 B_W/D_W parity reuse is confined to the noncentral linear sheet 18K-55")
