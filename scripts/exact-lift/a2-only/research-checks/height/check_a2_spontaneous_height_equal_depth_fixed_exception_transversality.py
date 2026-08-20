#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-fixed-exception-transversality.md."""

import sympy as sp

# Exact Bezout identities.
D,N,K=sp.symbols("D N K", integer=True)
RPD=55*D**2-36*D*N+6*N**2
F7=36*D-11*N
assert sp.expand(1296*RPD-(1980*D-691*N)*F7-175*N**2)==0

P=6*K**2-36*K+55
F2671=5*K-36
assert sp.expand(25*P-(30*K+36)*F2671-2671)==0

# p=7 first-layer root and distinct mod-49 lifts.
p=7
mod=p*p
d0=4
assert (55*d0*d0-36*d0+6)%p==0
assert (36*d0-11)%p==0
assert (110*d0-36)%p!=0
# Hensel lift of quadratic.
q=((55*d0*d0-36*d0+6)//p)%p
t=(-q*pow((110*d0-36)%p,-1,p))%p
dR=(d0+p*t)%mod
dF=(11*pow(36,-1,mod))%mod
assert dR==32
assert dF==18
assert dR!=dF
assert (55*dR*dR-36*dR+6)%mod==0
assert (36*dF-11)%mod==0
assert (1980*d0-691)%p==5

# p=2671 first-layer root and distinct p^2 lifts.
p=2671
mod=p*p
k0=2144
Pfun=lambda x: 6*x*x-36*x+55
dP=lambda x: 12*x-36
assert Pfun(k0)%p==0
assert (5*k0-36)%p==0
assert dP(k0)%p!=0
assert (30*k0+36)%p==252
q=(Pfun(k0)//p)%p
t=(-q*pow(dP(k0)%p,-1,p))%p
kP=(k0+p*t)%mod
kF=(36*pow(5,-1,mod))%mod
assert kP==2825391
assert kF==5707400
assert kP!=kF
assert Pfun(kP)%mod==0
assert (5*kF-36)%mod==0
assert ((kP-kF)//p)%p==1592

# Normalized transverse units from the Bezout identity.
assert ((5*kP-36)//p)%p==2618
assert pow(25,-1,p)==2030
assert (Pfun(kF)//p)%p==2030

print("OK: A2 fixed 7/2671 exceptional roots are transverse after the first p-adic layer")
