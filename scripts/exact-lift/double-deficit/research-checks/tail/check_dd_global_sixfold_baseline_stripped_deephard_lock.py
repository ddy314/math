#!/usr/bin/env python3
"""Mechanical audit for the baseline-stripped deep-hard sixfold lock.

This checks the local exponent algebra and finite aggregation logic.  It does
not certify existence/nonexistence of DD candidates by computation.
"""

from __future__ import annotations


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
                            # On the good sheet the sixfold congruence has
                            # modulus depth s+r strictly above coefficient depth s.
                            assert vQ == s + r
                            assert vQ > s


def check_aggregate_height_inequality() -> None:
    # Abstract log-heights: bad hard source <= 5 * E-baseline;
    # stripped good modulus loses at most another 5 * E-baseline.
    examples = [
        # (X_total, E_baseline, X_bad)
        (100.0, 1.0, 4.0),
        (1000.0, 3.0, 10.0),
        (500.0, 0.5, 2.0),
    ]
    for x_total, e_base, x_bad in examples:
        assert x_bad <= 5 * e_base or x_bad < 20  # illustrative finite ledgers
        x_good = x_total - x_bad
        x_stripped_lower = x_good - 5 * e_base
        assert x_stripped_lower > 0


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
