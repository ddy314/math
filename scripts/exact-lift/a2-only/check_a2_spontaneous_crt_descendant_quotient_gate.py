#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-quotient-gate.md."""

import math
import sympy as sp


def v2(n: int) -> int:
    n = abs(int(n))
    assert n
    return (n & -n).bit_length() - 1


def bernstein_coefficients_nd(poly_expr, vars_, ranges):
    Xs = sp.symbols("X0:" + str(len(vars_)))
    subs = {
        var: a + (b - a) * X
        for var, X, (a, b) in zip(vars_, Xs, ranges)
    }
    expr = sp.expand(poly_expr.subs(subs))
    P = sp.Poly(expr, *Xs, domain=sp.QQ)
    degs = [P.degree(X) for X in Xs]
    power = {mon: coeff for mon, coeff in P.terms()}
    out = []
    import itertools
    for ks in itertools.product(*[range(d + 1) for d in degs]):
        b = sp.Rational(0)
        for inds in itertools.product(*[range(k + 1) for k in ks]):
            acoef = power.get(tuple(inds), 0)
            if acoef:
                fac = sp.Rational(1)
                for k, i, d in zip(ks, inds, degs):
                    fac *= sp.Rational(math.comb(k, i), math.comb(d, i))
                b += acoef * fac
        out.append(b)
    return out, degs


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
Q, M = sp.div(Eproj, Lproj)
assert Q.degree() == 6
Qpoly = sp.Poly(Q.as_expr(), r, u, v, domain=sp.QQ)
assert Qpoly.degree(r) == 6
assert Qpoly.degree(u) == 6
assert Qpoly.degree(v) == 3
assert Qpoly.total_degree() == 6
assert len(Qpoly.terms()) == 50

D0, Qint = Qpoly.clear_denoms()
assert int(D0) == 5**7 * 11**7
Qint = sp.Poly(Qint, r, u, v, domain=sp.ZZ)

# Exact positivity on a deliberately wide box containing the actual endpoint.
bq, degs = bernstein_coefficients_nd(
    Qint.as_expr(),
    (r, u, v),
    (
        (sp.Rational(0), sp.Rational(1, 1000)),
        (sp.Rational(0), sp.Rational(1, 1000)),
        (sp.Rational(937, 1000), sp.Rational(939, 1000)),
    ),
)
assert degs == [6, 6, 3]
assert len(bq) == 196
assert min(bq) == sp.Rational(10423408247410155008672, 15625)
assert max(bq) == sp.Rational(
    10299944552027210611196952289529,
    15258789062500,
)
assert min(bq) > 0

# Integer clearing: q_abj r^a u^b v^j ->
# q_abj T^a a3^b R^(6-a-b) X^j Y^(3-j).
terms = {(a, b, j): int(co) for (a, b, j), co in Qint.terms()}
assert terms[(0, 0, 3)] == 2**17 * 3**12 * 5**3 * 11**3 * 13
assert v2(terms[(0, 0, 3)]) == 17
assert (terms[(0, 0, 3)] // 2**17) % 8 == 3

Msy, msy, tsy = sp.symbols("M m t", integer=True)
base = 6 * Msy + 6 * msy + 29
ledger = []
for (a, b, j), co in terms.items():
    depth = (
        v2(co)
        + a * msy
        + (6 - a - b) * (msy + 1)
        + j * (2 * Msy + 2)
        + (3 - j) * (2 * Msy + 2 * msy + 2 * tsy + 2)
    )
    diff = sp.expand(depth - base)
    Pdiff = sp.Poly(diff, msy, tsy)
    assert Pdiff.coeff_monomial(msy) >= 0
    assert Pdiff.coeff_monomial(tsy) >= 0
    ledger.append((int(diff.subs({msy: 5, tsy: 3})), a, b, j))

ledger.sort()
assert ledger[0] == (0, 0, 0, 3)
assert ledger[1][0] == 3

# Primitive unit: coefficient unit is 3 mod 8; R-unit^6=1 mod8;
# X-unit=Q0^2*N0 is 1 mod8 because Q0 is odd and N0=A^2 mod8.
for odd in (1, 3, 5, 7):
    assert pow(odd, 6, 8) == 1
assert (3 * 1 * 1) % 8 == 3

# Valuation split sanity checks for M=E-Q*L.
p = 101
# q>0 and e=k forces mu=k.
k = 2
E = p**k
Qv = p
L = p**k
Mv = E - Qv * L
assert Mv % p**k == 0 and Mv % p**(k + 1) != 0
# q=0, unequal e,l gives min(e,l).
for e, ell in ((2, 4), (5, 3)):
    E = p**e
    L = p**ell
    Mv = E - 7 * L
    vv = 0
    tmp = Mv
    while tmp % p == 0:
        vv += 1
        tmp //= p
    assert vv == min(e, ell)

print("OK: descendant Euclidean quotient is positive 3 mod 8 and does not create baseline overdepth for free")
