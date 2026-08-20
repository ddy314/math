#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-transport-resonance.md."""

import sympy as sp


def v2(n: int) -> int:
    n = abs(int(n))
    assert n
    return (n & -n).bit_length() - 1


K, zeta, J, R = sp.symbols("K zeta J R")
F, Lerr = sp.symbols("F Lerr")
U = 2 * K - 9

Phi = J * (J + 2 * zeta) * (K - J) ** 2 - R * (J + zeta) ** 2
PhiJ = sp.diff(Phi, J)
transport = sp.expand(
    Phi.subs({J: J + F / U, R: R + K**2 * Lerr}) - Phi
)

# Constant term is zero and linear coefficients are exactly as claimed.
P = sp.Poly(transport, F, Lerr)
assert P.coeff_monomial(1) == 0
assert sp.factor(P.coeff_monomial(F) - PhiJ / U) == 0
assert sp.factor(P.coeff_monomial(Lerr) + K**2 * (J + zeta) ** 2) == 0
for (ef, el), coeff in P.terms():
    if ef + el >= 2:
        assert coeff != 0

# J+zeta singular split on the exact root.
# If zeta=-J, Phi=-J^2(K-J)^2.
assert sp.factor(Phi.subs(zeta, -J) + J**2 * (K - J) ** 2) == 0

Fdelta = U * (U - J - 2 * zeta) - sp.Rational(63, 16) * K**2
Lk = K**2 - 576 * K + 1296
GD = 11 * K**2 - 240 * K + 432
assert sp.factor(16 * Fdelta.subs({J: 0, zeta: 0}) - Lk) == 0
assert sp.factor(16 * Fdelta.subs({J: K, zeta: -K}) - 3 * GD) == 0

# Universal cubic and descendant first-layer approximations.
R0 = K**2 - (18 + 4 * zeta) * K + 18 * zeta + 55
J0 = (K**2 - 64 * K * zeta - 576 * K + 288 * zeta + 1296) / (16 * U)
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

PhiJ0 = sp.together(PhiJ.subs({J: J0, R: R0}))
numPJ, denPJ = PhiJ0.as_numer_denom()
numPJ = sp.primitive(sp.Poly(sp.expand(numPJ), K, zeta).as_expr(), K, zeta)[1]
assert sp.factor(denPJ) == 1024 * U**3

H2 = 47 * K**2 + 144 * K - 416
H10 = (
    388341 * K**10
    - 601739280 * K**9
    + 229469500800 * K**8
    + 1907909697024 * K**7
    + 388001070336 * K**6
    + 472180427182080 * K**5
    - 5611474473205760 * K**4
    + 24390734431518720 * K**3
    - 51182973630480384 * K**2
    + 52664489116434432 * K
    - 21375786688708608
)
assert sp.Poly(H10, K).is_irreducible

res = sp.factor(sp.resultant(E63, numPJ, zeta))
expected = -2**43 * 3**2 * U**13 * Lk**2 * GD**2 * H2 * H10
assert sp.expand(res - expected) == 0

# Low tangent 2-adic orientation.
k0 = sp.symbols("k0", integer=True)
H2k = sp.expand(H2.subs(K, 2 * k0))
# H2/4 = 47 k0^2 + 72 k0 -104; for odd k0, latter terms vanish mod 8.
assert sp.expand(H2k / 4 - (47 * k0**2 + 72 * k0 - 104)) == 0
for odd in (1, 3, 5, 7):
    assert int((47 * odd**2 + 72 * odd - 104) % 8) == 7

# High tangent: unique 2-adic lowest term is leading K^10.
ledger = []
for (power,), coeff in sp.Poly(H10, K).terms():
    ledger.append((v2(int(coeff)) + power, power))
ledger.sort()
assert ledger[0] == (10, 10)
assert ledger[1][0] == 13
assert 388341 % 8 == 5
for odd in (1, 3, 5, 7):
    assert pow(odd, 10, 8) == 1

# Elementary positivity inequalities used for K>=2000.
KK = 2000
assert 388341 * KK - 601739280 > 0
assert 229469500800 * KK**4 > 5611474473205760
assert 1907909697024 * KK**5 > 51182973630480384
assert 472180427182080 * KK**5 > 21375786688708608

print("OK: transported overdepth is a normalized linear resonance; tangent singularity reduces to H2/H10")
