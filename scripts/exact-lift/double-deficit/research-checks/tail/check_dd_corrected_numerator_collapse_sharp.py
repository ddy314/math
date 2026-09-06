#!/usr/bin/env python3
"""Symbolic audits for dd-corrected-numerator-collapse-sharp-2026-09-06.md."""

from __future__ import annotations

from math import log10

import sympy as sp


def symbolic_uv2_sharp() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q2, n2, q5, g5, n5, rough, g2 = sp.symbols(
        "Q2 N2 Q5 G5 N5 R G2", nonnegative=True
    )

    u_dev = (
        2 * b * mu / 3
        - a * g2
        - 2 * b * q5 / 3
        - b * g5 / 3
        - b * n5 / 3
        - rough
    )
    v_dev = -a * g2 - b * g5 - rough
    m1 = (
        delta / 2
        - (1 - b / 3) * mu
        - b * q5 / 3
        + b * g5 / 3
        - b * n5 / 6
        + rough / 2
    )

    # log(U v2) - (1+U*) >= u_dev + v_dev - m1.
    expr = sp.expand(u_dev + v_dev - m1)

    # a*G2 <= m1 + a*Q2.
    expr = sp.expand(expr.subs(g2, (m1 + a * q2) / a))
    target = sp.expand(
        -3 * delta / 2
        + (3 - b / 3) * mu
        - 2 * a * q2
        + b * q5 / 3
        - 7 * b * g5 / 3
        + b * n5 / 6
        - 7 * rough / 2
    )
    assert sp.simplify(expr - target) == 0


def budget_coefficients() -> None:
    a = log10(2)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    eta = (3 - b / 3) / A

    assert abs(eta - 2.590736314681693) < 1e-12
    assert eta > 7 / 4

    coeffs = {
        "sigma": eta,
        "Q2": 2 * a * (eta - 1),
        "N2": a * eta,
        "Q5": b * (2 * eta + 1) / 3,
        "G5": b * (4 * eta - 7) / 3,
        "N5": b * (2 * eta + 1) / 6,
        "R": 2 * eta - 7 / 2,
    }
    assert all(value > 0 for value in coeffs.values())


def thresholds() -> None:
    a = log10(2)
    u_star = 0.691116422381969
    z_star = 1 - u_star
    kappa_dig = (2 + a) / 3

    delta_uv = 2 * u_star / 3
    delta_a2 = 1 / (1 + kappa_dig)
    delta_qv = 2 * z_star / 3

    assert abs(delta_uv - 0.460744281587979) < 1e-12
    assert abs(delta_a2 - 0.565927754125872) < 1e-12
    assert abs(delta_qv - 0.205922385078687) < 1e-12

    assert delta_qv < delta_uv < 0.5 < delta_a2

    # gap determinant: v2 height 1-delta beats delta-height determinant iff delta<1/2.
    for delta in (0.0, 0.1, 0.3, 0.49):
        assert 1 - delta > delta
    assert not (1 - 0.5 > 0.5)


def main() -> None:
    symbolic_uv2_sharp()
    budget_coefficients()
    thresholds()
    print("DD corrected sharp numerator collapse audit passed")


if __name__ == "__main__":
    main()
