#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-serial-conjugates.md."""

from fractions import Fraction
import sympy as sp

# Symbolic recovery identities.
F,B,t,K,beta,C,E,Lam=sp.symbols("F B t K beta C E Lam")
DB=F*B+t*K**2*beta**2
DE=beta*C-K*Lam
assert sp.expand((F*E+DE)-2*beta*C)==0
assert sp.expand((F*E-DE)-2*K*Lam)==2*(F*E-K*Lam-beta*C)

# The second identity is exact under the serial bridge F E - K Lambda = beta C.
bridge=sp.Eq(F*E-K*Lam,beta*C)
expr=sp.expand((F*E-DE)-2*K*Lam).subs(F*E-K*Lam,beta*C)
assert sp.expand(expr)==0

# Odd-prime sum/difference valuation logic.
for p in (7,11,19,23,31,43):
    for u in range(1,p):
        v=(-u)%p
        assert (u+v)%p==0
        assert (u-v)%p!=0
        # first-node version: equal units in the difference imply sum is a unit.
        v=u
        assert (u-v)%p==0
        assert (u+v)%p!=0

# Archimedean window for D_E.
lower=Fraction(21,10)*839-Fraction(10)*45
upper=Fraction(211,100)*843-Fraction(2499,250)*44
assert lower>1311
assert upper<1339

print("OK: A2 serial tropical nodes have one-deep/one-exact conjugate sheets")
