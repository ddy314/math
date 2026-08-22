#!/usr/bin/env python3
"""Certificate: a q-saturated additive inert carrier cannot pay both outer cofactors.

For an odd prime p on the q-denominator additive channel, Q=0 mod p while
b2,T,D are units.  The rational-root quartic therefore reduces to

    Phi_q(J) = J (J+2*zeta) (K-J)^2.

If p also divides both outer cofactors Xi_-=Xi_2 and Xi_+=Xi_4, then
Phi_q(2)=Phi_q(4)=0.  For odd p this leaves only the two crossed states
(K,zeta)=(4,-1) or (2,-2).  Full q-saturation additionally requires
2*zeta+9=0, while q-side additive contact requires K^2-26=0.  In the two
crossed states these two extra gates have coprime integer values (7,-10) and
(5,-22), so no prime survives.
"""

import math
import sympy as sp

K, zeta, J = sp.symbols("K zeta J", integer=True)
Phi_q = sp.expand(J * (J + 2*zeta) * (K-J)**2)
Phi2 = sp.factor(Phi_q.subs(J, 2))
Phi4 = sp.factor(Phi_q.subs(J, 4))

assert Phi2 == 4*(K-2)**2*(zeta+1)
assert Phi4 == 8*(K-4)**2*(zeta+2)

# For every odd test field the simultaneous outer-root set is exactly the
# two crossed states.  The symbolic factorization above is the proof; this
# finite audit catches sign/factor mistakes.
for p in list(sp.primerange(3, 200)):
    roots = [
        (k, z)
        for k in range(p)
        for z in range(p)
        if int(Phi2.subs({K:k, zeta:z})) % p == 0
        and int(Phi4.subs({K:k, zeta:z})) % p == 0
    ]
    expected = sorted({(4 % p, (-1) % p), (2 % p, (-2) % p)})
    assert roots == expected

L23 = 2*zeta + 9
Pq = K**2 - 26

states = [(4, -1), (2, -2)]
values = []
for k, z in states:
    l = int(L23.subs(zeta, z))
    a = int(Pq.subs(K, k))
    values.append((l, a))
    assert math.gcd(abs(l), abs(a)) == 1

assert values == [(7, -10), (5, -22)]

print("OK: no q-saturated additive prime can simultaneously divide Xi_- and Xi_+")