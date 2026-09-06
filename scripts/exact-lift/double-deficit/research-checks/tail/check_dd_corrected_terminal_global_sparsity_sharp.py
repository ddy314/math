#!/usr/bin/env python3
"""Mechanical constants audit for terminal-global-sparsity-sharp."""

from __future__ import annotations

from math import isclose, log10


def main() -> None:
    a = log10(2)
    lam = (2 + a) / (1 + 2 * a)
    inv_lam = 1 / lam
    U_star = 0.691116422381969
    old = 0.238062349248111
    new = 2 * U_star / 3
    factor = new / old

    assert isclose(lam, 1.436294525872677, rel_tol=0, abs_tol=1e-12)
    assert isclose(inv_lam, 0.696236030971719, rel_tol=0, abs_tol=1e-12)
    assert isclose(new, 0.460744281587979, rel_tol=0, abs_tol=1e-12)
    assert isclose(factor, 1.93539332466129, rel_tol=0, abs_tol=1e-12)
    assert new > old

    # Candidate-specific common-scale sharpening: R/2 is cheaper than sigma.
    r_entropy_per_defect = 0.5 / (2 * lam - 1)
    sigma_entropy_per_defect = 1 / lam
    assert r_entropy_per_defect < sigma_entropy_per_defect

    print("DD corrected terminal global sparsity sharp checks passed")


if __name__ == "__main__":
    main()
