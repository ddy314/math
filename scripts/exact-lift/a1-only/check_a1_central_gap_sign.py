#!/usr/bin/env python3
"""Symbolic/exact audit for central-gap-sign-collapse.md."""

from __future__ import annotations

import sympy as sp


T, n, s, gamma = sp.symbols("T n s gamma")
SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))

EXPECTED_REMAINING = {
    (1, 1): (32, 34, 36, 38),
    (1, 3): (24, 26, 28, 30, 32, 34, 36, 38),
    (3, 1): (22, 24, 26, 28, 30, 32, 34, 36, 38),
    (1, 2): (30, 32, 38),
    (3, 2): (22, 30, 32, 38),
    (1, 4): (24, 26),
}

PRE_2ADIC = {
    (1, 1): tuple(range(16, 40, 2)),
    (1, 3): tuple(range(16, 40, 2)),
    (3, 1): tuple(range(16, 40, 2)),
    (1, 2): (16, 22, 30, 32, 38),
    (3, 2): (16, 22, 30, 32, 38),
    (1, 4): (24, 26),
}


def symbolic_R(z: int, w: int) -> sp.Expr:
    c = 5 - z
    b1 = 10 * T**2 - w
    a2 = 10 * T**2 - z
    Q = 10 * b1 + 1
    D = T * Q
    a1 = 100 * T**3 + (10 * (c - w) + 1) * T + n - 1
    C = 10 * T**2 * a1 + a2
    N = a1**2 + (a2 * b1) ** 2
    K = b1**2 * C**2 - D**2 * N
    B = n * T - gamma
    return sp.expand(K - 2 * B * Q * N)


def l1_bound_in_s(expr: sp.Expr) -> int:
    poly = sp.Poly(sp.expand(expr), s)
    return sum(abs(int(c)) for c in poly.all_coeffs())


def main() -> None:
    global_remainder_bound = 0
    leading: dict[tuple[int, int], sp.Expr] = {}

    for z, w in SIX_TYPES:
        R = symbolic_R(z, w)
        Rs = sp.Poly(sp.expand(R.subs(n, s * T)), T)
        assert Rs.degree() == 10
        leading[(z, w)] = sp.factor(Rs.LC() / 10000)

        for G in range(16, 40):
            fixed = sp.Poly(sp.expand(Rs.as_expr().subs(gamma, G)), T)
            total = 0
            for j in range(10):
                total += l1_bound_in_s(fixed.coeff_monomial(T**j))
            global_remainder_bound = max(global_remainder_bound, total)

    assert global_remainder_bound == 101_834_561

    expected_leading = {
        (1, 1): s**2 - 280*s + 200*gamma - 5980,
        (1, 2): s**2 - 280*s + 200*gamma - 5180,
        (1, 3): s**2 - 280*s + 200*gamma - 4380,
        (1, 4): s**2 - 280*s + 200*gamma - 3580,
        (3, 1): s**2 - 240*s + 200*gamma - 4340,
        (3, 2): s**2 - 240*s + 200*gamma - 3940,
    }
    for typ in SIX_TYPES:
        assert sp.expand(leading[typ] - expected_leading[typ]) == 0

    for typ, gaps in PRE_2ADIC.items():
        F = leading[typ]
        remaining = []
        killed = []
        for G in gaps:
            # F is decreasing on [0.1,1], so F(0.1)<0 proves uniform negativity.
            endpoint = sp.Rational(1, 10)
            max_F = sp.expand(F.subs({gamma: G, s: endpoint}))
            # At T>=1e6 the remainder/T^10 is <102.
            if 10000 * max_F + 102 < 0:
                killed.append(G)
            else:
                remaining.append(G)

        assert tuple(remaining) == EXPECTED_REMAINING[typ]
        print(f"type={typ} killed={tuple(killed)} remaining={tuple(remaining)}")

    # Crossing case: at s=0.251 the leading negativity already dominates.
    F_cross = leading[(3, 1)].subs(gamma, 22)
    at_251 = sp.expand(F_cross.subs(s, sp.Rational(251, 1000)))
    assert 10000 * at_251 + 102 < 0

    total_remaining = sum(len(v) for v in EXPECTED_REMAINING.values())
    assert total_remaining == 30
    print(f"uniform lower-coefficient L1 bound = {global_remainder_bound}")
    print("central remaining type-gap combinations = 30")
    print("A1 central-gap sign audit OK")


if __name__ == "__main__":
    main()
