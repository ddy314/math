#!/usr/bin/env python3
"""Mechanical valuation ledger for tail-rough-general-transfer.md.

This is not a proof of the p-adic unit cancellations.  It exhaustively checks
bounded abstract valuation rows against the identities used in the written
case split, including the only place where a difference of equal-valuation
terms may lift.
"""

from __future__ import annotations


def tropical_ok(vals: tuple[int, int, int]) -> bool:
    m = min(vals)
    return sum(v == m for v in vals) >= 2


def first_g0_possible(n_term: int, mu_term: int, second_arg: int, g0: int) -> bool:
    """Whether v(gcd(N nu^2-mu^2,2Gmu nu)) can equal g0.

    If the two summands in the first argument have unequal valuations, its
    valuation is their minimum.  If equal, arbitrary further cancellation is
    allowed; this deliberately over-approximates the unit arithmetic.
    """
    if n_term != mu_term:
        return min(min(n_term, mu_term), second_arg) == g0
    base = n_term
    if g0 < min(base, second_arg):
        return False
    if second_arg < g0:
        return False
    # If second_arg == g0, any first valuation >= g0 works.
    # If second_arg > g0, choose first valuation exactly g0 (provided g0>=base).
    return g0 >= base


def check_box(limit: int = 18) -> int:
    rows = 0
    for E in range(limit):
        for j in range(limit):
            M = max(E, j)
            delta = M - j
            r3 = max(j - E, 0)

            for c in range(2 * limit):
                x = c - j - min(E, j)
                if x <= 0:
                    continue

                qv = E + c
                kv = 3 * E + c - j
                assert kv > 2 * E

                for t in range(limit):
                    for n0 in range(limit):
                        # We only enumerate the negation of the theorem.
                        if x <= max(t, n0, r3):
                            continue

                        for A in range(2 * limit):
                            diff = 2 * E + A - M
                            if diff >= 0:
                                r, s = diff, 0
                            else:
                                r, s = 0, -diff

                            g0 = 2 * E - j + r + s
                            if g0 < 0:
                                continue
                            if A + g0 != delta + 2 * r:
                                continue

                            n_total = 2 * E + n0
                            if not first_g0_possible(
                                n_total + 2 * s,
                                2 * r,
                                2 * E + r + s,
                                g0,
                            ):
                                continue

                            gap = (
                                j + 2 * A,
                                M + t + A,
                                c - E + 2 * M + n0,
                            )
                            if not tropical_ok(gap):
                                continue

                            quad = (
                                qv + 2 * E + 2 * r,
                                2 * E + kv + t + r + s,
                                kv + qv + n_total + 2 * s,
                            )
                            if not tropical_ok(quad):
                                continue

                            rows += 1

                            # Written Sections 3--4: the only possible hard
                            # valuation sheet has the first two gap terms tied.
                            assert A == t + delta
                            Delta = c + j - E + n0 - 2 * t
                            assert Delta > 0

                            # Written Section 5: K and discriminant inner term
                            # have strict valuation separation by Delta.
                            k_first = 4 * E + 2 * t
                            k_second = 4 * E + 2 * c + n0
                            assert k_second > k_first

                            inner_first = kv + k_first
                            inner_second = 6 * E + 2 * c + n0
                            assert inner_second - inner_first == Delta
                            assert inner_second > inner_first

                            w = 5 * E + c - j + t
                            baseline = M + t
                            d_der = w - baseline
                            assert d_der == 5 * E + c - j - M
                            assert d_der >= 0

                            # If d_der>0, derivative and gap contacts contradict
                            # v(mathcal M)=M+t.  Thus a surviving valuation row
                            # would need d_der=0; the theorem's strict
                            # x>third-excess assumption rules this out.
                            if d_der == 0:
                                assert j > E
                                assert c == 2 * j - 5 * E
                                assert x == j - 6 * E
                                assert x <= r3
                                raise AssertionError(
                                    "d_der=0 cannot coexist with x>r3"
                                )

    return rows


def main() -> None:
    rows = check_box()
    print(f"DD general rough transfer valuation checks passed ({rows} hard rows)")


if __name__ == "__main__":
    main()
