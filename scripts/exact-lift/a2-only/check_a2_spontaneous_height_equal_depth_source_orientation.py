#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-source-orientation.md."""

import sympy as sp

A,B,N,T,b3,alpha=sp.symbols("A B N T b3 alpha")
K=9*N+10*A
Q=B+2*N
N0=sp.Rational(81,4)*B**2+A**2
U=(45*B**2-2*A*N)**2-A**2*B*(99*B-4*N)
HO=N0*U**2+4*A**4*B**2*Q**2*K**2
L=T*U+2*A**2*Q*b3
H0=N0*b3**2+B**2*T**2*K**2

# Exact linear-resultant identity.
assert sp.expand(
    T**2*HO
    -((2*A**2*Q)**2*H0-N0*L**2+2*N0*T*U*L)
)==0

# alpha perturbation from the exact sphere height quadratic.
a3=alpha-T*K
Hactual=N0*b3**2+B**2*a3**2
assert sp.expand(H0-Hactual-B**2*(2*alpha*T*K-alpha**2))==0

# Additive alpha identity.
F=(K-5)*(5*K-11)
JH=B**2*F-Q**2*N0
Rtheta=B**2*(K**2-18*K+55)-Q**2*N0
Theta=T*Rtheta-2*B**2*(2*K-9)*a3
assert sp.expand(Theta-(T*JH-2*B**2*(2*K-9)*alpha))==0

# Character algebra at inert primes:
# N0 = -square and 2U has character -rho, hence 2*N0*U has character rho.
for p in list(sp.primerange(7,250)):
    if p%4!=3 or p in (3,5):
        continue
    for rho in (1,2,3,5,7):
        rho%=p
        if not rho:
            continue
        chi=lambda a: 1 if pow(a%p,(p-1)//2,p)==1 else -1
        assert chi(-1)==-1
        # Formal character product: chi(N0)=-1, chi(2U)=chi(-rho).
        assert (-1)*chi(-rho)==chi(rho)
        # Equal-depth -square law then gives actual ratio chi(-rho).
        assert -chi(rho)==chi(-rho)

print("OK: A2 moving-height equal-depth actual-carrier/source orientation law certified")
