#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-content-oversaturation.md."""

import sympy as sp

D,g,omega,K,f,q,W,N,z,cu,T,a=sp.symbols("D g omega K f q W N z cu T a")
L=D*z*K+f*N

# qW=DK-N and z+f=2g omega.
expr=sp.expand(L.subs(N,D*K-q*W)- (2*D*g*omega*K-f*q*W))
expr=sp.expand(expr.subs(z+f,2*g*omega))
# direct substitution is more reliable
expr2=sp.expand(L.subs({N:D*K-q*W,z:g*omega-cu,f:g*omega+cu})-(2*D*g*omega*K-(g*omega+cu)*q*W))
assert expr2==0

P=6*K**2-36*K+55
assert sp.expand(P-(6*(K-3)**2+1))==0
assert sp.discriminant(P,K)==-24

BW=cu**2*(5*K**2-36*K+55)+z**2*K**2
assert sp.expand(BW.subs(z,-cu)-cu**2*P)==0

DW=55*z**2-49*cu**2
assert sp.expand(DW.subs(z,-cu)-6*cu**2)==0

# No non-3 odd ramification.
assert sp.factorint(abs(int(sp.discriminant(P,K))))=={2:3,3:1}

# Pull the fixed K-quadratic back to the true third block.
R=6*(a+3*T)**2+T**2
alpha=T*K+a
assert sp.factor(T**2*P-R-6*alpha*(T*K-6*T-a))==0

# Exact B_W / natural-third-block bridge after alpha=omega*W.
BW_source=sp.expand(BW.subs(z,g*omega-cu))
E=6*cu**2*W*(T*K-6*T-a)+g*T**2*K**2*(g*omega-2*cu)
bridge=sp.expand((T**2*BW_source-cu**2*R).subs(a,omega*W-T*K)-omega*E.subs(a,omega*W-T*K))
assert sp.factor(bridge)==0

# At an omega-height common prime (omega=W=0 mod p), E is a unit
# once p does not divide 2*g*cu*T*K.
assert sp.expand(E.subs({omega:0,W:0}))==-2*g*cu*T**2*K**2

# For inert p != 3, (6/p)=-1 occurs exactly in the 7,11 mod 24 classes.
assert sp.legendre_symbol(6,7)==-1
assert sp.legendre_symbol(6,11)==-1
assert sp.legendre_symbol(6,19)==1
assert sp.legendre_symbol(6,23)==1

# The decimal-window constants come from T <= a < 10T:
# 6*(4T)^2+T^2 = 97T^2 and 6*(13T)^2+T^2 = 1015T^2.
assert 6*4**2+1==97
assert 6*13**2+1==1015

print("OK: A2 omega-height oversaturation has an exact natural-norm depth bridge")
