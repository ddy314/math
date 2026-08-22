#!/usr/bin/env python3
"""Certificate for source-common-outer-fixed-exception.md.

A genuine source-common prime lies on 18K-55=0.  If the same prime also
pays both outer rational-root cofactors, it lies on G_pm(K,zeta)=0; if it is
simultaneously reused by the descendant common pair, it also lies on the
universal descendant cubic E_63(K,zeta)=0.

Substituting K=55/18 and eliminating zeta gives a fixed 66-digit resultant.
Its complete squarefree factorization contains exactly one 3 mod 4 prime.
That prime has an actual F_p common zeta root (not merely an algebraic-closure
root), and it is compatible with the source-square character (55/p)=+1 and
the terminal character (-26/p)=-1.  Hence the moving source-common shared
reuse family collapses to one fixed giant exception, but that exception is
not eliminated here.
"""

import math
import sympy as sp

K, zeta = sp.symbols("K zeta")

Gpm = (
    -K**2*zeta**3 - 3*K**2*zeta**2
    + 12*K*zeta**3 + 60*K*zeta**2 + 96*K*zeta + 64*K
    - 28*zeta**3 - 156*zeta**2 - 288*zeta - 192
)

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

# Source-common linear sheet.
k_source = sp.Rational(55, 18)
Gs_num = sp.primitive(
    sp.Poly(sp.together(Gpm.subs(K, k_source)).as_numer_denom()[0], zeta)
)[1].as_expr()
Es_num = sp.primitive(
    sp.Poly(sp.together(E63.subs(K, k_source)).as_numer_denom()[0], zeta)
)[1].as_expr()

# Canonical primitive source cubics (sign is irrelevant for the resultant).
assert sp.expand(Gs_num - (217*zeta**3 + 219*zeta**2 - 1728*zeta - 1152)) == 0
expected_Es = (
    -472107612503015424*zeta**3
    + 5728570300274245632*zeta**2
    - 21821587044824975616*zeta
    + 19816509935574590969
)
assert sp.expand(Es_num - expected_Es) == 0

R = abs(int(sp.resultant(Gs_num, Es_num, zeta)))
expected_R = 377519852626542769621117894805749147492566419200897716610331068879
assert R == expected_R

factors = [
    41,
    64217,
    72238473017,
    2679539349324345019093,
    740759498168792879433565547,
]
assert math.prod(factors) == R
assert len(set(factors)) == len(factors)
assert all(sp.isprime(p) for p in factors)
assert [p % 4 for p in factors] == [1, 1, 1, 1, 3]

pstar = factors[-1]
assert pstar == 740759498168792879433565547

# The unique inert factor is a genuine F_p intersection, not an extension-field
# artifact.  The gcd is linear and fixes the actual decimal residue zeta.
Gp = sp.Poly(Gs_num, zeta, modulus=pstar)
Ep = sp.Poly(Es_num, zeta, modulus=pstar)
common = sp.gcd(Gp, Ep).monic()
assert common.degree() == 1
zeta0 = 121854543490110025177920950
assert common.eval(zeta0) % pstar == 0

# Source common itself requires D_W=55 z^2-49 c_u^2=0, hence (55/p)=+1.
# The surviving prime passes this check, so do not overclaim emptiness.
def legendre(a, p):
    r = pow(a % p, (p - 1)//2, p)
    if r == 1:
        return 1
    if r == p - 1:
        return -1
    return 0

assert legendre(55, pstar) == 1
# It also passes the historical terminal overdepth character.
assert legendre(-26, pstar) == -1

# The fixed resultant is squarefree.  Thus on the exact source sheet there is
# no simultaneous second-order lift of both reduced cubic equations at pstar.
assert R % (pstar*pstar) != 0

print(
    "OK: source-common shared outer/descendant reuse collapses to the single "
    "fixed inert prime 740759498168792879433565547"
)
