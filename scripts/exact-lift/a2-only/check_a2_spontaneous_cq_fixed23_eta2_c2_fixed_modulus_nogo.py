#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-fixed-modulus-nogo.md."""

from fractions import Fraction

p4 = 23**4
m_min = 9

# D > (2389/50) * 20^m, hence 3D/250 exceeds this exact value.
lower = Fraction(3 * 2389, 12500) * 20**m_min
assert lower == 293_560_320_000
assert lower > p4

# The fixed modulus itself.
assert p4 == 279_841

# m=9 is the smallest class compatible with M=2m-2=16 mod22.
assert (2 * m_min - 2) % 22 == 16
for m in range(0, m_min):
    assert (2 * m - 2) % 22 != 16 or (2 * m - 2) < 11

# Any residue class modulo p^4 has a positive representative <= p^4,
# while the allowed C interval has length strictly greater than p^4.
for residue in (0, 1, 3, 17, p4 - 1):
    r = residue % p4
    if r == 0:
        r = p4
    assert 0 < r <= p4 < lower

print("OK: fixed 23^4 orientation residue is asymptotically and already minimally too small to prune the C interval")
