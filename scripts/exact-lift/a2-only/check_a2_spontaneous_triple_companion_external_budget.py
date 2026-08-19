#!/usr/bin/env python3
"""Certificate for spontaneous-triple-companion-external-budget.md."""

import sympy as sp

K, H, cu, z, D, C = sp.symbols("K H cu z D C")

BW = cu**2 * (5 * K**2 - 36 * K + 55) + z**2 * K**2
expanded = sp.expand(4 * BW.subs(K, (H + 9) / 2))
target = (
    (5 * cu**2 + z**2) * H**2
    + 18 * (cu**2 + z**2) * H
    + (81 * z**2 - 23 * cu**2)
)
assert sp.factor(expanded - target) == 0

A = 15 * D - 2 * C
B = 12 * D - 4 * C
S23 = 81 * z**2 - 23 * cu**2
R23 = A * z + B * cu
R23c = A * z - B * cu
F23 = 1204 * C**2 - 6396 * C * D + 6489 * D**2

assert sp.factor(A**2 * S23 - 81 * R23 * R23c - cu**2 * F23) == 0
assert sp.factor(sp.discriminant(F23, C)) == 2**6 * 3**8 * 23 * D**2

# Reciprocity sign for inert p (p=3 mod4) against 23=3 mod4:
# (23/p)=+1 forces (p/23)=-1.  Check representative compatible primes.
for p in list(sp.primerange(7, 500)):
    if p in (23,):
        continue
    if p % 4 == 3 and sp.legendre_symbol(23, p) == 1:
        assert sp.legendre_symbol(p, 23) == -1

print("OK: A2 generic external triple companion reuse pays a short central and F23 depth")
