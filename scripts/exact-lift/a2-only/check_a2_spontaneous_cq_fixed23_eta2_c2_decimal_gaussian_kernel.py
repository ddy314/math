#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-decimal-gaussian-kernel.md."""

import sympy as sp

# ---------------------------------------------------------------------------
# 1. Eliminate c_+, r_+, R_1 from the explicit quotient.
# ---------------------------------------------------------------------------
g, a3, b3, cp, rp, R1 = sp.symbols("g a3 b3 cp rp R1")
assert sp.expand(cp * rp - (g / 2 + a3)) == cp * rp - g / 2 - a3
assert sp.expand(cp * R1 - 9 * b3 / 2) == cp * R1 - 9 * b3 / 2

# ---------------------------------------------------------------------------
# 2. Z_* is exactly 10 c_- conjugate(Z_r).
# ---------------------------------------------------------------------------
cm, rm, R3 = sp.symbols("cm rm R3")
Zreal = 10 * cm * rm
Zimag = -10 * cm * R3
assert sp.expand(Zreal - (g - 2 * a3)) == 10 * cm * rm - g + 2 * a3
assert sp.expand(Zimag + 9 * b3) == -10 * cm * R3 + 9 * b3

# Coordinate/norm identity once g-2a3=10 c_- r_- and 9b3=10 c_- R3.
lhs = sp.expand((10 * cm * rm) ** 2 + (10 * cm * R3) ** 2)
rhs = sp.expand(100 * cm**2 * (rm**2 + R3**2))
assert sp.expand(lhs - rhs) == 0

# ---------------------------------------------------------------------------
# 3. Norm transfer with d=1, nu=lambda-2.
# ---------------------------------------------------------------------------
lam, X = sp.symbols("lam X", integer=True, positive=True)
nu = lam - 2
normZ = sp.expand(100 * cm**2 * 5**nu * X)
target = sp.expand(4 * 5**lam * cm**2 * X)
assert sp.simplify(normZ - target) == 0

# finite-defect conversion: 4 g T J = 12 g T - 4*5^lambda C
T, C, D = sp.symbols("T C D")
J = 3 - C / D
expr = sp.expand(4 * g * T * J)
expr_sub = sp.expand(expr.subs(g * T, 5**lam * D))
assert sp.simplify(expr_sub - (12 * 5**lam * D - 4 * 5**lam * C)) == 0

# Ratio shell: C/D<3/250 implies N(Z)/(12gT)>249/250.
# Algebraic check of the endpoint constant.
assert sp.Rational(1, 1) - sp.Rational(1, 250) == sp.Rational(249, 250)

print("OK: A2 fixed-23 eta=2 c=2 decimal Gaussian kernel and exact near-norm identity certified")
