#!/usr/bin/env python3
"""Exact certificate for the A2 fixed-199 f-side angle residual collision.

At the f-side height center K=9/2, the additive quadratic P_f and the
coefficient U_f in the depth-mismatch Bezout identity split the fixed factors:

    P_f(9/2) = -7*43/4,
    U_f(9/2) = 5*199/4.

Thus 7 and 43 are the additive-common fixed primes, while 199 is the unique
non-3 inert coefficient-degeneration prime where the f angle/height residual
can acquire an extra first layer without additive contact.
"""

import sympy as sp


def order_mod_10(modulus: int) -> int:
    return int(sp.n_order(10, modulus))


def decimal_class(tau: int, modulus: int) -> tuple[int, int]:
    order = order_mod_10(modulus)
    hits = [m for m in range(order) if pow(10, -m, modulus) == tau % modulus]
    assert len(hits) == 1
    return hits[0], order


# ---------------------------------------------------------------------------
# Fixed center and Bezout coefficient degeneration
# ---------------------------------------------------------------------------

K = sp.Rational(9, 2)
A_pref = K**2
P_center = sp.factor(3 * K**2 - 36 * K + 26)
U_center = sp.factor(3 * A_pref + 26 + 36 * K)
R_center = sp.factor(P_center * U_center)

assert P_center == -sp.Rational(301, 4)
assert U_center == sp.Rational(995, 4)
assert R_center == -sp.Rational(299495, 16)
assert sp.factorint(301) == {7: 1, 43: 1}
assert sp.factorint(995) == {5: 1, 199: 1}
assert sp.factorint(299495) == {5: 1, 7: 1, 43: 1, 199: 1}
assert 199 % 4 == 3

# ---------------------------------------------------------------------------
# f-saturation + angle + height first-layer system
# ---------------------------------------------------------------------------

x, y, tau, s = sp.symbols("x y tau s", integer=True)
D = 2025 * x**2 - 18 * y - y**2
L = 200 * x**2 * (y + 9 - 9 * tau) - y * (x + 2) ** 2
H = 2 * (y + 9) - 9 * tau

# After H=0, write s=y+9 and eliminate s from D and L.
D_h = 2025 * x**2 - s**2 + 81
L_h = -200 * x**2 * s - (s - 9) * (x + 2) ** 2
F_h = 40401 * x**4 + 1608 * x**3 + 3240 * x**2 + 96 * x + 80
assert sp.factor(sp.resultant(D_h, L_h, s)) == 2025 * x**2 * F_h

p = 199
roots = [a for a in range(p) if int(F_h.subs(x, a)) % p == 0]
assert roots == [22, 124]

states = []
for xv in roots:
    denominator = (200 * xv * xv + (xv + 2) ** 2) % p
    sv = 9 * (xv + 2) ** 2 * pow(denominator, -1, p) % p
    yv = (sv - 9) % p
    tv = 2 * sv * pow(9, -1, p) % p
    states.append((xv, yv, tv))

assert states == [(22, 83, 131), (124, 146, 145)]

# The additive quadratic is a unit on both states: 199 is angle-only here.
for xv, yv, tv in states:
    kval = (yv + 9) * pow(tv, -1, p) % p
    assert kval == 9 * pow(2, -1, p) % p
    assert (3 * kval * kval - 36 * kval + 26) % p == 74

# ---------------------------------------------------------------------------
# Unique p^2 height/angle lifts and exact residual depth one
# ---------------------------------------------------------------------------

vars_ = (x, y, tau)
eqs = (D, L, H)
J = sp.Matrix([[sp.diff(f, v) for v in vars_] for f in eqs])

expected = [
    # first state, det mod p, lift mod p^2, M class mod ord_{p^2}(10)
    ((22, 83, 131), 58, (3206, 36102, 21225), 7549),
    ((124, 146, 145), 53, (12462, 17260, 21438), 9224),
]

for first, det_expected, lift, m_expected in expected:
    det = int(J.det().subs(dict(zip(vars_, first)))) % p
    assert det == det_expected
    assert det != 0
    assert tuple(v % p for v in lift) == first

    subs = dict(zip(vars_, lift))
    assert all(int(f.subs(subs)) % (p * p) == 0 for f in eqs)

    m_class, order = decimal_class(lift[2], p * p)
    assert order == 99 * 199
    assert m_class == m_expected

# If angle and height are both deep to p^2, then A_pref=K^2 and K=9/2
# modulo p^2.  Hence the mismatch residual is congruent to the fixed center
# value, which has exact p-adic valuation one at p=199.
num = abs(sp.numer(R_center))
assert num % p == 0
assert num % (p * p) != 0

# Higher decimal membership does not provide a new obstruction: 10^99 has a
# nonzero principal-unit coefficient, so the order grows by 199 per layer.
assert pow(10, 99, p * p) == 1 + 165 * p
assert order_mod_10(p * p) == 99 * p

print(
    "OK: A2 fixed 199 is the unique f-side height/angle coefficient "
    "degeneration, with two simple decimal-compatible p^2 branches and no "
    "additive contact"
)
