#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-h24-projective.md."""

import sympy as sp


t, s, z, c = sp.symbols("t s z c")
K, zz = sp.symbols("K zz")
u, v = sp.symbols("u v")

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

Et = sp.Poly(sp.expand(E63.subs({K: s / t, zz: z / t}) * t**8), t)
L = sp.Poly(55 * t**2 + 18 * (z - s) * t + s**2 - 4 * s * z - c, t)
rem = sp.Poly(sp.rem(Et, L).as_expr(), t)
A63 = sp.expand(rem.coeff_monomial(t))
B63 = sp.expand(rem.coeff_monomial(1))

# Recover H4/H24 from the coefficient-singular resultant.
R = sp.resultant(A63, B63, c)
_, primitive = sp.primitive(sp.Poly(R, s, z).as_expr(), s, z)
factors = sp.factor_list(primitive, s, z)[1]
assert [(sp.Poly(f, s, z).total_degree(), e) for f, e in factors] == [(4, 1), (24, 1)]
H24 = factors[1][0]
h24 = sp.Poly(sp.expand(H24.subs({s: 1, z: u})), u, domain=sp.QQ)
assert h24.degree() == 24
assert len(h24.terms()) == 25
assert [(sp.Poly(f, u).degree(), e) for f, e in sp.factor_list(h24.as_expr(), u)[1]] == [(24, 1)]

# Projectivize A63,B63 and take the last positive-degree subresultant in v.
Au = sp.Poly(sp.expand(A63.subs({s: 1, z: u, c: v})), v)
Bu = sp.Poly(sp.expand(B63.subs({s: 1, z: u, c: v})), v)
subres = sp.subresultants(Au.as_expr(), Bu.as_expr(), v)
S1 = sp.Poly(subres[-2], v)
assert S1.degree() == 1

a15 = sp.Poly(S1.coeff_monomial(v), u, domain=sp.QQ)
b17 = sp.Poly(S1.coeff_monomial(1), u, domain=sp.QQ)
assert a15.degree() == 15
assert b17.degree() == 17

a15z = a15.clear_denoms()[1].primitive()[1]
b17z = b17.clear_denoms()[1].primitive()[1]
assert [(sp.Poly(f, u).degree(), e) for f, e in sp.factor_list(a15z.as_expr(), u)[1]] == [(15, 1)]
assert [(sp.Poly(f, u).degree(), e) for f, e in sp.factor_list(b17z.as_expr(), u)[1]] == [(17, 1)]

# Eliminate u.  This is the canonical projected P24(v).
Rv = sp.resultant(h24.as_expr(), a15.as_expr() * v + b17.as_expr(), u)
P24 = sp.Poly(Rv, v, domain=sp.QQ).clear_denoms()[1].primitive()[1]
if P24.LC() < 0:
    P24 = -P24

assert P24.degree() == 24
assert len(P24.terms()) == 25
assert [(sp.Poly(f, v).degree(), e) for f, e in sp.factor_list(P24.as_expr(), v)[1]] == [(24, 1)]

# Exact Sturm root counts: all four real roots are outside the endpoint interval.
assert P24.count_roots(-sp.oo, sp.oo) == 4
assert P24.count_roots(-7, -6) == 1
assert P24.count_roots(-6, -5) == 1
assert P24.count_roots(sp.Rational(6, 5), sp.Rational(5, 4)) == 1
assert P24.count_roots(16, 17) == 1
assert P24.count_roots(0, sp.Rational(21, 20)) == 0

print("OK: H24 projective singular component has no real endpoint norm-ratio root")
