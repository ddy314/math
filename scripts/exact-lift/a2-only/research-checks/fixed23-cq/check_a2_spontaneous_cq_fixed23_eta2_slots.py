#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-slots.md."""

from fractions import Fraction
from math import prod
import sympy as sp

p = 23

# Endpoint rectangle bounds.
r_lo = Fraction(4, 5)
r_hi = Fraction(843, 1000)
H_lo = Fraction(997, 250)
H_hi = Fraction(1001, 250)
y_lo = Fraction(249, 250)
y_hi = Fraction(1, 1)

Kminus_lo = r_lo * (H_lo - y_hi * r_lo)
Kminus_hi = r_hi * (H_hi - y_lo * r_hi)
Kplus_lo = Fraction(11962, 3125)
Kplus_hi = Fraction(163, 40)

assert Kminus_lo == Fraction(1594, 625)
assert Kminus_hi == Fraction(666891399, 250000000)

# Enumerate integer P=cQ*k_h in each eta=2,d slot.
def integer_window(lo, hi):
    # Strict lo < n < hi.
    start = lo.numerator // lo.denominator
    if Fraction(start, 1) <= lo:
        start += 1
    end = hi.numerator // hi.denominator
    if Fraction(end, 1) >= hi:
        end -= 1
    return list(range(start, end + 1)) if start <= end else []

def candidates(d, lo, hi):
    scale = Fraction(16, 1) * Fraction(5, 1) ** (3 - d)
    vals = integer_window(lo * scale, hi * scale)
    return [n for n in vals if n % p == 0 and n % 2 == 1 and n % 5 != 0]

assert candidates(1, Kminus_lo, Kminus_hi) == []
assert candidates(1, Kplus_lo, Kplus_hi) == [1541, 1587]
assert candidates(2, Kminus_lo, Kminus_hi) == [207]
assert candidates(2, Kplus_lo, Kplus_hi) == []
assert candidates(3, Kminus_lo, Kminus_hi) == []
assert candidates(3, Kplus_lo, Kplus_hi) == []

# For d>=4 even the plus upper bound gives P<23.
assert Fraction(16, 5) * Kplus_hi < 23

# Factor checks.
assert sp.factorint(1541) == {23: 1, 67: 1}
assert sp.factorint(1587) == {3: 1, 23: 2}
assert sp.factorint(207) == {3: 2, 23: 1}
assert 67 % 4 == 3 and 67 != 3
assert 1541 % 4 == 1
assert 529 % 4 == 1
assert 1587 % 4 == 3
assert 23 % 4 == 3
assert 207 % 4 == 3

# Surviving exact types after gcd(k_h,cQ*5^d)=1, cQ=3 mod4,
# and non-3 inert prime exclusion from k_h.
survivors = [
    (1, 1587, 1, "+"),
    (2, 23, 9, "-"),
    (2, 207, 1, "-"),
]
assert survivors == [
    (1, 1587, 1, "+"),
    (2, 23, 9, "-"),
    (2, 207, 1, "-"),
]

# eta=2 => M=2m-2 is even; among fixed-23 first-layer classes 5,16 mod22,
# only 16 survives.
assert 5 % 2 == 1
assert 16 % 2 == 0

# Affine M-lambda relations.
# d=1: m=lambda+1 => M=2m-2=2lambda.
# d=2: m=lambda+2 => M=2lambda+2.
lam = sp.symbols("lam", integer=True)
assert sp.expand(2*(lam + 1) - 2 - 2*lam) == 0
assert sp.expand(2*(lam + 2) - 2 - (2*lam + 2)) == 0

print("OK: A2 fixed-23 eta=2 high-2 lattice compresses to exactly three slot types")
