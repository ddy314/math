#!/usr/bin/env python3
"""Mechanical audits for dd-corrected-neighborhood-square-source-crt-2026-08-22.md.

This script checks only algebraic identities, local exponent inequalities and the
reported linear-program cost ratios.  It is not a proof assistant and does not
certify the asymptotic hypotheses of the DD argument.
"""

from __future__ import annotations

from math import ceil, log10
from sympy import simplify, symbols


def check_sphere_source_identity() -> None:
    B, V, q, ghat, N = symbols("B V q ghat N", nonzero=True)
    b3 = B * V * q
    gstar = V * ghat
    rhs_original = (b3 / gstar) ** 2 * N
    rhs_new = B**2 * q**2 * N / ghat**2
    assert simplify(rhs_original - rhs_new) == 0


def check_generic_q_parent() -> None:
    w, L, v, omega, A12, D10 = symbols("w L v omega A12 D10")
    a3, Q1, a0, eps = symbols("a3 Q1 a0 eps")

    # Existing overlap identities:
    #   w*a0 = v*omega*A12*10^d - a3*Q1
    #   eps*w = L*Q1 + v
    # and (H+y3)/c = L*a0 + 2*a3*eps.
    parent_from_sphere = w * (L * a0 + 2 * a3 * eps)
    parent_expected = L * v * omega * A12 * D10 + a3 * (L * Q1 + 2 * v)

    substituted = simplify(
        parent_from_sphere.subs(
            {
                w * a0: v * omega * A12 * D10 - a3 * Q1,
                eps * w: L * Q1 + v,
            }
        )
    )
    assert simplify(substituted - parent_expected) == 0


def check_local_square_reader(bound: int = 12) -> None:
    checked = 0
    for s in range(bound + 1):
        for h in range(bound + 1):
            for gap in range(bound + 1):
                for n in range(bound + 1):
                    hplus = 2 * s + n - 2 * h - gap
                    if hplus < 0:
                        continue
                    for c in range(min(h, bound) + 1):
                        f = max(s - h - ceil(gap / 2) - ceil(c / 2), 0)
                        assert 2 * f <= hplus - c
                        checked += 1
    assert checked > 0
    print(f"local square-reader states checked: {checked}")


def check_pairmax_transversality(bound: int = 20) -> None:
    # Pair-max pattern: low exponent r, shared maximum E>r.
    # Source q gets r; normalized overlap ghat gets 2r.
    checked = 0
    for r in range(bound + 1):
        for E in range(r + 1, bound + 2):
            s = r
            h = 2 * r
            for gap in range(bound + 1):
                for c in range(bound + 1):
                    f = max(s - h - ceil(gap / 2) - ceil(c / 2), 0)
                    assert f == 0
                    checked += 1
    print(f"pair-max transverse states checked: {checked}")


def check_defect_cost_ratios() -> None:
    a = log10(2)
    b = 1 - a
    lam = (2 + a) / (1 + 2 * a)
    A = 2 * (1 + 2 * a) / 3

    # L_Q = (2b/3) mu + a Q2 + (b/3) Q5 + R + P_gap.
    # Substitute A*mu by the exact Schmidt-slack ledger.
    k = (2 * b / 3) / A
    loss = {
        "sigma": k,
        "Q2": k * 2 * a + a,
        "N2": k * a,
        "Q5": k * (2 * b / 3) + b / 3,
        "G5": k * (4 * b / 3),
        "N5": k * (b / 3),
        "R": 2 * k + 1,
        "Pgap": 1.0,
    }
    cost = {
        "sigma": lam,
        "Q2": 2 * a * lam,
        "N2": a * lam,
        "Q5": 2 * b * (lam + 1) / 3,
        "G5": 2 * b * (2 * lam - 1) / 3,
        "N5": b * (lam + 1) / 3,
        "R": 2 * lam - 1,
        "Pgap": 1.0,
    }
    ratios = {name: loss[name] / cost[name] for name in loss}
    assert max(ratios.values()) <= 1 + 1e-12
    assert abs(ratios["R"] - 1) < 1e-12
    assert abs(ratios["Pgap"] - 1) < 1e-12

    reported = {
        "sigma": 0.3037639690,
        "Q2": 0.6518819845,
        "N2": 0.3037639690,
        "Q5": 0.3843108934,
        "G5": 0.4659800029,
        "N5": 0.1790811912,
        "R": 1.0,
        "Pgap": 1.0,
    }
    for name, value in reported.items():
        assert abs(ratios[name] - value) < 2e-10

    zstar = 0.308883577618031
    c_one = 2.335049992773302
    threshold = 2 * zstar / (2 + c_one)
    assert abs(threshold - 0.1425051974639056) < 1e-12

    print("defect cost ratios:")
    for name in ratios:
        print(f"  {name:>6}: {ratios[name]:.12f}")
    print(f"source-square x pair-max capacity threshold: {threshold:.15f}")


def main() -> None:
    check_sphere_source_identity()
    check_generic_q_parent()
    check_local_square_reader()
    check_pairmax_transversality()
    check_defect_cost_ratios()
    print("DD corrected neighborhood square-source CRT audits passed")


if __name__ == "__main__":
    main()
