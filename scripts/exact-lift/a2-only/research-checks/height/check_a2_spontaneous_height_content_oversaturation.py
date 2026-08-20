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
Eomega=6*cu**2*W*(T*K-6*T-a)+g*T**2*K**2*(g*omega-2*cu)
bridge=sp.expand((T**2*BW_source-cu**2*R).subs(a,omega*W-T*K)-omega*Eomega.subs(a,omega*W-T*K))
assert sp.factor(bridge)==0

# At an omega-height common prime (omega=W=0 mod p), E is a unit
# once p does not divide 2*g*cu*T*K.
assert sp.expand(Eomega.subs({omega:0,W:0}))==-2*g*cu*T**2*K**2

# For inert p != 3, (6/p)=-1 occurs exactly in the 7,11 mod 24 classes.
assert sp.legendre_symbol(6,7)==-1
assert sp.legendre_symbol(6,11)==-1
assert sp.legendre_symbol(6,19)==1
assert sp.legendre_symbol(6,23)==1

# The decimal-window constants come from T <= a < 10T:
# 6*(4T)^2+T^2 = 97T^2 and 6*(13T)^2+T^2 = 1015T^2.
assert 6*4**2+1==97
assert 6*13**2+1==1015

# ----------------------------------------------------------------------
# Exact decimal determinant for omega.
# Write E_M=2^(M+1)c_Q abstractly as EM, so Q=EM*q and S=EM*D.
EM,S,beta,b=sp.symbols("EM S beta b")
det=K*b-Q*a
det0=sp.expand(det.subs({a:omega*W-T*K,b:omega*S-T*Q}))
det1=sp.expand(det0.subs({Q:EM*q,S:EM*D}))
det2=sp.expand(det1.subs(q*W,D*K-N))
assert sp.factor(det2-EM*N*omega)==0

# ----------------------------------------------------------------------
# Pure-prefix height gate and resultant.
B,Q,N0=sp.symbols("B Q N0")
beta=T*Q+b
alpha=T*K+a
H3=N0*b**2+B**2*a**2
Hpref=B**2*K**2+Q**2*N0
Epref=B**2*K*alpha+N0*Q*beta

assert sp.expand(
    T**2*Hpref
    - (H3+2*T*Epref-B**2*alpha**2-N0*beta**2)
)==0

X,Y=sp.symbols("X Y")
Hp=X*K**2+Y
Rpref=3025*X**2+636*X*Y+36*Y**2
assert sp.factor(sp.resultant(P,Hp,K)-Rpref)==0
assert sp.expand(Rpref-((55*X-6*Y)**2+1296*X*Y))==0
assert sp.expand(Rpref-((6*Y+53*X)**2+216*X**2))==0
assert sp.factor(sp.discriminant(Rpref,Y)+31104*X**2)==0
assert 31104==6*72**2

Lpref=sp.expand(X*P-6*Hp)
assert sp.expand(Lpref-(-36*X*K+55*X-6*Y))==0
assert sp.expand(
    Rpref-(1296*X*Hp+2*(55*X-6*Y)*Lpref-Lpref**2)
)==0

# 2-adic primitive orientation:
# B=2^(M+m+1)b0, Q=2^(M+1)Q0, with b0,Q0,N0 odd.
# After division by 2^(4M+6), the exact quotient is
# 9 Q0^4 N0^2 + 159*2^(2m)b0^2 Q0^2 N0
# + 3025*2^(4m-2)b0^4.
# Check the only delicate case m=1 modulo 8; m>=2 is immediate.
b0,Q0,n0=sp.symbols("b0 Q0 n0", integer=True)
for bv in (1,3,5,7):
    for qv in (1,3,5,7):
        for nv in (1,3,5,7):
            rhat_m1=(
                9*qv**4*nv**2
                +159*2**2*bv**2*qv**2*nv
                +3025*2**2*bv**4
            )
            assert rhat_m1%8==1

# Exact rational bounds used for the 8M+2 digit window.
n0_min=sp.Rational(81,400)+sp.Rational(249**2,250**2*100)
n0_max=sp.Rational(81,361)+sp.Rational(1,100)
assert n0_min>sp.Rational(53,250)
assert n0_max==sp.Rational(8461,36100)

Ymin=sp.Rational(21,10)**2*sp.Rational(53,250)
Ymax=sp.Rational(40,19)**2*n0_max
assert Ymin>sp.Rational(93,100)
assert Ymax<sp.Rational(26,25)

# Lower coefficient >31.
assert 36*sp.Rational(93,100)**2>31
# Upper leading coefficient leaves margin 39/625.
lead=36*sp.Rational(26,25)**2
assert 39-lead==sp.Rational(39,625)
# With X/N^2 < 4/361, the lower-order coefficients are <8 and <1.
assert 636*sp.Rational(4,361)*sp.Rational(26,25)<8
assert 3025*sp.Rational(4,361)**2<1
# N>=10^11 makes their relative contribution far below the remaining margin.
Nmin=10**11
assert sp.Rational(8,Nmin**2)+sp.Rational(1,Nmin**4)<sp.Rational(39,625)

print("OK: A2 omega-height oversaturation transfers to a fixed-length pure-prefix norm")
