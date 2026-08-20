#!/usr/bin/env python3
"""Mechanical checks for mixed-rational-good-extension.md.

The script checks the abstract same-prime Bad exclusion and the partial Good
excess / gcd-ladder bookkeeping.  It is not an emptiness proof.
"""

from __future__ import annotations


def bad_same_prime_exclusion() -> None:
    # On a partial rational main prime p^h|E, e0 and explicit coefficients
    # are p-units.  Therefore T_c has depth zero and cannot receive any
    # positive Bad depth.
    for h in range(1, 10):
        v_e0 = 0
        v_rtilde = 0
        v_5 = 0
        v_tc = v_e0 + 2 * v_rtilde + v_5
        assert v_tc == 0
        assert not (v_tc >= h)


def partial_good_excess_ledger() -> None:
    for h in range(1, 9):
        for r in range(0, 9):
            for n in range(0, 9):
                for eps in range(0, 9):
                    if eps > 0 and r != n:
                        continue
                    a = min(r, n) + eps
                    eps_axis = max(a - n, 0)
                    assert eps_axis == eps

                    c = max(h - n, 0)
                    x = min(c, eps)
                    assert x >= 0

                    for k in range(1, 6):
                        ladder = min(k * c, eps)
                        assert ladder >= x


def main() -> None:
    bad_same_prime_exclusion()
    partial_good_excess_ledger()
    print("DD mixed rational Good extension checks passed")


if __name__ == "__main__":
    main()
