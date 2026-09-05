#!/usr/bin/env python3
"""Certificate for external-shared-outer-fixed-templates.md.

Starting from the additive coefficient-ratio lock, a descendant-common prime
that also divides both outer rational-root cofactors must satisfy Phi(2)=0,
Phi(4)=0 and the universal descendant cubic E63=0.  The outer pair reduces to
K=3, 2K-9=0, or the irreducible quartic Q4(K).  This checker resolves all
non-3 inert first-layer triples, restores the actual defect root J, and uses a
divided-difference derivative test when J hits an outer denominator.
"""

import sympy as sp

K, z, J = sp.symbols("K z J")
R0 = K**2 - (18 + 4*z)*K + 18*z + 55
Phi = sp.expand(J*(J + 2*z)*(K - J)**2 - R0*(J + z)**2)
Phi2 = sp.expand(Phi.subs(J, 2))
Phi4 = sp.expand(Phi.subs(J, 4))
H24 = sp.factor((Phi4 - Phi2)/4)
PhiJ = sp.diff(Phi, J)

Q4 = 676*K**4 - 8004*K**3 + 34801*K**2 - 65868*K + 45964
assert sp.Poly(Q4, K, domain=sp.ZZ).is_irreducible
assert sp.factor(sp.resultant(Phi2, H24, z)) == 2*(K-3)**2*(2*K-9)*Q4

U = 2*K - 9
Lk = K**2 - 576*K + 1296
A0 = 5*K**2 + 144*K - 324
B2 = 381*K**4 - 78048*K**3 - 277520*K**2 + 2392704*K - 3074112
B1 = 189*K**4 - 126720*K**3 + 132784*K**2 + 1359360*K - 2218752
B0 = 63*K**4 - 54432*K**3 + 136672*K**2 + 239616*K - 539136
E63 = sp.expand(
    98304*U**3*A0*z**3
    - 1024*U**2*B2*z**2
    + 32*U*Lk*B1*z
    - Lk**2*B0
)

# Central sheet: Phi2/H24 already have resultant 144, hence no odd p != 3.
assert sp.resultant(Phi2.subs(K, sp.Rational(9,2)),
                    H24.subs(K, sp.Rational(9,2)), z) == 144

# K=3 sheet: Phi2 and H24 have the unique characteristic-zero root z=-3.
assert sp.gcd(sp.Poly(Phi2.subs(K,3), z), sp.Poly(H24.subs(K,3),z)).monic().as_expr() == z + 3
E3 = int(E63.subs({K:3,z:-3}))
assert sp.factorint(abs(E3)) == {3:10, 5:1, 7:2, 41:1, 173:1}

# Quartic component: the penultimate subresultant gives a linear z-reader.
subs = sp.subresultants(Phi2, H24, z)
Slin = sp.expand(subs[-2] / (2*(2*K-9)))
Az = sp.Poly(Slin,z).coeff_monomial(z)
Bz = sp.Poly(Slin,z).coeff_monomial(1)
assert sp.factor(Az) == (2*K-9)*(9*K**2-52*K+72)
assert Bz == 26*K**3-297*K**2+1052*K-1158

# On the regular quartic component substitute z=-B/A into E63 and reduce mod Q4.
Esub = sp.cancel(E63.subs(z,-Bz/Az)*Az**3)
Ered = sp.rem(sp.Poly(Esub,K,domain=sp.QQ), sp.Poly(Q4,K,domain=sp.QQ))
den, EredZ = Ered.clear_denoms(convert=True)
content, Eprim = sp.primitive(EredZ.as_expr(), K)
assert abs(int(content)) == 63
assert sp.degree(Eprim,K) == 3
Creg = abs(int(sp.resultant(Q4,Eprim,K)))
expected_fac = {
    2:50, 3:6, 7:1, 13:84, 23:6, 29:6, 31:6,
    1069:1, 11491:2, 408461:1, 39054007:1,
    5070995047:1, 24303427940647:1,
}
prod = 1
for p,e in expected_fac.items():
    assert sp.isprime(p)
    prod *= p**e
assert Creg == prod

# Only inert factors need auditing.  23/31 are leading-coefficient singular
# resultant shadows and have no actual triple root.  11491 has K=0 and is the
# nongenuine projective boundary.  The remaining actual triples are listed.
def lin_roots(poly, var, p):
    out=[]
    for f,e in sp.factor_list(sp.Poly(poly,var,modulus=p).as_expr(), modulus=p)[1]:
        P=sp.Poly(f,var,modulus=p)
        if P.degree()==1:
            a=int(P.nth(1))%p; b=int(P.nth(0))%p
            out.append((-b*pow(a,-1,p))%p)
    return out

inert = [7,23,31,11491,39054007,5070995047,24303427940647]
triples = {}
for p in inert:
    GK = sp.gcd(sp.Poly(Q4,K,modulus=p), sp.Poly(Eprim,K,modulus=p))
    for k in lin_roots(GK.as_expr(),K,p):
        Gz = sp.gcd(
            sp.gcd(sp.Poly(Phi2.subs(K,k),z,modulus=p),
                   sp.Poly(H24.subs(K,k),z,modulus=p)),
            sp.Poly(E63.subs(K,k),z,modulus=p),
        )
        for zz in lin_roots(Gz.as_expr(),z,p):
            triples[p]=(k,zz)

assert 23 not in triples and 31 not in triples
assert triples[11491] == (0,743)
assert triples[7] == (3,4)
assert triples[39054007] == (14318314,3933315)
assert triples[5070995047] == (1187202050,2738876184)
assert triples[24303427940647] == (21805672591624,9250192938088)

# Restore the actual defect root J from the universal descendant equation.
def defect_root(p,k,zz):
    num=(k*k-64*k*zz-576*k+288*zz+1296)%p
    den=(16*(2*k-9))%p
    return num*pow(den,-1,p)%p

actual = {
    7:(3,4,3),
    39054007:(14318314,3933315,2),
    5070995047:(1187202050,2738876184,4),
    24303427940647:(21805672591624,9250192938088,3),
}
for p,(k,zz,j) in actual.items():
    assert defect_root(p,k,zz)==j

# Divided-difference squeeze.  If J=2 then p|(D-C); after dividing F(2) by
# D-C, the remaining outer cofactor is a unit multiple of Phi'(2).  Likewise
# J=4 and D+C.  Hence these derivatives must vanish for shared outer reuse.
d390 = int(PhiJ.subs({K:14318314,z:3933315,J:2})) % 39054007
d507 = int(PhiJ.subs({K:1187202050,z:2738876184,J:4})) % 5070995047
assert d390 == 36568040 and d390 != 0
assert d507 == 1135701515 and d507 != 0

# The remaining generic template has J=3 (p|C), so the above outer-denominator
# derivative squeeze does not remove it.  p=7 also has J=3 and is singular.
pbig=24303427940647
assert int(PhiJ.subs({K:21805672591624,z:9250192938088,J:3})) % pbig == 807531366413

print("OK: external shared outer reuse collapses to singular 7 plus one generic fixed prime")
