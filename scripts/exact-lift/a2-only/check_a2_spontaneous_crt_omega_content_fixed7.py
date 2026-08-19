#!/usr/bin/env python3
"""Certificate for spontaneous-crt-omega-content-fixed7.md."""

import sympy as sp

p=7
x,y,tau=sp.symbols('x y tau')
F=202500*x**4-(101*x**2+4*x+4)*y**2-1800*x**2*y
G=100*x**2*(5*(y+9)**2-36*(y+9)*tau+55*tau**2)-(x+2)**2*(2025*x**2+y**2)
C=2*(y+9)-9*tau

sol=[]
for tv in range(1,p):
    for xv in range(1,p):
        if (xv+2)%p==0:
            continue
        for yv in range(p):
            if int(F.subs({x:xv,y:yv}))%p==0 and int(G.subs({x:xv,y:yv,tau:tv}))%p==0 and int(C.subs({y:yv,tau:tv}))%p==0:
                sol.append((tv,xv,yv))
assert sol == [(4,1,2),(5,4,3)]

# Not on source y=225x^2.
for tv,xv,yv in sol:
    assert (yv-225*xv*xv)%p != 0

J=sp.Matrix([F,G,C]).jacobian([x,y,tau])
assert int(J.det().subs({x:1,y:2,tau:4}))%p==1
assert int(J.det().subs({x:4,y:3,tau:5}))%p==5

# Decimal tau phases.
phases={M:pow(pow(10,M,p),-1,p) for M in range(1,7)}
assert phases[2]==4
assert phases[1]==5
assert [M for M,v in phases.items() if v==4]==[2]
assert [M for M,v in phases.items() if v==5]==[1]

print('OK: fixed 7 omega-content descendant center has exactly two simple genuine states')
