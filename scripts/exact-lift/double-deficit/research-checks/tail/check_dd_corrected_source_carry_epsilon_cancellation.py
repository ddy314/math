#!/usr/bin/env python3
"""Mechanical audits for dd-corrected-source-carry-epsilon-cancellation-2026-08-22.md.

Checks the exact w-cancellation algebra, the denominator valuation lemma behind
(q_Q, epsilon)=1, and the improved numerator-entropy constants.  This is not a
proof assistant and does not certify the asymptotic DD hypotheses.
"""

from __future__ import annotations

from math import isclose

import sympy as sp


def check_w_cancellation() -> None:
    g0, U, w, q2, K, eps, P = sp.symbols(
        "g0 U w q2 K eps P", integer=True, nonzero=True
    )
    Sigma, SQ = sp.symbols("Sigma SQ", integer=True, nonzero=True)

    # SQ=w*q2*K and Sigma=eps*w inside g0*U*SQ=2*Sigma*P.
    lhs = g0 * U * SQ
    rhs = 2 * Sigma * P
    residual = sp.expand(lhs - rhs).subs({SQ: w * q2 * K, Sigma: eps * w})
    assert sp.factor(residual) == w * (g0 * U * q2 * K - 2 * eps * P)


def local_q_exponent(s: int, hhat: int, gap: int = 0, c: int = 0) -> int:
    return max(s - hhat - (gap + 1) // 2 - (c + 1) // 2, 0)


def check_epsilon_coprime_ledger(bound: int = 12) -> None:
    states = 0

    # Assume a target p divides q_Q and epsilon.  Then p|Sigma and q_Q is
    # transverse to V, so U is a unit and v_p(Q)=v_p(q)=s.  Also b3 has depth s.
    # Enumerate prefix denominator depths e1,e2 compatible with v_p(Q)=s.
    for s in range(1, bound + 1):
        e3 = s
        for e1 in range(bound + 1):
            for e2 in range(bound + 1):
                if e1 != e2:
                    # For a sum of two p-adic terms with unequal depths,
                    # v_p(Q)=min(e1,e2) exactly.
                    if min(e1, e2) != s:
                        continue
                    M = max(e1, e2, e3)
                    c3 = M - e3
                    hhat = e1 + e2 - c3  # V is a p-unit.
                    assert hhat == 2 * s
                    assert local_q_exponent(s, hhat) == 0
                    states += 1
                else:
                    E = e1
                    # Equal prefix depths can only give Q-depth >= E.
                    if s < E:
                        continue
                    M = max(E, e3)
                    c3 = M - e3
                    assert c3 == 0
                    # epsilon divides c3, so a prime with positive epsilon-depth
                    # cannot occur in this branch.
                    states += 1

    assert states > 0
    print(f"epsilon-coprime valuation states checked: {states}")


def check_constants() -> None:
    kappa_dig = 0.767009998554660
    c_one = 2.335049992773302
    zstar = 0.308883577618031

    c_num = 1 + kappa_dig
    assert isclose(c_num, 1.767009998554660, rel_tol=0, abs_tol=1e-15)

    delta_crt = 2 * zstar / (2 + c_one)
    assert isclose(delta_crt, 0.1425051974639056, rel_tol=0, abs_tol=1e-15)

    # Below delta_crt the positive-part contribution from the remaining A12
    # lifts is zero, leaving only gap-fiber + short-suffix entropy.
    assert (2 + c_one) * (delta_crt * 0.99) - 2 * zstar < 0

    print(f"improved numerator entropy coefficient: {c_num:.15f}")
    print(f"full-period uniqueness threshold: {delta_crt:.15f}")


def main() -> None:
    check_w_cancellation()
    check_epsilon_coprime_ledger()
    check_constants()
    print("DD corrected source/carry epsilon-cancellation audits passed")


if __name__ == "__main__":
    main()
