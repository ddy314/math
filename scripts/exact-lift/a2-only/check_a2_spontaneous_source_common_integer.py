#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-common-integer.md."""

import sympy as sp

x, t, H, E, F, u = sp.symbols("x t H E F u")

C = sp.expand(
    440*(x+2)**2*t**2
    + 81*(9401*x**4 - 2392*x**3 - 1600*x**2 - 64*x - 64)*t
    - 324*x*(99*x-4)*(25*x**2+1)*(49*x**2-4*x-2)
)

# Defect form.
Cdef = sp.expand(10000*C.subs(x, (1+u)/10))
expected_def = sp.expand(
    44000*(u+21)**2*t**2
    + 81*(9401*u**4 + 13684*u**3 - 175354*u**2 - 418156*u - 878519)*t
    - 81*(u+1)*(99*u+59)*(u**2+2*u+5)*(49*u**2+58*u-191)
)
assert sp.expand(Cdef - expected_def) == 0

# Natural integer representative: F=5^(M-1), E=2^(M-1),
# u=H/F, t=1/(10EF).
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
assert sp.cancel(
    expected_def.subs({u:H/F, t:1/(10*E*F)})
    - Ksrc/(10*E**2*F**6)
) == 0

# tau-discriminant and its singular bad-prime set.
Dsc = sp.Poly(sp.discriminant(C, t)/81, x).as_expr()
expected_Dsc = (
    8012458881*x**8 - 332013104*x**7 + 1027170624*x**6
    + 111485312*x**5 + 130846848*x**4 + 25281536*x**3
    + 12020736*x**2 + 888832*x + 331776
)
assert sp.expand(Dsc - expected_Dsc) == 0

assert sp.factorint(int(sp.discriminant(Dsc, x))) == {
    2:96, 3:5, 5:4, 11:4, 101:24, 109:1, 233:1,
    1746991:1, 405504443:2,
}

# p=11: the tau^2 coefficient degenerates, but dC/dtau never vanishes
# on F_11, so there is no full singular state.
b = sp.Poly(C, t).coeff_monomial(t)
assert all(int(b.subs(x, j)) % 11 for j in range(11))

# p=405504443: the repeated discriminant factor is irreducible over F_p.
p405 = 405504443
G405 = sp.gcd(
    sp.Poly(Dsc, x, modulus=p405),
    sp.Poly(sp.diff(Dsc, x), x, modulus=p405),
)
expected_G405 = sp.Poly(
    x**2 - 63668219*x + 95115196, x, modulus=p405
)
assert G405.monic().as_expr() == expected_G405.monic().as_expr()
d405 = (63668219**2 - 4*95115196) % p405
assert pow(d405, (p405-1)//2, p405) == p405 - 1

# p=1746991: unique genuine singular first-layer point.
p = 1746991
G = sp.gcd(
    sp.Poly(Dsc, x, modulus=p),
    sp.Poly(sp.diff(Dsc, x), x, modulus=p),
)
assert G.degree() == 1
x0 = (-384338) % p

a = 440*(x+2)**2
b = sp.Poly(C, t).coeff_monomial(t)
a0 = int(a.subs(x, x0)) % p
b0 = int(b.subs(x, x0)) % p
t0 = (-b0 * pow(2*a0, -1, p)) % p
assert t0 == 807263

Cx = sp.diff(C, x)
Ct = sp.diff(C, t)
assert int(C.subs({x:x0, t:t0})) % p == 0
assert int(Cx.subs({x:x0, t:t0})) % p == 0
assert int(Ct.subs({x:x0, t:t0})) % p == 0

# Genuine/noncentral units.
for value in (
    x0,
    x0 + 2,
    99*x0 - 4,
    25*x0*x0 + 1,
    2*(9 + 225*x0*x0) - 9*t0,
):
    assert value % p

# Since both first derivatives vanish mod p, this nonzero p-adic
# residual cannot be corrected by x=x0+pX, t=t0+pT at the p^2 layer.
Cval = int(C.subs({x:x0, t:t0}))
assert Cval % p == 0
assert (Cval // p) % p == 1642591

print("OK: A2 source common integer gate and singular audit certified")
