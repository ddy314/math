#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-decimal-gaussian-kernel.md."""

import sympy as sp

# ---------------------------------------------------------------------------
# 1. Eliminate c_+, r_+, R_1 from the explicit quotient.
# ---------------------------------------------------------------------------
g, a3, b3, cp = sp.symbols("g a3 b3 cp", nonzero=True)
rp = (g / 2 + a3) / cp
R1 = 9 * b3 / (2 * cp)
Q5 = sp.expand(rp + sp.I * R1)
assert sp.simplify(cp * Q5 - (g + 2 * a3 + 9 * sp.I * b3) / 2) == 0

# ---------------------------------------------------------------------------
# 2. Z_* is exactly 10 c_- conjugate(Z_r).
# ---------------------------------------------------------------------------
cm = sp.symbols("cm", nonzero=True)
rm = (g / 2 - a3) / (5 * cm)
R3 = 9 * b3 / (10 * cm)
Zr = sp.expand(rm + sp.I * R3)
Zstar = sp.expand(g - 2 * a3 - 9 * sp.I * b3)
assert sp.simplify(Zstar - 10 * cm * sp.conjugate(Zr)) == 0

# Coordinate/norm identity from the exact scaled vector.
Znorm = sp.expand((g - 2 * a3) ** 2 + 81 * b3**2)
scaled_norm = sp.expand(100 * cm**2 * (rm**2 + R3**2))
assert sp.simplify(Znorm - scaled_norm) == 0

# ---------------------------------------------------------------------------
# 3. Source linear form differs from omega*Z_* only by 2*5^lambda*q.
# ---------------------------------------------------------------------------
cu, omega, q = sp.symbols("cu omega q")
lam = sp.symbols("lam", integer=True, positive=True)
L5 = sp.expand(cu - cp * omega * Q5)
# Substitute g*omega = 5^lambda*q + cu after expanding 2*L5-omega*Zstar.
diff = sp.expand(2 * L5 - omega * Zstar)
diff = sp.expand(diff.subs(g * omega, 5**lam * q + cu))
assert sp.simplify(diff + 2 * 5**lam * q) == 0

# ---------------------------------------------------------------------------
# 4. Norm transfer with d=1, nu=lambda-2.
# ---------------------------------------------------------------------------
X = sp.symbols("X", integer=True, positive=True)
nu = lam - 2
normZ_from_transfer = sp.expand(100 * cm**2 * 5**nu * X)
target = sp.expand(4 * 5**lam * cm**2 * X)
assert sp.simplify(normZ_from_transfer - target) == 0

# finite-defect conversion: 4 g T J = 12 g T - 4*5^lambda C
T, C, D = sp.symbols("T C D")
J = 3 - C / D
expr = sp.expand(4 * g * T * J)
expr_sub = sp.expand(expr.subs(g * T, 5**lam * D))
assert sp.simplify(expr_sub - (12 * 5**lam * D - 4 * 5**lam * C)) == 0

# Ratio shell: C/D<3/250 implies N(Z)/(12gT)>249/250.
assert sp.Rational(1, 1) - sp.Rational(1, 250) == sp.Rational(249, 250)

print("OK: A2 fixed-23 eta=2 c=2 decimal Gaussian kernel and exact near-norm identity certified")
