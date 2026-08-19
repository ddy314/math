#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-fixed-second-layer-squeeze.md."""

import sympy as sp

D,N,K,T,alpha,U,Rp = sp.symbols("D N K T alpha U Rp", integer=True)
P = 6*K**2 - 36*K + 55
RPD = 55*D**2 - 36*D*N + 6*N**2
U_expr = D*K - N
Rp_expr = D*P - K*U_expr

# Three exact exceptional-direction identities.
F7 = 36*D - 11*N
expr = RPD - (D*Rp + F7*U - 5*U**2)
expr = sp.expand(expr.subs(U,U_expr).subs(Rp,Rp_expr))
assert expr == 0

Lperp = (55*D-18*N)*(alpha-T*K+3*T) + N*T
Fperp = 53 - 15*K
rhs_perp = (55*D-18*N)*alpha + 3*T*Rp + T*Fperp*U
expr = Lperp-rhs_perp
expr = sp.expand(expr.subs(U,U_expr).subs(Rp,Rp_expr))
assert expr == 0

LD3 = T*(55*D-18*N) - 6*N*(alpha-T*K+3*T)
Fstar = 5*K - 36
rhs_par = T*Rp - T*Fstar*U - 6*N*alpha
expr = LD3-rhs_par
expr = sp.expand(expr.subs(U,U_expr).subs(Rp,Rp_expr))
assert expr == 0

# Bezout identities certifying one p-adic layer on h>=2 branches.
assert sp.expand(1296*RPD-(1980*D-691*N)*F7-175*N**2) == 0
assert sp.expand(75*P + (74-30*K)*(15*K-53) - 203) == 0
assert sp.expand(25*P-(30*K+36)*Fstar-2671) == 0
assert 203 == 7*29

# Hensel lifts for the two mod-7 P roots.
def lift_root(poly, var, root, p):
    der = sp.diff(poly,var)
    q = (int(poly.subs(var,root))//p) % p
    t = (-q * pow(int(der.subs(var,root)) % p, -1, p)) % p
    return root + p*t

k2 = lift_root(P,K,2,7)
k4 = lift_root(P,K,4,7)
assert k2 % 49 == 23
assert k4 % 49 == 32
assert int(P.subs(K,k2)) % 49 == 0
assert int(P.subs(K,k4)) % 49 == 0

# K=2 branch: U=0 mod49 gives D/N=K^{-1}=32 mod49.
d2 = pow(k2,-1,49)
assert d2 == 32
assert ((36*d2-11)//7) % 7 == 2
assert d2 % 7 == 4

# K=4 branch: orthogonal coefficient has exact first normalized digit 2.
assert ((53-15*k4)//7) % 7 == 2

# 2671 quadratic branch normalized transverse digit.
p=2671
k0=2144
kp=lift_root(P,K,k0,p) % (p*p)
assert kp == 2825391
assert ((5*kp-36)//p) % p == 2618
assert (-2618) % p == 53

# Verify the published normalized ratios algebraically modulo the primes.
# root K=2: 4 R1 + 2 U0 =0 <=> 2R1+U0=0.
for R1 in range(7):
    for U0 in range(1,7):
        assert ((4*R1+2*U0) % 7 == 0) == ((2*R1+U0) % 7 == 0)
# root K=4: 3R1+2U0.
# 2671: R1-2618U0 = R1+53U0.
for U0 in (1,2,17,2669):
    for R1 in (0,1,53,1000,2670):
        assert (R1-2618*U0) % p == (R1+53*U0) % p

print("OK: A2 fixed exceptional directions obey the h>=2 second-layer squeeze and fixed normalized ratios")
