"""5-adic monomial certificate for the A1 second-repunit minimal third edge.

On this edge:
    g = 0,
    n2 = 2k,
    a2 = 10^(2k)-1,
    b2 = 10^(k-1),
    ell = 2k+1,
    b3 = 10^(2k),
    a3 = 10^(2k+1)-h,
    h in {1,3,7,9,11}.

Write x=10^k, R=10^(m1-4k), b1=R*x^4-d, a1=10*R*x^4+e.
The mathematical sieve proves v5(d)=k-1.  This script verifies that in the
cleared exact-lift polynomial the monomial x^7*d^2 is the unique term of
minimal 5-adic valuation, independently of k>=1, R, and v5(e)>=0.
"""

from __future__ import annotations

import sympy as sp


x, R, d, e = sp.symbols("x R d e", integer=True)


def v5_integer(value: int) -> int:
    value = abs(int(value))
    assert value
    out = 0
    while value % 5 == 0:
        value //= 5
        out += 1
    return out


def build_phi(h: int) -> sp.Poly:
    b1 = R * x**4 - d
    a1 = 10 * R * x**4 + e
    b2 = x / 10
    a2 = x**2 - 1
    b3 = x**2
    a3 = 10 * x**2 - h

    C = a1 * x**2 + a2
    Q = b1 * x + b2
    T = 10 * x**2
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
    assert den == 100
    return sp.Poly(sp.expand(num), x, R, d, e)


for h in (1, 3, 7, 9, 11):
    phi = build_phi(h)
    target_monomial = (7, 0, 2, 0)  # x^7 R^0 d^2 e^0
    target_coeff = int(phi.coeff_monomial(x**7 * d**2))
    assert v5_integer(target_coeff) == 4

    # Under v5(x)=k, v5(R)>=1, v5(d)=k-1 and v5(e)>=0,
    # a monomial x^ax R^aR d^ad e^ae has lower-bound valuation
    #   (ax+ad) k + aR + (v5(coeff)-ad).
    # The target has (ax+ad, aR, constant) = (9, 0, 2), hence 9k+2.
    for monomial, coeff in phi.terms():
        if monomial == target_monomial:
            continue
        ax, aR, ad, ae = monomial
        coeff_v5 = v5_integer(int(coeff))
        k_slope = ax + ad
        constant = coeff_v5 - ad

        # Every other term is already at least one full k-step deeper;
        # R and e can only increase its valuation further.
        assert k_slope >= 10, (h, monomial, coeff)
        assert aR >= 0
        assert constant >= 2, (h, monomial, coeff)

print("A1 minimal-third 5-adic certificate: PASS")
print("unique minimal monomial: x^7*d^2")
print("valuation: 9*k+2")
