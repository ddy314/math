#!/usr/bin/env python3
"""Finite mechanical checks for tail-rough-gaussian-payer-split.md.

The proof is elementary; this script only checks the local valuation identities
and the primitive sum-of-two-squares support split on a bounded sample.
"""

from __future__ import annotations

from math import gcd


def vp(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    out = 0
    while n % p == 0:
        out += 1
        n //= p
    return out


def primes_upto(n: int) -> list[int]:
    ans = []
    for x in range(3, n + 1, 2):
        if all(x % q for q in range(3, int(x**0.5) + 1, 2)):
            ans.append(x)
    return ans


def check() -> int:
    rows = 0
    for p in primes_upto(43):
        if p == 5:
            continue
        for B1 in range(1, 16):
            for B2 in range(1, 16):
                if gcd(B1, B2) != 1:
                    continue
                for m2 in range(1, 4):
                    CQ = B1 * 10**m2 + B2
                    if CQ % p:
                        continue
                    # X_Q-support denominator-unit lemma.
                    assert B1 % p != 0
                    assert B2 % p != 0

                    for a1 in range(1, 13):
                        for a2 in range(1, 13):
                            X = a1 * B2
                            Y = a2 * B1
                            gA = gcd(X, Y)
                            X0, Y0 = X // gA, Y // gA
                            assert gcd(X0, Y0) == 1
                            Nang = X0 * X0 + Y0 * Y0
                            N0 = X * X + Y * Y

                            gp = vp(gA, p)
                            t = vp(a1 * 10**2 + a2, p)
                            # n2=2 is arbitrary here; 10 is a p-unit.
                            assert gp <= t
                            assert vp(N0, p) == 2 * gp + vp(Nang, p)

                            if p % 4 == 3:
                                assert Nang % p != 0
                                assert vp(N0, p) == 2 * gp
                                assert vp(N0, p) <= 2 * t
                            rows += 1
    return rows


def main() -> None:
    rows = check()
    print(f"DD rough Gaussian payer split checks passed ({rows} rows)")


if __name__ == "__main__":
    main()
