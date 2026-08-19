#!/usr/bin/env python3
"""Finite/simple-root certificate for spontaneous-height-equal-depth-fixed7-hensel.md."""

import sympy as sp

# Exceptional K root and its unique lift mod 49.
P=lambda k: 6*k*k-36*k+55
roots49=[k for k in range(49) if P(k)%49==0]
assert roots49==[23,32]
assert 23%7==2
assert (12*2-36)%7==2
assert pow(23,-1,49)==32

# Derivatives of the four surviving B roots mod 7.
B=sp.symbols("B")
F1=4*B**2+(B+6)**2*(B**2+1)   # M=1: N=3,A=1
F5=4*B**2+(B+10)**2*(B**2+4)  # M=5: N=5,A=2
assert int(sp.diff(F1,B).subs(B,2))%7==2
assert int(sp.diff(F1,B).subs(B,4))%7==3
assert int(sp.diff(F5,B).subs(B,1))%7==3
assert int(sp.diff(F5,B).subs(B,3))%7==4

# Mod-49 sanity: every M phase already allowed mod 7 has exactly two B lifts.
inv10=pow(10,-1,49)
inv2=pow(2,-1,49)
for Mmod in range(42):
    N=pow(10,Mmod,49)
    A=((23-9*N)*inv10)%49
    roots=[]
    for b in range(1,49):
        if b%7==0:
            continue
        Q=(b+2*N)%49
        if Q%7==0:
            continue
        N0=(((9*b*inv2)%49)**2 + A*A)%49
        if N0%7==0:
            continue
        H=(b*b*23*23 + Q*Q*N0)%49
        if H==0:
            roots.append(b)
    if Mmod%6 in (1,5):
        assert len(roots)==2
    else:
        assert len(roots)==0

print("OK: A2 fixed 7 prefix branch has two simple Hensel orbits per allowed phase")
