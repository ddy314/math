#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-projective-depth-reader.md."""

import sympy as sp


# Universal rational-root side.
K, zeta, J, R = sp.symbols("K zeta J R")
ferr, lerr = sp.symbols("ferr lerr")
U = 2 * K - 9

R0 = K**2 - (18 + 4 * zeta) * K + 18 * zeta + 55
J0 = (K**2 - 64 * K * zeta - 576 * K + 288 * zeta + 1296) / (16 * U)

Phi = lambda jj, RR: sp.expand(jj * (jj + 2 * zeta) * (K - jj) ** 2 - RR * (jj + zeta) ** 2)

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

# Exact universal-cubic identity.
assert sp.factor(Phi(J0, R0) - E63 / (65536 * U**4)) == 0

# Descendant residual F_Delta solves J0-J = F_Delta/U exactly.
Fdelta = U * (U - J - 2 * zeta) - sp.Rational(63, 16) * K**2
assert sp.factor(J0 - J - Fdelta / U) == 0

# Projective branch error satisfies R0-R = K^2 L_proj at the actual point.
r, u, v = sp.symbols("r u v")
Lproj = 55 * r**2 + 18 * (u - 1) * r + 1 - 4 * u - v
actual_L = sp.factor(K**2 * Lproj.subs({r: 1 / K, u: zeta / K, v: R / K**2}))
assert sp.expand(actual_L - (R0 - R)) == 0

# Error transport: after replacing J0=J+f/U and R0=R+K^2*l,
# Phi(J0,R0)-Phi(J,R) has no constant term in the two errors.
transport = sp.together(
    Phi(J + ferr / U, R + K**2 * lerr) - Phi(J, R)
)
num, den = transport.as_numer_denom()
Perr = sp.Poly(sp.expand(num), ferr, lerr)
assert Perr.coeff_monomial(1) == 0
for (ef, el), coeff in Perr.terms():
    if coeff:
        assert ef + el >= 1
assert sp.factor(den).has(U)

# Projective Euclidean remainder and exact local resultant identity.
Eproj = sp.Poly(sp.expand(E63.subs({K: 1 / r, zeta: u / r}) * r**8), r)
Lp = sp.Poly(Lproj, r)
rem = sp.Poly(sp.rem(Eproj, Lp).as_expr(), r)
assert rem.degree() == 1
A = rem.coeff_monomial(r)
B = rem.coeff_monomial(1)
M = A * r + B

Xraw = sp.expand(sp.resultant(Lp.as_expr(), M, r))
identity = sp.expand(A**2 * Lproj - A * sp.diff(Lproj, r) * M + 55 * M**2)
assert sp.expand(Xraw - identity) == 0

# The fixed resultant content is exactly 5^7*11^7, so genuine p!=5,11
# sees the same valuation after primitive normalization.
content = 0
for coeff in sp.Poly(Xraw, u, v).coeffs():
    content = sp.igcd(content, abs(int(coeff)))
assert content == 5**7 * 11**7

# Synthetic valuation sanity check for the local identity outside singular gates:
# unequal depths cannot cancel because the unique lowest term is visible.
p = 101
Aunit = 7
Lprime = 13
for ell, mu in ((1, 3), (2, 5), (4, 1), (5, 2)):
    Lval = p**ell
    Mval = p**mu
    Xval = Aunit**2 * Lval - Aunit * Lprime * Mval + 55 * Mval**2
    vp = 0
    tmp = Xval
    while tmp % p == 0:
        vp += 1
        tmp //= p
    assert vp == min(ell, mu)

print("OK: descendant common baseline depth enters the projective carrier; generic overdepth is equal-depth resonance")
