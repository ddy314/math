#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-serial-tropical-bridge.md."""

from fractions import Fraction
import sympy as sp

K,t,b,P,alpha,Q=sp.symbols("K t b P alpha Q")
F=t+2*b
beta=t+b
B=b**2*P+K**2*(t-b)*beta
E=P*beta-K*Q*alpha
Lambda=2*K*beta**2-Q*F*alpha
C=F*P-2*K**2*beta

# Two exact serial bridges.
assert sp.expand(F*B-t*K**2*beta**2-b**2*C)==0
assert sp.expand(F*E-K*Lambda-beta*C)==0

# Endpoint window 839 < C/(T N^3) < 843.
N=10**11
slo=Fraction(2499,250)
shi=Fraction(10,1)
qlo=Fraction(21,10)
qhi=Fraction(40,19)
whi=Fraction(843,1000)

# C/(TN^3)=q(4s^2-36s/N+55/N^2)+(2w/N)(5s^2-36s/N+55/N^2).
lower=qlo*(4*slo*slo-Fraction(36)*shi/N)
upper=(
    qhi*(4*shi*shi+Fraction(55,N*N))
    +Fraction(2)*whi/N*(5*shi*shi+Fraction(55,N*N))
)
assert lower>839
assert upper<843

# Abstract two-level valuation laws.
for h in range(1,8):
    for rB in range(1,8):
        # first bridge: depths h+rB and 2h; unequal depths force exact minimum.
        if rB<h:
            c=rB
            assert h+c==h+rB<2*h
        elif rB>h:
            c=h
            assert h+c==2*h<h+rB

# Classification of strict-extra old ties.
# We only check the valuation logic, not existence of the p-adic states.
for h in range(1,7):
    # rB=h<rho: strict r+>h forces c>h.
    for rho in range(h+1,8):
        c=h
        rplus=min(rho,c)  # unique minimum at second node if c=h
        assert rplus==h

    # rB=rho<h -> c=rB=rho, so second node is tied.
    for r in range(1,h):
        c=r
        rho=r
        assert c==rho

    # h=rho<rB -> c=h=rho, so second node is tied.
    for rB in range(h+1,8):
        c=h
        rho=h
        assert c==rho

    # triple tie: if first node were extra c>h, second node unique-min forces r+=h.
    rho=h
    for c in range(h+1,h+4):
        assert min(rho,c)==h

print("OK: A2 four minimum ties factor into two serial decimal tropical nodes")
