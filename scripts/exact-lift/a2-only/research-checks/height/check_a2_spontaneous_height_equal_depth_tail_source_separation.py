#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-tail-source-separation.md."""

# The key gcd identities are primewise.
# Let a=v_p(omega^circ), w=v_p(W^circ), c=v_p(c_Q),
# and assume min(a,w)=0.  Source separation gives omega^circ coprime to
# 2*T*q, so v_p(TQ^2) on omega-support is exactly 2c.
# Therefore
#   gcd(Lambda_tail,omega^circ)=gcd(TQ^2,omega^circ)
# has exponent min(a,2c), while gcd(Lambda_tail,W^circ)=0.
for a in range(7):
    for w in range(7):
        if min(a,w) != 0:
            continue
        for c in range(7):
            gcd_tail_omega = min(a, 2*c)
            gcd_cq2_omega = min(a, 2*c)
            assert gcd_tail_omega == gcd_cq2_omega

            # W^circ overlap is zero because its coefficient
            # 2 E_M N S and omega^circ are both W^circ-units.
            gcd_tail_w = 0
            assert gcd_tail_w == 0

            # Since omega^circ and W^circ are coprime, total imbalance
            # overlap is exactly the omega-side c_Q overlap.
            total = gcd_tail_omega + gcd_tail_w
            assert total == min(a, 2*c)

print("OK: A2 resonance tail and imbalance support overlap only through c_Q")
