#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0313; see history/sources.json.
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
assert sp.expand(P2.subs(K,3)+2*(z+3)*(3*z**2+8*z+6)) == 0
assert sp.expand(P4.subs(K,3)+2*(z+3)*(3*z**2+20*z+24)) == 0
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

# Resolve the K=3 sheet and the coefficient-singular inert labels rather
# than assuming generic division covers them.
assert sp.factorint(abs(int(E63.subs({K:3,z:-3})))) == {
    3:10,5:1,7:2,41:1,173:1,
}
for pp in (23,31):
    roots = [kk for kk in range(pp) if int(Q4.subs(K,kk)) % pp == 0]
    points = [
        (kk,zz) for kk in roots for zz in range(pp)
        if all(int(expr.subs({K:kk,z:zz})) % pp == 0
               for expr in (P2,P4,E63))
    ]
    assert not points

# On the noncentral pC sheet, the C=0 descendant equation fixes z.  The
# complete common gcd is linear, so the displayed point is the only F_p
# point of Q4=P2=P4=FD_C0=0.
common = sp.Poly(Q4,K,modulus=pC)
for expr in (P2,P4):
    numerator = sp.together(expr.subs(z,zFD)).as_numer_denom()[0]
    common = sp.gcd(common,sp.Poly(numerator,K,modulus=pC))
assert common.degree() == 1
assert common.monic().eval(kC) % pC == 0
assert (2*kC-9) % pC != 0

# Decimal orbit itself is not restrictive: 10 is primitive mod pC.
assert sp.n_order(10,pC) == pC-1

# Correct physical transport gives H4=26[27(X+Y)]^4-[55Y]^4.
# Thus the strict terminal character is (26/p)=+1; pC fails it.
def legendre(a,p):
    q=pow(a%p,(p-1)//2,p)
    return -1 if q==p-1 else q
assert legendre(-26,pC) == 1
assert legendre(26,pC) == -1

# The P2/P4 intersection has one second-order lift.  At that lift the C=0
# descendant equation has exact depth one, so the three equations cannot
# all vanish modulo pC**2.
point = {K:kC,z:zC}
jac = sp.Matrix([
    [int(sp.diff(expr,var).subs(point)) % pC for var in (K,z)]
    for expr in (P2,P4)
])
assert int(jac.det()) % pC == 3212002394182
residual = sp.Matrix([int(expr.subs(point)) // pC % pC for expr in (P2,P4)])
digits = [int(v) % pC for v in jac.inv_mod(pC)*(-residual)]
assert digits == [17757405664989,19804620386067]
point2 = {K:kC+pC*digits[0],z:zC+pC*digits[1]}
assert all(int(expr.subs(point2)) % pC**2 == 0 for expr in (P2,P4,Q4))
assert int(FD_C0.subs(point2)) // pC % pC == 2979046557878

# Reconstruct the first-balance gates canonically from the universal cubic,
# projective Euclidean quotient and rational-root derivative.  This avoids
# assuming the false character sign, or copying an unverified parent ratio.
rho,u,v,R,J = sp.symbols("rho u v R J")
Eproj = sp.Poly(sp.expand(E63.subs({K:1/rho,z:u/rho})*rho**8),rho)
Lproj = sp.Poly(55*rho**2+18*(u-1)*rho+1-4*u-v,rho)
Qproj,_ = sp.div(Eproj,Lproj)
Q0 = sp.factor(Qproj.as_expr().subs({rho:1/K,u:z/K,v:R0/K**2}))
J0 = (K**2-64*K*z-576*K+288*z+1296)/(16*U)
PhiJR = J*(J+2*z)*(K-J)**2-R*(J+z)**2
derivative = sp.factor(sp.diff(PhiJR,J).subs({J:J0,R:R0}))
raw_lt = sp.factor(-sp.Rational(65536)*U**4*(J0+z)**2/K**6-Q0)
raw_gt = sp.factor(sp.Rational(65536)*U**3/K**6*(derivative-U*(J0+z)**2)-Q0)
num_lt,den_lt = sp.together(raw_lt).as_numer_denom()
num_gt,den_gt = sp.together(raw_gt).as_numer_denom()
cont_lt,Glt = sp.primitive(sp.Poly(num_lt,K,z).as_expr(),K,z)
cont_gt,Ggt = sp.primitive(sp.Poly(num_gt,K,z).as_expr(),K,z)
assert (cont_lt,cont_gt) == (5184,128)
assert sp.factor(den_lt) == sp.factor(den_gt) == 5**7*11**7*K**6
gl = int(Glt.subs(point)) % pC
gg = int(Ggt.subs(point)) % pC
assert (gl,gg) == (9320260449125,13624230293838)
chi = (-2*gg*pow(81*gl,-1,pC)) % pC
assert chi == 5130679962854
H4 = (26*pow(27*(chi+1),4,pC)-55**4) % pC
assert H4 == 16192417895792
assert H4 != 0

# Reconstruct all homogeneous transport blocks.  At this actual balance
# ratio the first block vanishes, while the quadratic, cubic and quartic
# primitive coefficients are all units.  Hence overdepth >4h must go
# through exact rho=sigma=tau=h, rather than any strict saturation branch.
F,Lerr,X,Y = sp.symbols("F Lerr X Y")
Ctr = sp.Rational(65536)*U**4/K**8
Qact = sp.factor(Qproj.as_expr().subs({rho:1/K,u:z/K,v:R0/K**2-Lerr}))
transport = sp.expand(Ctr*(
    PhiJR.subs({J:J0,R:R0})
    -PhiJR.subs({J:J0-F/U,R:R0-K**2*Lerr})
))
assert sp.factor(transport+Ctr*PhiJR.subs({J:J0-F/U,R:R0-K**2*Lerr})-E63/K**8) == 0
remainder = sp.Poly(sp.factor(transport-Qact*Lerr),F,Lerr)
assert remainder.total_degree() == 4
expected_den = {
    1:5**7*11**7*K**6,2:5**5*11**6*K**4,
    3:5**5*11**5*K**2,4:5**4*11**4,
}
expected_content = {1:64,2:256,3:8192,4:65536}
actual_coefficients = []
for order in range(1,5):
    block = sum(
        cc*F**ef*Lerr**el for (ef,el),cc in remainder.terms()
        if ef+el == order
    )
    parent = sp.factor(block.subs({F:K**2*Y,Lerr:X+Y}))
    num,den = sp.together(parent).as_numer_denom()
    content,primitive = sp.primitive(sp.Poly(num,X,Y,K,z).as_expr(),X,Y,K,z)
    assert content == expected_content[order]
    assert sp.factor(den) == expected_den[order]
    actual_coefficients.append(int(primitive.subs({**point,X:chi,Y:1})) % pC)
assert actual_coefficients == [0,2328839710684,18611479848870,16192417895792]

# For unequal parent depth the unit Glt/Ggt forbids linear-tail recycling.
# For equal parent depth with first recycling, chi is the value above.
# Its quartic coefficient is a unit.  Thus if the lower homogeneous block
# is strictly deeper than 4h, the actual remainder stops exactly at 4h.
# This does not delete cancellation when the lower block has depth =4h.

print("OK: shared Q4 reuse leaves fixed pC; common C=0 lift stops at depth 1; actual strict-terminal character excludes pC, and H2/H3/H4 are units and terminal recycling requires exact triple saturation")
