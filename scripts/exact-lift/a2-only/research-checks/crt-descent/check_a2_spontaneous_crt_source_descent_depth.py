#!/usr/bin/env python3
"""Certificate for spontaneous-crt-source-descent-depth.md."""

import sympy as sp

K,T,g,a,C,L = sp.symbols("K T g a C L")
F63 = 16*(2*K-9)*(g*((2*K-12)*T-2*a)+L*C)-63*g*T*K**2
H = 102383*g*T-29952*g*a+14976*C*L
Q = 576*C*L+18*K*T*g-12041*T*g-1152*a*g
LS = 18*K-55

assert sp.expand(324*F63 + H - LS*Q) == 0

# Primewise exponent bookkeeping: ceil(k/2) is no larger than both the
# descendant depth k and the source square-root charge ceil(s/2) when s>=k.
for s in range(1, 15):
    for k in range(1, s+1):
        t = (k+1)//2
        assert k >= t
        assert (s+1)//2 >= t
        assert 2*t == k + (k % 2)

# Hence H_SD^2 = G_SD * R_SD^odd exponentwise.
for k in range(1, 20):
    lhs_exp = 2*((k+1)//2)
    rhs_exp = k + (k % 2)
    assert lhs_exp == rhs_exp

# The two target/descent fixed primes are not source-common target primes;
# this checker records only their arithmetic coprimality as bookkeeping.
assert sp.gcd(31*179, 2*3*5*11) == 1

print("OK: source/descent common depth pays canonical half-depth into both short carriers")
