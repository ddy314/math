#!/usr/bin/env python3
"""Mechanical checks for dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md."""

from __future__ import annotations

from math import log10, isclose


def check_constants() -> None:
    a = log10(2)
    lam = (2 + a) / (1 + 2 * a)
    kappa_dig = (2 + a) / 3
    c_one = 2.335049992773302
    c_ent = 1 + kappa_dig + c_one

    assert 2 * lam - 1 > 1
    assert isclose(kappa_dig, 0.767009998554660, rel_tol=0, abs_tol=1e-15)
    assert isclose(c_ent, 4.102059991327962, rel_tol=0, abs_tol=1e-15)

    print(f"2 lambda - 1 = {2*lam-1:.15f}")
    print(f"kappa_dig     = {kappa_dig:.15f}")
    print(f"C_ent         = {c_ent:.15f}")


def check_joint_gap_overlap_budget() -> None:
    # If P + c_R R <= delta and c_R>1, then P+R<=delta.
    a = log10(2)
    lam = (2 + a) / (1 + 2 * a)
    c_R = 2 * lam - 1

    for p_int in range(101):
        P = p_int / 100
        for r_int in range(101):
            R = r_int / 100
            cost = P + c_R * R
            if cost <= 1 + 1e-12:
                assert P + R <= 1 + 1e-12


def main() -> None:
    check_constants()
    check_joint_gap_overlap_budget()
    print("DD corrected gap-fiber entropy audits passed")


if __name__ == "__main__":
    main()
