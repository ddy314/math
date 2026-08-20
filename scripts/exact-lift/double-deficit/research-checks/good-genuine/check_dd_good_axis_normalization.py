#!/usr/bin/env python3
"""Mechanical certificate for good-axis-normalization.md.

This checks only the exact algebra and finite valuation logic used by the note.
It does not prove DD or the full-rational Good frontier empty.
"""

import sympy as sp


# ---------------------------------------------------------------------------
# 1. Local valuation identities.
# Existing input:
#   a = min(r,n) + eps, eps >= 0,
#   eps > 0 => r == n.
for h in range(1, 9):
    for r in range(9):
        for n in range(9):
            for eps in range(9):
                if eps > 0 and r != n:
                    continue

                a = min(r, n) + eps

                # epsilon is exactly the positive part of a-n.
                assert max(a - n, 0) == eps

                # Old G_exc depth from baseline/excess note.
                x_old = min(h, a) - min(h, r, n)

                # Axis-normalized decimal gcd depth.
                c_n = max(h - n, 0)
                a_n = max(a - n, 0)
                x_new = min(c_n, a_n)
                assert x_old == x_new

                # After removing G_exc, residual core/tail are disjoint.
                assert min(c_n - x_new, a_n - x_new) == 0

                # Companion pair:
                # T_+ has depth h+a.
                vp_plus = h + a

                # T_- compares A0-depth a against N_c-depth n.
                if a < n:
                    vp_minus_lower = h + a
                    # unequal valuations => exact
                    vp_gcd = min(vp_plus, vp_minus_lower)
                elif a > n:
                    vp_minus_lower = h + n
                    # unequal valuations => exact
                    vp_gcd = min(vp_plus, vp_minus_lower)
                else:
                    # equal valuations can cancel further, but T_+ itself caps gcd.
                    vp_minus_lower = h + a
                    vp_gcd = vp_plus

                assert vp_plus - vp_gcd == eps

                # Norm-tail reader:
                # v_p(N(Delta_1)) = min(r,n)+eps = a;
                # gcd with H_R,N_c removes min(r,n).
                assert a - min(a, r, n) == eps


# ---------------------------------------------------------------------------
# 2. Exact terminal algebra.
g0, a2, B, F, V, A0, R0, a3, E, e0, Nc = sp.symbols(
    "g0 a2 B F V A0 R0 a3 E e0 Nc", nonzero=True
)

M = 2 * B * F
C = g0 * a2 * B / 2

# Tail-axis identity is valid under VA0-g0*a3=2F*R0.
rel_source = V * A0 - g0 * a3 - 2 * F * R0

# g0*(2a3 + i M a2) = 2 V A0 + 4 i F (C+iR0)
real_diff = sp.expand(2 * g0 * a3 - (2 * V * A0 - 4 * F * R0))
imag_diff = sp.expand(g0 * M * a2 - 4 * F * C)
assert sp.factor(real_diff) == -2 * rel_source
assert sp.expand(imag_diff) == 0

# Companion coordinates from (C+iR0)(2a3-i M a2).
T_plus = 2 * C * a3 + R0 * M * a2
T_minus = 2 * R0 * a3 - C * M * a2

# T_+ = B*a2*V*A0 under the same source relation.
assert sp.factor(T_plus - B * a2 * V * A0) == B * a2 * (-rel_source)

# With C^2+R0^2=E*Nc and V=E*e0:
Nax = C**2 + R0**2
rhs_minus = 2 * E * (e0 * R0 * A0 - 2 * F * Nc)
expr_minus = sp.expand(g0 * T_minus - rhs_minus)
# Reduce by the two exact relations V=E*e0 and Nax=E*Nc plus source relation.
expr_minus = sp.expand(expr_minus.subs(V, E * e0))
expr_minus = sp.expand(expr_minus.subs(Nc, Nax / E))
assert sp.factor(expr_minus) == -2 * R0 * rel_source.subs(V, E * e0)

print("OK: DD Good axis-normalized excess and companion readers certified")
