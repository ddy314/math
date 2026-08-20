#!/usr/bin/env python3
"""Certificate for spontaneous-height-equal-depth-fixed7-h1-orthogonal-audit.md."""

import sympy as sp

k,k2,l,l2,a = sp.symbols("k k2 l l2 a", integer=True)
K = 4 + 7*k + 49*k2
d = 2 + 7*l + 49*l2
P = 6*K**2 - 36*K + 55
u = d*K - 1                    # U/N
rp = d*P - K*u                 # R_+/N
alpha_over_T = 49*a
lperp = (55*d-18)*alpha_over_T + 3*rp + (53-15*K)*u  # L_perp/(NT)


def mod_poly(expr, vars_, p=7):
    poly = sp.Poly(sp.expand(expr), *vars_)
    out = 0
    for mon, coeff in poly.terms():
        term = int(coeff) % p
        for var, exp in zip(vars_, mon):
            term *= var**exp
        out += term
    return sp.expand(out)

# First normalized digits.
assert mod_poly(P/7,[k,k2,l,l2,a]) == 5*k + 1
assert mod_poly(u/7,[k,k2,l,l2,a]) == 2*k + 4*l + 1
assert mod_poly(rp/7,[k,k2,l,l2,a]) == 2*k + 5*l + 5

# Deep R+ forces l=k+6, and exact h=1 excludes k=4.
for kv in range(7):
    roots_l = [lv for lv in range(7) if (5+2*kv+5*lv) % 7 == 0]
    assert roots_l == [(kv+6)%7]
    lv=(kv+6)%7
    punit=(1+5*kv)%7
    uunit=(1+2*kv+4*lv)%7
    assert (punit==0) == (kv==4)
    assert (uunit==0) == (kv==4)

# Use l=k+6; a 7-shift is absorbed into l2.
lperp49 = mod_poly(sp.expand(lperp.subs(l,k+6))/49,[k,k2,l2,a])
assert sp.Poly(lperp49-(a+k**2+6*k+6*k2+l2),k,k2,l2,a,modulus=7).is_zero

# Orthogonal second-extra uniquely fixes l2.
l2_sol = k2+k-k**2-a
assert sp.Poly(sp.expand(lperp49.subs(l2,l2_sol)),k,k2,a,modulus=7).is_zero

# Then R+/49 becomes 2a+2k^2+k-1, independent of k2.
rp49 = mod_poly(sp.expand(rp.subs(l,k+6))/49,[k,k2,l2,a])
rp49_sub = sp.Poly(sp.expand(rp49.subs(l2,l2_sol)),k,k2,a,modulus=7).as_expr()
expected = 2*a + 2*k**2 + k - 1
assert sp.Poly(rp49_sub-expected,k,k2,a,modulus=7).is_zero

# Complete exact-h=1 residue table.
expected_a={0:4,1:6,2:6,3:4,5:1,6:0}
classes={0:4,1:11,2:18,3:25,5:39,6:46}
for kv, kval in classes.items():
    assert (4+7*kv)%49 == kval
    solutions=[av for av in range(7) if (2*av+2*kv*kv+kv-1)%7==0]
    assert solutions == [expected_a[kv]]
# k=4 is the quadratic h>=2 lift; K=46 would require a=0, impossible for a unit.
assert (4+7*4)%49 == 32
assert expected_a[6] == 0

print("OK: A2 fixed-7 K=4 h=1 orthogonal branch has the stated finite normalized residue templates")
