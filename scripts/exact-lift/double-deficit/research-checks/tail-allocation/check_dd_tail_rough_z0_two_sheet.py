#!/usr/bin/env python3
"""Finite algebra audit for the DD Z0 two-sheet payer collapse.

This script checks bounded valuation tuples only.  The proof itself is the
case split in tail-rough-z0-two-sheet-collapse.md.
"""

from __future__ import annotations


def check(limit: int = 18) -> int:
    rows = 0
    for x in range(1, limit):
        for r in range(limit):
            for t in range(limit):
                for g in range(t + 1):
                    for omega in range(limit):
                        n = 2 * g + omega
                        if x > max(t, n, r):
                            continue

                        e3 = min(x, r)
                        rem = x - e3
                        eB = min(rem, t)
                        eP = x - eB

                        # Hidden max-payer inequality.
                        assert eP <= max(r, n - t)

                        if x <= r + t:
                            # Sheet T: projective depth is fully read by R3den.
                            assert eP <= r
                        else:
                            # Sheet N: bottom depth saturates and N0 pays all x.
                            assert x > r
                            assert x > t
                            assert e3 == r
                            assert eB == t
                            assert x <= n
                            assert eP == x - t
                            assert eP <= n - t

                        for alpha in range(limit):
                            ea = min(eP, alpha)
                            eZ = eP - ea

                            # Sharpened Z0 max-payer bound.
                            assert eZ <= max(
                                max(r - alpha, 0),
                                max(n - t - alpha, 0),
                            )

                            if x <= r + t:
                                # X_{a,T} X_{Z,3} | R3den.
                                assert ea + eZ == eP
                                assert ea + eZ <= r
                                assert eZ <= max(r - alpha, 0)
                            else:
                                # X_{B,N} X_{a,N} X_{Z,N} | N0.
                                assert eB == t
                                assert eB + ea + eZ == x
                                assert eB + ea + eZ <= n
                                assert eZ <= max(n - t - alpha, 0)

                            # Inert refinement: omega=0 and g<=t.
                            if omega == 0 and eZ > 0 and x > r + t:
                                assert eZ <= max(g - alpha, 0)
                                assert g > alpha

                        rows += 1
    return rows


def main() -> None:
    rows = check()
    print(f"DD Z0 two-sheet audit passed ({rows} valuation tuples)")


if __name__ == "__main__":
    main()
