#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-prefix-simple.md."""

import sympy as sp

E, F, H, e = sp.symbols("E F H e")

B = E*(F+H)
A0 = 9*E*F
C0 = sp.Rational(9,2)*B
a2 = E*F - e
Dsrc = sp.expand(C0**2 - A0*a2)

expected = sp.expand(
    sp.Rational(9,4)*E**2*(5*F**2 + 18*F*H + 9*H**2)
    + 9*E*F*e
)
assert sp.expand(Dsrc - expected) == 0
assert sp.diff(Dsrc, e) == 9*E*F

# Cleared linear source residue.
cleared = sp.expand(4*Dsrc/(9*E))
assert sp.expand(
    cleared
    - (E*(5*F**2 + 18*F*H + 9*H**2) + 4*F*e)
) == 0

# The common gate is independent of e, so eliminating e is tautological.
P4 = (
    9401*H**4 + 13684*H**3*F - 175354*H**2*F**2
    - 418156*H*F**3 - 878519*F**4
)
Prod = (
    (H+F)*(99*H+59*F)*(H**2+2*H*F+5*F**2)
    *(49*H**2+58*H*F-191*F**2)
)
Ksrc = sp.expand(
    4400*F**2*(H+21*F)**2
    + 81*E*F*P4
    - 810*E**2*Prod
)
assert sp.diff(Ksrc, e) == 0
assert sp.resultant(Dsrc, Ksrc, e) == Ksrc

print("OK: A2 source prefix simple lift and resultant no-go certified")
