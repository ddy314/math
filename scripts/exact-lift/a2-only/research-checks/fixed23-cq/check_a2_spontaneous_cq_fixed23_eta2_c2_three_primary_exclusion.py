#!/usr/bin/env python3
"""Exact mod-3 certificate for spontaneous-cq-fixed23-eta2-c2-three-primary-exclusion.md."""

import sympy as sp

A, B, N, T, Q, b3 = sp.symbols("A B N T Q b3", integer=True)
U = (45 * B**2 - 2 * A * N) ** 2 - A**2 * B * (99 * B - 4 * N)

# Q=0 mod3 gives B=-2N=N mod3. Substitute B=N into U and verify
# U=-A^2 N^2 mod3.
U_layer = sp.expand(U.subs(B, N))
poly = sp.Poly(sp.expand(U_layer + A**2 * N**2), A, N)
assert all(int(c) % 3 == 0 for c in poly.coeffs())

# Direct residue audit for all unit A,N,T residues and arbitrary b3.
for a in (1, 2):
    for n in (1, 2):
        b = n  # B=N mod3
        u = int(U.subs({A: a, N: n, B: b})) % 3
        assert u == (-a * a * n * n) % 3
        assert u != 0
        for t in (1, 2):
            for bb3 in range(3):
                # Q term vanishes mod3.
                for sign in (-1, 1):
                    oval = (t * u + sign * 2 * a * a * 0 * bb3) % 3
                    assert oval != 0

print("OK: p=3 is absent from both primitive angle signs in the A2 c_Q=3*23^2 type")
