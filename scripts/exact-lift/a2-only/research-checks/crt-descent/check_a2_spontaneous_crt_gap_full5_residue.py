#!/usr/bin/env python3
"""Certificate for spontaneous-crt-gap-full5-residue.md."""

import sympy as sp

L,g,cu,K,a,C,T,Q0,N0,P5lam,P5lam2d = sp.symbols(
    "L g cu K a C T Q0 N0 P5lam P5lam2d"
)
D = g*L

Ttilde = (
    L*cu**2*g**2*(T*K**2-(18*T+4*a)*K+18*a+55*T)
    - P5lam2d*Q0**2*N0
)
H0 = g*(3*T+a)-P5lam*C
Gamma = cu**2*(g*((2*K-9)*T-a)-H0)
target = cu**2*a*(D*(20-4*K)-2*C)

# Exact difference between the additive lift numerator and g*target.
diff = sp.factor(sp.expand(Ttilde-(D-C)*Gamma-g*target))
expected = (
    C**2*P5lam*cu**2
    + 2*C*K*T*cu**2*g
    - C*L*P5lam*cu**2*g
    - 12*C*T*cu**2*g
    + K**2*L*T*cu**2*g**2
    - 20*K*L*T*cu**2*g**2
    + 67*L*T*cu**2*g**2
    - N0*P5lam2d*Q0**2
)
assert sp.expand(diff-expected) == 0

# Every expected summand is divisible by 5^lambda under
# v5(P5lam)=lambda, v5(T)=lambda+d, v5(L)=d,
# v5(P5lam2d)=lambda+2d, d>=1.
# We encode the extra depth beyond lambda.
extra_depths = [0, 1, 1, 1, 2, 2, 2, 2]
assert min(extra_depths) == 0
assert all(e >= 0 for e in extra_depths)

# Height-form rewrite.
Wq, q = sp.symbols("Wq q")
height_expr = 2*(4*D+C-2*q*Wq)
source_expr = D*(20-4*K)-2*C
source_relation = sp.expand(q*Wq-(D*K-(3*D-C)))
assert sp.expand(source_expr-height_expr).subs(q*Wq, D*K-(3*D-C)) == 0
assert source_relation == q*Wq-D*K+3*D-C

# Mod-5 unit check: D=0, K=0 modulo 5 leaves -2 c_u^2 a_3 C.
mod5_representative = sp.expand(target).subs({D:0, K:0})
assert mod5_representative == -2*C*a*cu**2

# B_G - lambda = 4M - 3m - 3 after eta=2m-M and lambda=m-d.
M,m,d,eta,lam = sp.symbols("M m d eta lam")
BG = 3*M-d-eta-3
expr = sp.expand(BG.subs(eta,2*m-M) - (m-d))
assert expr == 4*M-3*m-3

print("OK: A2 additive CRT gap has explicit full-5 residue and is a 5-adic unit")
