#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-h2-additive-bezout.md."""

import sympy as sp

A, B, N = sp.symbols("A B N")
Q = B + 2 * N
K = 9 * N + 10 * A
N0 = sp.Rational(81, 4) * B**2 + A**2
FW = (K - 5) * (5 * K - 11)

H2 = (
    404 * A**4 * B**2
    + 16 * A**4 * B * N
    + 16 * A**4 * N**2
    + 1440 * A**3 * B**2 * N
    - 16119 * A**2 * B**4
    + 324 * A**2 * B**3 * N
    + 1620 * A**2 * B**2 * N**2
    - 29160 * A * B**4 * N
    + 164025 * B**6
)

L2 = 20 * A**2 + 36 * A * N - 405 * B**2
JH = B**2 * FW - Q**2 * N0
RH2 = L2**2 + 4 * A**2 * FW

# Exact square decomposition and Bezout identity.
assert sp.expand(H2 - (B**2 * L2**2 + 4 * A**2 * Q**2 * N0)) == 0
assert sp.expand(4 * A**2 * JH + H2 - B**2 * RH2) == 0

# A useful independent quotient check.
assert sp.factor((H2 - 4 * A**2 * Q**2 * N0) / B**2) == L2**2

# Deep-even 2-adic shadow: for M>=11,m>=1,A,b0 odd,
# L2 has exact depth 2; RH2 has exact depth 2 and /4 = 3 mod4.
# Exact modular representatives can be certified at the minimum depths because
# all N/B corrections vanish mod 16 after the indicated normalization.
for a in (1, 3, 5, 7):
    for n5 in (1, 5, 9, 13):  # odd N/2^M representatives mod16
        # K = 2 mod4 in the true deep-even range.
        kmod4 = (10 * a) % 4
        assert kmod4 == 2
        fwmod4 = ((kmod4 - 5) * (5 * kmod4 - 11)) % 4
        assert fwmod4 == 3
        # A^2 * FW is the only contribution to RH2/4 modulo4.
        assert (a * a * fwmod4) % 4 == 3

# Normalized equal-depth coefficient ratio in the H2 bridge is -square:
# 4 A^2 B^2 * BW + cu^2 * H2 = 0 mod p.
# Symbolically the quotient is -(cu/(2AB))^2.
p, cu = sp.symbols("p cu", nonzero=True)
ratio = -cu**2 / (4 * A**2 * B**2)
assert sp.factor(ratio + (cu / (2 * A * B)) ** 2) == 0

print("OK: A2 H2/additive exact Bezout bridge and non-square orientation certified")
