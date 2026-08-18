#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-singular-resolution.md."""

p = 1746991
x0 = 1362653
Dplus = 16651
Dminus = p - Dplus

# Angle normalized equation coefficients.
A0 = (99*x0 - 4) % p
aD = 8*(x0+2)*pow(A0, -1, p) % p
bphi = (-50625*pow(x0,5,p)) % p
assert aD == p - 8
assert bphi == 883946

# phi = kphi D^2.
kphi = (-aD * pow(bphi, -1, p)) % p
assert kphi == 1007439

# Corrected sphere after eliminating phi.
coef = (32070 - 680549*kphi) % p
assert coef == 286982
const = 572710
rhs = (-const * pow(coef, -1, p)) % p
assert rhs == 1231223

assert Dplus*Dplus % p == rhs
assert Dminus*Dminus % p == rhs
assert Dminus == p - Dplus

phi = kphi*rhs % p
assert phi == 987987

# Effective derivative is nonzero at both exceptional roots.
deff_plus = 2*coef*Dplus % p
deff_minus = 2*coef*Dminus % p
assert deff_plus == 1033794
assert deff_minus == 713197
assert deff_plus and deff_minus

# Full 2x2 Jacobian in (D, phi).
# F_ang = aD D^2 + bphi phi
# F_sph = 572710 + 32070 D^2 - 680549 phi

def det_at(D):
    return ((2*aD*D)*(-680549) - bphi*(2*32070*D)) % p

assert det_at(Dplus) == 1475138
assert det_at(Dminus) == 271853
assert det_at(Dplus) and det_at(Dminus)

print("OK: A2 source singular blow-up resolves into two simple branches")
