#!/usr/bin/env python3
"""Certificate for fixed3-f-contact-orientation.md.

In the Z=1, a2-shallow odd-3 channel, combine:
  * exact high/low sphere-factor 3-depths (e3, 4-e3), e3 in {1,3};
  * f-contact, f = 5^lambda q + 2 c_u = 0 mod 3;
  * Q0 = c_Q q = 5^M + 2^m g c_u;
  * lambda = m-d.

Writing B = c_Q 5^d mod 3 and delta=(-1)^(M+m)=(-1)^(m-eta),
Q0+f-contact gives B = g + delta*c_u^{-1}.  The exact sphere-factor
depths give epsilon*B=-g for e3=1 and epsilon*B=g for e3=3.
The finite F_3 unit audit below proves this forces

    e3=1 => epsilon=+1,
    e3=3 => epsilon=-1,

and in either case B=-g, g*c_u=delta, omega=-delta.
"""

P = 3
UNITS = (1, 2)  # 2 == -1 mod 3


def inv(x: int) -> int:
    return pow(x, -1, P)


solutions = []
for e3 in (1, 3):
    sigma = 2 if e3 == 1 else 1  # epsilon*B = sigma*g
    for eps in UNITS:             # +1 or -1
        for g in UNITS:
            for cu in UNITS:
                for delta in UNITS:
                    # Q0 identity after f-contact and lambda=m-d:
                    # B = g + delta*c_u^{-1}.
                    B = (g + delta * inv(cu)) % P
                    if B == 0:
                        continue

                    # Exact high/low 3-depth relation.
                    if (eps * B - sigma * g) % P:
                        continue

                    # f=g*omega+c_u=0 mod3 fixes omega.
                    omega = (-cu * inv(g)) % P
                    solutions.append((e3, eps, g, cu, delta, B, omega))

assert solutions

for e3, eps, g, cu, delta, B, omega in solutions:
    if e3 == 1:
        assert eps == 1
    else:
        assert e3 == 3 and eps == 2
    assert B == (-g) % P
    assert (g * cu) % P == delta
    assert omega == (-delta) % P

# Both allowed orientations really occur in the abstract unit system; the
# theorem is an orientation selector, not an abstract impossibility claim.
assert {e3 for e3, *_ in solutions} == {1, 3}

# The historical eta=1 odd-3 survivor has k_h=3 (e3=1) on the negative slot.
# The selector excludes it immediately.
assert not any(e3 == 1 and eps == 2 for e3, eps, *_ in solutions)

print("OK: a2-shallow fixed-3 f-contact forces e3=1/+ or e3=3/- orientation")
