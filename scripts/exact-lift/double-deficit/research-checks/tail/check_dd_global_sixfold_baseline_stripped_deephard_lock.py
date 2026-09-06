#!/usr/bin/env python3
"""Mechanical audit for the baseline-stripped deep-hard sixfold lock.

This checks the local exponent algebra and exact finite aggregation inequalities.
It does not certify existence/nonexistence of DD candidates by computation.
"""

from __future__ import annotations

from math import log


def check_local_ledger() -> None:
    # Sweep small deep-hard valuation ledgers.
    for E in range(0, 6):
        for j in range(0, 6):
            M = max(E, j)
            for t in range(0, 4):
                for n0 in range(0, 4):
                    y = 2 * t + n0 + M + j
                    for h in range(y + 1, y + 10):
                        c = h + y
                        vQ = E + c
                        s = M + t + 6 * E
                        r = vQ - s
                        expected = h + t + n0 + j - 5 * E
                        assert r == expected

                        if r <= 0:
                            assert h <= 5 * E - t - n0 - j
                            assert h <= 5 * E
                        else:
                            assert vQ == s + r
                            assert vQ > s
                            assert r >= h - 5 * E


def check_aggregate_height_inequality() -> None:
    # A finite synthetic valuation table.  We use logarithmic prime weights,
    # exactly as the proof sums h_p log p and E_p log p.
    rows = [
        # (p, E, j, t, n0, h); every row is deep-hard: h > 2t+n0+M+j.
        (3, 1, 0, 0, 0, 3),    # bad: r=-2, h<=5E
        (7, 1, 0, 0, 0, 8),    # good: r=3
        (13, 0, 1, 0, 0, 5),   # good: r=6
        (17, 1, 1, 1, 0, 8),   # good: r=5
    ]

    log_x_total = 0.0
    log_e_total = 0.0
    log_x_bad = 0.0
    log_x_good = 0.0
    log_x_stripped = 0.0
    log_e_good = 0.0

    for p, E, j, t, n0, h in rows:
        M = max(E, j)
        y = 2 * t + n0 + M + j
        assert h > y
        r = h + t + n0 + j - 5 * E
        w = log(p)

        log_x_total += h * w
        log_e_total += E * w
        if r <= 0:
            log_x_bad += h * w
            assert h <= 5 * E
        else:
            log_x_good += h * w
            log_x_stripped += r * w
            log_e_good += E * w
            assert r >= h - 5 * E

    # Exact aggregate consequences of the per-prime inequalities.
    assert log_x_bad <= 5 * log_e_total + 1e-12
    assert abs(log_x_good - (log_x_total - log_x_bad)) < 1e-12
    assert log_x_stripped + 1e-12 >= log_x_good - 5 * log_e_good


def check_full_height_margin() -> None:
    z_star = 0.308883577618031
    U_star = 1 - z_star
    assert abs(U_star - 0.691116422381969) < 1e-12
    assert U_star > 0


def main() -> None:
    check_local_ledger()
    check_aggregate_height_inequality()
    check_full_height_margin()
    print("DD global sixfold baseline-stripped deep-hard checks passed")


if __name__ == "__main__":
    main()
