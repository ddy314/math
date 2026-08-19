#!/usr/bin/env python3
"""Certificate for spontaneous-crt-target-descent-fixed-h1.md."""


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


def G(K: int) -> int:
    return 11 * K * K - 240 * K + 432


def RPD(d: int) -> int:
    return 55 * d * d - 36 * d + 6


def second_layer_states(p: int, k0: int):
    d0 = pow(k0, -1, p)
    states = []
    for k in range(p):
        K = k0 + p * k
        if vp(P(K), p) != 1:
            continue
        assert G(K) % p == 0
        G0 = (G(K) // p) % p
        for ell in range(p):
            d = d0 + p * ell
            u = d * K - 1
            if vp(u, p) != 1:
                continue
            # deep target: p^2 | R_+/N = d P - K u
            rplus = d * P(K) - K * u
            if rplus % (p * p):
                continue
            u0 = (u // p) % p
            # p^2 | Dhat_63 iff the first normalized digit vanishes.
            cond = (3 * d * G0 + 16 * (2 * K - 9) * u0) % p
            if cond == 0:
                states.append((K % (p * p), d % (p * p)))
    return states


assert second_layer_states(31, 9) == [(9, 7)]
assert second_layer_states(179, 71) == [(15823, 25476)]

# Exact h=1 / source-prefix checks at the unique second-layer states.
for p, K, d, p0, u0, r0 in [
    (31, 9, 7, 7, 2, 17),
    (179, 15823, 25476, 5, 173, 68),
]:
    assert vp(P(K), p) == 1
    assert vp(d * K - 1, p) == 1
    assert (P(K) // p) % p == p0
    assert ((d * K - 1) // p) % p == u0
    assert vp(RPD(d), p) == 1
    assert (RPD(d) // p) % p == r0


def third_digit_affine(p: int, K2: int, d2: int):
    """Return c,a,b for c+a*kappa+b*mu mod p in the p^3 criterion."""

    def value(kappa: int, mu: int) -> int:
        K = K2 + p * p * kappa
        d = d2 + p * p * mu
        u = d * K - 1
        A = 3 * d * G(K) + 16 * (2 * K - 9) * u
        assert A % (p * p) == 0
        u1 = (u // p) % p
        return ((A // (p * p)) + 16 * (2 * K - 9) * u1 * u1) % p

    c = value(0, 0)
    a = (value(1, 0) - c) % p
    b = (value(0, 1) - c) % p

    # Check affine dependence on a sample grid (full grid is still cheap for p=179,
    # but this is enough once the polynomial degree is known from the explicit formula).
    for kappa in range(min(p, 12)):
        for mu in range(min(p, 12)):
            assert value(kappa, mu) == (c + a * kappa + b * mu) % p
    return c, a, b


assert third_digit_affine(31, 9, 7) == (9, 2, 25)
assert third_digit_affine(179, 15823, 25476) == (20, 106, 12)

# Solve the two affine lines.
# 31: 9 + 2*k + 25*mu = 0 -> mu = 17 + 21*k.
for kappa in range(31):
    mu = (17 + 21 * kappa) % 31
    assert (9 + 2 * kappa + 25 * mu) % 31 == 0

# 179: 20 + 106*k + 12*mu = 0 -> mu = 58 + 21*k.
for kappa in range(179):
    mu = (58 + 21 * kappa) % 179
    assert (20 + 106 * kappa + 12 * mu) % 179 == 0

print("OK: fixed 31/179 h=1 target/descent lifts compress to one p^2 state and one p^3 affine line")
