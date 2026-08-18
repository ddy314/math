#!/usr/bin/env python3
"""Exact transverse certificate for spontaneous-source-common-integer.md."""

import sympy as sp

# ---------------------------------------------------------------------------
# Exact tangency on the source first-layer slice.
# ---------------------------------------------------------------------------
x, t, y = sp.symbols("x t y")

C = (
    440*(x+2)**2*t**2
    + 81*(9401*x**4 - 2392*x**3 - 1600*x**2 - 64*x - 64)*t
    - 324*x*(99*x-4)*(25*x**2+1)*(49*x**2-4*x-2)
)

y0 = 225*x**2
r0 = 2*(x+2)/(99*x-4)
w0 = sp.cancel(x/r0)
s = 9+y
Nbar = 2025*x**2 + y**2
ztheta = (
    x**2*(s**2 - 18*s*t + 55*t**2)
    - sp.Rational(1,100)*(x+2)**2*Nbar
) / (2*x**2*(2*s-9*t))

Sphere = sp.cancel(
    x**2*w0**2*(s+ztheta)**2
    - (x+2+w0)**2*(Nbar*w0**2/100 + x**2*ztheta**2)
)
Sy0 = sp.cancel(sp.diff(Sphere, y).subs(y, y0))

Pd = (
    783481*t**2*x**6 - 105752*t**2*x**5 - 40720*t**2*x**4
    - 1664*t**2*x**3 - 1664*t**2*x**2
    - 78586200*t*x**8 + 9590400*t*x**7 - 195048*t*x**6
    + 254016*t*x**5 + 117936*t*x**4 - 5184*t*x**3
    + 1964655000*x**10 - 239760000*x**9 + 83462400*x**8
    - 15940800*x**7 - 2753352*x**6 - 124416*x**5
    - 117936*x**4 + 5184*x**3
)
assert sp.cancel(
    Sy0
    - C*Pd/(23328*(x+2)**4*(50*x**2+2-t)**3)
) == 0

# ---------------------------------------------------------------------------
# Full second-order source/angle/common expansion at p=1746991.
# We work directly in F_p[eps]/(eps^3), with symbolic lift coordinates.
# ---------------------------------------------------------------------------
p = 1746991
x0 = 1362653
t0 = 807263
X, T, D, Ph = sp.symbols("X T D Ph")


def modexpr(expr):
    return sp.Poly(sp.expand(expr), X, T, D, Ph, modulus=p).as_expr()


class S2:
    """Truncated series c0 + c1 eps + c2 eps^2 over F_p[X,T,D,Ph]."""

    def __init__(self, c0=0, c1=0, c2=0):
        self.c = [modexpr(c0), modexpr(c1), modexpr(c2)]

    def __add__(self, other):
        if not isinstance(other, S2):
            other = S2(other)
        return S2(*(self.c[i] + other.c[i] for i in range(3)))

    __radd__ = __add__

    def __neg__(self):
        return S2(*(-c for c in self.c))

    def __sub__(self, other):
        if not isinstance(other, S2):
            other = S2(other)
        return self + (-other)

    def __rsub__(self, other):
        return S2(other) - self

    def __mul__(self, other):
        if not isinstance(other, S2):
            other = S2(other)
        a, b = self.c, other.c
        return S2(
            a[0]*b[0],
            a[0]*b[1] + a[1]*b[0],
            a[0]*b[2] + a[1]*b[1] + a[2]*b[0],
        )

    __rmul__ = __mul__

    def inv(self):
        c0 = int(self.c[0]) % p
        d0 = pow(c0, -1, p)
        c1, c2 = self.c[1], self.c[2]
        return S2(
            d0,
            -c1*d0*d0,
            c1*c1*d0**3 - c2*d0*d0,
        )

    def __truediv__(self, other):
        if not isinstance(other, S2):
            other = S2(other)
        return self * other.inv()

    def __pow__(self, n):
        out = S2(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out


xs = S2(x0, X, 0)
ts = S2(t0, T, 0)
ds = S2(0, D, 0)
As = 99*xs - 4

# Source equal-depth coordinates:
# d = eps D, Phi_s = eps^2 Ph, hence
# r_s = [2(x+2)+eps^2 Ph]/(99x-4).
rs = (2*(xs+2) + S2(0,0,Ph)) / As
ys = 225*(xs**2) - ds
ss = 9 + ys
nb = 2025*(xs**2) + ys**2

numz = (
    xs**2*(ss**2 - 18*ss*ts + 55*ts**2)
    - (xs+2)**2*nb/S2(100)
)
denz = 2*xs**2*(2*ss - 9*ts)
zs = numz/denz
ws = xs/rs

sphere_series = (
    xs**2*ws**2*(ss+zs)**2
    - (xs+2+ws)**2*(nb*ws**2/S2(100) + xs**2*zs**2)
)

assert sphere_series.c[0] == 0
assert sphere_series.c[1] == 0
assert modexpr(sphere_series.c[2] - (32070*D**2 - 680549*Ph)) == 0

# Angle extra-lift fixes the normalized source second-order correction.
A0 = (99*x0 - 4) % p
kphi = (
    8*(x0+2)
    * pow((50625*A0*pow(x0,5,p)) % p, -1, p)
) % p
assert kphi == 1007439

full_coeff = (32070 - 680549*kphi) % p
assert full_coeff == 286982
assert full_coeff != 0

print("OK: A2 source common transverse singular audit certified")
