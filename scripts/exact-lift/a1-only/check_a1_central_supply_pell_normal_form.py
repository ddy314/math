#!/usr/bin/env python3
"""Exact symbolic audit for central-supply-pell-normal-form.md.

No factorization or fixed-k search is performed.  The script verifies the
Euclidean-descent identity, the quadratic discriminant, and the k-independent
U window for all 30 surviving central type-gap combinations.
"""

from __future__ import annotations

from fractions import Fraction as F

import sympy as sp


CENTRAL = {
    (1, 1): (32, 34, 36, 38),
    (1, 3): (24, 26, 28, 30, 32, 34, 36, 38),
    (3, 1): (22, 24, 26, 28, 30, 32, 34, 36, 38),
    (1, 2): (30, 32, 38),
    (3, 2): (22, 30, 32, 38),
    (1, 4): (24, 26),
}


def v(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def c_gamma(gamma: int) -> int:
    return 2 ** v(gamma, 2) * 5 ** v(gamma, 5)


def symbolic_audit() -> None:
    N, L, c, r, w, U = sp.symbols("N L c r w U")
    C0 = w * (10 * w - 1)

    # The claimed quadratic normal form.
    quad = (
        C0 * N**2
        - U * L * N
        + 1000 * c**4 * r**2 * L**2
        + r * U
        - 10 * c**2 * r**2 * (20 * w - 1)
    )

    disc = sp.factor(sp.discriminant(quad, N))
    expected_disc = (
        (U**2 - 4000 * C0 * c**4 * r**2) * L**2
        - 4 * C0 * r * U
        + 40 * C0 * c**2 * r**2 * (20 * w - 1)
    )
    assert sp.expand(disc - expected_disc) == 0

    # Verify the two-stage Euclidean descent algebraically.
    B, m, tau = sp.symbols("B m tau")
    P = 1000 * c**4 * L**4 + 10 * c**2 * (1 - 20*w) * L**2 + C0
    h = N * L - r

    # Relations rm+C0=tau L and r^2 B+N C0+r tau=U L.
    m_sub = (tau * L - C0) / r
    B_sub = (U * L - N * C0 - r * tau) / r**2
    descended = sp.factor((h * (B * L + m) - P).subs({m: m_sub, B: B_sub}))
    assert sp.factor(descended + L**2 * quad / r**2) == 0


def window_audit() -> None:
    total = 0
    max_upper = 0

    for (z, w), gaps in CENTRAL.items():
        C0 = w * (10 * w - 1)
        for gamma in gaps:
            total += 1
            c = c_gamma(gamma)
            r = gamma // c

            lower = c * (C0 + 1000 * gamma * gamma)
            upper = F(c) * (F(C0, 10) + 10000 * gamma * gamma) + 1
            assert lower < upper

            # Exact error U-f(s) at the worst allowed k=26 is absurdly <1.
            # U-f(s) = [r(C0 s^2 + A0)-s C1] / [s(sL^2-r)].
            # Bound numerator upward and denominator downward on s in [c/10,c].
            A0 = 1000 * c**4 * r**2
            C1 = 10 * c**2 * r**2 * (20*w - 1)
            s_lo = F(c, 10)
            s_hi = F(c)
            L_min = 10**26 // c

            numerator_upper = r * (C0 * s_hi * s_hi + A0)
            denominator_lower = s_lo * (s_lo * L_min * L_min - r)
            assert numerator_upper < denominator_lower

            max_upper = max(max_upper, int(upper))
            print(
                f"type={(z,w)} gamma={gamma} c={c} r={r} "
                f"U in ({lower}, {float(upper):.1f})"
            )

    assert total == 30
    assert max_upper < 10**9
    print(f"central combinations={total}, all U<1e9")


def main() -> None:
    symbolic_audit()
    window_audit()
    print("A1 central supply Pell normal-form audit OK")


if __name__ == "__main__":
    main()
