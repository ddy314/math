#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-double-serial-budget.md."""

# Pure valuation certificate for double-serial weighted budgets.
for h in range(1,8):
    for c in range(h+1,h+7):
        rho=c
        for rplus in range(c+1,c+7):
            vC=h+c
            vL=2*h+c
            vD=2*h+c
            vE=2*h+rplus
            assert vC>=2*h+1
            assert vL>=3*h+1
            assert vD>=3*h+1
            assert vE>=3*h+2
            assert vE>=vD+1

# Aggregate-exponent bookkeeping: p^(3h+2)=p^(3h)*p^2,
# and p^(2h+c+1) contains p^(2h+c) times one radical layer.
for h in range(1,10):
    for c in range(h+1,h+10):
        assert 3*h+2 <= 2*h+(c+1)
        assert 3*h+1 <= 2*h+c

print("OK: A2 double-serial targets pay triple-baseline plus double-radical depth in E_+")
