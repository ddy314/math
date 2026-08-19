#!/usr/bin/env python3
"""Certificate for spontaneous-crt-hensel-sign-bridge.md."""

# The two proven sign laws are:
#   sgn(O_Delta) = -epsilon
#   sgn(chi_E)   = epsilon * sgn(z_E)
# with z_E != 0 and chi_E != 0.
# Exhaust the two epsilon choices and both z_E signs.
for eps in (-1, 1):
    for zsgn in (-1, 1):
        Osgn = -eps
        chisgn = eps * zsgn
        assert Osgn * zsgn * chisgn == -1

# Eliminating epsilon gives the equivalent mixed identity
# g chi_E = c_u C - sgn(O_Delta) a_2 c_- z_E.
# The strict dominance c_u C < a_2 c_- |z_E| forces
# sgn(chi_E) = -sgn(O_Delta) sgn(z_E).
for Osgn in (-1, 1):
    for zsgn in (-1, 1):
        chisgn = -Osgn * zsgn
        assert Osgn * zsgn * chisgn == -1

print("OK: A2 CRT orientation and centered Hensel kernel have fixed negative triple sign")
