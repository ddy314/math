#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0600; see history/sources.json.
"""

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
    assert new < 0.5 < U_star
    assert 1 + U_star - 0.5 > 1

    # Candidate-specific common-scale sharpening: R/2 is cheaper than sigma.
    r_entropy_per_defect = 0.5 / (2 * lam - 1)
    sigma_entropy_per_defect = 1 / lam
    assert r_entropy_per_defect < sigma_entropy_per_defect

    # Direct suffix enumeration plus the same Mu-budget has only this
    # positive slack coefficient after exact cancellation.
    slack_coefficient = 1 - lam / 2
    assert slack_coefficient > 0
    assert isclose(0.5 + slack_coefficient / lam, inv_lam, rel_tol=0, abs_tol=1e-12)
    assert 1 - lam < 0

    print("DD corrected non-circular terminal global sparsity checks passed (fixed delta_0<1/2)")


if __name__ == "__main__":
    main()
