#!/usr/bin/env python3
"""Certificate for outer-descendant-additive-lock.md.

The new additive/descendant gcd theorem says every descendant-common prime is
also a prime of the original primitive additive carrier.  Hence the coefficient
ratio in the rational-root quartic is no longer free: modulo such a prime it is
R0=K^2-(18+4*zeta)K+18*zeta+55.

If the same prime divides both outer cofactors Xi_-,Xi_+, then the normalized
quartic values at J=2 and J=4 both vanish with this fixed R0.  Their resultant
has only the sheets K=3, 2K-9=0, and one irreducible quartic Q4(K).
Intersecting these with the source-common line 18K-55=0 leaves only the odd
primes 13 and 1350049, both 1 mod 4.  Therefore a genuine inert source-common
prime cannot simultaneously pay both outer cofactors and descendant common.
"""

import sympy as sp

K, zeta, J = sp.symbols("K zeta J")

R0 = K**2 - (18 + 4*zeta)*K + 18*zeta + 55
Phi = sp.expand(J*(J + 2*zeta)*(K - J)**2 - R0*(J + zeta)**2)
Phi2 = sp.expand(Phi.subs(J, 2))
Phi4 = sp.expand(Phi.subs(J, 4))

expected2 = (
    -K**2*zeta**2 + 4*K*zeta**3 + 34*K*zeta**2 + 72*K*zeta + 56*K
    - 18*zeta**3 - 127*zeta**2 - 276*zeta - 204
)
expected4 = (
    -K**2*zeta**2 + 4*K*zeta**3 + 50*K*zeta**2 + 144*K*zeta + 160*K
    - 18*zeta**3 - 199*zeta**2 - 600*zeta - 624
)
assert sp.expand(Phi2 - expected2) == 0
assert sp.expand(Phi4 - expected4) == 0

H24 = sp.factor((Phi4 - Phi2)/4)
expected_H24 = (
    4*K*zeta**2 + 18*K*zeta + 26*K
    - 18*zeta**2 - 81*zeta - 105
)
assert sp.expand(H24 - expected_H24) == 0

Q4 = 676*K**4 - 8004*K**3 + 34801*K**2 - 65868*K + 45964
res = sp.factor(sp.resultant(Phi2, H24, zeta))
assert sp.expand(res - 2*(K - 3)**2*(2*K - 9)*Q4) == 0
assert sp.Poly(Q4, K, domain=sp.ZZ).is_irreducible

# Source-common line.
LS = 18*K - 55
assert sp.resultant(K - 3, LS, K) == -1
assert sp.resultant(2*K - 9, LS, K) == 52
res_q4 = int(sp.resultant(Q4, LS, K))
assert res_q4 == 21600784
assert sp.factorint(res_q4) == {2: 4, 1350049: 1}
assert sp.isprime(1350049)
assert 13 % 4 == 1
assert 1350049 % 4 == 1

# Thus there is no odd inert prime in the source-common intersection.
assert all(p % 4 == 1 for p in (13, 1350049))

# Historical fixed common labels: 31/179 miss Q4; 7 sits on the central
# factor and is handled by the direct F_p outer-pair audit in the companion
# checker, not by Q4 alone.
for p, k, expected in [(31, 9, 13), (179, 71, 41)]:
    assert int(Q4.subs(K, k)) % p == expected
assert (2*1 - 9) % 7 == 0

# The weaker source-common/E63 elimination had left one giant inert candidate.
# It is killed as soon as the additive coefficient-ratio lock is imposed.
pstar = 740759498168792879433565547
kstar = 55 * pow(18, -1, pstar) % pstar
zetastar = 121854543490110025177920950
assert int(Phi2.subs({K:kstar, zeta:zetastar})) % pstar != 0
assert int(Phi4.subs({K:kstar, zeta:zetastar})) % pstar != 0

print("OK: additive lock deletes the entire source-common shared outer/descendant inert pool")
