#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-unequal-parent-depth.md."""

import math
import sympy as sp


def bernstein_coefficients(poly_expr, xvar, yvar, xr, yr):
    X0, Y0 = sp.symbols("X0 Y0")
    xa, xb = xr
    ya, yb = yr
    expr = sp.expand(poly_expr.subs({
        xvar: xa + (xb - xa) * X0,
        yvar: ya + (yb - ya) * Y0,
    }))
    P = sp.Poly(expr, X0, Y0, domain=sp.QQ)
    m = P.degree(X0)
    n = P.degree(Y0)
    power = {(i, j): P.coeff_monomial(X0**i * Y0**j)
             for i in range(m + 1) for j in range(n + 1)}
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


K, zeta, R, J = sp.symbols("K zeta R J")
r, u, v = sp.symbols("r u v")
U = 2 * K - 9

# Universal cubic.
Lk = K**2 - 576 * K + 1296
A0 = 5 * K**2 + 144 * K - 324
B2 = 381 * K**4 - 78048 * K**3 - 277520 * K**2 + 2392704 * K - 3074112
B1 = 189 * K**4 - 126720 * K**3 + 132784 * K**2 + 1359360 * K - 2218752
B0 = 63 * K**4 - 54432 * K**3 + 136672 * K**2 + 239616 * K - 539136
E63 = sp.expand(
    98304 * U**3 * A0 * zeta**3
    - 1024 * U**2 * B2 * zeta**2
    + 32 * U * Lk * B1 * zeta
    - Lk**2 * B0
)

R0 = K**2 - (18 + 4 * zeta) * K + 18 * zeta + 55
J0 = (K**2 - 64 * K * zeta - 576 * K + 288 * zeta + 1296) / (16 * U)

# Projective Euclidean quotient.
Eproj = sp.Poly(sp.expand(E63.subs({K: 1 / r, zeta: u / r}) * r**8), r)
Lproj = sp.Poly(55 * r**2 + 18 * (u - 1) * r + 1 - 4 * u - v, r)
Qproj, _ = sp.div(Eproj, Lproj)
Q0 = sp.factor(Qproj.as_expr().subs({r: 1 / K, u: zeta / K, v: R0 / K**2}))

# Rational-root derivative at first layer.
Phi = J * (J + 2 * zeta) * (K - J)**2 - R * (J + zeta)**2
PhiJ = sp.diff(Phi, J)
PhiJ0 = sp.factor(PhiJ.subs({J: J0, R: R0}))

# Unequal-parent transported coefficients.
C_lt = sp.factor(-sp.Rational(65536) * U**4 * (J0 + zeta)**2 / K**6)
C_gt = sp.factor(
    sp.Rational(65536) * U**3 / K**6
    * (PhiJ0 - U * (J0 + zeta)**2)
)

num_lt, den_lt = sp.together(C_lt - Q0).as_numer_denom()
num_gt, den_gt = sp.together(C_gt - Q0).as_numer_denom()
Glt = sp.Poly(sp.primitive(sp.Poly(sp.expand(num_lt), K, zeta).as_expr(), K, zeta)[1], K, zeta, domain=sp.ZZ)
Ggt = sp.Poly(sp.primitive(sp.Poly(sp.expand(num_gt), K, zeta).as_expr(), K, zeta)[1], K, zeta, domain=sp.ZZ)

assert sp.factor(den_lt) == 5**7 * 11**7 * K**6
assert sp.factor(den_gt) == 5**7 * 11**7 * K**6
assert Glt.total_degree() == Ggt.total_degree() == 6
assert len(Glt.terms()) == len(Ggt.terms()) == 28

# Exact normalization ratio for b<a: L0/F0=1/K^2.
M, m, cu, g = sp.symbols("M m cu g", nonzero=True)
T = 2**m * 5**m
Bsq = 2**(2*M + 2*m + 2) * cu**2 * g**2
ratio = sp.factor(
    2**(2*M + 2) / (5**m * Bsq * K**2)
    * g * 2**m * cu**2 * g * T
)
assert ratio == K**-2

# Eliminate zeta; only one irreducible degree-48 K factor remains in each case.
res_lt = sp.factor(sp.resultant(E63, Glt.as_expr(), zeta))
res_gt = sp.factor(sp.resultant(E63, Ggt.as_expr(), zeta))
fl_lt = sp.factor_list(res_lt, K)
fl_gt = sp.factor_list(res_gt, K)
assert fl_lt[0] == -2**54 * 3**3
assert fl_gt[0] == -2**51 * 3**5
assert [(sp.Poly(f, K).degree(), e) for f, e in fl_lt[1]] == [(48, 1)]
assert [(sp.Poly(f, K).degree(), e) for f, e in fl_gt[1]] == [(48, 1)]
assert sp.Poly(fl_lt[1][0][0], K).is_irreducible
assert sp.Poly(fl_gt[1][0][0], K).is_irreducible

# Projectivize the compact degree-6 gates and certify strict real negativity.
Glt_proj = sp.Poly(sp.expand(Glt.as_expr().subs({K: 1 / r, zeta: u / r}) * r**6), r, u)
Ggt_proj = sp.Poly(sp.expand(Ggt.as_expr().subs({K: 1 / r, zeta: u / r}) * r**6), r, u)
assert Glt_proj.total_degree() == Ggt_proj.total_degree() == 6
assert len(Glt_proj.terms()) == len(Ggt_proj.terms()) == 28

box = (sp.Rational(0), sp.Rational(1, 1000))
b_lt = bernstein_coefficients(Glt_proj.as_expr(), r, u, box, box)
b_gt = bernstein_coefficients(Ggt_proj.as_expr(), r, u, box, box)
assert len(b_lt) == len(b_gt) == 49
assert min(b_lt) == -sp.Rational(112029905407645176473437498709, 976562500000000)
assert max(b_lt) == -sp.Integer(104415810491281)
assert min(b_gt) == -sp.Rational(9078214206708903545409301301679, 1953125000000000)
assert max(b_gt) == -sp.Integer(4264617552904693)
assert max(b_lt) < 0 and max(b_gt) < 0

print("OK: unequal descendant parent depths reduce to two fixed irreducible degree-48 K gates")
