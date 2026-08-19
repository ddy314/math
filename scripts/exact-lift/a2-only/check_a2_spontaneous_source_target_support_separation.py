#!/usr/bin/env python3
"""Certificate for spontaneous-source-target-support-separation.md."""

import sympy as sp
K=sp.symbols("K")
P=6*K**2-36*K+55
L=18*K-55
assert sp.resultant(P,L,K)==330
assert sp.factorint(330)=={2:1,3:1,5:1,11:1}
assert 180*98==17640
print("OK: A2 source-common and equal-depth target moving supports meet only at fixed 3/5/11")
