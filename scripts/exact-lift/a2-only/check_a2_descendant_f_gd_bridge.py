#!/usr/bin/env python3
"""Exact certificate for the A2 descendant f/G_D bridge.

The remaining fixed-3 terminal exceptions are f-contact and extra central
3-depth.  This script proves that they enter the descended quotient through
one exact identity, and records the first 3-adic depths of its two fixed
coefficients in the two endpoint channels.
"""

import sympy as sp

K, T, a3, g, omega, cu, f = sp.symbols(
    "K T a3 g omega cu f", integer=True
)
U, zeta = sp.symbols("U zeta", integer=True)

GD = 11*K**2 - 240*K + 432
Jf = K**2*T - 576*K*T - 32*K*a3 + 1296*T + 144*a3
Bdelta = g*((2*K - 9)*T - a3) - cu*(T*K + a3)/omega
F63 = (2*K - 9)*Bdelta - sp.Rational(63, 16)*g*T*K**2

# f = g*omega + cu.
bridge = sp.expand(16*omega*F63 - (f*Jf - 3*cu*T*GD))
assert sp.factor(bridge.subs(f, g*omega + cu)) == 0

# Project to the central variable U=2K-9 and zeta=a3/T.
K_U = (U + 9)/2
Jproj = sp.factor(
    4*(K_U**2 - 576*K_U - 32*K_U*zeta + 1296 + 144*zeta)
)
GDproj = sp.factor(4*(11*K_U**2 - 240*K_U + 432))
assert Jproj == U**2 - 64*U*zeta - 1134*U - 5103
assert GDproj == 11*U**2 - 282*U - 1701

assert sp.factorint(5103) == {3: 6, 7: 1}
assert sp.factorint(1134) == {2: 1, 3: 4, 7: 1}
assert sp.factorint(1701) == {3: 5, 7: 1}
assert sp.factorint(282) == {2: 1, 3: 1, 47: 1}


def v3(n: int) -> int:
    n = abs(int(n))
    assert n
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return e


# Channel A: v3(K)=1, v3(zeta)>=2.  J_f has exact depth 2.
# G_D has depth 2 unless K/3 == 1 mod3, in which case it is deeper.
for k in (1, 2):
    # represent K=3k modulo a sufficiently high 3-power and zeta=0 mod9
    kval = 3*k
    j = int((Jf/T).subs({K: kval, a3: 0}))
    assert v3(j) == 2
    gd = int(GD.subs(K, kval))
    if k == 2:
        assert v3(gd) == 2
    else:
        assert v3(gd) >= 3

# Channel B uses U directly.  If h=v3(U)=2 or 3, both fixed coefficients
# acquire exactly one extra 3 beyond h; hence the fJ_f term is one layer
# shallower than the 3*G_D term whenever f is a 3-unit.
for h in (2, 3):
    uval = 3**h
    zval = 3  # v3(zeta)=1
    jnum = int(Jproj.subs({U: uval, zeta: zval}))
    gdnum = int(GDproj.subs(U, uval))
    assert v3(jnum) == h + 1
    assert v3(gdnum) == h + 1

# Central/fixed-height transversality identity used in the sibling theorem.
assert sp.expand(4*GD - (
    11*(2*K - 9)**2 - 282*(2*K - 9) - 1701
)) == 0

print(
    "OK: A2 fixed-3 f-contact and central-depth exceptions meet through "
    "16*omega*F63 = f*Jf - 3*cu*T*G_D"
)
