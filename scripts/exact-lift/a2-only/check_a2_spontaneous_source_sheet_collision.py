#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-sheet-collision.md."""

import sympy as sp

y,t,x = sp.symbols("y t x")

E = sp.expand(
    11000*t**2*y + 9900000*t**2
    + 84609*t*y**2 - 3240000*t*y - 29160000*t
    - 19404*y**3 - 10836*y**2 + 1474200*y
)
O = sp.expand(
    5500*t**2 - 2691*t*y - 16200*t
    + 296*y**2 + 1764*y - 8100
)
Qy = sp.expand(
    2461063649*y**4 + 234628417800*y**3
    + 4390818840000*y**2 + 17723448000000*y
    - 144342000000000
)
Qt = sp.expand(
    7444717538225*t**4 + 119322760549410*t**3
    + 292869540803250*t**2 + 743568561885024*t
    - 87085495164087
)

assert sp.factor(sp.resultant(E,O,t) + 550000*(y+9)**2*Qy) == 0
assert sp.factor(sp.resultant(E,O,y) + 1000000*t**2*Qt) == 0

# y=-9 is only tau=0 for genuine non-3 inert primes.
assert sp.factor(E.subs(y,-9)) == 81*t*(121000*t+84609)
assert sp.factor(O.subs(y,-9)) == 11*t*(500*t+729)
assert sp.resultant(121000*t+84609,500*t+729,t) == 45904500
assert sp.factorint(45904500) == {2:2,3:2,5:3,101:2}

# Archimedean interval: Qy is increasing for y>0 and remains negative at y=1.
assert all(c > 0 for c in sp.Poly(sp.diff(Qy,y),y).all_coeffs())
assert int(Qy.subs(y,1)) == -121990643678551

# Singular bad-prime data.
assert sp.factorint(abs(int(sp.discriminant(Qy,y)))) == {
    2:32,3:32,5:25,101:7,113:1,7437536446892971:1
}
assert sp.factorint(2461063649) == {11:2,1609:1,12641:1}

J = sp.expand(sp.diff(E,y)*sp.diff(O,t)-sp.diff(E,t)*sp.diff(O,y))
sol11=[]
for yy in range(11):
    for tt in range(11):
        if int(E.subs({y:yy,t:tt})) % 11 == 0 and int(O.subs({y:yy,t:tt})) % 11 == 0:
            sol11.append((yy,tt,int(J.subs({y:yy,t:tt}))%11))
assert sol11 == [(2,0,0),(3,3,6),(5,9,1)]

p = 7437536446892971
assert sp.isprime(p) and p % 4 == 3
G = sp.gcd(sp.Poly(Qy,y,modulus=p),sp.Poly(sp.diff(Qy,y),y,modulus=p))
assert G.monic().as_expr() == sp.Poly(y+2367909658823161,y,modulus=p).monic().as_expr()
y0 = 5069626788069810
Gt = sp.gcd(sp.Poly(E.subs(y,y0),t,modulus=p),sp.Poly(O.subs(y,y0),t,modulus=p))
assert Gt.degree() == 1
t0 = 1327194327136915
assert int(E.subs({y:y0,t:t0})) % p == 0
assert int(O.subs({y:y0,t:t0})) % p == 0
assert pow(y0,(p-1)//2,p) == 1

Ey=int(sp.diff(E,y).subs({y:y0,t:t0}))%p
Et=int(sp.diff(E,t).subs({y:y0,t:t0}))%p
Oy=int(sp.diff(O,y).subs({y:y0,t:t0}))%p
Ot=int(sp.diff(O,t).subs({y:y0,t:t0}))%p
assert (Ey,Et,Oy,Ot) == (
    4769546899604225,5300490912652323,
    2429430622649786,4767246607889802
)
lam=Oy*pow(Ey,-1,p)%p
assert lam == 6415545761503029
assert (lam*Et-Ot)%p == 0

e1=(int(E.subs({y:y0,t:t0}))//p)%p
o1=(int(O.subs({y:y0,t:t0}))//p)%p
assert (e1,o1)==(1149464242486028,2576181903398455)
assert (lam*e1-o1)%p == 762004648349653

# Product identity in the source square quotient.
C = sp.expand(
    440*(x+2)**2*t**2
    + 81*(9401*x**4-2392*x**3-1600*x**2-64*x-64)*t
    - 324*x*(99*x-4)*(25*x**2+1)*(49*x**2-4*x-2)
)
prod = sp.expand(5625**2*C*C.subs(x,-x) - (E**2-14400*y*O**2))
assert sp.rem(prod,225*x**2-y,x) == 0

print("OK: A2 source conjugate-sheet collision audit certified")
