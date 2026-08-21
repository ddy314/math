#!/usr/bin/env python3
"""Certificate for A2 fixed-3 terminal-spill reduction.

This checker reconstructs the canonical descendant transport polynomials and
extracts the first nonzero 3-adic forms in the two odd fixed-3 endpoint
channels.  It proves that the third-order primitive parent has even 3-depth
in the generic sector; failure is forced back to an old fixed sheet:
f == 0 (mod 3), or, in the a3-shallow channel, extra central depth
v_3(2K-9) >= 3.
"""

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
        Phi.subs({J: J0 + F/U, R: R0 + K**2*Lerr})
        - Phi.subs({J: J0, R: R0})
    )
)
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
    A_H2 - (yy**2*kk**2 - xx*yy*kk**4),
    xx, yy, kk, zz, modulus=3,
).is_zero
assert sp.Poly(
    A_H3 - xx*yy**2*kk**2,
    xx, yy, kk, zz, modulus=3,
).is_zero

# Let s=(-1)^m.  B^2=(2^(M+m+1)c_u g)^2 is 1 mod 3.
# From N2/N3 recursion:
# N3/3^6 = y*k^2*(x+s)*(2y+s*k^2) mod 3.
ss = sp.symbols("ss")
A_N3 = yy*kk**2*(xx + ss)*(2*yy + ss*kk**2)

# Endpoint §16.58 gives a2 == 0 mod3, hence That_2 == s mod3;
# since Y is divisible by 9, x == s.  If f=g*omega+c_u is a unit mod3,
# its two unit summands must agree, so c_u == g*omega.  The exact identity
# omega B_Delta = f((2K-9)T-a3)-3c_u(K-3)T then gives
# Y/9 == 2s mod3.
for s in (1, 2):
    for k in (1, 2):
        value = int(A_N3.subs({ss: s, xx: s, yy: 2*s % 3, kk: k})) % 3
        assert value != 0

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

# Thus channel A has v3(N3)=6 unless 3|f.


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
    target = -yy*(kk**2 - kk + 1)*(zz*(kk + 1) - s*yy)
    assert sp.Poly(expr - target, kk, zz, yy, modulus=3).is_zero

# If the central factor has exact depth 2, then 2k-1 is a unit, i.e.
# k is 0 or 1 mod3 (k=0 simply means that K was actually deeper than 3^2).
# If f is a unit, c_u=g*omega mod3 and the normalized Dhat formula gives
# y=s(2k-1)z.  Substitution leaves a nonzero depth-10 coefficient.
for s in (1, 2):
    for z in (1, 2):
        for k in (0, 1):
            y = s*(2*k-1)*z % 3
            assert y != 0
            expr = -y*(k*k-k+1)*(z*(k+1)-s*y)
            assert expr % 3 != 0

# The only ways channel B can escape exact even depth 10 are therefore:
# (i) f == 0 mod3, which raises B_Delta/Y depth; or
# (ii) k == -1 mod3, equivalent to v3(2K-9)>=3.
for k in (0, 1, 2):
    central_deep = (2*k - 1) % 3 == 0
    assert central_deep == (k == 2)

# Exact source identity used above.
f, omega, g, cu, T, a3 = sp.symbols("f omega g cu T a3")
Wq = (T*K + a3)/omega
lhs = sp.expand(omega*(g*((2*K-9)*T-a3)-cu*Wq))
rhs = sp.expand(f*((2*K-9)*T-a3)-3*cu*(K-3)*T)
assert sp.expand(lhs.subs(f, g*omega+cu)-rhs.subs(f, g*omega+cu)) == 0

print(
    "OK: fixed-3 third-order spill has even generic depth; "
    "any escape is forced to f-contact or extra central 3-depth"
)
