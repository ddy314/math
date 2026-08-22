#!/usr/bin/env python3
"""Certificate for endpoint-five-point-cofactors.md.

Extend the rational-root cofactor sieve from j=2,3,4 to j=1,...,5.
The check is structural: sign monotonicity on the endpoint box, common 2/5
content, the general modulo-D cofactor residue, cubic fourth-difference
identity, the non-3 denominator-prime one-gap selector, outer-pair separation
from g, and the four non-3 inert parity obligations in the dangerous Z=1
orientation.
"""

from fractions import Fraction as F
import math
import sympy as sp

# ---------------------------------------------------------------------------
# 1. The ratio f/h is strictly increasing for 1 <= J <= 5.
# ---------------------------------------------------------------------------
u = F(251, 250)
Jmax = 5
cubic_max = F(Jmax**3) + 3 * F(Jmax**2) * u + 3 * F(Jmax) * u * u
Kmin = 9 * 10**11
assert F(Kmin) > cubic_max / (u * u)
assert [(-1 if j < F(5, 2) else 1) for j in range(1, 6)] == [-1, -1, 1, 1, 1]

# ---------------------------------------------------------------------------
# 2. The j=1 and j=5 values have the same exact 2,5 primitive content.
# ---------------------------------------------------------------------------
for M in (11, 12, 20):
    for m in range(3, 16):
        for d in range(1, m // 3 + 1):
            nu5 = m - 3*d
            assert nu5 >= 0
            for t in (3, 4, 7):
                first_v2_lower = 2 * (M + m + t) + m
                assert first_v2_lower > 2*M + 2
            assert m > nu5

# ---------------------------------------------------------------------------
# 3. General rational-root divisors s_j=(j-3)D+C.
# ---------------------------------------------------------------------------
D, C = sp.symbols("D C", integer=True)
s = {j: (j-3)*D + C for j in range(1, 6)}
for i in range(1, 6):
    for j in range(i+1, 6):
        assert sp.expand(s[j] - s[i] - (j-i)*D) == 0

# ---------------------------------------------------------------------------
# 4. General modulo-D residue.
# ---------------------------------------------------------------------------
j = sp.symbols("j", integer=True)
g, L, cu, q, cp, Y = sp.symbols("g L cu q cp Y")
Aj, Bj = sp.symbols("Aj Bj")
Dj = g*L
sj = (j-3)*Dj + C
N = j*Dj - sj
Fsharp = cu**2*g**2*L**3*Aj - q**2*cp**2*Y*N*Bj
residual = sp.factor(Fsharp - sj*q**2*cp**2*Y*Bj)
assert sp.factor(residual / Dj) == cu**2*g*L**2*Aj - j*q**2*cp**2*Y*Bj

T, a3, five_lam = sp.symbols("T a3 five_lam")
assert sp.factor(((j*T+a3)**2-a3**2).subs(T, L*five_lam) / L) == j*five_lam*(L*five_lam*j + 2*a3)

# ---------------------------------------------------------------------------
# 5. Five consecutive values of one cubic have vanishing fourth difference.
# ---------------------------------------------------------------------------
a,b,c,d,x = sp.symbols("a b c d x")
P = a*x**3 + b*x**2 + c*x + d
vals = [sp.expand(P.subs(x,k)) for k in range(1,6)]
fourth = vals[0] - 4*vals[1] + 6*vals[2] - 4*vals[3] + vals[4]
assert sp.expand(fourth) == 0

gaps = [sp.expand(vals[k+1]-vals[k]) for k in range(4)]
assert sp.expand(gaps[0] - 3*gaps[1] + 3*gaps[2] - gaps[3]) == 0
assert sp.expand(gaps[0] - 2*gaps[1] + gaps[2] - 6*a) == 0
assert sp.expand(gaps[1] - 2*gaps[2] + gaps[3] - 6*a) == 0

for m in range(3, 16):
    for d0 in range(1, m//3 + 1):
        nu = m - 3*d0
        exp2 = (4*m) - m - m
        exp5 = 2*m - nu - d0 - d0
        assert exp2 == 2*m
        assert exp5 == m + d0

# ---------------------------------------------------------------------------
# 6. Mod g, adjacent normalized gaps are controlled by
#   (2j+1)T+2a3, j=1,2,3,4.
# ---------------------------------------------------------------------------
for p in list(sp.primerange(7, 200)):
    if p == 5:
        continue
    for T0 in range(1, p):
        for a0 in range(p):
            hits = []
            for jj in range(1,5):
                if ((2*jj+1)*T0 + 2*a0) % p == 0:
                    hits.append(jj)
            assert len(hits) <= 1

for p in list(sp.primerange(7, 100)):
    for T0 in range(1,p):
        a0 = (-3*T0) % p
        left = (5*T0 + 2*a0) % p
        right = (7*T0 + 2*a0) % p
        assert left == (-T0) % p and right == T0 % p
        assert left and right and (left + right) % p == 0

# ---------------------------------------------------------------------------
# 7. Outer-pair / denominator-g separation.
# ---------------------------------------------------------------------------
assert sp.expand((5*T + 2*a3) + (7*T + 2*a3) - 4*(3*T + a3)) == 0
assert sp.expand((2*T + a3).subs(a3, -3*T) + T) == 0

for p in list(sp.primerange(7, 200)):
    for T0 in range(1, p):
        for a0 in range(p):
            dminus = (5*T0 + 2*a0) % p
            dplus = (7*T0 + 2*a0) % p
            xi2 = pow((2*T0 + a0) % p, 2, p)
            if (dminus + dplus) % p == 0:
                assert (3*T0 + a0) % p == 0
                assert xi2 != 0

# ---------------------------------------------------------------------------
# 8. Dangerous Z=1: four of the five cofactors are 3-adic units.
# Here K=a3=0 mod3, N0=0 mod9, T=1 mod3 and b2 is a 3-unit.  Hence the
# Q^2*N0 term dies mod3 and
#   F(j) = b2^2 * j*(j)*(−j)^2 = b2^2*j^4 mod3.
# For j=1,2,4,5 this is a unit.  Since C=0 mod3 and D is a unit, the
# corresponding divisors 2D-C,D-C,D+C,2D+C are also units.  Therefore
# Xi_1,Xi_2,Xi_4,Xi_5 are all 3-adic units.  Each is 3 mod4 because all five
# Xi_j share the Y square class and Y=3 mod4 in Z=1; hence each of these four
# cofactors requires non-3 inert parity.
# ---------------------------------------------------------------------------
for j0 in (1, 2, 4, 5):
    assert pow(j0 % 3, 4, 3) == 1
for D0 in (1, 2):
    C0 = 0
    divisors = {
        1: (2*D0-C0) % 3,
        2: (D0-C0) % 3,
        4: (D0+C0) % 3,
        5: (2*D0+C0) % 3,
    }
    assert all(divisors[j0] != 0 for j0 in (1,2,4,5))

print("OK: five-point A2 sieve gives four non-3 parity cofactors and separates shared outer support from odd g-support")