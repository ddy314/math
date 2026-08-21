#!/usr/bin/env python3
"""Exact residue certificate for the A2 f-height intersection collapse.

This checks the algebra used in primitive-reduction.md §10:

* f-side prefix contact gives K^2-26 = -(2 a3/T)^2 at a height overlap;
* saturation gives a3/T = -9/2;
* reduced-numerator height contact gives K = 9/2;
* hence every such inert carrier prime divides 301 = 7*43.

The script also checks that the two surviving primes satisfy the older
quadratic-character necessary conditions, so the new reduction is genuinely
stronger than the character filter rather than a disguised contradiction.
"""

from fractions import Fraction

from sympy import factorint, legendre_symbol

K = Fraction(9, 2)
a3_over_T = Fraction(-9, 2)

prefix_side = K * K - 26
height_side = -(2 * a3_over_T) ** 2

gap = prefix_side - height_side
assert gap == Fraction(301, 4)
assert factorint(gap.numerator) == {7: 1, 43: 1}

for p in (7, 43):
    assert p % 4 == 3
    assert legendre_symbol(p, 23) == -1
    assert legendre_symbol(p, 5) * legendre_symbol(p, 11) == 1
    assert legendre_symbol(-55, p) == 1
    assert legendre_symbol(23, p) == 1

# 301 is squarefree at both surviving primes. Therefore a congruence
# p^t | 301, obtained by lifting all three contacts to depth t, forces t=1.
assert all(e == 1 for e in factorint(301).values())

print("OK: A2 f-height carrier support collapses to {7,43}, with no common second-order depth")
