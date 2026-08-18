#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-numerator-length.md."""

import sympy as sp

x, y, t = sp.symbols("x y t")
S, A, e = sp.symbols("S A e", integer=True)

C = sp.expand(
    440*(x+2)**2*t**2
    + 81*(9401*x**4 - 2392*x**3 - 1600*x**2 - 64*x - 64)*t
    - 324*x*(99*x-4)*(25*x**2+1)*(49*x**2-4*x-2)
)

Epoly = sp.expand(
    11000*t**2*y + 9900000*t**2
    + 84609*t*y**2 - 3240000*t*y - 29160000*t
    - 19404*y**3 - 10836*y**2 + 1474200*y
)
Opoly = sp.expand(
    5500*t**2 - 2691*t*y - 16200*t
    + 296*y**2 + 1764*y - 8100
)

# On 225 x^2 = y, the even/odd decomposition is
# 5625 C = E + 1800 x O = E + 120 r O, r=15x.
rem = sp.rem(sp.expand(5625*C - Epoly - 1800*x*Opoly), 225*x**2-y, x)
assert sp.expand(rem) == 0

Ryt = sp.expand(Epoly**2 - 14400*y*Opoly**2)
res = sp.resultant(225*x**2-y, C, x)
assert sp.factor(res - 2025**2*Ryt) == 0

Esc = sp.expand(10*S**3*Epoly.subs({y:A/S, t:1/(10*S)}))
Osc = sp.expand(10*S**2*Opoly.subs({y:A/S, t:1/(10*S)}))

expected_E = sp.expand(
    -194040*A**3 - 108360*A**2*S + 84609*A**2
    + 14742000*A*S**2 - 3240000*A*S + 1100*A
    - 29160000*S**2 + 990000*S
)
expected_O = sp.expand(
    2960*A**2 + 17640*A*S - 2691*A
    - 81000*S**2 - 16200*S + 550
)
assert sp.expand(Esc-expected_E) == 0
assert sp.expand(Osc-expected_O) == 0

Rint = sp.expand(Esc**2 - 14400*A*S*Osc**2)
assert sp.cancel(
    Ryt.subs({y:A/S,t:1/(10*S)}) - Rint/(100*S**6)
) == 0

Ee = sp.expand(Esc.subs(A,S-e))
Oe = sp.expand(Osc.subs(A,S-e))
expected_Ee = sp.expand(
    14439600*S**3 - 13943160*S**2*e - 32315391*S**2
    - 690480*S*e**2 + 3070782*S*e + 991100*S
    + 194040*e**3 + 84609*e**2 - 1100*e
)
expected_Oe = sp.expand(
    -60400*S**2 - 23560*S*e - 18891*S
    + 2960*e**2 + 2691*e + 550
)
assert sp.expand(Ee-expected_Ee) == 0
assert sp.expand(Oe-expected_Oe) == 0

# Endpoint parity: S is divisible by 8 and e is odd.
# Enumerate residue classes to certify E=5 mod 8 and O odd.
for er in (1,3,5,7):
    assert int(Ee.subs({S:0,e:er})) % 8 == 5
    assert int(Oe.subs({S:0,e:er})) % 2 == 1

# Then Rint = E^2 mod 8 because 14400*S is divisible by 8.
for er in (1,3,5,7):
    ev = int(Ee.subs({S:0,e:er})) % 8
    assert ev*ev % 8 == 1

# Coarse real bounds used in the proof.
base_lower = sp.Rational(249,250)*(1474200-10836-19404)
linear_loss = sp.Rational(84609+3240000+29160000,10**11)
assert base_lower-linear_loss > 1_438_000
O_bound = sp.Rational(296+1764+8100,1) + sp.Rational(2691+16200,10**11) + sp.Rational(5500,10**22)
assert 120*O_bound < 1_220_000

print("OK: A2 source numerator/length eliminant and 1 mod 8 residual certified")
