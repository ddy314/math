#!/usr/bin/env python3
"""Symbolic audits for dd-corrected-common-scale-ray-sharp-2026-09-06.md.

Checks the fixed-width determinant box and the shared-defect cancellation that
upgrades the common-scale ray to the full corrected one-channel neighborhood.
This is an algebra/constant sanity check, not a proof assistant.
"""

from __future__ import annotations

from math import log10

import sympy as sp


def symbolic_uv_cancellation() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q2, q5, g5, n5, rough = sp.symbols("Q2 Q5 G5 N5 R", nonnegative=True)
    g2 = sp.symbols("G2", nonnegative=True)

    # Uncoarsened log(UV)/(S) - (1+U_*).
    uv_dev = (
        2 * b * mu / 3
        - 2 * a * g2
        - 2 * b * q5 / 3
        - 4 * b * g5 / 3
        - b * n5 / 3
        - 2 * rough
    )

    # Sharp short-denominator upper.
    m1 = (
        delta / 2
        - (1 - b / 3) * mu
        - b * q5 / 3
        + b * g5 / 3
        - b * n5 / 6
        + rough / 2
    )

    # Since a*G2 <= m1+a*Q2 and G2 occurs with negative coefficient,
    # substitute the upper endpoint to obtain the lower bound.
    after_g2 = sp.expand(uv_dev.subs(g2, (m1 + a * q2) / a))
    target = sp.expand(-delta + 2 * mu - 2 * a * q2 - 2 * b * g5 - 3 * rough)
    assert sp.simplify(after_g2 - target) == 0


def numeric_mu_budget_signs() -> None:
    a = log10(2)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    lam = (2 + a) / (1 + 2 * a)
    u_star = 0.691116422381969

    assert abs(2 / A - (2 * lam - 1)) < 1e-12
    assert lam > 1.25
    assert 4 * lam - 5 > 0

    # Positive corrections in UV-sharp-full.
    coeffs = {
        "sigma": 2 * lam - 1,
        "Q2": 4 * a * (lam - 1),
        "N2": a * (2 * lam - 1),
        "Q5": 2 * b * (2 * lam - 1) / 3,
        "G5": 2 * b * (4 * lam - 5) / 3,
        "N5": b * (2 * lam - 1) / 3,
        "R": 4 * lam - 5,
    }
    assert all(value > 0 for value in coeffs.values())

    # Current one-channel theorem assumes delta <= 1/2, safely inside delta<U_*.
    assert 0.5 < u_star


def determinant_box() -> None:
    # Check the elementary fixed-width cross-product box on many small examples.
    for m1 in range(1, 4):
        for m2 in range(1, 4):
            S = m1 + m2
            for v1 in range(1, 8):
                for v2 in range(1, 8):
                    V = v1 * v2
                    # Pick valid positive blocks divisible by v_i.
                    vals1 = [b for b in range(10 ** (m1 - 1), 10**m1) if b % v1 == 0][:4]
                    vals2 = [b for b in range(10 ** (m2 - 1), 10**m2) if b % v2 == 0][:4]
                    for b1 in vals1:
                        for b1p in vals1:
                            for b2 in vals2:
                                for b2p in vals2:
                                    t1, t1p = b1 // v1, b1p // v1
                                    t2, t2p = b2 // v2, b2p // v2
                                    det = t2 * t1p - t2p * t1
                                    assert abs(det) < 2 * 10**S / V


def main() -> None:
    symbolic_uv_cancellation()
    numeric_mu_budget_signs()
    determinant_box()
    print("DD corrected sharp common-scale ray audit passed")


if __name__ == "__main__":
    main()
