#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-lambda52-divisor-exclusion.md."""

import sympy as sp

lam = 52
cu = 29

S = 5 ** (3 * lam) + 1587 * cu
L = 2 ** (lam + 1) * 5**lam * cu
lo2 = 39 * L          # lower bound is lo2 / 2
hi4 = 79 * L          # upper bound is hi4 / 4

P72 = int(
    "600954647989450344901853769984896357520599617802323154990245217256098773"
)

factors = {
    2: 3,
    311: 1,
    1013: 1,
    1540787: 1,
    4691120092228268769101767: 1,
    P72: 1,
}

prod = 1
for p, e in factors.items():
    prod *= p**e
assert prod == S

for p in factors:
    assert sp.isprime(p)

small = S // P72
assert small == 18217088908728795407321637435454176376

# Exact centered-window comparisons without floating point.
assert 2 * small < lo2
assert 4 * P72 > hi4

# Optional exact decimal values recorded in the proof.
assert L == 580000000000000000000000000000000000000000000000000000
assert lo2 // 2 == 11310000000000000000000000000000000000000000000000000000
assert hi4 // 4 == 11455000000000000000000000000000000000000000000000000000

print("OK: A2 fixed-23 eta=2 c=2 lambda=52 source state has a complete divisor gap")
