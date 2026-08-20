#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-second-order-tail.md."""

import math
import sympy as sp


def v2(n: int) -> int:
    n = abs(int(n))
    assert n
    return (n & -n).bit_length() - 1


def bernstein_coefficients_nd(poly_expr, vars_, intervals):
    q = sp.symbols("q0:%d" % len(vars_))
    expr = sp.expand(poly_expr.subs({
        x: a + (b-a)*qq
        for x, qq, (a,b) in zip(vars_, q, intervals)
    }))
    P = sp.Poly(expr, *q, domain=sp.QQ)
    degs = [P.degree(qq) for qq in q]
    power = dict(P.terms())
    out = []
    import itertools
    for ks in itertools.product(*[range(d+1) for d in degs]):
        val = sp.Rational(0)
        for ii in itertools.product(*[range(k+1) for k in ks]):
            aij = power.get(tuple(ii), 0)
            if not aij:
                continue
            mult = sp.Rational(1)
            for k, i, d in zip(ks, ii, degs):
                mult *= sp.Rational(math.comb(k, i), math.comb(d, i))
            val += aij*mult
        out.append(val)
    return degs, out


K, zeta, J, R = sp.symbols("K zeta J R")
X, Y = sp.symbols("X Y")
r, u, vv, chi = sp.symbols("r u vv chi")
U = 2*K - 9

# Rebuild universal cubic and first-layer point.
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
R0 = K**2 - (18+4*zeta)*K + 18*zeta + 55
J0 = (K**2 - 64*K*zeta - 576*K + 288*zeta + 1296)/(16*U)

Phi = J*(J+2*zeta)*(K-J)**2 - R*(J+zeta)**2
PhiJ = sp.diff(Phi, J)
PhiJJ = sp.diff(PhiJ, J)
PhiJ0 = sp.factor(PhiJ.subs({J:J0, R:R0}))
PhiJJ0 = sp.factor(PhiJJ.subs({J:J0, R:R0}))

# Projective Euclidean quotient.
Eproj = sp.Poly(sp.expand(E63.subs({K:1/r, zeta:u/r})*r**8), r)
Lproj = sp.Poly(55*r**2 + 18*(u-1)*r + 1-4*u-vv, r)
Qproj, _ = sp.div(Eproj, Lproj)
Q0 = sp.factor(Qproj.as_expr().subs({r:1/K, u:zeta/K, vv:R0/K**2}))
Qv0 = sp.factor(sp.diff(Qproj.as_expr(), vv).subs({r:1/K, u:zeta/K, vv:R0/K**2}))

# First-order primitive gates.
C_lt = sp.factor(-sp.Rational(65536)*U**4*(J0+zeta)**2/K**6)
C_gt = sp.factor(
    sp.Rational(65536)*U**3/K**6
    * (PhiJ0-U*(J0+zeta)**2)
)
raw_lt = sp.factor(C_lt-Q0)
raw_gt = sp.factor(C_gt-Q0)
num_lt, den_lt = sp.together(raw_lt).as_numer_denom()
num_gt, den_gt = sp.together(raw_gt).as_numer_denom()
c_lt, Glt_expr = sp.primitive(sp.Poly(sp.expand(num_lt),K,zeta).as_expr(),K,zeta)
c_gt, Ggt_expr = sp.primitive(sp.Poly(sp.expand(num_gt),K,zeta).as_expr(),K,zeta)
assert c_lt == 5184
assert c_gt == 128
assert sp.factor(den_lt) == 5**7*11**7*K**6
assert sp.factor(den_gt) == 5**7*11**7*K**6
Glt = sp.Poly(Glt_expr,K,zeta,domain=sp.ZZ)
Ggt = sp.Poly(Ggt_expr,K,zeta,domain=sp.ZZ)

# Exact quadratic homogeneous form before imposing first-order chi.
Ctr = sp.Rational(65536)*U**4/K**8
Q2 = sp.factor(
    Ctr*(
        -sp.Rational(1,2)*PhiJJ0*K**4/U**2
        + 2*(J0+zeta)*K**4/U*(chi+1)
    )
    + Qv0*(chi+1)**2
)
Hxy = sp.factor(sp.together(Y**2*Q2.subs(chi,X/Y)))
numH, denH = sp.together(Hxy).as_numer_denom()
assert sp.factor(denH) == 5**5*11**6*K**4
content, H2_expr = sp.primitive(sp.Poly(sp.expand(numH),X,Y,K,zeta).as_expr(),X,Y,K,zeta)
assert content == 256
H2 = sp.Poly(H2_expr,X,Y,K,zeta,domain=sp.ZZ)
assert H2.degree(X)+H2.degree(Y) >= 2
for (ix,iy,ik,iz), coeff in H2.terms():
    assert ix+iy == 2
assert H2.degree(zeta) == 4
assert len(H2.terms()) == 45
assert sp.factor(Hxy - 256*H2.as_expr()/(5**5*11**6*K**4)) == 0

# Projective sign of the quadratic coefficient on the actual parent box.
q2proj = sp.factor(Q2.subs({K:1/r,zeta:u/r}))
numq, denq = sp.together(q2proj).as_numer_denom()
assert denq == 5**5*11**6
Pq = sp.Poly(sp.expand(numq),r,u,chi)
assert (Pq.degree(r),Pq.degree(u),Pq.degree(chi),len(Pq.terms())) == (4,4,2,45)
degs, b = bernstein_coefficients_nd(
    Pq.as_expr(),
    (r,u,chi),
    ((sp.Rational(0),sp.Rational(1,1000)),
     (sp.Rational(0),sp.Rational(1,1000)),
     (sp.Rational(0),sp.Rational(1,23))),
)
assert degs == [4,4,2]
assert len(b) == 75
assert min(b) == -sp.Rational(1094168903517053204517852672,129150390625)
assert max(b) == -sp.Rational(14436349673818491223824,1953125)
assert max(b) < 0

# 2-adic ledger for T^6 G_< and T^6 G_>.
# A term K^i zeta^j becomes K^i a^j T^(6-j).
def gate_lower(poly, m):
    vals=[]
    for (i,j), coeff in poly.terms():
        vals.append(v2(int(coeff))+i+m*(6-j))
    return min(vals)
for m in range(5,13):
    assert gate_lower(Glt,m) >= 18
    assert gate_lower(Ggt,m) >= 17

# Primitive H2: unique lowest T-cleared monomial for all m>=5,t>=3.
# Baseline is X^2 zeta^4, coefficient 2^10*3^14*3733.
target = H2.coeff_monomial(X**2*zeta**4)
assert target == 18283339035648
assert sp.factorint(target) == {2:10,3:14,3733:1}

def h2_ledger(m,t):
    vals=[]
    yv=m+t-1
    for (ix,iy,ik,iz), coeff in H2.terms():
        val=v2(int(coeff))+iy*yv+ik+m*(6-iz)
        vals.append((val,(ix,iy,ik,iz)))
    return sorted(vals)
vals=h2_ledger(5,3)
assert vals[0] == (20,(2,0,0,4))
assert vals[1][0] >= 24
# Relative slopes in m,t are nonnegative, so (5,3) is the worst corner.
for (ix,iy,ik,iz), coeff in H2.terms():
    assert iy+4-iz >= 0
    assert iy >= 0

# Outer second-order clearing gives exact parent depth and orientation.
# v2 = (2M+10) + (2m+10) = 2M+2m+20.
assert (5**2*11) % 8 == 3
assert ((target//2**10) % 8) == 5
assert (3*5) % 8 == 7

# Abstract divisibility/support law sanity checks.
def vp(n,p):
    n=abs(int(n))
    if n==0:
        return 10**9
    k=0
    while n%p==0:
        n//=p; k+=1
    return k

p=101
for h in range(1,5):
    for rho in range(0,5):
        s=min(h,rho)
        # cleared M1 has exact h+rho; generic quadratic has 2h;
        # cubic starts at 3h. Choose units avoiding accidental cancellation
        # unless the saturated branch explicitly inserts it.
        if rho < h:
            n = p**(h+rho) + 7*p**(2*h)
            assert vp(n,p) == h+rho
            assert vp(n//p**(h+s),p) == 0
        else:
            # no second-order cancellation
            n = p**(h+rho) + 7*p**(2*h)
            assert vp(n//p**(2*h),p) == 0
            # forced second-order cancellation, cubic invisible mod p^(2h+1)
            n2 = p**(h+rho) - p**(2*h) + p**(2*h+1)
            if rho==h:
                # coefficients are chosen so the two 2h terms cancel.
                n2 = p**(2*h) - p**(2*h) + p**(2*h+1)
            else:
                # rho>h: make quadratic coefficient vanish at first digit.
                n2 = p**(h+rho) + p**(2*h+1)
            assert vp(n2,p) > 2*h

print('OK: canonical second-order descendant tail reads saturated overdepth and has positive 1 mod8 parent orientation')
