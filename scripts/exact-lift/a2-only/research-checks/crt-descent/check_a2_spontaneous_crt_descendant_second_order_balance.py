#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-second-order-balance.md."""

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


K, zeta, J, R = sp.symbols("K zeta J R")
r, u, v = sp.symbols("r u v")
U = 2 * K - 9

# Universal cubic and first-layer point.
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

Phi = J * (J + 2 * zeta) * (K - J)**2 - R * (J + zeta)**2
PhiJ = sp.diff(Phi, J)
PhiJJ = sp.diff(PhiJ, J)
PhiJ0 = sp.factor(PhiJ.subs({J: J0, R: R0}))
PhiJJ0 = sp.factor(PhiJJ.subs({J: J0, R: R0}))

# Projective Euclidean quotient and v derivative.
Eproj = sp.Poly(sp.expand(E63.subs({K: 1 / r, zeta: u / r}) * r**8), r)
Lproj = sp.Poly(55 * r**2 + 18 * (u - 1) * r + 1 - 4 * u - v, r)
Qproj, _ = sp.div(Eproj, Lproj)
Q0 = sp.factor(Qproj.as_expr().subs({r: 1 / K, u: zeta / K, v: R0 / K**2}))
Qv0 = sp.factor(sp.diff(Qproj.as_expr(), v).subs({r: 1 / K, u: zeta / K, v: R0 / K**2}))

# First-order gates and geometric balance.
C_lt = sp.factor(-sp.Rational(65536) * U**4 * (J0 + zeta)**2 / K**6)
C_gt = sp.factor(
    sp.Rational(65536) * U**3 / K**6
    * (PhiJ0 - U * (J0 + zeta)**2)
)
raw_lt = sp.factor(C_lt - Q0)
raw_gt = sp.factor(C_gt - Q0)
num_lt, _ = sp.together(raw_lt).as_numer_denom()
num_gt, _ = sp.together(raw_gt).as_numer_denom()
_, Glt_expr = sp.primitive(sp.Poly(sp.expand(num_lt), K, zeta).as_expr(), K, zeta)
_, Ggt_expr = sp.primitive(sp.Poly(sp.expand(num_gt), K, zeta).as_expr(), K, zeta)
Glt = sp.Poly(Glt_expr, K, zeta, domain=sp.ZZ)
Ggt = sp.Poly(Ggt_expr, K, zeta, domain=sp.ZZ)
chi = sp.factor(-sp.Rational(2) * Ggt.as_expr() / (81 * Glt.as_expr()))

# Quadratic transported/Euclidean coefficient after factoring s_L^2 Y^2.
Ctr = sp.Rational(65536) * U**4 / K**8
Q2chi = sp.factor(
    Ctr * (
        -sp.Rational(1, 2) * PhiJJ0 * K**4 / U**2
        + 2 * (J0 + zeta) * K**4 / U * (chi + 1)
    )
    + Qv0 * (chi + 1)**2
)
num_q2, den_q2 = sp.together(Q2chi).as_numer_denom()
content, S2_expr = sp.primitive(sp.Poly(sp.expand(num_q2), K, zeta).as_expr(), K, zeta)
S2 = sp.Poly(S2_expr, K, zeta, domain=sp.ZZ)
assert content == 256
assert sp.factor(den_q2 - 81 * K**4 * Glt.as_expr()**2) == 0
assert S2.total_degree() == 16
assert S2.degree(zeta) == 14
assert len(S2.terms()) == 150

# Eliminate zeta: central U^8 plus one irreducible degree-110 gate.
res = sp.factor(sp.resultant(E63, S2.as_expr(), zeta))
fl = sp.factor_list(res, K)
assert fl[0] == -2**140 * 3**11
assert [(sp.Poly(f, K).degree(), e) for f, e in fl[1]] == [(1, 8), (110, 1)]
assert sp.expand(fl[1][0][0] - U) == 0
P110 = sp.Poly(fl[1][1][0], K, domain=sp.ZZ)
assert P110.is_irreducible
assert len(P110.terms()) == 111

# Exact real positivity of the second-order numerator on the actual wide projective box.
S2proj = sp.Poly(sp.expand(S2.as_expr().subs({K: 1 / r, zeta: u / r}) * r**16), r, u)
assert S2proj.degree(r) == 16
assert S2proj.degree(u) == 14
assert len(S2proj.terms()) == 150
box = (sp.Rational(0), sp.Rational(1, 1000))
b = bernstein_coefficients(S2proj.as_expr(), r, u, box, box)
assert len(b) == 255
assert min(b) == sp.Rational(
    198730569009592634141902074605524422074200621380891689557678786752875433,
    3725290298461914062500000000000000000000,
)
assert max(b) == sp.Integer(162937721250850407546364808657801)
assert min(b) > 0

# Abstract depth trichotomy sanity checks.
def vp(n, p):
    n = abs(int(n))
    if n == 0:
        return 10**9
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

p = 101
for h in range(1, 4):
    # rho<h: linear term uniquely shallow.
    for rho in range(0, h):
        Mv = p**(h + rho) + p**(2*h)
        assert vp(Mv, p) == h + rho
    # rho>h and regular nonzero quadratic coefficient: exact 2h.
    for rho in range(h + 1, h + 4):
        Mv = p**(h + rho) + 7 * p**(2*h) + p**(3*h)
        assert vp(Mv, p) == 2*h

print("OK: second-order balance saturation is regular outside central/P110; only rho=h retains a normalized cancellation")
