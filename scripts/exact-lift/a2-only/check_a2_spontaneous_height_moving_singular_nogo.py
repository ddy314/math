#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-moving-singular-nogo.md."""

import sympy as sp

x, y, tau = sp.symbols("x y tau")

H1 = 202500*x**4 + (101*x**2 + 4*x + 4)*y**2
H2 = (
    410062500*x**6 - 402975*x**4*y**2 - 7290000*x**4*y
    + 8100*x**3*y**2 + 101*x**2*y**4 + 3600*x**2*y**3
    + 40500*x**2*y**2 + 4*x*y**4 + 4*y**4
)
G = (
    100*x**2*(5*(y+9)**2 - 36*(y+9)*tau + 55*tau**2)
    - (x+2)**2*(2025*x**2 + y**2)
)
DH = (
    22275*x**4 + 89100*x**3 + 991*x**2*y**2 + 17640*x**2*y
    + 168480*x**2 + 44*x*y**2 + 44*y**2
)

# ---------------------------------------------------------------------------
# 1. Repeated-phase reduction
# ---------------------------------------------------------------------------
assert sp.factor(G.subs(tau, sp.Rational(18, 55)*(y+9))) == -DH/11

P1 = (
    240046103025*x**8 - 431151600*x**7 + 18108996360*x**6
    - 937618080*x**5 + 354227216*x**4 + 108902528*x**3
    + 76745984*x**2 + 8466432*x + 2768896
)
P2 = (
    629879737734025*x**8 + 220216678224400*x**7
    + 297840014098760*x**6 + 74145474010720*x**5
    + 52673580295056*x**4 + 7788392965248*x**3
    + 3650462246144*x**2 + 247566938112*x + 80965287936
)

assert sp.factor(sp.resultant(H1, DH, y)) == 164025*x**4*P1
assert sp.factor(sp.resultant(H2, DH, y)) == 430467210000*x**8*(25*x**2 + 1)**2*P2

fac_disc1 = {
    2:120, 3:7, 5:34, 7:28, 11:4, 13:4, 89:2, 101:4,
    367:2, 102251:1, 630451:1, 136776907:1,
}
fac_disc2 = {
    2:116, 3:5, 5:26, 7:64, 11:4, 13:4, 19:2, 101:4,
    5827:2, 9323:2, 8971:1, 5019481:2,
    833453052690874208617:1,
}

def product_factorization(fac):
    z = 1
    for p, e in fac.items():
        z *= p**e
    return z

assert abs(int(sp.discriminant(P1, x))) == product_factorization(fac_disc1)
assert abs(int(sp.discriminant(P2, x))) == product_factorization(fac_disc2)
for p in set(fac_disc1) | set(fac_disc2):
    if p > 1:
        assert sp.isprime(p)

# ---------------------------------------------------------------------------
# 2. Finite-field root helpers
# ---------------------------------------------------------------------------
def linear_roots(poly_expr, var, p):
    P = sp.Poly(poly_expr, var, modulus=p)
    roots = []
    for f, _ in sp.factor_list(P, modulus=p)[1]:
        if f.degree() == 1:
            a = int(f.nth(1)) % p
            b = int(f.nth(0)) % p
            roots.append((-b * pow(a, -1, p)) % p)
    return sorted(set(roots))


def repeated_singular_states(H, P, p):
    Pg = sp.gcd(sp.Poly(P, x, modulus=p), sp.Poly(sp.diff(P, x), x, modulus=p))
    xroots = linear_roots(Pg.as_expr(), x, p)
    Hx, Hy = sp.diff(H, x), sp.diff(H, y)
    Dx, Dy = sp.diff(DH, x), sp.diff(DH, y)
    states = []
    for xr in xroots:
        gy = sp.gcd(sp.Poly(H.subs(x, xr), y, modulus=p),
                    sp.Poly(DH.subs(x, xr), y, modulus=p))
        for yr in linear_roots(gy.as_expr(), y, p):
            det = Hx.subs({x:xr,y:yr})*Dy.subs({x:xr,y:yr}) \
                  - Hy.subs({x:xr,y:yr})*Dx.subs({x:xr,y:yr})
            if int(det) % p == 0:
                states.append((xr, yr))
    return xroots, states

# H1 candidate audit.
assert repeated_singular_states(H1, P1, 7)[1] == []
assert repeated_singular_states(H1, P1, 367)[0] == []
assert repeated_singular_states(H1, P1, 102251)[1] == [(61220, 95782)]
assert repeated_singular_states(H1, P1, 630451)[1] == [(340435, 610253)]
assert repeated_singular_states(H1, P1, 136776907)[1] == [(4766067, 102799536)]

# H2 candidate audit.
assert repeated_singular_states(H2, P2, 7)[1] == []
assert repeated_singular_states(H2, P2, 19)[1] == [(0, 0)]
assert repeated_singular_states(H2, P2, 5827)[1] == []
assert repeated_singular_states(H2, P2, 8971)[1] == [(2914, 6787)]
assert repeated_singular_states(H2, P2, 9323)[1] == []

# ---------------------------------------------------------------------------
# 3. No-lift carry certificate
# ---------------------------------------------------------------------------
def carry_data(H, p, xr, yr):
    tr = 18*(yr+9)*pow(55, -1, p) % p
    vals = {x:xr, y:yr, tau:tr}
    Hv, Gv = int(H.subs(vals)), int(G.subs(vals))
    assert Hv % p == 0 and Gv % p == 0
    gradH = [int(sp.diff(H,v).subs(vals)) % p for v in (x,y,tau)]
    gradG = [int(sp.diff(G,v).subs(vals)) % p for v in (x,y,tau)]
    idx = next(i for i,a in enumerate(gradH) if a)
    c = gradG[idx]*pow(gradH[idx], -1, p) % p
    assert all((gradG[i] - c*gradH[i]) % p == 0 for i in range(3))
    hcarry = Hv//p % p
    gcarry = Gv//p % p
    residual = (gcarry - c*hcarry) % p
    return tr, c, residual

expected_carry = [
    (H1, 102251, 61220, 95782, 35068, 51620, 99510),
    (H1, 630451, 340435, 610253, 474828, 365778, 401091),
    (H1, 136776907, 4766067, 102799536, 58512016, 46110684, 133381104),
    (H2, 8971, 2914, 6787, 4997, 8281, 3710),
]
for H, p, xr, yr, tr, c, residual in expected_carry:
    got = carry_data(H, p, xr, yr)
    assert got == (tr, c, residual)
    assert residual != 0

# ---------------------------------------------------------------------------
# 4. p=11 must be audited without dividing by 55
# ---------------------------------------------------------------------------
def full_singular_mod_11(H):
    Hgr = [sp.diff(H,v) for v in (x,y,tau)]
    Ggr = [sp.diff(G,v) for v in (x,y,tau)]
    out = []
    for xr in range(11):
        for yr in range(11):
            for tr in range(11):
                vals = {x:xr,y:yr,tau:tr}
                if int(H.subs(vals)) % 11 or int(G.subs(vals)) % 11:
                    continue
                a = [int(z.subs(vals)) % 11 for z in Hgr]
                b = [int(z.subs(vals)) % 11 for z in Ggr]
                minors = [(a[i]*b[j]-a[j]*b[i]) % 11
                          for i in range(3) for j in range(i+1,3)]
                if all(v == 0 for v in minors):
                    out.append((xr,yr,tr))
    return out

for H in (H1,H2):
    states = full_singular_mod_11(H)
    assert states == [(0,0,t) for t in range(11)]

# ---------------------------------------------------------------------------
# 5. H2 intrinsic singularity: all inert candidates are boundary/empty
# ---------------------------------------------------------------------------
H2x, H2y = sp.diff(H2,x), sp.diff(H2,y)
Ry = sp.factor(sp.resultant(H2,H2y,y))
Rx = sp.factor(sp.resultant(H2,H2x,y))

C2 = 101*x**2 + 4*x + 4
A6 = (64478501*x**6 + 1908012*x**5 + 9602508*x**4 + 106144*x**3
      + 438960*x**2 + 4800*x + 8000)
A8 = (6512328601*x**8 + 708537220*x**7 + 1501885036*x**6
      + 121752064*x**5 + 219524016*x**4 + 3371072*x**3
      + 8584000*x**2 + 89600*x + 128000)

assert Ry == 2**6*3**24*5**14*x**14*(x+2)**4*C2*A6
assert Rx == 2**8*3**32*5**20*x**16*(x+2)**4*A8
assert abs(int(sp.resultant(C2,A8,x))) == 2**24*13**2*101**2*59729*22177889
assert abs(int(sp.resultant(A6,A8,x))) == (
    2**72*5**9*17**6*31*47**6*101**6*181**2*251
    *371069497788281179471251313
)
for q in (59729,22177889,31,47,251,371069497788281179471251313):
    assert sp.isprime(q)

# Nonboundary gcds at the only inert candidates 31,47,251 have no full y state.
for p in (31,47,251):
    gx = sp.gcd(sp.Poly(C2*A6,x,modulus=p), sp.Poly(A8,x,modulus=p))
    for xr in linear_roots(gx.as_expr(),x,p):
        gy = sp.gcd(sp.gcd(sp.Poly(H2.subs(x,xr),y,modulus=p),
                            sp.Poly(H2x.subs(x,xr),y,modulus=p)),
                    sp.Poly(H2y.subs(x,xr),y,modulus=p))
        assert linear_roots(gy.as_expr(),y,p) == []

print("OK: A2 moving endpoint-height common channel has no surviving genuine inert singular Hensel branch")
