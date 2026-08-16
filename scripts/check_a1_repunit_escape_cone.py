"""Symbolic coefficient certificate for the A1 second-repunit escape cone.

The proof treats
    r = m1 - 4k >= 1,
    s = ell - 2k >= 1,
    R = 10^r,
    S = 10^s,
and writes exact lift as a polynomial Phi(x), x=10^k.

This script verifies the universal top coefficients and the L1 coefficient
bound used with Cauchy's root bound.  It does not enumerate k, r, or s.
"""

from __future__ import annotations

import sympy as sp


x, R, S, d, e, h, f = sp.symbols("x R S d e h f", integer=True)

b1 = R * x**4 - d
a1 = 10 * R * x**4 + e
b2 = x / 10
a2 = x**2 - 1
b3 = S * x**2 / 10 + f
a3 = S * x**2 - h

C = a1 * x**2 + a2
Q = b1 * x + b2
T = S * x**2
alpha = T * C + a3
beta = T * Q + b3

raw = sp.together(
    alpha**2 * b1**2 * b2**2 * b3**2
    - beta**2
    * (
        (a1 * b2 * b3) ** 2
        + (a2 * b1 * b3) ** 2
        + (a3 * b1 * b2) ** 2
    )
)
num, den = sp.fraction(raw)
# b2=x/10 and b3=S*x^2/10+f introduce a fixed denominator 10^6
# in this generic R,S parameterization.  The numerator below is the integer
# polynomial used in the proof; multiplying by this harmless fixed scalar does
# not change its roots.
assert den == 1_000_000
phi = sp.Poly(sp.expand(num), x)
assert phi.degree() == 26

coeffs = {monom[0]: sp.expand(coeff) for monom, coeff in phi.terms()}
assert sp.factor(coeffs[26]) == 2000 * R**3 * S**3 * (
    -5 * R * S + 100 * R * f + 10 * R * h + 10 * S * d + S * e
)
assert coeffs[25] == -2000 * R**3 * S**4

# Proven offset envelope used in the document:
#   |d| <= R, |e| <= 7R, |h| <= 2S, |f| <= S.
# Every monomial of every coefficient therefore has absolute value bounded by
# its numerical coefficient times R^4 S^4, after multiplying by 7^e_exp and
# 2^h_exp.  Compute an exact L1 bound for each x-coefficient.
def l1_weighted_bound(expr: sp.Expr) -> int:
    poly = sp.Poly(expr, R, S, d, e, h, f)
    total = 0
    for monom, coeff in poly.terms():
        r_exp, s_exp, d_exp, e_exp, h_exp, f_exp = monom
        weighted_r_degree = r_exp + d_exp + e_exp
        weighted_s_degree = s_exp + h_exp + f_exp
        assert weighted_r_degree <= 4
        assert weighted_s_degree <= 4
        total += abs(int(coeff)) * 7**e_exp * 2**h_exp
    return total

bounds = {degree: l1_weighted_bound(expr) for degree, expr in coeffs.items()}
max_bound = max(bounds.values())
assert max_bound == 19_849_340

# The proof uses the round bound 9,925 after division by the universal leading
# coefficient factor 2,000.
assert max_bound < 2000 * 9925

print("A1 repunit escape-cone symbolic certificate: PASS")
print(f"degree: {phi.degree()}")
print(f"uniform coefficient bound: {max_bound}")
print("Cauchy ratio constant: < 9925")
