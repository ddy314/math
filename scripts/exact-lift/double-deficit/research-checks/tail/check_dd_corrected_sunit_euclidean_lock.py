#!/usr/bin/env python3
"""Symbolic and finite audits for dd-corrected-sunit-euclidean-lock-2026-09-06.md.

Checks the shared-defect cancellations behind Z,V < 5^T, the U/Z separation,
and exact Euclidean/least-residue reconstruction on toy S-unit examples.
This does not certify the asymptotic hypotheses.
"""

from __future__ import annotations

from math import gcd, log10

import sympy as sp


def symbolic_five_over_z() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q2, n2, q5, g5, n5, rough, g2 = sp.symbols(
        "Q2 N2 Q5 G5 N5 R G2", nonnegative=True
    )

    # Deviation of log(5^T/Z)/S from baseline 1.
    expr = (
        -(2 * b / 3 + 2 * a) * mu
        + 2 * a * q2
        + a * n2
        - a * g2
        + 2 * b * q5 / 3
        + b * g5 / 3
        + b * n5 / 3
        + rough
    )
    m1 = (
        delta / 2
        - (1 - b / 3) * mu
        - b * q5 / 3
        + b * g5 / 3
        - b * n5 / 6
        + rough / 2
    )
    # -aG2 >= -m1-aQ2.
    after = sp.expand(expr.subs(g2, (m1 + a * q2) / a))
    target = sp.expand(
        -delta / 2
        - a * mu
        + a * q2
        + a * n2
        + b * q5
        + b * n5 / 2
        + rough / 2
    )
    assert sp.simplify(after - target) == 0


def five_over_z_loss_ratios() -> None:
    a = log10(2)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    lam = (2 + a) / (1 + 2 * a)

    defect_cost = {
        "sigma": lam,
        "G5": 2 * b * (2 * lam - 1) / 3,
        "R": 2 * lam - 1,
    }
    losses = {
        "sigma": a / A,
        "G5": 4 * a * b / (3 * A),
        "R": max(2 * a / A - 0.5, 0.0),
    }
    ratios = {key: losses[key] / defect_cost[key] for key in losses}

    assert abs(ratios["sigma"] - 0.196236030971719) < 1e-12
    assert abs(ratios["G5"] - a) < 1e-12
    assert abs(ratios["R"] - 0.034019997109321) < 1e-12
    assert max(ratios.values()) == ratios["G5"]

    coeff = 0.5 + a
    assert abs(coeff - 0.801029995663981) < 1e-12
    assert 1 - coeff * 0.5 > 0


def five_over_v_margin() -> None:
    a = log10(2)
    b = 1 - a
    z_star = 0.308883577618031
    margin = z_star - b / 3
    assert abs(margin - 0.075893579064050) < 1e-12
    assert margin > 0


def symbolic_u_over_z() -> None:
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
    z_dev = 2 * a * mu - 2 * a * q2 - a * n2 + a * g2 - b * g5 - rough
    expr = sp.expand(u_dev - z_dev)
    m1 = (
        delta / 2
        - (1 - b / 3) * mu
        - b * q5 / 3
        + b * g5 / 3
        - b * n5 / 6
        + rough / 2
    )
    # -2aG2 >= -2m1-2aQ2.
    after = sp.expand(expr.subs(g2, (m1 + a * q2) / a))
    target = sp.expand(-delta + 2 * b * mu + a * n2 - rough)
    assert sp.simplify(after - target) == 0

    # After Mu-budget, 2b*mu-R has only nonnegative residual coefficients.
    A = 2 * (1 + 2 * a) / 3
    theta = sp.simplify(2 * b / A)
    assert float(theta.subs(a, log10(2))) > 0.5


def euclidean_toys() -> None:
    # Full one-channel-style Euclidean remainder example: Z,V < 5^T.
    H, T, U, Z, V = 4, 2, 7, 11, 1
    modulus = 5**T
    value = 2**H * Z
    assert gcd(U * V * Z, 10) == 1
    assert value == modulus * U + V
    assert 0 < Z < modulus and 0 < V < modulus
    assert value // modulus == U
    assert value % modulus == V
    rho5 = (pow(2**H, -1, modulus) * V) % modulus
    assert rho5 == Z

    # A second example also lies in Z<U, verifying the modulo-U reader.
    H, T, U, Z, V = 5, 2, 11, 9, 13
    modulus = 5**T
    value = 2**H * Z
    assert gcd(U * V * Z, 10) == 1
    assert gcd(U, Z) == gcd(U, V) == gcd(V, Z) == 1
    assert value == modulus * U + V
    assert 0 < Z < U and 0 < V < modulus
    rho5 = (pow(2**H, -1, modulus) * V) % modulus
    rhou = (pow(2**H, -1, U) * V) % U
    assert rho5 == Z
    assert rhou == Z


def constants() -> None:
    z_star = 0.308883577618031
    gap = 1 - 2 * z_star
    assert abs(gap - 0.382232844763938) < 1e-12

    a = log10(2)
    b = 1 - a
    m_star = 2.808883577618031
    t5_star = 2 * b * m_star / 3
    assert abs(t5_star - (1 + z_star)) < 1e-12


def main() -> None:
    symbolic_five_over_z()
    five_over_z_loss_ratios()
    five_over_v_margin()
    symbolic_u_over_z()
    euclidean_toys()
    constants()
    print("DD corrected S-unit Euclidean lock audit passed")


if __name__ == "__main__":
    main()
