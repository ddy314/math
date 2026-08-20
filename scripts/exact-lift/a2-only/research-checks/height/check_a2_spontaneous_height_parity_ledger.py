#!/usr/bin/env python3
"""Exact certificate for spontaneous-height-parity-ledger.md."""

import sympy as sp

A,B,N,T,a3,b3,omega,Wq,R = sp.symbols(
    "A B N T a3 b3 omega Wq R", nonzero=True
)
x,y,t,w,z = sp.symbols("x y t w z")

Q = B + 2*N
K = 9*N + 10*A
N0 = sp.Rational(81,4)*B**2 + A**2
U = (45*B**2-2*A*N)**2 - A**2*B*(99*B-4*N)

Oplus = T*U + 2*A**2*Q*b3
Ominus = T*U - 2*A**2*Q*b3
Rtheta = B**2*(K**2-18*K+55) - Q**2*N0
Theta = T*Rtheta - 2*B**2*(2*K-9)*a3
JH = B**2*(5*K**2-36*K+55) - Q**2*N0

# Additive-height bridge after alpha=TK+a3=omega*Wq.
a3_sub = omega*Wq - T*K
assert sp.expand(
    Theta.subs(a3,a3_sub)
    - (T*JH - 2*B**2*(2*K-9)*omega*Wq)
) == 0

# Actual/conjugate angle sheets.
assert sp.expand(Oplus-Ominus-4*A**2*Q*b3) == 0

HO = sp.expand(N0*U**2 + 4*A**4*B**2*Q**2*K**2)
base_diff = sp.expand(T**2*HO - N0*Oplus*Ominus)
base_grouped = 4*A**4*Q**2*(b3**2*N0+B**2*T**2*K**2)
assert sp.factor(base_diff-base_grouped) == 0

# Height square: b3^2*N0+B^2*a3^2=(R*Wq)^2, R=B*c_u/g.
# And alpha=TK+a3=omega*Wq. Verify the two substitutions in grouped form,
# avoiding fragile AST substitution after expand().
height_after_square = 4*A**4*Q**2*(
    R**2*Wq**2 + B**2*((omega*Wq-a3)**2-a3**2)
)
height_claimed = 4*A**4*Q**2*Wq*(
    Wq*(R**2+B**2*omega**2)-2*B**2*omega*a3
)
assert sp.expand(height_after_square-height_claimed) == 0

# Pure-prefix orientation factorization.
H1 = sp.expand(
    2025*B**4 + 101*A**2*B**2 + 4*A**2*B*N + 4*A**2*N**2
)
H2 = sp.expand(
    404*A**4*B**2 + 16*A**4*B*N + 16*A**4*N**2
    + 1440*A**3*B**2*N - 16119*A**2*B**4
    + 324*A**2*B**3*N + 1620*A**2*B**2*N**2
    - 29160*A*B**4*N + 164025*B**6
)
assert sp.expand(H1*H2 - 4*HO) == 0

# Normalized geometry: angle root + height root zeta=-s factors exactly H1(x,y)H2(x,y).
s = y+9
Nnorm = 2025*x**2+y**2
d = 225*x**2-y
Asp = 4*d**2 - x*y**2*(99*x-4)
Aminus = Asp - 2*y**2*(x+2)**2
w0 = -Asp/(2*y**2*(x+2))
S = sp.expand(
    x**2*w**2*(s+z)**2
    - (x+2+w)**2*(Nnorm*w**2/100 + x**2*z**2)
)
H1n = 202500*x**4 + 101*x**2*y**2 + 4*x*y**2 + 4*y**2
H2n = (
    410062500*x**6 - 402975*x**4*y**2 - 7290000*x**4*y
    + 8100*x**3*y**2 + 101*x**2*y**4 + 3600*x**2*y**3
    + 40500*x**2*y**2 + 4*x*y**4 + 4*y**4
)
rem = sp.factor(S.subs({w:w0,z:-s}))
expected = -Aminus**2*H1n*H2n/(1600*y**8*(x+2)**4)
assert sp.factor(rem-expected) == 0

# Scaling identities for H1/H2.
assert sp.factor(H1n.subs({x:B/N,y:10*A/N})*N**4/100 - H1) == 0
assert sp.factor(H2n.subs({x:B/N,y:10*A/N})*N**6/2500 - H2) == 0

# Endpoint positivity bound for J_H: normalized first term >499, subtraction <104.
first_lower = 5*sp.Rational(2499,250)**2 - 36*10*sp.Rational(1,10**11)
second_upper = (sp.Rational(40,19))**2 * (2025*sp.Rational(2,19)**2 + 1)
assert first_lower > 499
assert second_upper < 104
assert first_lower-second_upper > 395

# Primitive mod-4 orientations. Here N0 is not an arbitrary odd residue:
# N0=(9B/2)^2+A^2 == 1 mod4. Thus Jhat is 0-1 == 3 mod4.
for m in range(1,5):
    for b0 in (1,3):
        for q0 in (1,3):
            n0 = 1
            assert ((2**(2*m))*b0*b0 - q0*q0*n0) % 4 == 3

# O+/- primitive: a 1 mod4 term +/- twice an odd unit are both 3 mod4.
for uhat in (1,5):
    for odd in (1,3,5,7):
        assert (uhat + 2*odd) % 4 == 3
        assert (uhat - 2*odd) % 4 == 3

print("OK: A2 spontaneous/additive height parity ledger certified")
