#!/usr/bin/env python3
"""Exact certificate for spontaneous-angle-parity.md."""

import sympy as sp

M, m = sp.symbols("M m", integer=True, positive=True)
A, b0, q0, b30 = sp.symbols("A b0 q0 b30", integer=True)
N, B, Q, b3, T = sp.symbols("N B Q b3 T", integer=True)

U = (45*B**2 - 2*A*N)**2 - A**2*B*(99*B - 4*N)
O = T*U + 2*A**2*Q*b3

# Substitute the exact 2-adic source scales, keeping 5-powers symbolic.
fiveM, fivem = sp.symbols("fiveM fivem", integer=True)
subs = {
    N: 2**M * fiveM,
    B: 2**(M+m+1) * b0,
    Q: 2**(M+1) * q0,
    b3: 2**(M+m+1) * b30,
    T: 2**m * fivem,
}
Us = sp.expand(U.subs(subs))
Os = sp.expand(O.subs(subs))

# Exact quotient U / 2^(2M+2).
Usharp = sp.simplify(Us / 2**(2*M+2))
expected_Usharp = (
    (45*2**(M+2*m+1)*b0**2 - A*fiveM)**2
    - A**2 * 2**(m+1)*b0*(99*2**(m-1)*b0 - fiveM)
)
assert sp.simplify(Usharp - expected_Usharp) == 0

# Exact quotient O / 2^(2M+m+2).
Osharp = sp.simplify(Os / 2**(2*M+m+2))
expected_Osharp = fivem*expected_Usharp + 2*A**2*q0*b30
assert sp.simplify(Osharp - expected_Osharp) == 0

# Parity certificate: for all odd inputs and m>=1, Usharp == 1 mod 4,
# Osharp == 3 mod 4.  Exhaust all odd residue classes modulo 8 and a few m.
for mm in range(1, 5):
    for aa in (1,3,5,7):
        for bb in (1,3,5,7):
            for qq in (1,3,5,7):
                for cc in (1,3,5,7):
                    # fiveM and fivem are odd powers of 5; modulo 8 each is 1 or 5.
                    for fm in (1,5):
                        for fn in (1,5):
                            us = int(expected_Usharp.subs({M:3,m:mm,A:aa,b0:bb,fiveM:fm}))
                            os = int(expected_Osharp.subs({M:3,m:mm,A:aa,b0:bb,q0:qq,b30:cc,fiveM:fm,fivem:fn}))
                            assert us % 4 == 1
                            assert os % 4 == 3

print("OK: A2 spontaneous angle parity carrier certified")
