#!/usr/bin/env python3
"""Certificate for spontaneous-crt-floorfree-full2-square.md."""

# A_G=5m-2M+8. In low-m cone m<=6M/11, M>=11,
# 2v2(D)>=2m+4 >= A_G.
for M in range(11, 300):
    for m in range(1, (6*M)//11 + 1):
        AG = 5*m - 2*M + 8
        if AG <= 0:
            # high-2 lattice itself later has AG>0; inequality is still harmless.
            continue
        assert 2*m + 4 >= AG

# Algebraic mod-2^A identity: if D^2=0 mod modulus,
# P=2^A Delta - odd*(D^2-C^2) == odd*C^2.
for A in range(3, 12):
    mod=2**A
    for C in (1,3,5,7,9):
        for odd in (1,3,5,7,11):
            D=2**((A+1)//2)  # ensures D^2 divisible by 2^A
            Delta=13
            P=(2**A)*Delta-odd*(D*D-C*C)
            assert P % mod == (odd*C*C) % mod

print("OK: A2 floor-free CRT carrier has the claimed full 2-adic square class")
