#!/usr/bin/env python3
"""Certificate for spontaneous-crt-floorfree-modulus-overlap.md."""

import sympy as sp
from fractions import Fraction as F

D,C,K,T,a,cu,z = sp.symbols("D C K T a cu z")
Ns=3*D-C
DDelta=cu**2*(
    D**2*(T*K**2-14*K*T-4*K*a+37*T+14*a)
    +D*Ns*(-2*K*T+7*T+2*a)
    +T*Ns**2
)-z**2*Ns*(T*Ns+2*a*D)

F2=cu**2*(T*K**2-(18*T+4*a)*K+55*T+18*a)-4*z**2*(T+a)
F4=cu**2*(T*K**2-(22*T+4*a)*K+81*T+22*a)-8*z**2*(2*T+a)
R2=C*T*(cu**2-z**2)+2*D*K*T*cu**2-12*D*T*cu**2+5*D*T*z**2-2*D*a*cu**2+2*D*a*z**2
R4=C*T*(cu**2-z**2)+2*D*K*T*cu**2-14*D*T*cu**2+7*D*T*z**2-2*D*a*cu**2+2*D*a*z**2

assert sp.expand(DDelta-(D**2*F2+(C-D)*R2)) == 0
assert sp.expand(DDelta-(D**2*F4+(C+D)*R4)) == 0

# Rational endpoint bounds for F2/(cu^2 T N^2), F4/(...).
N=10**11
slo,shi=F(2499,250),F(10)
xlo,xhi=F(1,10),F(2,19)
wlo,whi=F(837,1000),F(843,1000)
zlo,zhi=F(1),F(251,250)

f2_lo=slo**2-(F(18)+4*zhi)*shi/F(N)-4*((F(2)+xhi)/wlo)**2*(1+zhi)
f2_hi=shi**2+(55+18*zhi)/F(N*N)-4*((F(2)+xlo)/whi)**2*(1+zlo)
assert f2_lo > 49
assert f2_hi < 51

f4_lo=slo**2-(F(22)+4*zhi)*shi/F(N)-8*((F(2)+xhi)/wlo)**2*(2+zhi)
f4_hi=shi**2+(81+22*zhi)/F(N*N)-8*((F(2)+xlo)/whi)**2*(2+zlo)
assert f4_lo > -53
assert f4_hi < -48

# D-C and D+C are coprime because D even, C odd, gcd(C,D)=1:
# gcd(D-C,D+C)=gcd(D-C,2C)=1. Algebraic linear combination sanity.
assert sp.expand((D+C)-(D-C)-2*C) == 0

print("OK: A2 floor-free CRT/modulus overlap pays full depth to F2 or F4")
