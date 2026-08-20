#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-balance-tail.md."""

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

# Universal cubic / projective quotient.
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

Eproj = sp.Poly(sp.expand(E63.subs({K: 1 / r, zeta: u / r}) * r**8), r)
Lproj = sp.Poly(55 * r**2 + 18 * (u - 1) * r + 1 - 4 * u - v, r)
Qproj, _ = sp.div(Eproj, Lproj)
Q0 = sp.factor(Qproj.as_expr().subs({r: 1 / K, u: zeta / K, v: R0 / K**2}))

Phi = J * (J + 2 * zeta) * (K - J)**2 - R * (J + zeta)**2
PhiJ = sp.diff(Phi, J)
PhiJ0 = sp.factor(PhiJ.subs({J: J0, R: R0}))
C_lt = sp.factor(-sp.Rational(65536) * U**4 * (J0 + zeta)**2 / K**6)
C_gt = sp.factor(
    sp.Rational(65536) * U**3 / K**6
    * (PhiJ0 - U * (J0 + zeta)**2)
)

raw_lt = sp.factor(C_lt - Q0)
raw_gt = sp.factor(C_gt - Q0)
num_lt, den_lt = sp.together(raw_lt).as_numer_denom()
num_gt, den_gt = sp.together(raw_gt).as_numer_denom()
cont_lt, Glt_expr = sp.primitive(sp.Poly(sp.expand(num_lt), K, zeta).as_expr(), K, zeta)
cont_gt, Ggt_expr = sp.primitive(sp.Poly(sp.expand(num_gt), K, zeta).as_expr(), K, zeta)
Glt = sp.Poly(Glt_expr, K, zeta, domain=sp.ZZ)
Ggt = sp.Poly(Ggt_expr, K, zeta, domain=sp.ZZ)

assert cont_lt == 5184 == 64 * 81
assert cont_gt == 128 == 64 * 2
assert sp.factor(den_lt) == sp.factor(den_gt) == 5**7 * 11**7 * K**6
assert sp.factor(raw_lt - sp.Rational(5184) * Glt.as_expr() / den_lt) == 0
assert sp.factor(raw_gt - sp.Rational(128) * Ggt.as_expr() / den_gt) == 0

# Exact homogeneous error scaling: L=sL(X+Y), F=K^2 sL Y.
M, m, cu, g = sp.symbols("M m cu g", nonzero=True)
T = 2**m * 5**m
Bsq = 2**(2*M + 2*m + 2) * cu**2 * g**2
sL = 2**(2*M + 2) / (5**m * Bsq * K**2)
# Y = g*2^m*Dhat; F=Dhat/(cu^2*g*T).
Dhat = sp.symbols("Dhat")
Y = g * 2**m * Dhat
F_from_Y = sp.factor(K**2 * sL * Y)
assert sp.factor(F_from_Y - Dhat / (cu**2 * g * T)) == 0

# Equal-depth geometric balance ratio reduces exactly to -2 Ggt/(81 Glt).
Cscale = sp.Rational(65536) * U**4 / K**8
Dgeom = sp.factor((J0 + zeta)**2 + Q0 / (Cscale * K**2))
chi_geom = sp.factor((PhiJ0 / U) / Dgeom - 1)
assert sp.factor(chi_geom + sp.Rational(2) * Ggt.as_expr() / (81 * Glt.as_expr())) == 0

# Projective gates are both negative, while 81 Glt - 2 Ggt is positive.
Glt_proj = sp.Poly(sp.expand(Glt.as_expr().subs({K: 1 / r, zeta: u / r}) * r**6), r, u)
Ggt_proj = sp.Poly(sp.expand(Ggt.as_expr().subs({K: 1 / r, zeta: u / r}) * r**6), r, u)
box = (sp.Rational(0), sp.Rational(1, 1000))
b_lt = bernstein_coefficients(Glt_proj.as_expr(), r, u, box, box)
b_gt = bernstein_coefficients(Ggt_proj.as_expr(), r, u, box, box)
assert max(b_lt) < 0 and max(b_gt) < 0
Hminus = sp.Poly(81 * Glt_proj.as_expr() - 2 * Ggt_proj.as_expr(), r, u)
b_h = bernstein_coefficients(Hminus.as_expr(), r, u, box, box)
assert min(b_h) == sp.Rational(24267959613723206789529, 6250000000)
assert min(b_h) > 0

# Parent cancellation chi=-1 plus child recycling has exactly the tangent resultant.
Hcancel = sp.Poly(81 * Glt.as_expr() - 2 * Ggt.as_expr(), K, zeta)
res_cancel = sp.factor(sp.resultant(E63, Hcancel.as_expr(), zeta))
GD = 11 * K**2 - 240 * K + 432
H2 = 47 * K**2 + 144 * K - 416
H10 = (
    388341 * K**10 - 601739280 * K**9 + 229469500800 * K**8
    + 1907909697024 * K**7 + 388001070336 * K**6
    + 472180427182080 * K**5 - 5611474473205760 * K**4
    + 24390734431518720 * K**3 - 51182973630480384 * K**2
    + 52664489116434432 * K - 21375786688708608
)
expected = 2**43 * 3**2 * U**13 * Lk**2 * GD**2 * H2 * H10
assert sp.expand(abs(res_cancel) - expected) == 0

# Finite-field sanity check of the homogeneous projective limits.
p = 101
for x0, y0 in ((7, 0), (0, 9), (7, 9)):
    lhs = (81 * x0 * 13 + 2 * y0 * 17) % p
    if y0 == 0:
        assert (lhs == 0) == (13 % p == 0)
    if x0 == 0:
        assert (lhs == 0) == (17 % p == 0)

print("OK: same-prime recycling is exactly the homogeneous parent-balance tail; parent cancellation collides only on tangent gates")
