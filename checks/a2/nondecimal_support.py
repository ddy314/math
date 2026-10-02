"""A2-G11: complete nondecimal common support and original tag lock.

Exact symbolic tag identity and bounded denominator/sphere projection audits.
These regressions do not enumerate Exact Lift solutions or prove the theorem;
the unbounded argument is written in PROOF.md. Python integers are unbounded.
"""

from math import gcd, lcm

import sympy as sp


def decimal_unit(n):
    for p in (2, 5):
        while n % p == 0:
            n //= p
    return n


def main():
    B, T, U, b, c, k = sp.symbols("B T U b c k", positive=True)
    M = c * (B * U * T + b) / k
    assert sp.expand(k * (B * T + M) - (B * (k + c * U) * T + c * b)) == 0
    alpha = sp.symbols("alpha", positive=True)
    beta = B * T * U + M * U + b
    q = M * b / c
    assert sp.factor(beta - (k + c * U) * M / c) == 0
    assert sp.factor(q * alpha / beta - b * alpha / (k + c * U)) == 0
    reduced_denominator = q / c
    ell = (k + c * U) / (b / c)
    assert sp.factor(beta / reduced_denominator - ell) == 0
    projections = 0
    for B in (1, 2):
        for M in range(1, 100):
            for b in range(1, 100):
                for T in (100, 1000):
                    if b % B:
                        continue
                    U = 1000
                    if lcm(B, b, B * T * U + b) % M:
                        continue
                    if lcm(B, M, (B * T + M) * U) % b:
                        continue
                    M0 = decimal_unit(M)
                    Q0 = decimal_unit(B * T + M)
                    assert gcd(M0, Q0) == 1
                    support = decimal_unit(lcm(B, M, B * T + M))
                    assert support == M0 * Q0
                    C = decimal_unit(b)
                    assert support % C == 0
                    CM = gcd(C, M0)
                    CQ = C // CM
                    assert Q0 % CQ == 0 and gcd(CM, CQ) == 1
                    assert gcd(CM, M0 // CM) == 1
                    c = gcd(M, b)
                    common, rest = decimal_unit(c), decimal_unit(b // c)
                    assert gcd(common, rest) == 1
                    assert c * (B * T * U + b) % M == 0
                    k = c * (B * T * U + b) // M
                    assert (k + c * U) % rest == 0
                    projections += 1
    primes = list(sp.primerange(3, 128))
    for p in primes:
        if p == 5:
            continue
        units = {n * n % p for n in range(1, p)}
        assert ((-1) % p in units) == (p % 4 == 1)
        if p % 4 == 3:
            assert not any((x + y) % p == 0 for x in units for y in units)
    assert projections == 1314
    print(f"OK: A2-G11 exact original tag lock; {projections} denominator projections")
    print("Common nondecimal primes require equal depths and p=1 mod4")
    print(
        "Bounded projection audit; unbounded proof is in PROOF.md; no emptiness claim"
    )


if __name__ == "__main__":
    main()
