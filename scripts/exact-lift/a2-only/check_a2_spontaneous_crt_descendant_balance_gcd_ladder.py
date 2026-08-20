#!/usr/bin/env python3
"""Certificate for spontaneous-crt-descendant-balance-gcd-ladder.md."""

import math


# Local valuation model:
# M = unit * p^(h+rho) + O(p^(2h)).
def vp(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


for p in (7, 11, 19, 31):
    for h in range(1, 5):
        for rho in range(0, 7):
            # Choose unit linear coefficient 1 and a generic quadratic correction p^(2h).
            M = p ** (h + rho) + p ** (2 * h)
            vM = vp(M, p)
            # If h+rho == 2h this particular sample cancels only when 1+1 == 0 mod p;
            # all chosen odd p avoid that.  The truncated law is independent of deeper details.
            assert min(vM, 2 * h) == h + min(rho, h)

# Ordinary gcd ladder identity v_p(gcd(G^j,B))=min(jh,rho).
for p in (7, 11, 19):
    for h in range(1, 5):
        for rho in range(0, 9):
            G = p**h
            B = p**rho
            for j in range(1, 6):
                D = math.gcd(G**j, B)
                assert vp(D, p) == min(j * h, rho)

# Support selector: p divides Sigma_rec iff rho>0, i.e. first extra layer exists.
for p in (7, 11, 19):
    for h in range(1, 4):
        G = p**h
        for rho in range(0, 5):
            B = p**rho
            Sigma = math.gcd(G, B)
            assert (Sigma % p == 0) == (rho > 0)

print("OK: balance tail reads all extra depth below one full baseline and its gcd ladder has the claimed local exponents")
