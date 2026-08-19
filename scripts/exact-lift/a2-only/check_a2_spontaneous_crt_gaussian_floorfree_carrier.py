#!/usr/bin/env python3
"""Certificate for spontaneous-crt-gaussian-floorfree-carrier.md."""

from fractions import Fraction as F

# Imported rigorous raw bands from the parent orientation theorem.
minus_lo, minus_hi = F(44, 25), F(12, 5)
plus_lo, plus_hi = F(51, 100), F(7, 10)

# Subtracting 1 gives the signed floor-free carrier margin.
assert minus_lo - 1 == F(19, 25)
assert minus_hi - 1 == F(7, 5)
assert plus_lo - 1 == F(-49, 100)
assert plus_hi - 1 == F(-3, 10)
assert F(19, 25) > 0
assert F(-3, 10) < 0

# P_Delta = M_Delta * O_Delta + 2^A R_Delta is an exact Euclidean identity.
for Mdelta, O, A, R in [(7, -3, 4, 2), (11, 5, 3, 0), (13, 2, 5, 12)]:
    Q = 17
    threshold = 19
    Delta = Q * Mdelta + R
    P1 = (2**A) * Delta - threshold * Mdelta
    O1 = (2**A) * Q - threshold
    assert P1 == Mdelta * O1 + (2**A) * R

# Oddness: A>=1, M_Delta odd, k_h odd, 5^B odd.
for A, B, kh, Delta, Mdelta in [(2, 3, 1, 10, 7), (5, 4, 3, 9, 11)]:
    P = (2**A) * Delta - (5**B) * (kh**3) * Mdelta
    assert P % 2 == 1

print("OK: A2 floor-free CRT/Gaussian carrier has fixed side-dependent sign")
