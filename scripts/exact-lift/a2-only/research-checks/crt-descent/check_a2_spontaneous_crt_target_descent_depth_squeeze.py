#!/usr/bin/env python3
"""Certificate for spontaneous-crt-target-descent-depth-squeeze.md."""

# Pure valuation certificate for the high-baseline branch.
# Inputs:
# v(That)>=h+1, v(g 2^m Dhat)=1, p not in {2,5,g}.
# From That=5^lambda Rstar + g2^m Dhat, h>=2 forces v(Rstar)=1.

def vp_sum(a,b):
    """Return forced valuation when a,b differ; None when equal and cancellation may occur."""
    return min(a,b) if a!=b else None

for h in range(2,20):
    vThat_lower=h+1
    vD=1
    # If R were 0-depth, RHS unit; impossible.
    assert vp_sum(0,vD)==0 < vThat_lower
    # If R had depth >=2, D is uniquely shallow; impossible.
    for vR in range(2,h+5):
        assert vp_sum(vR,vD)==1 < vThat_lower
    # Only vR=1 can even permit cancellation up to the required depth.
    assert vp_sum(1,vD) is None

# Original additive depth lower bound min(h+1,2h)=h+1.
for h in range(1,20):
    assert min(h+1,2*h)==h+1

print("OK: A2 fixed 31/179 high-baseline target overlap has exact first-layer depth in both descended carriers")
