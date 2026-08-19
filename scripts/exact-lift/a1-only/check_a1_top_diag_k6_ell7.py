#!/usr/bin/env python3
"""Exact certificate for A1 minimal diagonal k=g=6, ell=7.

Residual window:
    51 <= t <= 504.

Regular residuals (v2(t),v5(t)<7) are checked by the finite h congruence from
residual-shell-supply.md.  The only deep residuals are t=128,256,384.  For
those v5(t)=0, hence v5(b3)=0 and b3=h*2^u.  We enumerate the finite u-window
forced by the 13-digit denominator condition and check exact decimal recovery.
"""

from __future__ import annotations

import sympy as sp


K = 6
ELL = 7
M3 = K + ELL
T_MIN = 51
T_MAX = 504
EXPECTED_H_COUNTS = {1: 64, 2: 32, 3: 2, 4: 8}
EXPECTED_DEEP = (128, 256, 384)
EXPECTED_REGULAR_HITS = 0
EXPECTED_DEEP_HITS = 0


def vp(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def all_divisors(factors: dict[int, int]) -> list[int]:
    out = [1]
    for p, e in sorted(factors.items()):
        out = [d * p**j for d in out for j in range(e + 1)]
    return sorted(out)


def odd_prime_supply(w: int) -> list[int]:
    b1 = 10 ** (2 * K + 1) - w
    Q = 10 * b1 + 1

    q_divisors = all_divisors(sp.factorint(Q))
    blocks = [
        p**e
        for p, e in sp.factorint(b1).items()
        if p not in (2, 5) and p % 4 == 1
    ]

    selectors = [1]
    for block in blocks:
        selectors += [s * block for s in selectors]

    hs = sorted({q * s for q in q_divisors for s in selectors})
    expected = EXPECTED_H_COUNTS[w]
    if len(hs) != expected:
        raise AssertionError(f"w={w}: h supply changed: {len(hs)} != {expected}")
    return hs


def run() -> None:
    deep = tuple(
        t
        for t in range(T_MIN, T_MAX + 1)
        if vp(t, 2) >= ELL or vp(t, 5) >= ELL
    )
    if deep != EXPECTED_DEEP:
        raise AssertionError(f"deep residual set changed: {deep} != {EXPECTED_DEEP}")

    regular_total = 0
    deep_total = 0

    for w in (1, 2, 3, 4):
        hs = odd_prime_supply(w)
        regular_hits = 0
        deep_hits = 0

        # Regular residuals: exact decimal-supply congruence.
        for t in range(T_MIN, T_MAX + 1):
            e2 = vp(t, 2)
            e5 = vp(t, 5)
            if e2 >= ELL or e5 >= ELL:
                continue

            a_t = 2**e2 * 5**e5
            t_hat = t // a_t
            modulus = 10**ELL // a_t

            for h in hs:
                if (h + t_hat) % modulus != 0:
                    continue

                N0 = a_t * (h + t_hat) // 10**ELL
                if 10 ** (K - 1) <= N0 < 10**K:
                    regular_hits += 1
                    print(f"REGULAR HIT w={w} t={t} h={h} N0={N0}")

        # Deep residuals: all are pure deep-2 here and have v5(t)=0.
        for t in deep:
            if vp(t, 5) != 0:
                raise AssertionError(f"unexpected deep-5 residual t={t}")

            for h in hs:
                # v5(b3)=0, so b3=h*2^u for some u>=0.
                u = 0
                b3 = h
                while b3 < 10 ** (M3 - 1):
                    b3 *= 2
                    u += 1

                while b3 < 10**M3:
                    if (b3 + t) % 10**ELL == 0:
                        N0 = (b3 + t) // 10**ELL
                        if 10 ** (K - 1) <= N0 < 10**K:
                            deep_hits += 1
                            print(
                                f"DEEP HIT w={w} t={t} h={h} "
                                f"u={u} N0={N0} b3={b3}"
                            )
                    b3 *= 2
                    u += 1

        regular_total += regular_hits
        deep_total += deep_hits
        print(
            f"w={w} h_supply={len(hs)} "
            f"regular_hits={regular_hits} deep_hits={deep_hits}"
        )

    if regular_total != EXPECTED_REGULAR_HITS:
        raise AssertionError(
            f"regular hit count changed: {regular_total} != {EXPECTED_REGULAR_HITS}"
        )
    if deep_total != EXPECTED_DEEP_HITS:
        raise AssertionError(
            f"deep hit count changed: {deep_total} != {EXPECTED_DEEP_HITS}"
        )

    print(f"regular_hits={regular_total}")
    print(f"deep_hits={deep_total}")
    print("CERTIFICATE OK: k=g=6, ell=7 residual shell is empty.")


if __name__ == "__main__":
    run()
