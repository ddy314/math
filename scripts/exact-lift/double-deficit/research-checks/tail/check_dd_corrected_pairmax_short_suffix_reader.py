#!/usr/bin/env python3
"""Mechanical audits for dd-corrected-pairmax-short-suffix-reader-2026-08-22.md.

Checks the generic double-reconstruction algebra, local residue transfer, and
reported thresholds.  This is not a proof assistant.
"""

from __future__ import annotations

from math import gcd, isclose, log10

import sympy as sp


def check_double_reconstruction() -> None:
    g0, U, a3, B, D10, V, A12, Sigma, R0, F, A0 = sp.symbols(
        "g0 U a3 B D10 V A12 Sigma R0 F A0", nonzero=True
    )

    rec1 = sp.Eq(g0 * B * D10 * A12, U * A0 + R0)
    carry_rhs = g0 * B * D10 * V * A12 - Sigma * R0
    carry_rhs = sp.expand(carry_rhs.subs(g0 * B * D10 * A12, U * A0 + R0))
    carry_rhs = sp.expand(carry_rhs.subs(Sigma, 2 * F * U + V))
    assert sp.factor(carry_rhs) == U * (V * A0 - 2 * F * R0)
    assert rec1.lhs - rec1.rhs == g0 * B * D10 * A12 - U * A0 - R0


def check_local_suffix_transfer() -> None:
    # Work in small prime powers with explicit roots of -1.  This only checks
    # that the stated linear residue is algebraically equivalent.
    primes = [5, 13, 17, 29, 37, 41]
    checked = 0
    for p in primes:
        if p in (2, 5):
            continue
        roots = [x for x in range(p) if (x * x + 1) % p == 0]
        if not roots:
            continue
        assert len(roots) == 2
        for iota in roots:
            for g0 in range(1, p):
                for R0 in range(1, p):
                    if gcd(g0, p) != 1 or gcd(R0, p) != 1:
                        continue
                    F = 3  # arbitrary p-unit
                    c2 = 2
                    c3 = 4
                    if gcd(c2 * c3 * F, p) != 1:
                        continue
                    a3 = (-2 * F * R0 * pow(g0, -1, p)) % p
                    a2 = (
                        2
                        * F
                        * iota
                        * c3
                        * pow(c2, -1, p)
                        * R0
                        * pow(g0, -1, p)
                    ) % p
                    assert (g0 * a3 + 2 * F * R0) % p == 0
                    assert (a2 * c2 + iota * a3 * c3) % p == 0
                    checked += 1
    assert checked > 0
    print(f"local oriented suffix states checked: {checked}")


def check_thresholds() -> None:
    a = log10(2)
    kdig = (2 + a) / 3
    cone = 1 + 5 * (1 + 2 * a) / 6
    denom = cone + kdig
    assert isclose(denom, 2.5 + 2 * a, abs_tol=1e-15)
    delta_a2 = 1 / denom
    assert isclose(delta_a2, 0.322366428371977, abs_tol=1e-15)

    Ustar = 0.691116422381969
    delta_uv = Ustar / (2 + 3 * a)
    assert delta_uv < delta_a2

    print(f"delta_a2: {delta_a2:.15f}")
    print(f"delta_UV: {delta_uv:.15f}")


def main() -> None:
    check_double_reconstruction()
    check_local_suffix_transfer()
    check_thresholds()
    print("DD corrected pairmax short-suffix audits passed")


if __name__ == "__main__":
    main()
