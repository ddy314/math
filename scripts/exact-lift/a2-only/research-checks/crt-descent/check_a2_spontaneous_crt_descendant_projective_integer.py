#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-projective-integer.md."""

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
R = sp.expand(sp.resultant(Lproj.as_expr(), Eproj.as_expr(), r))
content, primitive = sp.primitive(sp.Poly(R, u, v).as_expr(), u, v)
assert int(content) == 5**7 * 11**7
Xproj = sp.Poly(primitive, u, v, domain=sp.ZZ)
assert Xproj.total_degree() == 11
assert Xproj.degree(u) == Xproj.degree(v) == 8
assert len(Xproj.terms()) == 59

# Actual endpoint rectangle u in [0,1/1000], v in [937/1000,939/1000].
coeffs = bernstein_coefficients(
    Xproj.as_expr(),
    u,
    v,
    (sp.Rational(0), sp.Rational(1, 1000)),
    (sp.Rational(937, 1000), sp.Rational(939, 1000)),
)
assert len(coeffs) == 81
assert min(coeffs) == sp.Rational(
    170202247140227961698711469574928714478754971,
    9313225746154785156250,
)
assert min(coeffs) > 0

# Exact coefficient ledger for the integer clearing
# P63 = sum c_ij a3^i R^(8-i) X^j Y^(8-j).
c = {(i, j): int(co) for (i, j), co in Xproj.terms()}
assert c[(0, 8)] == 2**34 * 3**24 * 13**2
assert v2(c[(0, 8)]) == 34
assert (c[(0, 8)] // 2**34) % 8 == 1

# extra depth after extracting 8*v2(R)+8*v2(X):
# eps_ij = v2(c_ij)-i*(m+1)+(8-j)*(2m+2t).
# Every slope is nonnegative, so the minimum occurs at m=5,t=3.
for (i, j), co in c.items():
    assert 16 - i - 2 * j >= 0
    assert 16 - 2 * j >= 0

ledger = []
for (i, j), co in c.items():
    eps = v2(co) - i * 6 + (8 - j) * 16  # m=5,t=3
    ledger.append((eps, i, j))
ledger.sort()
assert ledger[0] == (34, 0, 8)
assert ledger[1][0] == 39

M, m = sp.symbols("M m", integer=True)
assert sp.expand(8 * (m + 1) + 8 * (2 * M + 2) + 34 - (16 * M + 8 * m + 58)) == 0

for odd in (1, 3, 5, 7):
    assert pow(odd, 8, 8) == 1

print("OK: canonical descendant-only projective integer is positive with exact primitive orientation 1 mod 8")
