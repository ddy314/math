#!/usr/bin/env python3
"""Exact certificate for fixed19-secant-center.md.

Uses only Python's standard library. It checks the unique inert secant
resonance, the genuine mod-19 decimal fingerprint, the exact rational
secant-center values, the cofactor ratios modulo 19^2, and the resulting
first-order cancellation in the additive cofactor. It is not a global A2
solver.
"""

from fractions import Fraction


def frac_mod(q: Fraction, modulus: int) -> int:
    return (q.numerator * pow(q.denominator, -1, modulus)) % modulus


def legendre_value(a: int, p: int) -> int:
    """Return the Euler-criterion residue 0, 1, or p-1."""
    return pow(a % p, (p - 1) // 2, p)


p = 19
p2 = p * p

# 1. Only p=19 can make the inert external double root K=55/18 hit
#    one of J=2,3,4.  The J=4 collision is p=17, which is 1 mod 4.
assert [55 - 18 * j for j in (2, 3, 4)] == [19, 1, -17]
assert 19 % 4 == 3
assert 17 % 4 == 1

# The extra first-term factor J+2a_* gives 37, 7, 19.  p=7 is excluded
# from discriminant-zero because (55/7)=(-1/7)=-1.
assert [9 * j - 55 for j in (2, 3, 4)] == [-37, -28, -19]
assert 37 % 4 == 1
assert legendre_value(55, 7) == 6  # -1 mod 7

# 2. Genuine p=19 branch fingerprint.
#    M=10 mod 18 => M-1=9 mod 18.
assert pow(10, 9, p) == -1 % p
assert pow(5, 9, p) == 1

x = 11
y = 6
H = pow(5, 9, p) * (10 * x - 1) % p
e = pow(10, 9, p) * (1 - y) % p
assert (H, e) == (14, 5)

ten_M = pow(10, 10, p)
b2 = x * ten_M % p
a2 = y * pow(10, 9, p) % p
C0 = 9 * b2 * pow(2, -1, p) % p
N0 = (C0 * C0 + a2 * a2) % p
Q = (2 + x) * ten_M % p
Delta0 = (2025 * x * x - 18 * y - y * y) % p
Dsrc0 = (2025 * x * x - 9 * y) % p

assert (b2, a2, C0, N0, Q) == (4, 13, 18, 18, 3)
assert (Delta0, Dsrc0) == (9, 4)

# 3. Exact rational 19-adic center.
K = Fraction(55, 18)
a = -K
R = Fraction(-2695, 324)


def phi(j: int) -> Fraction:
    return j * (j + 2 * a) * (K - j) ** 2 - R * (j + a) ** 2


assert phi(2) == Fraction(p2 * 31, 18**4)
assert phi(3) == Fraction(-7 * 47, 18**4)
assert phi(4) == Fraction(-(17**2) * 41, 18**4)

# 4. Exact cofactor ratios at d_C=D/C=-18.
r_minus = Fraction(-19 * 31, 7 * 47)
r_plus = Fraction(-17 * 41, 7 * 47)
assert r_plus - 1 == Fraction(-54 * 19, 7 * 47)

assert frac_mod(r_minus, p2) == 323  # 19 * 17
assert frac_mod(r_plus, p2) == 191   # 1 + 19 * 10

# Therefore L*Delta_-/Xi_C and L*Delta_+/Xi_C are fixed mod 19^2.
delta_minus_scaled = (1 - frac_mod(r_minus, p2)) % p2
delta_plus_scaled = (frac_mod(r_plus, p2) - 1) % p2
assert delta_minus_scaled == 39      # 1 + 2*19
assert delta_plus_scaled == 190      # 10*19
assert delta_minus_scaled % p != 0
assert delta_plus_scaled % p == 0
assert delta_plus_scaled % p2 != 0

# 5. Additive cofactor first-order cancellation.
# D/C=-18 gives (D+C)/C=-17 and (D-C)/C=-19.
assert ((-17) * delta_plus_scaled + (-19) * delta_minus_scaled) % p2 == 0

# 6. The dimensionless additive-cofactor kernel vanishes at the exact
#    p-adic center, explaining why further purely local lifting cannot by
#    itself create a contradiction.
J_center = K * K - (18 + 4 * a) * K + 18 * a + 55 - R
assert J_center == 0

print("fixed-19 secant center certificate: OK")
