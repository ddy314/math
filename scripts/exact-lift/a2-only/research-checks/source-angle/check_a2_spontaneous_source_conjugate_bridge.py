#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-conjugate-bridge.md."""

import sympy as sp

H,E,F,e = sp.symbols("H E F e")
S = E*F
A = S-e

P4 = (
    9401*H**4 + 13684*H**3*F - 175354*H**2*F**2
    - 418156*H*F**3 - 878519*F**4
)
Prod = (
    (H+F)*(99*H+59*F)*(H**2+2*H*F+5*F**2)
    *(49*H**2+58*H*F-191*F**2)
)
K = sp.expand(
    4400*F**2*(H+21*F)**2
    + 81*E*F*P4
    - 810*E**2*Prod
)
Kvee = sp.expand(K.subs(H,-H-2*F))

Esc = sp.expand(
    -194040*A**3 - 108360*A**2*S + 84609*A**2
    + 14742000*A*S**2 - 3240000*A*S + 1100*A
    - 29160000*S**2 + 990000*S
)
Osc = sp.expand(
    2960*A**2 + 17640*A*S - 2691*A
    - 81000*S**2 - 16200*S + 550
)
Rsrc = sp.expand(Esc**2 - 14400*A*S*Osc**2)

Dlin = sp.expand(E*(5*F**2+18*F*H+9*H**2)+4*F*e)
Dsrc = sp.Rational(9,4)*E*Dlin
assert sp.factor(Dsrc - (
    sp.Rational(9,4)*E**2*(5*F**2+18*F*H+9*H**2)+9*E*F*e
)) == 0

bridge = sp.expand(81*E**2*K*Kvee - 256*F**6*Rsrc)
q,rem = sp.div(sp.Poly(bridge,H,e,E,F),sp.Poly(Dlin,H,e,E,F))
assert rem.as_expr() == 0
assert len(q.terms()) == 90

# The normalized scaling constant is exactly 256/81.
assert sp.Rational(10**8,5625**2) == sp.Rational(256,81)

# Conjugation H -> -H-2F is exactly x -> -x.
x = (H+F)/(10*F)
xvee = sp.cancel(((-H-2*F)+F)/(10*F))
assert sp.cancel(xvee+x) == 0

print("OK: A2 source actual/conjugate gate product bridge certified")
