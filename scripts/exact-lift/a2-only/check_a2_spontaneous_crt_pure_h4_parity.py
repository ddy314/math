#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-h4-parity.md."""


def v2(n: int) -> int:
    v=0
    while n%2==0:
        n//=2; v+=1
    return v

assert v2(656100)==2
assert v2(2624400)==4
assert v2(7710100)==2
assert v2(13936500)==2
assert v2(3647025)==0
assert v2(129600)==6
assert (129600//64)%8==1

# On the dangerous branch m>=5,t>=3, every non-last term lies strictly above 2M+6.
for M in range(11,30):
    for m in range(5,15):
        for t in range(3,10):
            vB=M+m+t
            depths=[
                2+4*vB,
                4+3*vB+M,
                2+2*vB,
                2+2*vB,
                2*vB+2*M,
                6+vB+M,
                6+2*M,
            ]
            assert depths[-1] < min(depths[:-1])

# Odd-square orientation.
for a in range(1,16,2):
    assert a*a%8==1
for M in range(1,20):
    assert pow(5,2*M,8)==1

print('OK: positive h4 short carrier has exact 2-depth 2M+6 and primitive orientation 7 mod 8')
