#!/usr/bin/env python3
"""Mechanically check the algebra used in DD Section 27.11.

The script checks symbolic eliminations, exact rational comparison margins, and
the tiny residue list for the top weighted-valuation layer. It is not a proof
of the hypotheses and does not enumerate DD candidates.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    S, m = sp.symbols("S m", integer=True, positive=True)
    VQ, VG, VN = sp.symbols("V_Q V_G V_N", nonnegative=True)
    a = sp.log(2, 10)
    b = 1 - a
    c = sp.log(11, 10)

    m_bound = 3 * S + sp.Rational(3, 2) + a / 2 - VQ - VG / 2 - VN / 2
    n_before_substitution = (
        4 * S
        + sp.Rational(4, 3) * m
        - sp.Rational(2, 3) * VQ
        - VG / 3
        - VN / 3
        + 4
        + a / 3
    )
    weighted_bound = sp.simplify(n_before_substitution.subs(m, m_bound))
    expected_bound = 8 * S + 6 + a - 2 * VQ - VG - VN
    assert sp.simplify(weighted_bound - expected_bound) == 0

    t2_one_m_slope = 6 / (1 + 2 * a)
    t2_one_m_constant = 3 * (1 + c + 2 * a) / (2 * (1 + 2 * a))
    t2_one_n_slope = (10 + 8 * a) / (1 + 2 * a)
    t2_one_n_constant = 5 + 2 * a + b * (1 + c + 2 * a) / (1 + 2 * a)
    other_slope = 2 * (8 + a) / (2 + a)
    other_constant = 2 * (7 + 2 * a) / (2 + a)

    assert 10**3 < 2**10
    assert 2**3 < 10
    assert 11**20 < 10**21
    assert sp.Rational(31, 4) * 4 + sp.Rational(6581, 960) < 8 * 4 + 6
    assert sp.Rational(35, 4) * 3 + sp.Rational(163, 64) < 8 * 3 + 6
    assert sp.Rational(29, 4) + sp.Rational(20, 3) < 8 + 6

    top_kernels: list[tuple[int, int, int, int]] = []
    for exponent_2 in range(5):
        for exponent_5 in range(2):
            xi = 2**exponent_2 * 5**exponent_5
            if xi >= 20 or (exponent_2 - exponent_5 - 1) % 3:
                continue
            for m_mod_3 in range(3):
                if (2 * m_mod_3 + exponent_2 - 1) % 3 == 0 and (
                    2 * m_mod_3 + exponent_5
                ) % 3 == 0:
                    top_kernels.append((exponent_2, exponent_5, m_mod_3, xi))

    assert top_kernels == [(1, 0, 0, 2), (4, 0, 0, 16)]

    print(f"weighted resonance bound = {weighted_bound}")
    print(
        "t2=1 constants =",
        sp.N(t2_one_m_slope, 12),
        sp.N(t2_one_m_constant, 12),
        sp.N(t2_one_n_slope, 12),
        sp.N(t2_one_n_constant, 12),
    )
    print(
        "other-position constants =",
        sp.N(other_slope, 12),
        sp.N(other_constant, 12),
    )
    print(f"top kernels (A2, A5, m mod 3, Xi) = {top_kernels}")
    print("DD 27.11 symbolic checks: OK")


if __name__ == "__main__":
    main()
