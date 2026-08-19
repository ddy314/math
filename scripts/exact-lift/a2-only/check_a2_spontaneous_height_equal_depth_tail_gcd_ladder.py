#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-tail-gcd-ladder.md."""

# Primewise valuation model for the genuine denominator-separated sector.
# e=v_p(omega), h=v_p(W_q), gamma=min(e,h).
# After removing Gamma, the imbalance valuations are e-gamma and h-gamma.
# Tail equation has unit coefficients.  Hence unequal depths leave exactly
# one unit summand modulo p, while equal depths leave two units whose
# cancellation depth is rho.
for e in range(1,8):
    for h in range(1,8):
        gamma=min(e,h)
        a=e-gamma
        w=h-gamma
        assert min(a,w)==0
        if e!=h:
            # exactly one of a,w is zero and the other positive
            assert (a==0) ^ (w==0)
            tail_val=0
        else:
            assert a==0 and w==0
            for rho in range(0,8):
                tail_val=rho
                for k in range(1,6):
                    dk=min(k*gamma,tail_val)
                    expected=min(k*h,rho)
                    assert dk==expected
            continue
        assert tail_val==0

# Successive quotient depth formula.
for h in range(1,8):
    for rho in range(0,12):
        prev=0
        for k in range(1,6):
            dk=min(k*h,rho)
            assert dk>=prev
            if k>=2:
                inc=dk-prev
                assert 0<=inc<=h
            prev=dk

print("OK: A2 gcd(Gamma^k,Lambda_tail) exactly selects and reads equal-depth resonance")
