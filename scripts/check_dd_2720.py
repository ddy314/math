#!/usr/bin/env python3
"""Finite denominator certificate for DD Section 27.20.

The unbounded argument of Section 27.18 already removes the t2 >= 2,
five-adic resonance cores for S >= 7.  This script exhausts the remaining
real denominator blocks for S in {4,5,6}.  It applies the fixed core
valuations, the exact tail interval, and the large-divisor condition for the
constant F_- quotient.  No denominator survives.

Numerator blocks are not enumerated.  This is not a certificate for any
five-adic non-resonance state or for a different 2-adic position.
"""

from __future__ import annotations

from math import gcd


EXPECTED_COUNTS = {
    4: (129600, 54219, 8373),
    5: (1296000, 542960, 83661),
    6: (12960000, 5429698, 836574),
}


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def minimum_rho(required_divisor: int, u: int, v: int) -> int | None:
    """Smallest multiple with v2=u+1 and v5=v, or None if impossible."""

    required_two = valuation(required_divisor, 2)
    required_five = valuation(required_divisor, 5)
    if required_two > u + 1 or required_five > v:
        return None
    return (
        required_divisor
        * 2 ** (u + 1 - required_two)
        * 5 ** (v - required_five)
    )


def check_size(S: int) -> tuple[tuple[int, int, int], list[tuple[int, ...]]]:
    T = 10 ** (2 * S)
    checked = 0
    local_rows = 0
    tail_rows = 0
    survivors: list[tuple[int, ...]] = []

    for c in range(1, 9):
        u = valuation(c, 2)
        v = valuation(c, 5)
        A2 = 1 + 3 * u
        A5 = 3 * v
        k2 = 2 * S + u
        kappa = c * T

        for short_first in (True, False):
            for short_denominator in range(1, 10):
                for long_denominator in range(10 ** (S - 2), 10 ** (S - 1)):
                    checked += 1
                    if short_first:
                        b1, b2 = short_denominator, long_denominator
                        Q = b1 * 10 ** (S - 1) + b2
                    else:
                        b1, b2 = long_denominator, short_denominator
                        Q = 10 * b1 + b2
                    G = short_denominator * long_denominator

                    q2 = valuation(Q, 2)
                    g2 = valuation(G, 2)
                    q5 = valuation(Q, 5)
                    g5 = valuation(G, 5)
                    if 2 * q2 + g2 > A2 or 2 * q5 + g5 > A5:
                        continue
                    if k2 - g2 < 2:
                        continue
                    local_rows += 1

                    if not Q * G < kappa <= 10 * Q * G:
                        continue
                    tail_rows += 1

                    large_divisor = (kappa + 2 * G) // gcd(kappa, G)
                    required_rho_factor = large_divisor // gcd(large_divisor, Q)
                    rho = minimum_rho(required_rho_factor, u, v)
                    if rho is not None and rho < 20000:
                        survivors.append(
                            (
                                c,
                                int(short_first),
                                b1,
                                b2,
                                Q,
                                G,
                                required_rho_factor,
                                rho,
                            )
                        )

    return (checked, local_rows, tail_rows), survivors


def main() -> None:
    summaries: dict[int, tuple[int, int, int]] = {}
    for S in range(4, 7):
        counts, survivors = check_size(S)
        assert counts == EXPECTED_COUNTS[S]
        assert survivors == []
        summaries[S] = counts
        print(f"S={S}: checked/local/tail = {counts}; survivors = 0", flush=True)

    assert summaries == EXPECTED_COUNTS
    print("DD 27.20 finite denominator certificates: OK")


if __name__ == "__main__":
    main()
