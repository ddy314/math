#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-content-oversaturation.md."""

import sympy as sp

D,g,omega,K,f,q,W,N,z,cu=sp.symbols("D g omega K f q W N z cu")
L=D*z*K+f*N

# qW=DK-N and z+f=2g omega.
expr=sp.expand(L.subs(N,D*K-q*W)- (2*D*g*omega*K-f*q*W))
expr=sp.expand(expr.subs(z+f,2*g*omega))
# direct substitution is more reliable
expr2=sp.expand(L.subs({N:D*K-q*W,z:g*omega-cu,f:g*omega+cu})-(2*D*g*omega*K-(g*omega+cu)*q*W))
assert expr2==0

P=6*K**2-36*K+55
assert sp.discriminant(P,K)==-24

BW=cu**2*(5*K**2-36*K+55)+z**2*K**2
assert sp.expand(BW.subs(z,-cu)-cu**2*P)==0

DW=55*z**2-49*cu**2
assert sp.expand(DW.subs(z,-cu)-6*cu**2)==0

# No non-3 odd ramification.
assert sp.factorint(abs(int(sp.discriminant(P,K))))=={2:3,3:1}

print("OK: A2 height companion oversaturation reduces to simple omega-content quadratic")
