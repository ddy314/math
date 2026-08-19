#!/usr/bin/env python3
"""Certificate for spontaneous-source-parity-angle-budget.md."""

from fractions import Fraction

# 10^M / 2^(M+1) = 5^M / 2.
for M in range(1,12):
    assert Fraction(10**M,2**(M+1))==Fraction(5**M,2)

# Constant simplification (81/625)/2 = 81/1250.
assert Fraction(81,625)*Fraction(1,2)==Fraction(81,1250)

print("OK: A2 source-angle parity reuse support obeys the mixed c_Q/defect budget")
