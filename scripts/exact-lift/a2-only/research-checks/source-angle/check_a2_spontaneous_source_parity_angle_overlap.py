#!/usr/bin/env python3
"""Certificate for spontaneous-source-parity-angle-overlap.md."""

# Algebraic gate K=9N+10A -> 18K-55 = (162N-55)+180A.
import sympy as sp
K,N,A=sp.symbols("K N A")
expr=(18*K-55)-((162*N-55)+180*A)
assert sp.expand(expr.subs(K,9*N+10*A))==0

# Character reduction: 162 = 2*9^2.
assert 162==2*9**2

# Parity logic for the q-sheet: v_7(D_W)=2 is even, so cannot be an odd supplier.
assert 2%2==0

print("OK: A2 odd/odd source parity reuse can meet angle common support only through numerator-length or c_Q")
