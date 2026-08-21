#!/usr/bin/env python3
"""Exact finite audit for the sharpened w=1 complement minimum.

The written proof splits by r3=v3(2k+1).  The only finite data needed are
multiplicative orders of 10 for the p=3 mod 4 primes below 71, plus the
mod-36 identity used to rule out the old u=27 branch when r3=1.

This script computes every order by exhaustive divisor testing of p-1, so the
small-prime table is an exact finite certificate rather than a heuristic.
"""

from __future__ import annotations


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, n + 1):
        if n % d == 0:
            out.append(d)
    return out


def multiplicative_order_10(p: int) -> int:
    assert p not in (2, 5)
    for d in divisors(p - 1):
        if pow(10, d, p) == 1:
            return d
    raise AssertionError(p)


def main() -> None:
    primes_3mod4_below_71 = [7, 11, 19, 23, 31, 43, 47, 59, 67]
    expected = {
        7: 6,
        11: 2,
        19: 18,
        23: 22,
        31: 15,
        43: 21,
        47: 46,
        59: 58,
        67: 33,
    }
    got = {p: multiplicative_order_10(p) for p in primes_3mod4_below_71}
    assert got == expected, got
    assert multiplicative_order_10(71) == 35

    # r3=0 means n=2k+1 is odd and 3 does not divide n.  Every order below
    # 71 is therefore impossible: it is either even or divisible by 3.
    for p, order in got.items():
        assert order % 2 == 0 or order % 3 == 0, (p, order)
    order71 = multiplicative_order_10(71)
    assert order71 % 2 == 1 and order71 % 3 != 0

    # r3=1: n=3m, 3 does not divide m.  LTE gives v3(10^m-1)=2.
    # For every m>=2, 10^m == 28 mod 36, hence
    # (10^m-1)/9 == 3 mod 4.  That quotient is not divisible by 3, so it
    # contains a p=3 mod 4 factor outside the 3-primary block.  Thus u=27
    # is impossible.
    for m in range(2, 100):
        assert pow(10, m, 36) == 28
        a = (10**m - 1) // 9
        assert a % 4 == 3
        assert a % 3 != 0 if m % 3 != 0 else True

    # Typewise product lower bounds used in the proof.
    bounds = {
        "r3=0": 9 * 71 * 7,
        "r3=1": 27 * 31 * 23,
        "r3 odd >=3": 3**5 * 19,
        "r3 even >=2": 3**4 * 31 * 19,
    }
    assert bounds == {
        "r3=0": 4473,
        "r3=1": 19251,
        "r3 odd >=3": 4617,
        "r3 even >=2": 47709,
    }
    assert min(bounds.values()) == 4473
    assert 10001 < 3 * 4473

    print("w=1 global complement minimum audit: OK")
    print("orders below 71:", got)
    print("ord_71(10)=", order71)
    print("branch product bounds:", bounds)
    print("global theorem: M>=4473, hence D/T^2<10001/4473<3")


if __name__ == "__main__":
    main()
