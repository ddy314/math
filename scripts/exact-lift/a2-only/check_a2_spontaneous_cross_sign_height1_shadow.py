#!/usr/bin/env python3
"""Exact certificate for spontaneous-cross-sign-height1-shadow.md."""

import sympy as sp

x,y=sp.symbols("x y")
C1=101*x**2+4*x+4
H1=202500*x**4+C1*y**2
X=(205031250*x**6+2025*x**4*y**2-1822500*x**4*y
   +8100*x**3*y**2-99*x**2*y**4-1800*x**2*y**3
   +4050*x**2*y**2+4*x*y**4+4*y**4)
S=90*x*(225*x**2*(9*x-2)*(11*x+2)-C1*y)
Q1=(20252025*x**6+16200*x**5-9999*x**4*y**2-181800*x**4*y+48600*x**4
    +8*x**3*y**2-7200*x**3*y+64800*x**3
    +24*x**2*y**2-7200*x**2*y+32400*x**2
    +32*x*y**2+16*y**2)

assert sp.expand(S**2+2*C1**2*X-2*H1*Q1)==0

# H2 shadow identity from the earlier cross-sign proof, checked here for symmetry.
H2=(410062500*x**6-402975*x**4*y**2-7290000*x**4*y
    +8100*x**3*y**2+101*x**2*y**4+3600*x**2*y**3
    +40500*x**2*y**2+4*x*y**4+4*y**4)
L2=10*x*(2025*x**2-2*y**2-27*y)
assert sp.expand(2*X-2*H2+L2**2)==0

# Finite-field sanity: whenever H1=0 and C1,X are units, -2X is a square.
for p in list(sp.primerange(7,100)):
    if p%4!=3 or p in (3,5):
        continue
    for xv in range(1,p):
        for yv in range(1,p):
            vals={x:xv,y:yv}
            if int(H1.subs(vals))%p:
                continue
            cv=int(C1.subs(vals))%p
            xv_cross=int(X.subs(vals))%p
            if cv and xv_cross:
                target=(-2*xv_cross)%p
                assert pow(target,(p-1)//2,p)==1

print("OK: A2 cross-sign quadratic gate is an exact square shadow on H1 and H2")
