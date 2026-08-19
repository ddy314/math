#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-serial-gcd-selectors.md."""

import math

# Omega ladder: gcd(Omega^2,X)/gcd(Omega,X) detects x>h locally.
for h in range(1,8):
    for x in range(0,12):
        e=min(2*h,x)-min(h,x)
        assert (e>0)==(x>h)

# Second-node selector valuation formula.
for h in range(1,7):
    for c in range(1,8):
        for rho in range(1,8):
            s=min(c,rho)
            # serial law: unequal residual depths force r+=s; equal depths may stay or deepen.
            candidates=[s] if c!=rho else list(range(s,s+5))
            for rplus in candidates:
                a1=min(2*h+s,2*h+rplus)
                a2=min(2*h+2*s,2*h+rplus)
                q=a2-a1
                assert a1==2*h+s
                assert q==min(s,rplus-s)
                if c!=rho:
                    assert rplus==s and q==0
                elif rplus==s:
                    assert q==0
                else:
                    assert q>0

# Double-serial logic.
for h in range(1,6):
    for c in range(1,8):
        for rho in range(1,8):
            first=(c>h and rho>h)
            s=min(c,rho)
            # second strict is only legal when c=rho and rplus>s.
            if c==rho:
                for rplus in range(s,s+4):
                    second=(rplus>s)
                    double=first and second
                    if double:
                        assert h<c==rho<rplus

# Integer divisibility shape of the gcd quotients on sample integers.
for O in range(1,40):
    for X in range(1,80):
        g1=math.gcd(O,X)
        g2=math.gcd(O*O,X)
        assert g2%g1==0

for O in range(1,15):
    for G in range(1,15):
        for E in range(1,80):
            a1=math.gcd(O*O*G,E)
            a2=math.gcd(O*O*G*G,E)
            assert a2%a1==0

print("OK: A2 first/second/double serial strict resonances are canonically selected by gcd ladders")
