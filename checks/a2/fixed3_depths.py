#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0292; see history/sources.json.
"""

import runpy
from pathlib import Path
import sympy as sp

K, zeta, J, R = sp.symbols("K zeta J R")
F, Lerr = sp.symbols("F Lerr")
X, Y = sp.symbols("X Y")
r, u, v = sp.symbols("r u v")
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
R0 = K**2 - (18 + 4*zeta)*K + 18*zeta + 55
J0 = (K**2 - 64*K*zeta - 576*K + 288*zeta + 1296)/(16*U)

Phi = J*(J + 2*zeta)*(K - J)**2 - R*(J + zeta)**2
PhiJ = sp.diff(Phi, J)
PhiJ0 = sp.factor(PhiJ.subs({J: J0, R: R0}))
Ctr = sp.Rational(65536)*U**4/K**8

Eproj = sp.Poly(sp.expand(E63.subs({K: 1/r, zeta: u/r})*r**8), r)
Lproj = sp.Poly(55*r**2 + 18*(u - 1)*r + 1 - 4*u - v, r)
Qproj, _ = sp.div(Eproj, Lproj)
Q0 = sp.factor(Qproj.as_expr().subs({r: 1/K, u: zeta/K, v: R0/K**2}))

C_lt = sp.factor(-sp.Rational(65536)*U**4*(J0 + zeta)**2/K**6)
C_gt = sp.factor(
    sp.Rational(65536)*U**3/K**6
    * (PhiJ0 - U*(J0 + zeta)**2)
)
num_lt, _ = sp.together(C_lt - Q0).as_numer_denom()
num_gt, _ = sp.together(C_gt - Q0).as_numer_denom()
c_lt, Glt_expr = sp.primitive(
    sp.Poly(sp.expand(num_lt), K, zeta).as_expr(), K, zeta
)
c_gt, Ggt_expr = sp.primitive(
    sp.Poly(sp.expand(num_gt), K, zeta).as_expr(), K, zeta
)
assert c_lt == 5184
assert c_gt == 128
Glt = sp.Poly(Glt_expr, K, zeta, domain=sp.ZZ)
Ggt = sp.Poly(Ggt_expr, K, zeta, domain=sp.ZZ)

Qact = sp.factor(
    Qproj.as_expr().subs({r: 1/K, u: zeta/K, v: R0/K**2 - Lerr})
)
transport = sp.expand(
    Ctr * (
        Phi.subs({J: J0, R: R0})
        - Phi.subs({J: J0 - F/U, R: R0 - K**2*Lerr})
    )
)
assert sp.factor(transport+Ctr*Phi.subs({J:J0-F/U,R:R0-K**2*Lerr})-E63/K**8) == 0
M = sp.factor(transport - Qact*Lerr)
PM = sp.Poly(M, F, Lerr)

Hprim = {}
for n in range(1, 5):
    block = sp.Integer(0)
    for (ef, el), coeff in PM.terms():
        if ef + el == n:
            block += coeff*F**ef*Lerr**el
    hrat = sp.factor(block.subs({F: K**2*Y, Lerr: X + Y}))
    num, _ = sp.together(hrat).as_numer_denom()
    _, prim = sp.primitive(
        sp.Poly(sp.expand(num), X, Y, K, zeta).as_expr(),
        X, Y, K, zeta,
    )
    Hprim[n] = sp.Poly(prim, X, Y, K, zeta, domain=sp.ZZ)

H2 = Hprim[2]
H3 = Hprim[3]


def vp3(n: int) -> int:
    n = abs(int(n))
    assert n
    out = 0
    while n % 3 == 0:
        n //= 3
        out += 1
    return out


kk, zz, yy, xx = sp.symbols("kk zz yy xx")


def initial_form_2(poly, vk, vz, depth):
    out = 0
    for (ik, iz), coeff in poly.terms():
        val = vp3(coeff) + ik*vk + iz*vz
        if val == depth:
            unit = (int(coeff) // 3**vp3(coeff)) % 3
            out += unit*kk**ik*zz**iz
    return sp.Poly(sp.expand(out), kk, zz, modulus=3).as_expr()


def initial_form_4(poly, vx, vy, vk, vz, depth):
    out = 0
    for (ix, iy, ik, iz), coeff in poly.terms():
        val = vp3(coeff) + ix*vx + iy*vy + ik*vk + iz*vz
        if val == depth:
            unit = (int(coeff) // 3**vp3(coeff)) % 3
            out += unit*xx**ix*yy**iy*kk**ik*zz**iz
    return sp.Poly(sp.expand(out), xx, yy, kk, zz, modulus=3).as_expr()


# ---------------------------------------------------------------------------
# Channel A: v3(K)=1, v3(zeta)>=2, generic v3(Y)=2.
# ---------------------------------------------------------------------------

A_Ggt = initial_form_2(Ggt, 1, 2, 4)
A_H2 = initial_form_4(H2, 0, 2, 1, 2, 6)
A_H3 = initial_form_4(H3, 0, 2, 1, 2, 6)

assert sp.Poly(A_Ggt + kk**4, kk, zz, modulus=3).is_zero
assert sp.Poly(
    A_H2 - (xx*yy*kk**4 - yy**2*kk**2),
    xx, yy, kk, zz, modulus=3,
).is_zero
assert sp.Poly(
    A_H3 - xx*yy**2*kk**2,
    xx, yy, kk, zz, modulus=3,
).is_zero

# Let s=(-1)^m.  B^2=(2^(M+m+1)c_u g)^2 is 1 mod 3.
# Correctly directed quadratic transport changes the depth-six form.
ss = sp.symbols("ss")
A_N3 = sp.expand(yy*kk**4+2*ss*A_H2+2*A_H3)

# Endpoint §16.58 gives a2 == 0 mod3, hence That_2 == s mod3;
# since Y is divisible by 9, x == s.  If f=g*omega+c_u is a unit mod3,
# its two unit summands must agree, so c_u == g*omega.  The exact identity
# omega B_Delta = f((2K-9)T-a3)-3c_u(K-3)T then gives
# Y/9 == 2s mod3.
for s in (1, 2):
    for k in (1, 2):
        value = int(A_N3.subs({ss: s, xx: s, yy: 2*s % 3, kk: k})) % 3
        assert value == 0

# Exhaust the unit implication f != 0 => c_u == g*omega and the normalized
# Y/9 formula y/s = 1 + g*c_u/omega = 2.
for g in (1, 2):
    for omega in (1, 2):
        for cu in (1, 2):
            fmod = (g*omega + cu) % 3
            if fmod:
                assert cu == (g*omega) % 3
                ratio = (1 + g*cu*pow(omega, -1, 3)) % 3
                assert ratio == 2

# The historical depth-six assertion fails: the corrected coefficient is zero.


# ---------------------------------------------------------------------------
# Channel B: v3(zeta)=1, v3(K)>=2.
# Generic sector: v3(2K-9)=2.  Write K=9k after extracting the
# guaranteed 3^2; then k can be 0 or 1 mod3, while k=2 is exactly the
# extra-central branch.  If 3∤f, one has v3(Y)=3.
# ---------------------------------------------------------------------------

B_Glt = initial_form_2(Glt, 2, 1, 6)
B_Ggt = initial_form_2(Ggt, 2, 1, 7)
B_H2 = initial_form_4(H2, 0, 3, 2, 1, 10)
B_H3 = initial_form_4(H3, 0, 3, 2, 1, 10)

assert sp.Poly(
    B_Glt - zz**2*(kk - 1), kk, zz, modulus=3
).is_zero
assert sp.Poly(
    B_Ggt + zz*(kk + 1)*(kk**2 - kk + 1),
    kk, zz, modulus=3,
).is_zero

# Assemble the exact N3 recursion at depth 10:
# h_bal = 81 X G_< + 2 Y G_>
# N2 = 64*5^m B^2*h_bal + 2^(2M+10)*5^2*11*T^6 H2
# N3 = 5^m B^2*N2 + 2^(4M+17)*5^2*11^2*T^6 H3.
# Mod 3, B^2=T=1, 5^m=s, 11=-1, and the last 2-power is -1.
hbal_B = xx*zz**2*(kk - 1) + yy*zz*(kk + 1)*(kk**2 - kk + 1)
B_N3_raw = sp.expand(hbal_B + 2*ss*B_H2 + 2*B_H3)

for s in (1, 2):
    expr = sp.Poly(
        sp.expand(B_N3_raw.subs({ss: s, xx: s})),
        kk, zz, yy, modulus=3,
    ).as_expr()
    assert sp.Poly(expr, kk, zz, yy, modulus=3).is_zero

# If the central factor has exact depth 2, then 2k-1 is a unit, i.e.
# k is 0 or 1 mod3 (k=0 simply means that K was actually deeper than 3^2).
# If f is a unit, c_u=g*omega mod3 and the normalized Dhat formula gives
# y=s(2k-1)z.  The entire corrected depth-ten coefficient vanishes.
for s in (1, 2):
    for z in (1, 2):
        for k in (0, 1):
            y = s*(2*k-1)*z % 3
            assert y != 0
            expr = int(B_N3_raw.subs({ss:s,xx:s,yy:y,kk:k,zz:z}))
            assert expr % 3 == 0

# The higher depth and parity remain unknown.  The elementary central-depth
# equivalence itself is retained.
for k in (0, 1, 2):
    central_deep = (2*k - 1) % 3 == 0
    assert central_deep == (k == 2)

# Exact source identity used above.
f, omega, g, cu, T, a3 = sp.symbols("f omega g cu T a3")
Wq = (T*K + a3)/omega
lhs = sp.expand(omega*(g*((2*K-9)*T-a3)-cu*Wq))
rhs = sp.expand(f*((2*K-9)*T-a3)-3*cu*(K-3)*T)
assert sp.expand(lhs.subs(f, g*omega+cu)-rhs.subs(f, g*omega+cu)) == 0


# ---------------------------------------------------------------------------
# Exact sphere/plane normalization; all coefficients refer to one N3 parent.
# ---------------------------------------------------------------------------
# Set theta=c_u/(g*omega), a=2^m*c_u^2*g^2*T, t=2^(2M+2).
# Then A=5^m*B^2=t*a, C=70400*t, D=24780800*t^2 exactly.
# The sphere and source rows are
#   H0^2-g^2*a3^2 = c_Q^2*5^(2d)*N0,
#   H0=c_u*T*(K+zeta)/omega, c_Q*q=Q0,
#   5^lambda*q=g*omega-c_u, lambda+d=m.
# Dividing 5^m*Q0^2*N0 by a therefore yields the expression audited below.
theta, kk, zz, hh = sp.symbols("theta kk zz hh")
source_norm = (
    (g*omega-cu)**2/(cu**2*g**2)
    * (cu**2*(K+zeta)**2/omega**2-g**2*zeta**2)
)
norm_target = (1-theta)**2*(K+zeta)**2 - ((1-theta)/theta)**2*zeta**2
assert sp.factor(source_norm-norm_target.subs(theta,cu/(g*omega))) == 0

ynorm = sp.expand(U*(U-zeta-theta*(K+zeta))-sp.Rational(63,16)*K**2)
wnorm = sp.expand(R0-norm_target)
xnorm = sp.expand(wnorm-ynorm)
# The same normalization recovers the actual root and decimal coefficient.
# Thus xnorm/ynorm are not free projective parents with unrelated budgets.
Jsource = theta*(K+zeta)-zeta
Rsource = norm_target
assert sp.factor(J0-ynorm/U-Jsource) == 0
assert sp.factor(R0-wnorm-Rsource) == 0
assert sp.factor(Phi.subs({J:Jsource,R:Rsource})) == 0
# Y_d/a=F63/(g*T), while (X_d+Y_d)/a=That_2/a.
F63_source = U*(g*T*(U-zeta)-cu*T*(K+zeta)/omega)-sp.Rational(63,16)*g*T*K**2
assert sp.factor(F63_source/(g*T)-ynorm.subs(theta,cu/(g*omega))) == 0
assert 2**8*25*11 == 70400
assert 2**13*25*11**2 == 24780800

E3norm = (
    64*(81*X*Glt.as_expr()+2*Y*Ggt.as_expr())
    +70400*H2.as_expr()+24780800*H3.as_expr()
)
# N3 = T^6*t^2*a^3*theta^(-6)*P3.  The prefactor is a 3-unit.
P3 = sp.Poly(
    sp.expand(theta**6*E3norm.subs({X:xnorm,Y:ynorm})),
    K,zeta,theta,domain=sp.ZZ,
)
assert len(P3.terms()) == 350


def exact_initial_form(ksub, zsub, tsub, depth):
    poly = sp.Poly(
        sp.expand(P3.as_expr().subs({K:ksub,zeta:zsub,theta:tsub})),
        kk,zz,hh,domain=sp.ZZ,
    )
    assert min(vp3(cc) for _,cc in poly.terms()) == depth
    return sp.Poly(poly.as_expr()/3**depth,kk,zz,hh,modulus=3).as_expr()


# a2-shallow, f-unit: theta=1 mod3.  Every k-unit gives depth exactly 8.
A8 = exact_initial_form(3*kk,9*zz,1+3*hh,8)
assert sp.Poly(A8+kk**8,kk,zz,hh,modulus=3).is_zero
for kmod in (1,2):
    assert int(A8.subs(kk,kmod)) % 3 != 0

# a3-shallow, f-unit: z-unit; K/9 may have any residue, including central.
B12 = exact_initial_form(9*kk,3*zz,1+3*hh,12)
assert sp.Poly(B12-((kk+1)**4*zz**4+1),kk,zz,hh,modulus=3).is_zero
for kmod in (0,1,2):
    for zmod in (1,2):
        assert int(B12.subs({kk:kmod,zz:zmod})) % 3 != 0

# a3-shallow, f-contact: theta=-1 mod3, with constant depth-twelve digit.
B12_contact = exact_initial_form(9*kk,3*zz,-1+3*hh,12)
assert sp.Poly(B12_contact-1,kk,zz,hh,modulus=3).is_zero

# a2-shallow, f-contact: odd depth 9 iff this coefficient is nonzero.
# Vanishing leaves depth >=10 with unresolved parity, not an exclusion.
A9_contact = exact_initial_form(3*kk,9*zz,-1+3*hh,9)
assert sp.Poly(
    A9_contact-kk**7*(kk*(hh-1)+1),kk,zz,hh,modulus=3,
).is_zero

# The vanishing digit has an actual positive source carrier, not a free h.
# A3=U*g*omega-K*c_u=5^lambda*q*U+c_u*(K-9)>0 on the endpoint.
A3source = U*g*omega-K*cu
Bdelta_source = g*(U*T-a3)-cu*(T*K+a3)/omega
assert sp.expand(omega*Bdelta_source-T*A3source+(g*omega+cu)*a3) == 0
q5 = sp.symbols("q5")
assert sp.expand(A3source.subs(omega,(q5+cu)/g)-q5*U-cu*(K-9)) == 0
assert sp.expand(
    A3source.subs({K:3*kk,cu:(-1+3*hh)*g*omega})/(9*g*omega)
    +kk*(hh-1)+1
) == 0

# In the collision branch v3(A3)>=3, write A3/(g*omega)=27*r.
# Here hh denotes this r.  Only the k-unit is cleared from the substitution.
theta_collision = 2-3/kk-9*hh/kk
collision_poly = sp.Poly(
    sp.expand(kk**12*P3.as_expr().subs({K:3*kk,zeta:9*zz,theta:theta_collision})),
    kk,zz,hh,domain=sp.ZZ,
)
assert min(vp3(cc) for _,cc in collision_poly.terms()) == 10
collision_initial = sp.Poly(
    collision_poly.as_expr()/3**10,kk,zz,hh,modulus=3,
).as_expr()
assert sp.Poly(
    collision_initial-kk**18*(zz*(kk-1)-kk**2-kk*hh-1),
    kk,zz,hh,modulus=3,
).is_zero
for kmod in (1,2):
    for zmod in (0,1,2):
        for rmod in (0,1,2):
            value = int(collision_initial.subs({kk:kmod,zz:zmod,hh:rmod})) % 3
            assert value == (zmod*(kmod-1)-kmod*rmod+1) % 3

# Two explicit unbounded source slices with exact even depth 10.
# v3(A3)>=4 means r=0 mod3.  With k=1 there is no z exception;
# with k=2 the sole next residue is z=2, where parity remains unresolved.
for zmod in (0,1,2):
    assert int(collision_initial.subs({kk:1,zz:zmod,hh:0})) % 3 != 0
for zmod in (0,1):
    assert int(collision_initial.subs({kk:2,zz:zmod,hh:0})) % 3 != 0
assert int(collision_initial.subs({kk:2,zz:2,hh:0})) % 3 == 0

# On the actual k=1 source word, the only depth-ten zero sheet is r=1.
# Resolve its next coefficient from the full integer polynomial.  The
# factor k^12 remains a 3-unit, so it does not change any valuation.
jj, rr = sp.symbols("jj rr")
collision11_poly = sp.Poly(
    sp.expand(collision_poly.as_expr().subs({kk:1+3*jj,hh:1+3*rr})),
    jj,zz,rr,domain=sp.ZZ,
)
assert min(vp3(cc) for cc in collision11_poly.coeffs()) == 11
collision11_initial = sp.Poly(
    collision11_poly.as_expr()/3**11,jj,zz,rr,modulus=3,
)
assert sp.Poly(
    collision11_initial.as_expr()-(1-rr+zz*(jj-1)),
    jj,zz,rr,modulus=3,
).is_zero

# The new source/height/descendant 7-sheet uses this same actual P3.
# This is an exact full-coefficient expansion, not a parity guess after
# its first digit vanishes.  At p=7 all prefactors T,t,a,theta are units.
sheet7_poly = sp.Poly(
    sp.expand(P3.as_expr().subs({K:3+7*kk,zeta:4+7*zz,theta:-1+7*hh})),
    kk,zz,hh,domain=sp.ZZ,
)
assert all(cc % 7**2 == 0 for cc in sheet7_poly.coeffs())
assert any(cc % 7**3 != 0 for cc in sheet7_poly.coeffs())
sheet7_initial = sp.Poly(sheet7_poly.as_expr()/7**2,kk,zz,hh,modulus=7)
assert sp.Poly(
    sheet7_initial.as_expr()-hh**2+2*(kk+zz+1)**2,
    kk,zz,hh,modulus=7,
).is_zero

# Resolve a genuine zero of the first source7 digit using the complete
# original-source lift.  Its unit Jacobian gives infinite local source
# extensions; no decimal candidate or independent budget is asserted.
eta2_data = runpy.run_path(str(Path(__file__).parent / "contact_slots.py"))
source7_lift = eta2_data["source7_lift"]
odd7_counts = []
mod = 7**4
for cq,kh in ((31,51),(527,3)):
    for m in range(14,294,21):  # complete m mod294 with 7|m, m=2 mod3
        count = 0
        T,N = pow(10,m,mod),pow(10,2*m-2,mod)
        for dc in range(7):
            for dg in range(7):
                cu,g,om,a2,a3 = source7_lift(m,cq,kh,dc,dg)
                k = (9*N+10*a2) % mod
                z = a3*pow(T,-1,mod) % mod
                th = cu*pow(g*om,-1,mod) % mod
                us = (2*k-9) % mod
                rs0 = (k*k-(18+4*z)*k+18*z+55) % mod
                rs = ((1-th)**2*(k+z)**2
                      -((1-th)*pow(th,-1,mod))**2*z*z) % mod
                ys = (us*(us-z-th*(k+z))-63*k*k*pow(16,-1,mod)) % mod
                ws = (rs0-rs) % mod
                source_a = (us*g*om-k*cu) % mod
                wq = ((g*g*kh-2*5*cq*a2)*pow(2*cu,-1,mod)) % mod
                outer = [(jj0*(jj0+2*z)*(k-jj0)**2-rs*(jj0+z)**2) % mod
                         for jj0 in (2,4)]
                gates = (source_a,wq,ws,ys,*outer)
                assert all(v % 7 == 0 for v in gates)
                kp = [pow(k,i,mod) for i in range(21)]
                zp = [pow(z,i,mod) for i in range(21)]
                tp = [pow(th,i,mod) for i in range(21)]
                pv = sum(int(c)*kp[ik]*zp[iz]*tp[it]
                         for (ik,iz,it),c in P3.terms()) % mod
                assert pv % 7**3 == 0  # the first source7 digit vanishes
                if all(v % 49 != 0 for v in gates) and pv != 0:
                    count += 1
        assert count > 0
        odd7_counts.append(count)
assert len(odd7_counts) == 28
assert min(odd7_counts) == 12 and max(odd7_counts) == 17

print(
    "OK: corrected exact sphere/plane gives a2-shallow f-unit depth 8 and "
    "all a3-shallow depth 12; a2-shallow f-contact is the remaining fixed-3 "
    "parity channel; its exact source A3 controls depth 9 and the next "
    "depth-10/11 collision digits; actual source7 initial form is h^2-2(k+z+1)^2; "
    "source7 zero sheet has exact odd-depth3 local lifts"
)
