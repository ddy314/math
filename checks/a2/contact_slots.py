#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0307; see history/sources.json.
"""

from fractions import Fraction as Q
from collections import Counter
from itertools import product as cartesian_product
import sympy as sp


def factor_trial(n):
    factors = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            factors[p] = factors.get(p,0)+1
            n //= p
        p += 1
    if n > 1:
        factors[n] = factors.get(n,0)+1
    return factors


ETA = 2
W_LO,W_HI = Q(837,1000),Q(843,1000)
CHI_HI = Q(20,19)
SLOTS = {"-":(Q(393,125),Q(1607,500)),
         "+":(Q(2389,500),Q(606,125))}
# d>=5 already exceeds the largest possible high-2 G slot.
assert Q(3,8)*5**(5-3)/W_HI > Q(1212,125)

raw = []
retained = []
for d in range(1,5):
    scale = Q(2**(ETA+2))*Q(5)**(ETA+1-d)
    for sign,(slo,shi) in SLOTS.items():
        lo,hi = scale*slo*W_LO/CHI_HI,scale*shi*W_HI
        for product in range(int(lo)+1,int(hi)+1):
            if not lo < product < hi:
                continue
            for kh in range(1,product+1,2):
                if product % kh:
                    continue
                cq = product//kh
                if cq % 4 != 3 or cq % 5 == 0 or cq % 3 == 0:
                    continue
                factors = factor_trial(kh)
                e3 = factors.get(3,0)
                if e3 not in (1,3):
                    continue
                row = (d,cq,kh,sign)
                raw.append(row)
                if 5 in factors or any(p != 3 and p % 4 == 3 for p in factors):
                    continue
                if (e3 == 1 and sign != "+") or (e3 == 3 and sign != "-"):
                    continue
                retained.append(row)

expected = [(1,7,219,"+"),(1,31,51,"+"),(1,511,3,"+"),
            (1,523,3,"+"),(1,527,3,"+"),(1,539,3,"+"),
            (2,103,3,"+"),(2,107,3,"+")]
assert len(raw) == 27
assert sorted(retained) == expected
assert all(factor_trial(kh).get(3) == 1 for _,_,kh,_ in retained)

# If one inert prime also recycles A3/Wq/GDelta and outer parity, the
# independent source-overlap certificate restricts it to p=7 with
# (K,zeta,theta)=(3,4,-1).  Audit the original decimal rows, not a
# coefficient-ratio-only projection.  m is a complete exponent residue
# modulo 6; all physical m >= 7 are covered by this periodic calculation.
p = 7
overlap7 = []
for d,cq,kh,sign in retained:
    assert sign == "+"
    for m in range(6):
        M = 2*m-2
        lam = m-d
        a2 = (3-9*pow(10,M % 6,p))*pow(10,-1,p) % p
        a3 = -3*pow(10,m,p) % p
        for cu in range(1,p):
            for g in range(1,p):
                q = -2*cu*pow(pow(5,lam % 6,p),-1,p) % p
                if (cq*q-pow(5,M % 6,p)-pow(2,m,p)*cu*g) % p:
                    continue
                b2 = pow(2,(M+m+1) % 6,p)*cu*g % p
                prefix_norm = (9*b2*pow(2,-1,p))**2+a2*a2
                B = cq*pow(5,d,p) % p
                if (B*B*prefix_norm+g*g*a3*a3) % p:
                    continue
                if (B*a2-g*g*kh*pow(2,-1,p)) % p:
                    continue
                omega = -cu*pow(g,-1,p) % p
                assert (4*g*omega-3*cu) % p == 0  # actual A3
                overlap7.append((d,cq,kh,m,cu,g,a2,a3))
assert sorted(overlap7) == [(1,31,51,2,4,4,2,1),
                    (1,31,51,5,3,3,2,6),
                    (1,527,3,2,6,5,2,1),
                    (1,527,3,5,1,2,2,6)]

# The remaining original-source sheets are smooth over Z_7.  Fix c_u,g
# and use (omega,a2,a3) as implicit variables.  The three rows below are
# respectively Q0, the concatenation/height plane, and the sphere with
# the actual positive high factor substituted.  Their Jacobian minor
# never vanishes at the four states, so every verified mod49 point lifts
# to all 7-adic depths.  This is local compatibility, not an Exact Lift.
all_odd_counts = []
for d,cq,kh,mc,cv,gv,av,tv in sorted(overlap7):
    ov = -cv*pow(gv,-1,7) % 7
    for m in range(mc,42,6):  # complete period of all powers modulo 49
        mod = 49
        M = 2*m-2
        T = pow(10,m,mod)
        N = pow(10,M,mod)
        B = cq*5**d % mod
        source_power = pow(5,M+m,mod)
        binary_power = pow(2,M+m+1,mod)

        def rows(cu,g,om,a2,a3):
            k = (9*N+10*a2) % mod
            b2 = binary_power*cu*g % mod
            two_h = (g*g*kh-2*B*a2) % mod
            return ((B*(g*om-cu)-source_power-T*cu*g) % mod,
                    (om*two_h-2*cu*(T*k+a3)) % mod,
                    (two_h*two_h-4*g*g*a3*a3-B*B*(81*b2*b2+4*a2*a2)) % mod)

        jq = B*gv % 7
        ha,hb = (-2*B*ov-20*cv*T) % 7, -2*cv % 7
        sa,sb = -8*B*B*av % 7, -8*gv*gv*tv % 7
        det2 = (ha*sb-hb*sa) % 7
        det3 = jq*det2 % 7
        assert det3 == (3 if cq == 31 else 4)

        # Expand the complete source polynomials at the mod7 point.  All
        # higher-degree coefficients disappear after division by 7 and
        # reduction mod7, so this determines every possible first lift.
        dcS,dgS,doS,daS,dzS = sp.symbols("dc dg do da dz")
        cs,gs = cv+7*dcS,gv+7*dgS
        os,as2,as3 = ov+7*doS,av+7*daS,tv+7*dzS
        ks = 9*N+10*as2
        b2s = binary_power*cs*gs
        hs = gs*gs*kh-2*B*as2
        source_polynomials = (
            B*(gs*os-cs)-source_power-T*cs*gs,
            os*hs-2*cs*(T*ks+as3),
            hs*hs-4*gs*gs*as3*as3-B*B*(81*b2s*b2s+4*as2*as2),
        )
        initials = []
        for expr in source_polynomials:
            full = sp.Poly(sp.expand(expr),dcS,dgS,doS,daS,dzS,domain=sp.ZZ)
            assert all(cc % 7 == 0 for cc in full.coeffs())
            initial = sp.Poly(full.as_expr()/7,dcS,dgS,doS,daS,dzS,modulus=7)
            assert initial.total_degree() <= 1
            initials.append(initial.as_expr())
        free = {doS:0,daS:0,dzS:0}
        bq,bh,bs = [-expr.subs(free) for expr in initials]
        do_sol = bq*pow(jq,-1,7)
        da_sol = (bh*sb-hb*bs)*pow(det2,-1,7)
        dz_sol = (ha*bs-sa*bh)*pow(det2,-1,7)
        implicit = {doS:do_sol,daS:da_sol,dzS:dz_sol}
        assert all(sp.Poly(expr.subs(implicit),dcS,dgS,modulus=7).is_zero
                   for expr in initials)
        h_word = -((cv+gv*ov)//7+dcS+ov*dgS+gv*do_sol)*pow(cv,-1,7)
        k_word = (9*N+10*av-3)//7+10*da_sol
        t_inv = pow(T,-1,mod)
        z_word = (tv*t_inv-4)//7+t_inv*dz_sol
        height_word = 1+k_word+z_word  # alpha/(7T) modulo 7
        assert sp.Poly(h_word-3*height_word-5*m,dcS,dgS,modulus=7).is_zero

        count = 0
        for dc in range(7):
            for dg in range(7):
                cu,g = cv+7*dc,gv+7*dg
                rQ,rH,rS = rows(cu,g,ov,av,tv)
                assert rQ % 7 == rH % 7 == rS % 7 == 0
                bQ,bH,bS = -rQ//7,-rH//7,-rS//7
                do = bQ*pow(jq,-1,7) % 7
                da = (bH*sb-hb*bS)*pow(det2,-1,7) % 7
                dz = (ha*bS-sa*bH)*pow(det2,-1,7) % 7
                om,a2,a3 = ov+7*do,av+7*da,tv+7*dz
                assert rows(cu,g,om,a2,a3) == (0,0,0)
                k = (9*N+10*a2) % mod
                u = (2*k-9) % mod
                z = a3*pow(T,-1,mod) % mod
                theta = cu*pow(g*om,-1,mod) % mod
                source_a = (u*g*om-k*cu) % mod
                h0 = (g*g*kh-2*B*a2)*pow(2,-1,mod) % mod
                wq = h0*pow(cu,-1,mod) % mod
                r0 = (k*k-(18+4*z)*k+18*z+55) % mod
                r_actual = ((1-theta)**2*(k+z)**2
                            -((1-theta)*pow(theta,-1,mod))**2*z*z) % mod
                w = (r0-r_actual) % mod
                y = (u*(u-z-theta*(k+z))-63*k*k*pow(16,-1,mod)) % mod
                outer = [(j*(j+2*z)*(k-j)**2-r_actual*(j+z)**2) % mod
                         for j in (2,4)]
                gates = (source_a,wq,w,y,*outer)
                assert all(x % 7 == 0 for x in gates)
                if all(x != 0 for x in gates):
                    count += 1
        assert count > 0
        all_odd_counts.append(count)
assert len(all_odd_counts) == 28
assert min(all_odd_counts) == 17 and max(all_odd_counts) == 27


def source7_lift(m, cq, kh, dc, dg):
    """Exact original-source point mod343, with two free first digits.

    Used by the same-P3 companion check to resolve the vanishing first
    N3 digit.  Fixing the higher free digits to zero is a local slice;
    it does not impose the global decimal windows or prime supports.
    """
    base = [r for r in overlap7 if r[1:3] == (cq,kh) and r[3] == m % 6]
    assert len(base) == 1
    _,_,_,_,cv,gv,av,tv = base[0]
    ov = -cv*pow(gv,-1,7) % 7
    cu,g = cv+7*dc,gv+7*dg

    def rows(om,a2,a3,mod):
        T,N = pow(10,m,mod),pow(10,2*m-2,mod)
        B = 5*cq % mod
        k = (9*N+10*a2) % mod
        b2 = pow(2,3*m-1,mod)*cu*g % mod
        two_h = (g*g*kh-2*B*a2) % mod
        return ((B*(g*om-cu)-pow(5,3*m-2,mod)-T*cu*g) % mod,
                (om*two_h-2*cu*(T*k+a3)) % mod,
                (two_h*two_h-4*g*g*a3*a3-B*B*(81*b2*b2+4*a2*a2)) % mod)

    B,T = 5*cq % 7,pow(10,m,7)
    jq = B*gv % 7
    ha,hb = (-2*B*ov-20*cv*T) % 7,-2*cv % 7
    sa,sb = -8*B*B*av % 7,-8*gv*gv*tv % 7
    det2 = (ha*sb-hb*sa) % 7
    assert jq*det2 % 7 == (3 if cq == 31 else 4)
    om,a2,a3,mod = ov,av,tv,7
    assert rows(om,a2,a3,mod) == (0,0,0)
    while mod < 343:
        res = rows(om,a2,a3,7*mod)
        assert all(v % mod == 0 for v in res)
        bq,bh,bs = [-v//mod % 7 for v in res]
        do = bq*pow(jq,-1,7) % 7
        da = (bh*sb-hb*bs)*pow(det2,-1,7) % 7
        dz = (ha*bs-sa*bh)*pow(det2,-1,7) % 7
        om,a2,a3 = om+mod*do,a2+mod*da,a3+mod*dz
        mod *= 7
        assert rows(om,a2,a3,mod) == (0,0,0)
    return cu,g,om,a2,a3

# Integer recovery uses the same source rows, without a direction change.
cuS,gS,omS,khS,BS,cqS,TS,NS,a2S,a3S,b2S,b3S,AS = sp.symbols(
    "cu g omega kh B cq T N a2 a3 b2 b3 Astar"
)
LS = BS*omS+10*cuS*TS
ES = omS*gS*gS*khS/2-9*cuS*TS*NS
planeS = omS*(gS*gS*khS-2*BS*a2S)-2*cuS*(TS*(9*NS+10*a2S)+a3S)
assert sp.expand(planeS-2*(ES-LS*a2S-cuS*a3S)) == 0
om_recovery = (AS/gS+TS*cuS/5)/cqS
qrowS = 5*cqS*(gS*om_recovery-cuS)-5*(AS-cqS*cuS)-TS*cuS*gS
assert sp.cancel(qrowS) == 0
sphereS = (gS*gS*khS-2*BS*a2S)**2-4*gS*gS*a3S*a3S-BS*BS*(81*b2S*b2S+4*a2S*a2S)
assert sp.expand(sphereS.subs(b2S,gS*b3S/BS)
                 +gS*gS*(81*b3S*b3S+4*a3S*a3S+4*khS*BS*a2S-khS*khS*gS*gS)) == 0
assert Q(1,250)/30 == Q(1,7500)  # recovered a2 interval is narrower than 1

# The same exact sphere identity fixes the actual shallow-3 prefix word.
# kh=3*kappa, a2=3*A and 9 | a3; divide by 9 before reducing mod3.
kap,A,a3div9,b3unit,gunit,Bunit = sp.symbols("kappa A a3div9 b3unit gunit Bunit")
sphere3 = ((3*kap)**2*gunit**2-81*b3unit**2-4*(9*a3div9)**2
           -4*(3*kap)*Bunit*(3*A))/9
assert sp.Poly(sp.expand(sphere3-(kap**2*gunit**2-kap*Bunit*A)),
               kap,A,a3div9,b3unit,gunit,Bunit,modulus=3).is_zero
for cq,kh in ((31,51),(527,3)):
    kappa = kh//3
    Bmod = cq*5 % 3
    assert kappa*Bmod % 3 == 1
    for gmod in (1,2):
        allowed = [amod for amod in (1,2)
                   if (kappa*kappa*gmod*gmod-kappa*Bmod*amod) % 3 == 0]
        assert allowed == [1]  # K/3 == a2/3 == 1 mod3

# Reconstruct the same three source rows after extracting their known
# 3-content.  This chart records local compatibility only.  With g,Z
# free and (omega,A2,c_u) implicit, the Jacobian is a 3-unit and all
# verified residue points lift to arbitrary 3-adic depth.
normalized_plane3 = (omS*(kap*gS*gS-2*BS*A)
                     -2*cuS*(TS*(3*NS+10*A)+3*a3div9))
assert sp.expand(planeS.subs({khS:3*kap,a2S:3*A,a3S:9*a3div9})
                 -3*normalized_plane3) == 0
normalized_sphere3 = kap**2*gS**2-4*kap*BS*A-9*b3S**2-36*a3div9**2
assert sp.expand(sphereS.subs({khS:3*kap,a2S:3*A,a3S:9*a3div9,
                              b2S:gS*b3S/BS})
                 -9*gS*gS*normalized_sphere3) == 0


def source3_lift(cq, kh, m, g, Z):
    B, kappa = 5*cq, kh//3

    def rows(om, A2, cu, mod):
        T, N = pow(10,m,mod), pow(10,2*m-2,mod)
        b3 = B*pow(2,3*m-1,mod)*cu
        return ((B*(g*om-cu)-pow(5,3*m-2,mod)-T*cu*g) % mod,
                (om*(kappa*g*g-2*B*A2)
                 -2*cu*(T*(3*N+10*A2)+3*Z)) % mod,
                (kappa*kappa*g*g-4*kappa*B*A2
                 -9*b3*b3-36*Z*Z) % mod)

    delta = pow(2,m,3)
    gbase = -B % 3
    cubase, ombase = delta*pow(gbase,-1,3) % 3, -delta % 3
    om, A2, cu = ombase, 1, cubase
    assert rows(om,A2,cu,3) == (0,0,0)
    base9 = rows(om,A2,cu,9)
    jac = []
    for vo,vA,vc in ((3,0,0),(0,3,0),(0,0,3)):
        moved = rows(om+vo,A2+vA,cu+vc,9)
        jac.append(tuple((a-b)//3 % 3 for a,b in zip(moved,base9)))
    inverse = {tuple(sum(v[i]*jac[i][j] for i in range(3)) % 3
                     for j in range(3)):v
               for v in cartesian_product(range(3),repeat=3)}
    assert len(inverse) == 27  # exact invertibility, not a numerical rank
    mod = 3
    while mod < 81:
        residue = rows(om,A2,cu,3*mod)
        assert all(v % mod == 0 for v in residue)
        rhs = tuple(-v//mod % 3 for v in residue)
        vo,vA,vc = inverse[rhs]
        om, A2, cu = om+mod*vo, A2+mod*vA, cu+mod*vc
        mod *= 3
        assert rows(om,A2,cu,mod) == (0,0,0)
    return om,A2,cu


source3_counts = []
for cq,kh in ((31,51),(527,3)):
    for m in range(8,26,3):  # complete m mod18 exponent period modulo81
        counts = Counter()
        for g in range(-5*cq % 3,81,3):
            for Z in range(81):
                om,A2,cu = source3_lift(cq,kh,m,g,Z)
                k = (3*pow(10,2*m-2,81)+10*A2) % 81
                theta = cu*pow(g*om,-1,81) % 81
                # A3/(9*g*omega)=(2k-3-k*theta)/3.
                a3digit = (2*k-3-k*theta)//3 % 27
                if a3digit % 3:
                    counts["N9"] += 1
                    continue
                r = a3digit//3 % 9
                if r % 3 != 1:
                    counts["N10"] += 1
                    continue
                j,z,s = ((k-1)//3 % 3, Z*pow(pow(10,m,3),-1,3) % 3,
                         (r-1)//3 % 3)
                initial11 = (1-s+z*(j-1)) % 3
                counts["N11_"+str(initial11)] += 1
        assert counts == {"N9":1458,"N10":486,
                          "N11_0":81,"N11_1":81,"N11_2":81}
        source3_counts.append(counts)
assert len(source3_counts) == 12

# The surcharge subcase v2(g)=2 has an exact CRT phase mod168.
crt_expected = {(31,2):(25,4),(31,5):(101,52),
                (527,2):(41,68),(527,5):(85,44)}
for d,cq,kh,mc,cv,gv,_,_ in sorted(overlap7):
    delta = pow(2,mc,3)
    cu3 = delta if cq == 31 else -delta % 3
    g3 = -cq*5 % 3
    cu_classes = [n for n in range(168)
                  if n % 8 == pow(5,mc,8) and n % 7 == cv and n % 3 == cu3]
    g_classes = [n for n in range(168)
                 if n % 8 == 4 and n % 7 == gv and n % 3 == g3]
    assert (cu_classes,g_classes) == ([crt_expected[cq,mc][0]],[crt_expected[cq,mc][1]])
    for om in (1,3,5,7):
        assert (cq*5*(4*om-cu_classes[0])-pow(5,3*mc-2,8)) % 8 == 0

first_units = {}
for cq in (31,527):
    survivors = []
    for m in range(8,81,3):
        lo = Q(2*837,5000*cq)*Q(5,4)**m
        hi = Q(2*843,5000*cq)*Q(5,4)**m
        residue = crt_expected[cq,m % 6][0]
        for cu in range(int(lo)+1,int(hi)+1):
            if not lo < cu < hi or cu % 168 != residue or cu % 5 == 0:
                continue
            if any(p % 4 != 1 for p in factor_trial(cu)):
                continue
            survivors.append((m,cu))
        if survivors:
            break
    first_units[cq] = survivors
assert first_units == {31:[(68,42193)],527:[(80,35993),(80,36161)]}
print("OK: eta=2 shared7 two-slot source/word certificate; exact source3 chart keeps depth9/10/11 and >=12 locally compatible; actual integer recovery has one numerator pair per (m,cu,g); v2(g)=2 unit windows require m>=68 or m>=80")
