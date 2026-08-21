#!/usr/bin/env python3
"""Finite algebra audit for the DD coefficient-stripped angular residual.

The search checks bounded valuation tuples.  It is only a consistency audit;
the unbounded proof is in tail-rough-angular-coefficient-stripped.md.
"""

from __future__ import annotations


def check(limit: int = 16) -> int:
    rows = 0
    for x in range(1, limit):
        for r in range(limit):
            for g in range(limit):
                for q in range(limit):
                    t = g + q
                    for omega in range(limit):
                        n = 2 * g + omega
                        if x > max(t, n, r):
                            continue
                        if x <= r + t:
                            continue

                        e3 = min(x, r)
                        eB = min(x - e3, t)
                        eP = x - eB
                        assert e3 == r
                        assert eB == t
                        assert x <= n

                        # Minimal source depth is c=x; larger c only helps.
                        for c in range(x, limit):
                            for alpha in range(limit):
                                ea = min(eP, alpha)
                                eZ = eP - ea
                                common_cap = max(g - alpha, 0)
                                eZC = min(eZ, common_cap)
                                eZA = eZ - eZC

                                assert eZA <= max(omega - q, 0)
                                assert eZA <= max(c - q, 0)

                                # Exact same-orientation valuation possibilities.
                                if omega < c:
                                    nu_values = [omega]
                                elif omega > c:
                                    nu_values = [c]
                                else:
                                    nu_values = range(c, limit)

                                for nu in nu_values:
                                    assert min(omega, nu) == min(omega, c)
                                    assert eZA <= max(nu - q, 0)

                                    if eZA > 0:
                                        assert q < omega
                                        assert q < c
                                        assert q < nu
                                        left = min(omega - q, nu - q)
                                        right = min(omega - q, c - q)
                                        assert left == right

                                    rows += 1
    return rows


def main() -> None:
    rows = check()
    print(
        "DD coefficient-stripped angular audit passed "
        f"({rows} valuation cases)"
    )


if __name__ == "__main__":
    main()
