#!/usr/bin/env python3
"""Exact arithmetic checks for source-length-resultant.md."""

from math import isqrt

R_COEFF = (-480029, 40568, 4496, 7040, 3520)
L_COEFF = (
    19964008847990601,
    26176176015770484,
    -6142888878869754,
    -12826705293056556,
    3373694017753081,
)


def bareiss_det(a):
    a = [row[:] for row in a]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
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
        for j in range(k + 1, n):
            a[k][j] = 0
    return sign * a[-1][-1]


def resultant_desc(f, g):
    m = len(f) - 1
    n = len(g) - 1
    size = m + n
    mat = []
    for i in range(n):
        mat.append([0] * i + list(f) + [0] * (size - i - len(f)))
    for i in range(m):
        mat.append([0] * i + list(g) + [0] * (size - i - len(g)))
    return bareiss_det(mat)


def eval_desc(c, x):
    y = 0
    for a in c:
        y = y * x + a
    return y


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    x = pow(a, (p - 1) // 2, p)
    return 1 if x == 1 else -1


def is_prime_trial(n):
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return False
    return True


def check_length_resultant() -> None:
    # G_s(x)=225*s*x^2 + (9*s-11).  The resultant has degree <=4 in s;
    # checking more than five integer s values certifies the displayed quartic.
    for s in (-7, -3, 1, 2, 5, 8, 11, 17):
        g = (225 * s, 0, 9 * s - 11)
        got = resultant_desc(R_COEFF, g)
        want = eval_desc(L_COEFF, s)
        assert got == want, (s, got, want)


def check_discriminant_factorization() -> None:
    # Exact discriminant value obtained as resultant(f,f')/leading coefficient.
    # The factor product is the audit target relevant to bad primes.
    factor_product = -(
        2**48
        * 3**29
        * 5**28
        * 7**6
        * 11**18
        * 19**2
        * 101**4
        * 748057
        * 45503**2
    )
    # Compute discriminant directly with the same Sylvester/Bareiss machinery.
    a, b, c, d, e = L_COEFF
    deriv = (4 * a, 3 * b, 2 * c, d)
    res = resultant_desc(L_COEFF, deriv)
    disc = res // a  # sign is + for degree 4
    assert disc == factor_product
    assert is_prime_trial(748057)
    assert is_prime_trial(45503)
    assert 748057 % 4 == 1
    assert 45503 % 4 == 3


def check_45503_gate() -> None:
    assert legendre(55, 45503) == -1


def check_mod19_reduction_and_lengths() -> None:
    p = 19
    for s in range(p):
        lhs = eval_desc(L_COEFF, s) % p
        rhs = ((s - 2) * (s - 8)) % p
        assert lhs == rhs

    # actual roots are simple
    roots = [s for s in range(p) if eval_desc(L_COEFF, s) % p == 0]
    assert roots == [2, 8]

    # ord_19(10)=18 and the two length classes are n=M-1 = 7,9 mod 18.
    seen = []
    v = 1
    for n in range(1, 19):
        v = (v * 10) % p
        seen.append(v)
    assert v == 1 and len(set(seen)) == 18
    hits = []
    for n in range(18):
        s = (36 * pow(10, n, p)) % p
        if s in (2, 8):
            hits.append((n, s))
    assert hits == [(7, 8), (9, 2)]


def check_mod19_source_roots() -> None:
    p = 19
    pairs = []
    for s in (2, 8):
        for x in range(p):
            if eval_desc(R_COEFF, x) % p == 0 and (225 * s * x * x + 9 * s - 11) % p == 0:
                A = (99 * x - 4) % p
                B = (2 * x + 4) % p
                r = B * pow(A, -1, p) % p
                zu = r * (x + 2) * pow(x, -1, p) % p
                pairs.append((s, x, zu))
    assert pairs == [(2, 13, 2), (8, 15, 2)]


def main() -> None:
    check_length_resultant()
    check_discriminant_factorization()
    check_45503_gate()
    check_mod19_reduction_and_lengths()
    check_mod19_source_roots()
    print("A2 source-length resultant certificate: OK")


if __name__ == "__main__":
    main()
