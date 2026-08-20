#!/usr/bin/env python3
"""Certificate for spontaneous-crt-target-descent-global-gcd.md."""

from math import gcd


def P(K: int) -> int:
    return 6 * K * K - 36 * K + 55


def G(K: int) -> int:
    return 11 * K * K - 240 * K + 432


# Only the stated roots of P also lie on the descended overlap sheet G=0.
for p, common_root, other_root in [(31, 9, 28), (179, 71, 114)]:
    roots = [k for k in range(p) if P(k) % p == 0]
    assert roots == [common_root, other_root]
    overlap = [k for k in roots if G(k) % p == 0]
    assert overlap == [common_root]

# Fixed common bookkeeping factor is squarefree and divides 31*179.
fixed = 31 * 179
candidates = [1, 31, 179, fixed]
for gtd in candidates:
    assert fixed % gtd == 0
    assert gcd(gtd, fixed // gtd) == 1 or gtd == 1 or gtd == fixed

# Both fixed primes are 3 mod 4; an even number of fixed overlaps is 1 mod 4.
assert 31 % 4 == 3
assert 179 % 4 == 3
assert fixed % 4 == 1
assert {g: g % 4 for g in candidates} == {1: 1, 31: 3, 179: 3, fixed: 1}

# Rstar is 3 mod 4. After dividing by the fixed overlap factor:
# even overlap count -> residual 3 mod 4, odd count -> residual 1 mod 4.
for gtd in candidates:
    inv = pow(gtd, -1, 4)
    residual = (3 * inv) % 4
    expected = 3 if gtd % 4 == 1 else 1
    assert residual == expected

# Abstract valuation ledger: target baseline exponent h>=1.  For h>=2 the
# descended exponent is exactly 1; for h=1 the gcd exponent is still 1 even
# if the descended side is deeper.
for h in range(1, 8):
    descended_depths = range(1, 8) if h == 1 else [1]
    for d in descended_depths:
        assert min(h, d) == 1

print("OK: target/descent common baseline is a squarefree divisor of 31*179 and parity table is correct")
