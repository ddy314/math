#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-equal-depth-orthogonal-decimal-norm.md."""

import sympy as sp

D,N,K,T,EM,om,Q,a3 = sp.symbols("D N K T EM om Q a3", integer=True)
alpha,beta,Delta,U,Rp,c = sp.symbols("alpha beta Delta U Rp c", integer=True)

P = 6*K**2 - 36*K + 55
RPD = 55*D**2 - 36*D*N + 6*N**2
u3 = a3 + 3*T
LD3 = T*(55*D - 18*N) - 6*N*nu3
Lperp = (55*D - 18*N)*nu3 + N*T

# Raw norm identities.
assert sp.expand(55*RPD - ((55*D-18*N)**2 + 6*N**2)) == 0
assert sp.expand(RPD*(55) * (T**2 + 6*nu3**2) - (LD3**2 + 6*Lperp**2)) == 0

# Source identity for the orthogonal cross carrier.
U_expr = D*K - N
Rp_expr = D*P - K*U_expr
alpha_expr = T*K + a3
orth_rhs = (55*D-18*N)*alpha + 3*T*Rp + T*(53-15*K)*U
check = sp.expand(Lperp - orth_rhs)
check = check.subs({alpha: alpha_expr, Rp: Rp_expr, U: U_expr})
assert sp.expand(check) == 0

# Decimal scaling relations: cD=beta, cN=Delta, cU=Qalpha, cRp=Eplus.
Eplus = sp.symbols("Eplus", integer=True)
XiPD = 55*beta**2 - 36*beta*Delta + 6*Delta**2
Xipar = 55*T*beta - 36*T*Delta - 6*a3*Delta
Xiperp = (55*beta - 18*Delta)*(a3+3*T) + Delta*T

# Check direct scaling by substituting beta=cD, Delta=cN.
assert sp.expand(XiPD.subs({beta:c*D, Delta:c*N}) - c**2*RPD) == 0
assert sp.expand(Xipar.subs({beta:c*D, Delta:c*N}) - c*LD3) == 0
assert sp.expand(Xiperp.subs({beta:c*D, Delta:c*N}) - c*Lperp) == 0

# Decimal norm identity.
R3 = 6*(a3+3*T)**2 + T**2
assert sp.expand(55*XiPD*R3 - Xipar**2 - 6*Xiperp**2) == 0

# Positive form for XiPD.
assert sp.expand(XiPD - (beta**2 + 6*(Delta-3*beta)**2)) == 0
assert sp.expand(55*XiPD - ((55*beta-18*Delta)**2 + 6*Delta**2)) == 0

# Corrected parallel form.  Use Delta=K beta-Q alpha and Eplus=(P-K^2)beta+K Delta.
FH = P-K**2
Eplus_expr = FH*beta + K*Delta
corr = T*(Eplus_expr - (5*K-36)*Q*alpha) - 6*Delta*alpha
corr = sp.expand(corr - Xipar)
corr = corr.subs({Delta: K*beta-Q*alpha, alpha:T*K+a3})
assert sp.expand(corr) == 0

# Bezout for the orthogonal extra-depth coefficient.
assert sp.expand(75*P + (74-30*K)*(15*K-53) - 203) == 0
assert 203 == 7*29
assert 29 % 24 == 5

# Mod-7 P roots and complementary exceptional roots.
roots7 = [k for k in range(7) if int(P.subs(K,k)) % 7 == 0]
assert roots7 == [2,4]
# RPD extra coefficient after U=0 is 36-11K; orthogonal coefficient is 15K-53.
assert (36-11*2) % 7 == 0
assert (36-11*4) % 7 != 0
assert (15*2-53) % 7 != 0
assert (15*4-53) % 7 == 0

print("OK: A2 source/third equal-depth carriers form an exact decimal orthogonal norm with complementary fixed-7 roots")
