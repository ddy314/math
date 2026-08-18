#!/usr/bin/env python3
"""Exact certificate for spontaneous-bad-primes.md.

Uses only Python's standard library. It checks the two octic discriminants,
the listed repeated roots/orbit gates, the original three-equation solutions,
and the singular first-order Hensel compatibility at the exceptional primes.
It is not a global A2 solver.
"""

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


def eval_high(c, z):
    out = 0
    for a in c:
        out = out * z + a
    return out


def derivative_high(c):
    n = len(c) - 1
    return [c[i] * (n - i) for i in range(n)]


def bareiss_det(mat):
    a = [row[:] for row in mat]
    n = len(a)
    if not n:
        return 1
    prev = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            q = next((i for i in range(k + 1, n) if a[i][k]), None)
            if q is None:
                return 0
            a[k], a[q] = a[q], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def resultant_high(f, g):
    m, n = len(f) - 1, len(g) - 1
    rows = []
    for i in range(n):
        rows.append([0] * i + f + [0] * (n - 1 - i))
    for i in range(m):
        rows.append([0] * i + g + [0] * (m - 1 - i))
    return bareiss_det(rows)


def discriminant(c):
    n = len(c) - 1
    res = resultant_high(c, derivative_high(c))
    sign = -1 if (n * (n - 1) // 2) & 1 else 1
    return sign * res // c[0]


def factor_product(items):
    out = 1
    for p, e in items:
        out *= p**e
    return out


def check_discriminants():
    f1 = [
        (2, 88), (3, 75), (5, 38), (7, 12), (11, 28), (13, 4),
        (23, 4), (89, 2), (101, 4), (181, 2), (367, 2),
        (102251, 1), (630451, 1), (136776907, 1),
        (74218718085901254661, 2),
    ]
    f2 = [
        (2, 88), (3, 101), (5, 38), (7, 24), (11, 28), (13, 4),
        (19, 6), (67, 2), (101, 4), (281, 2), (8971, 1),
        (5019481, 2), (3833513, 2),
        (833453052690874208617, 1),
        (115850970866446584757213999, 2),
    ]
    assert discriminant(P1) == factor_product(f1)
    assert discriminant(P2) == factor_product(f2)


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def repeated(poly, p, s):
    return eval_high(poly, s) % p == 0 and eval_high(derivative_high(poly), s) % p == 0


def check_repeated_root_gates():
    assert all(not repeated(P1, 23, s) for s in range(23))
    assert [s for s in range(367) if repeated(P1, 367, s)] == [0]
    assert repeated(P1, 102251, 81690)
    assert repeated(P1, 630451, 271429)
    assert repeated(P1, 136776907, 8516046)

    p = 136776907
    order10 = 7598717
    target = 8516046 * pow(36, -1, p) % p
    assert pow(10, order10, p) == 1
    assert pow(target, order10, p) != 1

    assert repeated(P2, 19, 16)
    assert repeated(P2, 67, 17)
    assert repeated(P2, 8971, 6356)

    assert legendre(55, 7) == -1
    assert legendre(55, 115850970866446584757213999) == -1


def nsp(s, x):
    y = 11 - 9 * s
    return (x + 2) ** 2 * (2025 * s * s * x * x + y * y) + 10780 * x * x


def osp(s, x, r):
    y = 11 - 9 * s
    return (
        r * (4 * (225 * s * x * x + 9 * s - 11) ** 2 - x * y * y * (99 * x - 4))
        + 2 * x * y * y * (x + 2)
    )


def gsp(x, r):
    return 55 * r * r * (x + 2) ** 2 - 49 * x * x


def jacobian(s, x, r):
    y = 11 - 9 * s
    dN_ds = 2 * (x + 2) ** 2 * (2025 * s * x * x - 9 * y)
    dN_dx = (
        2 * (x + 2) * (2025 * s * s * x * x + y * y)
        + (x + 2) ** 2 * 4050 * s * s * x
        + 21560 * x
    )

    term = 225 * s * x * x + 9 * s - 11
    A = 4 * term * term - x * y * y * (99 * x - 4)
    dA_ds = 8 * term * (225 * x * x + 9) + 18 * x * y * (99 * x - 4)
    dA_dx = 8 * term * 450 * s * x - y * y * (198 * x - 4)
    dO_ds = r * dA_ds - 36 * x * y * (x + 2)
    dO_dx = r * dA_dx + 2 * y * y * (2 * x + 2)
    dO_dr = A

    dG_dx = 110 * r * r * (x + 2) - 98 * x
    dG_dr = 110 * r * (x + 2) ** 2

    return [
        [dN_ds, dN_dx, 0],
        [dO_ds, dO_dx, dO_dr],
        [0, dG_dx, dG_dr],
    ]


def det3(a, p):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    ) % p


def linear_compatible(A, b, p):
    aug = [[v % p for v in row] + [b[i] % p] for i, row in enumerate(A)]
    m, n = len(aug), len(A[0])
    row = 0
    for col in range(n):
        q = next((i for i in range(row, m) if aug[i][col] % p), None)
        if q is None:
            continue
        aug[row], aug[q] = aug[q], aug[row]
        inv = pow(aug[row][col], -1, p)
        aug[row] = [(z * inv) % p for z in aug[row]]
        for i in range(m):
            if i != row and aug[i][col] % p:
                f = aug[i][col] % p
                aug[i] = [(aug[i][j] - f * aug[row][j]) % p for j in range(n + 1)]
        row += 1
    return not any(
        all(aug[i][j] % p == 0 for j in range(n)) and aug[i][n] % p
        for i in range(row, m)
    )


def check_solution_and_lift(p, s, x, r, expect_lift):
    vals = [nsp(s, x), osp(s, x, r), gsp(x, r)]
    assert all(v % p == 0 for v in vals)
    J = jacobian(s, x, r)
    det = det3(J, p)
    if det:
        assert expect_lift
        return det
    b = [(-v // p) % p for v in vals]
    ok = linear_compatible(J, b, p)
    assert ok == expect_lift
    return 0


def check_full_system_bad_primes():
    assert check_solution_and_lift(102251, 81690, 61220, 84227, False) == 0
    assert check_solution_and_lift(630451, 271429, 340435, 204669, False) == 0

    assert nsp(16, 0) % 19 == 0

    d1 = check_solution_and_lift(67, 17, 53, 63, True)
    d2 = check_solution_and_lift(67, 17, 37, 57, True)
    assert (d1, d2) == (32, 49)
    assert pow(10, 32, 67) * 36 % 67 == 17

    assert check_solution_and_lift(8971, 6356, 2914, 7633, False) == 0


def main():
    check_discriminants()
    check_repeated_root_gates()
    check_full_system_bad_primes()
    print("A2 spontaneous bad-prime certificate: OK")


if __name__ == "__main__":
    main()
