#!/usr/bin/env python3
"""Exact certificate for spontaneous-prefix-eliminant.md.

Requires SymPy from the repository uv environment.  It checks the two
pure-decimal linearizations, reconstructs the exact sphere elimination from
literal quadratic factors, verifies the branch resultant, and checks the
nested collision discriminants.
"""

import sympy as sp

x, y, t = sp.symbols("x y t")
N, A, B, T, b3, a3 = sp.symbols("N A B T b3 a3")
r = sp.symbols("r")

d = 225*x**2-y
Asp = sp.expand(4*d**2-x*y**2*(99*x-4))
Omega = sp.expand(Asp*r+2*x*y**2*(x+2))
U = sp.expand((45*B**2-2*A*N)**2-A**2*B*(99*B-4*N))
lhs = sp.together(Omega.subs({x:B/N, y:10*A/N, r:B*T/b3}))
rhs = 100*B*(T*U+2*A**2*(2*N+B)*b3)/(b3*N**4)
assert sp.cancel(lhs-rhs) == 0

Q = 2*N+B
K = 9*N+10*A
N0 = sp.Rational(81, 4)*B**2+A**2
S0 = T*(K**2-26)-(2*K-9)*(2*a3+9*T)
Theta = sp.expand(B**2*S0-T*Q**2*N0)
Rtheta = sp.expand(B**2*(K**2-18*K+55)-Q**2*N0)
assert sp.expand(Theta-(T*Rtheta-2*B**2*(2*K-9)*a3)) == 0

# Literal primitive quadratic factors in tau=t=10^{-M}.  Keeping these
# expanded makes the checker independent of SymPy's factor-order choices.
q1 = sp.sympify('11000*t**2*x**4*y**3 + 44000*t**2*x**3*y**3 + 44000*t**2*x**2*y**3 - 369056250000*t*x**8 + 3280500000*t*x**6*y + 84609*t*x**4*y**4 + 1571400*t*x**4*y**3 - 21528*t*x**3*y**4 - 194400*t*x**3*y**3 - 21384*t*x**2*y**4 - 194400*t*x**2*y**3 + 288*t*x*y**4 + 144*t*y**4 + 82012500000*x**8*y + 738112500000*x**8 - 4050*x**6*y**3 - 729000000*x**6*y**2 - 6561000000*x**6*y - 32400*x**5*y**3 - 19404*x**4*y**5 - 529218*x**4*y**4 - 3288600*x**4*y**3 + 2368*x**3*y**5 + 43056*x**3*y**4 + 64800*x**3*y**3 + 2304*x**2*y**5 + 42768*x**2*y**4 + 129600*x**2*y**3 - 128*x*y**5 - 576*x*y**4 - 64*y**5 - 288*y**4', locals={"x":x,"y":y,"t":t})
q2 = sp.sympify('-22275000*t**2*x**6*y**3 - 89100000*t**2*x**5*y**3 + 11000*t**2*x**4*y**5 + 198000*t**2*x**4*y**4 - 89100000*t**2*x**4*y**3 + 44000*t**2*x**3*y**5 + 792000*t**2*x**3*y**4 + 44000*t**2*x**2*y**5 + 792000*t**2*x**2*y**4 - 747338906250000*t*x**10 + 1107168750000*t*x**8*y**2 + 19929037500000*t*x**8*y - 535796775*t*x**6*y**4 - 19584585000*t*x**6*y**3 - 177147000000*t*x**6*y**2 + 43885800*t*x**5*y**4 + 393660000*t*x**5*y**3 + 84609*t*x**4*y**6 + 4714200*t*x**4*y**5 + 130782600*t*x**4*y**4 + 918540000*t*x**4*y**3 - 21528*t*x**3*y**6 - 583200*t*x**3*y**5 - 2916000*t*x**3*y**4 - 21384*t*x**2*y**6 - 583200*t*x**2*y**5 - 3207600*t*x**2*y**4 + 288*t*x*y**6 + 144*t*y**6 + 166075312500000*x**10*y + 1494677812500000*x**10 - 246029298750*x**8*y**3 - 6643012500000*x**8*y**2 - 39858075000000*x**8*y + 65610000*x**7*y**3 + 120280950*x**6*y**5 + 5445520650*x**6*y**4 + 78830415000*x**6*y**3 + 354294000000*x**6*y**2 - 4892400*x**5*y**5 - 88354800*x**5*y**4 - 131220000*x**5*y**3 - 19404*x**4*y**7 - 1238454*x**4*y**6 - 33874200*x**4*y**5 - 380829600*x**4*y**4 - 1312200000*x**4*y**3 + 2368*x**3*y**7 + 85968*x**3*y**6 + 842400*x**3*y**5 + 2304*x**2*y**7 + 85104*x**2*y**6 + 907200*x**2*y**5 + 1749600*x**2*y**4 - 128*x*y**7 - 1728*x*y**6 - 64*y**7 - 864*y**6', locals={"x":x,"y":y,"t":t})

Nbar = 2025*x**2+y**2
wbar = -Asp/(2*y**2*(x+2))
znum = x**2*((9+y)**2-18*(9+y)*t+55*t**2)-(x+2)**2*Nbar/100
zden = 2*x**2*(2*(9+y)-9*t)
zbar = znum/zden
sphere = x**2*wbar**2*(9+y+zbar)**2-(2+x+wbar)**2*(Nbar*wbar**2/100+x**2*zbar**2)
num, _ = sp.fraction(sp.cancel(sphere))
assert sp.Poly(sp.expand(num+q1*q2), t, x, y).is_zero

Delta0 = 2025*x**2-18*y-y**2
C0 = 11000*x**2*y**3*(x+2)**2
assert sp.factor(sp.Poly(q1,t).coeff_monomial(t**2)-C0) == 0
assert sp.factor(sp.Poly(q2,t).coeff_monomial(t**2)+C0*Delta0) == 0

Aminus = sp.expand(Asp-2*y**2*(x+2)**2)
Cstar = sp.expand(164025*x**4+656100*x**3+2381*x**2*y**2+41400*x**2*y+842400*x**2+324*x*y**2+324*y**2)
expected = -7128000*x**2*y**6*(x+2)**4*d**2*Aminus**2*Asp**2*Cstar
res = sp.resultant(q1,q2,t)
assert sp.Poly(sp.expand(res-expected), x, y).is_zero

Ew = sp.expand(220*y**4*(x+2)**4-49*Asp**2)
re = sp.resultant(Aminus,Ew,y)
expected_e = 2**14*3**18*5**16*x**16*(x+2)**8
assert sp.Poly(sp.expand(re-expected_e), x).is_zero

assert sp.factor(sp.discriminant(Aminus,y)-900**2*x**4*(101*x**2+4*x+8)) == 0
assert sp.factor(sp.discriminant(101*x**2+4*x+8,x)+16*3*67) == 0
assert sp.factor(sp.discriminant(Cstar,y)+810**2*x**2*(x+2)**2*(2381*x**2+324*x+416)) == 0
assert sp.factor(sp.discriminant(2381*x**2+324*x+416,x)+16*23*47*223) == 0

print('OK: A2 spontaneous prefix eliminant certified')
