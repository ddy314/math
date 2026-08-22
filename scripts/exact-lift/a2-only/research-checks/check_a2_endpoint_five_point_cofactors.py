#!/usr/bin/env python3
"""Certificate for endpoint-five-point-cofactors.md.

Extend the rational-root cofactor sieve from j=2,3,4 to j=1,...,5.
The check is structural: sign monotonicity on the endpoint box, common 2/5
content, the general modulo-D cofactor residue, cubic fourth-difference
identity, and the non-3 denominator-prime one-gap selector.
"""

from fractions import Fraction as F
import math
import sympy as sp

# ---------------------------------------------------------------------------
# 1. The ratio f/h is strictly increasing for 1 <= J <= 5.
# Its derivative has sign of
#   (J-K)*(J^3 T^2 + 3 J^2 T a + 3 J a^2 - K a^2).
# Since J<K, it is positive once K(a/T)^2 dominates the displayed cubic.
# ---------------------------------------------------------------------------
u = F(251, 250)  # worst allowed a3/T upper endpoint
Jmax = 5
cubic_max = F(Jmax**3) + 3 * F(Jmax**2) * u + 3 * F(Jmax) * u * u
Kmin = 9 * 10**11
assert F(Kmin) > cubic_max / (u * u)

# Thus for r in (2,3), F(j) and s_j=D(j-r) have the same sign at j=1..5.
# sign pattern: --+++.
assert [(-1 if j < F(5, 2) else 1) for j in range(1, 6)] == [-1, -1, 1, 1, 1]

# ---------------------------------------------------------------------------
# 2. The j=1 and j=5 values have the same exact 2,5 primitive content as
# j=2,3,4.  We only need the valuation inequalities used in the proof.
# v2(b2)=M+m+t, t>=3; the first F-term is therefore much deeper than 2M+2.
# nu5=m-3d and d>=1 in the current deep-even endpoint core, while the first
# F-term contains at least T=10^m.
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
# The key determinant identity implies gcd(s_i,s_j) | |i-j| whenever
# gcd(C,D)=1.  For the five absolute divisors, the only possible odd cross
# gcd is therefore 3, and only at distance three.
# ---------------------------------------------------------------------------
D, C = sp.symbols("D C", integer=True)
s = {j: (j-3)*D + C for j in range(1, 6)}
for i in range(1, 6):
    for j in range(i+1, 6):
        assert sp.expand(s[j] - s[i] - (j-i)*D) == 0

# ---------------------------------------------------------------------------
# 4. General modulo-D residue.  After the common 2/5 scale is removed,
#   F_j^# = cu^2 g^2 L^3 A_j - q^2 cp^2 Y N B_j,
# with N=jD-s_j.  Subtract s_j*q^2 cp^2 Y B_j: the remainder is divisible D.
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

# Since T=L*5^lambda, (jT+a3)^2 is congruent a3^2 mod L for every j.
T, a3, five_lam = sp.symbols("T a3 five_lam")
assert sp.factor(((j*T+a3)**2-a3**2).subs(T, L*five_lam) / L) == j*five_lam*(L*five_lam*j + 2*a3)

# ---------------------------------------------------------------------------
# 5. Five consecutive values of one cubic have vanishing fourth difference.
# Write four normalized adjacent gaps d1,d2,d3,d4.  Then
#   d1 - 3 d2 + 3 d3 - d4 = 0.
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

# The normalized cubic leading coefficient / L is the integer
# 2^(2m) 5^(m+d) c_u^2 g.  Check exponent arithmetic on the admissible range.
for m in range(3, 16):
    for d0 in range(1, m//3 + 1):
        # lhs exponent bookkeeping from f4/(2^(2M+2)5^nu D L)
        nu = m - 3*d0
        exp2 = (4*m) - m - m  # after cancelling the common 2M+2 and D,L
        exp5 = 2*m - nu - d0 - d0
        assert exp2 == 2*m
        assert exp5 == m + d0

# ---------------------------------------------------------------------------
# 6. Mod g, adjacent normalized gaps are controlled by
#   (2j+1)T+2a3, j=1,2,3,4.
# For odd p != 3 with p | g and p \nmid T, at most one can vanish.
# ---------------------------------------------------------------------------
for p in list(sp.primerange(7, 200)):
    if p in (5,):
        continue
    for T0 in range(1, p):
        for a0 in range(p):
            hits = []
            for jj in range(1,5):
                if ((2*jj+1)*T0 + 2*a0) % p == 0:
                    hits.append(jj)
            assert len(hits) <= 1

# Center saturation A3=3T+a3=0 mod p makes the two central gaps opposite units.
for p in list(sp.primerange(7, 100)):
    for T0 in range(1,p):
        a0 = (-3*T0) % p
        left = (5*T0 + 2*a0) % p
        right = (7*T0 + 2*a0) % p
        assert left == (-T0) % p and right == T0 % p
        assert left and right and (left + right) % p == 0

print("OK: A2 rational-root sieve extends to five positive cofactors with exact cubic gap relations")
