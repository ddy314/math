#!/usr/bin/env python3
"""Mechanical checks for genuine-discriminant-cross-audit.md."""

from __future__ import annotations

from decimal import Decimal, getcontext


def check_height_ledger() -> None:
    """Check the leading base-10 height arithmetic used in the audit."""

    getcontext().prec = 30
    S = Decimal(1)
    h_Q = S
    h_G = S
    h_kappa = Decimal(2) * S
    h_C = Decimal("4.5") * S
    h_N12 = Decimal(4) * S

    h_M = h_kappa + h_G + h_C
    h_M2 = Decimal(2) * h_M
    h_R = Decimal(2) * h_Q + h_N12 + h_kappa + h_kappa
    h_W = h_M
    h_Omega = h_Q + Decimal(0) + h_kappa

    assert h_M == Decimal("7.5")
    assert h_M2 == Decimal(15)
    assert h_R == Decimal(10)
    assert h_M2 - h_R == Decimal(5)
    assert h_W - h_Omega == Decimal("4.5")

    h_y2_over_y3 = Decimal("-4.5")
    cross_ratio = (h_Omega - h_W) + h_y2_over_y3
    assert cross_ratio == Decimal(-9)


def check_frontier_digit_arithmetic() -> None:
    n3 = Decimal("6.308883577618")
    m3 = Decimal("2.808883577618")
    d3 = n3 - m3
    s2 = Decimal(-1)
    k12 = s2 + d3
    m2 = Decimal(1)
    n1 = Decimal(1)

    assert d3 == Decimal("3.500000000000")
    assert k12 == Decimal("2.500000000000")
    assert m2 + k12 + n1 == Decimal("4.500000000000")


def main() -> None:
    check_height_ledger()
    check_frontier_digit_arithmetic()
    print("DD genuine discriminant-cross audit checks passed")


if __name__ == "__main__":
    main()
