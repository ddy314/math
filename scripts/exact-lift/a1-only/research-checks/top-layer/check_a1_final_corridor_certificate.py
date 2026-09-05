#!/usr/bin/env python3
"""Exact certificate for the final A1 d=2, r=s=1 corridors k-g in {1,2}.

Inputs:
  * mixed L=2^a5^b (a,b>0) is empty;
  * pure-2 only needs (g,c)=(2..6,1),(3..4,2);
  * pure-5 only needs (g,c,w)=(2,1,2),(2,1,4);
  * corridor phase center:
        0 < ((J+1) tau L - M) H tau < 40 L,
    hence J is uniquely determined by (M,L);
  * global kappa-square + exact decimal-height synchronization.

No floating point is used. Small factorizations are hard-coded and primality-checked.
"""

from math import gcd, isqrt
from sympy import isprime

TYPES = ((1,1),(1,2),(1,3),(1,4),(3,1),(3,2))
LAYERS = ((2,1),(3,1),(4,1),(5,1),(6,1),(3,2),(4,2))

FACTORS = {
    (2,1,1): ({3:2,239:1,4649:1}, {7:1,13:1,769:1,1429:1}),
    (2,1,2): ({2:1,4999999:1}, {3:3,3703703:1}),
    (2,1,3): ({7:1,1428571:1}, {99999971:1}),
    (2,1,4): ({2:2,3:1,191:1,4363:1}, {179:2,3121:1}),
    (3,1,1): ({3:4,37:1,333667:1}, {19:2,277:1,100003:1}),
    (3,1,2): ({2:1,691:1,723589:1}, {3:2,17:1,2557:1,25561:1}),
    (3,1,3): ({71:1,2251:1,6257:1}, {13:1,109:1,1657:1,4259:1}),
    (3,1,4): ({2:2,3:1,83333333:1}, {7:1,23:1,62111801:1}),
    (4,1,1): ({3:2,21649:1,513239:1}, {757:1,1321:1,1000003:1}),
    (4,1,2): ({2:1,29:1,1724137931:1}, {3:2,577:1,192566917:1}),
    (4,1,3): ({17:1,5882352941:1}, {7:1,8011:1,17832623:1}),
    (4,1,4): ({2:2,3:1,13:1,7477:1,85733:1}, {999999999961:1}),
    (5,1,1): ({3:2,53:1,79:1,265371653:1}, {7:1,13:1,769231:1,1428571:1}),
    (5,1,2): ({2:1,491:1,10183299389:1}, {3:3,127:1,29163021289:1}),
    (5,1,3): ({7:2,56527:1,3610339:1}, {99999999999971:1}),
    (5,1,4): ({2:2,3:1,311:1,2679528403:1}, {433:1,1297:1,178062361:1}),
    (6,1,1): ({3:3,31:1,37:1,41:1,271:1,2906161:1}, {643:1,1297:1,77101:1,155521:1}),
    (6,1,2): ({2:1,499999999999999:1}, {3:2,5261:1,211197702169:1}),
    (6,1,3): ({599:1,2131:1,3733:1,209861:1}, {13:1,521:1,1669:1,9461:1,93503:1}),
    (6,1,4): ({2:2,3:1,307:1,271444082519:1}, {7:1,67:1,1579:1,15383:1,877817:1}),
    (3,2,1): ({3:2,21649:1,513239:1}, {757:1,1321:1,1000003:1}),
    (3,2,2): ({2:1,29:1,1724137931:1}, {3:2,577:1,192566917:1}),
    (3,2,3): ({17:1,5882352941:1}, {7:1,8011:1,17832623:1}),
    (3,2,4): ({2:2,3:1,13:1,7477:1,85733:1}, {999999999961:1}),
    (4,2,1): ({3:2,53:1,79:1,265371653:1}, {7:1,13:1,769231:1,1428571:1}),
    (4,2,2): ({2:1,491:1,10183299389:1}, {3:3,127:1,29163021289:1}),
    (4,2,3): ({7:2,56527:1,3610339:1}, {99999999999971:1}),
    (4,2,4): ({2:2,3:1,311:1,2679528403:1}, {433:1,1297:1,178062361:1}),
}


def valuation(n, p):
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def only_2_5(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n == 1


def factor_product(fac):
    out = 1
    for p,e in fac.items():
        assert isprime(p)
        out *= p**e
    return out


def merge_factor(dst, src):
    for p,e in src.items():
        dst[p] = dst.get(p,0) + e


def divisors(fac):
    ds = [1]
    for p,e in fac.items():
        old = ds
        ds = []
        pe = 1
        for _ in range(e+1):
            ds.extend(d*pe for d in old)
            pe *= p
    return ds


def phase_axis_states(g, c, w, shape):
    H = 10**g
    tau = 10**c
    n2 = 2*g + 2*c + 1
    b1 = 10**n2 - w
    Q0 = 10*b1 + 1

    fb, fq = FACTORS[(g,c,w)]
    assert factor_product(fb) == b1
    assert factor_product(fq) == Q0

    fac = {2:g+2*c, 5:g+2*c}
    merge_factor(fac, fb)
    merge_factor(fac, fq)

    basep = 2 if shape == "pure2" else 5

    for M in divisors(fac):
        if M % basep == 0:
            continue

        L = basep
        while H*L <= 10*M:
            if M < H*L:
                den = L*tau
                s = (M + den - 1)//den
                J = s - 1
                A = s*tau*L - M
                u = g-c

                if 10**(u-1) < s <= 10**u and A > 0 and A*H*tau < 40*L:
                    yield M,L,J,A
            L *= basep


def terminal_survives(g,c,z,w,J,M,L):
    H = 10**g
    tau = 10**c
    n2 = 2*g + 2*c + 1

    b1 = 10**n2 - w
    b2 = tau
    a2 = 10**n2 - z
    a1 = 10**(3*g + 2*c + 2) + (10*(5-z-w)+1)*H + J

    Q0 = 10*b1 + 1
    Q = tau*Q0
    G = tau*b1
    D = H*Q
    C = a1*10**n2 + a2
    N = (a1*b2)**2 + (a2*b1)**2
    K = G*G*C*C - D*D*N

    base = H*Q*G
    assert base % M == 0
    kappa = base*L//M

    W2 = kappa*(kappa*K - 2*G*D*D*N)
    if W2 < 0:
        return False
    W = isqrt(W2)
    if W*W != W2:
        return False

    Y = kappa*kappa*(kappa+2*G)
    M10 = M
    while M10 % 2 == 0:
        M10 //= 2
    while M10 % 5 == 0:
        M10 //= 5

    aL = valuation(L,2)
    bL = valuation(L,5)

    for sigma in (1,-1):
        X = kappa*G*G*C + sigma*(kappa+G)*W
        if X <= 0:
            continue

        h = gcd(X,Y)
        u = X//h
        v = Y//h

        if not (10*u >= v and u < v):
            continue
        if not only_2_5(v):
            continue

        d2 = valuation(v,2)
        d5 = valuation(v,5)
        H2 = max(d2,aL)
        H5 = max(d5,bL)
        if H2 != H5 or H2 < 1:
            continue
        if gcd(u,M10) != 1:
            continue

        return True

    return False


def main():
    phase_rows = []
    terminal_tests = 0
    survivors = []

    for g,c in LAYERS:
        for w in (1,2,3,4):
            for M,L,J,A in phase_axis_states(g,c,w,"pure2"):
                phase_rows.append((g,c,w,"pure2",M,L,J,A))
                for z,w2 in TYPES:
                    if w2 != w:
                        continue
                    terminal_tests += 1
                    if terminal_survives(g,c,z,w,J,M,L):
                        survivors.append((g,c,z,w,J,M,L,"pure2",A))

    for w in (2,4):
        g,c = 2,1
        for M,L,J,A in phase_axis_states(g,c,w,"pure5"):
            phase_rows.append((g,c,w,"pure5",M,L,J,A))
            for z,w2 in TYPES:
                if w2 != w:
                    continue
                terminal_tests += 1
                if terminal_survives(g,c,z,w,J,M,L):
                    survivors.append((g,c,z,w,J,M,L,"pure5",A))

    print(f"phase_states={len(phase_rows)}")
    print(f"terminal_tests={terminal_tests}")
    print(f"survivors={len(survivors)}")
    print("phase_rows:")
    for row in phase_rows:
        print(row)

    assert len(phase_rows) == 26
    assert terminal_tests == 37
    assert survivors == []


if __name__ == "__main__":
    main()
