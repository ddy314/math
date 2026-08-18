#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-common-gate.md."""

import sympy as sp

x, t = sp.symbols("x t")
y = 225*x**2
s = 9 + y
A = 99*x - 4
r = 2*(x+2)/A
w = x/r
Nbar = 2025*x**2 + y**2

# Theta-dec noncentral third-numerator root.
znum = x**2*(s**2 - 18*s*t + 55*t**2) - (x+2)**2*Nbar/sp.Integer(100)
zden = 2*x**2*(2*s - 9*t)
z = sp.cancel(znum/zden)

sphere = sp.cancel(
    x**2*w**2*(s+z)**2
    - (x+2+w)**2*(Nbar*w**2/sp.Integer(100) + x**2*z**2)
)
num, _ = sp.fraction(sphere)

H4 = 9401*x**4 - 2392*x**3 - 1600*x**2 - 64*x - 64
Csrc = sp.expand(
    440*(x+2)**2*t**2
    + 81*H4*t
    - 324*x*(99*x-4)*(25*x**2+1)*(49*x**2-4*x-2)
)

expected_num = -x**2*(25*x**2+1)*Csrc**2
assert sp.Poly(sp.expand(num-expected_num), x, t).is_zero

# Defect-coordinate form u=10x-1.
u = sp.symbols("u")
Cu = sp.factor(sp.together(Csrc.subs(x, (1+u)/10)))
num_u, den_u = sp.fraction(Cu)
assert den_u == 10000
expected_u = sp.expand(
    44000*(u+21)**2*t**2
    + 81*(9401*u**4 + 13684*u**3 - 175354*u**2 - 418156*u - 878519)*t
    - 81*(u+1)*(99*u+59)*(u**2+2*u+5)*(49*u**2+58*u-191)
)
assert sp.Poly(sp.expand(num_u-expected_u), u, t).is_zero

# Exact coarse real bounds used in the markdown.
const_lb = sp.Rational(1620081, 3610)
assert const_lb > sp.Rational(44877, 100)
abs_H_bound = (
    9401*sp.Rational(2,19)**4
    + 2392*sp.Rational(2,19)**3
    + 1600*sp.Rational(2,19)**2
    + 64*sp.Rational(2,19)
    + 64
)
assert abs_H_bound < 93
assert 81*93*sp.Rational(1,10**11) < sp.Rational(8,10**8)

# tau-discriminant.
D8 = sp.expand(
    8012458881*x**8 - 332013104*x**7 + 1027170624*x**6
    + 111485312*x**5 + 130846848*x**4 + 25281536*x**3
    + 12020736*x**2 + 888832*x + 331776
)
assert sp.factor(sp.discriminant(Csrc, t) - 81*D8) == 0

print("OK: A2 source-to-common decimal gate certified")
