#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md."""

import sympy as sp

p = 23

# ---------------------------------------------------------------------------
# 1. Exact finite-order high-2 bridge
# ---------------------------------------------------------------------------
K, rho, q2, N, T = sp.symbols("K rho q2 N T")
A = (K - 9 * N) / 10
B = -2 * N + p**2 * q2

Hminus = sp.expand(
    15 * B**2 * rho**2
    - 2 * B * K * T**2 * q2
    - 2 * p**2 * A * T**2 * q2**2
)
Hplus = sp.expand(
    15 * B**2 * rho**2 * (rho + 2)
    - 2 * B * rho * K * T**2 * q2
    - 2 * p**2 * A * T**2 * q2**2 * (rho + 2)
)

# First fixed-23 layer: N=4, B=15, T^2=9, K=16 mod23.
r, q = sp.symbols("r q")
hm = sp.expand(Hminus.subs({N: 4, K: 16, T**2: 9, rho: r, q2: q}))
hp = sp.expand(Hplus.subs({N: 4, K: 16, T**2: 9, rho: r, q2: q}))

# Mod 23 the bridges are equivalent to rho^2=16 q2 and
# rho(rho+2)=16 q2.
def coeffs_mod(poly, *gens):
    return [int(c) % p for c in sp.Poly(sp.expand(poly), *gens).coeffs()]

# Hminus - 17*(r^2-16q) is 0 mod23.
assert all(c == 0 for c in coeffs_mod(hm - 17 * (r**2 - 16 * q), r, q))
# Hplus - 17*r*(r(r+2)-16q) is 0 mod23.
assert all(c == 0 for c in coeffs_mod(hp - 17 * r * (r * (r + 2) - 16 * q), r, q))

# ---------------------------------------------------------------------------
# 2. M mod506 -> h_N -> kappa and the two forced depth-1 classes
# ---------------------------------------------------------------------------
inv9 = pow(9, -1, p)
inv16 = pow(16, -1, p)


def plus_rho(kappa):
    den = (1 + 14 * kappa) % p
    if den == 0:
        return None
    return (-11 * pow(den, -1, p)) % p


def minus_rho(kappa):
    den = (1 + 14 * kappa) % p
    if den == 0:
        return None
    return ((9 + 18 * kappa) * pow(den, -1, p)) % p

bad = []
survivors = []
for j in range(p):
    Mres = 16 + 22 * j
    hN = (5 + 3 * j) % p
    kappa = ((16 * hN + 22) * inv9) % p

    if kappa in (11, 18):
        bad.append((Mres, kappa))
        continue

    den = (1 + 14 * kappa) % p
    assert den != 0

    rp = plus_rho(kappa)
    rm = minus_rho(kappa)
    assert rp not in (None, 0, p - 2)
    assert rm not in (None, 0)
    # The minus chart itself never takes rho=-2.
    assert rm != p - 2

    qplus = (rp * (rp + 2) * inv16) % p
    qminus = (rm * rm * inv16) % p
    assert qplus != 0
    assert qminus != 0

    # Augmented triangular Jacobian.
    Jaug = ((-9) * den * (-16)) % p
    assert Jaug != 0

    survivors.append((Mres, kappa, rp, qplus, rm, qminus, Jaug))

assert sorted(bad) == [(170, 18), (236, 11)]
assert len(survivors) == 21

# Old simultaneous-gate class M=302 has kappa=4, rho=-1 in both charts,
# while the canonical high-2 bridge records orientation through q2.
row302 = [row for row in survivors if row[0] == 302]
assert len(row302) == 1
Mres, kappa, rp, qplus, rm, qminus, Jaug = row302[0]
assert kappa == 4
assert rp == rm == p - 1
assert qplus == 10
assert qminus == 13
assert Jaug != 0

print(
    "OK: A2 fixed-23 eta=2 c=2 high-2 bridge is smooth after first blow-up; "
    "only M=170,236 mod506 force depth 1"
)
