#!/usr/bin/env python3
"""Mechanical audits for dd-corrected-carry-u-pairmax-crt-2026-08-22.md.

Checks the carry divisibility, the joint loss/cost optimization, and the
reported uniqueness threshold.  This is not a proof assistant.
"""

from __future__ import annotations

from math import isclose, log10


def check_euclid_carry_small_box(bound: int = 40) -> None:
    # Abstract carry consequence: if gcd(R0,g0)=1 and g0 | Sigma*R0,
    # then g0 | Sigma.  Check a finite box as a sanity audit.
    import math

    states = 0
    for g0 in range(1, bound + 1):
        for R0 in range(1, bound + 1):
            if math.gcd(g0, R0) != 1:
                continue
            for Sigma in range(1, bound + 1):
                if (Sigma * R0) % g0 == 0:
                    assert Sigma % g0 == 0
                    states += 1
    assert states > 0
    print(f"Euclid carry states checked: {states}")


def check_joint_ratios() -> None:
    a = log10(2)
    b = 1 - a
    lam = (2 + a) / (1 + 2 * a)
    A = 2 * (1 + 2 * a) / 3
    c_mu = 2 * b / (3 * A)

    losses = {
        "Q2": 2 * a * (1 - c_mu),
        "Q5": 2 * b / 3 * (1 - c_mu),
        "G5": b / 3 * (7 - 4 * c_mu),
        "N5": b / 3 * (1 - c_mu),
        "R": 3.5 - 2 * c_mu,
    }
    costs = {
        "Q2": 2 * a * lam,
        "Q5": 2 * b * (lam + 1) / 3,
        "G5": 2 * b * (2 * lam - 1) / 3,
        "N5": b * (lam + 1) / 3,
        "R": 2 * lam - 1,
    }
    ratios = {k: losses[k] / costs[k] for k in losses}
    rho = max(ratios.values())

    assert isclose(ratios["G5"], 0.5 + 3 * a, abs_tol=1e-15)
    assert isclose(ratios["R"], 0.5 + 3 * a, abs_tol=1e-15)
    assert all(v <= rho + 1e-15 for v in ratios.values())

    Cuv = 1.5 + rho
    assert isclose(Cuv, 2 + 3 * a, abs_tol=1e-15)
    assert isclose(Cuv, log10(800), abs_tol=1e-15)

    print("joint loss/cost ratios:")
    for k, v in ratios.items():
        print(f"  {k}: {v:.15f}")
    print(f"C_UV: {Cuv:.15f}")


def check_threshold() -> None:
    a = log10(2)
    Ustar = 0.691116422381969
    Cuv = 2 + 3 * a
    delta_uv = Ustar / Cuv
    assert isclose(delta_uv, 0.238062349248111, abs_tol=1e-15)
    assert 1 + Ustar - Cuv * (0.99 * delta_uv) > 1
    assert 1 + Ustar - Cuv * (1.01 * delta_uv) < 1
    print(f"delta_UV: {delta_uv:.15f}")


def main() -> None:
    check_euclid_carry_small_box()
    check_joint_ratios()
    check_threshold()
    print("DD corrected carry-U pairmax CRT audits passed")


if __name__ == "__main__":
    main()
