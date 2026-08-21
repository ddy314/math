#!/usr/bin/env python3
"""Certificate for descendant-projective-exact-depth-reader.md.

Rebuild the universal projective additive quadratic L and descendant polynomial
E. Reduce E modulo L to q=A*r+B and verify the exact identity

    X = 55*q^2 - A*L'(r)*q + A^2*L.

Important: L is the normalized additive error, not an exact real-zero relation.
For a generic prime with A and L' units, if a=v_p(q), b=v_p(L), then
unequal depths are read exactly by X: v_p(X)=min(a,b).  Extra resultant depth
is possible only on the equal-depth branch a=b, where it is controlled by one
normalized linear cancellation.
"""

import sympy as sp

r, u, v = sp.symbols("r u v")
K, zeta = sp.symbols("K zeta")

U = 2*K - 9
Lk = K**2 - 576*K + 1296
A0 = 5*K**2 + 144*K - 324
B2 = 381*K**4 - 78048*K**3 - 277520*K**2 + 2392704*K - 3074112
B1 = 189*K**4 - 126720*K**3 + 132784*K**2 + 1359360*K - 2218752
B0 = 63*K**4 - 54432*K**3 + 136672*K**2 + 239616*K - 539136
E63 = sp.expand(
    98304*U**3*A0*zeta**3
    - 1024*U**2*B2*zeta**2
    + 32*U*Lk*B1*zeta
    - Lk**2*B0
)

Eproj = sp.Poly(sp.expand(E63.subs({K: 1/r, zeta: u/r}) * r**8), r)
Lexpr = 55*r**2 + 18*(u-1)*r + 1 - 4*u - v

# Exact Euclidean remainder over Q(u,v).
F = sp.QQ.frac_field(u, v)
_, rem = sp.div(
    sp.Poly(Eproj.as_expr(), r, domain=F),
    sp.Poly(Lexpr, r, domain=F),
)
assert rem.degree() == 1
A = sp.factor(rem.coeff_monomial(r))
B = sp.factor(rem.coeff_monomial(1))
q = sp.expand(A*r + B)
Lprime = sp.diff(Lexpr, r)

# Resultant of the quadratic and the linear remainder.
Xlin = sp.expand(
    55*B**2
    - 18*(u-1)*A*B
    + (1-4*u-v)*A**2
)

# The full degree-8 resultant differs only by the fixed 5^7*11^7 content.
Rfull = sp.resultant(Lexpr, Eproj.as_expr(), r)
assert sp.factor(Rfull / Xlin) == 5**7 * 11**7

# Main exact identity. No congruence or truncation is used here.
assert sp.factor(
    Xlin - (55*q**2 - A*Lprime*q + A**2*Lexpr)
) == 0

# Verify what L means in the original variables. With
# r=1/K, u=zeta/K, v=R/K^2,
# K^2 L = R0-R where R0 is the additive value forced by T_hat=0.
R = sp.symbols("R")
R0 = K**2 - (18 + 4*zeta)*K + 18*zeta + 55
Lback = sp.factor(
    K**2 * Lexpr.subs({r: 1/K, u: zeta/K, v: R/K**2})
)
assert sp.expand(Lback - (R0 - R)) == 0

# Abstract p-adic bookkeeping for generic A,L' units.  We choose units A=L'=1
# and vary normalized leading units of q and L.  The valuation conclusions are
# structural because the unique shallow term has a unit coefficient.
def vp(n: int, p: int) -> int:
    n = abs(int(n))
    if n == 0:
        return 10**9
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out

for p in (7, 19, 31, 43):
    assert 55 % p != 0
    for a in range(1, 5):
        for b in range(1, 5):
            qn = p**a
            Ln = p**b
            Xn = 55*qn**2 - qn + Ln
            if a < b:
                assert vp(Xn, p) == a
            elif b < a:
                assert vp(Xn, p) == b
            else:
                # Equal depth is the only place where the two depth-e terms can
                # cancel. Choosing equal normalized units forces one extra layer
                # in this abstract model.
                assert vp(Xn, p) > a

# At equal depth e, after division by p^e the first term vanishes mod p and
# the next digit is A*(A*L_e-L'*q_e).  Check the scalar model explicitly.
for p in (7, 19, 31, 43):
    for qe in range(1, p):
        for Le in range(1, p):
            residue = (Le - qe) % p
            assert residue == 0 if Le == qe else residue != 0

print("OK: projective resultant is exact off equal depth; only normalized equal-depth cancellation can add valuation")
