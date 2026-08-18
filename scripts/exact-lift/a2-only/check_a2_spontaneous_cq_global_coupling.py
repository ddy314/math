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

alpha_relation={a3:omega*Wq-T*K}
source_relation={z:g*omega-cu}

Rminus=T*cu*K-z*a3
Rplus=T*cu*K+(z+2*cu)*a3
Hminus=cu*Wq-g*a3
Hplus=cu*Wq+g*a3

expr_minus=sp.expand((Rminus-omega*Hminus).subs(source_relation).subs(alpha_relation))
expr_plus=sp.expand((Rplus-omega*Hplus).subs(source_relation).subs(alpha_relation))
assert expr_minus==0
assert expr_plus==0

# ---------------------------------------------------------------------------
# 3. Additive bridge
# ---------------------------------------------------------------------------
S0=T*(K**2-26)-(2*K-9)*(2*a3+9*T)
GcQ=(z+2*cu)*(K**2-18*K+55)+2*cu*K*(2*K-9)
Rplus_raw=(z+2*cu)*a3+T*cu*K

assert sp.expand(
    (z+2*cu)*S0
    -(T*GcQ-2*(2*K-9)*Rplus_raw)
)==0

GcQ_alt=z*(K**2-18*K+55)+2*cu*(3*K**2-27*K+55)
assert sp.expand(GcQ-GcQ_alt)==0

# ---------------------------------------------------------------------------
# 4. First-layer ratio degeneracy
# ---------------------------------------------------------------------------
A=K**2-18*K+55
C=3*K**2-27*K+55
res=sp.resultant(A,2*C,K)
assert int(res)==-5060
assert sp.factorint(abs(int(res)))=={2:2,5:1,11:1,23:1}

common_roots={}
for p in (11,23):
    roots=[]
    for k in range(p):
        if int(A.subs(K,k))%p==0 and int(C.subs(K,k))%p==0:
            roots.append(k)
    common_roots[p]=roots

assert common_roots[11]==[0]
assert common_roots[23]==[16]

# p=11 cannot also satisfy K^2 = 8181 N^2 with N a unit.
assert 8181%11==8

# p=23 leaves N^2=16, hence exactly two length classes mod ord_23(10)=22.
assert 8181%23==16
assert pow(16,2,23)==3
assert sp.n_order(10,23)==22
length_classes=[]
for M in range(1,23):
    Nmod=pow(10,M,23)
    if Nmod*Nmod%23==16:
        length_classes.append(M)
assert length_classes==[5,16]

# ---------------------------------------------------------------------------
# 5. Prefix defect at x=-2
# ---------------------------------------------------------------------------
B,N=sp.symbols("B N")
Dpref=2025*B**2+81*N**2-K**2
assert sp.expand(Dpref.subs(B,-2*N)-(8181*N**2-K**2))==0
assert sp.factorint(8181)=={3:4,101:1}
assert 101%4==1

print("OK: A2 pure-cQ sphere/additive coupling reduces to a simple source-prefix system")
