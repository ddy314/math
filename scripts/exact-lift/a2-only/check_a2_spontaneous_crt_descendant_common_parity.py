#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-common-parity.md."""

# Parent orientations: Rstar = 3 mod4; Dhat = 3*Z mod4.
for Z in (1, 3):
    R = 3
    D = (3 * Z) % 4
    assert R in (1, 3) and D in (1, 3)
    for G in (1, 3):
        inv = pow(G, -1, 4)
        Rc = (R * inv) % 4
        Dc = (D * inv) % 4
        if Z == 1:
            if G == 1:
                assert (Rc, Dc) == (3, 3)
            else:
                assert (Rc, Dc) == (1, 1)
        else:
            assert sorted((Rc, Dc)) == [1, 3]

# Fixed target labels are 3 mod4 and their product is 1 mod4.
assert 31 % 4 == 3
assert 179 % 4 == 3
assert (31 * 179) % 4 == 1

print("OK: descendant common gcd gives the stated Z-dependent mod-4 parity dichotomy")
