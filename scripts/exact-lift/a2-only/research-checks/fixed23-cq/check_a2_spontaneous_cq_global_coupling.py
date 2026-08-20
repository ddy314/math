#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-global-coupling.md."""

import sympy as sp

# ---------------------------------------------------------------------------
# 1. Q0-degenerate sphere factorization
# ---------------------------------------------------------------------------
x,s,zeta,u,n,cu,z=sp.symbols("x s zeta u n cu z")
w=sp.symbols("w")
f=z+2*cu

sphere=(
    x**2*w**2*(s+zeta)**2
    -(u+w)**2*(n*w**2+x**2*zeta**2)
)

sphere_sub=sp.factor(sphere.subs(w,cu*u/z))
reduced=sp.factor(
    u**2/z**4*(
        x**2*z**2*(cu*s-z*zeta)*(cu*s+f*zeta)
        -(z+cu)**2*n*cu**2*u**2
    )
)
assert sp.simplify(sphere_sub-reduced)==0

# ---------------------------------------------------------------------------
# 2. Integer branch factors = omega(H0 +/- Y3)
# ---------------------------------------------------------------------------
T,K,a3,omega,Wq,g=sp.symbols("T K a3 omega Wq g")
Rminus=T*cu*K-z*a3
Rplus=T*cu*K+(z+2*cu)*a3
Hminus=cu*Wq-g*a3
Hplus=cu*Wq+g*a3
subs={z:g*omega-cu,a3:omega*Wq-T*K}
assert sp.expand((Rminus-omega*Hminus).subs(subs))==0
assert sp.expand((Rplus-omega*Hplus).subs(subs))==0

# Important audit invariant: no symbolic identification of decimal N=10^M
# with the source quantity c_-^2 X occurs in this checker.

# ---------------------------------------------------------------------------
# 3. Two orientation-resolved additive bridges
# ---------------------------------------------------------------------------
S0=T*(K**2-26)-(2*K-9)*(2*a3+9*T)
A=K**2-18*K+55
E=K*(2*K-9)
Cplus=3*K**2-27*K+55
Gplus=(z+2*cu)*A+2*cu*E
Gminus=z*A-2*cu*E

assert sp.expand(
    (z+2*cu)*S0
    -(T*Gplus-2*(2*K-9)*Rplus)
)==0
assert sp.expand(
    z*S0
    -(T*Gminus+2*(2*K-9)*Rminus)
)==0

rho=sp.symbols("rho")
assert sp.expand(Gplus.subs(z,rho*cu)/cu-(rho*A+2*Cplus))==0
assert sp.expand(Gminus.subs(z,rho*cu)/cu-(rho*A-2*E))==0

# ---------------------------------------------------------------------------
# 4. Both orientations have the same ratio-degenerate resultant
# ---------------------------------------------------------------------------
res_plus=sp.resultant(A,2*Cplus,K)
res_minus=sp.resultant(A,2*E,K)
assert int(res_plus)==-5060
assert int(res_minus)==-5060
assert sp.factorint(abs(int(res_plus)))=={2:2,5:1,11:1,23:1}

for p in (11,23):
    roots_plus=[
        k for k in range(p)
        if int(A.subs(K,k))%p==0 and int(Cplus.subs(K,k))%p==0
    ]
    roots_minus=[
        k for k in range(p)
        if int(A.subs(K,k))%p==0 and int(E.subs(K,k))%p==0
    ]
    assert roots_plus==roots_minus

assert [k for k in range(11) if int(A.subs(K,k))%11==0 and int(E.subs(K,k))%11==0]==[0]
assert [k for k in range(23) if int(A.subs(K,k))%23==0 and int(E.subs(K,k))%23==0]==[16]

# p=11 cannot also satisfy K^2=8181*N_dec^2 with N_dec a unit.
assert 8181%11==8

# p=23 leaves N_dec^2=16 and exactly two decimal-length classes mod 22.
assert 8181%23==16
assert sp.n_order(10,23)==22
length_classes=[]
for M in range(1,23):
    Nmod=pow(10,M,23)
    if Nmod*Nmod%23==16:
        length_classes.append(M)
assert length_classes==[5,16]

# ---------------------------------------------------------------------------
# 5. Prefix defect and gate companion identities
# ---------------------------------------------------------------------------
B,Ndec=sp.symbols("B Ndec")
Dpref=2025*B**2+81*Ndec**2-K**2
assert sp.expand(Dpref.subs(B,-2*Ndec)-(8181*Ndec**2-K**2))==0
assert sp.factorint(8181)=={3:4,101:1}
assert 101%4==1

FW=5*K**2-36*K+55
assert sp.factor(FW)==(K-5)*(5*K-11)
assert sp.expand(Gplus-Gminus-2*cu*FW)==0
assert sp.expand(Gplus+Gminus-2*(z+cu)*A)==0

print("OK: corrected A2 pure-cQ coupling splits into symmetric c-/c+ orientations")
