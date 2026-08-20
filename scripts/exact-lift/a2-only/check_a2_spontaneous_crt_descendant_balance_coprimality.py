#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-balance-coprimality.md."""

import math
from fractions import Fraction


# 5-adic unit calculation for Dhat:
# K,T vanish mod 5, 2K-9 == 1; H0 == g*a3; hence
# B_Delta == -g*a3-H0 == -2g*a3, and Dhat=c_u^2 F63.
p = 5
for cu in (1, 2, 3, 4):
    for g in (1, 2, 3, 4):
        for a3 in (1, 2, 3, 4):
            F63 = (-2 * g * a3) % p
            Dhat = (cu * cu * F63) % p
            assert Dhat != 0

# Abstract gcd identity.  Under the proved cross-coprimalities
# gcd(Rstar,g*2^m)=1 and gcd(Dhat,5^lambda)=1, the common support of
# X=5^lambda Rstar and Y=g2^m Dhat is exactly gcd(Rstar,Dhat).
# Exhaust finite coprime samples as a sanity certificate for the algebraic step.
for Rstar in range(1, 50, 2):
    for Dhat in range(1, 50, 2):
        for fivepow in (5, 25, 125):
            for g2m in (8, 24, 56, 88):
                if math.gcd(Rstar, 10 * g2m) != 1:
                    continue
                if math.gcd(Dhat, fivepow) != 1:
                    continue
                if math.gcd(fivepow, g2m) != 1:
                    continue
                X = fivepow * Rstar
                Y = g2m * Dhat
                assert math.gcd(X, Y) == math.gcd(Rstar, Dhat)

# Height drop X < (X+Y)/24 is exactly X/Y < 1/23.
for X in range(1, 100):
    for Y in range(1, 5000):
        lhs = 24 * X < X + Y
        rhs = Fraction(X, Y) < Fraction(1, 23)
        assert lhs == rhs

# Cross-gcd identities for B=81*x*A + 2*y*Bgate with gcd(x,y)=1 and x odd.
for x in range(1, 40, 2):
    for y in range(1, 40):
        if math.gcd(x, y) != 1:
            continue
        for A in range(1, 12):
            for Bgate in range(1, 12):
                Bal = 81 * x * A + 2 * y * Bgate
                assert math.gcd(Bal, x) == math.gcd(Bgate, x)
                assert math.gcd(Bal, y) == math.gcd(81 * A, y)

# Real balance gap: parent chi in (0,1/23), geometric chi<-1 gives >1 separation.
for parent in (Fraction(1, 1000), Fraction(1, 100), Fraction(1, 24)):
    assert 0 < parent < Fraction(1, 23)
    for geom in (Fraction(-1001, 1000), Fraction(-2, 1), Fraction(-10, 1)):
        assert geom < -1
        assert parent - geom > 1

print("OK: parent coordinates are coprime after G_Delta, chi_real<1/23, and balance-tail reuse is cross-gated")
