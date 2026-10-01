#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0314; see history/sources.json.
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
# Primitive content removal does not choose a sign.  The document uses the
# positive-leading Gs normalization; the resultant support is sign invariant.
if sp.Poly(Gs_num, zeta).LC() < 0:
    Gs_num = -Gs_num
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

# Full Lucas n-1 certificates.  Each row gives a witness a and the complete
# factorization of n-1; all factors are certified recursively down to 2.
# No probable-prime call participates in the prime-support conclusion.
LUCAS = {
    3:(2,{2:1}),5:(2,{2:2}),7:(3,{2:1,3:1}),
    11:(2,{2:1,5:1}),13:(2,{2:2,3:1}),17:(3,{2:4}),
    19:(2,{2:1,3:2}),23:(5,{2:1,11:1}),29:(2,{2:2,7:1}),
    37:(2,{2:2,3:2}),41:(6,{2:3,5:1}),43:(3,{2:1,3:1,7:1}),
    59:(2,{2:1,29:1}),73:(5,{2:3,3:2}),97:(5,{2:5,3:1}),
    101:(2,{2:2,5:2}),109:(6,{2:2,3:3}),191:(19,{2:1,5:1,19:1}),
    211:(2,{2:1,3:1,5:1,7:1}),281:(3,{2:3,5:1,7:1}),
    349:(2,{2:2,3:1,29:1}),431:(7,{2:1,5:1,43:1}),
    821:(2,{2:2,5:1,41:1}),1063:(3,{2:1,3:2,59:1}),
    1151:(17,{2:1,5:2,23:1}),3449:(3,{2:3,431:1}),
    5051:(2,{2:1,5:2,101:1}),6113:(3,{2:5,191:1}),
    6569:(3,{2:3,821:1}),9929:(3,{2:3,17:1,73:1}),
    31891:(2,{2:1,3:1,5:1,1063:1}),64217:(3,{2:3,23:1,349:1}),
    131381:(2,{2:2,5:1,6569:1}),1091017:(10,{2:3,3:3,5051:1}),
    220239247:(5,{2:1,3:1,1151:1,31891:1}),
    15038046383:(5,{2:1,37:1,97:1,211:1,9929:1}),
    72238473017:(3,{2:3,41:1,220239247:1}),
    96006239837:(2,{2:2,13:1,43:1,59:1,211:1,3449:1}),
    25739721710998121:(3,{2:3,5:1,7:1,6113:1,15038046383:1}),
    2679539349324345019093:(6,{2:2,3:3,7:1,281:1,131381:1,96006239837:1}),
    740759498168792879433565547:(2,{2:1,11:2,109:1,1091017:1,25739721710998121:1}),
}
certified = {2}

def verify_lucas(n):
    if n in certified:
        return
    a,fs = LUCAS[n]
    assert math.prod(q**e for q,e in fs.items()) == n-1
    for q,e in fs.items():
        assert 2 <= q < n and e > 0
        verify_lucas(q)
    assert pow(a,n-1,n) == 1
    assert all(math.gcd(pow(a,(n-1)//q,n)-1,n) == 1 for q in fs)
    certified.add(n)

for p in factors:
    verify_lucas(p)
assert len(certified) == 42
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
# Correct physical quartic transport requires (26/p)=+1, which it passes.
assert legendre(-26, pstar) == -1
assert legendre(26, pstar) == 1

# The fixed resultant is squarefree.  Thus on the exact source sheet there is
# no simultaneous second-order lift of both reduced cubic equations at pstar.
assert R % (pstar*pstar) != 0

print(
    "OK: source-common shared outer/descendant reuse collapses to the single "
    "fixed inert prime 740759498168792879433565547"
)
