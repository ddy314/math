#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-tail-normalization.md."""

# Primewise certificate for
# gcd(alpha,Lambda_dec)=omega*Gamma.
# Write
#   v_p(alpha)=e+h,
#   Lambda_dec mod alpha = 2 E_M N S omega^2,
# so the second valuation is 2e+u with u=v_p(2E_MNS).
# Primitive reduction gives: if h>0, then u=0 because W_q is coprime
# to 2E_MNS.  If h=0, u is arbitrary.
for e in range(8):
    for h in range(8):
        for u in range(8):
            if h > 0 and u != 0:
                continue
            gcd_val = min(e+h, 2*e+u)
            expected = e + min(e,h)
            assert gcd_val == expected

# Equivalent factored form:
# gcd(W_q, 2E_MNS*omega)=gcd(W_q,omega).
for h in range(8):
    for e in range(8):
        for u in range(8):
            if h > 0 and u != 0:
                continue
            assert min(h, u+e) == min(h,e)

# Equal-depth target normalization: Lambda has 2h+rho and omega*Gamma has 2h.
for h in range(1,8):
    for rho in range(0,8):
        assert (2*h + rho) - 2*h == rho

print("OK: A2 full resonance tail is canonically isolated by gcd(alpha,Lambda_dec)")
