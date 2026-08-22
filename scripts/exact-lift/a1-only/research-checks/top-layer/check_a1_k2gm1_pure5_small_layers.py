#!/usr/bin/env python3
"""Direct global-terminal certificate for k=2g-1 pure-5 at g=2,3.

These two layers are deliberately checked without using the g>=4 local
valuation simplifications.  The script enumerates every 5-unit divisor M of
10^g Q G that can satisfy the slope window with a pure-5 L=5^b, then checks
exactly:

  * the global kappa-square;
  * both formal normalized roots;
  * the finite-decimal denominator condition;
  * exact decimal-height synchronization;
  * the odd-part coprimality condition.

All arithmetic is integer/rational.  The displayed factorizations are asserted
prime and multiplied back before use.
"""

from math import gcd, isqrt
from sympy import isprime

TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))

FACTORS = {
    (2, 1): ({3: 2, 239: 1, 4649: 1}, {7: 1, 13: 1, 769: 1, 1429: 1}),
    (2, 2): ({2: 1, 4999999: 1}, {3: 3, 3703703: 1}),
    (2, 3): ({7: 1, 1428571: 1}, {99999971: 1}),
    (2, 4): ({2: 2, 3: 1, 191: 1, 4363: 1}, {179: 2, 3121: 1}),
    (3, 1): ({3: 2, 21649: 1, 513239: 1}, {757: 1, 1321: 1, 1000003: 1}),
    (3, 2): ({2: 1, 29: 1, 1724137931: 1}, {3: 2, 577: 1, 192566917: 1}),
    (3, 3): ({17: 1, 5882352941: 1}, {7: 1, 8011: 1, 17832623: 1}),
    (3, 4): ({2: 2, 3: 1, 13: 1, 7477: 1, 85733: 1}, {999999999961: 1}),
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


def merge_factor(dst, src):
    for p, e in src.items():
        dst[p] = dst.get(p, 0) + e


def terminal_survives(g: int, z: int, w: int, J: int, M: int, b: int) -> bool:
    H = 10**g
    tau = 10 ** (g - 1)
    b1 = 10 ** (4 * g - 1) - w
    b2 = tau
    a2 = 10 ** (4 * g - 1) - z
    a1 = H**5 + (10 * (5 - z - w) + 1) * H + J

    Q0 = 10 * b1 + 1
    Q = tau * Q0
    G = tau * b1
    D = H * Q
    C = a1 * 10 ** (4 * g - 1) + a2
    N = (a1 * b2) ** 2 + (a2 * b1) ** 2
    K = G * G * C * C - D * D * N

    L = 5**b
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
        H2 = d2
        H5 = max(d5, b)
        if H2 != H5 or H2 < 1:
            continue
        if gcd(u, M10) != 1:
            continue

        return True

    return False


def main():
    test_counts = {2: 0, 3: 0}
    survivors = []

    for g in (2, 3):
        H = 10**g
        tau = 10 ** (g - 1)

        for w in (1, 2, 3, 4):
            b1 = 10 ** (4 * g - 1) - w
            Q0 = 10 * b1 + 1
            fb, fq = FACTORS[(g, w)]
            assert factor_product(fb) == b1
            assert factor_product(fq) == Q0

            # 5-free factorization of base=H*tau^2*b1*Q0.
            fac = {2: 3 * g - 2}
            merge_factor(fac, {p: e for p, e in fb.items() if p != 5})
            merge_factor(fac, {p: e for p, e in fq.items() if p != 5})

            for M in divisors(fac):
                # Pure-5 L=5^b and slope H/10 <= M/L < H.
                b = 1
                L = 5
                while H * L <= 10 * M:
                    if 10 * M >= H * L and M < H * L:
                        for z, w2 in TYPES:
                            if w2 != w:
                                continue
                            for J in range(10):
                                test_counts[g] += 1
                                if terminal_survives(g, z, w, J, M, b):
                                    survivors.append((g, z, w, J, M, b))
                    b += 1
                    L *= 5

    print(f"g2_tests={test_counts[2]}")
    print(f"g3_tests={test_counts[3]}")
    print(f"survivors={len(survivors)}")
    for row in survivors:
        print(row)

    assert test_counts == {2: 34160, 3: 40170}
    assert survivors == []


if __name__ == "__main__":
    main()
