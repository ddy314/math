#!/usr/bin/env python3
"""Certificate for spontaneous-crt-quotient-endpoint-parameterization.md."""

from fractions import Fraction

# Continuous coefficient kappa=s^2 w^3/(4x).
smin = Fraction(2499,250)
smax = Fraction(10,1)
wmin = Fraction(837,1000)
wmax = Fraction(843,1000)
xmin = Fraction(1,10)
xmax = Fraction(2,19)

kappa_min = smin**2 * wmin**3 / (4*xmax)
kappa_max = smax**2 * wmax**3 / (4*xmin)
assert kappa_min > 139
assert kappa_max < 150

# Combined coarse Q bounds use 139/17>8 and 150/14<11.
assert Fraction(139,17) > 8
assert Fraction(150,14) < 11

# Exponent bookkeeping:
# a_Delta = (s^2 w^3)/(4 x c_Q^3) * 2^(m-M) * 5^(4lambda+M).
# eta=2m-M and lambda=m-d give
# m-M=(eta-M)/2, 4lambda+M=3M+2eta-4d.
for M in range(11,25):
    for m in range(5,M+1):
        eta=2*m-M
        for d in range(1,m+1):
            lam=m-d
            assert 2*(m-M)==eta-M
            assert 4*lam+M==3*M+2*eta-4*d

# For fixed eta,d, growth in M along the parity-compatible subsequence M->M+2
# multiplies R by (125/sqrt(2))^2=15625/2 >1.
assert Fraction(15625,2) > 1

print("OK: A2 CRT quotient has a fixed normalized endpoint-lattice window")
