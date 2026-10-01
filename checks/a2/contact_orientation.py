#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0308; see history/sources.json.
"""

P = 3
UNITS = (1, 2)  # 2 == -1 mod 3


def inv(x: int) -> int:
    return pow(x, -1, P)


solutions = []
for e3 in (1, 3):
    sigma = 2 if e3 == 1 else 1  # epsilon*B = sigma*g
    for eps in UNITS:             # +1 or -1
        for g in UNITS:
            for cu in UNITS:
                for delta in UNITS:
                    # Q0 identity after f-contact and lambda=m-d:
                    # B = g + delta*c_u^{-1}.
                    B = (g + delta * inv(cu)) % P
                    if B == 0:
                        continue

                    # Exact high/low 3-depth relation.
                    if (eps * B - sigma * g) % P:
                        continue

                    # f=g*omega+c_u=0 mod3 fixes omega.
                    omega = (-cu * inv(g)) % P
                    solutions.append((e3, eps, g, cu, delta, B, omega))

assert solutions

for e3, eps, g, cu, delta, B, omega in solutions:
    if e3 == 1:
        assert eps == 1
    else:
        assert e3 == 3 and eps == 2
    assert B == (-g) % P
    assert (g * cu) % P == delta
    assert omega == (-delta) % P

# Both allowed orientations really occur in the abstract unit system; the
# theorem is an orientation selector, not an abstract impossibility claim.
assert {e3 for e3, *_ in solutions} == {1, 3}

# The historical eta=1 odd-3 survivor has k_h=3 (e3=1) on the negative slot.
# The selector excludes it immediately.
assert not any(e3 == 1 and eps == 2 for e3, eps, *_ in solutions)

# Physical binary source carrier A3=U*g*omega-K*c_u.
# H0=3, c_u=1 and c_Q*5^d=3 mod4 in the Z=1 orientation.
for e3,eps in ((1,1),(3,-1)):
    digit_mod4 = next(a for a in (1,3) if (3+eps*3*a) % 4 == 0)
    assert digit_mod4 == (3 if e3 == 1 else 1)
    for vg in (2,3):  # vg>=3 all have the same residue
        gmod8 = 4 if vg == 2 else 0
        for wmod in (1,3,5,7):
            raw_mod4 = (3*(gmod8//2)*wmod-digit_mod4) % 4
            assert raw_mod4 % 2 == 1  # v2(A3)=1 exactly
            expected = 3 if (vg == 2 and e3 == 1) or (vg >= 3 and e3 == 3) else 1
            assert raw_mod4 == expected

# Exact Euclidean identities behind the q/f/omega/g and height gcd interfaces.
import sympy as sp
K,g,omega,cu,T,a3,q5,f = sp.symbols("K g omega cu T a3 q5 f")
U=2*K-9
A3=U*g*omega-K*cu
D3=2*g*omega-cu
alpha=T*K+a3
height_gate=9*T*g*omega+D3*a3
assert sp.expand(A3-K*D3+9*g*omega) == 0
assert sp.expand(A3.subs(omega,(q5+cu)/g)-cu*(K-9)-U*q5) == 0
assert sp.expand(A3.subs(omega,(f-cu)/g)+3*cu*(K-3)-U*f) == 0
assert sp.expand(A3+K*cu-U*g*omega) == 0
assert sp.expand(D3*alpha-T*A3-height_gate) == 0

# Actual sphere/plane normalization, not the withdrawn plus transport.
# All denominators here are units for p not dividing 30 and p | q*f.
zeta,theta=sp.symbols("zeta theta")
r0=K*K-(18+4*zeta)*K+18*zeta+55
y=U*(U-zeta-theta*(K+zeta))-sp.Rational(63,16)*K*K
w=r0-(1-theta)**2*(K+zeta)**2+((1-theta)/theta)**2*zeta*zeta
q_w=-26-18*zeta+(K-9)*(K-9-4*zeta)
f_w=-26-18*zeta-3*(K-3)*(K+9+4*zeta)
assert sp.expand(w.subs(theta,1)-q_w) == 0
assert sp.expand(w.subs(theta,-1)-f_w) == 0
assert sp.cancel((w-w.subs(theta,1))/(theta-1)).as_numer_denom()[1] == theta**2
assert sp.cancel((w-w.subs(theta,-1))/(theta+1)).as_numer_denom()[1] == theta**2
for kval,tval,yval in ((9,1,-sp.Rational(3**4*47,16)),
                       (3,-1,-sp.Rational(3**4*7,16))):
    point={K:kval,zeta:-sp.Rational(9,2),theta:tval}
    assert w.subs(point) == 55
    assert y.subs(point) == yval
    assert int(yval.p)*pow(int(yval.q),-1,11) % 11 == (2 if kval == 9 else 1)
    assert int(yval.q) % 11 != 0
assert sp.factorint(55) == {5:1,11:1}
assert w.subs({K:0,zeta:0,theta:-1}) % 3 == 1

# Without L23 saturation, source/denominator/descendant support is still fixed.
assert sp.expand((y-w).subs({K:9,theta:1})) == -sp.Rational(4687,16)
assert sp.expand(y.subs({K:3,theta:-1})) == -sp.Rational(567,16)
assert sp.factorint(4687) == {43:1,109:1}
assert sp.factorint(567) == {3:4,7:1}
J=sp.symbols("J")
phi=J*(J+2*zeta)*(K-J)**2-r0*(J+zeta)**2
q_point={K:9,zeta:-sp.Rational(13,9)}
assert r0.subs(q_point) == 0
for jval,wanted in ((2,-sp.Rational(784,9)),(4,sp.Rational(1000,9))):
    val=phi.subs(q_point).subs(J,jval)
    assert val == wanted
    assert all(int(val.p) % p != 0 and int(val.q) % p != 0 for p in (43,109))

# For inert height p | A3,Wq, the proof first establishes p not dividing omega.
# Only then may zeta=-K and theta=U/K be used as a local unit substitution.
YA=11*K*K-240*K+432
WA=21*K**4-342*K**3+2002*K*K-4896*K+4455
assert sp.cancel(y.subs({zeta:-K,theta:U/K})-sp.Rational(3,16)*YA) == 0
assert sp.cancel(w.subs({zeta:-K,theta:U/K})-WA/U**2) == 0
bez_y=1999434528*K**3-28611870921*K**2+133944686430*K-202282077546
bez_w=20781450135-1047322848*K
height_result=3**10*7*12569471
assert sp.expand(bez_y*YA+bez_w*WA) == height_result
assert sp.resultant(YA,WA,K) == height_result
assert sp.isprime(12569471) and 12569471 < 2**64 and 12569471 % 4 == 3
for p,kval in ((7,3),(12569471,12569471-267471)):
    common=sp.gcd(sp.Poly(YA,K,modulus=p),sp.Poly(WA,K,modulus=p)).monic()
    assert common.degree() == 1
    assert int(common.all_coeffs()[1]) % p == (-kval) % p
    assert kval % p != 0 and (2*kval-9) % p != 0
    residues=[int(phi.subs({K:kval,zeta:-kval,J:jval})) % p for jval in (2,4)]
    assert residues == ([0,0] if p == 7 else [12143998,4798615])

# A3 cannot reuse the unique genuine external shared-outer pC label.
# Its unique root is proved independently by outer_root.
pC=24303427940647
kC,zC=21805672591624,9250192938088
uC=(2*kC-9) % pC
jC=(kC*kC-64*kC*zC-576*kC+288*zC+1296)*pow(16*uC,-1,pC) % pC
thetaC=(jC+zC)*pow(kC+zC,-1,pC) % pC
assert thetaC == 18367788003561
yC=(uC*(uC-zC-thetaC*(kC+zC))-63*kC*kC*pow(16,-1,pC)) % pC
assert yC == 0
r0C=(kC*kC-(18+4*zC)*kC+18*zC+55) % pC
wC=(r0C-(1-thetaC)**2*(kC+zC)**2+((1-thetaC)*pow(thetaC,-1,pC))**2*zC*zC) % pC
assert wC == 0
assert (uC-kC*thetaC) % pC == 11023269555785

print("OK: f-contact orientation, A3 parity/gcd interfaces, saturated overlap <= 11, source/height payer overlap bounds, and pC separation")
