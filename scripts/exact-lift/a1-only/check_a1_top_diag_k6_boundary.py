#!/usr/bin/env python3
"""Exact certificate for the first non-saturated A1 diagonal boundary at k=g=6.

Target:
    d=2, r=s=1, k=g=6, ell=k-1=5.

Inputs already proved in the A1 proof tree:
  * positive-tail-residual.md: t in {1,2,3,4,5};
  * boundary-residual-2adic.md:
        w=2 -> t=3,
        w=4 -> t=1;
  * minimal-diagonal odd-prime supply:
        h=q*s, q|Q, and s is a whole-block selector from the 1 mod 4
        prime-power blocks of b1;
  * boundary-decimal-supply.md:
        b3=a_t*h,
        10^(k-1)/a_t | h+t_hat.

The certificate deliberately checks an over-complete prefix-independent set:
it does not need gcd(a1,b1), K>0, z, or the rational-square sieve.  If even
this necessary divisor-congruence system has no state, the full boundary is
empty.
"""

from __future__ import annotations

import sympy as sp


K = 6
W_VALUES = (1, 2, 3, 4)
ALLOWED_T = {
    1: (1, 2, 3, 4, 5),
    2: (3,),
    3: (1, 2, 3, 4, 5),
    4: (1,),
}
EXPECTED_H_COUNTS = {1: 64, 2: 32, 3: 2, 4: 8}
EXPECTED_CONGRUENCE_HITS = 0


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


def residual_data(t: int) -> tuple[int, int, int]:
    """Return (a_t, t_hat, modulus) from boundary-decimal-supply.md."""
    a_t = 2 ** vp(t, 2) * 5 ** vp(t, 5)
    t_hat = t // a_t
    modulus = 10 ** (K - 1) // a_t
    return a_t, t_hat, modulus


def run() -> None:
    total_hits = 0

    for w in W_VALUES:
        hs = odd_prime_supply(w)
        print(f"w={w} h_supply={len(hs)}")

        for t in ALLOWED_T[w]:
            a_t, t_hat, modulus = residual_data(t)
            hits: list[tuple[int, int]] = []

            for h in hs:
                if (h + t_hat) % modulus != 0:
                    continue

                N0 = a_t * (h + t_hat) // 10 ** (K - 1)
                if not (10 ** (K - 1) <= N0 < 10**K):
                    continue

                hits.append((h, N0))

            total_hits += len(hits)
            print(
                f"  t={t} modulus={modulus} "
                f"divisor_congruence_hits={len(hits)}"
            )
            for h, N0 in hits:
                print(f"    h={h} N0={N0}")

    if total_hits != EXPECTED_CONGRUENCE_HITS:
        raise AssertionError(
            f"boundary hit count changed: {total_hits} != {EXPECTED_CONGRUENCE_HITS}"
        )

    print(f"total_divisor_congruence_hits={total_hits}")
    print("CERTIFICATE OK: k=g=6, ell=5 first boundary is empty.")


if __name__ == "__main__":
    run()
