"""Symbolic 5-adic Newton-ledger certificate for the A1 second-repunit edge.

Assumptions supplied mathematically by the surrounding proof:
  * 5-unsaturated side;
  * v5(d)=k-1 for b1=R*x^4-d;
  * x=10^k, R=10^r, S=10^s;
  * f>0 with q=v5(f);
  * v5(e), v5(h) are nonnegative, and h is a 5-unit whenever q>0.

The script verifies the finite monomial-ledger comparisons that create the
three Newton regions separated by
    3q = 5k+s-3
and q = 2k+s-1.
"""

from __future__ import annotations

from fractions import Fraction
import sympy as sp


x, R, S, d, e, h, f = sp.symbols("x R S d e h f", integer=True)


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
assert den == 1_000_000
phi = sp.Poly(sp.expand(num), x, R, S, d, e, h, f)

# A monomial c*x^ax R^aR S^aS d^ad e^ae h^ah f^af has lower-bound
# valuation
#   (ax+ad)k + aR*r + aS*s + af*q + (v5(c)-ad),
# plus nonnegative ae*v5(e)+ah*v5(h).
ledgers = []
for monomial, coeff in phi.terms():
    ax, aR, aS, ad, ae, ah, af = monomial
    ledgers.append(
        (
            ax + ad,
            aR,
            aS,
            af,
            v5_integer(int(coeff)) - ad,
            ae,
            ah,
            monomial,
            int(coeff),
        )
    )

LOW1 = (0, 0, 0, 2, 0, 0, 4)   # d^2 f^4
LOW2 = (2, 0, 0, 0, 2, 0, 4)   # x^2 e^2 f^4
MID = (5, 0, 1, 2, 0, 2, 1)    # x^5 S d^2 h^2 f
UP = (7, 0, 2, 2, 0, 2, 0)     # x^7 S^2 d^2 h^2

by_monomial = {row[7]: row for row in ledgers}
assert by_monomial[LOW1][:5] == (2, 0, 0, 4, 4)
assert by_monomial[LOW2][:5] == (2, 0, 0, 4, 4)
assert by_monomial[MID][:5] == (7, 0, 1, 1, 1)
assert by_monomial[UP][:5] == (9, 0, 2, 0, 0)


def diff_at_boundary(row, target, boundary: str):
    A, B, Cc, F, Dd, ae, ah, monomial, coeff = row
    At, Bt, Ct, Ft, Dt, aet, aht, _, _ = target
    ak = Fraction(A - At)
    br = Fraction(B - Bt)
    cs = Fraction(Cc - Ct)
    fq = F - Ft
    const = Fraction(Dd - Dt)

    if boundary == "lower":
        # q=(5k+s-3)/3
        ak += Fraction(5 * fq, 3)
        cs += Fraction(fq, 3)
        const -= fq
    elif boundary == "upper":
        # q=2k+s-1
        ak += 2 * fq
        cs += fq
        const -= fq
    else:
        raise ValueError(boundary)
    return ak, br, cs, const, ae - aet, ah - aht, monomial


# At the lower resonance, exactly LOW1, LOW2, MID can be minimal.
target_low = by_monomial[LOW1]
lower_equal = []
for row in ledgers:
    diff = diff_at_boundary(row, target_low, "lower")
    ak, br, cs, const, de, dh, monomial = diff
    assert ak >= 0 and br >= 0 and cs >= 0
    assert ak + br + cs + const >= 0
    if ak == br == cs == const == 0:
        lower_equal.append(monomial)
assert set(lower_equal) == {LOW1, LOW2, MID}

# In the open middle interval the MID monomial is uniquely minimal.
target_mid = by_monomial[MID]
for row in ledgers:
    if row[7] == MID:
        continue
    Fdiff = row[3] - target_mid[3]
    if Fdiff > 0:
        diff = diff_at_boundary(row, target_mid, "lower")
        # Strict q>lower makes equality rows strictly deeper.
    elif Fdiff < 0:
        diff = diff_at_boundary(row, target_mid, "upper")
        # Strict q<upper makes equality rows strictly deeper.
    else:
        A, B, Cc, F, Dd, ae, ah, monomial, coeff = row
        diff = (
            Fraction(A - target_mid[0]),
            Fraction(B - target_mid[1]),
            Fraction(Cc - target_mid[2]),
            Fraction(Dd - target_mid[4]),
            ae - target_mid[5],
            ah - target_mid[6],
            monomial,
        )
    ak, br, cs, const, de, dh, monomial = diff
    assert ak >= 0 and br >= 0 and cs >= 0
    assert ak + br + cs + const >= 0

# At the upper resonance exactly MID and UP can be minimal; above it UP is
# uniquely minimal.
target_up = by_monomial[UP]
upper_equal = []
for row in ledgers:
    diff = diff_at_boundary(row, target_up, "upper")
    ak, br, cs, const, de, dh, monomial = diff
    assert ak >= 0 and br >= 0 and cs >= 0
    assert ak + br + cs + const >= 0
    if ak == br == cs == const == 0:
        upper_equal.append(monomial)
assert set(upper_equal) == {MID, UP}

print("A1 repunit 5-adic Newton funnel certificate: PASS")
print("lower resonance: 3q = 5k+s-3")
print("upper resonance: q = 2k+s-1")
