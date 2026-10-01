#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0327; see history/sources.json.
"""

import math
import sympy as sp

X,Y=sp.symbols('X Y')
H4=2*3**12*13*(X+Y)**4-5**4*11**4*Y**4
compact=26*(27*(X+Y))**4-(55*Y)**4
assert sp.expand(H4-compact)==0

# For p=3 mod4, QR has odd order, so fourth powers equal squares.
# Finite checks over representative small primes sanity-check the group statement.
for p in list(sp.primerange(7,300)):
    if p%4!=3 or p in (13,):
        continue
    sq={pow(a,2,p) for a in range(1,p)}
    fourth={pow(a,4,p) for a in range(1,p)}
    assert sq==fourth

# Character classes modulo lcm(8,13)=104.
classes=[]
for a in range(1,104):
    if math.gcd(a,104)==1 and a%4==3 and sp.jacobi_symbol(26,a)==1:
        classes.append(a)
assert classes==[11,19,23,55,59,67,79,83,87,95,99,103]

# Direct implication: if H4(x,y)=0 with all shown denominators units,
# the fourth power of 55Y/[27(X+Y)] equals +26.
for p in list(sp.primerange(7,250)):
    if p%4!=3 or p in (13,):
        continue
    for x in range(1,p):
        for y in range(1,p):
            if (x+y)%p==0:
                # Then H4=-(55y)^4 is a unit for p!=5,11.
                if p not in (5,11):
                    assert (26*pow(27*(x+y),4,p)-pow(55*y,4,p))%p!=0
                continue
            if (26*pow(27*(x+y),4,p)-pow(55*y,4,p))%p==0 and p not in (5,11):
                ratio=55*y*pow(27*(x+y),-1,p)%p
                assert pow(ratio,4,p)==26%p
                assert sp.legendre_symbol(26,p)==1

print('OK: actual strict terminal overdepth forces +26 to be a fourth power, equivalently (26/p)=+1 for inert p')
