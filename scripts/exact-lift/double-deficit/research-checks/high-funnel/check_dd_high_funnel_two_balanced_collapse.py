#!/usr/bin/env python3
"""Mechanical checks for high-funnel-two-balanced-collapse.md."""

from __future__ import annotations

import math


def constant_check() -> None:
    a = math.log10(2)
    c = (13 + 10 * a) / (2 * (1 + a))
    c2 = 2 + 3 * (1.5 + a) / (1 + a)
    assert abs(c - c2) < 1e-14
    assert abs(c - 6.152932680260361) < 1e-12
    assert c < 6.215109404735


def dual_check() -> None:
    a = math.log10(2)
    lam = (1.5 + a) / (1 + a)

    # Objective after 2-balanced and G5<=M/4:
    # (1.5+a) M + (a/2) Q2 + 1*G0.
    # Budget: (1+a)M + 2a Q2 + a N2 + 2 G0 <= 3.
    assert abs(lam * (1 + a) - (1.5 + a)) < 1e-14
    assert lam * (2 * a) >= a / 2
    assert lam * a >= 0
    assert lam * 2 >= 1


def final_five_geometry() -> None:
    # M=2Q5+4G5+N5 implies G5<=M/4.
    for q5 in range(20):
        for g5 in range(20):
            for n5 in range(20):
                m = 2 * q5 + 4 * g5 + n5
                assert 4 * g5 <= m


def main() -> None:
    constant_check()
    dual_check()
    final_five_geometry()
    print("DD 2-balanced collapse checks passed")


if __name__ == "__main__":
    main()
