#!/usr/bin/env python3
"""Exact certificate for spontaneous-tangent-f-denominator.md."""

import sympy as sp

x, y, z, t = sp.symbols("x y z t")
s = 9 + y
Delta = 2025*x**2 - 18*y - y**2
Nbar = 2025*x**2 + y**2

d = 225*x**2-y
Asp = sp.expand(4*d**2 - x*y**2*(99*x-4))
assert sp.factor(-Asp + y**2*(x+2)**2 + 100*x**2*Delta) == 0

# f denominator line fixes wbar and, on Delta=0, the unique sphere root.
w = -(x+2)/2
sphere = sp.expand(
    x**2*w**2*(s+z)**2
    - (x+2+w)**2*(Nbar*w**2/100 + x**2*z**2)
)
zf = y*(x+2)**2/(400*x**2) - s/2
num = sp.together(sphere.subs(z, zf)).as_numer_denom()[0]
assert sp.rem(sp.Poly(num, y), sp.Poly(Delta, y)).is_zero

# Repeated tangent length and reduced G_f.
tf = sp.Rational(9,55)*(s-zf)
c = (x+2)**2*Nbar/(100*x**2)
R = sp.cancel(495*tf**2 - 220*s*tf + 27*s**2 + 9*c)
rnum = sp.together(R).as_numer_denom()[0]
rem = sp.rem(sp.Poly(rnum, y), sp.Poly(Delta, y)).as_expr()
G = sp.expand(
    225*x**2*(975627*x**4 + 222616*x**3 + 259848*x**2 + 864*x + 432)
    - 2*(x+2)**2*(27827*x**2 + 108*x + 108)*y
)
assert sp.factor(rem - 243*G) == 0

F8 = sp.expand(
    951848043129*x**8 + 434380360464*x**7 + 560807241744*x**6
    + 134769639744*x**5 + 88351387616*x**4 + 5400711936*x**3
    + 2954700032*x**2 + 28892160*x + 10416384
)
assert sp.factor(sp.resultant(Delta, G, y) + 50625*x**4*F8) == 0

# Endpoint defect u=10x-1 gives a polynomial with all positive coefficients.
u = sp.symbols("u")
FH = sp.expand(sp.together(10**8 * F8.subs(x, (1+u)/10)))
FH_expected = sp.expand(
    951848043129*u**8 + 11958587949672*u**7 + 113139094614492*u**6
    + 615777350903064*u**5 + 2617235426677430*u**4
    + 6748774195745624*u**3 + 12182775750721052*u**2
    + 12400944702783912*u + 5904991117326169
)
assert sp.expand(FH-FH_expected) == 0
assert all(int(c) > 0 for c in sp.Poly(FH, u).all_coeffs())

# Discriminant factorization.
disc_expected = (
    2**136 * 3**10 * 5**20 * 11**4 * 17**4 * 23**6 * 43**2 * 101**8
    * 163 * 673**2 * 2521**2 * 49663**2 * 188359**2
    * 33719039 * 118599997
)
assert abs(int(sp.discriminant(F8, x))) == disc_expected

# Full-system singular candidates and first p^2 compatibility.
Fx = [sp.diff(Delta,x), sp.diff(Delta,y)]
Gx = [sp.diff(G,x), sp.diff(G,y)]
full = [(11,10,9,10), (163,56,155,148), (33719039,27256238,16620484,30845985)]

def obstruction(p, x0, y0):
    f1 = int(Delta.subs({x:x0,y:y0}))
    f2 = int(G.subs({x:x0,y:y0}))
    assert f1 % p == 0 and f2 % p == 0
    A = [
        [int(Fx[0].subs({x:x0,y:y0})) % p, int(Fx[1].subs({x:x0,y:y0})) % p, -(f1//p) % p],
        [int(Gx[0].subs({x:x0,y:y0})) % p, int(Gx[1].subs({x:x0,y:y0})) % p, -(f2//p) % p],
    ]
    # 2x3 modular row reduction; singular candidates have rank 1.
    if A[0][0] == 0 and A[0][1] == 0:
        A[0], A[1] = A[1], A[0]
    pivot_col = 0 if A[0][0] else 1
    inv = pow(A[0][pivot_col], -1, p)
    A[0] = [(v*inv) % p for v in A[0]]
    factor = A[1][pivot_col] % p
    A[1] = [(A[1][j] - factor*A[0][j]) % p for j in range(3)]
    # The coefficient row vanishes; augmented entry is the obstruction.
    assert A[1][0] == 0 and A[1][1] == 0
    return A[1][2]

for p, x0, y0, expected in full:
    assert obstruction(p,x0,y0) == expected
    assert expected != 0

print("OK: A2 repeated f-denominator singular audit certified")
