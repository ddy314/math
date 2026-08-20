#!/usr/bin/env python3
"""Exact certificate for spontaneous-denominator-depth-residuals.md."""

import sympy as sp

B, N, K = sp.symbols("B N K")

A = 2025*B**2 + 81*N**2
D = A - K**2
Pq = K**2 - 26
Pf = 3*K**2 - 36*K + 26
Rq = 8181*N**2 - 26
Q = B + 2*N

# q exact bridge.
assert sp.expand(Pq + D - Rq - 2025*Q*(B-2*N)) == 0
assert sp.diff(Rq, N) == 2*8181*N
assert sp.gcd(8181, 26) == 1
assert 8181 == 3**4 * 101

# f exact Bezout residual.
Cf = 3*A + 26
Uf = Cf + 36*K
Vf = 3*Uf - 1296
Rf = 9*A**2 - 1140*A + 676
assert sp.expand(Rf - (Pf + 3*D)*Uf + 1296*D) == 0
assert sp.expand(Rf - Pf*Uf - D*Vf) == 0

# Exact reductions modulo the common ideal (D,Pf):
# Uf = 72K and Vf = 216(K-6).
assert sp.expand(Uf - 72*K - (Pf + 3*D)) == 0
assert sp.expand(Vf - 216*(K-6) - 3*(Pf + 3*D)) == 0
assert Pf.subs(K, 0) == 26
assert Pf.subs(K, 6) == -82 == -2*41
assert 41 % 4 == 1

# f residual discriminant is unramified at every non-3 inert prime.
AA = sp.symbols("AA")
Rf_poly = 9*AA**2 - 1140*AA + 676
disc_Rf = sp.discriminant(Rf_poly, AA)
assert disc_Rf == 1275264
assert sp.factorint(disc_Rf) == {2: 7, 3: 5, 41: 1}
assert disc_Rf == 72**2 * 246

# Same quadratic square class as additive f-root.
disc_Pf = sp.discriminant(Pf, K)
assert disc_Pf == 984 == 4*246

print("OK: A2 denominator depth residuals certified")
