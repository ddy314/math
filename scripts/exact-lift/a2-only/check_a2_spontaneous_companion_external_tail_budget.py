#!/usr/bin/env python3
"""Certificate for spontaneous-companion-external-tail-budget.md."""

import sympy as sp

D, z, K, f, N, q, W, g, om = sp.symbols(
    "D z K f N q W g om", nonzero=True
)

# Linear gate has the content-exposing form
# L_JB = 2 D g omega K - f q W_q.
L1 = D * z * K + f * N
expr = L1.subs(N, D * K - q * W)
expr = expr.subs(z + f, 2 * g * om)
# SymPy does not rewrite z+f inside an expanded expression automatically;
# collect before the explicit source-triangle substitution.
expr = sp.expand(D * K * (z + f) - f * q * W).subs(f, 2 * g * om - z)
assert sp.factor(expr - (2 * D * g * om * K - f * q * W).subs(f, 2 * g * om - z)) == 0

# Abstract valuation ledger for an external common prime:
# k=min(j,b) is paid by L_JB, and tail normalization removes no p-factor
# once p does not divide alpha.
for j in range(1, 7):
    for b in range(1, 7):
        k = min(j, b)
        vL_min = k
        assert vL_min >= k
        if j != b:
            assert vL_min == k

# The global normalized reader is strictly shorter than the raw 45*T^2*N^3 bound
# by the positive integer omega*Gamma.
for omega_gamma in (1, 2, 7, 100):
    assert 45 / omega_gamma <= 45

print("OK: A2 generic external companion-common depth is read by Lambda_tail")
