#!/usr/bin/env python3
"""Exact certificate for spontaneous-denominator-common.md."""

import sympy as sp

x, y, t, N = sp.symbols("x y t N")

Delta0 = 2025*x**2 - 18*y - y**2
s = 9 + y
Nbar = 2025*x**2 + y**2

# q-side collapse.
assert sp.expand(Delta0.subs(x, -2) + (y + 9)**2 - 8181) == 0
Rq = 8181*N**2 - 26
assert sp.gcd(8181, 26) == 1
# A common root of Rq and Rq' at an odd prime with N a unit would force
# p | gcd(8181,26), hence cannot occur.
assert sp.diff(Rq, N) == 2*8181*N
assert sp.factor(8181 - 3**4 * 101) == 0

# f-side saturation system.
# Saturation gives zbar = -9 t / 2 and f-line gives wbar=-(x+2)/2.
# With Delta0=0, the sphere reduces to Lsat=0.
Lsat = sp.expand(200*x**2*(s - 9*t) - y*(x+2)**2)
P_f = sp.expand(100*x**2*(s**2 - 26*t**2) - (x+2)**2*Nbar)

Rt = sp.factor(sp.resultant(P_f, Lsat, t))
Fsat = sp.expand(
    1150871947369*x**8
    - 233661590896*x**7
    - 130208799184*x**6
    + 3933739968*x**5
    - 5129302560*x**4
    + 594074368*x**3
    + 85765888*x**2
    + 2675712*x
    + 389376
)
Rxy = sp.factor(sp.resultant(Delta0, Rt, y))
expected_Rxy = 164025000000*x**8*Fsat
assert sp.Poly(sp.expand(Rxy - expected_Rxy), x).is_zero

# Real endpoint defect u=10x-1 has no roots on (0,1/19).
u = sp.symbols("u")
FH = sp.Poly(sp.expand(10**8 * Fsat.subs(x, (1+u)/10)), u, domain=sp.QQ)
assert sp.count_roots(FH, sp.Rational(0), sp.Rational(1,19)) == 0
assert FH.eval(0) > 0
assert FH.eval(sp.Rational(1,19)) > 0

# Exact octic discriminant and inert singular audit.
disc = sp.factor(sp.discriminant(Fsat, x))
expected_disc = (
    2**114 * 3**20 * 5**22 * 11**6 * 13**3 * 41**4 * 101**8
    * 181**2 * 5927**2 * 197377693**2 * 326937937 * 1484772181
)
assert disc == expected_disc

for p in [11, 13, 41, 101, 181, 5927, 197377693, 326937937, 1484772181]:
    assert sp.isprime(p)

# Among non-3 odd factors of the discriminant, only 11 and 5927 are 3 mod 4.
assert 11 % 4 == 3 and 5927 % 4 == 3
for p in [13, 41, 101, 181, 197377693, 326937937, 1484772181]:
    assert p % 4 == 1

F11 = sp.Poly(Fsat, x, modulus=11)
dF11 = sp.Poly(sp.diff(Fsat, x), x, modulus=11)
g11 = sp.gcd(F11, dF11)
assert sp.Poly(g11.as_expr() - (x+2)**3, x, modulus=11).is_zero
# x=-2 cannot satisfy the f-line F_f=r(x+2)+2x=0 at p=11.
assert (-4) % 11 != 0

# 5927 appears only through leading-degree degeneration: no finite repeated root.
assert sp.LC(sp.Poly(Fsat, x)) % 5927 == 0
F5927 = sp.Poly(Fsat, x, modulus=5927)
dF5927 = sp.Poly(sp.diff(Fsat, x), x, modulus=5927)
assert sp.gcd(F5927, dF5927).degree() == 0

print("OK: A2 spontaneous/additive denominator common bridge certified")
