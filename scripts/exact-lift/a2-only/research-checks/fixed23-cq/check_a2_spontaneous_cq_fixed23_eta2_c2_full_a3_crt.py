#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md."""

from math import gcd

cQ = 1587
assert cQ == 3 * 23**2

allocations = [(1, 1587), (3, 529), (529, 3), (1587, 1)]
for cm, cp in allocations:
    assert cm * cp == cQ
    assert gcd(cm, cp) == 1

assert [cm for cm, cp in allocations if cm % (23**2) == 0] == [529, 1587]
assert [cm for cm, cp in allocations if cp % (23**2) == 0] == [1, 3]


def crt_pair(a, m, b, n):
    """Return unique residue modulo mn for gcd(m,n)=1."""
    assert gcd(m, n) == 1
    k = ((b - a) * pow(m, -1, n)) % n
    return (a + m * k) % (m * n)


# Canonical a3 mod cQ from g/2 signs on c_-,c_+.
for g0 in (4, 8, 20, 100):
    half = g0 // 2
    for cm, cp in allocations:
        rq = crt_pair(half % cm if cm > 1 else 0, cm,
                      (-half) % cp if cp > 1 else 0, cp)
        if cm > 1:
            assert rq % cm == half % cm
        if cp > 1:
            assert rq % cp == (-half) % cp

# Full CRT scale and window fraction.
for lam in (8, 19, 52):
    m = lam + 1
    T = 10**m
    Mtwo = 2**m
    Mfive = 5**(lam - 1)
    Mfull = cQ * Mtwo * Mfive
    assert Mtwo * Mfive == T // 25
    assert Mfull == cQ * (T // 25)
    # T/250 = Mfull/15870 exactly.
    assert T * 15870 == 250 * Mfull

    # Synthetic three-way CRT sanity check.
    r2 = 1
    r5 = 2 % Mfive
    rq = 3 % cQ
    r25 = crt_pair(r2, Mtwo, r5, Mfive)
    rfull = crt_pair(r25, Mtwo * Mfive, rq, cQ)
    assert rfull % Mtwo == r2
    assert rfull % Mfive == r5
    assert rfull % cQ == rq

    shifted = (rfull - T) % Mfull
    assert 0 <= shifted < Mfull

print("OK: A2 fixed-23 c2 full canonical a3 CRT has cell fraction 1/15870")
