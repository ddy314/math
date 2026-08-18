#!/usr/bin/env python3
"""Corrected exact transverse certificate for spontaneous-source-common-integer.md.

Important: this checker keeps the genuine integer representative at the
p=1746991 singular residue.  A previous F_p[eps]/(eps^3) expansion treated
C_src(x0,t0) as literally zero and therefore lost the nonzero carry
C_src(x0,t0)/p mod p.
"""

import sympy as sp

x, t, d, ph = sp.symbols("x t d ph")

# First-layer common gate.
C = sp.expand(
    440*(x+2)**2*t**2
    + 81*(9401*x**4 - 2392*x**3 - 1600*x**2 - 64*x - 64)*t
    - 324*x*(99*x-4)*(25*x**2+1)*(49*x**2-4*x-2)
)

# Full Theta-recovered sphere in source transverse coordinates.
A = 99*x - 4
y = 225*x**2 - d
r = (2*(x+2) + ph)/A
w = sp.cancel(x/r)
s = 9 + y
Nbar = 2025*x**2 + y**2
z = sp.cancel(
    (
        x**2*(s**2 - 18*s*t + 55*t**2)
        - sp.Rational(1,100)*(x+2)**2*Nbar
    )
    / (2*x**2*(2*s - 9*t))
)
Sphere = sp.cancel(
    x**2*w**2*(s+z)**2
    - (x+2+w)**2*(Nbar*w**2/100 + x**2*z**2)
)

# On the exact source slice the sphere is a unit times C_src^2.
S0 = sp.factor(Sphere.subs({d:0, ph:0}))
expected_S0 = sp.cancel(
    -x**2*(25*x**2+1)*C**2
    / (5184*(x+2)**4*(50*x**2+2-t)**2)
)
assert sp.cancel(S0 - expected_S0) == 0

# Exact transverse tangency.  Since d=225x^2-y, d/dy = -d/dd.
Sd = sp.factor(sp.diff(Sphere, d).subs({d:0, ph:0}))
Pd = (
    783481*t**2*x**6 - 105752*t**2*x**5 - 40720*t**2*x**4
    - 1664*t**2*x**3 - 1664*t**2*x**2
    - 78586200*t*x**8 + 9590400*t*x**7 - 195048*t*x**6
    + 254016*t*x**5 + 117936*t*x**4 - 5184*t*x**3
    + 1964655000*x**10 - 239760000*x**9 + 83462400*x**8
    - 15940800*x**7 - 2753352*x**6 - 124416*x**5
    - 117936*x**4 + 5184*x**3
)
expected_Sd = sp.cancel(
    -C*Pd/(23328*(x+2)**4*(50*x**2+2-t)**3)
)
assert sp.cancel(Sd - expected_Sd) == 0

# Singular projected residue.
p = 1746991
x0 = 1362653
t0 = 807263

Cx = sp.diff(C, x)
Ct = sp.diff(C, t)
Cval = int(C.subs({x:x0, t:t0}))
assert Cval % p == 0
assert (Cval // p) % p == 1642591
assert int(Cx.subs({x:x0, t:t0})) % p == 0
assert int(Ct.subs({x:x0, t:t0})) % p == 0


def vp_int(n, prime):
    n = int(n)
    if n == 0:
        return 10**9
    n = abs(n)
    v = 0
    while n % prime == 0:
        n //= prime
        v += 1
    return v


def rational_data(expr):
    q = sp.Rational(sp.cancel(expr.subs({x:x0, t:t0})))
    num, den = int(q.p), int(q.q)
    v = vp_int(num, p) - vp_int(den, p)
    if v >= 0:
        num //= p**v
    else:
        den //= p**(-v)
    residue = (num % p) * pow(den % p, -1, p) % p
    return v, residue

# The genuine p-adic carry and transverse Taylor coefficients.
Sdd2 = sp.diff(Sphere, d, 2).subs({d:0, ph:0})/2
Sph = sp.diff(Sphere, ph).subs({d:0, ph:0})
Sx = sp.diff(S0, x)
St = sp.diff(S0, t)

assert rational_data(S0) == (2, 572710)
assert rational_data(Sd) == (2, 707577)
assert rational_data(Sdd2) == (0, 32070)
assert rational_data(Sph) == (0, 1066442)  # = -680549 mod p

# Projected x,t lifts cannot alter the p^2 leading coefficient.
assert rational_data(Sx)[0] >= 2
assert rational_data(St)[0] >= 2

# Source angle-extra correction phi = kphi*D^2.
A0 = (99*x0 - 4) % p
kphi = (
    8*(x0+2)
    * pow((50625*A0*pow(x0,5,p)) % p, -1, p)
) % p
assert kphi == 1007439

# Correct h=1 equation keeps the carry 572710.
coef_D2 = (32070 + 1066442*kphi) % p
assert coef_D2 == 286982
rhs = (-572710 * pow(coef_D2, -1, p)) % p
assert rhs == 1231223
roots = sorted(sp.sqrt_mod(rhs, p, all_roots=True))
assert roots == [16651, 1730340]
assert roots[1] == p - roots[0]

phi_residue = kphi * roots[0]**2 % p
assert phi_residue == 987987
assert kphi * roots[1]**2 % p == phi_residue

# Hence h=1 has two normalized transverse templates; it is NOT dead.
# For h>=2, the p^2 projected leading term cannot be reached by source
# transverse terms: linear d has depth >= h+2, d^2 and Phi have depth >=2h.
assert 572710 % p != 0

print("OK: corrected A2 source common carry/transverse audit certified")
