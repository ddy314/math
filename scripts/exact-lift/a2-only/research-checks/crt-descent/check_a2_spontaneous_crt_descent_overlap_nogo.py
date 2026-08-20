#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descent-overlap-nogo.md."""

import sympy as sp

K,C,T,a,g,cu,Am,Vd,Pl,Q0,N0 = sp.symbols(
    "K C T a g cu Am Vd Pl Q0 N0"
)
Trel = Am*Vd*Pl

F16 = 16*(2*K-9)*(g*((2*K-12)*T-2*a)+Pl*C)-63*g*T*K**2
R16 = (
    Am**2*Vd*cu**2*g**2*(15*K**2+384*K-848)
    -16*Am*g*cu**2*C*(2*K-9)
    -16*Vd*Q0**2*N0
)
That = (
    Am*cu**2*g**2*(T*K**2-(18*T+4*a)*K+18*a+55*T)
    - (Am*Vd)**1 * Pl * Q0**2*N0
)
# Since 5^m = Am? No: T=Am*5^m, and 5^m=Vd*Pl.
That = (
    Am*cu**2*g**2*(T*K**2-(18*T+4*a)*K+18*a+55*T)
    - Vd*Pl*Q0**2*N0
)

resC = sp.factor(sp.resultant(F16, R16, C).subs(T, Trel))
expectedC = sp.factor(256*(2*K-9)*That.subs(T,Trel))
assert sp.expand(resC-expectedC) == 0

# K-resultant discriminant factorization. Remove the obvious scalar factor first.
resK = sp.factor(sp.resultant(F16, R16, K).subs(T,Trel))
# Treat the resultant as polynomial in C and compute its discriminant.
polyC = sp.Poly(resK, C)
discC = sp.factor(sp.discriminant(polyC.as_expr(), C))
H63 = cu**2*g**2*(26*Trel**2+18*Trel*a+4*a**2) + (Vd*Pl)**2*Q0**2*N0
sqfac = 1270*Am**2*cu**2*g**2 - N0*Q0**2
# The discriminant has a large scalar square from the resultant's content.
# Check the squarefree/nontrivial factor after removing all perfect-square factors symbolically.
ratio = sp.factor(discC / (Pl**2 * cu**2 * sqfac**2 * H63))
# Remaining ratio must be a perfect square monomial/constant.
fac = sp.factor_list(ratio)
const, factors = fac
assert const > 0
assert all(exp % 2 == 0 for _, exp in factors)

# Square collapse of H63 on That=0.
base = Trel*K**2-(18*Trel+4*a)*K+18*a+55*Trel
collapse = sp.expand(
    26*Trel**2+18*Trel*a+4*a**2 + Trel*base - (Trel*K-9*Trel-2*a)**2
)
assert collapse == 0

# Pure-prefix rescaling of the second singular square factor:
# Am*cu*g = B/2^(M+1), Q0=Q/2^(M+1), hence common denominator yields 1270 B^2-Q^2 N0.
B,Q,U = sp.symbols("B Q U")
expr = (1270*Am**2*cu**2*g**2-N0*Q0**2).subs({Am*cu*g:B/U,Q0:Q/U})
assert sp.factor(expr*U**2) == 1270*B**2-Q**2*N0

print("OK: A2 Rstar/D63 resultants are syzygetic generically; only the two singular gates remain")
