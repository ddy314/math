#!/usr/bin/env python3
"""Finite checks for tail-rough-angular-source-transfer.md.

Checks exact gcd/linear identities, norm-depth transfer, and the cyclotomic
overlap on a bounded sample.  This is a mechanical certificate, not a proof of
the unbounded theorem.
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
    out = []
    for x in range(3, n + 1, 2):
        if all(x % q for q in range(3, int(x**0.5) + 1, 2)):
            out.append(x)
    return out


def check(limit: int = 13) -> int:
    rows = 0
    for B1 in range(1, limit):
        for B2 in range(1, limit):
            if gcd(B1, B2) != 1:
                continue
            for a1 in range(1, limit):
                for a2 in range(1, limit):
                    gn = gcd(a1, a2)
                    aa1, aa2 = a1 // gn, a2 // gn

                    X, Y = a1 * B2, a2 * B1
                    assert gcd(X, Y) == gn

                    for m2 in range(1, 4):
                        CQ = B1 * 10**m2 + B2
                        # Source-angular linear identity, componentwise.
                        zang_re, zang_im = aa1 * B2, aa2 * B1
                        znum_re, znum_im = -aa1 * 10**m2, aa2
                        assert zang_re - B1 * znum_re == aa1 * CQ
                        assert zang_im - B1 * znum_im == 0

                        Nang = zang_re * zang_re + zang_im * zang_im
                        Nnum = znum_re * znum_re + znum_im * znum_im

                        for p in primes_upto(43):
                            if p == 5:
                                continue
                            c = vp(CQ, p)
                            omega = vp(Nang, p)
                            if c and omega:
                                # Norm consequence of same-orientation transfer.
                                assert vp(Nnum, p) >= min(c, omega)

                            for n2 in range(1, 5):
                                Acirc = aa1 * 10**n2 + aa2
                                common = min(vp(Acirc, p), vp(Nnum, p))
                                if common:
                                    cyc = 10 ** (2 * abs(n2 - m2)) + 1
                                    assert vp(cyc, p) >= common
                            rows += 1
    return rows


def main() -> None:
    rows = check()
    print(f"DD angular source transfer checks passed ({rows} prime rows)")


if __name__ == "__main__":
    main()
