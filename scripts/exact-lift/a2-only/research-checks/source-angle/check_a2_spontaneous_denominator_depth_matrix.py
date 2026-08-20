#!/usr/bin/env python3
"""Exact certificate for spontaneous-denominator-depth-matrix.md."""

import sympy as sp

x, y, t, w, z = sp.symbols("x y t w z")
N, B, Q, K, N0 = sp.symbols("N B Q K N0")

s = 9 + y
Nbar = 2025*x**2 + y**2
Delta0 = 2025*x**2 - 18*y - y**2
Pq = K**2 - 26
Pf = 3*K**2 - 36*K + 26

# Additive K quadratics are unramified at every non-3 inert prime.
assert sp.discriminant(Pq, K) == 104
assert sp.factorint(104) == {2: 3, 13: 1}
assert 13 % 4 == 1
assert sp.discriminant(Pf, K) == 984
assert sp.factorint(984) == {2: 3, 3: 1, 41: 1}
assert 41 % 4 == 1

# f-line+saturation remainder of the exact sphere.
S100 = sp.expand(
    100*x**2*w**2*(s+z)**2
    - (x+2+w)**2*(Nbar*w**2 + 100*x**2*z**2)
)
w0 = -(x+2)/2
z0 = -sp.Rational(9,2)*t
Rs = sp.expand(400*x**2*s*(s-9*t) - Nbar*(x+2)**2)
assert sp.factor(S100.subs({w:w0, z:z0}) - (x+2)**2*Rs/16) == 0

# Integer scaling of the sphere remainder.  Use independent abstract symbols
# so the checker does not depend on SymPy recognizing already-expanded
# Nbar or (x+2) as replaceable subexpressions.
X, S, TAU, NBAR = sp.symbols("X S TAU NBAR")
Rs_abs = 400*X**2*S*(S-9*TAU) - NBAR*(X+2)**2
Rs_dec = sp.cancel(Rs_abs.subs({
    X: B/N,
    S: K/N,
    TAU: 1/N,
    NBAR: 100*N0/N**2,
}))
expected_B = 100*(4*B**2*K*(K-9) - (B+2*N)**2*N0)/N**4
assert sp.cancel(Rs_dec - expected_B) == 0
# Q is exactly B+2N, so this is the claimed Q-form.
expected_Q = 100*(4*B**2*K*(K-9) - Q**2*N0)/N**4
assert sp.cancel(expected_Q.subs(Q, B+2*N) - expected_B) == 0

# Exact f-prefix bridge.
Psi = B**2*(K**2-26) - Q**2*N0
Rint = Q**2*N0 - 4*B**2*K*(K-9)
assert sp.expand(Psi + Rint + B**2*Pf) == 0

# q-side exact decimal-length bridge.
# K=N(9+y), B=Nx, Q=N(x+2).
qbridge = sp.expand(
    (N*s)**2 - 26
    + N**2*Delta0
    - (8181*N**2 - 26)
    - (N*(x+2))*(2025*N*(x+2)-8100*N)
)
assert sp.Poly(qbridge, x, y, N).is_zero

Rq = 8181*N**2 - 26
assert sp.diff(Rq, N) == 2*8181*N
assert sp.gcd(8181, 26) == 1

# f common character is a square shadow on Pf=0.
assert sp.expand((K**2-26) - 4*K*(K-9) + Pf) == 0

print("OK: A2 denominator prefix depth matrix certified")
