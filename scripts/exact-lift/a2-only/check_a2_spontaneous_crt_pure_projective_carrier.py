#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-projective-carrier.md."""

import math
import sympy as sp


r, u, v = sp.symbols("r u v")
K, zz = sp.symbols("K zz")
x, y = sp.symbols("x y")

U = 2 * K - 9
Lk = K**2 - 576 * K + 1296
A0 = 5 * K**2 + 144 * K - 324
B2 = 381 * K**4 - 78048 * K**3 - 277520 * K**2 + 2392704 * K - 3074112
B1 = 189 * K**4 - 126720 * K**3 + 132784 * K**2 + 1359360 * K - 2218752
B0 = 63 * K**4 - 54432 * K**3 + 136672 * K**2 + 239616 * K - 539136
E63 = (
    98304 * U**3 * A0 * zz**3
    - 1024 * U**2 * B2 * zz**2
    + 32 * U * Lk * B1 * zz
    - Lk**2 * B0
)

Eproj = sp.Poly(sp.expand(E63.subs({K: 1 / r, zz: u / r}) * r**8), r)
Lproj = sp.Poly(55 * r**2 + 18 * (u - 1) * r + 1 - 4 * u - v, r)
assert Eproj.degree() == 8

R = sp.expand(sp.resultant(Lproj.as_expr(), Eproj.as_expr(), r))
content, primitive = sp.primitive(sp.Poly(R, u, v).as_expr(), u, v)
assert int(content) == 5**7 * 11**7
X = sp.Poly(primitive, u, v, domain=sp.ZZ)
assert X.total_degree() == 11
assert X.degree(u) == 8
assert X.degree(v) == 8
assert len(X.terms()) == 59
assert [(sp.Poly(f, u, v).total_degree(), e) for f, e in sp.factor_list(X.as_expr(), u, v)[1]] == [(11, 1)]


def bernstein_coefficients(poly_expr, xvar, yvar, xr, yr):
    """Exact tensor Bernstein coefficients after affine map of a rational box to [0,1]^2."""
    X0, Y0 = sp.symbols("X0 Y0")
    xa, xb = xr
    ya, yb = yr
    expr = sp.expand(poly_expr.subs({xvar: xa + (xb - xa) * X0, yvar: ya + (yb - ya) * Y0}))
    P = sp.Poly(expr, X0, Y0, domain=sp.QQ)
    m = P.degree(X0)
    n = P.degree(Y0)
    power = {
        (i, j): P.coeff_monomial(X0**i * Y0**j)
        for i in range(m + 1)
        for j in range(n + 1)
    }
    out = []
    for k in range(m + 1):
        for ell in range(n + 1):
            b = sp.Rational(0)
            for i in range(k + 1):
                for j in range(ell + 1):
                    aij = power[(i, j)]
                    if aij:
                        b += (
                            aij
                            * sp.Rational(math.comb(k, i), math.comb(m, i))
                            * sp.Rational(math.comb(ell, j), math.comb(n, j))
                        )
            out.append(b)
    return out


# Exact endpoint box.
xr = (sp.Rational(1, 10), sp.Rational(2, 19))
yr = (sp.Rational(249, 250), sp.Rational(1))

# Exact v window.  The displayed derivatives have fixed sign on the box.
vexpr = (x + 2) ** 2 * (2025 * x**2 + y**2) / (100 * x**2 * (9 + y) ** 2)
dvx = sp.factor(sp.diff(vexpr, x))
dvy = sp.factor(sp.diff(vexpr, y))
assert dvx == (x + 2) * (2025 * x**3 - 2 * y**2) / (50 * x**3 * (y + 9) ** 2)
assert dvy == -9 * (x + 2) ** 2 * (225 * x**2 - y) / (50 * x**2 * (y + 9) ** 3)

vmin = sp.factor(vexpr.subs({x: xr[0], y: yr[1]}))
vmax = sp.factor(vexpr.subs({x: xr[1], y: yr[0]}))
assert vmin == sp.Rational(7497, 8000)
assert vmax == sp.Rational(234947716, 250493929)
assert vmin > sp.Rational(937, 1000)
assert vmax < sp.Rational(939, 1000)

# Branch-1 u window using exact Bernstein positivity after clearing its positive denominator.
d = 225 * x**2 - y
Asp = 4 * d**2 - x * y**2 * (99 * x - 4)
Aplus = 202500 * x**4 + 99 * x**2 * y**2 - 4 * x * y**2 - 4 * y**2
N1 = sp.expand(Aplus * Asp)
D1 = sp.expand(400 * x**2 * y**3 * (x + 2) ** 2 * (9 + y))

lower_poly = sp.expand(93 * D1 - 100 * N1)
upper_poly = sp.expand(50 * N1 - 27 * D1)
bl = bernstein_coefficients(lower_poly, x, y, xr, yr)
bu = bernstein_coefficients(upper_poly, x, y, xr, yr)
assert min(bl) == sp.Rational(1041285803156808768, 6634204312890625)
assert min(bu) == sp.Rational(73, 25)
assert min(bl) > 0 and min(bu) > 0

# Final projective carrier is strictly negative on the rational enclosure.
ur = (sp.Rational(-93, 100), sp.Rational(-27, 50))
vr = (sp.Rational(937, 1000), sp.Rational(939, 1000))
bx = bernstein_coefficients(X.as_expr(), u, v, ur, vr)
assert len(bx) == 81
assert max(bx) == -sp.Rational(
    77096177819298948415154163591507164734582999,
    7450580596923828125,
)
assert max(bx) < 0

print("OK: projective descendant carrier is irreducible and branch 1 is strictly real-negative")
