"""Exact certificate for the A1 top-layer double boundary.

This script checks the finite constant-offset core described in
`docs/proofs/exact-lift/branches/a1-top-layer-slope4-double-boundary-closure-2026-08-16.md`.

It does not enumerate k.  For each constant type it constructs the exact-lift
error polynomial Phi(x), x=10^k, and proves it cannot vanish for any x>=10 by
coefficient dominance.
"""

from __future__ import annotations

import sympy as sp


x, d, e, h, f = sp.symbols("x d e h f", integer=True)

# Boundary data, x = 10^k.
b1 = 10 * x**4 - d
a1 = 100 * x**4 + e
b2 = x / 10
a2 = x**2 - 1
b3 = x**2 + f
a3 = 10 * x**2 - h

# g=0, m2=k, n2=2k, ell=2k+1.
C = a1 * x**2 + a2
Q = b1 * x + b2
T = 10 * x**2
alpha = T * C + a3
beta = T * Q + b3

# Exact lift squared and cleared of the harmless denominator 100 coming from b2=x/10.
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
assert den == 100
phi = sp.Poly(sp.expand(num), x)
assert phi.degree() == 26

coeff_expr = {monom[0]: coeff for monom, coeff in phi.terms()}
assert sp.expand(coeff_expr[26]) == 2_000_000 * (
    10 * d + e + 100 * f + 10 * h - 50
)
assert coeff_expr[25] == -2_000_000


def integer_coeffs(dd: int, ee: int, hh: int, ff: int) -> dict[int, int]:
    subs = {d: dd, e: ee, h: hh, f: ff}
    return {degree: int(coeff.subs(subs)) for degree, coeff in coeff_expr.items()}


def dominant_for_x_ge_10(coeffs: dict[int, int]) -> bool:
    """Sufficient sign certificate using x=10 as the worst ratio."""
    degree = max(j for j, value in coeffs.items() if value)
    lead = abs(coeffs[degree]) * 10**degree
    rest = sum(abs(value) * 10**j for j, value in coeffs.items() if j < degree)
    return lead > rest


total = 0
nonzero_lead = 0
zero_lead_cases: list[tuple[int, int, int, int]] = []

for dd in range(1, 6):
    for ee in range(0, 53 - 10 * dd):
        for hh in range(1, 12):
            for ff in (0, 1):
                total += 1
                coeffs = integer_coeffs(dd, ee, hh, ff)
                if coeffs[26] != 0:
                    nonzero_lead += 1
                    assert dominant_for_x_ge_10(coeffs), (dd, ee, hh, ff)
                else:
                    zero_lead_cases.append((dd, ee, hh, ff))

assert total == 2530
assert nonzero_lead == 2520
assert len(zero_lead_cases) == 10

# In the ten leading-cancellation cases:
#   f=0, 10d+e+10h=50,
# the degree is exactly 25 with coefficient -2,000,000.  Every positive lower
# term has degree <=22.  We verify a uniform coefficient-sum bound, which then
# proves negativity for every x>=10.
max_positive_sum = 0
for dd, ee, hh, ff in zero_lead_cases:
    assert ff == 0
    assert 10 * dd + ee + 10 * hh == 50
    coeffs = integer_coeffs(dd, ee, hh, ff)
    degree = max(j for j, value in coeffs.items() if value)
    assert degree == 25
    assert coeffs[25] == -2_000_000
    positive_terms = [(j, value) for j, value in coeffs.items() if value > 0]
    assert all(j <= 22 for j, _ in positive_terms)
    positive_sum = sum(value for _, value in positive_terms)
    max_positive_sum = max(max_positive_sum, positive_sum)
    # For x>=10, sum(pos_j x^j) <= positive_sum*x^22, while
    # 2,000,000*x^25 >= 2,000,000*10^3*x^22.
    assert positive_sum < 2_000_000 * 10**3

assert max_positive_sum == 149_711_768

print("A1 slope-4 double-boundary certificate: PASS")
print(f"constant types checked: {total}")
print(f"nonzero x^26 leading coefficient: {nonzero_lead}")
print(f"leading-cancellation types: {len(zero_lead_cases)}")
print(f"max positive lower-coefficient sum: {max_positive_sum}")
