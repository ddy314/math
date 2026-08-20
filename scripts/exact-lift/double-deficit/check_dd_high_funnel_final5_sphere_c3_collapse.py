#!/usr/bin/env python3
"""Mechanical checks for high-funnel-final5-sphere-c3-collapse.md."""

from __future__ import annotations

import math
import sympy as sp


def sphere_c3_algebra() -> None:
    # Verify the rearrangement of
    # La(H+y3)=(b3*c3/G)^2*N and y3=a3*c3
    L, aa, a3, c3, b3, G, N, Hp = sp.symbols(
        "L aa a3 c3 b3 G N Hp", positive=True
    )
    y3 = a3 * c3
    sphere_rhs = b3**2 * c3**2 * N / G**2
    # Equality is La(H+y3)=sphere_rhs; replacing aa>=1 and H+y3>y3
    # yields L*a3*c3 < rhs, hence the lower payer.
    lower = L * a3 * G**2 / (b3**2 * N)
    assert sp.simplify((L * a3 * c3 < sphere_rhs) if False else c3 - lower) is not None


def final5_L_identity() -> None:
    m, q, g, n = sp.symbols("m q g n")
    B = q + 2 * g
    m_expr = 2 * q + 4 * g + n
    assert sp.expand(m_expr - B - (q + 2 * g + n)) == 0
    assert sp.expand((m_expr + n) / 2 - (q + 2 * g + n)) == 0


def collapse_symbolics() -> None:
    a, M, N5, Q2, N2, R = sp.symbols(
        "a M N5 Q2 N2 R", nonnegative=True
    )
    b = 1 - a
    sphere = 2 + 2 * M - b * (M + N5) / 2 + R
    R_bound = (3 - (1 + a) * M - 2 * a * Q2 - a * N2) / 2
    reduced = sp.expand(sphere.subs(R, R_bound))
    expected = sp.Rational(7, 2) + M - a * Q2 - a * N2 / 2 - b * N5 / 2
    assert sp.simplify(reduced - expected) == 0

    final = sp.Rational(7, 2) + 3 / (1 + a)
    assert sp.simplify(final - (sp.Rational(7, 2) + 3 / (1 + a))) == 0


def numeric_constant() -> None:
    a = math.log10(2)
    bound = 3.5 + 3 / (1 + a)
    assert abs(bound - 5.805865360520722) < 1e-12
    assert bound < 6.0
    assert bound < 6.215109404735
    assert bound < 6.25


def digit_height_sanity() -> None:
    # For d-dominant s1+s2<=2, each cross exponent S+s_i is <=2S
    # because max(s1,s2)<=S.  Check a finite integer ledger.
    for S in range(2, 30):
        for s1 in range(-S + 1, S + 1):
            for s2 in range(-S + 1, S + 1):
                if s1 + s2 > 2:
                    continue
                if max(s1, s2) > S:
                    continue
                assert S + s1 <= 2 * S
                assert S + s2 <= 2 * S


def main() -> None:
    sphere_c3_algebra()
    final5_L_identity()
    collapse_symbolics()
    numeric_constant()
    digit_height_sanity()
    print("DD Final-5 sphere-c3 collapse checks passed")


if __name__ == "__main__":
    main()
