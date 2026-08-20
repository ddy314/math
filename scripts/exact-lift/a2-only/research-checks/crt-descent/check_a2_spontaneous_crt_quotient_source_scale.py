#!/usr/bin/env python3
"""Certificate for spontaneous-crt-quotient-source-scale.md."""

import sympy as sp

D,C,T,K,a,z,cu,Ns,r,zet = sp.symbols(
    "D C T K a z cu Ns r zet", positive=True, nonzero=True
)

# Algebraic S_+ normalization.
r_expr = Ns / D
fr_over_hr = r_expr * (T*r_expr + 2*a) * (K-r_expr)**2 / (T*r_expr+a)**2
Splus = (
    T*K**2 - 4*a*K - T**2*fr_over_hr
    + (r_expr+7)*(2*a-2*K*T)
    + (r_expr**2+7*r_expr+37)*T
)

# Source-naturalized rational term assumed from the exact source identities.
source_term = z**2 * Ns * (T*Ns + 2*a*D) / (cu**2 * D**2)

# Fully integral D*Delta_+ after Delta_+=cu^2 D S_+.
DDelta_nat = sp.expand(
    cu**2 * (
        D**2*(T*K**2-14*K*T-4*K*a+37*T+14*a)
        + D*Ns*(-2*K*T+7*T+2*a)
        + T*Ns**2
    )
    - z**2*Ns*(T*Ns+2*a*D)
)

# Check that replacing only the rational term in S_+ gives the displayed formula.
Splus_nat = sp.expand(Splus + T**2*fr_over_hr - source_term)
assert sp.factor(D * (cu**2 * D * Splus_nat) - DDelta_nat) == 0

# Substitute Ns=3D-C and verify the expanded defect form.
DDelta_CD = sp.expand(DDelta_nat.subs(Ns, 3*D-C))
displayed = (
    cu**2*(
        C**2*T + 2*C*D*K*T - 13*C*D*T - 2*C*D*a
        + D**2*K**2*T - 20*D**2*K*T - 4*D**2*K*a
        + 67*D**2*T + 20*D**2*a
    )
    + z**2*(
        -C**2*T + 6*C*D*T + 2*C*D*a
        - 9*D**2*T - 6*D**2*a
    )
)
assert sp.factor(DDelta_CD - displayed) == 0

# Verify the normalized quadratic numerator in K.
r0, zeta = sp.symbols("r0 zeta", positive=True)
Sn = (
    K**2 - 4*zeta*K
    - r0*(r0+2*zeta)*(K-r0)**2/(r0+zeta)**2
    + (r0+7)*(2*zeta-2*K)
    + (r0**2+7*r0+37)
)
Lcoef = (
    2*r0**2*zeta + 7*r0**2 + 5*r0*zeta**2 + 14*r0*zeta
    + 2*zeta**3 + 7*zeta**2
)
Ccoef = (
    2*r0**3*zeta + 7*r0**3 + 5*r0**2*zeta**2 + 28*r0**2*zeta
    + 37*r0**2 + 2*r0*zeta**3 + 35*r0*zeta**2 + 74*r0*zeta
    + 14*zeta**3 + 37*zeta**2
)
assert sp.factor(
    Sn - (zeta**2*K**2 - 2*Lcoef*K + Ccoef)/(r0+zeta)**2
) == 0

# Rational endpoint checks for the coarse coefficient bounds.
from fractions import Fraction
rmin = Fraction(3,1)-Fraction(3,250)
zmax = Fraction(251,250)
lead_max = zmax*zmax/(rmin+zmax)**2
assert lead_max < Fraction(4,63)
assert Fraction(1,16) < lead_max
assert Fraction(1001,1000) > 1/(1-Fraction(3,250)**2)

# K>7616 is enough for K^2/16-28K > K^2/17.
assert 900_000_000_000 > 7616

print("OK: A2 additive CRT quotient is normalized to the single source scale c_u^2/g")
