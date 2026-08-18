#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-primary-bridge.md."""

import sympy as sp

A,B,N,T,Q,b3,D = sp.symbols("A B N T Q b3 D")

U = (45*B**2-2*A*N)**2 - A**2*B*(99*B-4*N)
O = sp.expand(T*U + 2*A**2*Q*b3)
Ssrc = sp.expand(T*B*(99*B-4*N) - 2*Q*b3)

# Q=B+2N is the exact decimal denominator block.
assert sp.expand(
    Ssrc.subs(Q,B+2*N)
    - (T*B*(99*B-4*N)-2*(B+2*N)*b3)
) == 0

# Raw angle-source bridge.
assert sp.expand(
    O - (T*(45*B**2-2*A*N)**2 - A**2*Ssrc)
) == 0

# D_src = 81 B^2/4 - 9 A N/10, hence 45B^2-2AN = 20D/9.
Dsrc = sp.Rational(81,4)*B**2 - sp.Rational(9,10)*A*N
assert sp.factor(45*B**2-2*A*N-sp.Rational(20,9)*Dsrc) == 0
assert sp.factor(
    81*O - (400*T*Dsrc**2 - 81*A**2*Ssrc)
) == 0

# Source Hensel integer: with x=B/N and r=BT/b3,
# N*b3*Phi = Ssrc after Q=B+2N.
x = B/N
r = B*T/b3
Phi = (99*x-4)*r - 2*x - 4
assert sp.cancel(N*b3*Phi-Ssrc.subs(Q,B+2*N)) == 0

print("OK: A2 source primary / prefix / angle integer bridge certified")
