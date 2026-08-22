#!/usr/bin/env python3
"""Certificate for outer-cofactor-reuse-gate.md.

In the dangerous Z=1 (mod 4) odd-3 orientation, the adjacent rational-root
values F(2),F(4) are 3-adic units.  Since D-C|F(2), D+C|F(4) and 3∤D,
this forces 3|C and makes the outer cofactors Xi_-,Xi_+ 3-adic units.
Their common mod-2^m square class is Y, hence both are 3 mod 4.

If one genuine non-3 inert prime divides both outer cofactors, it divides
F(2),F(4).  Eliminating their common coefficient ratio gives a compact cubic
G_pm(K,zeta).  Intersecting G_pm with the universal descendant cubic E_63
produces one primitive irreducible degree-30 K-gate.

For the three fixed descendant-common old-pool labels, use their actual
first-layer K residues directly.  The compact cubic G_pm(K,zeta) has no root
in F_p for (p,K)=(7,1),(31,9),(179,71).  Thus none of the three fixed labels
can simultaneously pay both outer-cofactor parities.  Note that P30(1)=0 mod7
only signals an algebraic-closure common root and is not sufficient for an
actual decimal residue zeta in F_7.
"""

import sympy as sp

J,T,a,K,A,B = sp.symbols("J T a K A B")
D,C,b2,Q,N0 = sp.symbols("D C b2 Q N0", integer=True)
zeta = sp.symbols("zeta")

# Rational-root quartic, with A=b2^2*T and B=Q^2*N0.
f = lambda j: sp.expand(j*(T*j+2*a)*(K-j)**2)
h = lambda j: sp.expand((T*j+a)**2)
F = lambda j: sp.expand(A*f(j)-B*h(j))

# Odd-3 orientation: T,b2,D are 3-units, while K,a,N0 are divisible by 3
# (indeed 9|N0).  Mod 3 the B*h term vanishes and the first term is b2^2.
k0,z0,n0,b0,q0,t0 = sp.symbols("k0 z0 n0 b0 q0 t0")
subs3 = {K:3*k0, a:3*z0, N0:9*n0, A:b0**2*t0, B:q0**2*9*n0, T:t0}
F2m = sp.Poly(sp.expand(F(2).subs(subs3)), b0,t0,k0,z0,n0,q0, modulus=3)
F4m = sp.Poly(sp.expand(F(4).subs(subs3)), b0,t0,k0,z0,n0,q0, modulus=3)
assert sp.Poly(F2m.as_expr().subs(t0,1)-b0**2, b0,k0,z0,n0,q0, modulus=3).is_zero
assert sp.Poly(F4m.as_expr().subs(t0,1)-b0**2, b0,k0,z0,n0,q0, modulus=3).is_zero

# If D is a 3-unit, the simultaneous conditions 3∤(D-C),3∤(D+C)
# force C=0 mod3.
for d in (1,2):
    good=[]
    for c in (0,1,2):
        if (d-c)%3 and (d+c)%3:
            good.append(c)
    assert good == [0]

# In Z=1, Y=-Z=3 mod4.  The common denominator-wide square class then
# forces both outer odd cofactors to be 3 mod4 (m>=2 in the endpoint cone).
for odd_square in (1,3):
    assert (odd_square*odd_square)%4 == 1
    assert (3*odd_square*odd_square)%4 == 3

# Common outer-prime elimination: F(2)=F(4)=0 and A a unit imply
# f(2)h(4)-f(4)h(2)=0.
cross = sp.factor(f(2)*h(4)-f(4)*h(2))
Graw = sp.factor(cross/4)
Gpm = sp.factor(Graw.subs(a,zeta*T)/T**3)
expected = (
    -K**2*zeta**3 - 3*K**2*zeta**2
    + 12*K*zeta**3 + 60*K*zeta**2 + 96*K*zeta + 64*K
    - 28*zeta**3 - 156*zeta**2 - 288*zeta - 192
)
assert sp.expand(Gpm-expected) == 0

# Universal descendant cubic.
U=2*K-9
Lk=K**2-576*K+1296
A0=5*K**2+144*K-324
B2=381*K**4-78048*K**3-277520*K**2+2392704*K-3074112
B1=189*K**4-126720*K**3+132784*K**2+1359360*K-2218752
B0=63*K**4-54432*K**3+136672*K**2+239616*K-539136
E63=sp.expand(
    98304*U**3*A0*zeta**3
    -1024*U**2*B2*zeta**2
    +32*U*Lk*B1*zeta
    -Lk**2*B0
)

res = sp.resultant(E63, expected, zeta)
content, primitive = sp.primitive(sp.Poly(res,K).as_expr(), K)
assert abs(int(content)) == 1
P30 = sp.Poly(primitive,K,domain=sp.ZZ)
assert P30.degree() == 30
assert len(P30.terms()) == 31
assert P30.is_irreducible

# Historical fixed common labels and their actual first-layer K residues.
fixed = [(7,1),(31,9),(179,71)]
for p,k in fixed:
    roots=[zz for zz in range(p) if int(expected.subs({K:k,zeta:zz})) % p == 0]
    assert roots == []

# The degree-30 elimination already excludes the target labels 31/179.
assert int(P30.eval(9)) % 31 == 16
assert int(P30.eval(71)) % 179 == 63

# For p=7, P30(1)=0 only because the common root exists over an extension
# field; the actual zeta residue lies in F_7, and the direct root audit above
# is the decisive condition.
assert int(P30.eval(1)) % 7 == 0

print("OK: Z=1 forces two non-3 outer cofactors; fixed 7/31/179 cannot pay both simultaneously")
