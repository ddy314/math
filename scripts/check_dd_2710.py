#!/usr/bin/env python3
"""Mechanically check the algebra used in DD Section 27.10.

This script verifies symbolic eliminations and the two monotone height margins.
It does not prove the hypotheses that feed those identities and is not a finite
certificate for the DD branch.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    k, M, g = sp.symbols("k M g", integer=True)
    u = 2 * k - M - g
    B = M + g - k

    c_if_nonpositive = sp.simplify(g - u - B)
    c_if_positive = sp.simplify(g + u - B)
    f_minus_if_positive = sp.simplify(g + 2 * u - c_if_positive)

    assert c_if_nonpositive == g - k
    assert c_if_positive == 3 * k - 2 * M - g
    assert f_minus_if_positive == k

    S = sp.symbols("S", integer=True, positive=True)
    L5 = sp.log(10) / sp.log(5)
    entrance = (5 + 2 * L5) * S + L5
    kappa_depth_cap = (2 * S + 1) * L5
    equal_case_cap = 2 * L5 * S + sp.log(11) / sp.log(5)

    strict_margin = sp.simplify(entrance - kappa_depth_cap)
    equal_margin_at_two = sp.N((entrance - equal_case_cap).subs(S, 2), 16)

    assert strict_margin == 5 * S
    assert equal_margin_at_two > 0

    print(f"c(u<=0) = {c_if_nonpositive}")
    print(f"c(u>0) = {c_if_positive}")
    print(f"v5(F_-) for u>0 = {f_minus_if_positive}")
    print(f"entrance - kappa depth cap = {strict_margin}")
    print(f"equal-case margin at S=2 = {equal_margin_at_two}")
    print("DD 27.10 symbolic checks: OK")


if __name__ == "__main__":
    main()
