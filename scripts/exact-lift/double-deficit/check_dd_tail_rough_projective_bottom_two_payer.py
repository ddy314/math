#!/usr/bin/env python3
"""Abstract valuation checks for tail-rough-projective-bottom-two-payer.md."""

from __future__ import annotations


def check(limit: int = 28) -> int:
    rows = 0
    for x in range(1, limit):
        for r in range(limit):
            for g in range(limit):
                for t in range(g, limit):
                    for omega in range(limit):
                        if x > max(t, 2 * g + omega, r):
                            continue

                        e3 = min(x, r)
                        rem = x - e3
                        eB = min(rem, t)
                        rem -= eB
                        eG = min(rem, g)
                        rem -= eG
                        eA = rem

                        if eA:
                            assert x > r + t + g
                            assert x <= 2 * g + omega
                            assert eA <= omega

                        eP = e3 + eG + eA
                        assert eP + eB == x
                        assert eP <= r + g + omega

                        # Projective formula gives v(Z0*a)=max(alpha,r+g+omega)
                        # for arbitrary alpha>=0; its minimum is r+g+omega.
                        for alpha in (0, max(0, r + g + omega - 1), r + g + omega, 2 * limit):
                            z0a = max(alpha, r + g + omega)
                            assert eP <= z0a
                        rows += 1
    return rows


def main() -> None:
    rows = check()
    print(f"DD projective-bottom two-payer checks passed ({rows} rows)")


if __name__ == "__main__":
    main()
