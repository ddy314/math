#!/usr/bin/env python3
"""Abstract valuation check for tail-rough-canonical-payer-decomposition.md."""

from __future__ import annotations


def check(limit: int = 24) -> int:
    rows = 0
    for x in range(1, limit):
        for r in range(limit):
            for t in range(limit):
                for g in range(t + 1):
                    for omega in range(limit):
                        if x > max(t, 2 * g + omega, r):
                            continue
                        # x<=c on X_Q support; choose the minimal allowed c=x.
                        c = x
                        # Same-orientation transfer guarantees this much N_num depth.
                        nu = min(c, omega)

                        e3 = min(x, r)
                        rem = x - e3
                        eB = min(rem, t)
                        rem -= eB
                        eG = min(rem, g)
                        rem -= eG
                        eA = rem

                        assert x == e3 + eB + eG + eA
                        assert e3 <= r
                        assert eB <= t
                        assert eG <= g
                        assert eA <= nu
                        rows += 1
    return rows


def main() -> None:
    rows = check()
    print(f"DD canonical payer decomposition checks passed ({rows} rows)")


if __name__ == "__main__":
    main()
