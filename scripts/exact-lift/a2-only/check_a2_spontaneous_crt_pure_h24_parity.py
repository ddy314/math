#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-h24-parity.md."""

import sympy as sp


def v2(n: int) -> int:
    n = abs(int(n))
    assert n
    return (n & -n).bit_length() - 1


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

# Recover the projective H24 component and its last linear subresultant.
R = sp.resultant(A63, B63, c)
_, primitive = sp.primitive(sp.Poly(R, s, z).as_expr(), s, z)
factors = sp.factor_list(primitive, s, z)[1]
H24 = factors[1][0]
h24 = sp.Poly(sp.expand(H24.subs({s: 1, z: u})), u, domain=sp.QQ)

Au = sp.Poly(sp.expand(A63.subs({s: 1, z: u, c: v})), v)
Bu = sp.Poly(sp.expand(B63.subs({s: 1, z: u, c: v})), v)
S1 = sp.Poly(sp.subresultants(Au.as_expr(), Bu.as_expr(), v)[-2], v)
a15 = sp.Poly(S1.coeff_monomial(v), u, domain=sp.QQ)
b17 = sp.Poly(S1.coeff_monomial(1), u, domain=sp.QQ)

Rv = sp.resultant(h24.as_expr(), a15.as_expr() * v + b17.as_expr(), u)
P24 = sp.Poly(Rv, v, domain=sp.QQ).clear_denoms()[1].primitive()[1]
if P24.LC() < 0:
    P24 = -P24

assert P24.degree() == 24
assert len(P24.terms()) == 25
assert P24.TC() > 0
assert P24.count_roots(0, sp.Rational(21, 20)) == 0

# Coefficient 2-adic ledger.  For p_j v^j, clearing v=X/Y gives p_j X^j Y^(24-j).
coeff = {mon[0]: int(co) for mon, co in P24.terms()}
assert set(coeff) == set(range(25))
assert v2(coeff[24]) == 99
assert (coeff[24] // 2**99) % 8 == 5

# In the dangerous branch delta=v2(Y)-v2(X)=2m+2t >= 16.
weighted_lower = [v2(coeff[j]) + (24 - j) * 16 for j in range(24)]
assert min(weighted_lower) == 109
assert min(weighted_lower) > 99

# Symbolic block-depth consequences used in the proof:
# v2(X)=2M+2, so 24*v2(X)+99 = 48M+147.
M = sp.symbols("M", integer=True)
assert sp.expand(24 * (2 * M + 2) + 99 - (48 * M + 147)) == 0

# The unique lowest term has odd unit 5 mod 8; X/2^(2M+2) is odd,
# and every odd unit to the 24th power is 1 mod 8.
for odd in (1, 3, 5, 7):
    assert pow(odd, 24, 8) == 1

print("OK: H24 compact carrier is positive with exact primitive orientation 5 mod 8")
