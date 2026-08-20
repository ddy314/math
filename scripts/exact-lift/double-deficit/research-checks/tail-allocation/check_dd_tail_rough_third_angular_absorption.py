#!/usr/bin/env python3
"""Mechanical checks for tail-rough-third-angular-absorption.md."""

from __future__ import annotations


def check_sphere_sheet(limit: int = 20) -> int:
    rows = 0
    for r in range(1, limit):
        for omega in range(limit):
            total = 2 * r + omega
            # Gap sheet.
            A, comp = total, 0
            z0 = max(comp - r, 0)
            assert z0 + A >= r + omega
            # Complementary sheet.
            A, comp = 0, total
            z0 = max(comp - r, 0)
            assert z0 == r + omega
            assert z0 + A >= r + omega
            rows += 2
    return rows


def check_layer_absorption(limit: int = 20) -> int:
    rows = 0
    for x in range(1, limit):
        for r in range(1, limit):
            for t in range(limit):
                for omega in range(limit):
                    # third-exclusive => g=0; general transfer becomes this.
                    if x > max(t, omega, r):
                        continue
                    e3 = min(x, r)
                    rem = x - e3
                    eB = min(rem, t)
                    rem -= eB
                    eA = rem
                    if eA:
                        assert x > r + t
                        assert x <= omega
                        assert eA <= omega
                    assert e3 + eA <= r + omega
                    rows += 1
    return rows


def main() -> None:
    a = check_sphere_sheet()
    b = check_layer_absorption()
    print(f"DD third-angular absorption checks passed ({a+b} rows)")


if __name__ == "__main__":
    main()
