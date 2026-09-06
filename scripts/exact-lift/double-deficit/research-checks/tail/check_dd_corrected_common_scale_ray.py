#!/usr/bin/env python3
"""Mechanical audits for dd-corrected-common-scale-ray-2026-09-06.md.

Checks the explicit projective-lock constant, the determinant identity behind
cofactor ratio uniqueness, the primitive-ray/common-scale reconstruction, and
homogeneity under a common denominator scale.  This is an algebra/constant
sanity check, not a proof assistant for the asymptotic DD hypotheses.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, log10, sqrt


def constants() -> None:
    a = log10(2)
    u_star = 0.691116422381969
    kappa_dig = (2 + a) / 3
    c_one = 1 + 5 * (1 + 2 * a) / 6
    denom = (1 + a) + kappa_dig + c_one
    delta_ray = u_star / denom
    delta_qz = 0.075150109396892

    assert abs(kappa_dig - 0.767009998554660) < 1e-12
    assert abs(c_one - 2.335049992773302) < 1e-12
    assert abs(kappa_dig + c_one - 3.102059991327962) < 1e-12
    assert abs(denom - 4.403089986991944) < 1e-12
    assert abs(delta_ray - 0.156961684731344) < 1e-12
    assert delta_qz < delta_ray

    # At the threshold, the U lower exponent and determinant upper exponent meet.
    lhs = u_star - (1 + a) * delta_ray
    rhs = (kappa_dig + c_one) * delta_ray
    assert abs(lhs - rhs) < 1e-12


def determinant_identity() -> None:
    # Toy fixed phase/factor fiber:
    # U=133, V=v1*v2=33, m2=2.  Then
    #   v1*10^m2*tau1 + v2*tau2 == 0 (mod U)
    # becomes 100*tau1 + 33*tau2 == 0 (mod 133), i.e.
    # tau2 == tau1 (mod 133).  Inside a short box this leaves one ray.
    U = 133
    v1 = 1
    v2 = 33
    m2 = 2
    assert gcd(U, v1 * v2 * 10) == 1

    solutions: list[tuple[int, int]] = []
    for tau1 in range(1, 20):
        for tau2 in range(1, 20):
            if (v1 * 10**m2 * tau1 + v2 * tau2) % U == 0:
                solutions.append((tau1, tau2))

    assert solutions
    assert all(t1 == t2 for t1, t2 in solutions)

    for t1, t2 in solutions:
        for s1, s2 in solutions:
            determinant = t2 * s1 - s2 * t1
            assert determinant % U == 0
            assert determinant == 0


def common_scale_reconstruction() -> None:
    U = 133
    v1 = 1
    v2 = 33
    V = v1 * v2
    m2 = 2
    r = 1
    s = 1
    B = 1

    D = v1 * r * 10**m2 + v2 * s
    g = gcd(U, D)
    U0 = U // g
    D0 = D // g

    assert D == 133
    assert g == 133
    assert U0 == D0 == 1

    bar_b1 = v1 * U0 * r
    bar_b2 = v2 * U0 * s
    bar_q = D0
    bar_b3 = B * V * D0
    bar_gamma = U0**2 * r * s

    for ell in range(1, 10):
        tau1 = U0 * ell * r
        tau2 = U0 * ell * s
        q = D0 * ell
        b1 = v1 * tau1
        b2 = v2 * tau2
        b3 = B * V * q
        gamma = tau1 * tau2
        Q = b1 * 10**m2 + b2

        assert Q == U * q
        assert b1 == ell * bar_b1
        assert b2 == ell * bar_b2
        assert b3 == ell * bar_b3
        assert q == ell * bar_q
        assert gamma == ell**2 * bar_gamma
        assert b1 * b2 == gamma * V


def scale_homogeneity() -> None:
    # Keep the original padded denominator widths fixed.  The algebraic equality
    # scales by 1/ell even when the unscaled bar blocks would have leading zeros.
    m2 = 2
    m3 = 2
    bar_b1, bar_b2, bar_b3 = 1, 33, 33
    a1, a2, a3 = 1, 2, 3

    # Numerator blocks are all one digit here, so alpha=123.
    alpha = 123
    beta_bar = bar_b1 * 10 ** (m2 + m3) + bar_b2 * 10**m3 + bar_b3

    base_lhs = Fraction(alpha, beta_bar)
    base_norm_sq = sum(
        Fraction(a * a, b * b)
        for a, b in ((a1, bar_b1), (a2, bar_b2), (a3, bar_b3))
    )

    for ell in (2, 3, 7):
        b1, b2, b3 = ell * bar_b1, ell * bar_b2, ell * bar_b3
        beta = b1 * 10 ** (m2 + m3) + b2 * 10**m3 + b3
        lhs = Fraction(alpha, beta)
        norm_sq = sum(
            Fraction(a * a, b * b)
            for a, b in ((a1, b1), (a2, b2), (a3, b3))
        )

        assert beta == ell * beta_bar
        assert lhs == base_lhs / ell
        assert norm_sq == base_norm_sq / (ell * ell)
        # Floating sqrt is only used as a final sanity check of the same scaling.
        assert abs(sqrt(float(norm_sq)) - sqrt(float(base_norm_sq)) / ell) < 1e-15


def main() -> None:
    constants()
    determinant_identity()
    common_scale_reconstruction()
    scale_homogeneity()
    print("DD corrected common-scale ray audit passed")


if __name__ == "__main__":
    main()
