#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-halfdepth-blowup.md."""

import sympy as sp

x,eps,D,phi,Z,t,y = sp.symbols("x eps D phi Z t y")
A = 99*x-4
y0 = 225*x**2
r0 = 2*(x+2)/A
r = r0 + eps**2*phi/A
w = sp.cancel(x/r)
w0 = sp.cancel(x/r0)
zs = sp.cancel(x**2*(297*x-12)**2/(16*(x+2)**2))

Y,W,ZZ = sp.symbols("Y W ZZ")
S = sp.expand(
    x**2*W**2*(9+Y+ZZ)**2
    - (x+2+W)**2*((2025*x**2+Y**2)*W**2/sp.Integer(100)+x**2*ZZ**2)
)
Spert = sp.cancel(S.subs({Y:y0-eps*D,W:w,ZZ:zs+eps*Z}))
ser = sp.series(Spert,eps,0,3).removeO()
assert sp.expand(ser).coeff(eps,0) == 0
assert sp.expand(ser).coeff(eps,1) == 0
Bquad = sp.factor(sp.expand(ser).coeff(eps,2))

az = -4*x**2*(25*x**2+1)
bz = -x**4*(99*x-4)**2/(2*(x+2)**2)
cd = -x**2*(99*x-4)**2*(81*x**2-36*x+8)*(121*x**2+44*x+8)/(1600*(x+2)**4)
cphi = 81*x**5*(99*x-4)**3*(101*x**2+4*x+8)**2/(512*(x+2)**5)
expected = az*Z**2+bz*D*Z+cd*D**2+cphi*phi
assert sp.factor(Bquad-expected) == 0

disc = sp.factor((bz*D)**2-4*az*(cd*D**2+cphi*phi))
expected_disc = sp.factor(
    x**4*(99*x-4)**2*(101*x**2+4*x+8)**2/(800*(x+2)**5)
    *(-8*(x+2)*D**2+2025*x**3*(99*x-4)*(25*x**2+1)*phi)
)
assert sp.factor(disc-expected_disc) == 0

phi_extra = 8*(x+2)*D**2/(50625*(99*x-4)*x**5)
extra_disc = sp.factor(disc.subs(phi,phi_extra))
assert sp.factor(
    extra_disc
    - D**2*x**2*(99*x-4)**2*(101*x**2+4*x+8)**2/(2500*(x+2)**4)
) == 0

c1 = -(99*x-4)*(99*x**2-4*x-8)/(400*x*(x+2)**2)
c2 = -(99*x-4)*(2475*x**4-100*x**3+101*x**2+4*x+8)/(400*x*(x+2)**2*(25*x**2+1))
assert sp.factor(expected.subs({Z:c1*D,phi:phi_extra})) == 0
assert sp.factor(expected.subs({Z:c2*D,phi:phi_extra})) == 0
assert sp.factor(
    c2-c1 + (99*x-4)*(101*x**2+4*x+8)/(200*x*(x+2)**2*(25*x**2+1))
) == 0

# A_- source-slice boundary.
d0 = 225*x**2-y
Asp = 4*d0**2-x*y**2*(99*x-4)
Aminus = sp.expand(Asp-2*y**2*(x+2)**2)
assert sp.factor(Aminus.subs(y,y0)) == -50625*x**4*(101*x**2+4*x+8)

# Additive affine root and its first d-coefficient.
ztheta = (
    x**2*((9+y)**2-18*(9+y)*t+55*t**2)
    -(x+2)**2*(2025*x**2+y**2)/100
)/(2*x**2*(2*(9+y)-9*t))
Csrc = sp.expand(
    440*(x+2)**2*t**2
    +81*(9401*x**4-2392*x**3-1600*x**2-64*x-64)*t
    -324*x*(99*x-4)*(25*x**2+1)*(49*x**2-4*x-2)
)
uc = 1/(144*(x+2)**2*(50*x**2+2-t))
assert sp.factor(ztheta.subs(y,y0)-zs-uc*Csrc) == 0

q = sp.symbols("q")
ctheta = sp.factor(sp.limit((ztheta.subs(y,y0-q)-ztheta.subs(y,y0))/q,q,0))
expected_ctheta = -(
    104*t**2-8019*t*x**2+324*t*x
    +200475*x**4-8100*x**3+8019*x**2-324*x
)/(324*(50*x**2+2-t)**2)
assert sp.factor(ctheta-expected_ctheta) == 0

print("OK: A2 source odd-extra half-depth blowup splits into two simple affine orientations")
