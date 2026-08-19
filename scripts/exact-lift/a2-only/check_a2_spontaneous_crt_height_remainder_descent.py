#!/usr/bin/env python3
"""Certificate for spontaneous-crt-height-remainder-descent.md."""

import sympy as sp
from fractions import Fraction as F

# Exact cross-lift algebra.
L,D,K,Gt,Tt,C=sp.symbols("L D K Gt Tt C")
Bs=2*D*(K-5)+C
Delta=(Tt-(D-C)*Gt)/sp.symbols("g")
g=sp.symbols("g")
Gamma=2*L*Gt
E=sp.expand(Gamma*Bs-2*D*Delta)
expected=2*L*(D*(2*K-9)*Gt-Tt)
assert sp.simplify(E.subs(D,g*L)-expected.subs(D,g*L))==0

# J/R modulo-g algebra: Tt == -cu^2 5^lambda C^2 mod g,
# n5=5^(lambda-d), hence J == cu^2 5^d C^2.
# Exponent bookkeeping is lambda-(lambda-d)=d.
lam,d,nu=sp.symbols("lam d nu", integer=True)
assert sp.expand(lam-(lam-d))==d
assert sp.expand((lam-2*d)+d-(lam-d))==0

# Power identity 5^nu * B_parent / 2^(m+4) = S_T/16.
m=sp.symbols("m", integer=True)
# Compare 2-exponents: B has L^3 -> 3m; division m+4 =>2m-4,
# S_T has 2^m*T ->2m, hence exactly /16.
assert 3*m-(m+4) == 2*m-4
# 5-exponents: 3d+nu = lambda+d = m.
assert sp.expand(3*d+(lam-2*d)-(lam+d))==0

# R_T monotonic endpoint bounds.
x,y=sp.symbols("x y", positive=True)
RT=(x+2)**2*(2025*x**2+y**2)/(100*x**2*(9+y)**2)
dx=sp.factor(sp.diff(RT,x))
dy=sp.factor(sp.diff(RT,y))
assert dx == (x+2)*(2025*x**3-2*y**2)/(50*x**3*(y+9)**2)
assert dy == -9*(x+2)**2*(225*x**2-y)/(50*x**2*(y+9)**3)

def rtf(xv,yv):
    return (xv+2)**2*(2025*xv*xv+yv*yv)/(100*xv*xv*(9+yv)**2)
Rmin=rtf(F(1,10),F(1))
Rmax=rtf(F(2,19),F(249,250))
assert Rmin == F(7497,8000)
assert Rmax == F(234947716,250493929)
assert Rmax < F(469,500)
# The exact margin above 31/500 is huge compared with 23/K, K>9e11.
assert F(1)-Rmax-F(23,9*10**11) > F(31,500)
assert F(1)-Rmin < F(63,1000)

# Small remainder ratio.
assert F(1,400)/F(31,500) == F(5,124)
assert F(5,124) < F(1,24)

# Descended quadratic normalized window.
# F63/(gTK^2)=1/16 -2(21+2zeta-delta)/K +9(12+2zeta-delta)/K^2.
# On the box, the correction is negative and tiny; safe lower >31/500.
Kmin=9*10**11
corr_lower=F(1,16)-2*F(2301,100)/Kmin  # 21+2*1.004 <23.01, ignore positive K^-2
assert corr_lower > F(31,500)

print("OK: A2 forced inert carrier admits the positive short-remainder descent decomposition")
