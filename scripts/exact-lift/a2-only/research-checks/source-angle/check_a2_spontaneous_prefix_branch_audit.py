#!/usr/bin/env python3
"""Exact checks for spontaneous-prefix-branch-audit.md."""

import sympy as sp

x, y, t, z = sp.symbols("x y t z")

q1 = sp.sympify('11000*t**2*x**4*y**3 + 44000*t**2*x**3*y**3 + 44000*t**2*x**2*y**3 - 369056250000*t*x**8 + 3280500000*t*x**6*y + 84609*t*x**4*y**4 + 1571400*t*x**4*y**3 - 21528*t*x**3*y**4 - 194400*t*x**3*y**3 - 21384*t*x**2*y**4 - 194400*t*x**2*y**3 + 288*t*x*y**4 + 144*t*y**4 + 82012500000*x**8*y + 738112500000*x**8 - 4050*x**6*y**3 - 729000000*x**6*y**2 - 6561000000*x**6*y - 32400*x**5*y**3 - 19404*x**4*y**5 - 529218*x**4*y**4 - 3288600*x**4*y**3 + 2368*x**3*y**5 + 43056*x**3*y**4 + 64800*x**3*y**3 + 2304*x**2*y**5 + 42768*x**2*y**4 + 129600*x**2*y**3 - 128*x*y**5 - 576*x*y**4 - 64*y**5 - 288*y**4', locals={"x":x,"y":y,"t":t})
q2 = sp.sympify('-22275000*t**2*x**6*y**3 - 89100000*t**2*x**5*y**3 + 11000*t**2*x**4*y**5 + 198000*t**2*x**4*y**4 - 89100000*t**2*x**4*y**3 + 44000*t**2*x**3*y**5 + 792000*t**2*x**3*y**4 + 44000*t**2*x**2*y**5 + 792000*t**2*x**2*y**4 - 747338906250000*t*x**10 + 1107168750000*t*x**8*y**2 + 19929037500000*t*x**8*y - 535796775*t*x**6*y**4 - 19584585000*t*x**6*y**3 - 177147000000*t*x**6*y**2 + 43885800*t*x**5*y**4 + 393660000*t*x**5*y**3 + 84609*t*x**4*y**6 + 4714200*t*x**4*y**5 + 130782600*t*x**4*y**4 + 918540000*t*x**4*y**3 - 21528*t*x**3*y**6 - 583200*t*x**3*y**5 - 2916000*t*x**3*y**4 - 21384*t*x**2*y**6 - 583200*t*x**2*y**5 - 3207600*t*x**2*y**4 + 288*t*x*y**6 + 144*t*y**6 + 166075312500000*x**10*y + 1494677812500000*x**10 - 246029298750*x**8*y**3 - 6643012500000*x**8*y**2 - 39858075000000*x**8*y + 65610000*x**7*y**3 + 120280950*x**6*y**5 + 5445520650*x**6*y**4 + 78830415000*x**6*y**3 + 354294000000*x**6*y**2 - 4892400*x**5*y**5 - 88354800*x**5*y**4 - 131220000*x**5*y**3 - 19404*x**4*y**7 - 1238454*x**4*y**6 - 33874200*x**4*y**5 - 380829600*x**4*y**4 - 1312200000*x**4*y**3 + 2368*x**3*y**7 + 85968*x**3*y**6 + 842400*x**3*y**5 + 2304*x**2*y**7 + 85104*x**2*y**6 + 907200*x**2*y**5 + 1749600*x**2*y**4 - 128*x*y**7 - 1728*x*y**6 - 64*y**7 - 864*y**6', locals={"x":x,"y":y,"t":t})

d = 225*x**2-y
Asp = sp.expand(4*d**2-x*y**2*(99*x-4))
Aminus = sp.expand(Asp-2*y**2*(x+2)**2)
Delta0 = 2025*x**2-18*y-y**2
Cstar = sp.expand(164025*x**4+656100*x**3+2381*x**2*y**2+41400*x**2*y+842400*x**2+324*x*y**2+324*y**2)

subs = sp.subresultants(q1, q2, t)
S1 = sp.factor(next(s for s in subs if sp.Poly(s, t).degree() == 1))
expected = 198000*x**2*y**3*(x+2)**2*d*Aminus*Asp*(2*(y+9)-9*t)
assert sp.cancel(S1/expected) == 1

tc = 2*(y+9)/9
assert sp.factor(q1.subs(t,tc)+sp.Rational(2,81)*y**3*(x+2)**2*Cstar) == 0
assert sp.factor(q2.subs(t,tc)-sp.Rational(2,81)*y**3*(x+2)**2*Delta0*Cstar) == 0

Ccentral = sp.expand(81*(x+2)**2*(2025*x**2+y**2)+2300*x**2*(y+9)**2)
assert sp.expand(Ccentral-Cstar) == 0

ncent = sp.Rational(9,2)/(y+9)
Kcent = sp.Rational(9,2)
wbar = -Asp/(2*y**2*(x+2))
wcent = sp.factor(ncent*wbar)
Qcent = sp.factor(ncent*(x+2))
sphere = sp.factor(x**2*wcent**2*(Kcent+z)**2-(Qcent+wcent)**2*((2025*x**2+y**2)*wcent**2/100+x**2*z**2))
num, _ = sp.fraction(sp.together(sphere))
disc = sp.factor(sp.discriminant(num,z))
sq = (10497600*x**2*y**3*(x+2)**2*(y+9)*d*Aminus*Asp)**2
assert sp.expand(disc-sq) == 0

print("OK: A2 spontaneous prefix branch audit certified")
