#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-central-23-norm.md."""

import sympy as sp

x,y=sp.symbols("x y")
H1=202500*x**4+(101*x**2+4*x+4)*y**2
H2=(410062500*x**6-402975*x**4*y**2-7290000*x**4*y
    +8100*x**3*y**2+101*x**2*y**4+3600*x**2*y**3
    +40500*x**2*y**2+4*x*y**4+4*y**4)
C23=(164025*x**4+656100*x**3+2381*x**2*y**2+41400*x**2*y
     +842400*x**2+324*x*y**2+324*y**2)

P1=(52862746561*x**8-297975024*x**7+3382320136*x**6
    -1007998624*x**5-296526576*x**4+68673664*x**3
    +46155008*x**2+9850880*x+2768896)
P2=(36718521895561*x**8+38488616399376*x**7+56248633454536*x**6
    +35159103841376*x**5+26427713499024*x**4+10019584910464*x**3
    +4638014590208*x**2+892499578880*x+250864746496)

assert sp.factor(sp.resultant(H1,C23,y))==4100625*x**4*P1
assert sp.factor(sp.resultant(H2,C23,y))==269042006250000*x**8*(25*x**2+1)**2*P2

D1=229919**2
A1=(52862746561*x**4-148987512*x**3+2287110116*x**2
    +681039760*x+382854784)
B1=1655416800*x**3+1636358400*x**2-5328000*x-2995200
assert sp.expand(A1**2-23*B1**2-D1*P1)==0

D2=6059581**2
A2=(36718521895561*x**4+19244308199688*x**3+23396680107716*x**2
    +6119130687760*x+3439943737984)
B2=(-1003466613600*x**3-1275716491200*x**2
    -600588144000*x-337627929600)
assert sp.expand(A2**2-23*B2**2-D2*P2)==0

fac1={2:38,3:8,5:12,13:2,19:6,23:2,101:2,12101:6}
fac2={2:36,3:10,5:8,11:6,13:2,23:8,83:6,101:2,251:1,6637:6,5419:1}

def prod(fac):
    z=1
    for p,e in fac.items(): z*=p**e
    return z

assert abs(int(sp.resultant(A1,B1,x)))==prod(fac1)
assert abs(int(sp.resultant(A2,B2,x)))==prod(fac2)
for q in set(fac1)|set(fac2):
    assert sp.isprime(q)

assert sp.factorint(229919)=={19:1,12101:1}
assert sp.factorint(6059581)=={11:1,83:1,6637:1}

# Every inert exceptional prime from the common-root resultants has 23 square.
for p in (19,11,83,251,5419):
    assert p%4==3
    assert sp.legendre_symbol(23,p)==1

# Central B_W equation: at K=9/2, F_W=-23/4 and K^2=81/4.
K=sp.Rational(9,2)
assert 5*K**2-36*K+55==-sp.Rational(23,4)
assert K**2==sp.Rational(81,4)

print("OK: A2 central moving-height exception is a signed Q(sqrt(23)) quartic norm")
