"""Symbolic 5-adic certificate for the A1 second-repunit lower endpoint.

This verifies the monomial-valuation statement used to rule out
    b3 = 10^(ell-1)
for every ell on the second-repunit edge.

Set x=10^k, S=10^(ell-2k), R=10^(m1-4k),
    b1=R*x^4-d, a1=10*R*x^4+e,
    b2=x/10, a2=x^2-1,
    b3=S*x^2/10, a3=S*x^2-h.
The mathematical sieve supplies v5(d)=k-1 and gcd(h,10)=1.
"""

from __future__ import annotations

import sympy as sp


x, R, S, d, e, h = sp.symbols("x R S d e h", integer=True)


def v5_integer(value: int) -> int:
    value = abs(int(value))
    assert value
    out = 0
    while value % 5 == 0:
        value //= 5
        out += 1
    return out


b1 = R * x**4 - d
a1 = 10 * R * x**4 + e
b2 = x / 10
a2 = x**2 - 1
b3 = S * x**2 / 10
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
assert den == 1_000_000
phi = sp.Poly(sp.expand(num), x, R, S, d, e, h)

# Target monomial: -200*x^7*S^2*d^2*h^2.
target_monomial = (7, 0, 2, 2, 0, 2)
target_coeff = int(phi.coeff_monomial(x**7 * S**2 * d**2 * h**2))
assert target_coeff == -200
assert v5_integer(target_coeff) == 2

# Under
#   v5(x)=k,
#   v5(R)>=1,
#   v5(S)=s>=1,
#   v5(d)=k-1,
#   v5(e)>=0,
#   v5(h)=0,
# a monomial c*x^ax R^aR S^aS d^ad e^ae h^ah has lower-bound
# valuation
#   (ax+ad)k + aR + aS*s + (v5(c)-ad).
# The target has ledger (9,0,2,0), hence valuation 9k+2s.
for monomial, coeff in phi.terms():
    if monomial == target_monomial:
        continue
    ax, aR, aS, ad, ae, ah = monomial
    ledger = (
        ax + ad,
        aR,
        aS,
        v5_integer(int(coeff)) - ad,
    )

    assert ledger[0] >= 9, (monomial, coeff, ledger)
    assert ledger[1] >= 0
    assert ledger[2] >= 2, (monomial, coeff, ledger)
    assert ledger[3] >= 0, (monomial, coeff, ledger)
    assert ledger != (9, 0, 2, 0), (monomial, coeff, ledger)

print("A1 repunit lower-endpoint 5-adic certificate: PASS")
print("unique minimal monomial: -200*x^7*S^2*d^2*h^2")
print("valuation: 9*k + 2*s")
