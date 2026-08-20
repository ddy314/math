#!/usr/bin/env python3
"""Certificate for spontaneous-crt-target-descent-fixed-h1-third.md."""


def vp(n: int, p: int) -> int:
    if n == 0:
        return 99
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def P(K: int) -> int:
    return 6 * K * K - 36 * K + 55


def rplus(K: int, d: int) -> int:
    u = d * K - 1
    return d * P(K) - K * u


# The two affine systems from the proof.
# p=31:
#   Dhat^3: mu = 17 + 21*kappa
#   R_+^3: mu = 18 + 2*kappa
sol31 = []
for kappa in range(31):
    for mu in range(31):
        if (mu - 17 - 21 * kappa) % 31 == 0 and (mu - 18 - 2 * kappa) % 31 == 0:
            sol31.append((kappa, mu))
assert sol31 == [(18, 23)]

# p=179:
#   Dhat^3: mu = 58 + 21*kappa
#   R_+^3: mu = 70 + 58*kappa
sol179 = []
for kappa in range(179):
    mu_d = (58 + 21 * kappa) % 179
    mu_r = (70 + 58 * kappa) % 179
    if mu_d == mu_r:
        sol179.append((kappa, mu_d))
assert sol179 == [(169, 27)]

states = [
    (31, 9, 7, 18, 23, 17307, 22110),
    (179, 15823, 25476, 169, 27, 5430752, 890583),
]

for p, K2, d2, kappa, mu, K3_expected, d3_expected in states:
    K3 = K2 + p * p * kappa
    d3 = d2 + p * p * mu
    assert K3 % (p ** 3) == K3_expected
    assert d3 % (p ** 3) == d3_expected

    # Baseline remains exactly h=1.
    assert vp(P(K3), p) == 1
    assert vp(d3 * K3 - 1, p) == 1

    # The deep decimal direction really reaches the third layer.
    assert vp(rplus(K3, d3), p) >= 3

# Explicit normalized third digits quoted in the proof.
# For p=31: R_+/(p^2 N) = 1 + 7*kappa + 12*mu mod p.
for kappa in range(31):
    for mu in range(31):
        K = 9 + 31 * 31 * kappa
        d = 7 + 31 * 31 * mu
        assert (rplus(K, d) // (31 * 31)) % 31 == (1 + 7 * kappa + 12 * mu) % 31

# For p=179: R_+/(p^2 N) = 61 + 71*kappa + 150*mu mod p.
# Here rplus is already normalized by N because d=D/N.
for kappa in range(12):
    for mu in range(12):
        K = 15823 + 179 * 179 * kappa
        d = 25476 + 179 * 179 * mu
        assert (rplus(K, d) // (179 * 179)) % 179 == (61 + 71 * kappa + 150 * mu) % 179

print("OK: fixed 31/179 h=1 simultaneous descent/E+ third depth leaves one point per prime")
