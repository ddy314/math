#!/usr/bin/env python3
"""Full global-terminal certificate for k=2g-2 at g=3,4.

No prime-shape assumption on L is used.  Every divisor M of 10^g Q G and
every coprime 2/5-smooth L in the slope window is tested against the global
kappa-square and exact decimal-height recovery theorem.
"""

from math import gcd, isqrt
from sympy import isprime

TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))

FACTORS = {
    (3, 1): ({3: 4, 37: 1, 333667: 1}, {19: 2, 277: 1, 100003: 1}),
    (3, 2): ({2: 1, 691: 1, 723589: 1}, {3: 2, 17: 1, 2557: 1, 25561: 1}),
    (3, 3): ({71: 1, 2251: 1, 6257: 1}, {13: 1, 109: 1, 1657: 1, 4259: 1}),
    (3, 4): ({2: 2, 3: 1, 83333333: 1}, {7: 1, 23: 1, 62111801: 1}),
    (4, 1): ({3: 2, 53: 1, 79: 1, 265371653: 1}, {7: 1, 13: 1, 769231: 1, 1428571: 1}),
    (4, 2): ({2: 1, 491: 1, 10183299389: 1}, {3: 3, 127: 1, 29163021289: 1}),
    (4, 3): ({7: 2, 3610339: 1, 56527: 1}, {99999999999971: 1}),
    (4, 4): ({2: 2, 3: 1, 311: 1, 2679528403: 1}, {433: 1, 1297: 1, 178062361: 1}),
}


def valuation(n: int, p: int) -> int:
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def only_2_5(n: int) -> bool:
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n == 1


def factor_product(fac):
    out = 1
    for p, e in fac.items():
        assert isprime(p)
        out *= p**e
    return out


def merge_factor(dst, src):
    for p, e in src.items():
        dst[p] = dst.get(p, 0) + e


def divisors(fac):
    ds = [1]
    for p, e in fac.items():
        old = ds
        ds = []
        pe = 1
        for _ in range(e + 1):
            ds.extend(d * pe for d in old)
            pe *= p
    return ds


def smooth_L_values(H: int, M: int):
    upper = (10 * M) // H
    p2 = 1
    a = 0
    while p2 <= upper:
        p5 = 1
        b = 0
        while p2 * p5 <= upper:
            L = p2 * p5
            if M < H * L <= 10 * M and gcd(L, M) == 1:
                yield L, a, b
            p5 *= 5
            b += 1
        p2 *= 2
        a += 1


def terminal_survives(g: int, z: int, w: int, J: int, M: int, L: int, aL: int, bL: int) -> bool:
    H = 10**g
    tau = 10 ** (g - 2)
    n2 = 4 * g - 3

    b1 = 10**n2 - w
    b2 = tau
    a2 = 10**n2 - z
    a1 = 10 ** (5 * g - 2) + (10 * (5 - z - w) + 1) * H + J

    Q0 = 10 * b1 + 1
    Q = tau * Q0
    G = tau * b1
    D = H * Q
    C = a1 * 10**n2 + a2
    N = (a1 * b2) ** 2 + (a2 * b1) ** 2
    K = G * G * C * C - D * D * N

    base = H * Q * G
    assert base % M == 0
    kappa = base * L // M

    W2 = kappa * (kappa * K - 2 * G * D * D * N)
    if W2 < 0:
        return False
    W = isqrt(W2)
    if W * W != W2:
        return False

    Y = kappa * kappa * (kappa + 2 * G)
    M10 = M
    while M10 % 2 == 0:
        M10 //= 2
    while M10 % 5 == 0:
        M10 //= 5

    for sigma in (1, -1):
        X = kappa * G * G * C + sigma * (kappa + G) * W
        if X <= 0:
            continue
        h = gcd(X, Y)
        u = X // h
        v = Y // h

        if not (10 * u >= v and u < v):
            continue
        if not only_2_5(v):
            continue

        d2 = valuation(v, 2)
        d5 = valuation(v, 5)
        H2 = max(d2, aL)
        H5 = max(d5, bL)
        if H2 != H5 or H2 < 1:
            continue
        if gcd(u, M10) != 1:
            continue

        return True

    return False


def main():
    test_counts = {3: 0, 4: 0}
    survivors = []

    for g in (3, 4):
        H = 10**g
        tau = 10 ** (g - 2)

        for w in (1, 2, 3, 4):
            b1 = 10 ** (4 * g - 3) - w
            Q0 = 10 * b1 + 1
            fb, fq = FACTORS[(g, w)]
            assert factor_product(fb) == b1
            assert factor_product(fq) == Q0

            # base=H*tau^2*b1*Q0 has base 2/5 depth 3g-4.
            fac = {2: 3 * g - 4, 5: 3 * g - 4}
            merge_factor(fac, fb)
            merge_factor(fac, fq)

            for M in divisors(fac):
                for L, aL, bL in smooth_L_values(H, M):
                    for z, w2 in TYPES:
                        if w2 != w:
                            continue
                        for J in range(109):
                            test_counts[g] += 1
                            if terminal_survives(g, z, w, J, M, L, aL, bL):
                                survivors.append((g, z, w, J, M, L, aL, bL))

    print(f"g3_tests={test_counts[3]}")
    print(f"g4_tests={test_counts[4]}")
    print(f"survivors={len(survivors)}")
    for row in survivors:
        print(row)

    assert test_counts == {3: 5408362, 4: 9450518}
    assert survivors == []


if __name__ == "__main__":
    main()
