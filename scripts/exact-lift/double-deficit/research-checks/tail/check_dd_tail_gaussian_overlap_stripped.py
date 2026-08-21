#!/usr/bin/env python3
"""Finite sanity audit for dd-gaussian-overlap-stripped-2026-08-21.md.

The markdown file contains the unbounded proof.  This script checks the local
valuation arithmetic in a bounded box and separately verifies the exact norm
resultant as a polynomial identity on many integer samples.
"""

from __future__ import annotations


BOUND = 12


def audit_nonthird() -> int:
    count = 0
    for E in range(BOUND + 1):
        for j in range(BOUND + 1):
            r = max(j - E, 0)
            for c in range(BOUND + 1):
                x = max(c - j - min(E, j), 0)
                if x == 0:
                    continue
                assert x <= c
                for t in range(BOUND + 1):
                    for g in range(t + 1):
                        a_circ = t - g
                        for alpha in range(BOUND + 1):
                            # No third-excess capacity.
                            if r > t + alpha:
                                continue
                            z = max(x - t - alpha, 0)
                            if z <= g:
                                continue
                            e = z - g
                            for omega in range(BOUND + 1):
                                # General-transfer refinement.
                                if x > max(t, 2 * g + omega, r):
                                    continue

                                count += 1
                                lhs = e + a_circ
                                assert lhs == x - alpha - 2 * g
                                assert lhs <= c
                                assert lhs <= omega
                                assert lhs <= min(c, omega)
    return count


def audit_third_to_gaussian() -> int:
    count = 0
    for E in range(BOUND + 1):
        for j in range(E + 1, BOUND + 1):
            r = j - E
            for c in range(BOUND + 1):
                x = max(c - j - E, 0)
                if x == 0 or x <= r:
                    continue
                # dd-third-excess-collapse has already forced t=g=alpha=0.
                t = g = alpha = 0
                a_circ = 0
                for omega in range(BOUND + 1):
                    if x > max(t, 2 * g + omega, r):
                        continue
                    count += 1
                    e = x
                    assert x <= omega
                    assert e + a_circ <= min(c, omega)
    return count


def audit_norm_resultant() -> int:
    count = 0
    # Exact identity:
    # B1^2*N_num - N_ang
    # = abar1^2*(B1*D-B2)*(B1*D+B2).
    for abar1 in range(1, 8):
        for abar2 in range(1, 8):
            for B1 in range(1, 8):
                for B2 in range(1, 8):
                    for D in (1, 10, 100, 1000):
                        n_num = (abar1 * D) ** 2 + abar2**2
                        n_ang = (abar1 * B2) ** 2 + (abar2 * B1) ** 2
                        lhs = B1**2 * n_num - n_ang
                        rhs = abar1**2 * (B1 * D - B2) * (B1 * D + B2)
                        assert lhs == rhs
                        count += 1
    return count


def main() -> None:
    n_nonthird = audit_nonthird()
    n_third = audit_third_to_gaussian()
    n_identity = audit_norm_resultant()

    assert n_nonthird > 0
    assert n_third > 0
    assert n_identity > 0

    print("DD Gaussian overlap-stripping finite audit: PASS")
    print(f"bound={BOUND}")
    print(f"non-third Gaussian states={n_nonthird}")
    print(f"third-to-Gaussian states={n_third}")
    print(f"norm-resultant integer samples={n_identity}")


if __name__ == "__main__":
    main()
