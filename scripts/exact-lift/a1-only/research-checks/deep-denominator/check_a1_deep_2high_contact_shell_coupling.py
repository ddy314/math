#!/usr/bin/env python3
"""Symbolic/exact audit for deep-2high-contact-shell-coupling.md.

This checks the algebraic coupling between the stripped four-factor system,
the first complement remainder, and the normalized R shell.  It also verifies
the uniform 1e-63 correction bound used by the integer slot certificate.
"""

import sympy as sp


def main() -> None:
    beta, alpha, u, v, b1, f = sp.symbols(
        "beta alpha u v b1 f", integer=True
    )
    R = sp.symbols("R", integer=True)

    Q = 10 * b1 + 1

    # After multiplying the stripped supply equation by M=uv, its left side
    # is beta*u*Q - 5*alpha*v*b1.  Use the complement relation
    # 2*beta*u-alpha*v=f.
    lhs = beta * u * Q - 5 * alpha * v * b1
    reduced = beta * u + 5 * b1 * f
    assert sp.expand(lhs - reduced).subs(alpha * v, 2 * beta * u - f) == 0

    # R=2 beta u + alpha v and complement difference=f imply beta*u=(R+f)/4.
    assert sp.expand(
        (2 * beta * u + alpha * v) - R
    ).subs(alpha * v, 2 * beta * u - f).subs(beta * u, (R + f) / 4) == 0

    # Decimal polynomial identity used in the first-remainder comparison.
    T, w = sp.symbols("T w", integer=True)
    b1T = 10 * T**2 - w
    assert sp.expand(5 * T * (1 + 20 * b1T) - (1000 * T**3 - (100*w - 5)*T)) == 0

    # J1/T = 5(y+20w-1).
    y = sp.symbols("y")
    c2 = 10 * (1 - 20 * w)
    R1_over_T = 5 * y - (100 * w - 5)
    J1_over_T = sp.expand(R1_over_T - c2)
    assert sp.expand(J1_over_T - 5 * (y + 20*w - 1)) == 0

    # Eliminate mu between y^2=1+mu*xi/25 and
    # J1/T=mu*Gamma+C0/T^2.
    xi, Gamma, mu = sp.symbols("xi Gamma mu", positive=True)
    C0 = w * (10*w - 1)
    gamma_expr = xi * (y + 20*w - 1 - C0/(5*T**2)) / (5*(y**2 - 1))
    eq = sp.expand(
        5 * (y + 20*w - 1)
        - (25 * (y**2 - 1) / xi) * gamma_expr
        - C0 / T**2
    )
    assert sp.simplify(eq) == 0

    # Exact global correction bound at k>=32, xi<15,214,000,
    # C0<=156, y>3780, T>=10^32:
    # xi*C0 / (25*T^2*(y^2-1)) < 1e-63.
    num = 15_214_000 * 156 * 10**63
    den = 25 * 10**64 * (3780**2 - 1)
    assert num < den

    print("A1 contact-shell coupling symbolic audit OK")
    print("uniform F0-Gamma correction < 1e-63 verified exactly")


if __name__ == "__main__":
    main()
