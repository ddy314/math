#!/usr/bin/env python3
"""Certificate for spontaneous-source-parity-decimal-gcd.md."""

from fractions import Fraction

# Windows used in the proof.
N=10**11
qlo=Fraction(21,10); qhi=Fraction(40,19)
w=Fraction(843,1000)
slo=Fraction(2499,250); shi=Fraction(10)
Dlo=55*qlo*qlo-49*(w/N)**2
Dhi=55*qhi*qhi
assert Dlo>242 and Dhi<244
Blo=qlo*qlo*slo*slo
Bhi=qhi*qhi*shi*shi+(w*w/N**2)*(500+Fraction(55,N*N))
assert Blo>440 and Bhi<444

# Common square scale cancels exactly in gcd and residual quotients.
import math
for L in range(1,20):
    for BW in range(1,30,2):
        for DW2 in range(1,30,2):
            Bdec=L*L*BW
            Ddec2=L*L*DW2
            G=math.gcd(Bdec,Ddec2)
            GS=math.gcd(BW,DW2)
            assert G==L*L*GS
            assert Bdec//G==BW//GS
            assert Ddec2//G==DW2//GS

print("OK: A2 source parity residual gcd is fully decimal with 242/244 and 440/444 windows")
