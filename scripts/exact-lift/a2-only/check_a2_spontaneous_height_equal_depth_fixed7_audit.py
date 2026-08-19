#!/usr/bin/env python3
"""Finite mod-7 certificate for spontaneous-height-equal-depth-fixed7-audit.md."""

p=7
inv2=pow(2,-1,p)
rows=[]

for Mmod in range(6):
    N=pow(3,Mmod,p)  # 10^M == 3^M mod 7
    A=(3*(1-N))%p    # forced by K == 2 mod 7
    K=(9*N+10*A)%p
    assert K==2

    admissible=[]
    for B in range(1,p):
        Q=(B+2*N)%p
        N0=(((9*B*inv2)%p)**2 + A*A)%p
        if Q==0 or N0==0:
            continue
        H=(B*B*K*K + Q*Q*N0)%p
        if H==0:
            admissible.append((B,Q,N0))

    rows.append((Mmod,N,A,admissible))

expected=[
    (0,1,0,[]),
    (1,3,1,[(2,1,5),(4,3,3)]),
    (2,2,4,[]),
    (3,6,6,[]),
    (4,4,5,[]),
    (5,5,2,[(1,4,5),(3,6,6)]),
]
assert rows==expected

# All surviving N0 values are quadratic nonresidues mod 7.
squares={x*x%7 for x in range(1,7)}
for _,_,_,states in rows:
    for _,_,N0 in states:
        assert N0 not in squares

print("OK: A2 fixed 7 extra-depth target survives only M=1,5 mod 6 in four residue states")
