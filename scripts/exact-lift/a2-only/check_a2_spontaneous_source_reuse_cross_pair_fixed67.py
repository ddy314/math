#!/usr/bin/env python3
"""Certificate for spontaneous-source-reuse-cross-pair-fixed67.md."""

p=67
assert pow(10,33,p)==1
assert all(pow(10,d,p)!=1 for d in (1,3,11))
assert pow(2,33,p)==p-1
assert pow(10,-1,p)==47
assert (55*pow(18,-1,p))%p==44
A=((44-9)*pow(10,-1,p))%p
assert A==37
assert (47-A)%p==10

for tpar,coeff,expected in [
    (0,34,{53:12,37:47}),
    (1,33,{53:55,37:20}),
]:
    for B,H in expected.items():
        assert ((B-47)*pow(coeff,-1,p))%p==H

print("OK: A2 fixed 67 cross-pair states reduce to four simple decimal-defect templates")
