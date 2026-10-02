"""A2-G10/F05/F06: effective tail bound for fixed first two blocks.

Complete m2=2,3,4 prefix census and finite support enumeration; product and
lcm-sphere discriminants are independently expanded on every tail row.
All arithmetic uses arbitrary-precision integers and exact fractions.
"""

import argparse
from fractions import Fraction as F
from math import gcd, isqrt, lcm

import sympy as sp
from sympy import divisors


def vp(n, p):
    assert n > 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def cutoff(base, exp, threshold):
    m = 0
    while base ** (exp * m) < threshold:
        m += 1
    return m - 1


def bounds(A, B, N, M, T):
    Q = B * T + M
    C0 = A * T + 10 * N
    D0 = (B * M) ** 2
    S = (A * M) ** 2 + (B * N) ** 2
    k2 = vp(S, 2) - vp(D0, 2)
    k5 = vp(S, 5) - vp(D0, 5)
    d2, d5 = vp(Q, 2), vp(Q, 5)
    c2, c5 = vp(C0, 2), vp(C0, 5)
    assert c2 >= 1 and c5 >= 1
    L = lcm(B, M, Q)
    L //= 2 ** vp(L, 2) * 5 ** vp(L, 5)
    sheets = [
        6,
        vp(M, 2) - d2 - 2,
        2 * d2 + k2 - 3 * c2 - 1,
        2 * d5 + k5 - 3 * c5,
        cutoff(2, 2, F(L**3) * F(2) ** (d2 + 4 - k2) * F(5) ** (3 * d5)),
        cutoff(5, 2, F(L**3) * F(2) ** (3 * d2) * F(5) ** (d5 - k5)),
        cutoff(5, 1, L * 2**d2),
    ]
    return max(sheets), L, sheets


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--middle-digits", type=int, choices=(2, 3, 4), default=2)
    m2 = parser.parse_args().middle_digits
    A, B, N, M, T, U, b = sp.symbols("A B N M T U b", positive=True)
    Q = B * T + M
    C0 = A * T + 10 * N
    D0 = (B * M) ** 2
    S = (A * M) ** 2 + (B * N) ** 2
    beta = Q * U + b
    D = C0 * C0 * D0 - Q * Q * S
    z2 = D0 * (beta**2 - b**2)
    z1 = -2 * C0 * U * b * b * D0
    z0 = beta**2 * b * b * S - C0 * C0 * U * U * b * b * D0
    W = U * (U * D - 2 * Q * b * S)
    assert sp.factor(z1 * z1 - 4 * z2 * z0 - 4 * (B * M * beta * b) ** 2 * W) == 0
    prefixes = []
    T = 10**m2
    for B in (1, 2):
        for A in range(1, 9) if B == 1 else (5, 7, 9, 11, 13):
            for M in range(T // 10, T):
                for N in range(T // 100, T // 10):
                    if gcd(N, M) != 1:
                        continue
                    Q = B * T + M
                    C0 = A * T + 10 * N
                    D0 = (B * M) ** 2
                    S = (A * M) ** 2 + (B * N) ** 2
                    D = C0 * C0 * D0 - Q * Q * S
                    if D <= Q * Q * D0:
                        continue
                    bound, L, _sheets = bounds(A, B, N, M, T)
                    assert bound >= 6
                    prefixes.append((A, B, N, M, bound, L))
    assert (len(prefixes), max(r[4] for r in prefixes)) == {
        2: (102, 20),
        3: (11993, 30),
        4: (1229008, 40),
    }[m2]
    counts = [0, 0]
    squares = []
    hits = []
    for A, B, N, M, bound, L in prefixes:
        T = 10**m2
        Q = B * T + M
        C0 = A * T + 10 * N
        D0 = (B * M) ** 2
        S = (A * M) ** 2 + (B * N) ** 2
        D = C0 * C0 * D0 - Q * Q * S
        e, f, F5 = vp(B, 2), vp(M, 2), vp(M, 5)
        d2, d5 = vp(Q, 2), vp(Q, 5)
        c2p, c5p = vp(C0, 2), vp(C0, 5)
        k2p, k5p = vp(S, 2) - vp(D0, 2), vp(S, 5) - vp(D0, 5)
        Cs = divisors(L)
        for m in range(1, bound + 1):
            U = 10**m
            gs = (
                set(range(max(e, f, d2 + m) + 1))
                if m2 == 2
                else {0, d2 + m, m + d2 - 1}
            )
            if m2 >= 3:
                numerator = m + d2 + 1 - k2p
                if numerator % 3 == 0:
                    gs.add(numerator // 3)
                gs.update(range(max(e, f) + 1, d2 - c2p + 1))
            for g in sorted(gs):
                if g < 0:
                    continue
                if g == 0 and (B != 1 or M % 2 == 0 or A % 2 or N % 2 or m > 6):
                    continue
                Js = set(range(max(F5, d5 + m) + 1)) if m2 == 2 else {0, m + d5}
                if m2 >= 3:
                    numerator = m + d5 - k5p
                    if numerator % 3 == 0:
                        Js.add(numerator // 3)
                    Js.update(range(F5 + 1, d5 - c5p + 1))
                for J in sorted(Js):
                    if J < 0:
                        continue
                    if not ((F5, J) == (0, 0) or J > F5):
                        continue
                    for C in Cs:
                        b = 2**g * 5**J * int(C)
                        if not (U // 2 < b < U):
                            continue
                        if B == 2 and 6 * b <= 5 * U:
                            continue
                        beta = Q * U + b
                        if g > 0:
                            E = max(e, f, g)
                            if [e, f, g].count(E) != 1:
                                continue
                            if E >= 2 and [e, f, g].count(E - 1) % 2:
                                continue
                            if vp(beta, 2) != E:
                                continue
                        if J > F5 and vp(beta, 5) != J:
                            continue
                        if lcm(B, b, B * T * U + b) % M:
                            continue
                        counts[0] += 1
                        W = U * (U * D - 2 * Q * b * S)
                        if W < 0:
                            continue
                        counts[1] += 1
                        w = isqrt(W)
                        q = lcm(B, M, b)
                        y1 = q * A // B
                        y2 = q * N // M
                        z2 = beta * beta * (q // b) ** 2 - q * q
                        z1 = -2 * q * q * C0 * U
                        z0 = beta * beta * (y1 * y1 + y2 * y2) - (q * C0 * U) ** 2
                        delta = z1 * z1 - 4 * z2 * z0
                        scale = (B * M * b // q) ** 2
                        assert delta * scale**2 == 4 * (B * M * beta * b) ** 2 * W
                        assert delta >= 0 and (isqrt(delta) ** 2 == delta) == (
                            w * w == W
                        )
                        if w * w != W:
                            continue
                        c2 = D0 * (beta * beta - b * b)
                        c1 = -2 * C0 * U * b * b * D0
                        root = 2 * B * M * beta * b * w
                        roots = {F(-c1 + s * root, 2 * c2) for s in (-1, 1)}
                        squares.append((A, B, N, M, m, b, sorted(roots)))
                        for a in roots:
                            if (
                                a.denominator == 1
                                and U <= a < 2 * b
                                and gcd(a.numerator, b) == 1
                                and (B == 1 or 5 * a < 6 * b)
                            ):
                                hits.append((A, B, N, M, m, b, a))
    assert (
        counts == {2: [12025, 12025], 3: [55508, 55508], 4: [7448321, 7448321]}[m2]
        and not squares
        and not hits
    )
    print(
        f"PASS: m2={m2} all tail lengths; prefixes={len(prefixes)},max_m3={max(r[4] for r in prefixes)},tail quadratics={counts[0]},legal=0"
    )


if __name__ == "__main__":
    main()
