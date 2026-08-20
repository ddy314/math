#!/usr/bin/env python3
"""Exact certificate for spontaneous-angle-pair-q0-depth.md."""

import sympy as sp

A,B,N,T,Q,b3 = sp.symbols("A B N T Q b3")

Qexpr = B + 2*N
U = sp.expand((45*B**2 - 2*A*N)**2 - A**2*B*(99*B - 4*N))
DQ = sp.expand(2025*B**2 - 180*A*N - 100*A**2)
E = 11*A**2 + 20*A*N - 225*B**2

# Exact second-order Q bridge.
assert sp.expand(U - (-4*N*(B+N)*DQ - 9*Qexpr**2*E)) == 0

Oplus = sp.expand(T*U + 2*A**2*Qexpr*b3)
Ominus = sp.expand(T*U - 2*A**2*Qexpr*b3)
assert sp.expand(Oplus - Ominus - 4*A**2*Qexpr*b3) == 0

# On Q=0, x=-2 and U is exactly 4 N^2 D_Q.
assert sp.expand(U.subs(B,-2*N) - 4*N**2*DQ.subs(B,-2*N)) == 0

# Normalized prefix defect.
x,y = sp.symbols("x y")
Delta = 2025*x**2 - 18*y - y**2
assert sp.expand(DQ.subs({B:x*N,A:y*N/10}) - N**2*Delta) == 0

# First-layer conic at x=-2.
conic = sp.factor(Delta.subs(x,-2))
assert sp.expand(conic - (8181-(y+9)**2)) == 0
assert sp.factor(sp.discriminant(sp.Poly(conic,y))) == 2**2 * 3**4 * 101
assert 101 % 4 == 1

# A-content exclusion: modulo A, U=(45B^2)^2.
assert sp.rem(U, A, domain=sp.ZZ[B,N]) == 45**2 * B**4

# Local valuation model check for the exact min law.
# O_± = unit*D + p^(e+c)*R_± with difference exactly p^(e+c)*unit.
# Exhaust finite toy p-adic residues to certify the valuation logic itself.
def vp(n,p):
    if n == 0:
        return 99
    k=0
    while n%p==0:
        n//=p; k+=1
    return k

for p in (7,11,19):
    for e in (1,2,3):
        for c in range(e+1):
            cap=e+c
            for d in range(0,cap+3):
                Dv=p**d
                # unit coefficient 1; choose two corrections whose difference has exact cap.
                Rp=1
                Rm=1-p**0
                # Better model: corrections p^cap*r1,p^cap*r2 with r1-r2 unit.
                op=Dv+p**cap*1
                om=Dv+p**cap*2
                lhs=min(vp(op,p),vp(om,p))
                assert lhs == min(d,cap)

print("OK: A2 angle sign-pair Q0 depth law certified")
