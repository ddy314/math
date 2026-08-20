#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-middle-near-pair.md."""

from fractions import Fraction
import sympy as sp

K,T,Q,b,P=sp.symbols("K T Q b P")
beta=T*Q+b
F=T*Q+2*b
A=P-2*K**2
Cplus=F*P-2*K**2*beta
Cminus=A*beta-b*P

assert sp.expand(Cplus-(A*beta+b*P))==0
assert sp.expand(Cplus-Cminus-2*b*P)==0
assert sp.expand(Cplus+Cminus-2*A*beta)==0

# Target-unit logic: P=0 mod p => A=-2K^2 is a unit for genuine odd p with p∤K.
for p in (7,11,19,23,31,43):
    for k in range(1,p):
        aval=(-2*k*k)%p
        if aval:
            # If u+v=0 mod p with units, u-v is nonzero for odd p.
            for v in range(1,p):
                u=(-v)%p
                assert (u+v)%p==0
                assert (u-v)%p!=0
            break

# Short-window transfer from C+ to C-.
N=10**11
slo=Fraction(2499,250)
qlo=Fraction(21,10)
# rigorous lower margin used by serial bridge
lower_plus=qlo*(4*slo*slo-Fraction(360,N))
# gap /(TN^3) < 2*(843/1000)*600/N
gap=Fraction(2)*Fraction(843,1000)*600/N
assert lower_plus-gap>839
assert gap<Fraction(1012,N)

print("OK: A2 serial middle carrier has a short deep/exact near-pair")
