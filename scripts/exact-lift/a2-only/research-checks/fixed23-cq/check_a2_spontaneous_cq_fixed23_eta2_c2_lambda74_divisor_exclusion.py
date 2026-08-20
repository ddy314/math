#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-lambda74-divisor-exclusion.md."""

import sympy as sp

lam = 74
cu = 3917
cq = 1587

S = 5 ** (3 * lam) + cq * cu
L = 2 ** (lam + 1) * 5**lam * cu

p16 = 1660311777398843
p21 = 755010757548746032247
p114 = int(
    "443275675908365257356310830167221246577649755270106234437033874498268569377246437010851938887432890877364857937953"
)

factors = {2: 8, 7: 1, 149: 1, p16: 1, p21: 1, p114: 1}

product = 1
for p, e in factors.items():
    product *= p**e
assert product == S

for p in (7, 149, p16, p21, p114):
    assert sp.isprime(p)

small = S // p114
assert small == 334708746929231021723648971080910156928768

# Exact strict centered interval comparisons.
assert 2 * small < 39 * L
assert 4 * p114 > 79 * L

# The explicit endpoints quoted in the proof.
assert L == int(
    "783400000000000000000000000000000000000000000000000000000000000000000000000000"
)
assert (39 * L) // 2 == int(
    "15276300000000000000000000000000000000000000000000000000000000000000000000000000"
)
assert (79 * L) // 4 == int(
    "15472150000000000000000000000000000000000000000000000000000000000000000000000000"
)

print(
    "OK: lambda=74, c_u=3917 has no source divisor in the centered 19.5--19.75 L_* interval"
)
