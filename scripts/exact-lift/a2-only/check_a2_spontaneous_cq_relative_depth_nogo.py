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

Jplus=sp.factor((-2*K)*sp.diff(cu*gplus,rho))
Jminus=sp.factor((-2*K)*sp.diff(cu*gminus,rho))
assert Jplus==-2*cu*K*A
assert Jminus==-2*cu*K*A
assert int(sp.resultant(A,2*Cplus,K))==-5060
assert int(sp.resultant(A,2*E,K))==-5060

# ---------------------------------------------------------------------------
# 2. p=23 first-layer / normalized gates
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

for coeff in sp.Poly(sp.expand(Aq-(1+14*kap)),kap).all_coeffs():
    assert int(coeff)%p==0
for coeff in sp.Poly(sp.expand(Cpq-17),kap).all_coeffs():
    assert int(coeff)%p==0
for coeff in sp.Poly(sp.expand(Eq-(16+9*kap)),kap).all_coeffs():
    assert int(coeff)%p==0

r=sp.symbols("r")
plus_norm=sp.expand(r*Aq+2*Cpq)
minus_norm=sp.expand(r*Aq-2*Eq)
plus_target=r*(1+14*kap)+11
minus_target=r*(1+14*kap)-9-18*kap
for coeff in sp.Poly(sp.expand(plus_norm-plus_target),kap,r).coeffs():
    assert int(coeff)%p==0
for coeff in sp.Poly(sp.expand(minus_norm-minus_target),kap,r).coeffs():
    assert int(coeff)%p==0

# kappa=18 is the projective pole; kappa=11 hits the primitive unit boundary.
assert (1+14*18)%p==0
assert 11%p!=0
assert (-9-18*18)%p!=0
assert ((-11)*pow(1+14*11,-1,p))%p == (-2)%p
assert (9+18*11)%p==0

# ---------------------------------------------------------------------------
# 3. The two Mobius charts are bijections onto rho != 0,-2
# ---------------------------------------------------------------------------
kap_domain=[k for k in range(p) if k not in (11,18)]
rho_target=set(range(1,p))-{p-2}

plus_image={(-11*pow(1+14*k,-1,p))%p for k in kap_domain}
minus_image={((9+18*k)*pow(1+14*k,-1,p))%p for k in kap_domain}
assert plus_image==rho_target
assert minus_image==rho_target
assert len(plus_image)==21
assert len(minus_image)==21

# Inverse formulas.
for rr in rho_target:
    kp=(-(rr+11)*pow(14*rr,-1,p))%p
    km=((9-rr)*pow(14*rr-18,-1,p))%p
    assert kp in kap_domain and km in kap_domain
    assert (-11*pow(1+14*kp,-1,p))%p==rr
    assert ((9+18*km)*pow(1+14*km,-1,p))%p==rr

# Blow-up Jacobian is a unit throughout the genuine depth>=2 chart.
for k in kap_domain:
    J=(-9*(1+14*k))%p
    assert J!=0

# ---------------------------------------------------------------------------
# 4. Prefix defect normalized equation at p^2
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
# 5. Decimal length lifting modulo 23^2
# ---------------------------------------------------------------------------
mod=p*p
assert sp.n_order(10,mod)==506
assert pow(10,22,mod)==1+8*p

length_data={}
for M0,h0 in ((5,15),(16,5)):
    vals=[]
    for j in range(23):
        M=M0+22*j
        N=pow(10,M,mod)
        h=((N*N-16)//p)%p
        assert h==(h0+3*j)%p
        # q1=0 when v_23(c_Q)>=2
        k=((16*h+22)*pow(9,-1,p))%p
        vals.append((M%506,k))
    length_data[M0]=vals

forced_depth_one=[]
for vals in length_data.values():
    forced_depth_one += [M for M,k in vals if k in (11,18)]
assert sorted(forced_depth_one)==[170,236,423,489]

print("OK: A2 fixed-23 chart corrected: depth-one vs depth-two is explicit, Mobius charts are bijective, and the blow-up is smooth")
