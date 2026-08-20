#!/usr/bin/env python3
"""Mechanical ledger for frontier-five-adic-closure.md.

This script checks the frontier constants and abstract valuation mismatch.
The semantic identification of W is documented in the proof note via the
canonical global notation / migrated DD section; this script does not certify
symbol scope.  It is not a global DD emptiness certificate.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


def constants() -> None:
    getcontext().prec = 40
    m = Decimal("2.808883577618")
    T = Decimal("1.872589051745")
    d = Decimal("3.5")

    # Stored frontier values are rounded; 3T=2m at leading order.
    assert abs(Decimal(3) * T - Decimal(2) * m) < Decimal("2e-12")

    first = Decimal(2) * T - m
    half_T = T / Decimal(2)
    assert abs(first - half_T) < Decimal("2e-12")
    assert half_T < T < d
    assert d - half_T > Decimal("2.5")


def abstract_mismatch() -> None:
    # Model r=T/2+o(S), s>=T+o(S), d=3.5S+o(S).
    # For sufficiently small normalized errors the two valuations remain
    # distinct and the sum has the shallow valuation, below d.
    T = 1.872589051745
    d = 3.5
    for eps in (1e-4, 1e-3, 1e-2, 5e-2, 1e-1):
        r_hi = T / 2 + eps
        s_lo = T - eps
        d_lo = d - eps
        assert r_hi < s_lo
        assert r_hi < d_lo


def tail_normalization() -> None:
    # Abstract leading exponents: e3=m-T, v5(L)=m-e3=T.
    m = 2.808883577618
    T = 1.872589051745
    e3 = m - T
    l5 = m - e3
    assert abs(l5 - T) < 1e-12
    assert 0 < e3 < m


def main() -> None:
    constants()
    abstract_mismatch()
    tail_normalization()
    print("DD 6.308883 frontier five-adic closure ledger passed")


if __name__ == "__main__":
    main()
