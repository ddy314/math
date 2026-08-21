#!/usr/bin/env python3
"""Exact p^2 certificate for A2 fixed denominator-height-angle templates.

The mechanically merged fixed-denominator-height-angle ledger already gives
five genuine first-layer templates at p=7,23,43 and proves that denominator,
height W_q, and additive cofactor T_hat cannot all have depth >= 2.

This certificate classifies what happens when the saturated denominator and
angle/common equations *do* continue to p^2.  For every first-layer template
there are exactly two nonsingular asymmetric continuations:

* height-deep: denominator + angle + height continue to p^2, while additive
  depth is exactly one;
* additive-deep: denominator + angle + additive continue to p^2, while height
  depth is exactly one.

It also checks the refined decimal exponent class M modulo ord_{p^2}(10).
"""

import sympy as sp


def order_mod_10(modulus: int) -> int:
    value = 1
    for exponent in range(1, 10_000):
        value = value * 10 % modulus
        if value == 1:
            return exponent
    raise AssertionError("order search bound too small")


def decimal_class(tau: int, modulus: int) -> tuple[int, int]:
    order = order_mod_10(modulus)
    hits = [m for m in range(order) if pow(10, -m, modulus) == tau % modulus]
    assert len(hits) == 1
    return hits[0], order


def normalized_first_layer(value: int, p: int) -> int:
    modulus = p * p
    residue = value % modulus
    assert residue % p == 0
    return residue // p % p


# ---------------------------------------------------------------------------
# q-side fixed p=23 templates
# ---------------------------------------------------------------------------

y, tau = sp.symbols("y tau", integer=True)
s = y + 9
D_q = 8100 - 18 * y - y**2
H_q = 2 * s - 9 * tau
A_q = s**2 - 26 * tau**2
q_vars = (y, tau)

q_rows = [
    # first layer, branch, p^2 lift, det, shallow unit, M class mod 506
    ((18, 6), "height", (156, 213), 3, 14, 236),
    ((18, 6), "additive", (156, 75), 12, 8, 302),
    ((10, 17), "height", (355, 316), 20, 14, 489),
    ((10, 17), "additive", (355, 454), 12, 15, 49),
]

for first, branch, lift, det_expected, shallow_expected, m_expected in q_rows:
    p = 23
    modulus = p * p
    assert tuple(v % p for v in lift) == first

    deep = (D_q, H_q) if branch == "height" else (D_q, A_q)
    shallow = A_q if branch == "height" else H_q

    jac = sp.Matrix([[sp.diff(f, v) for v in q_vars] for f in deep])
    det = int(jac.det().subs(dict(zip(q_vars, first)))) % p
    assert det == det_expected
    assert det != 0

    subs = dict(zip(q_vars, lift))
    assert all(int(f.subs(subs)) % modulus == 0 for f in deep)
    shallow_unit = normalized_first_layer(int(shallow.subs(subs)), p)
    assert shallow_unit == shallow_expected
    assert shallow_unit != 0

    m_class, order = decimal_class(lift[1], modulus)
    assert order == 506
    assert m_class == m_expected


# ---------------------------------------------------------------------------
# f-side fixed p=7,43 templates
# ---------------------------------------------------------------------------

x, y, tau = sp.symbols("x y tau", integer=True)
s = y + 9
D_f = 2025 * x**2 - 18 * y - y**2
L_f = 200 * x**2 * (s - 9 * tau) - y * (x + 2) ** 2
H_f = 2 * s - 9 * tau
A_f = 3 * s**2 - 36 * s * tau + 26 * tau**2
f_vars = (x, y, tau)

f_rows = [
    # p, first layer, branch, p^2 lift, det, shallow unit, M class, order
    (7, (4, 6, 1), "height", (39, 48, 29), 4, 5, 18, 42),
    (7, (4, 6, 1), "additive", (25, 34, 22), 3, 5, 24, 42),
    (43, (5, 37, 15), "height", (1252, 424, 918), 4, 4, 640, 903),
    (43, (5, 37, 15), "additive", (1295, 1327, 359), 31, 30, 787, 903),
    (43, (18, 33, 38), "height", (1738, 1065, 855), 3, 10, 575, 903),
    (43, (18, 33, 38), "additive", (1007, 76, 683), 3, 33, 92, 903),
]

for p, first, branch, lift, det_expected, shallow_expected, m_expected, order_expected in f_rows:
    modulus = p * p
    assert tuple(v % p for v in lift) == first

    deep = (D_f, L_f, H_f) if branch == "height" else (D_f, L_f, A_f)
    shallow = A_f if branch == "height" else H_f

    jac = sp.Matrix([[sp.diff(f, v) for v in f_vars] for f in deep])
    det = int(jac.det().subs(dict(zip(f_vars, first)))) % p
    assert det == det_expected
    assert det != 0

    subs = dict(zip(f_vars, lift))
    assert all(int(f.subs(subs)) % modulus == 0 for f in deep)
    shallow_unit = normalized_first_layer(int(shallow.subs(subs)), p)
    assert shallow_unit == shallow_expected
    assert shallow_unit != 0

    m_class, order = decimal_class(lift[2], modulus)
    assert order == order_expected
    assert m_class == m_expected


# Principal-unit generators: higher decimal-orbit membership cannot kill the
# unique Hensel branches merely by passing from p^2 to p^k.
assert pow(10, 6, 49) == 1 + 1 * 7
assert pow(10, 22, 529) == 1 + 8 * 23
assert pow(10, 21, 1849) == 1 + 12 * 43

# Hence ord_{p^k}(10) grows by p at each higher layer.  For p=7,23 this is
# the full unit group; for p=43 it is the same index-2 Teichmueller subgroup,
# with the full principal-unit direction available above the first layer.
assert order_mod_10(49) == 6 * 7
assert order_mod_10(529) == 22 * 23
assert order_mod_10(1849) == 21 * 43

print(
    "OK: A2 fixed 7/23/43 templates have exactly the certified asymmetric "
    "p^2 continuations, with the complementary depth equal to one"
)
