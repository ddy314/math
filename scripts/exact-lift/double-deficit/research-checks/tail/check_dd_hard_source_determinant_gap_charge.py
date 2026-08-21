#!/usr/bin/env python3
"""Finite valuation audit for corrected DD hard-source determinant/gap charge.

This checks only the exponent arithmetic in
`dd-hard-source-determinant-gap-charge-2026-08-22.md`.
It is not a proof of the global DD statement.
"""

from __future__ import annotations


def audit(limit: int = 14) -> None:
    checked = 0

    for E in range(limit + 1):
        for j in range(limit + 1):
            for c in range(1, 2 * limit + 4):
                x = max(c - j - min(E, j), 0)
                if x == 0:
                    continue

                for t in range(limit + 1):
                    for n0 in range(limit + 1):
                        r3 = max(j - E, 0)
                        if not (x > t and x > n0 and x > r3):
                            continue

                        delta = max(E - j, 0)
                        gap_depth = t + delta

                        # Hard-H implies the a3*Q term is strictly deeper
                        # than the b3*C term in the decimal determinant.
                        q_depth = E + c
                        det_depth = j + t
                        assert q_depth > det_depth

                        d = min(x, det_depth)
                        rem_after_det = x - d
                        a_charge = min(rem_after_det, gap_depth)
                        residual = x - d - a_charge

                        by_M = max(x - max(E, j) - 2 * t, 0)
                        by_c = max(c - E - 2 * j - 2 * t, 0)

                        assert residual == by_M == by_c
                        if residual > 0:
                            assert c > E + 2 * j + 2 * t

                        checked += 1

    assert checked > 0
    print(f"DD corrected hard-source charge audit passed ({checked} rows)")


if __name__ == "__main__":
    audit()
