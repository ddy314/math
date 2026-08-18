#!/usr/bin/env python3
"""Exact certificate for spontaneous-source-equal-depth-nogo.md."""

import sympy as sp

x, eps, d1, phi = sp.symbols("x eps d1 phi")
A = 99*x - 4
y0 = 225*x**2
r0 = 2*(x+2)/A

y = y0 - eps*d1
r = r0 + eps**2*phi/A

Phi = sp.expand(A*r - 2*x - 4)
Psi = sp.expand(3600*(r+1)**2 - y*(99*r-2)**2)
d = sp.expand(225*x**2-y)
Omega = sp.expand(4*r*d**2 - x*y**2*Phi)

# The parametrization exactly realizes the equal-depth coordinates.
assert sp.cancel(Phi - eps**2*phi) == 0
assert sp.expand(d - eps*d1) == 0
assert sp.cancel(r0 + 1 - 101*x/A) == 0
assert sp.cancel(99*r0 - 2 - 404/A) == 0

# First nonzero coefficient of the second Hensel equation.
psi_series = sp.series(Psi, eps, 0, 2).removeO()
expected_psi = eps*d1*404**2/A**2
assert sp.cancel(psi_series-expected_psi) == 0

# First nonzero normalized angle coefficient.  Extract the epsilon^2 Taylor
# coefficient directly; this avoids representation-dependent 0/0 behavior
# from substituting epsilon=0 after rational cancellation.
omega_series = sp.series(Omega, eps, 0, 3).removeO()
omega2 = sp.expand(omega_series).coeff(eps, 2)
expected_omega2 = 8*(x+2)*d1**2/A - 50625*x**5*phi
assert sp.cancel(omega2-expected_omega2) == 0

# The extra-lift equation is linear and nondegenerate in phi away from
# genuine source boundary factors p | 3*5*x.
assert sp.diff(expected_omega2, phi) == -50625*x**5
assert sp.factorint(50625) == {3: 4, 5: 4}

phi_root = sp.cancel(8*(x+2)*d1**2/(50625*A*x**5))
assert sp.cancel(expected_omega2.subs(phi, phi_root)) == 0

print("OK: A2 source equal-depth second-order no-go certified")
