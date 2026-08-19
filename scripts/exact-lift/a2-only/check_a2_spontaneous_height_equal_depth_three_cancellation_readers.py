#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-three-cancellation-readers.md."""

import sympy as sp

K,T,Q,b3,P,beta,alpha = sp.symbols("K T Q b3 P beta alpha")
FH=P-K**2
Delta=K*beta-Q*alpha
Fdec=T*Q+2*b3
Bdec=b3**2*FH+T**2*Q**2*K**2
Eplus=FH*beta+K*Delta
Lambda=2*beta*Delta+T*Q**2*alpha

# Exact two-term forms, using beta=TQ+b3 for Bdec/Lambda simplifications.
expr=Bdec-(b3**2*P+K**2*(T*Q-b3)*beta)
assert sp.factor(expr.subs(beta,T*Q+b3)) == 0
assert sp.expand(Eplus-(P*beta-K*Q*alpha)) == 0
expr=Lambda-(2*K*beta**2-Q*Fdec*alpha)
assert sp.factor(expr.subs(beta,T*Q+b3)) == 0

# First normalized rank-2 system over several finite fields.
# Variables are units b,K,Q,beta0; derive P0 and A0 from B/E equations,
# then verify the tail equation automatically.
for p in (7,11,31,43,59):
    for b in range(1,min(p,8)):
        for kval in range(1,min(p,8)):
            for q in range(1,min(p,8)):
                for bet0 in range(1,min(p,8)):
                    P0=(2*kval*kval*bet0*pow(b,-1,p))%p
                    A0=(bet0*P0*pow((kval*q)%p,-1,p))%p
                    # B first digit.
                    assert (b*P0-2*kval*kval*bet0)%p==0
                    # E+ first digit.
                    assert (bet0*P0-kval*q*A0)%p==0
                    # Tail first digit follows.
                    assert (2*kval*bet0*bet0-q*b*A0)%p==0

print("OK: A2 B_dec, E+, Lambda_dec are exact two-term readers and the first tail digit is rank-2 shadow")
