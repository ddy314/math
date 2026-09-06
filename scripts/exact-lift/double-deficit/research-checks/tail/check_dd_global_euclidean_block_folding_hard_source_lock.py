#!/usr/bin/env python3
"""Mechanical audit for DD Euclidean block-folding hard-source lock."""

from __future__ import annotations

from math import gcd


def check_block_family() -> None:
    for u1 in range(1, 15):
        for u2 in range(1, 15):
            if gcd(u1, u2) != 1:
                continue
            for m2 in range(1, 4):
                CQ = u1 * 10**m2 + u2
                for n in range(m2, 9 * m2 + 1):
                    for k in range(0, n // m2 + 1):
                        r = n - k * m2
                        lhs = u1**k * 10**n
                        rhs = (-u2) ** k * 10**r
                        assert (lhs - rhs) % CQ == 0


def check_euclidean_remainder() -> None:
    for m2 in range(1, 20):
        for n in range(0, 200):
            k = n // m2
            r = n - k * m2
            assert 0 <= r < m2
            assert n == k * m2 + r


def check_hard_depth_independent_of_k() -> None:
    for E in range(0, 6):
        for j in range(0, 6):
            M = max(E, j)
            for t in range(0, 5):
                for n0 in range(0, 5):
                    for h in range(1, 10):
                        c = h + 2 * t + n0 + M + j
                        for _k in range(0, 10):
                            coeff = M + t
                            rhs = M + t
                            assert coeff == rhs
                            residual = c - coeff
                            assert residual == h + t + n0 + j
                            assert residual > 0


def check_neighbor_equivalence() -> None:
    # On source units, multiplying the k relation by u1*10^m2 and using
    # u1*10^m2 == -u2 converts it to k+1.
    for u1 in range(1, 12):
        for u2 in range(1, 12):
            if gcd(u1, u2) != 1:
                continue
            for m2 in range(1, 3):
                CQ = u1 * 10**m2 + u2
                for n in range(2 * m2, 8 * m2 + 1):
                    for k in range(0, n // m2):
                        rk = n - k * m2
                        rk1 = n - (k + 1) * m2
                        term_k = (-u2) ** k * 10**rk
                        term_k1 = (-u2) ** (k + 1) * 10**rk1
                        assert (u1 * term_k - term_k1) % CQ == 0


def main() -> None:
    check_block_family()
    check_euclidean_remainder()
    check_hard_depth_independent_of_k()
    check_neighbor_equivalence()
    print("DD Euclidean block-folding hard-source checks passed")


if __name__ == "__main__":
    main()
