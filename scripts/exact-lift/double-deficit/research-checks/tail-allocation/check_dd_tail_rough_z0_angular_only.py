#!/usr/bin/env python3
"""Finite algebra audit for the DD Z0 angular-only collapse.

The bounded enumeration checks only the valuation bookkeeping on Sheet N.
The exact small-factor charge in the proof file is an integer inequality and
is not certified by this finite search.
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

                        # Only the norm-overflow sheet needs the new split.
                        if x <= r + t:
                            continue

                        assert x > r
                        assert x > t
                        assert x <= n
                        assert e3 == r
                        assert eB == t
                        assert eP == x - t

                        for alpha in range(limit):
                            ea = min(eP, alpha)
                            eZ = eP - ea

                            # Previous two-sheet theorem.
                            assert eZ <= max(n - t - alpha, 0)

                            common_cap = max(g - alpha, 0)
                            eZC = min(eZ, common_cap)
                            eZA = eZ - eZC

                            # Common remainder is already under bottom depth.
                            assert eZC <= g
                            assert eZC <= eB

                            # Independent remainder is primitive angular depth.
                            assert eZA <= omega

                            # Orientation transfer uses x <= c=v_p(C_Q).
                            assert eZA <= eZ <= eP <= x
                            assert eZA <= min(x, omega)

                            # Inert case omega=0 has no independent remainder.
                            if omega == 0:
                                assert eZA == 0

                            rows += 1
    return rows


def main() -> None:
    rows = check()
    print(f"DD Z0 angular-only audit passed ({rows} sheet-N tuples)")


if __name__ == "__main__":
    main()
