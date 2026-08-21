#!/usr/bin/env python3
"""Certificate for fixed-target-serial-dichotomy.md.

The historical h=1 target/descent audit leaves exactly one triple-deep
p^3 state for p=31 and p=179.  This checker verifies that both states have
baseline target depth h=1 and exact R_+ depth 3, hence r_+=2, and then
exhausts the canonical two-node serial valuation laws.  The result is a
strict dichotomy: rho=1 forces the second serial node to be the extra node;
rho>1 forces the first node to be extra and min(c,rho)=2.
"""


def vp(n: int, p: int) -> int:
    n = abs(int(n))
    assert n
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def P(K: int) -> int:
    return 6*K*K - 36*K + 55


def U_over_N(K: int, d: int) -> int:
    return d*K - 1


def Rplus_over_N(K: int, d: int) -> int:
    u = U_over_N(K, d)
    return d*P(K) - K*u


# Unique p^3 triple-deep states from the historical fixed-h1 audit.
states = {
    31: (17307, 22110),
    179: (5430752, 890583),
}

for p, (K, d) in states.items():
    assert 0 <= K < p**3
    assert 0 <= d < p**3
    assert vp(P(K), p) == 1
    assert vp(U_over_N(K, d), p) == 1
    assert vp(Rplus_over_N(K, d), p) == 3
    # h=1 and v_p(R_+)=3, so the actual extra depth is exactly r_+=2.
    assert vp(Rplus_over_N(K, d), p) - 1 == 2


# Canonical serial laws at h=1.
# r_B, rho, c are positive depths and r_+=2 is fixed above.
# Historical tropical law: min(r_B,rho)=1.
# First node: c >= min(r_B,1), with equality if r_B != 1.
# Second node: r_+ >= min(rho,c), with equality if rho != c.
solutions = []
for rB in range(1, 8):
    for rho in range(1, 8):
        for c in range(1, 8):
            rplus = 2
            if min(rB, rho) != 1:
                continue
            if c < min(rB, 1):
                continue
            if rB != 1 and c != min(rB, 1):
                continue
            if rplus < min(rho, c):
                continue
            if rho != c and rplus != min(rho, c):
                continue
            solutions.append((rB, rho, c))

assert solutions
for rB, rho, c in solutions:
    if rho == 1:
        # second-node strict: c=rho=1<r_+=2
        assert c == 1
        assert c == rho < 2
        # The second conjugate D_E therefore has exact depth 2h+c=3.
        assert 2 + c == 3
    else:
        # tropical forces r_B=h=1; r_+>1 then forbids c=1.
        assert rB == 1
        assert c > 1
        # Since r_+=2, the second-node minimum is forced to be exactly 2.
        assert min(c, rho) == 2
        # Hence the first serial node is strict: r_B=h<c and rho>h.
        assert rB == 1 < c
        assert rho > 1
        # B_W has exponent h+r_B=2, so this fixed prime is parity-neutral there.
        assert 1 + rB == 2

print("OK: fixed 31/179 triple-deep targets split into second-node rho=1 or first-node rho>1 serial regimes")
