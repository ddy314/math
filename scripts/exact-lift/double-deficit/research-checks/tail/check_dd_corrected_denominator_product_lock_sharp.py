#!/usr/bin/env python3
"""Symbolic audits for dd-corrected-denominator-product-lock-sharp-2026-09-06.md.

This script checks the no-double-count cancellations and constants in the sharp
qZ/v2 comparison.  It does not certify the asymptotic hypotheses themselves.
"""

from __future__ import annotations

from math import log10

import sympy as sp


def symbolic_qz_cancellation() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q2, n2, q5, g5, n5, rough = sp.symbols(
        "Q2 N2 Q5 G5 N5 R", nonnegative=True
    )
    g2 = sp.symbols("G2", nonnegative=True)

    # Uncoarsened q and Z deviations from z_*.
    q_dev = (
        -2 * b * mu / 3
        + a * g2
        + 2 * b * q5 / 3
        + b * g5 / 3
        + b * n5 / 3
        + rough
    )
    z_dev = 2 * a * mu - 2 * a * q2 - a * n2 + a * g2 - b * g5 - rough
    qz_dev = sp.expand(q_dev + z_dev)

    # Sharp m1 upper from the uncoarsened digit-polarization inequality.
    m1 = (
        delta / 2
        - (1 - b / 3) * mu
        - b * q5 / 3
        + b * g5 / 3
        - b * n5 / 6
        + rough / 2
    )

    # a*G2 <= m1 + a*Q2.  Substitute the upper endpoint; all the advertised
    # Q2/Q5/G5/N5 terms must cancel.
    qz_after_g2 = sp.expand(qz_dev.subs(g2, (m1 + a * q2) / a))
    target = sp.expand(delta - 2 * b * mu + rough - a * n2)
    assert sp.simplify(qz_after_g2 - target) == 0


def symbolic_v2_cancellation() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q2, q5, g5, n5, rough = sp.symbols("Q2 Q5 G5 N5 R", nonnegative=True)

    m1 = (
        delta / 2
        - (1 - b / 3) * mu
        - b * q5 / 3
        + b * g5 / 3
        - b * n5 / 6
        + rough / 2
    )

    # 1-log(v2)/S <= 2*m1 + a*Q2 + b*G5 + R.
    loss = sp.expand(2 * m1 + a * q2 + b * g5 + rough)
    target = sp.expand(
        delta
        - 2 * (1 - b / 3) * mu
        + a * q2
        - 2 * b * q5 / 3
        + 5 * b * g5 / 3
        - b * n5 / 3
        + 2 * rough
    )
    assert sp.simplify(loss - target) == 0

    A = 2 * (1 + 2 * a) / 3
    lam = (2 + a) / (1 + 2 * a)
    assert sp.simplify(2 * (1 - b / 3) - lam * A) == 0


def numeric_signs_and_thresholds() -> None:
    a = log10(2)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    lam = (2 + a) / (1 + 2 * a)
    z_star = 0.308883577618031
    theta = 2 * b / A

    assert abs(theta - 1.308883577618031) < 1e-12
    assert theta > 0.5
    assert lam > 1.25
    assert 4 * lam - 5 > 0

    # qZ-sharp-full correction magnitudes: every displayed term after delta
    # is subtracted, so these must be positive.
    qz_coeffs = {
        "sigma": theta,
        "Q2": 2 * a * theta,
        "N2": a * (theta + 1),
        "Q5": 2 * b * theta / 3,
        "G5": 4 * b * theta / 3,
        "N5": b * theta / 3,
        "R": 2 * theta - 1,
    }
    assert all(value > 0 for value in qz_coeffs.values())

    # v2-sharp-full correction magnitudes: every term after 1-delta is added.
    v2_coeffs = {
        "sigma": lam,
        "Q2": a * (2 * lam - 1),
        "N2": a * lam,
        "Q5": 2 * b * (lam + 1) / 3,
        "G5": b * (4 * lam - 5) / 3,
        "N5": b * (lam + 1) / 3,
        "R": 2 * (lam - 1),
    }
    assert all(value > 0 for value in v2_coeffs.values())

    delta_sharp = 0.5 - z_star
    delta_ray = 0.156961684731344
    delta_uv = 0.238062349248111
    old_delta_qz = 0.075150109396892

    assert abs(delta_sharp - 0.191116422381969) < 1e-12
    assert old_delta_qz < delta_ray < delta_sharp < delta_uv

    # At the sharp threshold the baseline exponents meet.
    qz_exp = 2 * z_star + delta_sharp
    v2_exp = 1 - delta_sharp
    assert abs(qz_exp - v2_exp) < 1e-12


def main() -> None:
    symbolic_qz_cancellation()
    symbolic_v2_cancellation()
    numeric_signs_and_thresholds()
    print("DD corrected sharp denominator qZ product-lock audit passed")


if __name__ == "__main__":
    main()
