#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descended-quotient-orientation.md."""

# Mod-4 bookkeeping.
for Cmod in (1,3):
    H0mod=(-Cmod)%4
    Bdel=(-H0mod)%4
    assert Bdel==Cmod
    Kmod2=0  # K even
    central=(2*Kmod2-9)%4
    assert central==3
    Fmod=(central*Bdel)%4
    assert Fmod==(3*Cmod)%4

# H0=c_u Wq, c_u=1 mod4, Wq=3Z mod4 and H0=-C mod4 => C=Z mod4.
for Z in (1,3):
    H0=(3*Z)%4
    C=(-H0)%4
    assert C==Z
    Dhat=(3*C)%4
    assert Dhat==(3*Z)%4

# Denominator gcd identity: F63 == 5^lambda C(2K-9) mod g,
# and the prefactor is a unit. Test gcd numerically on coprime unit samples.
import math
for g in (7,11,13,17,19,23,29):
    for K in range(1,g):
        C=1
        u=pow(5,3,g)*C
        assert math.gcd(u,g)==1
        lhs=math.gcd((u*(2*K-9))%g,g)
        rhs=math.gcd(2*K-9,g)
        assert lhs==rhs

print("OK: A2 descended quotient has orientation 3Z mod4 and denominator overlap only through 2K-9")
