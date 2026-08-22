#!/usr/bin/env python3
"""Certificate for additive-descendant-gcd-interface.md.

The fully primitive descendant split is

    T = 5^lambda R + g 2^m D,

with gcd(R,10g)=1 and gcd(D,5)=1.  Hence

    gcd(T,R) = gcd(R,D),
    gcd(T,D) = gcd(R,D).

This script exhausts many bounded integer models satisfying exactly these
coprimality hypotheses and verifies the identities, including prime-support
consequences.  The proof itself is elementary Euclid/gcd algebra; the finite
loop is only a regression certificate, not an A2 enumeration.
"""

from math import gcd

for lam in range(1, 5):
    five = 5**lam
    for m in range(1, 5):
        two = 2**m
        for g in range(1, 50, 2):
            if gcd(g, 5) != 1:
                continue
            for R in range(1, 120, 2):
                if gcd(R, 10*g) != 1:
                    continue
                for D in range(1, 120, 2):
                    if gcd(D, 5) != 1:
                        continue
                    T = five*R + g*two*D
                    G = gcd(R, D)
                    assert gcd(T, R) == G
                    assert gcd(T, D) == G

                    # Any prime shared by T and one descendant parent is shared
                    # by both parents.  Check by trial division of this bounded
                    # model; this is just a support-level regression audit.
                    n = T
                    p = 3
                    while p*p <= n:
                        if n % p == 0:
                            if R % p == 0 or D % p == 0:
                                assert R % p == 0 and D % p == 0
                            while n % p == 0:
                                n //= p
                        p += 2
                    if n > 1 and (R % n == 0 or D % n == 0):
                        assert R % n == 0 and D % n == 0

print("OK: additive support meets either descendant parent exactly through the common gcd")
