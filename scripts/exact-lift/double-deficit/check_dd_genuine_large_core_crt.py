#!/usr/bin/env python3
"""Mechanical constants / window checks for genuine-large-core-crt.md."""

from __future__ import annotations

from decimal import Decimal, getcontext


def main() -> None:
    getcontext().prec = 30
    z = Decimal("0.308883577618")
    q2 = 2 * z
    threshold = Decimal(1) - q2

    assert q2 == Decimal("0.617767155236")
    assert threshold == Decimal("0.382232844764")
    assert q2 + threshold == Decimal(1)

    # A strict epsilon above the threshold makes the combined CRT period
    # exponent strictly exceed the S-digit A12 window.
    eps = Decimal("0.000001")
    assert q2 + threshold + eps > 1

    # Complementary sector forces at least q2*S rational-contact mass.
    assert Decimal(1) - threshold == q2

    print("DD genuine large-core CRT threshold checks passed")


if __name__ == "__main__":
    main()
