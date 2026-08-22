#!/usr/bin/env python3
"""Finite audit for DD pair-max gap-fiber rational reconstruction.

The bounded search checks the elementary modular Farey lemma used in
`dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md`.
It is only a consistency audit; the asymptotic proof is in the document.
"""

from __future__ import annotations

from math import gcd, log10


def check_constants() -> None:
    a = log10(2)
    c_one = 1 + 5 * (1 + 2 * a) / 6
    delta_gap = 1 / (1 + c_one)
    delta_gap_closed = 6 / (17 + 10 * a)

    kappa_dig = (2 + a) / 3
    delta_a2 = 1 / (c_one + kappa_dig)

    u_star = 0.691116422381969
    c_uv = 2 + 3 * a
    delta_uv = u_star / c_uv

    assert abs(delta_gap - delta_gap_closed) < 1e-15
    assert abs(delta_gap - 0.29984558017627727) < 1e-14
    assert abs(delta_a2 - 0.322366428371977) < 1e-12
    assert abs(delta_uv - 0.238062349248111) < 1e-12
    assert delta_uv < delta_gap < delta_a2

    # At delta_gap the exponents meet exactly:
    # 1 - C_one*delta = delta.
    assert abs((1 - c_one * delta_gap) - delta_gap) < 1e-14


def reduced_pairs(r_cap: int, g_cap: int):
    for r in range(1, r_cap + 1):
        for g in range(1, g_cap + 1):
            if gcd(r, g) == 1:
                yield r, g


def check_farey_model(max_cap: int = 8) -> int:
    """Check uniqueness once modulus exceeds the determinant box.

    For fixed A,K modulo M with K invertible, all reduced positive pairs
    satisfying K*R == A*g (mod M) lie on one modular projective line.
    If M > 2*R_cap*g_cap there can be at most one such pair, because the
    determinant of two candidate pairs is a nonzero multiple of M but has
    absolute value at most 2*R_cap*g_cap.
    """

    rows = 0
    for r_cap in range(1, max_cap + 1):
        for g_cap in range(1, max_cap + 1):
            modulus = 2 * r_cap * g_cap + 1
            pairs = list(reduced_pairs(r_cap, g_cap))

            for k in range(1, modulus):
                if gcd(k, modulus) != 1:
                    continue
                for a in range(modulus):
                    hits = [
                        (r, g)
                        for r, g in pairs
                        if (k * r - a * g) % modulus == 0
                    ]
                    assert len(hits) <= 1
                    rows += 1
    return rows


def check_entropy_bookkeeping() -> None:
    a = log10(2)
    u_star = 0.691116422381969
    c_uv = 2 + 3 * a
    delta_uv = u_star / c_uv

    def exponent(delta: float) -> float:
        return max(c_uv * delta - u_star, 0.0)

    assert exponent(delta_uv * 0.9) == 0.0
    assert abs(exponent(delta_uv)) < 1e-14
    assert exponent(delta_uv * 1.1) > 0.0


def main() -> None:
    check_constants()
    rows = check_farey_model()
    check_entropy_bookkeeping()
    print(
        "DD gap-fiber pairmax rational reconstruction audit passed "
        f"({rows} bounded modular lines)"
    )


if __name__ == "__main__":
    main()
