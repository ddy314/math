#!/usr/bin/env python3
"""Certificate for descendant-projective-exact-depth-reader.md.

Rebuild the universal projective branch quadratic L and descendant polynomial
E.  Reduce E modulo L to q=A*r+B and verify the exact resultant identity

    X = 55*q^2 - A*L'(r)*q + A^2*L.

On the actual branch L=0 this becomes X=q(55q-A L'), hence every prime for
which A and L' are units reads the complete q-depth without loss or gain.
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
Lproj = sp.Poly(Lexpr, r)

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

# Main exact identity.  No congruence or truncation is used here.
assert sp.factor(
    Xlin - (55*q**2 - A*Lprime*q + A**2*Lexpr)
) == 0

# Equivalent companion form: C=A*L'-55q.
C = sp.expand(A*Lprime - 55*q)
assert sp.factor(Xlin - (-q*C + A**2*Lexpr)) == 0

# On L=0 and q=0 mod p, C is congruent to A*L'.  Thus if A,L' are p-units,
# the second factor is a p-unit at every higher lift and v_p(X)=v_p(q).
# Exhaust an abstract p-adic model to certify the valuation bookkeeping.
def vp(n: int, p: int) -> int:
    n = abs(int(n))
    assert n
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out

for p in (7, 11, 19, 31):
    for e in range(1, 6):
        # q=p^e*q0, A*L'=unit.  55q-A L' remains a unit provided p does not
        # divide the chosen unit; choose 1 for the abstract unit.
        qn = p**e
        second = 55*qn - 1
        if second % p:
            assert vp(qn*second, p) == e

print("OK: generic projective carrier reads the complete descendant compatibility depth exactly")
