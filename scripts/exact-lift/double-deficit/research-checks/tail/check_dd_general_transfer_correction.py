#!/usr/bin/env python3
"""Finite sanity audit for the DD general-transfer correction.

This is NOT a proof and does not enumerate DD solutions.  It checks the
valuation bookkeeping in the correction note and exhibits many finite
valuation states satisfying the valid pre-discriminant hard-sheet
constraints while violating the formerly claimed local transfer.
"""


def vp_formula_audit(limit: int = 12) -> None:
    hard = 0
    old_transfer_violations = 0
    corrected_ledger = 0
    deep = 0

    for E in range(limit + 1):
        for j in range(limit + 1):
            M = max(E, j)
            delta = max(E - j, 0)
            r3 = max(j - E, 0)
            for c in range(1, limit + 1):
                x = max(c - j - min(E, j), 0)
                if x == 0:
                    continue
                for t in range(min(x, limit + 1)):
                    for n0 in range(min(x, limit + 1)):
                        if not (x > t and x > n0 and x > r3):
                            continue

                        # Surviving, pre-error hard-sheet conclusions.
                        alpha = t + delta
                        Delta = c + j - E + n0 - 2 * t
                        if Delta <= 0:
                            continue

                        hard += 1

                        # Correct Xi valuation from Xi^2 identity.
                        v_m2 = 2 * (M + t)
                        v_other = 2 * (M + t) + Delta
                        assert v_other > v_m2
                        v_xi = M + t

                        # Unified discriminant root differs by kappa*G/q.
                        v_kappa = 3 * E + c - j
                        v_norm = v_kappa + 2 * E - M
                        v_w_tilde = v_norm + v_xi
                        assert v_w_tilde == 5 * E + c - j + t

                        # The old transfer would assert x <= max(t,n0,r3),
                        # precisely false on this deliberately hard sheet.
                        assert x > max(t, n0, r3)
                        old_transfer_violations += 1

                        # Corrected charged allocation.
                        eB = min(x, t)
                        x1 = x - eB
                        ea = min(x1, alpha)
                        x2 = x1 - ea
                        eN = min(x2, n0)
                        x3 = x2 - eN
                        e3 = min(x3, r3)
                        h = x3 - e3
                        assert x == eB + ea + eN + e3 + h

                        if h > 0:
                            # Once hard residual survives, every capacity
                            # above is saturated and the exact ledger follows.
                            assert eB == t
                            assert ea == alpha
                            assert eN == n0
                            assert e3 == r3
                            y = 2 * t + n0 + M + j
                            assert c == h + y
                            corrected_ledger += 1
                            if h > y:
                                deep += 1

    print(f"hard valuation states checked: {hard}")
    print(f"states contradicting old transfer implication: {old_transfer_violations}")
    print(f"positive corrected hard residual states: {corrected_ledger}")
    print(f"deep corrected hard states: {deep}")


def exact_normalization_spot_checks(limit: int = 8) -> None:
    """Check the algebraic normalization formula with exact rational arithmetic.

    We choose arbitrary positive integers for L,Q,G,tau,C,N and keep only
    choices for which kappa=L*Q*G/tau is integral.  These are algebra checks,
    not DD solution generation.
    """
    from fractions import Fraction

    checked = 0
    for L in range(1, limit + 1):
        for Q in range(1, limit + 1):
            for G in range(1, limit + 1):
                for tau in range(1, limit + 1):
                    num = L * Q * G
                    if num % tau:
                        continue
                    kappa = num // tau
                    C0 = L * Q + 2 * tau
                    for C in range(1, 4):
                        for N in range(1, 4):
                            bracket = Fraction(C * C, 1) - Fraction(C0 * Q * N, L * G * G)
                            wt2 = (kappa * G) ** 2 * bracket
                            direct = (kappa * G * C) ** 2 - kappa * (kappa + 2 * G) * Q * Q * N
                            assert wt2 == direct
                            checked += 1
    print(f"exact normalization algebra spot checks: {checked}")


if __name__ == "__main__":
    vp_formula_audit()
    exact_normalization_spot_checks()
