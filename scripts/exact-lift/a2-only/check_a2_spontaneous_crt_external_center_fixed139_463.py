#!/usr/bin/env python3
"""Certificate for spontaneous-crt-external-center-fixed139-463.md."""

import sympy as sp


def order10(p: int) -> int:
    x = 1
    for d in range(1, p):
        x = x * 10 % p
        if x == 1:
            return d
    raise AssertionError


def solutions(p: int):
    ord10 = order10(p)
    out = []
    s = 36 % p
    for n in range(ord10):
        Ys = (11 - 9*s) % p
        y = Ys * pow(s, -1, p) % p
        for x in range(1,p):
            if (x+2) % p == 0:
                continue
            Nsp = ((x+2)**2*(2025*s*s*x*x+Ys*Ys)+10780*x*x) % p
            if Nsp:
                continue
            Asp = (4*(225*s*x*x+9*s-11)**2 - x*Ys*Ys*(99*x-4)) % p
            rhs = (-2*x*Ys*Ys*(x+2)) % p
            if Asp == 0:
                continue
            r = rhs * pow(Asp,-1,p) % p
            if (55*r*r*(x+2)**2 - 49*x*x) % p:
                continue
            out.append((n+1,s,x,y,r)) # M=n+1
        s = s*10 % p
    return out

assert order10(139)==46
assert order10(463)==154
assert solutions(139)==[(44,94,124,34,41)]
assert solutions(463)==[(140,141,299,349,458),(147,172,328,376,416)]

# Genuine separation factors.
for p, states in [(139,solutions(139)),(463,solutions(463))]:
    for M,s,x,y,r in states:
        phi=((99*x-4)*r-2*x-4)%p
        fline=(r*(x+2)+2*x)%p
        assert x%p and (x+2)%p and y%p and phi and fline

# Quoted values.
assert ((99*124-4)*41-2*124-4)%139 == 137
assert (41*(124+2)+2*124)%139 == 132
assert ((99*299-4)*458-2*299-4)%463 == 36
assert (458*(299+2)+2*299)%463 == 19
assert ((99*328-4)*416-2*328-4)%463 == 318
assert (416*(328+2)+2*328)%463 == 425

# Full Jacobians.
s,x,r=sp.symbols('s x r')
Ys=11-9*s
Nsp=(x+2)**2*(2025*s**2*x**2+Ys**2)+10780*x**2
Osp=r*(4*(225*s*x**2+9*s-11)**2-x*Ys**2*(99*x-4))+2*x*Ys**2*(x+2)
Gsp=55*r**2*(x+2)**2-49*x**2
J=sp.Matrix([Nsp,Osp,Gsp]).jacobian([s,x,r])
assert int(J.det().subs({s:94,x:124,r:41}))%139 == 111
assert int(J.det().subs({s:141,x:299,r:458}))%463 == 397
assert int(J.det().subs({s:172,x:328,r:416}))%463 == 159

# Non-Wieferich exponent directions.
assert ((pow(10,46,139**2)-1)//139)%139 == 43
assert ((pow(10,154,463**2)-1)//463)%463 == 217

print('OK: external-center descendant support has one simple 139 orbit and two simple 463 orbits')
