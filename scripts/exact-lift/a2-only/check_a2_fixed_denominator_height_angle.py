#!/usr/bin/env python3
"""Exact finite certificate for fixed-denominator-height-angle.md."""

import sympy as sp

x,y,t = sp.symbols("x y t")
s = y+9
center = 2*s-9*t
Delta = 2025*x**2-18*y-y**2
Lf = 200*x**2*(s-9*t)-y*(x+2)**2

# q-side p=23: x=-2.
p=23
qstates=[]
for yy in range(p):
    for tt in range(1,p):
        if int(center.subs({y:yy,t:tt}))%p==0 and int(Delta.subs({x:-2,y:yy}))%p==0:
            qstates.append((yy,tt))
assert qstates == [(10,17),(18,6)]

Jq = sp.det(sp.Matrix([
    [sp.diff(center,y),sp.diff(center,t)],
    [sp.diff(Delta,y),sp.diff(Delta,t)],
]))
for yy,tt in qstates:
    assert int(Jq.subs({x:-2,y:yy,t:tt}))%p != 0
assert sp.n_order(10,23)==22
assert pow(10,-16,23)==6
assert pow(10,-5,23)==17

# f-side systems and Jacobian.
Jf = sp.det(sp.Matrix([
    [sp.diff(center,v) for v in (x,y,t)],
    [sp.diff(Delta,v) for v in (x,y,t)],
    [sp.diff(Lf,v) for v in (x,y,t)],
]))

def enumerate_f(p):
    out=[]
    for xx in range(p):
        for yy in range(p):
            for tt in range(1,p):
                if (int(center.subs({y:yy,t:tt}))%p==0
                    and int(Delta.subs({x:xx,y:yy}))%p==0
                    and int(Lf.subs({x:xx,y:yy,t:tt}))%p==0):
                    out.append((xx,yy,tt))
    return out

s7=enumerate_f(7)
assert s7 == [(0,0,2),(4,6,1)]
assert int(Jf.subs({x:4,y:6,t:1}))%7 == 4
assert sp.n_order(10,7)==6
assert pow(10,-6,7)==1

s43=enumerate_f(43)
assert s43 == [(0,0,2),(5,37,15),(18,33,38)]
assert int(Jf.subs({x:5,y:37,t:15}))%43 == 4
assert int(Jf.subs({x:18,y:33,t:38}))%43 == 3
assert sp.n_order(10,43)==21
assert pow(10,-10,43)==15
assert pow(10,-8,43)==38

# The fixed K-center is exactly why only these primes appear.
K=sp.Rational(9,2)
Pq=K**2-26
Pf=3*K**2-36*K+26
assert Pq == -sp.Rational(23,4)
assert Pf == -sp.Rational(301,4)
assert sp.factorint(301)=={7:1,43:1}

print("OK: A2 fixed 7/23/43 denominator-height-angle templates certified")
