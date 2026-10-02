"""Audit A2-G01/G02/G03/G06/G07/G09/G10 and A2-F01 identities and constants.

The unbounded argument is in PROOF.md. No search cutoff is asserted here.
New derivation, independent of the archived first-block compression summary.
"""

from fractions import Fraction

import sympy as sp


def main():
    a, b, x, y, z = sp.symbols("a b x y z", positive=True)
    f = (a + y) ** 2 / (b + x) ** 2 - a**2 / b**2 - y**2 / (100 * x**2)
    fb = 1 / (x * (2 * b + x)) - 1 / (100 * x**2)
    center = b**2 * y / (x * (2 * b + x))
    coefficient = x * (2 * b + x) / (b**2 * (b + x) ** 2)
    assert sp.factor(f + coefficient * (a - center) ** 2 - y**2 * fb) == 0
    assert (
        sp.factor(
            sp.diff(fb, x)
            + (-4 * b**2 + 96 * b * x + 99 * x**2) / (50 * x**3 * (2 * b + x) ** 2)
        )
        == 0
    )

    for denominator, cap in ((1, Fraction(79, 21)), (2, Fraction(59, 41))):
        assert fb.subs({b: denominator, x: sp.Rational(1, 10)}) == cap
        assert (
            -4 * denominator**2 + Fraction(96 * denominator, 10) + Fraction(99, 100) > 0
        )
    at_y1 = f.subs(y, 1)
    assert (
        sp.factor(sp.diff(at_y1, x) + 2 * (a + 1) ** 2 / (b + x) ** 3 - 1 / (50 * x**3))
        == 0
    )
    for numerator, cap in (
        (4, Fraction(443, 121)),
        (6, Fraction(423, 121)),
        (8, Fraction(235, 121)),
    ):
        assert at_y1.subs({a: numerator, b: 1, x: sp.Rational(1, 10)}) == cap
    for denominator, numerators in ((1, range(1, 9)), (2, (5, 7, 9, 11, 13))):
        assert all(
            100 * (numerator + 1) > (10 * denominator + 1) ** 2
            for numerator in numerators
        )
    assert Fraction(2081, 1000) ** 3 > 9
    assert Fraction(215, 1000) ** 3 < Fraction(1, 100)
    assert Fraction(933, 500) ** 3 < Fraction(13, 2)
    assert Fraction(28, 3) ** 3 < 900
    assert Fraction(1588, 1000) ** 3 > 4
    assert Fraction(1373, 1000) ** 3 < Fraction(13, 5)
    assert Fraction(3302, 1000) ** 3 > 36
    assert Fraction(3087, 1000) ** 3 < Fraction(59, 2)
    assert Fraction(757, 200) ** 3 < Fraction(163, 3)

    # Both positive quadratics used to exclude a1=3 have negative discriminant.
    q1 = sp.Rational(13, 4) + z**2 - (sp.Rational(7, 4) + z / 5) ** 2
    q2 = 40 * z * (2 * z / 5 + sp.Rational(7, 40) / z - sp.Rational(1, 2))
    assert sp.factor(q1 - (384 * z**2 - 280 * z + 75) / 400) == 0
    assert sp.factor(q2 - (16 * z**2 - 20 * z + 7)) == 0
    for polynomial in (q1, sp.expand(q2)):
        assert sp.Poly(polynomial, z).LC() > 0
        assert sp.discriminant(polynomial, z) < 0
    assert sp.Rational(7, 2) + sp.Rational(1, 50) + sp.Rational(1, 2) > 4

    # Upper numerator thresholds: positivity at the endpoint and thereafter.
    for denominator, threshold, polynomial in (
        (1, 9, 21 * a**2 - 200 * a + 142),
        (2, 15, 41 * a**2 - 800 * a + 3128),
    ):
        raw = (sp.Rational(10 * denominator + 1, 10)) ** 2 * (
            a**2 / denominator**2 + 2
        ) - (a + 1) ** 2
        scale = 100 if denominator == 1 else 400
        assert sp.factor(scale * raw - polynomial) == 0
        assert polynomial.subs(a, threshold) > 0
        assert sp.diff(polynomial, a).subs(a, threshold) > 0
        assert threshold**2 / denominator**2 + 1 >= 10 * denominator

    # Mod four is complete at this local projection; it is not an original search.
    for h in range(4):
        for tail in range(4):
            if h % 2 != tail % 2:
                continue
            for first in range(4):
                for second in range(4):
                    if (h * h - tail * tail - first * first - second * second) % 4 == 0:
                        assert first % 2 == second % 2 == 0
    for valuation in (1, 2, 3):
        for other in range(1, 7):
            first = 2**valuation
            second = 3 * 2**other
            total = first * first + second * second
            actual = (total & -total).bit_length() - 1
            predicted = 2 * min(valuation, other) + (valuation == other)
            assert actual == predicted <= 2 * valuation + 1

    # Exact affine denominator and recovery quadratic, not a new free root.
    t, tail_power, tail_den, tail_num, c, k, second_num = sp.symbols(
        "T U d e c k n", positive=True
    )
    second_den = c * (tail_power * t + tail_den) / k
    lam = k + c * tail_power
    beta = (t + second_den) * tail_power + tail_den
    alpha = a * t * tail_power + 10 * second_num * tail_power + tail_num
    assert sp.factor(beta - second_den * lam / c) == 0
    recovered = (
        a * k * second_den
        + 10 * c * tail_power * second_num
        + c * (tail_num - a * tail_den)
    )
    assert sp.factor(recovered - c * alpha) == 0
    quadratic = (
        lam**2 * ((a**2 + tail_num**2 / tail_den**2) * second_den**2 + second_num**2)
        - recovered**2
    )
    original = (
        beta**2 * (a**2 + second_num**2 / second_den**2 + tail_num**2 / tail_den**2)
        - alpha**2
    )
    assert sp.factor(quadratic - c**2 * original) == 0
    # The original odd denominators force k odd; lambda is odd and u is even.
    for odd_c in (1, 3, 5):
        for odd_k in (1, 3, 9, 11):
            for exponent in range(1, 7):
                odd_lam = odd_k + odd_c * 10**exponent
                even_u = 10 * odd_c * 10**exponent
                assert (odd_lam**2 - even_u**2) % 2 == 1
    # G03: the quadratic discriminant is nonzero on every original tag.
    moving_den = sp.symbols("B", positive=True)
    offset = c * (tail_num - a * tail_den)
    sphere = a**2 + tail_num**2 / tail_den**2
    u = 10 * c * tail_power
    h = lam**2 - u**2
    recovered_at_b = a * k * moving_den + u * second_num + offset
    f_at_b = lam**2 * (sphere * moving_den**2 + second_num**2) - recovered_at_b**2
    assert (
        sp.factor(
            f_at_b.subs(moving_den, 0).subs(tail_num, a * tail_den) - h * second_num**2
        )
        == 0
    )
    p_at_b = (a * k * moving_den + offset) ** 2 - h * sphere * moving_den**2
    assert sp.factor(sp.discriminant(f_at_b, second_num) - 4 * lam**2 * p_at_b) == 0
    assert (
        sp.factor(sp.discriminant(p_at_b, moving_den) - 4 * h * sphere * offset**2) == 0
    )
    affine = p_at_b.subs(moving_den, second_den)
    assert (
        sp.factor(
            sp.discriminant(affine, t)
            - (c * tail_power / k) ** 2 * 4 * h * sphere * offset**2
        )
        == 0
    )
    integer_square = (
        k**2 * tail_den**2 * (a * tail_power * t + tail_num) ** 2
        - h * (a**2 * tail_den**2 + tail_num**2) * (tail_power * t + tail_den) ** 2
    )
    assert sp.factor((k * tail_den / c) ** 2 * affine - integer_square) == 0
    # G09: arbitrary first denominator B=1,2, without odd-tail parity.
    first_den = sp.symbols("B0", positive=True)
    M = c * (first_den * tail_power * t + tail_den) / k
    j = c * (first_den * tail_num - a * tail_den)
    C = a**2 + first_den**2 * tail_num**2 / tail_den**2
    rhs = a * k * M + u * first_den * second_num + j
    general_alpha = a * t * tail_power + 10 * second_num * tail_power + tail_num
    general_beta = (first_den * t + M) * tail_power + tail_den
    assert sp.factor(rhs - c * first_den * general_alpha) == 0
    assert sp.factor(general_beta - M * lam / c) == 0
    recovery = lam**2 * (C * M**2 + first_den**2 * second_num**2) - rhs**2
    original_general = (
        general_beta**2
        * (a**2 / first_den**2 + second_num**2 / M**2 + tail_num**2 / tail_den**2)
        - general_alpha**2
    )
    assert sp.factor(recovery - c**2 * first_den**2 * original_general) == 0
    P = (a * k * moving_den + j) ** 2 - h * C * moving_den**2
    assert sp.factor(sp.discriminant(P, moving_den) - 4 * h * C * j**2) == 0
    assert (
        sp.factor(a * k * M + j - c * first_den * (a * tail_power * t + tail_num)) == 0
    )
    assert (
        sp.factor(
            j * (2 * a * c * tail_den + j)
            - c**2 * ((first_den * tail_num) ** 2 - (a * tail_den) ** 2)
        )
        == 0
    )
    assert sp.factor((general_beta - M * lam / c).subs(k, 9 * c * tail_power)) == 0
    # h=0 would require 9*U*M=B*T*U+b, impossible for 0<b<U.
    assert (
        sp.factor(
            9 * tail_power * M.subs(k, 9 * c * tail_power)
            - first_den * t * tail_power
            - tail_den
        )
        == 0
    )
    linear_slope, constant, X = sp.symbols("ell constant X", positive=True)
    for parity in (0, 1):
        polynomial = linear_slope * 10**parity * X**2 + constant
        assert (
            sp.discriminant(polynomial, X) == -4 * linear_slope * 10**parity * constant
        )
    p2, p1, p0 = sp.symbols("p2 p1 p0", positive=True)
    approximation = sp.sqrt(p2) * t + p1 / (2 * sp.sqrt(p2))
    assert sp.expand(p2 * t**2 + p1 * t + p0 - approximation**2) == p0 - p1**2 / (
        4 * p2
    )
    # The route's unit-first example passes geometry but is not an Exact Lift.
    ratios = (Fraction(4), Fraction(8, 11), Fraction(10, 9))
    radius_squared = sum(r * r for r in ratios)
    prefix = Fraction(4 * 100 + 10 * 8, 100 + 11)
    word = Fraction(4810, 1119)
    assert prefix * prefix > radius_squared
    assert word * word != radius_squared
    # The table records t>=3/4 as rays. This finite grid is a regression;
    # the formula in PROOF.md covers arbitrary numerator valuations.
    for valuation in (1, 2, 3):
        for tail_depth in range(valuation):
            for middle_depth in range(tail_depth + 1, 9):
                predicted_length = (
                    2 * min(valuation - tail_depth, middle_depth - tail_depth)
                    + (valuation == middle_depth)
                    - 1
                )
                if predicted_length < 2:
                    continue
                if valuation == 1:
                    assert (tail_depth, middle_depth, predicted_length) == (0, 1, 2)
                elif valuation == 2:
                    assert (
                        (
                            tail_depth == 0
                            and middle_depth == 2
                            and predicted_length == 4
                        )
                        or (
                            tail_depth == 0
                            and middle_depth >= 3
                            and predicted_length == 3
                        )
                        or (
                            tail_depth == 1
                            and middle_depth == 2
                            and predicted_length == 2
                        )
                    )
                else:
                    assert (
                        (
                            tail_depth == 0
                            and middle_depth == 2
                            and predicted_length == 3
                        )
                        or (
                            tail_depth == 0
                            and middle_depth == 3
                            and predicted_length == 6
                        )
                        or (
                            tail_depth == 0
                            and middle_depth >= 4
                            and predicted_length == 5
                        )
                        or (
                            tail_depth == 1
                            and middle_depth == 3
                            and predicted_length == 4
                        )
                        or (
                            tail_depth == 1
                            and middle_depth >= 4
                            and predicted_length == 3
                        )
                        or (
                            tail_depth == 2
                            and middle_depth == 3
                            and predicted_length == 2
                        )
                    )
    # G10: substitute the maximal nondecimal support into both gap bounds.
    M, Q, t2, t5, q2, q5, B2, s2, s5 = sp.symbols(
        "M Q t2 t5 q2 q5 B2 s2 s5", positive=True
    )
    support = M * Q / (t2 * t5 * q2 * q5)
    threshold2 = support**3 * q2 * 16 * B2**2 * t2**2 / s2 * q5**3
    threshold5 = support**3 * q2**3 * q5 * t5**2 / s5
    assert sp.factor(
        threshold2 - 16 * B2**2 * M**3 * Q**3 / (t2 * q2**2 * t5**3 * s2)
    ) == 0
    assert sp.factor(
        threshold5 - M**3 * Q**3 / (t2**3 * t5 * q5**2 * s5)
    ) == 0
    assert 2**20 > 10**6 and 2**10 > 10**3
    assert fb.subs({b: 1, x: sp.Rational(2, 5)}) == sp.Rational(47, 48)
    assert fb.subs({b: 2, x: sp.Rational(37, 200)}) == sp.Rational(1145200, 1145853)
    assert 16 * Fraction(14, 25)**3 < 4
    assert 64 * Fraction(16169, 40000)**3 < Fraction(2**42, 10**12)
    assert 5**3 > 10**2 and Fraction(101, 25) < 5
    for n in range(2, 13):
        T = 10**n
        m = 10 * n + 1
        assert 2 ** (2 * m) > 64 * Fraction(16169, 40000)**3 * T**6
        assert 2**m > T**2
        assert 5 ** (3 * n + 1) > Fraction(101, 25) * T**2
    print("OK: A2-G10 relative bound m3<=10*m2 and five-unit bound m3<=3*m2")
    print(
        "OK: A2-G01 first block {b1=1,a1=1..8} or {b1=2,a1=5,7,9,11,13}; exact real bounds"
    )
    print(
        "OK: A2-G02 odd-tail parity/length and exact finite-family recovery; no effective m2 cutoff"
    )
    print(
        "OK: A2-G03 odd nonzero quadratic coefficient and discriminants; Subspace Theorem is external"
    )
    print(
        "OK: A2-G06 normalized odd-tail valuation table; A2-F01 integer-square identity"
    )
    print(
        "OK: A2-G09 general tag recovery, nonzero degeneracies, and linear parity split"
    )


if __name__ == "__main__":
    main()
