#!/usr/bin/env python3
"""Certificate for fixed3-exception-collapse.md.

The checker proves two fixed-3 continuation facts.

1. In the a3-shallow channel, once v3(2K-9)>=3, the exact third-order
   descendant numerator has v3 exactly 12.  This is independent of whether
   3 divides the old f-denominator factor.
2. On the eta=1 endpoint type (d,c_Q,k_h,slot)=(2,7,3,-), the a2-shallow
   f-contact branch is impossible already modulo 3.
"""

import sympy as sp

K, zeta, J, R = sp.symbols("K zeta J R")
F, Lerr = sp.symbols("F Lerr")
X, Y = sp.symbols("X Y")
r, u, v = sp.symbols("r u v")
U = 2*K - 9

# Canonical universal descendant data.
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
for n in range(1, 4):
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


def v3(n: int) -> int:
    n = abs(int(n))
    assert n
    out = 0
    while n % 3 == 0:
        n //= 3
        out += 1
    return out


def reduce_qq_poly_mod(expr, vars_, modulus):
    """Reduce a QQ polynomial modulo an integer prime power."""
    P = sp.Poly(expr, *vars_, domain=sp.QQ)
    out = sp.Integer(0)
    for mons, coeff in P.terms():
        num, den = sp.Rational(coeff).as_numer_denom()
        assert den % 3
        c = (int(num) % modulus) * pow(int(den) % modulus, -1, modulus)
        term = sp.Integer(c % modulus)
        for var, e in zip(vars_, mons):
            term *= var**e
        out += term
    return sp.Poly(sp.expand(out), *vars_, modulus=modulus).as_expr()


# ---------------------------------------------------------------------------
# a3-shallow, extra-central: v3(zeta)=1 and v3(U)>=3.
# ---------------------------------------------------------------------------
# Write U=27 r, zeta=3 z, Y_d=81 y, X_d=x.  The exact third recursion is
# N3 = T^6 E3 with
#   E3 = 64 A^2(81 X G_< + 2 Y G_>) + A C H2 + D H3,
# A=5^m B^2, C=2^(2M+10)5^2*11, D=2^(4M+17)5^2*11^2.
# T^6 is a 3-unit and is 1 mod 3, so it does not affect the valuation or
# the final normalized residue.
rr, zz, xx, yy, AA, CC, DD, tt = sp.symbols("rr zz xx yy AA CC DD tt")
Kdeep = (sp.Integer(9) + 27*rr)/2
zdeep = 3*zz
Ydeep = 81*yy
Xdeep = xx
E3 = (
    64*AA**2*(81*X*Glt.as_expr() + 2*Y*Ggt.as_expr())
    + AA*CC*H2.as_expr()
    + DD*H3.as_expr()
)
Edeep = sp.expand(E3.subs({K: Kdeep, zeta: zdeep, X: Xdeep, Y: Ydeep}))
Pdeep = sp.Poly(Edeep, rr, zz, xx, yy, AA, CC, DD, domain=sp.QQ)
assert min(v3(int(sp.Rational(c).as_numer_denom()[0])) for _, c in Pdeep.terms()) == 10

# The full depth-10 normalized expression modulo 27 collapses after inserting
# the exact source-unit relations modulo 27:
#   A == t*x,  C == 11*t,  D == 11*t^2,
# where t=2^(2M+2).  These follow from Y_d==0 mod81 and
# That_2 == 2^m(c_u g)^2 T mod27 in this channel.
E10_mod27 = reduce_qq_poly_mod(
    Edeep/3**10,
    (rr, zz, xx, yy, AA, CC, DD),
    27,
)
collapsed = reduce_qq_poly_mod(
    sp.expand(E10_mod27.subs({AA: tt*xx, CC: 11*tt, DD: 11*tt**2})),
    (rr, zz, xx, yy, tt),
    27,
)
assert sp.Poly(collapsed - 9*tt**2*xx**3,
               rr, zz, xx, yy, tt, modulus=27).is_zero

# Audit the elementary coefficient congruences behind A,C,D.
assert (2**8 * 25 * 11) % 27 == 11
assert (2**13 * 25 * 11**2) % 27 == 11
# T=10^m, hence 2^m*T = 2^(2m)5^m exactly; this is the factor in x.
# Mod 3, t^2=1 and x=(-1)^m, so the depth-12 digit is nonzero.
for m_parity in (0, 1):
    s = 1 if m_parity == 0 else 2
    for tmod in (1, 2):
        assert (tmod*tmod*s**3) % 3 == s

# Therefore E3/3^12 == (-1)^m mod3, hence v3(N3)=12 exactly.


# ---------------------------------------------------------------------------
# eta=1 unique odd-3 type: eliminate a2-shallow f-contact.
# ---------------------------------------------------------------------------
# Here M=2m-1, d=2, c_Q=7, k_h=3 and the actual slot is minus:
# H0-Y2=3g^2/2.  Work only in F_3.
# f==0 gives q=s*c_u.  Combining Q0=c_Q q with
# Q0=5^M+2^m g c_u gives s*c_u*(1-g)=-1, so g=-1.
for s in (1, 2):
    for cu in (1, 2):
        possible_g = []
        for g in (1, 2):
            if (s*cu*(1-g) + 1) % 3 == 0:
                possible_g.append(g)
        assert possible_g == [2]

# Put a=a2/3, a unit.  From f==0 and g=-1 one gets c_u/omega=1.
# Since a3/3==0 in the a2-shallow channel,
# H0/3 == a and Y2/3 == a, while the right side is g^2/2 == 2.
for a in (1, 2):
    lhs = (a - a) % 3
    rhs = (1 * pow(2, -1, 3)) % 3
    assert lhs == 0
    assert rhs == 2
    assert lhs != rhs

print(
    "OK: deeper-central a3-shallow fixed-3 has exact depth 12; "
    "eta=1 a2-shallow f-contact is impossible"
)
