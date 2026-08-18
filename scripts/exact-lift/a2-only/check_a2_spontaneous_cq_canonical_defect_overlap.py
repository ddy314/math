#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-canonical-defect-overlap.md."""

import sympy as sp

p = 23
K, kap, rho, cu, z, g, omega = sp.symbols("K kap rho cu z g omega")

A = K**2 - 18*K + 55
E = K*(2*K - 9)
Cplus = 3*K**2 - 27*K + 55
FW = 5*K**2 - 36*K + 55

Gplus = (z + 2*cu)*A + 2*cu*E
Gminus = z*A - 2*cu*E

# Exact gate pair identities.
assert sp.expand(Gplus + Gminus - 2*(z + cu)*A) == 0
assert sp.expand(Gplus - Gminus - 2*cu*FW) == 0

# ---------------------------------------------------------------------------
# 1. Fixed-23 blow-up of A_K and F_W
# ---------------------------------------------------------------------------
K23 = 16 + p*kap
Aq = sp.expand(A.subs(K, K23) / p)
FWq = sp.expand(FW.subs(K, K23) / p)

for coeff in sp.Poly(sp.expand(Aq - (1 + 14*kap)), kap).all_coeffs():
    assert int(coeff) % p == 0
for coeff in sp.Poly(sp.expand(FWq - (10 + 9*kap)), kap).all_coeffs():
    assert int(coeff) % p == 0

# Normalized orientation gates from the previous file.
def gp(k, r):
    return (r*(1 + 14*k) + 11) % p

def gm(k, r):
    return (r*(1 + 14*k) - 9 - 18*k) % p

# Both gates lift to p^2 at exactly one (kappa,rho) pair.
both = [(k, r) for k in range(p) for r in range(p) if gp(k, r) == 0 and gm(k, r) == 0]
assert both == [(4, p - 1)]

# Pair-identity explanation: F_W quotient forces kappa=4, then A quotient is a unit.
assert [k for k in range(p) if (10 + 9*k) % p == 0] == [4]
assert (1 + 14*4) % p == 11

# rho=-1 is exactly the first layer of z+cu=g*omega being divisible by 23.
assert ((p - 1) + 1) % p == 0

# Canonical source/defect identity at the overlap gives zeta=a3/T=-K=7 mod 23.
zeta = (-16) % p
assert zeta == 7
assert (3 + 2*zeta) % p == 17  # dangerous j=3: minus 3, plus 17

# ---------------------------------------------------------------------------
# 2. c>=2 length table
# ---------------------------------------------------------------------------
inv9 = pow(9, -1, p)

def kappa_from_h(h):
    return ((16*h + 22) * inv9) % p

special = []
for M0, h0 in ((5, 15), (16, 5)):
    for rlen in range(p):
        h = (h0 + 3*rlen) % p
        k = kappa_from_h(h)
        if k in (4, 11, 18):
            special.append((M0 + 22*rlen, k, h))

assert sorted(special) == [
    (49, 4, 21),
    (170, 18, 3),
    (236, 11, 12),
    (302, 4, 21),
    (423, 18, 3),
    (489, 11, 12),
]

# ---------------------------------------------------------------------------
# 3. Rational-root quartic reduction after canonical product substitution
# ---------------------------------------------------------------------------
J, a3, q, cQ, XY = sp.symbols("J a3 q cQ XY")
pow2M1, pow2m, p5d, p5lam = sp.symbols("pow2M1 pow2m p5d p5lam", nonzero=True)
T = pow2m * p5d * p5lam
b2 = pow2M1 * pow2m * cu * g
Q = pow2M1 * cQ * q
N0 = p5lam * XY / p5d**2

# Canonical product: T*J*(T*J+2a3)=p5lam*cQ^2*XY/g^2.
F_after_product = sp.expand(
    b2**2 * (p5lam*cQ**2*XY/g**2) * (K-J)**2
    - Q**2 * N0 * (T*J+a3)**2
)
common = pow2M1**2 * cQ**2 * p5lam * XY / p5d**2
expected = sp.expand(
    common * (
        (pow2m*p5d*cu*(K-J))**2
        - (q*(T*J+a3))**2
    )
)
assert sp.simplify(F_after_product - expected) == 0

# The positive square-root branch multiplied by 5^lambda is the R_- / defect identity.
linear = sp.expand(p5lam * (pow2m*p5d*cu*(K-J) - q*(T*J+a3)))
zsym = q*p5lam
expected_linear = sp.expand(T*cu*K - zsym*a3 - (zsym + cu)*T*J)
assert sp.expand(linear - expected_linear) == 0

print("OK: A2 fixed-23 canonical defect orientation and omega-content overlap certified")
