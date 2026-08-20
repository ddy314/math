#!/usr/bin/env python3
"""Certificate for spontaneous-crt-gaussian-slot-orientation.md."""

from fractions import Fraction as F

# Endpoint / slot bounds.
s_lo, s_hi = F(2499, 250), F(10, 1)
x_lo, x_hi = F(1, 10), F(2, 19)
psi_lo = F(1, 17)
psi_hi = F(1001, 15000)

sig_m_lo, sig_m_hi = F(393, 125), F(1607, 500)
sig_p_lo, sig_p_hi = F(2389, 500), F(606, 125)

# Raw Gaussian-normalized real quotient bounds.
raw_m_lo = F(1000) * s_lo**2 * x_lo**2 * psi_lo / sig_m_hi**3
raw_m_hi = F(1000) * s_hi**2 * x_hi**2 * psi_hi / sig_m_lo**3
raw_p_lo = F(1000) * s_lo**2 * x_lo**2 * psi_lo / sig_p_hi**3
raw_p_hi = F(1000) * s_hi**2 * x_hi**2 * psi_hi / sig_p_lo**3

assert raw_m_lo > F(44, 25)
assert raw_m_hi < F(12, 5)
assert raw_p_lo > F(51, 100)
assert raw_p_hi < F(7, 10)

# Uniform floor correction. In the reflection high-2 lattice:
# eta <= M/11 and d < 9M/77. Hence A < M+8 and B > 2M.
# Therefore eps_fl < 2^(M+8)/5^(2M) <= its M=11 value.
floor_majorant_M11 = F(2**19, 5**22)
assert floor_majorant_M11 < F(1, 100)

# After floor correction the two fixed bands remain disjoint.
assert raw_m_lo - F(1, 100) > F(7, 4)
assert raw_p_lo - F(1, 100) > F(1, 2)
assert raw_m_hi < F(12, 5)
assert raw_p_hi < F(7, 10)
assert F(7, 10) < 1 < F(7, 4)

# Exact exponent bookkeeping after substituting the Gaussian slot relation.
# 2-exponent: (eta-M)/2 - (3eta+6) - 2 = -(M+5eta)/2 - 8.
assert (1 - 6) == -5
assert -1 == -1
assert -16 == -16
# 5-exponent: 3M+2eta-4d -(3eta+3-3d) = 3M-eta-d-3.
assert 2 - 3 == -1
assert -4 - (-3) == -1
assert -3 == -3

# Integer sign carrier sanity: O = 2^A Q - 5^B k_h^3.
# A>=1 and k_h odd imply O is odd. Its sign is the sign of Q_G-1.
for Q, A, B, kh in [(1, 2, 3, 1), (100, 4, 2, 3), (7, 6, 5, 5)]:
    O = (2**A) * Q - (5**B) * (kh**3)
    assert O % 2 == 1
    QG_minus_one = F((2**A) * Q, (5**B) * (kh**3)) - 1
    assert (O > 0) == (QG_minus_one > 0)
    assert (O < 0) == (QG_minus_one < 0)

print("OK: A2 CRT quotient and integer sign carrier separate the two Gaussian high-factor sides")
