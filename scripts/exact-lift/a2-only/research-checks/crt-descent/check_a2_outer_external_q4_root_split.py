#!/usr/bin/env python3
"""Certificate for outer-external-q4-root-split.md.

This checker refines the additive-locked shared-outer descendant gate.  It
splits the K=3 / central / Q4 branches, proves the Q4 generic fourth-root
formula, deletes the r=2 and r=4 natural-root collisions on inert support,
and reduces the remaining r=3 (C=0) external branch to one fixed prime.
"""

import math
import sympy as sp

K, z, r = sp.symbols("K z r")

R0 = K**2 - (18 + 4*z)*K + 18*z + 55
Phi = lambda J: sp.expand(J*(J + 2*z)*(K - J)**2 - R0*(J + z)**2)
P2, P3, P4 = Phi(2), Phi(3), Phi(4)
H24 = sp.factor((P4 - P2)/4)
Q4 = 676*K**4 - 8004*K**3 + 34801*K**2 - 65868*K + 45964

assert sp.factor(sp.resultant(P2, H24, z)) == 2*(K-3)**2*(2*K-9)*Q4
assert sp.Poly(Q4, K).is_irreducible

# Full subresultant chain.  On generic Q4 the last positive-degree member is
# linear in z.
subs = sp.subresultants(P2, P4, z)
assert [sp.degree(s, z) for s in subs] == [3, 3, 2, 1, 0]
L1 = sp.factor(subs[-2] / (64*(2*K-9)**2))
A1 = 18*K**3 - 185*K**2 + 612*K - 648
B1 = 26*K**3 - 297*K**2 + 1052*K - 1158
assert sp.expand(L1 - (A1*z + B1)) == 0
assert sp.factor(A1) == (2*K-9)*(9*K**2-52*K+72)
assert sp.factorint(abs(int(sp.resultant(Q4, A1, K)))) == {
    2:10, 23:2, 29:2, 31:2,
}
assert sp.factorint(abs(int(sp.resultant(Q4, B1, K)))) == {
    2:15, 13:1, 23:1, 29:2, 31:2,
}

# On generic Q4, z=-B1/A1 and J=3 is automatically a root too.
zlin = -B1/A1
num3 = sp.together(P3.subs(z, zlin)).as_numer_denom()[0]
assert sp.rem(sp.Poly(num3, K), sp.Poly(Q4, K)).is_zero

# Phi is monic quartic.  Once 2,3,4 are roots, Vieta gives the fourth root.
Pr = sp.Poly(Phi(r), r)
assert Pr.LC() == 1
assert -Pr.coeff_monomial(r**3) == 2*K - 2*z
rstar = 2*K - 2*z - 9
assert sp.expand(2 + 3 + 4 + rstar - (2*K - 2*z)) == 0

# Central factor is only a degree-drop artifact: at K=9/2 the two outer
# equations differ by the fixed unit 48.
kcen = sp.Rational(9,2)
assert sp.factor((P4-P2).subs(K, kcen)) == 48

# K=3 branch: common z is -3 and the actual quartic roots are 2,3,3,4.
assert sp.factor(P2.subs(K,3)) == -2*(z+3)*(3*z**2+8*z+6)
assert sp.factor(P4.subs(K,3)) == -2*(z+3)*(3*z**2+20*z+24)
assert sp.gcd(sp.Poly(P2.subs(K,3),z), sp.Poly(P4.subs(K,3),z)).monic() == sp.Poly(z+3,z).monic()
assert sp.factor(Phi(r).subs({K:3,z:-3})) == (r-4)*(r-3)**2*(r-2)

# If the actual rational root r=2 (resp. 4), Xi_- (resp. Xi_+) being paid by
# the same prime forces that root to be double, hence rstar=2 (resp. 4).
# Eliminate K on those collision lines.  The simultaneous P2/P4/Q4 support
# contains no non-3 inert odd prime.
for rv, zexpr, expected in [
    (2, K-sp.Rational(11,2), {2:12, 3:3, 137:1}),
    (4, K-sp.Rational(13,2), {2:24, 3:3, 17:1}),
]:
    resultants=[]
    for PP in (P2,P4):
        num = sp.Poly(sp.together(PP.subs(z,zexpr)).as_numer_denom()[0],K)
        resultants.append(abs(int(sp.resultant(sp.Poly(Q4,K),num,K))))
    g=math.gcd(*resultants)
    assert sp.factorint(g) == expected
    assert all(p in (2,3) or p % 4 == 1 for p in expected)

# Remaining Q4 collision r=3 means C=0.  Then H0=g(3T+a3), so the exact
# descendant F63=0 equation reduces to the following linear z gate.
FD_C0 = K**2 - 64*K*z - 672*K + 288*z + 1728
zFD = (K**2 - 672*K + 1728)/(32*(2*K-9))
assert sp.factor(FD_C0.subs(z,zFD)) == 0

# Eliminate z with FD_C0, then K with Q4.  Any common prime must divide both
# resultants, so it divides their gcd.
rs=[]
for PP in (P2,P4):
    num=sp.Poly(sp.together(PP.subs(z,zFD)).as_numer_denom()[0],K)
    rs.append(abs(int(sp.resultant(sp.Poly(Q4,K),num,K))))
g=math.gcd(*rs)
pC=24303427940647
assert sp.factorint(g) == {2:18, 7:1, 23:2, pC:1}
assert sp.isprime(pC) and pC % 4 == 3

# p=23 is central and hence impossible by the 48 difference.  p=7 is the
# fixed K=3 sheet.  The only genuinely external inert first-layer candidate
# is pC; certify its actual K,z residue and E63 compatibility.
kC=21805672591624
zC=9250192938088
assert 0 < kC < pC and 0 < zC < pC
for expr in (Q4,P2,P4,FD_C0):
    assert int(expr.subs({K:kC,z:zC})) % pC == 0

U=2*K-9
Lk=K**2-576*K+1296
A0=5*K**2+144*K-324
E2=381*K**4-78048*K**3-277520*K**2+2392704*K-3074112
E1=189*K**4-126720*K**3+132784*K**2+1359360*K-2218752
E0=63*K**4-54432*K**3+136672*K**2+239616*K-539136
E63=sp.expand(98304*U**3*A0*z**3-1024*U**2*E2*z**2+32*U*Lk*E1*z-Lk**2*E0)
assert int(E63.subs({K:kC,z:zC})) % pC == 0

# Decimal orbit itself is not restrictive: 10 is primitive mod pC.
assert sp.n_order(10,pC) == pC-1

# But this fixed candidate cannot itself propagate into the old terminal
# overdepth character, which requires (-26/p)=-1.
def legendre(a,p):
    q=pow(a%p,(p-1)//2,p)
    return -1 if q==p-1 else q
assert legendre(-26,pC) == 1

print("OK: external shared Q4 reuse reduces to root collisions; r=2/4 die and r=3 leaves one fixed pC incompatible with terminal overdepth")
