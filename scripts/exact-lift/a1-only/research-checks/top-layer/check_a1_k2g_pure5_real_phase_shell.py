#!/usr/bin/env python3
"""Exact coefficient audit for the A1 k=2g, J=0 real phase shell.

This is a research/check certificate for
  d=2, r=s=1, g>=1, k=2g, J=0,
primitive-pruned types (z,w)=(1,1),(1,3).

All arithmetic in the assertions is exact SymPy integer/rational arithmetic.
No floating-point comparison is used.
"""

import sympy as sp

H, eta, t, w = sp.symbols("H eta t w")
z = sp.Integer(1)

b1 = 10 * H**4 - w
b2 = H
a2 = 10 * H**4 - z
a1 = H * (100 * H**4 + 51 - 10 * z - 10 * w)
Q0 = 10 * b1 + 1
Q = H * Q0
G = b1 * b2
D = H * Q
C = a1 * (10 * H**4) + a2
N = (a1 * b2) ** 2 + (a2 * b1) ** 2
rho = H - t / H**2

# Exact-lift equation, with H^8 clearing the rho denominators.
F = sp.expand(
    H**8
    * (
        G**2 * rho**2 * (C + eta) ** 2
        - (D + rho) ** 2 * (N * rho**2 + G**2 * eta**2)
    )
)
P = sp.Poly(F, H)
assert P.degree() == 30
assert sp.expand(P.coeff_monomial(H**30)) == 200000 * (
    -5 * eta**2 + 10 * t + 40 * w - 339
)
assert sp.expand(P.coeff_monomial(H**29)) == 200000 * (eta - 5)
assert P.coeff_monomial(H**28) == 0


def abs_monomial_bound(expr, fixed, eta_max=sp.Integer(1), t_max=sp.Integer(95)):
    """Triangle bound on |expr| for 0<=eta<=eta_max, 0<=t<=t_max."""
    poly = sp.Poly(sp.expand(expr.subs(fixed)), eta, t)
    total = sp.Integer(0)
    for (e_eta, e_t), coeff in poly.terms():
        total += abs(coeff) * eta_max**e_eta * t_max**e_t
    return sp.factor(total)


def normalized_tail_bound(poly, fixed, max_degree, t_value=None):
    """Bound sum_{d<=max_degree} |c_d|/10^(30-d), valid for H>=10."""
    total = sp.Integer(0)
    for d in range(max_degree, -1, -1):
        coeff = sp.expand(poly.coeff_monomial(H**d))
        if coeff == 0:
            continue
        fixed_now = dict(fixed)
        if t_value is not None:
            fixed_now[t] = t_value
            q = sp.Poly(sp.expand(coeff.subs(fixed_now)), eta)
            bound = sum(abs(c) for _, c in q.terms())
        else:
            bound = abs_monomial_bound(coeff, fixed_now)
        total += bound / sp.Integer(10) ** (30 - d)
    return sp.factor(total)


# Monotonicity in t. The H^30 coefficient of dF/dt is exactly 2,000,000.
dP = sp.Poly(sp.diff(F, t), H)
assert dP.coeff_monomial(H**30) == 2_000_000
assert dP.coeff_monomial(H**29) == 0

for wv, cap in [(1, 945_519), (3, 910_317)]:
    tail = normalized_tail_bound(dP, {w: wv}, 28)
    assert tail < cap
    assert 2_000_000 - tail > 0

# Endpoint signs. At the lower endpoint the H^30 term is <= -10,000 H^30
# (eta>=1/10), and the H^29 term is <= -80,000 H^30 (H>=10).
# At the upper endpoint the H^30 term is >= +200,000 H^30 (eta<1),
# while the H^29 term is > -100,000 H^30.
endpoints = {
    1: (sp.Rational(299, 10), sp.Rational(305, 10), 10_697, 85_231),
    3: (sp.Rational(219, 10), sp.Rational(225, 10), 7_768, 62_514),
}

for wv, (lo, hi, lo_tail_cap, hi_tail_cap) in endpoints.items():
    lo_tail = normalized_tail_bound(P, {w: wv}, 28, lo)
    hi_tail = normalized_tail_bound(P, {w: wv}, 28, hi)
    assert lo_tail < lo_tail_cap
    assert hi_tail < hi_tail_cap

    # Uniform endpoint signs after division by H^30.
    assert -10_000 - 80_000 + lo_tail < 0
    assert 200_000 - 100_000 - hi_tail > 0

print("PASS: exact k=2g,J=0 real-phase shell coefficient audit")
print("w=1: 299/10 < t < 305/10")
print("w=3: 219/10 < t < 225/10")
