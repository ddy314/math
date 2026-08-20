#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-linear-depth-reader.md."""

import math
import sympy as sp


def v2(n: int) -> int:
    n = abs(int(n))
    assert n
    return (n & -n).bit_length() - 1


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


r, u, v = sp.symbols("r u v")
K, zz = sp.symbols("K zz")

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
rem = sp.Poly(sp.rem(Eproj, Lproj).as_expr(), r)
assert rem.degree() == 1
A = sp.Poly(rem.coeff_monomial(r), u, v, domain=sp.QQ)
B = sp.Poly(rem.coeff_monomial(1), u, v, domain=sp.QQ)

D0 = 5**7 * 11**7
Aint = sp.Poly(sp.expand(D0 * A.as_expr()), u, v, domain=sp.ZZ)
Bint = sp.Poly(sp.expand(D0 * B.as_expr()), u, v, domain=sp.ZZ)
assert Aint.total_degree() == 7 and Bint.total_degree() == 8
assert Aint.degree(u) == 7 and Bint.degree(u) == 7
assert Aint.degree(v) == 3 and Bint.degree(v) == 4
assert len(Aint.terms()) == 20
assert len(Bint.terms()) == 24

# Exact Bernstein sign/height audit on the actual projective rectangle.
ur = (sp.Rational(0), sp.Rational(1, 1000))
vr = (sp.Rational(937, 1000), sp.Rational(939, 1000))
ba = bernstein_coefficients(Aint.as_expr(), u, v, ur, vr)
bb = bernstein_coefficients(Bint.as_expr(), u, v, ur, vr)

assert min(ba) == sp.Rational(186871147561988154254304, 15625)
assert max(ba) == sp.Rational(
    5744925543296429255273134446887094,
    476837158203125,
)
assert min(ba) > 0

assert min(bb) == -sp.Rational(82743358059276934923729, 1953125)
assert max(bb) == -sp.Rational(
    18219304842663055778170041164244,
    476837158203125,
)
assert max(bb) < 0

margin = -max(bb) - max(ba) / 1000
assert margin == sp.Rational(
    6237189649683313261448453358678453,
    238418579101562500,
)
assert margin > 0

# Coefficient-depth audit after clearing u=a3/R and v=X/Y with R^7 Y^4.
ca = {(i, j): int(co) for (i, j), co in Aint.terms()}
cb = {(i, j): int(co) for (i, j), co in Bint.terms()}
assert cb[(0, 4)] == 2**17 * 3**12 * 5**3 * 11**3 * 13
assert v2(cb[(0, 4)]) == 17
assert (cb[(0, 4)] // 2**17) % 8 == 3

# Slopes in m,t after extracting 7(m+1)+4(2M+2).
for (i, j), co in ca.items():
    assert 8 - i - 2 * j >= 0  # coefficient of m after simplification
    assert 8 - 2 * j >= 0      # coefficient of t
for (i, j), co in cb.items():
    assert 8 - i - 2 * j >= 0
    assert 8 - 2 * j >= 0

ledger = []
for (i, j), co in ca.items():
    eps = v2(co) - i * 6 + (4 - j) * 16  # m=5,t=3
    ledger.append((eps, "A", i, j))
for (i, j), co in cb.items():
    eps = v2(co) + 1 - i * 6 + (4 - j) * 16
    ledger.append((eps, "B", i, j))
ledger.sort()
assert ledger[0] == (18, "B", 0, 4)
assert ledger[1][0] == 21

M, m = sp.symbols("M m", integer=True)
assert sp.expand(7 * (m + 1) + 4 * (2 * M + 2) + 18 - (8 * M + 7 * m + 33)) == 0

# Signed primitive residue: 3*5^m (mod 8); positive carrier is its negative.
for mm in range(8):
    signed = (3 * pow(5, mm, 8)) % 8
    positive = (-signed) % 8
    if mm % 2 == 0:
        assert signed == 3 and positive == 5
    else:
        assert signed == 7 and positive == 1
    assert positive % 4 == 1

print("OK: shorter descendant linear carrier is negative and its positive primitive part is always 1 mod 4")
