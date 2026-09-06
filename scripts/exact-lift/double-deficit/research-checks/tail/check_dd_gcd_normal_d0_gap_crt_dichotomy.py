#!/usr/bin/env python3
"""Mechanical checks for dd-gcd-normal-d0-gap-crt-dichotomy-2026-09-06.md.

This script checks exact algebra, local exponent simplifications, and the
large-gap inequality.  The small integer example is an algebraic normalization
toy, not a claimed Exact-Lift solution.
"""

from __future__ import annotations

import math

import sympy as sp


def exact_normalization_toy() -> None:
    # Actual denominator-side gcd-normal data:
    # b1=1, b2=2, m2=1 => Q=12, G=2.
    # m=1, b3=16 => kappa=10*12*2/16=15.
    b1, b2, m2 = 1, 2, 1
    Q = b1 * 10**m2 + b2
    G = b1 * b2
    m, b3 = 1, 16
    kappa = 10**m * Q * G // b3
    gamma = math.gcd(kappa, G)
    u, v = kappa // gamma, G // gamma
    d0 = math.gcd(u, Q)
    L, q = u // d0, Q // d0
    omega = 10**m // L
    q_lcm = math.lcm(b1, b2, b3)
    c3 = q_lcm // b3

    assert (Q, G, kappa, gamma, u, v) == (12, 2, 15, 1, 15, 2)
    assert (d0, L, q, omega, q_lcm, c3) == (3, 5, 4, 2, 16, 1)
    assert math.gcd(d0, v) == 1
    assert math.gcd(L, v) == 1
    assert b3 == v * omega * q
    assert q_lcm == v * omega * q * c3
    assert kappa * b3 == 10**m * Q * G


def source_gap_toy() -> None:
    # Standalone exact source-gap algebra toy.
    # omega*c3*A12*10^d = a + d0*H0
    # v*H0 = a3*c3 + L*a
    d0, L, v = 3, 1, 2
    omega, c3, A12, d = 1, 1, 1, 1
    H0, a, a3 = 3, 1, 5

    assert math.gcd(d0, v) == 1
    assert math.gcd(L, v) == 1
    assert omega * c3 * A12 * 10**d == a + d0 * H0
    assert v * H0 == a3 * c3 + L * a

    rho_d0 = (omega * c3 * A12 * 10**d) % d0
    rho_v = (-a3 * c3 * pow(L, -1, v)) % v
    assert a % d0 == rho_d0
    assert a % v == rho_v

    # CRT modulus d0*v uniquely recovers 0<a<d0*v.
    candidates = [x for x in range(d0 * v) if x % d0 == rho_d0 and x % v == rho_v]
    assert candidates == [a]


def local_depth_symbolic() -> None:
    E, j, c, t = sp.symbols("E j c t", nonnegative=True, integer=True)

    # Case E >= j.
    d0_depth_1 = E + c - j
    c3_depth_1 = E - j
    raw_1 = sp.expand(d0_depth_1 - c3_depth_1 - t)
    assert sp.simplify(raw_1 - (c - t)) == 0

    # Case j > E.
    d0_depth_2 = E + c - j
    c3_depth_2 = 0
    raw_2 = sp.expand(d0_depth_2 - c3_depth_2 - t)
    assert sp.simplify(raw_2 - (c - t - (j - E))) == 0

    # Compare pre-positive-part expressions with old Euclidean depth.
    old_1 = c - E - t
    old_2 = c - j - t
    assert sp.simplify(raw_1 - old_1 - E) == 0
    assert sp.simplify(raw_2 - old_2 - E) == 0


def corrected_split_coverage() -> None:
    # Exhaust finite local ledgers satisfying the exact formulas and check
    # r_d0 >= h+n0 on hard support.
    for E in range(6):
        for j in range(6):
            for t in range(5):
                for n0 in range(5):
                    for h in range(1, 6):
                        M = max(E, j)
                        c = h + 2 * t + n0 + M + j
                        r = max(c - t - max(j - E, 0), 0)
                        assert r >= h + n0

    # Soft e_N support: use the corrected split identities directly.
    for E in range(6):
        for j in range(6):
            for t in range(5):
                for alpha in range(5):
                    for eN in range(1, 6):
                        if j > E:
                            for e3 in range(j - E + 1):
                                x = t + alpha + eN + e3
                                c = x + j + E
                                r = max(c - t - (j - E), 0)
                                assert r >= eN
                        else:
                            e3 = 0
                            x = t + alpha + eN
                            c = x + 2 * j
                            r = max(c - t, 0)
                            assert r >= eN


def large_gap_lower() -> None:
    # Pure algebra: a>=d0*v, u=d0*L, gstar/v>=1.
    for d0 in range(1, 8):
        for L in range(1, 8):
            for v in range(1, 8):
                u = d0 * L
                # Choose a at the threshold and the minimal overlap factor 1.
                a = d0 * v
                F_lower = L * (u + 2 * v) * a
                assert F_lower == u * v * (u + 2 * v)
                assert F_lower > u * u * v

                # Whenever u/v>Q, the claimed Q^2 v^3 lower follows.
                Q = max(0, (u - 1) // v)
                if Q > 0 and u > Q * v:
                    assert u * u * v > Q * Q * v**3


def circular_bound() -> None:
    # Verify the exact interval-to-nearest-multiple bound used after d0 stripping.
    for m2 in range(1, 30):
        for c10 in range(0, m2 + 3):
            for s10 in range(0, m2 + 3):
                for d in range(0, 2 * m2 + 1):
                    vals = []
                    for shift in range(-s10, c10 + 1):
                        z = d + shift
                        r = min(z % m2, (-z) % m2)
                        vals.append(r)
                    actual = min(vals)
                    bound = max(0, (m2 - c10 - s10) // 2)
                    assert actual <= bound
                    assert actual <= m2 // 2


def main() -> None:
    exact_normalization_toy()
    source_gap_toy()
    local_depth_symbolic()
    corrected_split_coverage()
    large_gap_lower()
    circular_bound()
    print("DD gcd-normal d0 gap CRT dichotomy checks passed")


if __name__ == "__main__":
    main()
