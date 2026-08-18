#!/usr/bin/env python3
"""Exact certificate for spontaneous-omega-content-common.md."""

import sympy as sp

x,y,t = sp.symbols("x y t")
A,B,N,T,b3,beta = sp.symbols("A B N T b3 beta")

Q = B+2*N
K = 9*N+10*A
N0 = sp.Rational(81,4)*B**2+A**2
U = (45*B**2-2*A*N)**2-A**2*B*(99*B-4*N)
Cw = sp.expand(U-2*A**2*Q**2)
Oplus = sp.expand(T*U+2*A**2*Q*b3)
assert sp.expand(Oplus-(T*Cw+2*A**2*Q*(T*Q+b3))) == 0

# Normalized C_omega = N^4/100 A_-.
Aminus = sp.expand(
    202500*x**4-(101*x**2+4*x+4)*y**2-1800*x**2*y
)
assert sp.factor(Cw.subs({B:x*N,A:y*N/10})-N**4*Aminus/100) == 0

# Common additive gate.
s = y+9
J = sp.expand(
    100*x**2*(5*s**2-36*s*t+55*t**2)
    -(x+2)**2*(2025*x**2+y**2)
)

# Singular class I: F itself singular.
Fx = sp.diff(Aminus,x)
Fy = sp.diff(Aminus,y)
res_Fy = sp.factor(sp.resultant(Aminus,Fy,y))
res_Fx = sp.factor(sp.resultant(Aminus,Fx,y))
assert res_Fy == 810000*x**4*(101*x**2+4*x+4)*(101*x**2+4*x+8)
Q4 = 10201*x**4+1212*x**3+1652*x**2+128*x+128
assert res_Fx == 164025000000*x**6*Q4
P1 = (101*x**2+4*x+4)*(101*x**2+4*x+8)
res_singF = int(sp.resultant(P1,Q4,x))
assert sp.factorint(abs(res_singF)) == {
    2:22,3:2,5:2,17:1,37:1,67:2,101:4
}

# Singular class II: repeated tau.
Gt = sp.diff(J,t)
assert sp.factor(Gt-200*x**2*(55*t-18*s)) == 0
Domega = sp.expand(
    22275*x**4+89100*x**3+991*x**2*y**2+17640*x**2*y
    +168480*x**2+44*x*y**2+44*y**2
)
assert sp.factor(sp.discriminant(J,t)-2000*x**2*Domega) == 0
Qomega = sp.expand(
    251056113025*x**8+44533768400*x**7+67275876360*x**6
    +8529261920*x**5+6336428816*x**4+503628928*x**3
    +239152384*x**2+8466432*x+2768896
)
assert sp.factor(sp.resultant(Aminus,Domega,y)-164025*x**4*Qomega) == 0
assert all(c>0 for c in sp.Poly(Qomega,x).all_coeffs())
assert sp.factorint(int(sp.discriminant(Qomega,x))) == {
    2:120,3:11,5:26,7:12,11:4,13:4,23:2,101:8,
    557:1,4357:2,7596456621900959:1
}

# Full singular system rank test.
Gx = sp.diff(J,x)
Gy = sp.diff(J,y)
minor_xy = sp.expand(Fx*Gy-Fy*Gx)
minor_xt = sp.expand(Fx*Gt)
minor_yt = sp.expand(Fy*Gt)

def singular_states(p):
    out=[]
    for xx in range(p):
        for yy in range(p):
            if int(Aminus.subs({x:xx,y:yy})) % p:
                continue
            for tt in range(p):
                subs={x:xx,y:yy,t:tt}
                if int(J.subs(subs)) % p:
                    continue
                if int(minor_xy.subs(subs)) % p:
                    continue
                if int(minor_xt.subs(subs)) % p:
                    continue
                if int(minor_yt.subs(subs)) % p:
                    continue
                out.append((xx,yy,tt))
    return out

for p in (7,11,23,67):
    states=singular_states(p)
    assert states == [(0,0,tt) for tt in range(p)]

# Unique genuine large singular state.
p = 7596456621900959
assert sp.isprime(p) and p % 4 == 3
poly = sp.Poly(Qomega,x,modulus=p)
g = sp.gcd(poly,poly.diff())
assert g.degree() == 1
x0 = 596722596594438
assert int(g.eval(x0)) % p == 0

gy = sp.gcd(
    sp.Poly(Aminus.subs(x,x0),y,modulus=p),
    sp.Poly(Domega.subs(x,x0),y,modulus=p),
)
assert gy.degree() == 1
y0 = 7182062884214340
assert int(gy.eval(y0)) % p == 0
t0 = 7460836853203523
subs0={x:x0,y:y0,t:t0}
assert all(int(f.subs(subs0)) % p == 0 for f in (Aminus,J,minor_xy,minor_xt,minor_yt))
assert (55*t0-18*(y0+9)) % p == 0

# p^2 lift compatibility obstruction.
F0=int(Aminus.subs(subs0))
G0=int(J.subs(subs0))
fc=(F0//p) % p
gc=(G0//p) % p
rowF=[int(sp.diff(Aminus,v).subs(subs0)) % p for v in (x,y,t)]
rowG=[int(sp.diff(J,v).subs(subs0)) % p for v in (x,y,t)]
assert rowF == [3088566246132647,763538860035101,0]
assert rowG == [5543473436650293,7013503068586219,0]
assert fc == 7136724306802588
assert gc == 6411661286654023
lam = rowG[0]*pow(rowF[0],-1,p) % p
assert lam == 2399356256055466
assert (rowG[1]-lam*rowF[1]) % p == 0
obstruction=(gc-lam*fc) % p
assert obstruction == 4160590904825983
assert obstruction != 0

print("OK: A2 omega-content common branch and singular audit certified")
