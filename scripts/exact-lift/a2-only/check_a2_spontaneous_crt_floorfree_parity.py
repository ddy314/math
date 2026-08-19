#!/usr/bin/env python3
"""Certificate for spontaneous-crt-floorfree-parity.md."""

# eta=1 surviving types: (d,cQ,kh,epsilon), epsilon +1/-1.
types = [
    (1, 3, 53, +1, 3),
    (1, 103, 1, -1, 1),
    (1, 159, 1, +1, 7),
    (2, 7, 3, -1, 7),
    (2, 31, 1, +1, 3),
]

# eta=1 forces M odd. B_G=3M-d-eta-3.
Mpar = 1
eta = 1
for d, cQ, kh, eps, expected_abs_mod8 in types:
    BGpar = (3*Mpar-d-eta-3) % 2
    Pmod8 = (pow(5, BGpar, 8) * (kh % 8)) % 8
    # sign(P)=-epsilon, hence |P|=(-epsilon)P.
    abs_mod8 = ((-eps) * Pmod8) % 8
    assert abs_mod8 == expected_abs_mod8

# Exactly four of the five are 3 mod 4.
assert sum(1 for *_, r in types if r % 4 == 3) == 4

# General mod-4 criterion: kh has no 3 mod4 prime except 3,
# so kh mod4=(-1)^v3(kh). Test representative exponents.
for e3 in range(6):
    kh_mod4 = (-1)**e3 % 4
    for eps in (-1, 1):
        abs_mod4 = ((-eps) * kh_mod4) % 4
        criterion = eps == ((-1)**e3)
        assert (abs_mod4 == 3) == criterion

# k_h=3 type mod-3 reduction of D Delta_+ leaves cu^2 D^2 T.
# The logical unit conclusion is checked with sample nonzero residues.
for cu in (1, 2):
    for D in (1, 2):
        for T in (1, 2):
            residue = (cu*cu*D*D*T) % 3
            assert residue != 0

print("OK: A2 floor-free CRT carrier has the claimed mod-8 parity and eta=1 surcharge")
