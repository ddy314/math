#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-decimal-pair.md."""

import sympy as sp

# ----------------------------------------------------------------------
# Symbolic algebra.
D,g,omega,cu,q,W,N,K,z,EM,T,Q,a,b=sp.symbols(
    "D g omega cu q W N K z EM T Q a b"
)
A=g*omega
f=A+cu
P=6*K**2-36*K+55
F=5*K**2-36*K+55
BW=cu**2*P+A*(A-2*cu)*K**2
L=2*D*A*K-f*q*W
Rplus=D*F+K*N
Rminus=D*F-K*N

# qW=DK-N gives Rplus = D*P-K*qW.
assert sp.expand((D*P-K*q*W).subs(q*W,D*K-N)-Rplus)==0

# Exact source Bezout identity.
bez=sp.expand(
    cu**2*f*(D*P-K*q*W)
    -(D*f*BW-D*z*A**2*K**2+K*cu**2*L)
)
assert sp.factor(bez.subs(z,A-cu))==0

# ----------------------------------------------------------------------
# Decimalization.
alpha=T*K+a
beta=T*Q+b
Delta=K*b-Q*a
Eplus=F*beta+K*Delta
Eminus=F*beta-K*Delta

# Substitute alpha=omega W, beta=omega E_M D, Q=E_M q,
# then qW=DK-N.  The definitions of a,b are the corresponding
# concatenation remainders.
def decimalize(expr):
    out=sp.expand(expr.subs({a:omega*W-T*K,b:omega*EM*D-T*Q}))
    out=sp.expand(out.subs(Q,EM*q))
    out=sp.expand(out.subs(q*W,D*K-N))
    return sp.factor(out)

assert sp.factor(decimalize(Delta)-EM*N*omega)==0
assert sp.factor(decimalize(Eplus)-EM*omega*Rplus)==0
assert sp.factor(decimalize(Eminus)-EM*omega*Rminus)==0
assert sp.expand(Eplus-Eminus-2*K*Delta)==0

# ----------------------------------------------------------------------
# Exact rational endpoint bounds.
Nmin=10**11
slo=sp.Rational(2499,250)
shi=sp.Integer(10)
xplus_lo=sp.Rational(21,10)
xplus_hi=sp.Rational(40,19)
wmax=sp.Rational(843,1000)

# Main normalized term F*beta/(T*N^3).
main_lo=(5*slo**2-sp.Rational(360,Nmin))*xplus_lo
main_hi=(sp.Integer(500)+sp.Rational(55,Nmin**2))*(
    xplus_hi+wmax/sp.Integer(Nmin)
)

# |K*Delta|/(T*N^3) < s^2*w/N < 843/(10N).
gap_max=sp.Rational(843,10*Nmin)
assert main_lo-gap_max>1049
assert main_hi+gap_max<1053

# The E+ - E- gap bound: 2*K*Delta < 2*K^2*b
# with K<10N and b<843T/1000 gives 843/5*T*N^2.
assert 2*100*wmax==sp.Rational(843,5)

print("OK: A2 equal-depth resonance decimalizes to a near-equal asymmetric-depth pair")
