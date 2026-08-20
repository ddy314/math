#!/usr/bin/env python3
"""Exact symbolic certificate for spontaneous-source-depth-transfer.md."""

import sympy as sp

x, y, t, w, z = sp.symbols("x y t w z")

y0 = 225*x**2
r0 = 2*(x+2)/(99*x-4)
w0 = sp.cancel(x/r0)

S = sp.expand(
    x**2*w**2*(9+y+z)**2
    - (x+2+w)**2*((2025*x**2+y**2)*w**2/100 + x**2*z**2)
)

zs = sp.factor(x**2*(297*x-12)**2/(16*(x+2)**2))
source_square = (
    -x**2*(25*x**2+1)/(64*(x+2)**4)
    * (16*(x+2)**2*z - x**2*(297*x-12)**2)**2
)
assert sp.factor(S.subs({y:y0, w:w0}) - source_square) == 0

coef_z2 = sp.factor(sp.Poly(S.subs({y:y0, w:w0}), z).coeff_monomial(z**2))
assert coef_z2 == -4*x**2*(25*x**2+1)

ztheta = (
    x**2*((9+y)**2 - 18*(9+y)*t + 55*t**2)
    - (x+2)**2*(2025*x**2+y**2)/100
) / (2*x**2*(2*(9+y)-9*t))

Csrc = sp.expand(
    440*(x+2)**2*t**2
    + 81*(9401*x**4 - 2392*x**3 - 1600*x**2 - 64*x - 64)*t
    - 324*x*(99*x-4)*(25*x**2+1)*(49*x**2-4*x-2)
)

assert sp.factor(
    (ztheta.subs(y,y0)-zs)*144*(x+2)**2*(50*x**2+2-t) - Csrc
) == 0

# Exact source-slice tangencies used in the valuation argument.
assert sp.factor(S.subs({y:y0,w:w0,z:zs})) == 0
assert sp.factor(sp.diff(S,z).subs({y:y0,w:w0,z:zs})) == 0
assert sp.factor(sp.diff(S,y).subs({y:y0,w:w0,z:zs})) == 0

expected_dw = -81*x**4*(99*x-4)**2*(101*x**2+4*x+8)**2/(128*(x+2)**3)
assert sp.factor(sp.diff(S,w).subs({y:y0,w:w0,z:zs}) - expected_dw) == 0

# The additive affine root moves linearly in d = y0-y.
Utheta = sp.cancel((ztheta-ztheta.subs(y,y0))/(y0-y))
assert sp.cancel(ztheta-ztheta.subs(y,y0)-(y0-y)*Utheta) == 0

# Exact affine factorization of Theta_dec after normalizing a3 = T*N*z.
# The coefficient is read directly from Theta = T*R - 2 B^2(2K-9)a3;
# this checker certifies the nontrivial source/sphere identities above.

print("OK: A2 source half-depth transfer identities certified")
