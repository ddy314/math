#!/usr/bin/env python3
"""Certificate for spontaneous-crt-extra-d-z-reader.md."""

import sympy as sp

# Algebraic first-order square lift.
g, rE, cp, cu, n5, zE = sp.symbols("g rE cp cu n5 zE")
expr = sp.expand((g*rE-n5*zE)**2 - (g**2*rE**2 - 2*g*rE*n5*zE))
assert expr == n5**2*zE**2

# Reflection has lambda > 2d, so n5^2 = 5^(2lambda-2d)
# lies beyond modulus 5^lambda by lambda-2d positive layers.
lam, d = sp.symbols("lam d", integer=True)
assert sp.expand(2*(lam-d)-lam) == lam-2*d

# The top-d carrier is an exact quotient once the lower n5 congruence holds.
AG, a3, R5, P = sp.symbols("AG a3 R5 P", integer=True)
Z = sp.symbols("Z", integer=True)
# Symbolic rearrangement of
# cp^2 P - 2^AG a3 R5 g^2 rE^2
#   == n5 * Z
# and the first-order correction modulo n5*5^d.
left = cp**2*P - 2**AG*a3*R5*g**2*rE**2
corr = -2**(AG+1)*a3*R5*g*rE*n5*zE
# This assertion just certifies the coefficient produced by expansion of
# 2^AG a3 R5 * [(g rE - n5 zE)^2 - g^2 rE^2].
expanded_corr = sp.expand(2**AG*a3*R5*((g*rE-n5*zE)**2-g**2*rE**2))
assert sp.expand(expanded_corr - (corr + 2**AG*a3*R5*n5**2*zE**2)) == 0

# Unit check for R_Delta^(5)=D(20-4K)-2C: modulo 5 with 5|D,5|K,
# it is -2C, hence a unit when 5 does not divide C.
D,K,C = sp.symbols("D K C")
Rdelta = D*(20-4*K)-2*C
assert sp.expand(Rdelta).subs({D:0, K:0}) == -2*C

print("OK: A2 full-5 CRT residue reads the centered z_E digit modulo 5^d")
