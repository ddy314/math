#!/usr/bin/env python3
"""Finite sanity audit for the DD charged-first Z0 valuation lemma.

This script is not a proof.  It exhausts a bounded box of the nonnegative
valuation variables used in
`dd-z0-charged-first-2026-08-21.md` and checks the purely arithmetic
implications claimed there.
"""

from __future__ import annotations

import argparse


def check_box(limit: int) -> int:
    checked = 0

    for x in range(limit + 1):
        for t in range(limit + 1):
            for g in range(t + 1):  # existing theorem: g <= t
                for omega in range(limit + 1):
                    for r in range(limit + 1):
                        for alpha in range(limit + 1):
                            # Existing general-transfer refinement.
                            if x > max(t, 2 * g + omega, r):
                                continue

                            b = min(x, t)
                            a_star = min(x - b, alpha)
                            z = x - b - a_star

                            assert z == max(x - t - alpha, 0)

                            z0 = max(0, r + g + omega - alpha)
                            sharp_cap = max(
                                0,
                                g + omega - alpha,
                                r - t - alpha,
                            )

                            assert z <= sharp_cap
                            assert z <= z0

                            r_star = max(r - t - alpha, 0)
                            g_star = max(g + omega - alpha, 0)

                            z3 = min(z, r_star)
                            z_gaussian = z - z3

                            assert z_gaussian <= g_star

                            zg = min(z_gaussian, g)
                            zomega = z_gaussian - zg

                            assert z == z3 + zg + zomega
                            assert z3 <= r_star
                            assert zg <= g
                            assert zomega <= omega
                            assert zomega <= x

                            checked += 1

    return checked


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="maximum value for each valuation variable (default: 10)",
    )
    args = parser.parse_args()

    if args.limit < 0:
        raise SystemExit("--limit must be nonnegative")

    checked = check_box(args.limit)
    print(
        "charged-first DD valuation audit passed: "
        f"{checked} admissible tuples checked (limit={args.limit})"
    )


if __name__ == "__main__":
    main()
