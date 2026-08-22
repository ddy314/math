#!/usr/bin/env python3
"""Finite sanity checks for the corrected DD terminal denominator/S-unit entropy ledger.

This script does not prove the asymptotic theorem.  It checks the numerical
constants, the two-variable shared-budget inequality on a finite grid, the
exact divisor-assignment reconstruction used in the counting argument, and
the final exponent bookkeeping.
"""

from __future__ import annotations

import math


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def main() -> None:
    a = math.log10(2.0)
    lam = (2.0 + a) / (1.0 + 2.0 * a)
    inv_lam = 1.0 / lam

    c_uv = 2.0 + 3.0 * a
    u_star = 0.691116422381969
    delta_uv = u_star / c_uv

    c_one = 1.0 + 5.0 * (1.0 + 2.0 * a) / 6.0
    delta_gap = 1.0 / (1.0 + c_one)

    assert abs(inv_lam - (1.0 + 2.0 * a) / (2.0 + a)) < 1e-14
    assert 2.0 * lam - 1.0 > lam
    assert abs(delta_uv - 0.238062349248111) < 5e-13
    assert abs(delta_gap - 0.299845580176277) < 5e-13
    assert delta_uv < delta_gap

    # Finite grid check of
    #   lam*sigma + (2*lam-1)*R <= delta
    #       => sigma + R <= delta/lam.
    checked_budget = 0
    for delta_i in range(1, 101):
        delta = delta_i / 100.0
        for sigma_i in range(0, 101):
            sigma = sigma_i / 100.0
            for r_i in range(0, 101):
                rough = r_i / 100.0
                cost = lam * sigma + (2.0 * lam - 1.0) * rough
                if cost <= delta + 1e-12:
                    assert sigma + rough <= delta * inv_lam + 1e-12
                    checked_budget += 1

    # Exact divisor-assignment reconstruction:
    # V=v1*v2, gamma=t1*t2, b1=v1*t1, b2=v2*t2
    # must give b1*b2=gamma*V.  Conversely the ordered divisor choices
    # determine b1,b2 exactly.
    checked_factorizations = 0
    for V in range(1, 81):
        for gamma in range(1, 81):
            seen: set[tuple[int, int, int, int]] = set()
            for v1 in divisors(V):
                v2 = V // v1
                for t1 in divisors(gamma):
                    t2 = gamma // t1
                    b1 = v1 * t1
                    b2 = v2 * t2
                    assert b1 * b2 == gamma * V
                    key = (v1, t1, b1, b2)
                    assert key not in seen
                    seen.add(key)
                    checked_factorizations += 1

    # Exponent bookkeeping for the global terminal count.
    # For delta < delta_gap:
    #   E(delta) = delta/lambda + max(C_UV*delta-U_*, 0).
    # Below delta_UV the numerator contribution vanishes exactly.
    for k in range(1, 1000):
        delta = delta_gap * k / 1000.0
        exponent = delta * inv_lam + max(c_uv * delta - u_star, 0.0)
        assert exponent >= 0.0
        if delta < delta_uv - 1e-12:
            assert abs(exponent - delta * inv_lam) < 1e-12

    print(f"lambda = {lam:.15f}")
    print(f"1/lambda = {inv_lam:.15f}")
    print(f"delta_UV = {delta_uv:.15f}")
    print(f"delta_gap = {delta_gap:.15f}")
    print(f"checked shared-budget grid points: {checked_budget}")
    print(f"checked divisor assignments: {checked_factorizations}")
    print("DD corrected terminal denominator/S-unit entropy checks passed.")


if __name__ == "__main__":
    main()
