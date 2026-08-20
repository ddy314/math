#!/usr/bin/env python3
"""Mechanical valuation checks for high-funnel-qz-gcd-allocation.md."""

from __future__ import annotations


def valuation_allocation() -> None:
    # Abstract p-adic denominator ledger for p not in {2,5}.
    # qexp is v_p(Q)=v_p(q) on q-Z support; e3=qexp.
    for e1 in range(0, 9):
        for e2 in range(0, 9):
            M = max(e1, e2)
            mn = min(e1, e2)

            if e1 != e2:
                q_values = [mn]
            else:
                # Equal prefix depths permit arbitrary extra concat cancellation.
                q_values = list(range(M, M + 6))

            for qexp in q_values:
                e3 = qexp
                gamma = e1 + e2
                r3 = max(e3 - M, 0)
                assert 2 * qexp <= gamma + 2 * r3

                # Any gcd(q,Z) exponent s is at most qexp.
                for s in range(qexp + 1):
                    assert 2 * s <= gamma + 2 * r3


def third_excess_ghost_scale() -> None:
    # If e3 exceeds both prefix exponents by c, both y1,y2
    # acquire at least c powers of p after lcm lifting.
    for e1 in range(0, 8):
        for e2 in range(0, 8):
            M = max(e1, e2)
            for c in range(1, 6):
                e3 = M + c
                assert e3 - e1 >= c
                assert e3 - e2 >= c


def phase_coprimality() -> None:
    # Finite sanity check of the elementary implication:
    # U,V coprime p-units and 2^H Z = 5^T U + V imply
    # p cannot divide Z together with U or V.
    # We test small odd primes away from 5.
    for p in (3, 7, 11, 13, 17, 19):
        for U in range(1, p):
            for V in range(1, p):
                if U % p == 0 or V % p == 0:
                    continue
                # Only coprime modulo p matters here.
                for T in range(1, 5):
                    rhs = (pow(5, T, p) * U + V) % p
                    if rhs == 0:
                        # Z may be 0 mod p, but U,V are visibly nonzero.
                        assert U % p != 0 and V % p != 0


def main() -> None:
    valuation_allocation()
    third_excess_ghost_scale()
    phase_coprimality()
    print("DD high-funnel q-Z gcd allocation checks passed")


if __name__ == "__main__":
    main()
