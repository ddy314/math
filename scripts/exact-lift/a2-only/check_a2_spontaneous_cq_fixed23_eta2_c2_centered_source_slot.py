#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md."""

from fractions import Fraction

cQ = 1587
Hlo = Fraction(997, 250)
Hhi = Fraction(1001, 250)
ylo = Fraction(249, 250)
yhi = Fraction(1, 1)
Glo = Fraction(9619, 1000)
Ghi = Fraction(9653, 1000)


def P(G, H, y):
    return G * G - 2 * H * G - Fraction(cQ, 100) * y

# Exact signs proving the G window.
assert P(Glo, Hlo, ylo) == Fraction(-2503, 1_000_000)
assert P(Ghi, Hhi, yhi) == Fraction(1837, 200_000)

wlo = Fraction(837, 1000)
whi = Fraction(843, 1000)
xlo = Fraction(20, cQ) * Glo * wlo
xhi = Fraction(20, cQ) * Ghi * whi

assert xlo > Fraction(1, 10)
assert xhi < Fraction(2, 19)

# Lower centered bound: theta/L < 79/4.
assert Fraction(2, 1) / xlo + Fraction(1, 1000) < Fraction(79, 4)
# Upper centered bound: varrho/L < 1/2.
assert Fraction(20, 1) - Fraction(2, 1) / xhi < Fraction(1, 2)

# Equivalent theta window and relative width.
lo_theta = Fraction(39, 2)
hi_theta = Fraction(79, 4)
assert Fraction(20, 1) - Fraction(1, 2) == lo_theta
assert Fraction(20, 1) - Fraction(1, 4) == hi_theta
assert (hi_theta - lo_theta) / lo_theta == Fraction(1, 78)

print("OK: A2 fixed-23 eta=2 c=2 centered source divisor slot is (19.5,19.75)*L_*")
