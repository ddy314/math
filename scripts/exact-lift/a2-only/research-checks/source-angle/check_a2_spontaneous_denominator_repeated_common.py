#!/usr/bin/env python3
"""Exact certificate for spontaneous-denominator-repeated-common.md."""

import sympy as sp

K, x, y, t = sp.symbols("K x y t")

Pq = K**2 - 26
Pf = 3*K**2 - 36*K + 26
LrepK = 18*K - 29

# f-saturation sphere quadratic and its simple inert roots.
assert sp.discriminant(Pf, K) == 984
assert sp.factorint(984) == {2: 3, 3: 1, 41: 1}
assert 41 % 4 == 1
assert sp.expand((K**2 - 26) - 4*K*(K-9) + Pf) == 0

# repeated+saturation K-center.
Kstar = sp.Rational(29, 18)
assert sp.factor(Pq.subs(K, Kstar)) == -sp.Rational(7583, 324)
assert sp.isprime(7583) and 7583 % 4 == 3
assert sp.legendre_symbol(101, 7583) == -1

assert sp.factor(Pf.subs(K, Kstar)) == -sp.Rational(2615, 108)
assert 2615 == 5*523
assert sp.isprime(523) and 523 % 4 == 3

# Full f-side first-layer system.
Delta0 = 2025*x**2 - 18*y - y**2
s = 9 + y
Nbar = 2025*x**2 + y**2
Lsat = 200*x**2*(s - 9*t) - y*(x+2)**2
Ppref = 100*x**2*(s**2 - 26*t**2) - (x+2)**2*Nbar
Frep = 18*s - 29*t
Asp = 4*(225*x**2-y)**2 - x*y**2*(99*x-4)

p = 523
inv29 = pow(29, -1, p)
sols = []
for xv in range(1, p):
    if (xv + 2) % p == 0:
        continue
    for yv in range(1, p):
        if (2025*xv*xv - 18*yv - yv*yv) % p:
            continue
        sv = (9 + yv) % p
        if sv == 0:
            continue
        tv = (18*sv*inv29) % p
        if tv == 0:
            continue
        if (200*xv*xv*(sv - 9*tv) - yv*(xv+2)**2) % p:
            continue
        nbarv = (2025*xv*xv + yv*yv) % p
        if (100*xv*xv*(sv*sv - 26*tv*tv) - (xv+2)**2*nbarv) % p:
            continue
        aspv = int(Asp.subs({x:xv, y:yv})) % p
        if nbarv == 0 or aspv == 0:
            continue
        sols.append((xv, yv, tv))

assert sols == [(115, 215, 121)]

pt = {x:115, y:215, t:121}
assert int(Nbar.subs(pt)) % p == 88
assert int(Asp.subs(pt)) % p == 509
Kmod = ((9+215) * pow(121, -1, p)) % p
assert Kmod == (29 * pow(18, -1, p)) % p == 205
rmod = (-2*115*pow(117, -1, p)) % p
wmod = (115*pow(rmod, -1, p)) % p
zmod = (-9*121*pow(2, -1, p)) % p
assert (rmod, wmod, zmod) == (302, 203, 240)

# p^2 lift obstruction for F1=Delta0,F2=Lsat,F3=Ppref,F4=Frep.
eqs = [Delta0, Lsat, Ppref, Frep]
vals = [int(F.subs(pt)) for F in eqs]
assert all(v % p == 0 for v in vals)
rhs = [(-(v // p)) % p for v in vals]
vars_ = (x, y, t)
J = [[int(sp.diff(F, v).subs(pt)) % p for v in vars_] for F in eqs]

# Modular RREF of the 4x4 augmented matrix.
A = [row[:] + [r] for row, r in zip(J, rhs)]
row = 0
for col in range(3):
    pivot = next((i for i in range(row, 4) if A[i][col] % p), None)
    if pivot is None:
        continue
    A[row], A[pivot] = A[pivot], A[row]
    inv = pow(A[row][col] % p, -1, p)
    A[row] = [(v*inv) % p for v in A[row]]
    for i in range(4):
        if i == row:
            continue
        factor = A[i][col] % p
        if factor:
            A[i] = [(A[i][j] - factor*A[row][j]) % p for j in range(4)]
    row += 1

assert A[-1] == [0, 0, 0, 27]

print("OK: A2 repeated spontaneous / saturated denominator shell certified")
