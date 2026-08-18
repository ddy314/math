#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c1-source-bridge.md."""

p = 23

# eta=2,d=2 gives M=16 mod22 and m=9 or20 mod22.
assert pow(10, 16, p) == 4
assert (-2 * pow(10, 16, p)) % p == 15
assert pow(10, 9, p) == 20
assert pow(10, 20, p) == 3
assert pow(10, 9, p) ** 2 % p == 9
assert pow(10, 20, p) ** 2 % p == 9

# Both c=1 eta=2 types have (c_Q/23)*k_h=9 and d=2.
# In rho = s*2*q1*zeta*T^2 / (cbar*k_h*B*5^d),
# the coefficient is 20 mod23.
den = (9 * 15 * 25) % p
assert (2 * 9 * pow(den, -1, p)) % p == 20


def plus_rho(kappa):
    den = (1 + 14 * kappa) % p
    if den == 0:
        return None
    return (-11 * pow(den, -1, p)) % p


def minus_rho(kappa):
    den = (1 + 14 * kappa) % p
    if den == 0:
        return None
    return ((9 + 18 * kappa) * pow(den, -1, p)) % p


plus_records = []
minus_records = []

for kappa in range(p):
    rho = plus_rho(kappa)
    # plus canonical orientation requires rho and rho+2 to be units.
    if rho is not None and rho not in (0, p - 2):
        # rho(rho+2)=21 q1.
        q1 = (rho * (rho + 2) * pow(21, -1, p)) % p
        # 9 kappa = 16 h_N + 22 - 16 q1.
        h = ((9 * kappa + 16 * q1 - 22) * pow(16, -1, p)) % p
        poly = (
            11 * h * kappa**2
            - 5 * h * kappa
            - h
            + kappa**3
            + 5 * kappa**2
            - 9 * kappa
            - 2
        ) % p
        assert poly == 0
        j = ((h - 5) * pow(3, -1, p)) % p
        plus_records.append((kappa, rho, q1, h, 16 + 22 * j))

    rho = minus_rho(kappa)
    # minus canonical orientation requires rho to be a unit; rho=-2 is also
    # excluded by the opposite source factor f being a unit in the pure-cQ setup.
    if rho is not None and rho not in (0, p - 2):
        # rho^2=21 q1.
        q1 = (rho * rho * pow(21, -1, p)) % p
        h = ((9 * kappa + 16 * q1 - 22) * pow(16, -1, p)) % p
        poly = (
            11 * h * kappa**2
            - 5 * h * kappa
            - h
            + kappa**3
            + 4 * kappa**2
            - 3 * kappa
            + 7
        ) % p
        assert poly == 0
        j = ((h - 5) * pow(3, -1, p)) % p
        minus_records.append((kappa, rho, q1, h, 16 + 22 * j))

# Shared pole and source-unit boundary.
assert plus_rho(18) is None
assert minus_rho(18) is None
assert plus_rho(11) == p - 2
assert minus_rho(11) == 0

all_lengths = {16 + 22 * j for j in range(23)}
plus_lengths = {row[-1] for row in plus_records}
minus_lengths = {row[-1] for row in minus_records}

assert sorted(plus_lengths) == [
    38, 104, 126, 192, 214, 258, 280, 302,
    324, 390, 412, 434, 456, 478, 500,
]
assert sorted(minus_lengths) == [
    16, 82, 104, 126, 214, 236, 258, 302,
    324, 368, 434, 456,
]

plus_depth1 = all_lengths - plus_lengths
minus_depth1 = all_lengths - minus_lengths

assert sorted(plus_depth1) == [16, 60, 82, 148, 170, 236, 346, 368]
assert sorted(minus_depth1) == [38, 60, 148, 170, 192, 280, 346, 390, 412, 478, 500]
assert sorted(plus_depth1 & minus_depth1) == [60, 148, 170, 346]

print("OK: A2 fixed-23 eta=2 c=1 high-2/source bridge and forced depth-1 length classes certified")
