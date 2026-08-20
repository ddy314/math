#!/usr/bin/env python3
"""Mechanical checks for good-short-residue-audit.md.

This script certifies only finite valuation identities and symbolic algebraic
identities used in the proof note.  It does not prove DD emptiness.
"""

from __future__ import annotations

from sympy import symbols, simplify


def check_valuation_ledger(limit: int = 16) -> None:
    """Check the nested C_N/C ladders and overflow split."""

    for h in range(1, limit + 1):
        for n in range(0, limit + 1):
            c = max(h - n, 0)
            g_axis = min(h, n)

            for eps in range(0, limit + 1):
                g_exc = min(c, eps)
                g_full = min(h, eps)
                g_reuse = g_full - g_exc
                deep = max(eps - h, 0)
                over = max(eps - c, 0)

                assert g_exc >= 0
                assert g_full >= g_exc
                assert 0 <= g_reuse <= g_axis
                assert over == g_reuse + deep

                # The square-source divisibility is already covered by
                # C_L * N(Delta_1): on an excess prime a=n+eps.
                a = n + eps
                assert 2 * g_exc <= h + a


def check_dot_identity() -> None:
    """Verify g0*B*D = 2*(E*Nc + U*R0*A0)."""

    g0, a2, B, R0, U, A0, E, Nc = symbols(
        "g0 a2 B R0 U A0 E Nc", nonzero=True
    )

    Cstar = g0 * a2 * B / 2

    # Reconstruction: 10^d*A12=(U*A0+R0)/(g0*B).
    ten_d_A12 = (U * A0 + R0) / (g0 * B)
    Y = 2 * ten_d_A12
    D = Cstar * a2 + R0 * Y

    # Axis norm: Cstar^2+R0^2=E*Nc.
    lhs = g0 * B * D
    rhs = 2 * (E * Nc + U * R0 * A0)
    rhs_axis = rhs.subs(E * Nc, Cstar**2 + R0**2)

    assert simplify(lhs - rhs_axis) == 0


def check_secondary_norm_scaling() -> None:
    """Verify the exact scaling behind Square-collapse abstractly.

    If lambda*Re(G1)=q*P0 and lambda*ImAbs(G1)=2*r*5^T*R0,
    then the proposed short norm is lambda^2*N(G1).  The proof note
    separately records lambda=2*5^(m-T) from B=2^(m-1)5^(m-T).
    """

    lam, A, B1, qP0, tail = symbols("lam A B1 qP0 tail", nonzero=True)

    candidate = qP0**2 + tail**2
    scaled_norm = lam**2 * (A**2 + B1**2)

    substituted = candidate.subs({qP0: lam * A, tail: lam * B1})
    assert simplify(substituted - scaled_norm) == 0


def main() -> None:
    check_valuation_ledger()
    check_dot_identity()
    check_secondary_norm_scaling()
    print("DD Good short-residue audit checks passed")


if __name__ == "__main__":
    main()
