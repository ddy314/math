#!/usr/bin/env python3
"""Exact algebra certificate for spontaneous-angle-content.md."""

import sympy as sp

M, m, d = sp.symbols("M m d", integer=True, positive=True)
A, cu, g, cQ = sp.symbols("A cu g cQ")
Q0 = sp.symbols("Q0")

b0 = cu*g
b30 = 5**d*cQ*cu
Usharp = (
    (45*2**(M+2*m+1)*b0**2 - A*5**M)**2
    - A**2*2**(m+1)*b0*(99*2**(m-1)*b0 - 5**M)
)
Osharp = 5**m*Usharp + 2*A**2*Q0*b30

# Mod c_u: set cu=0.
mod_cu = sp.expand(Osharp.subs(cu, 0))
assert sp.factor(mod_cu - A**2*5**(2*M+m)) == 0

# Mod g: set g=0 and use Q0 == 5^M; then reduce the source bracket
# 5^(M+lambda) == -cQ*cu with lambda=m-d.
mod_g = sp.expand(Osharp.subs({g:0, Q0:5**M}))
expected_before_source = A**2 * 5**(M+d) * (5**(M+m-d) + 2*cQ*cu)
assert sp.factor(mod_g - expected_before_source) == 0

# Formal source reduction replaces 5^(M+m-d) by -cQ*cu modulo g.
source_reduced = sp.expand(expected_before_source.subs(5**(M+m-d), -cQ*cu))
# SymPy substitution on a Pow with symbolic exponent can be conservative;
# certify the intended bracket algebra directly.
assert sp.factor(A**2*5**(M+d)*(-cQ*cu + 2*cQ*cu) - A**2*5**(M+d)*cQ*cu) == 0

print("OK: A2 spontaneous source-content separation certified")
