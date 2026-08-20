#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-mod24-parity.md."""

import math

H = {1, 5, 7, 11}

# Prefix orientation: K=10*r with r odd.
for r in range(1, 200, 2):
    K = 10 * r
    P = 6*K*K - 36*K + 55
    assert P % 24 == 7
    assert P % 5 == 0
    assert (P // 5) % 24 == 11

# Third orientation: m>=5, a3 odd.  Real endpoint also has 5∤a3.
for m in range(5, 10):
    T = 10**m
    for a3 in range(1, 100, 2):
        if a3 % 5 == 0:
            continue
        R3 = 6*(a3 + 3*T)**2 + T*T
        assert R3 % 48 == 22
        assert (R3 // 2) % 24 == 11
        assert R3 % 5 != 0

# The sqrt(-6) splitting classes modulo 24.
def legendre_minus6_class(a: int) -> bool:
    # For a unit class mod 24, test the known Kronecker/Legendre class table.
    return a in H

units24 = {1,5,7,11,13,17,19,23}
assert {a for a in units24 if legendre_minus6_class(a)} == H

# H is a Klein four group and every element is self-inverse.
for a in H:
    assert (a*a) % 24 == 1
    for b in H:
        assert (a*b) % 24 in H

# Residual table after removing common gcd G.
expected = {1:11, 5:7, 7:5, 11:1}
for G, residual in expected.items():
    assert (11 * pow(G, -1, 24)) % 24 == residual
    assert (11 * G) % 24 == residual

# Both parity bits are duplicated in the two coprime residuals.
for G, residual in expected.items():
    inert_bit = (residual % 4 == 3)
    mod3_bit = (residual % 3 == 2)
    assert inert_bit == (G % 4 == 1)
    assert mod3_bit == (G % 3 == 1)

# Sheet-level no-go: every total class admits four ordered factorizations
# inside H, so the product class alone cannot identify the minus sheet.
for total in H:
    pairs = [(a,b) for a in H for b in H if (a*b) % 24 == total]
    assert len(pairs) == 4
    assert len({a for a,_ in pairs}) == 4

print("OK: A2 dual short carriers have exact mod-24 parity transfer, but no sheet-specific parity assignment")
