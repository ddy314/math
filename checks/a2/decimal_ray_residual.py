"""A2-G15/F09: unbounded norm obstruction and the full E=3..12 certificate.

Exact symbolic identities carry the unbounded reduction in PROOF.md.
The E=3 readers use independently chosen variables and coefficient systems.
Python integers and Fraction have no fixed width. E>=13 remains open;
an exact sum-of-two-squares witness at E=13 guards that boundary.
"""

from fractions import Fraction as F
from math import isqrt

import sympy as sp

PERIODS = (
    (19, 9, 6, 171, 96),
    (71, 35, 9, 2485, 1549),
    (79, 13, 9, 1027, 815),
    (139, 23, 5, 3197, 189),
)
ODD_FACTORS = {
    4: 1811,
    5: 139,
    6: 19,
    7: 25391,
    8: 3823,
    9: 71,
    10: 361617239,
    11: 7757594443,
    12: 431,
}


def trial_prime(n):
    """Complete trial division, not a probable-prime oracle."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def symbolic_certificate():
    z, N, a, k = sp.symbols("z N a k")
    T, M, U, b = 10 * z**2, sp.Rational(12, 5) * z**2, z**3, sp.Rational(4, 5) * z**3
    q, H = 3 * b, 3 * a + z**2 * k / 2
    alpha, beta = (2 * T + 10 * N) * U + a, (T + M) * U + b
    word = (1 + 31 * z**2 / 2) * k - 120 * z**3 - 60 * N * z + 93 * a
    sphere = k * (3 * a + z**2 * k / 4) - sp.Rational(576, 25) * z**4 - N**2
    P = (
        31 * N**2
        - 60 * z * N * k
        + (1 + 31 * z**2 / 4) * k**2
        - 120 * z**3 * k
        + sp.Rational(17856, 25) * z**4
    )
    assert sp.expand(beta * H - q * alpha - b * z**2 * word / 2) == 0
    assert (
        sp.expand(H**2 - (2 * q) ** 2 - (q * N / M) ** 2 - (3 * a) ** 2 - z**2 * sphere)
        == 0
    )
    assert sp.expand(P + 31 * sphere - k * word) == 0
    delta, S = 2639 * z**2 - 124, 816 * z**2 - 31
    X, Y, V = 31 * N - 30 * z * k, delta * k + 7440 * z**3, sp.Rational(2976, 5) * z**2
    assert sp.expand(Y**2 - 4 * delta * X**2 - V**2 * S + 124 * delta * P) == 0
    assert (
        sp.expand(
            Y**2 + (50 * z * X) ** 2 - S * (V**2 + (4 * X) ** 2) + 124 * delta * P
        )
        == 0
    )
    # Validate the rational norm quotient without relying on complex arithmetic.
    numerator_real = Y * V + 200 * z * X**2
    numerator_imag = 50 * z * X * V - 4 * X * Y
    norm_denom = V**2 + 16 * X**2
    assert (
        sp.expand(
            numerator_real**2
            + numerator_imag**2
            - (Y**2 + 2500 * z**2 * X**2) * norm_denom
        )
        == 0
    )

    # Reader 1 discriminant in N.
    coeffs = sp.Poly(P, N).all_coeffs()
    disc_k = delta * k**2 + 14880 * z**3 * k - sp.Rational(2214144, 25) * z**4
    assert sp.expand(coeffs[1] ** 2 - 4 * coeffs[0] * coeffs[2] - disc_k) == 0
    # Reader 2: direct original equation, independently expanded in a.
    C0 = 2 * T + 10 * N
    AA = M**2 * (beta**2 - b**2)
    BB = -2 * M**2 * b**2 * C0 * U
    CC = beta**2 * b**2 * (4 * M**2 + N**2) - M**2 * b**2 * C0**2 * U**2
    original = (
        beta**2 * (4 * M**2 * b**2 + N**2 * b**2 + a**2 * M**2) - M**2 * b**2 * alpha**2
    )
    assert sp.expand(original - (AA * a**2 + BB * a + CC)) == 0
    print("Exact original recovery, conic, norm identity, and both discriminants: PASS")


def window_certificate():
    s = sp.symbols("s")
    cap = sp.Rational(625, 961) * (2 + s) ** 2 - 4 - sp.Rational(25, 144) * s**2
    assert (
        sp.expand(
            sp.diff(cap, s) - sp.Rational(2500, 961) - sp.Rational(65975, 69192) * s
        )
        == 0
    )
    low = F(625, 961) * (2 + F(24, 25)) ** 2 - 4 - F(25, 144) * F(24, 25) ** 2
    assert low == F(36956, 24025) and low < F(25, 16)
    high = F(16, 25) * (F(625 * 9, 961) - 4 - F(25, 144))
    assert high == F(232439, 216225) and high < F(441, 400)
    lower_k = 5 * (3 * F(21, 20) + F(5, 4))
    assert lower_k == 22 and lower_k < F(576, 25)
    assert 120 + 60 - 93 == 87 and F(87 * 2, 31) == F(174, 31)
    z = 1000
    assert 5 * z + 1 == 5001 and (174 * z - 1) // 31 == 5612
    assert 24 * z * z // 25 + 1 == 960001 and z * z - 1 == 999999
    print("Full recovery windows: 24*z^2/25<N<z^2 and 5*z<k<174*z/31")


def periodic_obstructions():
    for p, order, root, order2, root2 in PERIODS:
        assert trial_prime(p) and p % 4 == 3
        for modulus, period, residue in ((p, order, root), (p * p, order2, root2)):
            # Exact order and one root establish the entire exponent class.
            assert pow(100, period, modulus) == 1
            assert all(
                pow(100, period // ell, modulus) != 1 for ell in prime_factors(period)
            )
            assert (816 * pow(100, residue, modulus) - 31) % modulus == 0
            # Independent full-period reader uses multiplication only.
            current, found = 1, []
            for E in range(period):
                if (816 * current - 31) % modulus == 0:
                    found.append(E)
                current = current * 100 % modulus
            assert current == 1 and found == [residue]
        assert order2 == p * order and root2 % order == root
    print("Four complete exponent-class obstructions; no bound on E")


def finite_odd_factors():
    for E, p in ODD_FACTORS.items():
        assert trial_prime(p) and p % 4 == 3
        residue = (816 * pow(100, E, p * p) - 31) % (p * p)
        assert residue % p == 0 and residue != 0
        # Independently divide the whole integer; no cofactor factorization needed.
        S = 816 * 100**E - 31
        assert S % p == 0 and (S // p) % p != 0
    assert set(ODD_FACTORS) == set(range(4, 13))
    print("All E=4..12 excluded by nine trial-proved primes of exact odd depth 1")


def finite_E3():
    z = 1000
    gap_rows = 0
    for k in range(5 * z + 1, (174 * z - 1) // 31 + 1):
        disc = (2639 * z * z - 124) * k * k + 14880 * z**3 * k - 2214144 * (z**4 // 25)
        assert disc >= 0 and isqrt(disc) ** 2 != disc
        gap_rows += 1
    assert gap_rows == 612

    T, M, U, b = 10 * z * z, 12 * z * z // 5, z**3, 4 * z**3 // 5
    beta = (T + M) * U + b
    AA = M * M * (beta * beta - b * b)
    numerator_rows = 0
    for N in range(24 * z * z // 25 + 1, z * z):
        C0 = 2 * T + 10 * N
        BB = -2 * M * M * b * b * C0 * U
        CC = beta * beta * b * b * (4 * M * M + N * N) - M * M * b * b * C0 * C0 * U * U
        disc = BB * BB - 4 * AA * CC
        assert disc < 0 or isqrt(disc) ** 2 != disc
        numerator_rows += 1
    assert numerator_rows == 39999
    print(
        f"E=3: {gap_rows} gap rows and {numerator_rows} independent original-numerator rows; zero squares"
    )


def boundary_witnesses():
    assert 816 * 100**3 - 31 == 7712**2 + 27505**2
    assert 816 * 100**13 - 31 == 83674539967313**2 + 273127390353400**2
    # These exact identities are allowed norm projections, not original solutions.
    print(
        "Boundary: E=3 and E=13 pass the norm condition; only E=3 is fully excluded here"
    )


def main():
    symbolic_certificate()
    window_certificate()
    periodic_obstructions()
    finite_odd_factors()
    finite_E3()
    boundary_witnesses()
    print(
        "PASS: A2-G15 necessary conditions and A2-F09 full E=3..12 certificate; E>=13 open"
    )


if __name__ == "__main__":
    main()
