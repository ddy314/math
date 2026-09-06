#!/usr/bin/env python3
"""Symbolic audits for dd-corrected-source-quotient-lock-sharp-2026-09-06.md."""

from __future__ import annotations

from math import gcd, log10

import sympy as sp


def symbolic_v2_over_q() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q2, q5, g5, n5, rough, g2 = sp.symbols("Q2 Q5 G5 N5 R G2", nonnegative=True)

    m1 = (
        delta / 2
        - (1 - b / 3) * mu
        - b * q5 / 3
        + b * g5 / 3
        - b * n5 / 6
        + rough / 2
    )
    q_dev = (
        -2 * b * mu / 3
        + a * g2
        + 2 * b * q5 / 3
        + b * g5 / 3
        + b * n5 / 3
        + rough
    )
    v2_dev = -a * g2 - b * g5 - rough - m1
    diff = sp.expand(v2_dev - q_dev)

    # -2aG2 >= -2m1-2aQ2.
    after = sp.expand(diff.subs(g2, (m1 + a * q2) / a))
    target = sp.expand(
        -3 * delta / 2
        + (3 - b / 3) * mu
        - 2 * a * q2
        + b * q5 / 3
        - 7 * b * g5 / 3
        + b * n5 / 6
        - 7 * rough / 2
    )
    assert sp.simplify(after - target) == 0


def numeric_coefficients() -> None:
    a = log10(2)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    eta = (3 - b / 3) / A
    u_star = 0.691116422381969

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

    delta_q = 2 * u_star / 3
    delta_uv = 0.238062349248111
    assert abs(delta_q - 0.460744281587979) < 1e-12
    assert delta_uv < delta_q < 0.5


def toy_source_lock() -> None:
    # Decimal-valid toy:
    #   Q=26=2*10+6=13*2,
    #   m2=1 and b2=6 really is a one-digit block,
    #   v2=3 divides b2, gcd(U,v2)=1, and 0<q<v2.
    m2 = 1
    b1 = 2
    b2 = 6
    U = 13
    q = 2
    v2 = 3
    Q = b1 * 10**m2 + b2

    assert 10 ** (m2 - 1) <= b2 < 10**m2
    assert Q == 26 == U * q
    assert b2 % v2 == 0
    assert gcd(U, v2) == 1
    assert 0 < q < v2

    rho = (pow(U, -1, v2) * b1 * 10**m2) % v2
    assert rho == q


def main() -> None:
    symbolic_v2_over_q()
    numeric_coefficients()
    toy_source_lock()
    print("DD corrected direct source quotient lock audit passed")


if __name__ == "__main__":
    main()
