#!/usr/bin/env python3
"""Exact checks for spontaneous-angle.md and length-orbit.md.

The script uses only Python's standard library. It certifies the fixed
algebraic identities/resultant factorization by exact integer/rational
arithmetic and checks the explicitly listed 19-adic branches. It is not a
global A2 solver.
"""

from fractions import Fraction


def phi(x, r):
    return (99 * x - 4) * r - 2 * x - 4


def delta0(x, y):
    return 2025 * x * x - 18 * y - y * y


def omega(x, y, r):
    d = 225 * x * x - y
    return 4 * r * d * d - x * y * y * phi(x, r)


def a_sp(x, y):
    d = 225 * x * x - y
    return 4 * d * d - x * y * y * (99 * x - 4)


def check_spontaneous_identities():
    samples = [
        (Fraction(1, 9), Fraction(997, 1000), Fraction(17, 5)),
        (Fraction(2, 19), Fraction(999, 1000), Fraction(41, 7)),
        (Fraction(13, 125), Fraction(249, 250), Fraction(101, 11)),
    ]
    for x, y, r in samples:
        den = (x + 2) * (r * (x + 2) + 2 * x)
        lhs = (
            4 * r * (225 * x * x - y) ** 2 / (y * y * den)
            - x * phi(x, r) / den
        )
        rhs = omega(x, y, r) / (y * y * den)
        assert lhs == rhs

        a1 = 99 * x - 4
        b1 = -2 * x - 4
        a2 = a_sp(x, y)
        b2 = 2 * x * y * y * (x + 2)
        res_source = a1 * b2 - a2 * b1
        assert res_source == 8 * (x + 2) * (225 * x * x - y) ** 2

        af = x + 2
        bf = 2 * x
        res_f = af * b2 - a2 * bf
        assert res_f == -200 * x**3 * delta0(x, y)

        assert omega(Fraction(-2), y, r) == 400 * r * delta0(Fraction(-2), y)

        res_gamma = 55 * b2 * b2 * (x + 2) ** 2 - 49 * x * x * a2 * a2
        target = x * x * (220 * y**4 * (x + 2) ** 4 - 49 * a2 * a2)
        assert res_gamma == target

    lower = Fraction(25, 4) - Fraction(244, 361)
    assert lower == Fraction(8049, 1444)
    assert lower > 5


def check_theta_scaling():
    samples = [
        (11, 5, 1, 3, 4, 7, 11, 13, 17, 19, 23),
        (4, 6, 2, 5, 8, 3, 7, 11, 13, 17, 29),
    ]
    for M, m, d, cu, g, cQ, q, X, Y, K, a3 in samples:
        lam = m - d
        assert lam >= 2 * d
        b2 = 2 ** (M + m + 1) * cu * g
        Q = 2 ** (M + 1) * cQ * q
        N0 = 5 ** (lam - 2 * d) * X * Y
        T = 10**m
        S0 = T * (K * K - 26) - (2 * K - 9) * (2 * a3 + 9 * T)
        that = (
            2**m * cu * cu * g * g * S0
            - (cQ * q) ** 2 * 5 ** (2 * lam - d) * X * Y
        )
        theta = b2 * b2 * S0 - T * Q * Q * N0
        assert theta == 2 ** (2 * M + m + 2) * that

        psi_f = b2 * b2 * (K * K - 26) - Q * Q * N0
        assert theta == T * psi_f - b2 * b2 * (2 * K - 9) * (2 * a3 + 9 * T)

        Fw = 5 * K * K - 36 * K + 55
        phi_h = b2 * b2 * Fw - Q * Q * N0
        alpha = T * K + a3
        assert theta == T * phi_h - 2 * b2 * b2 * (2 * K - 9) * alpha


def padd(a, b):
    n = max(len(a), len(b))
    c = [0] * n
    for i in range(n):
        c[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c


def pscale(a, k):
    return [k * v for v in a]


def pmul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c


def ppow(a, n):
    out = [1]
    base = a[:]
    while n:
        if n & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        n //= 2
    return out


def bareiss_det(mat):
    a = [row[:] for row in mat]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def resultant_int(f, g):
    """Resultant of integer polynomials stored low-degree first."""
    m = len(f) - 1
    n = len(g) - 1
    fh = list(reversed(f))
    gh = list(reversed(g))
    matrix = []
    for i in range(n):
        matrix.append([0] * i + fh + [0] * (n - 1 - i))
    for i in range(m):
        matrix.append([0] * i + gh + [0] * (m - 1 - i))
    return bareiss_det(matrix)


P1 = [
    1382549089196025,
    -133844136247800,
    3690923035544910,
    7960772236243860,
    3163200960625101,
    10662174653755284,
    13341353191482096,
    -1874385042496296,
    62480266566916,
]

P2 = [
    363844061254628703225,
    989345243267031420000,
    1615741998157561468590,
    1886040813505705898580,
    1569626813501484989229,
    956049258626593813836,
    390256979886873318384,
    44160413329248524616,
    1475531078426217604,
]


def peval_high(coeffs, z):
    out = 0
    for c in coeffs:
        out = out * z + c
    return out


def coupled_polynomials_at_s(s):
    ys = 11 - 9 * s
    xp2 = [2, 1]
    x2 = [0, 0, 1]

    term = padd(pscale(x2, 225 * s), [9 * s - 11])
    asp = padd(pscale(pmul(term, term), 4), pscale([0, -4, 99], -ys * ys))
    rspd = padd(pscale(ppow(xp2, 4), 220 * ys**4), pscale(pmul(asp, asp), -49))

    inside = padd(pscale(x2, 2025 * s * s), [ys * ys])
    nsp_poly = padd(pmul(ppow(xp2, 2), inside), pscale(x2, 10780))
    return nsp_poly, rspd


def check_octic_resultant():
    C = 1205534785939344000000000000
    for s in range(1, 38):
        nsp_poly, rspd = coupled_polynomials_at_s(s)
        res = resultant_int(nsp_poly, rspd)
        predicted = (
            C
            * s**8
            * (9 * s - 11) ** 8
            * peval_high(P1, s)
            * peval_high(P2, s)
        )
        assert res == predicted

    for s in range(19):
        p1 = peval_high(P1, s) % 19
        rhs1 = (
            -2
            * (s - 9)
            * (s**3 - 4 * s**2 + 6 * s + 3)
            * (s**4 - 2 * s**3 + 2 * s**2 - 4 * s - 8)
        ) % 19
        assert p1 == rhs1

        p2 = peval_high(P2, s) % 19
        rhs2 = (
            -3
            * (s - 2)
            * (s + 3) ** 2
            * (s**3 + 3 * s**2 - 4 * s + 6)
        ) % 19
        assert p2 == rhs2


def nsp(s, x):
    ys = 11 - 9 * s
    return (x + 2) ** 2 * (2025 * s * s * x * x + ys * ys) + 10780 * x * x


def osp(s, x, r):
    ys = 11 - 9 * s
    return (
        r * (4 * (225 * s * x * x + 9 * s - 11) ** 2 - x * ys * ys * (99 * x - 4))
        + 2 * x * ys * ys * (x + 2)
    )


def gsp(x, r):
    return 55 * r * r * (x + 2) ** 2 - 49 * x * x


def jac_det_mod19(s, x, r):
    p = 19
    ys = 11 - 9 * s

    dN_ds = 2 * (x + 2) ** 2 * (2025 * s * x * x - 9 * ys)
    dN_dx = (
        2 * (x + 2) * (2025 * s * s * x * x + ys * ys)
        + (x + 2) ** 2 * 4050 * s * s * x
        + 21560 * x
    )
    dN_dr = 0

    term = 225 * s * x * x + 9 * s - 11
    A = 4 * term * term - x * ys * ys * (99 * x - 4)
    dA_ds = 8 * term * (225 * x * x + 9) + 18 * x * ys * (99 * x - 4)
    dA_dx = 8 * term * (450 * s * x) - ys * ys * (198 * x - 4)
    dO_ds = r * dA_ds - 36 * x * ys * (x + 2)
    dO_dx = r * dA_dx + 2 * ys * ys * (2 * x + 2)
    dO_dr = A

    dG_ds = 0
    dG_dx = 110 * r * r * (x + 2) - 98 * x
    dG_dr = 110 * r * (x + 2) ** 2

    a, b, c = dN_ds % p, dN_dx % p, dN_dr
    d, e, f = dO_ds % p, dO_dx % p, dO_dr % p
    g, h, i = dG_ds, dG_dx % p, dG_dr % p
    return (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)) % p


def check_19adic_branches():
    p = 19
    roots = [
        [(2, 11, 9), (2, 239, 199), (2890, 961, 2726), (50903, 48974, 16444)],
        [(9, 3, 14), (47, 3, 356), (47, 6140, 3966), (96073, 88448, 58838)],
    ]
    exponents = [
        [9, 81, 2817, 100287],
        [2, 200, 1226, 46712],
    ]

    assert jac_det_mod19(*roots[0][0]) == 1
    assert jac_det_mod19(*roots[1][0]) == 10

    s_a, x_a, r_a = roots[0][0]
    s_b, x_b, r_b = roots[1][0]
    zratio_a = r_a * (x_a + 2) * pow(x_a, -1, p) % p
    zratio_b = r_b * (x_b + 2) * pow(x_b, -1, p) % p
    assert zratio_a == 2
    assert (zratio_a + 2) % p != 0
    assert zratio_b == p - 2
    assert (zratio_b + 2) % p == 0

    for branch, ns in zip(roots, exponents):
        prev = None
        for k, ((s, x, r), n) in enumerate(zip(branch, ns), start=1):
            mod = p**k
            assert nsp(s, x) % mod == 0
            assert osp(s, x, r) % mod == 0
            assert gsp(x, r) % mod == 0
            if prev is not None:
                assert tuple(v % (p ** (k - 1)) for v in (s, x, r)) == prev
            prev = tuple(v % mod for v in (s, x, r))

            order = 18 * p ** (k - 1)
            assert 36 * pow(10, n, mod) % mod == s % mod
            assert pow(10, order, mod) == 1
            assert pow(10, order // 2, mod) != 1
            assert pow(10, order // 3, mod) != 1
            if k > 1:
                assert pow(10, order // 19, mod) != 1

    assert pow(10, 18, 19**2) == 1 + 15 * 19


def check_19_secant_deep():
    p = 19
    mod = p * p
    inv18 = pow(18, -1, mod)

    T = 1
    K = 55 * inv18 % mod
    a3 = -55 * inv18 % mod
    b2 = 1
    q2n0 = 3

    F2 = (
        4 * b2 * b2 * T * (T + a3) * (K - 2) ** 2
        - q2n0 * (2 * T + a3) ** 2
    )
    assert F2 % (p * p) == 0
    assert F2 % (p**3) != 0
    assert (F2 // (p * p)) % p == (-7 * pow(18, -2, p)) % p

    F3 = (
        b2 * b2 * T * 3 * (3 * T + 2 * a3) * (K - 3) ** 2
        - q2n0 * (3 * T + a3) ** 2
    )
    F4 = (
        b2 * b2 * T * 4 * (4 * T + 2 * a3) * (K - 4) ** 2
        - q2n0 * (4 * T + a3) ** 2
    )
    assert F3 % p == -6 % p
    assert F4 % p == -12 % p
    assert (F4 * pow(F3, -1, p)) % p == 2

    assert (2 * pow(2, -1, p)) % p == 1


def main():
    check_spontaneous_identities()
    check_theta_scaling()
    check_octic_resultant()
    check_19adic_branches()
    check_19_secant_deep()
    print("A2 spontaneous-angle/length-orbit certificate: OK")


if __name__ == "__main__":
    main()
