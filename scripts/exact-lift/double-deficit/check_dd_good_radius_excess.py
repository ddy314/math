#!/usr/bin/env python3
"""Exact/mechanical checks for good-radius-excess.md.

This script does not prove the DD frontier empty.  It certifies the finite
valuation bookkeeping used in the canonical baseline/excess lemma and the
exact decimal-alpha identity recorded in the note.
"""

import sympy as sp


# ---------------------------------------------------------------------------
# 1. Valuation ledger.
#
# Existing theorem (Radius-split):
#   a_raw = min(r, n) + eps, eps >= 0,
#   eps > 0 => r == n.
# The main C_L depth is truncated at h.
for h in range(1, 9):
    for r in range(9):
        for n in range(9):
            for eps in range(9):
                # We enumerate exactly the logical regime allowed by
                # eps > 0 => r == n.
                if eps > 0 and r != n:
                    continue

                a_raw = min(r, n) + eps
                a = min(h, a_raw)
                b = min(h, r, n)
                x = a - b

                assert x >= 0

                if x > 0:
                    # Proposition 3.1: positive excess forces true equal depth
                    # below the available main C_L exponent.
                    assert r == n
                    assert r == b
                    assert n == b
                    assert b < h

                    # After removing the baseline p^b, both cofactor terms
                    # have valuation zero.  The surviving depth is therefore
                    # a unit-unit cancellation.  x is the portion still
                    # visible inside p^h || C_L.
                    assert r - b == 0
                    assert n - b == 0
                    assert x == min(h - b, eps)


# ---------------------------------------------------------------------------
# 2. Slot separation.
# Existing slot rules:
#   min(r,j)=0 and min(j,n)=0.
# If baseline b=min(h,r,n) is positive, j must vanish.
for h in range(1, 9):
    for r in range(9):
        for n in range(9):
            for j in range(9):
                if min(r, j) != 0:
                    continue
                if min(j, n) != 0:
                    continue
                b = min(h, r, n)
                if b > 0:
                    assert j == 0


# ---------------------------------------------------------------------------
# 3. Exact decimal-alpha no-go.
# Replace 10^d by P and 5^T by F.  The terminal identity 10^m=2*B*5^T
# is encoded by M=2*B*F.
B, P, F, V, U, A12, a3 = sp.symbols(
    "B P F V U A12 a3", nonzero=True
)
M = 2 * B * F
Sigma = V + 2 * F * U
Rdec = B * P * V * A12 - U * a3
alpha = A12 * M * P + a3

assert sp.expand(Rdec + U * alpha - B * P * A12 * Sigma) == 0

# Substituting the two exact bridges
#   g0*Rdec = Sigma*R0,
#   g0*alpha = Sigma*A0
# into the previous identity leaves precisely numerator reconstruction.
g0, R0, A0 = sp.symbols("g0 R0 A0", nonzero=True)
reconstructed = sp.expand(
    (Sigma * R0 / g0)
    + U * (Sigma * A0 / g0)
    - B * P * A12 * Sigma
)
assert sp.factor(reconstructed) == Sigma * (A0 * U - A12 * B * P * g0 + R0) / g0

print("OK: DD Good radius excess ledger and decimal-alpha no-go certified")
