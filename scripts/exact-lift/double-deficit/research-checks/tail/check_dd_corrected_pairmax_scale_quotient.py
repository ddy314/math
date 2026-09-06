#!/usr/bin/env python3
"""Mechanical audits for dd-corrected-pairmax-scale-quotient-2026-09-06.md."""

from __future__ import annotations

from math import gcd, log10

import sympy as sp


def local_strip() -> None:
    # Two pair-max primes with low baselines r and excess h.
    local = [(13, 2, 3), (17, 1, 2)]  # (p,r,h)
    ell_v = 1
    v2 = 1
    b1 = b2 = b3 = q = gamma = 1
    for p, r, h in local:
        ell_v *= p**r
        v2 *= p**h
        b1 *= p**r
        b2 *= p ** (r + h)
        b3 *= p ** (r + h)
        q *= p**r
        gamma *= p ** (2 * r)

    qv = q // ell_v
    b1v = b1 // ell_v
    b2v = b2 // ell_v
    b3v = b3 // ell_v
    gammav = gamma // (ell_v * ell_v)

    assert gcd(qv, v2) == 1
    assert gcd(b1v, v2) == 1
    assert gcd(gammav, v2) == 1
    assert b2v % v2 == 0
    assert b3v % v2 == 0


def symbolic_qv_lower() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q5, g5, n5, rough, g2 = sp.symbols(
        "Q5 G5 N5 R G2", nonnegative=True
    )

    q_dev = (
        -2 * b * mu / 3
        + a * g2
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
    diff = sp.expand(q_dev - m1)
    target = sp.expand(
        -delta / 2
        + a * mu
        + a * g2
        + b * q5
        + b * n5 / 2
        + rough / 2
    )
    assert sp.simplify(diff - target) == 0


def thresholds() -> None:
    a = log10(2)
    z_star = 0.308883577618031
    kappa_dig = (2 + a) / 3
    delta_head = 1 / (1 + kappa_dig)

    assert z_star - 0.5 / 2 > 0
    assert abs(delta_head - 0.565927754125872) < 1e-12
    assert delta_head > 0.5


def toy_short_head_reader() -> None:
    # Padded-width quotient identity U*qV=b1V*10^m2+b2V, with v2|b2V.
    U = 13
    qv = 2
    v2 = 3
    m2 = 1
    b1v = 2
    b2v = U * qv - b1v * 10**m2

    assert b2v == 6
    assert b2v % v2 == 0
    assert gcd(U * qv, v2) == 1
    assert 0 < b1v < v2

    rho = (U * qv * pow(10, -m2, v2)) % v2
    assert rho == b1v


def main() -> None:
    local_strip()
    symbolic_qv_lower()
    thresholds()
    toy_short_head_reader()
    print("DD corrected pairmax scale quotient audit passed")


if __name__ == "__main__":
    main()
