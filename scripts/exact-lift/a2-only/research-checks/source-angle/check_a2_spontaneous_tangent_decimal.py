#!/usr/bin/env python3
"""Exact certificate for spontaneous-tangent-decimal.md."""

import sympy as sp

# Compact branch / orientation elimination.
t, s, z, c = sp.symbols("t s z c")
L = 55*t**2 + 18*(z-s)*t + s**2 - 4*s*z - c
z_tan = s - sp.Rational(55, 9)*t
R = 495*t**2 - 220*s*t + 27*s**2 + 9*c
assert sp.factor(9*L.subs(z, z_tan) + R) == 0

# C_* completion identity in normalized variables.
x = sp.symbols("x")
Cstar = 100*x**2*(23*s**2 + 81*c)
assert sp.factor(900*x**2*R - Cstar - 5500*x**2*(9*t-2*s)**2) == 0

# Raw decimalization.
B, N, Q, N0, K = sp.symbols("B N Q N0 K")
Rint = B**2*(27*K**2 - 220*K + 495) + 9*Q**2*N0
Rraw = R.subs({t:1/N, s:K/N, c:Q**2*N0/(B**2*N**2)})
assert sp.cancel(B**2*N**2*Rraw - Rint) == 0

Cint = 23*B**2*K**2 + 81*Q**2*N0
assert sp.expand(9*Rint - Cint - 55*B**2*(2*K-9)**2) == 0

# Prefix syzygies.
RN = 324*Q**2*N0 + 2695*B**2
Psi = B**2*(K**2-26) - Q**2*N0
assert sp.expand(36*Rint - RN - B**2*(18*K-55)*(54*K-275)) == 0
assert sp.expand(Rint + 9*Psi - B**2*(2*K-9)*(18*K-29)) == 0

# Tangent / alpha / Theta / S0 syzygies.
T, a3 = sp.symbols("T a3")
alpha = T*K + a3
Ltan = 9*(T*K-a3) - 55*T
assert sp.expand(9*alpha + Ltan - T*(18*K-55)) == 0

Rtheta = B**2*(K**2-18*K+55) - Q**2*N0
Theta = T*Rtheta - 2*B**2*(2*K-9)*a3
assert sp.expand(9*Theta + T*Rint - 2*B**2*(2*K-9)*Ltan) == 0

Ptan = 27*K**2 - 220*K + 495
S0 = T*(K**2-26) - (2*K-9)*(2*a3+9*T)
assert sp.expand(9*S0 + T*Ptan - 2*(2*K-9)*Ltan) == 0

# Defect substitution.
hH, he = sp.symbols("hH he")
x_def = (1+hH)/10
y_def = 1-he
s_def = 10-he
Nbar = 2025*x_def**2 + y_def**2
c_from_xy = sp.factor((x_def+2)**2*Nbar/(100*x_def**2))
c_expected = ((hH+21)**2*(4*he**2-8*he+81*hH**2+162*hH+85))/(400*(hH+1)**2)
assert sp.cancel(c_from_xy-c_expected) == 0

# Parity checks used in the proof: for K even, P_tan(K) is odd.
k = sp.symbols("k", integer=True)
Ptan_even = sp.expand(Ptan.subs(K, 2*k))
assert sp.expand(Ptan_even - (108*k**2 - 440*k + 495)) == 0
assert (108*7**2 - 440*7 + 495) % 2 == 1  # coefficient parity pattern is constant.

print("OK: A2 spontaneous tangent decimalization certified")
