#!/usr/bin/env python3
"""Exact divisor-congruence certificate for A1 k=g=6, ell=6.

The positive residual theorem gives exactly t in {6,...,50}.  Every such t
has v2(t),v5(t)<ell, so residual-shell-supply.md applies:

    b3 = a_t * h,
    10^ell / a_t | h + t_hat,

with h in the finite minimal-diagonal odd-prime supply.  The script checks the
complete supply and asserts that no k-digit N0 can be recovered.
"""

from __future__ import annotations

import sympy as sp


K = 6
ELL = 6
T_MIN = 6
T_MAX = 50
EXPECTED_H_COUNTS = {1: 64, 2: 32, 3: 2, 4: 8}
EXPECTED_HITS = 0


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
    total_hits = 0

    for w in (1, 2, 3, 4):
        hs = odd_prime_supply(w)
        w_hits = 0

        for t in range(T_MIN, T_MAX + 1):
            e2 = vp(t, 2)
            e5 = vp(t, 5)
            if not (e2 < ELL and e5 < ELL):
                raise AssertionError(f"unexpected deep residual t={t}")

            a_t = 2**e2 * 5**e5
            t_hat = t // a_t
            modulus = 10**ELL // a_t

            for h in hs:
                if (h + t_hat) % modulus != 0:
                    continue

                N0 = a_t * (h + t_hat) // 10**ELL
                if not (10 ** (K - 1) <= N0 < 10**K):
                    continue

                w_hits += 1
                print(f"HIT w={w} t={t} h={h} N0={N0}")

        total_hits += w_hits
        print(f"w={w} h_supply={len(hs)} shell_hits={w_hits}")

    if total_hits != EXPECTED_HITS:
        raise AssertionError(f"ell=6 hit count changed: {total_hits} != {EXPECTED_HITS}")

    print(f"total_shell_hits={total_hits}")
    print("CERTIFICATE OK: k=g=6, ell=6 residual shell is empty.")


if __name__ == "__main__":
    run()
