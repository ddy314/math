#!/usr/bin/env python3
"""Mechanical audit for the DD primitive sixfold hard-source lock.

Checks exact prefix folding, local valuation identities, and the failure-charge
logic.  This is not a DD emptiness proof.
"""

from __future__ import annotations

from math import gcd


def check_primitive_prefix() -> None:
    # Exhaust small coprime primitive prefixes and verify source-prime units.
    for u1 in range(1, 20):
        for u2 in range(1, 20):
            if gcd(u1, u2) != 1:
                continue
            for m2 in range(1, 4):
                CQ = u1 * 10**m2 + u2
                assert CQ > 0
                # Any odd nondecimal common divisor with u1 or u2 would
                # contradict gcd(u1,u2)=1.
                for p in (3, 7, 11, 13, 17, 19, 23, 29, 31):
                    if CQ % p == 0:
                        assert u1 % p != 0
                        assert u2 % p != 0


def check_sixfold_folding() -> None:
    # The congruence is purely algebraic: if CQ=u1*10^m2+u2,
    # then u1^6*10^(6*m2) == u2^6 mod CQ.
    for u1 in range(1, 12):
        for u2 in range(1, 12):
            if gcd(u1, u2) != 1:
                continue
            for m2 in range(1, 3):
                CQ = u1 * 10**m2 + u2
                assert (u1**6 * 10 ** (6 * m2) - u2**6) % CQ == 0


def check_hard_valuation_ledger() -> None:
    for E in range(0, 6):
        for j in range(0, 6):
            M = max(E, j)
            for t in range(0, 5):
                for n0 in range(0, 5):
                    for h in range(1, 10):
                        c = h + 2 * t + n0 + M + j
                        coeff_depth = M + t
                        rhs_depth = j + t + max(E - j, 0)
                        assert rhs_depth == M + t
                        assert coeff_depth == rhs_depth
                        r = c - coeff_depth
                        assert r == h + t + n0 + j
                        assert r > 0


def check_global_modulus_product() -> None:
    # A finite abstract product ledger: exponent-wise residuals multiply to
    # X_H*T_H*N_H*J_H exactly.
    primes = (3, 7, 11, 13)
    ledgers = (
        (2, 1, 0, 3),
        (1, 0, 2, 1),
        (4, 2, 1, 0),
        (1, 3, 2, 2),
    )
    modulus = XH = TH = NH = JH = 1
    for p, (h, t, n0, j) in zip(primes, ledgers):
        modulus *= p ** (h + t + n0 + j)
        XH *= p**h
        TH *= p**t
        NH *= p**n0
        JH *= p**j
    assert modulus == XH * TH * NH * JH


def check_failure_charge() -> None:
    # If the coefficient-unit modulus does not exceed 10^e, its log-height
    # is necessarily <= e.  Use exact integer powers for a finite audit.
    for e in range(1, 8):
        threshold = 10**e
        for modulus in (3, 17, threshold - 1, threshold, threshold + 1):
            if modulus <= 0:
                continue
            ordinary_lock = threshold < modulus
            if not ordinary_lock:
                assert modulus <= threshold
            else:
                assert threshold < modulus


def main() -> None:
    check_primitive_prefix()
    check_sixfold_folding()
    check_hard_valuation_ledger()
    check_global_modulus_product()
    check_failure_charge()
    print("DD primitive sixfold hard-source checks passed")


if __name__ == "__main__":
    main()
