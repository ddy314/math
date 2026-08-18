#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-source-window.md."""

from fractions import Fraction
import sympy as sp


def bounds(lam):
    lo = Fraction(837, 1000) * Fraction(5, 4) ** lam / 3174
    hi = Fraction(843, 1000) * Fraction(5, 4) ** lam / 3174
    return lo, hi


def strict_integer_interval(lo, hi):
    first = lo.numerator // lo.denominator + 1
    last = (hi.numerator - 1) // hi.denominator
    return range(first, last + 1)


def valid_source_content(n):
    if n <= 0 or n % 2 == 0 or n % 5 == 0:
        return False
    return all(p % 4 == 1 for p in sp.factorint(n))

# lambda is 8 mod11.
assert all((lam - 8) % 11 == 0 for lam in (8, 19, 30, 41, 52, 63, 74))

# No positive integer source content before lambda=52.
for lam in (8, 19, 30, 41):
    lo, hi = bounds(lam)
    assert list(strict_integer_interval(lo, hi)) == []

# First three surviving source windows.
expected = {
    52: [29],
    63: [337],
    74: [3917, 3929],
}
for lam, want in expected.items():
    lo, hi = bounds(lam)
    got = [n for n in strict_integer_interval(lo, hi) if valid_source_content(n)]
    assert got == want

# Exact primality / 1 mod4 audit for the listed contents.
for n in (29, 337, 3917, 3929):
    assert sp.isprime(n)
    assert n % 4 == 1

# Corresponding M,m values.
assert [(2*l, l+1) for l in (52,63,74)] == [(104,53),(126,64),(148,75)]

print("OK: A2 fixed-23 eta=2 c=2 has lambda>=52 and certified first source-content windows")
