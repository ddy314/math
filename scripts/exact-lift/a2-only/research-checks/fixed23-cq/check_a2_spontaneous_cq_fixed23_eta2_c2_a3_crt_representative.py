#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md."""

import sympy as sp

# ---------------------------------------------------------------------------
# 1. Eliminate C from the binary phases.
# ---------------------------------------------------------------------------
g, a, theta, cu = sp.symbols("g a theta cu", integer=True)
cQ = 1587
A0 = g / 2 - a

# A0^2 + g*a = g^2/4 + a^2.
assert sp.expand(A0**2 + g * a - (g**2 / 4 + a**2)) == 0

# If g*theta = 5^(3 lambda)+cQ*cu, then
# -theta*A0^2 = 5^(3lambda)*a is equivalent to F2(a)=0.
P = sp.symbols("P")  # P stands for 5^(3 lambda)
raw = sp.expand(-theta * A0**2 - P * a)
raw = sp.expand(raw.subs(P, g * theta - cQ * cu))
F2 = sp.expand(theta * (g**2 / 4 + a**2) - cQ * cu * a)
assert sp.expand(raw + F2) == 0

# Derivative is always odd for odd theta,a,cQ,cu.
Fp = sp.diff(F2, a)
assert sp.expand(Fp - (2 * theta * a - cQ * cu)) == 0
# mod 2: even - odd = 1.
assert (-cQ) % 2 == 1

# ---------------------------------------------------------------------------
# 2. Unique 2-adic root: brute certification for generic odd unit samples.
# This is a finite sanity check; the proof uses ordinary Hensel via F' odd.
# ---------------------------------------------------------------------------
def roots_mod_2n(bits, g0, th0, cu0):
    mod = 2**bits
    roots = []
    for a0 in range(1, mod, 2):
        val = (th0 * ((g0 * g0 // 4) + a0 * a0) - cQ * cu0 * a0) % mod
        if val == 0:
            roots.append(a0)
    return roots

for g0 in (4, 8, 12, 20):
    for th0 in (1, 3, 5, 7):
        for cu0 in (1, 5, 9, 13):
            for bits in range(1, 8):
                roots = roots_mod_2n(bits, g0, th0, cu0)
                assert len(roots) == 1

# ---------------------------------------------------------------------------
# 3. CRT scale identity.
# ---------------------------------------------------------------------------
lam = sp.symbols("lam", integer=True, positive=True)
m = lam + 1
T = 10 ** m
M3 = 2**m * 5 ** (lam - 1)
assert sp.simplify(T / M3 - 25) == 0
assert sp.simplify((T / 250) / M3 - sp.Rational(1, 10)) == 0

# Concrete integer instances of the scale identity.
for l in (8, 19, 30):
    mm = l + 1
    TT = 10**mm
    MM3 = 2**mm * 5**(l - 1)
    assert TT == 25 * MM3
    assert TT // 250 == MM3 // 10

print("OK: unique binary a3 Hensel root and T/25 CRT representative scale certified")
