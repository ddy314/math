#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-relative-depth-nogo.md."""

import sympy as sp

# ---------------------------------------------------------------------------
# 1. Generic Jacobian
# ---------------------------------------------------------------------------
K,rho,cu=sp.symbols("K rho cu")
A=K**2-18*K+55
Cplus=3*K**2-27*K+55
E=K*(2*K-9)
gplus=rho*A+2*Cplus
gminus=rho*A-2*E

# D_pref has d/dK=-2K and no rho dependence.
Jplus=sp.factor((-2*K)*sp.diff(cu*gplus,rho))
Jminus=sp.factor((-2*K)*sp.diff(cu*gminus,rho))
assert Jplus==-2*cu*K*A
assert Jminus==-2*cu*K*A

assert int(sp.resultant(A,2*Cplus,K))==-5060
assert int(sp.resultant(A,2*E,K))==-5060

# ---------------------------------------------------------------------------
# 2. p=23 first-layer data
# ---------------------------------------------------------------------------
p=23
assert 8181%p==16
assert sp.n_order(10,p)==22
assert [M for M in range(1,23) if pow(10,M,p)**2%p==16]==[5,16]

kap=sp.symbols("kap")
K23=16+p*kap
Aq=sp.expand(A.subs(K,K23)/p)
Cpq=sp.expand(Cplus.subs(K,K23)/p)
Eq=sp.expand(E.subs(K,K23)/p)

# Quotients modulo 23.
assert sp.Poly(sp.expand(Aq-(1+14*kap)),kap).all_coeffs()[0] % p == 0
for coeff in sp.Poly(sp.expand(Aq-(1+14*kap)),kap).all_coeffs():
    assert int(coeff)%p==0
for coeff in sp.Poly(sp.expand(Cpq-17),kap).all_coeffs():
    assert int(coeff)%p==0
for coeff in sp.Poly(sp.expand(Eq-(16+9*kap)),kap).all_coeffs():
    assert int(coeff)%p==0

# Normalized gate formulas modulo 23.
r=sp.symbols("r")
plus_norm=sp.expand(r*Aq+2*Cpq)
minus_norm=sp.expand(r*Aq-2*Eq)
plus_target=r*(1+14*kap)+11
minus_target=r*(1+14*kap)-9-18*kap
for coeff in sp.Poly(sp.expand(plus_norm-plus_target),kap,r).coeffs():
    assert int(coeff)%p==0
for coeff in sp.Poly(sp.expand(minus_norm-minus_target),kap,r).coeffs():
    assert int(coeff)%p==0

# The shared forbidden correction kappa=18.
assert (1+14*18)%p==0
assert 11%p!=0
assert (-9-18*18)%p!=0

# ---------------------------------------------------------------------------
# 3. Prefix defect normalized equation at p^2
# ---------------------------------------------------------------------------
n1,t=sp.symbols("n1 t")
for n0 in (4,19):
    N=n0+p*n1
    Q=p*t
    Dpref=8181*N**2-K23**2+2025*Q*(Q-4*N)
    hN=sp.expand((N**2-16)/p)
    target=16*hN+22-9*kap-4*n0*t
    diff=sp.expand(Dpref/p-target)
    for coeff in sp.Poly(diff,kap,n1,t).coeffs():
        assert int(coeff)%p==0

# ---------------------------------------------------------------------------
# 4. Decimal length lifting modulo 23^2
# ---------------------------------------------------------------------------
mod=p*p
assert sp.n_order(10,mod)==506
assert pow(10,22,mod)==1+8*p

for M0,h0 in ((5,15),(16,5)):
    for j in range(23):
        M=M0+22*j
        N=pow(10,M,mod)
        h=((N*N-16)//p)%p
        assert h==(h0+3*j)%p

print("OK: A2 pure-cQ generic derivative route is smooth; fixed 23 has explicit p^2 compatibility")
