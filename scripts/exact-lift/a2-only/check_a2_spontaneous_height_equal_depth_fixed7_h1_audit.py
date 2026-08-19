#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-fixed7-h1-audit.md."""

import sympy as sp

k,l,j,k2 = sp.symbols("k l j k2", integer=True)
K = 2 + 7*k
D_over_N = 4 + 7*l

P = 6*K**2 - 36*K + 55
U_over_N = D_over_N*K - 1
Rplus_over_N = D_over_N*P - K*U_over_N
RPD_over_N2 = 55*D_over_N**2 - 36*D_over_N + 6

# First normalized digits.
assert sp.expand(P/7 - (42*k**2 - 12*k + 1)) == 0
assert sp.expand(U_over_N/7 - (7*k*l + 4*k + 2*l + 1)) == 0

# R+/7 modulo 7 is 2+3l; verify by coefficient reduction.
def mod_poly(expr, vars_, p):
    poly = sp.Poly(sp.expand(expr), *vars_)
    out = 0
    for mon, coeff in poly.terms():
        term = int(coeff) % p
        for var, exp in zip(vars_, mon):
            term *= var**exp
        out += term
    return sp.expand(out)

assert mod_poly(Rplus_over_N/7, [k,l], 7) == 3*l + 2

# Deep R+ forces l=4 mod7.
assert [(x) for x in range(7) if (2+3*x) % 7 == 0] == [4]

# With l=4, P and U exact-depth units differ by factor 2.
P0 = mod_poly((P/7).subs(l,4), [k], 7)
U0 = mod_poly((U_over_N/7).subs(l,4), [k], 7)
assert P0 == 2*k + 1
assert sp.expand(U0 - 2*P0) % 7 == 0
assert [x for x in range(7) if (int(P0.subs(k,x)) % 7) == 0] == [3]

# Second extra digit of RPD: d=32+49j, condition is 6+5j=0 mod7.
d = 32 + 49*j
RPD2 = 55*d**2 - 36*d + 6
assert mod_poly(RPD2/49, [j], 7) == 5*j + 6
assert [x for x in range(7) if (6+5*x) % 7 == 0] == [3]
assert (32 + 49*3) % 343 == 179

# Under d=179 mod343, R+/49 mod7 is 6(k-1)(k-3), independent of k2.
K2 = 2 + 7*k + 49*k2
d2 = 179
P2 = 6*K2**2 - 36*K2 + 55
U2 = d2*K2 - 1
Rplus2 = d2*P2 - K2*U2
next_digit = mod_poly(Rplus2/49, [k,k2], 7)
expected = sp.expand(6*(k-1)*(k-3))
assert sp.Poly(next_digit-expected,k,k2, modulus=7).is_zero

# Exact h=1 excludes k=3; only k=1 then gives one more R+ digit.
admissible_k = [x for x in range(7) if x != 3]
deep_k = [x for x in admissible_k if int(next_digit.subs({k:x,k2:0})) % 7 == 0]
assert deep_k == [1]

classes = sorted((2 + 7*x) % 49 for x in admissible_k)
assert classes == [2,9,16,30,37,44]
assert (2 + 7*1) % 49 == 9

print("OK: A2 fixed-7 h=1 extra-resultant branch collapses to D/N=179 mod343 and one deep E+ class K=9 mod49")
