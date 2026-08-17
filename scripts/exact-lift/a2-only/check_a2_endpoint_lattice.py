#!/usr/bin/env python3
"""Exact rational checks for the A2 endpoint-lattice continuation.

This script intentionally uses only Python's standard library. It verifies the
finite rational inequalities and Sturm sign checks used in
`docs/proofs/exact-lift/branches/a2-only/endpoint-lattice.md`. It does not enumerate A2
candidates and it is not a global A2 certificate.
"""

from fractions import Fraction as F


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def deriv(p):
    return trim([F(i) * p[i] for i in range(1, len(p))] or [F(0)])


def divmod_poly(a, b):
    a = trim(a)
    b = trim(b)
    if b == [0]:
        raise ZeroDivisionError
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b) and r != [0]:
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] += c
        for i in range(len(b)):
            r[i + k] -= c * b[i]
        r = trim(r)
    return trim(q), trim(r)


def sturm(p):
    seq = [trim(p), deriv(p)]
    while seq[-1] != [0]:
        _, r = divmod_poly(seq[-2], seq[-1])
        if r == [0]:
            break
        seq.append(trim([-x for x in r]))
    return seq


def eval_poly(p, x):
    acc = F(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc


def sign(v):
    return (v > 0) - (v < 0)


def variations(seq, x):
    signs = [sign(eval_poly(p, x)) for p in seq]
    signs = [s for s in signs if s]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def roots_in(p, lo, hi):
    seq = sturm(p)
    return variations(seq, lo) - variations(seq, hi)


def q0sq(a, x, y):
    A = F(a) + y
    B = F(2) + x
    S = F(a * a, 4) + y * y / (100 * x * x)
    D = A * A - B * B * S
    assert D > 0
    return A * A / D


def check_q0_windows():
    # For a=5 and a=7, q0(x,1) stays above the desired rational threshold.
    # Polynomial coefficients are constant-first.
    p5 = [64, 64, -9484, 40000, 10000]
    p7 = [438244, 438244, -100231939, 536848900, 134212225]
    assert roots_in(p5, F(27, 250), F(3, 16)) == 0
    assert eval_poly(p5, F(3, 20)) > 0
    assert roots_in(p7, F(1, 10), F(7, 40)) == 0
    assert eval_poly(p7, F(3, 25)) > 0

    assert q0sq(9, F(1, 10), F(1)) == F(8000, 503)
    assert q0sq(11, F(1, 10), F(1)) == F(256, 11)
    assert q0sq(13, F(1, 10), F(1)) == F(1600, 43)
    assert F(8000, 503) > F(997, 250) ** 2
    assert F(256, 11) > F(603, 125) ** 2
    assert F(1600, 43) > F(609, 100) ** 2

    # q0<4 in (a,k)=(9,2) forces x<2/19 and y>249/250.
    assert q0sq(9, F(2, 19), F(1)) == F(9025, 564) > 16
    assert q0sq(9, F(1, 10), F(249, 250)) == F(708050, 44237) > 16


def check_remainder_windows():
    # Upper bounds: J < sqrt(1+Smax)-1 and R/D = J-k.
    tests = [
        (5, F(27, 250), 1, F(17, 20)),
        (7, F(1, 10), 2, F(31, 40)),
        (9, F(1, 10), 3, F(18, 25)),
        (11, F(1, 10), 4, F(17, 25)),
        (13, F(1, 10), 5, F(33, 50)),
    ]
    for a, x_min, k, upper in tests:
        smax = F(a * a, 4) + 1 / (100 * x_min * x_min)
        assert 1 + smax < (F(k + 1) + upper) ** 2

    assert F(8000, 503) > F(997, 250) ** 2


def check_a9_endpoint():
    qsq = F(8000, 503)

    # zeta < 251/250.
    assert qsq > F(1001, 251) ** 2

    # w lower bound.
    w2_lower = F(7497, 503) / F(85, 4)
    assert w2_lower == F(1764, 2515)
    assert F(1764, 2515) > F(837, 1000) ** 2

    # w upper bound.
    num = F(3) * (F(3) + 2 * F(251, 250))
    smin = F(81, 4) + F(249, 250) ** 2 / (100 * F(2, 19) ** 2)
    assert num / smin < F(843, 1000) ** 2

    # v = y w/(10x) > 99/125.
    assert F(1764, 2515) > F(1320, 1577) ** 2

    v_lo, v_hi = F(99, 125), F(843, 1000)
    z_lo, z_hi = F(1), F(251, 250)
    delta_hi = F(3, 250)
    minus_lo = F(3) + z_lo - delta_hi - v_hi
    minus_hi = F(3) + z_hi - v_lo
    plus_lo = F(3) + z_lo - delta_hi + v_lo
    plus_hi = F(3) + z_hi + v_hi
    assert minus_lo > F(393, 125)
    assert minus_hi < F(1607, 500)
    assert plus_lo > F(2389, 500)
    assert plus_hi < F(606, 125)


def check_height_split():
    assert 5 ** 3 < 2 ** 7
    assert 20 ** 6 > 5 ** 11
    assert F(9, 14) > F(6, 11)
    assert F(6, 11) - F(3, 7) == F(9, 77)

    assert 4 * F(3, 7) - 3 * F(6, 11) == F(6, 77)
    assert 3 * F(3, 7) - 2 * F(6, 11) == F(15, 77)

    # m+d < 51M/77; for M>=11 this is < M-3.
    assert F(51, 77) * 11 < 11 - 3
    assert F(25, 2) / F(3, 250) > 1000


def slot_intersects(lo, hi, slo, shi):
    return lo < shi and slo < hi


def check_midline_high_rho_exclusion():
    low_slot = (F(786, 125), F(1607, 250))
    high_slot = (F(2389, 250), F(1212, 125))

    # d>=3 is impossible already from c_Q>=3 and w<843/1000.
    lower_d3 = F(3) * 25 * F(500, 843)
    assert lower_d3 > high_slot[1]

    # d=1, c_Q in {3,7,11}; each continuous interval misses every odd slot.
    for cq in (3, 7, 11):
        lo = F(500 * cq, 843)
        hi = F(10000 * cq, 15903)
        for kh in range(1, 51, 2):
            assert not slot_intersects(lo, hi, low_slot[0] / kh, low_slot[1] / kh)
            assert not slot_intersects(lo, hi, high_slot[0] / kh, high_slot[1] / kh)
        assert high_slot[1] / 51 < lo

    # d=2 forces c_Q=3.
    lo = F(7500, 843)
    hi = F(150000, 15903)
    for kh in range(1, 51, 2):
        assert not slot_intersects(lo, hi, low_slot[0] / kh, low_slot[1] / kh)
        assert not slot_intersects(lo, hi, high_slot[0] / kh, high_slot[1] / kh)
    assert high_slot[1] / 51 < lo

    # Boundary arithmetic in the proof of m>(M-2)/2.
    assert F(20, 4) == 5


def check_eta_one_lattice():
    """Verify the constant-size eta=1 slot classification.

    This enumerates only the bounded interval types forced by the rational
    endpoint windows.  It does not enumerate prefixes or A2 candidates.
    """

    low_slot = (F(786, 125), F(1607, 250))
    high_slot = (F(2389, 250), F(1212, 125))
    slots = (("-", low_slot), ("+", high_slot))
    w_lo, w_hi = F(837, 1000), F(843, 1000)
    q_hi = F(20, 19)

    # eta=-1 is impossible before entering the lattice.
    assert F(15_000, 843) > high_slot[1]

    # For eta=1, d>=4 is above every slot.  At d=3, c_Q>=7 is
    # likewise too large, while c_Q=3 lies in the gap between k_h=1
    # and all k_h>=3 slots.
    assert F(75_000, 4 * 843) > high_slot[1]
    d3_lo = F(3750, 843)
    d3_hi = F(75_000, 15_903)
    assert high_slot[1] / 3 < d3_lo
    assert d3_hi < low_slot[0]

    expected = {
        1: [
            (3, 35, "-"),
            (3, 51, "+"),
            (3, 53, "+"),
            (7, 15, "-"),
            (7, 23, "+"),
            (23, 7, "+"),
            (31, 5, "+"),
            (51, 3, "+"),
            (103, 1, "-"),
            (107, 1, "-"),
            (159, 1, "+"),
            (163, 1, "+"),
        ],
        2: [(3, 7, "-"), (7, 3, "-"), (31, 1, "+")],
    }

    actual = {}
    for d in (1, 2):
        scale = F(5) ** (d - 2) / 4
        cq_max = int(high_slot[1] * w_hi / scale)
        hits = []
        for cq in range(3, cq_max + 1, 4):
            if cq % 5 == 0:
                continue
            g_lo = cq * scale / w_hi
            g_hi = cq * scale * q_hi / w_lo
            for label, (slot_lo, slot_hi) in slots:
                kh_max = int(slot_hi / g_lo)
                for kh in range(1, kh_max + 1, 2):
                    if slot_intersects(g_lo, g_hi, slot_lo / kh, slot_hi / kh):
                        hits.append((cq, kh, label))
        actual[d] = hits

    assert actual == expected

    # The coarse-slot-only uniform exclusion is false: this eta=1
    # type has a genuine interval overlap.
    witness_lo = F(7750, 843)
    witness_hi = F(155_000, 15_903)
    assert witness_lo < high_slot[0]
    assert high_slot[1] < witness_hi


def check_eta_one_correlated_bounds():
    """Check the exact correlated bounds that remove two eta=1 types."""

    h_hi = F(1001, 250)
    y_lo = F(249, 250)
    r_hi = F(843, 1000)

    minus_hi = r_hi * (h_hi - y_lo * r_hi)
    assert minus_hi == F(666_891_399, 250_000_000)
    assert minus_hi < F(107, 40)

    # In the positive slot, exact concatenation gives
    # r < h_hi * a/(b+y).  The normalized upper function is increasing
    # in y because b*(1-a)+y*(a+1)<0 throughout y<=1.
    a = F(21, 10)
    b = F(9) - F(3, 10**11)
    assert b * (1 - a) + (a + 1) < 0
    c_at_one = a / (b + 1)
    plus_hi = h_hi * h_hi * c_at_one * (1 + c_at_one)
    assert plus_hi < F(163, 40)


def check_prefix_barrier_r_bound():
    """Verify the polynomial certificate for r>4/5 and its consequence."""

    chi_hi = F(20, 19)
    y_lo = F(249, 250)

    def p(chi, y):
        return (
            324 * chi**4
            + 12_960 * chi**3
            - 1584 * chi**2 * y**2
            - 28_800 * chi**2 * y
            + 25 * chi**2
            + 640 * chi * y**2
            + 1000 * chi
            + 6400 * y**2
            + 10_000
        )

    assert p(chi_hi, F(1)) == F(160_000, 130_321) > 0

    # P_y=-32*B_y and B_y>0 on the rectangle.
    by_lower = 999 * F(1) ** 2 - 40 * F(1) - 400
    assert by_lower > 0

    # P_chi=-2*B_chi.  This coarse endpoint bound stays positive,
    # hence P decreases in chi as well as in y.
    bchi_lower = (
        -648 * chi_hi**3
        - 19_440 * chi_hi**2
        + 1584 * y_lo**2
        + 28_800 * y_lo
        - 25 * chi_hi
        - 320
        - 500
    )
    assert bchi_lower > 0

    k_plus_lower = F(4, 5) * (F(997, 250) + y_lo * F(4, 5))
    assert k_plus_lower == F(11_962, 3125)
    assert k_plus_lower > F(153, 40)


def check_eta_one_norm_support():
    """Check the finite consequence of the Gaussian norm support lemma."""

    eta_one_types = [
        (1, 3, 35, "-"),
        (1, 3, 53, "+"),
        (1, 7, 15, "-"),
        (1, 7, 23, "+"),
        (1, 23, 7, "+"),
        (1, 31, 5, "+"),
        (1, 103, 1, "-"),
        (1, 159, 1, "+"),
        (2, 3, 7, "-"),
        (2, 7, 3, "-"),
        (2, 31, 1, "+"),
    ]

    def allowed_prime_support(n):
        p = 3
        if n % 5 == 0:
            return False
        while p * p <= n:
            if n % p:
                p += 2
                continue
            if p % 4 == 3 and p != 3:
                return False
            while n % p == 0:
                n //= p
            p += 2
        return not (n > 1 and n % 4 == 3 and n != 3)

    survivors = [row for row in eta_one_types if allowed_prime_support(row[2])]
    assert survivors == [
        (1, 3, 53, "+"),
        (1, 103, 1, "-"),
        (1, 159, 1, "+"),
        (2, 7, 3, "-"),
        (2, 31, 1, "+"),
    ]

    # k_h=3 forces a second factor of 3 in the complementary odd
    # quotient, but the global LCM sphere need not be primitive.  This
    # type therefore remains; the implication is structural, not a
    # contradiction.
    assert (2, 7, 3, "-") in survivors


def check_eta_one_exact_phases():
    """Check the finite CRT phase tables for the five eta=1 types."""

    roots_one = {
        modulus: [x for x in range(modulus) if x * x % modulus == 1]
        for modulus in (515, 795, 775)
    }
    assert roots_one == {
        515: [1, 104, 411, 514],
        795: [1, 211, 266, 319, 476, 529, 584, 794],
        775: [1, 249, 526, 774],
    }

    roots_minus_one_53 = [x for x in range(53) if x * x % 53 == 52]
    assert roots_minus_one_53 == [23, 30]


def check_quotient_angle_wedge():
    """Check the endpoint constants in the eta-uniform quotient angle wedge."""

    assert F(606, 125) < 5

    # M>=11, so S=10^(M-1)>=10^10.  The lower estimate is increasing
    # to 90/21 and the upper estimate is decreasing to
    # (1800/19)/(498/25); the endpoint already gives 4<tan(phi)<5.
    s = 10**10
    lower = F(90 * s, 21 * s + 5)
    upper = F(1800 * s, 19) / (F(498 * s, 25) - 5)
    assert lower > 4
    assert upper < 5

    # Uniform small-remainder constant in (16.122).
    small_remainder_ratio = F(25, 27) * F(5**7, 2**21)
    assert small_remainder_ratio < F(1, 25)

    # The relative centered error in (16.129) is bounded using
    # sqrt(5/2)<8/5, c_Q>=3 and M>=11.  The induced tangent strip in
    # (16.133) uses tan(phi_S),tan(phi_a)<5.
    relative_error = F(8, 5) / (3 * 2**12)
    assert relative_error == F(1, 7680)
    assert F(26, 7679) < F(7, 2000)

    # The exact angular decoding (16.138) has magnitude below
    # 15/(20*a_2-4), which is already below 1/a_2 for every a_2>=1.
    assert F(15, 16) < 1

    # Audit the two decimal cancellations behind (16.138) with exact
    # rationals.  Here h=9w/2, N=9*2^M*c_Q*q, and the only relations
    # used are K*C0=N+h and C0*U=h*a2.
    a2, c0, j = F(997), F(4511), F(299, 100)
    u, k = F(4, 5), F(41, 2)
    h = c0 * u / a2
    n = k * c0 - h
    for epsilon in (-1, 1):
        denominator = k * a2 - u - epsilon * j
        lhs = n / denominator - c0 / a2
        rhs = F(epsilon) * c0 * j / (a2 * denominator)
        assert lhs == rhs

    # Uniform Euclidean split constants (16.144)--(16.148); a_2>=4
    # is far weaker than the actual endpoint digit lower bound.
    a2_min = 4
    lower_area_ratio = F(9, 2) * F(747, 250) * a2_min / (
        21 * a2_min + 3
    )
    upper_area_ratio = F(15 * a2_min, 20 * a2_min - 4)
    assert lower_area_ratio > F(3, 5)
    assert upper_area_ratio < F(4, 5)

    # Matrix determinants in (16.151).
    for epsilon in (-1, 1):
        a2, c0 = 7, 31
        if epsilon == 1:
            det = (-c0) * (-a2) - a2 * (c0 + 1)
        else:
            det = c0 * a2 - (-a2) * (1 - c0)
        assert det == -epsilon * a2

    # Constants in the genuine Gaussian Euclidean step (16.153)--(16.159).
    assert 4**11 > 5
    assert F(1, 3) > F(4, 25)

    # Scalar quadratic kernel (16.166)--(16.167).
    y, r_plus, r1, c_u, r_e = 5, 1, 2, 3, 7
    k_h = F(r_plus**2 + r1**2, y)
    quadratic = y * r_e**2 - 2 * c_u * r_plus * r_e + c_u**2 * k_h
    assert quadratic > 0
    discriminant = (-2 * c_u * r_plus) ** 2 - 4 * y * c_u**2 * k_h
    assert discriminant == -4 * c_u**2 * r1**2

    # Second centered representative and prefix-discriminant norm.
    assert 5**9 < 2**21
    five_nu, x_factor, y_factor = 5, 1, 1
    a2, c0, c_u, c_minus, z_e, epsilon = 1, 2, 3, 1, 2, 1
    assert five_nu * x_factor * y_factor == a2**2 + c0**2
    second_quadratic = (
        five_nu * y_factor * z_e**2
        - 2 * epsilon * c_u * a2 * c_minus * z_e
        + c_u**2 * c_minus**2 * x_factor
    )
    completed_square = (
        five_nu * y_factor * z_e - epsilon * c_u * a2 * c_minus
    ) ** 2 + (c_u * c_minus * c0) ** 2
    assert completed_square == five_nu * y_factor * second_quadratic
    second_discriminant = (-2 * epsilon * c_u * a2 * c_minus) ** 2 - (
        4 * five_nu * y_factor * c_u**2 * c_minus**2 * x_factor
    )
    assert second_discriminant == -4 * c_u**2 * c_minus**2 * c0**2

    # Uniform source-ratio constants in (16.190)--(16.194).
    assert F(25, 3 * 2**16) < F(1, 7000)
    assert F(8, 5) * F(1, 7000) < F(1, 4000)
    assert F(1, 4000) / (1 - F(1, 4000)) == F(1, 3999)


def check_rational_root_cofactors():
    """Audit the algebra and constants in (16.196)--(16.216).

    This checks identities, not existence of an Exact Lift candidate.
    """

    # The logarithmic derivative is positive on both intervals used in
    # (16.200) and (16.212).  M>=11 makes the decimal prefix enormous;
    # this much weaker endpoint check is sufficient.
    assert 60 < 10 * (9 * 10**10) - 3
    assert 120 < 10 * (9 * 10**10) - 4

    # Exact normalized decomposition (16.202)--(16.203), audited with
    # arbitrary integral structural data.  No root/existence claim is made.
    m, d, g = 5, 1, 7
    l_scale = 2**m * 5**d
    d_big = g * l_scale
    c_small = 3
    c_minus, c_plus = 1, 7
    x_factor = 3 * d_big - c_small
    c_u, q, y_factor = 3, 11, 13
    t, a3, p = 10**m, 10**m + 1, 10**11 + 9
    a_term = (3 * t + 2 * a3) * (10 * p - 3) ** 2
    b_term = (3 * t + a3) ** 2
    normalized = (
        3 * c_u**2 * g**2 * l_scale**3 * a_term
        - (c_minus * c_plus) ** 2 * q**2 * x_factor * y_factor * b_term
    )
    decomposed = 3 * d_big * (
        c_u**2 * g * l_scale**2 * a_term
        - q**2 * c_plus**2 * y_factor * b_term
    ) + c_small * q**2 * c_plus**2 * y_factor * b_term
    assert normalized == decomposed

    # The two adjacent shifted denominators are odd, coprime, and coprime
    # to D whenever gcd(C,D)=1.
    assert d_big % 2 == 0 and c_small % 2 == 1
    from math import gcd

    assert gcd(c_small, d_big) == 1
    assert gcd(d_big - c_small, d_big + c_small) == 1

    # Decimal-scale separation used in (16.220)--(16.224).
    assert F(1250, 4731 * 64) < F(1, 200)
    assert F(3, 250) * F(1, 200) == F(3, 50_000)

    # Generic polynomial audit for (16.210): if N/D is a rational root,
    # every shifted numerator s_j=jD-N divides F(j).
    d0, n0 = 10, 3

    def polynomial(j):
        return (d0 * j - n0) * (j**3 + 2 * j + 5)

    for j in range(-3, 7):
        shifted = j * d0 - n0
        assert polynomial(j) % shifted == 0

    # Principal-square audit for the g^2 lift (16.231)--(16.233).
    for prime, exponent in ((3, 2), (7, 3), (11, 1)):
        modulus = prime ** (2 * exponent)
        d_local, c_local = prime**exponent * 10, 13
        c_inverse = pow(c_local, -1, modulus)
        half = pow(2, -1, modulus)
        correction = (1 - 3 * d_local * c_inverse) % modulus
        root = (1 - 3 * half * d_local * c_inverse) % modulus
        assert root * root % modulus == correction

    # For 2^(2e), every principal unit congruent to 1 mod 8 is a square.
    for exponent in (2, 3, 5):
        modulus = 2 ** (2 * exponent)
        d_local, c_local = 2 ** (exponent + 2) * 5, 3
        correction = (1 - 3 * d_local * pow(c_local, -1, modulus)) % modulus
        assert correction % 8 == 1
        assert any(x * x % modulus == correction for x in range(modulus))

    # Secant cubic audit for (16.234)--(16.251).
    t_scale, a3, k_big = F(10), F(11), F(1000)
    root = F(299, 100)
    a_scale = F(17)

    def f_value(j):
        return j * (t_scale * j + 2 * a3) * (k_big - j) ** 2

    def h_value(j):
        return (t_scale * j + a3) ** 2

    b_scale = a_scale * f_value(root) / h_value(root)

    def polynomial_value(j):
        return a_scale * f_value(j) - b_scale * h_value(j)

    def secant(j):
        return polynomial_value(j) / (j - root)

    h2, h3, h4 = (secant(F(j)) for j in (2, 3, 4))
    assert h2 < h3 < h4
    assert h4 - h3 < h3 - h2
    leading4 = a_scale * t_scale
    leading3 = a_scale * (2 * a3 - 2 * k_big * t_scale)
    curvature = 2 * h3 - h2 - h4
    assert curvature == -2 * (leading3 + (root + 9) * leading4)
    assert curvature == 2 * leading4 * (
        2 * k_big - root - 9 - 2 * a3 / t_scale
    )
    right_gap = h4 - h3
    assert 0 < curvature < right_gap

    # Exact unit content of the curvature bracket in (16.245)--(16.256).
    m, d, c_u, g, c_small = 5, 1, 3, 28, 1
    t_scale = 10**m
    a3, k_big = t_scale + 1, 10**12
    five_lambda = 5 ** (m - d)
    h0 = g * (3 * t_scale + a3) - five_lambda * c_small
    bracket = g * ((2 * k_big - 9) * t_scale - a3) - h0

    def valuation(n, prime):
        value = 0
        while n % prime == 0:
            value += 1
            n //= prime
        return value

    curvature_integer = 2 ** (m + 1) * 5**d * c_u**2 * bracket
    assert bracket % 2 == 1 and bracket % 5 != 0
    assert valuation(curvature_integer, 2) == m + 1
    assert valuation(curvature_integer, 5) == d

    # Once-normalized additive cofactor (16.263)--(16.271).
    l_scale = 2**m * 5**d
    d_big = g * l_scale
    gamma_tilde = c_u**2 * bracket
    delta_plus = 6
    t2_tilde = (d_big - c_small) * gamma_tilde + g * delta_plus
    assert t2_tilde % g == (-5 ** (m - d) * (c_u * c_small) ** 2) % g
    assert t2_tilde % 4 == 3
    assert gcd(t2_tilde, g) == 1

    # The second exact 5^d content and the genuinely 2,5-primitive
    # cofactor in (16.288)--(16.302).  These are structural data, not an
    # existence sample.
    m, d = 5, 1
    five_lambda = 5 ** (m - d)
    c_u, g, c_q, q = 3, 28, 11, 19
    x_factor, y_factor = 17, 41
    t_scale, a3, k_big = 10**m, 10**m + 1, 10**12
    s0 = (
        t_scale * k_big**2
        - (18 * t_scale + 4 * a3) * k_big
        + 18 * a3
        + 55 * t_scale
    )
    t2_tilde = (
        2**m * 5**d * c_u**2 * g**2 * s0
        - (c_q * q * five_lambda) ** 2 * x_factor * y_factor
    )
    assert valuation(s0, 5) == 0
    assert valuation(t2_tilde, 5) == d
    t2_hat = t2_tilde // 5**d
    assert t2_hat > 0 and t2_hat % 5 != 0 and t2_hat % 4 == 3

    q0 = c_q * q
    assert gcd(c_u * g, q0 * x_factor * y_factor) == 1
    assert gcd(t2_hat, q0 * x_factor * y_factor) == gcd(
        s0, q0 * x_factor * y_factor
    )

    f_factor = five_lambda * q + 2 * c_u
    r_f = 2**m * 5**d * g**2 * s0 - 4 * c_q**2 * x_factor * y_factor
    assert gcd(f_factor, 5 * c_u * q) == 1
    assert gcd(t2_hat, f_factor) == gcd(r_f, f_factor)

    # Curvature discriminants (16.314) and (16.319).
    r_23 = 2 * a3**2 + 9 * t_scale * a3 + 13 * t_scale**2
    base_b = -(18 * t_scale + 4 * a3)
    base_c = 18 * a3 + 55 * t_scale
    base_discriminant = base_b**2 - 4 * t_scale * base_c
    assert base_discriminant == 8 * r_23
    assert r_23 == (
        2 * (a3 + 2 * t_scale) ** 2
        + (a3 + 2 * t_scale) * t_scale
        + 3 * t_scale**2
    )
    a_f = 2**m * 5**d * g**2
    rf_discriminant = (a_f * base_b) ** 2 - 4 * (
        a_f * t_scale
    ) * (a_f * base_c - 4 * c_q**2 * x_factor * y_factor)
    r_23_f = a_f * r_23 + 2 * t_scale * c_q**2 * x_factor * y_factor
    assert rf_discriminant == 8 * a_f * r_23_f

    # Global square completion (16.322)--(16.324).
    c_23 = (
        2 * c_u**2 * g**2 * r_23
        + 5 ** (m + 2 * (m - d) - d)
        * q0**2
        * x_factor
        * y_factor
    )
    square_side = (
        c_u * g * (t_scale * k_big - 9 * t_scale - 2 * a3)
    ) ** 2
    assert square_side == c_23 + 5**m * t2_hat
    hat_discriminant = (
        2**m * c_u**2 * g**2 * base_b
    ) ** 2 - 4 * (
        2**m * c_u**2 * g**2 * t_scale
    ) * (
        2**m * c_u**2 * g**2 * base_c
        - q0**2 * 5 ** (2 * (m - d) - d) * x_factor * y_factor
    )
    assert hat_discriminant == (2 ** (m + 1) * c_u * g) ** 2 * c_23
    u_23 = c_u * g * (2 * a3 + 9 * t_scale // 2)
    v_23 = c_u * g * t_scale // 2
    assert c_23 == (
        u_23**2
        + 23 * v_23**2
        + 5 ** (3 * (m - d)) * q0**2 * x_factor * y_factor
    )
    assert c_23 % 5 ** (2 * m) == u_23**2 % 5 ** (2 * m)
    assert c_23 % 8 == 1

    # Restore the common 5^(lambda-d) content omitted by the compressed
    # wording in core section 13; cf. (16.329a).
    lambda_value = m - d
    nu_value = lambda_value - 2 * d
    common_five = 5 ** (lambda_value - d)
    c_minus, c_plus = 1, c_q
    u_minus_alloc = common_five * f_factor * c_minus**2 * x_factor
    u_plus_alloc = common_five * q * c_plus**2 * y_factor
    n0_alloc = 5**nu_value * x_factor * y_factor
    assert u_minus_alloc * u_plus_alloc == (
        5**lambda_value * c_q**2 * q * f_factor * n0_alloc
    )

    # Canonical/companion shifted factorization (16.329)--(16.335).
    # The scale identity is checked from the original core definition.
    t_exponent = 3
    rho = g // 2 ** (t_exponent - 1)
    assert g == 2 ** (t_exponent - 1) * rho
    u_source = c_u * rho
    p_prefix = k_big // 10
    canonical_a = (
        5 ** ((m - d) + 1)
        * 2 ** (m + t_exponent)
        * u_source
        * p_prefix
    )
    assert 5**d * canonical_a == t_scale * c_u * g * k_big
    canonical_z = canonical_a - 101
    u_minus = canonical_a - canonical_z
    u_plus = canonical_a + canonical_z
    e_23 = c_u * g * (9 * t_scale + 2 * a3)
    w_23 = c_u * g * (t_scale * k_big - 9 * t_scale - 2 * a3)
    assert w_23 == 5**d * canonical_a - e_23
    v_minus = 5**d * u_minus - e_23
    v_plus = 5**d * u_plus - e_23
    assert v_minus == w_23 - 5**d * canonical_z
    assert v_plus == w_23 + 5**d * canonical_z
    assert v_minus * v_plus == w_23**2 - 5 ** (2 * d) * canonical_z**2

    # Uniform positivity constant in (16.333)--(16.334).
    assert F(747, 250) * 2**12 * 5**11 > F(1376, 125)

    # Eliminate the canonical square root and audit the denominator
    # square-depth laws (16.341)--(16.347).
    nu_5 = m - 3 * d
    assert nu_5 >= 0
    n0 = 5**nu_5 * x_factor * y_factor
    c_source = c_q * c_u
    z_square = canonical_a**2 - (
        5 ** (m - d)
        * q0
        * n0
        * (5 ** (m - d) * q0 + 2 * c_source)
    )
    d_z = e_23**2 - (
        5 ** (m + d)
        * q0
        * n0
        * (5 ** (m - d) * q0 + 2 * c_source)
    )
    assert d_z == (
        5 ** (2 * d) * z_square
        - w_23 * (e_23 + 5**d * canonical_a)
    )
    l_23 = 9 * t_scale // 2 + a3
    assert e_23 == 2 * c_u * g * l_23
    assert gcd(q, f_factor) == 1
    assert gcd(2 * c_u * g, q * f_factor) == 1
    assert gcd(d_z, q * f_factor) == gcd(l_23**2, q * f_factor)

    # Source/digit Hensel targets and their H-defect rewrite
    # (16.359)--(16.366).
    big_m = 6
    h_defect = 4 * c_u * 2**m * g - 5 ** (big_m - 1)
    h_q = 2 * a3 * g * c_u - 9 * 5 ** (big_m + m)
    h_f = h_q - 18 * c_source * 5**d
    g_q = 5 ** (big_m - 1) * (a3 - 90 * t_scale) + a3 * h_defect
    g_f = g_q - 18 * 2 ** (m + 1) * c_source * 5**d
    assert 2 ** (m + 1) * h_q == g_q
    assert 2 ** (m + 1) * h_f == g_f
    w_scale = F(2 ** (big_m + 1) * c_source, 5 ** (m - d))
    assert F(g_q - g_f, 5 ** (big_m - 1) * t_scale) == (
        F(18) * w_scale / (2**big_m * 5 ** (big_m - 1))
    )

    # Exact saturation/additive-contact resultant (16.385)--(16.388).
    u_23 = 2 * a3 + 9 * t_scale
    s_0 = (
        t_scale * k_big**2
        - (18 * t_scale + 4 * a3) * k_big
        + 18 * a3
        + 55 * t_scale
    )
    assert s_0 == (
        t_scale * (k_big**2 - 26) - (2 * k_big - 9) * u_23
    )
    assert 9**2 - 26 == 5 * 11
    assert 9**2 - 4 * 26 == -23

    # Exact f-side resultant and correction threshold (16.400)--(16.402).
    r_lambda = 2**m * 5 ** (m - d) * g
    phi_f = r_lambda**2 * (k_big**2 - 26) - 4 * c_q**2 * n0
    r_f_exact = 2**m * 5**d * g**2 * s_0 - 4 * c_q**2 * x_factor * y_factor
    assert 5**nu_5 * r_f_exact == (
        phi_f
        - 2**m
        * 5 ** (d + nu_5)
        * g**2
        * (2 * k_big - 9)
        * u_23
    )

    # q/f local-type normalization and the prefix rotation
    # (16.395q)--(16.399).
    nu_local = m - 3 * d
    lambda_local = m - d
    assert m + d + nu_local == 2 * lambda_local
    prefix_m, b2_local, a2_local = 4, 200, 997
    q_concat = 2 * 10**prefix_m + b2_local
    c0_local = 9 * b2_local // 2
    p_local = 9 * 10 ** (prefix_m - 1) + a2_local
    k_local = 10 * p_local
    assert k_local - 9 * q_concat // 2 == 10 * a2_local - c0_local
    j_101 = 10 * c0_local + a2_local
    n0_local = c0_local**2 + a2_local**2
    assert (10 * a2_local - c0_local) ** 2 + j_101**2 == 101 * n0_local
    psi_f = b2_local**2 * (k_local**2 - 26) - q_concat**2 * n0_local
    x_local = F(b2_local, 10**prefix_m)
    y_local = F(a2_local, 10 ** (prefix_m - 1))
    s9_local = F(81, 4) + y_local**2 / (100 * x_local**2)
    assert F(psi_f, b2_local**2 * q_concat**2) == (
        (9 + y_local) ** 2 / (2 + x_local) ** 2
        - s9_local
        - F(26, q_concat**2)
    )
    endpoint_ratio = F(9) + F(249, 250)
    endpoint_ratio /= F(2) + F(2, 19)
    assert endpoint_ratio**2 / 16 > 1

    # Canonical factor allocation selects the q-side third branch
    # (16.414)--(16.418).
    canonical_scale = 2**m * 5 ** (m - d) * c_u * g * k_big
    assert canonical_scale // (c_u * 5 ** (m - 2 * d)) == d_big * k_big

    # Endpoint-external factor is the true sphere height (16.431)--(16.433).
    c_endpoint = 3
    n_endpoint = 3 * d_big - c_endpoint
    h0_endpoint = g * (3 * t_scale + a3) - 5 ** (m - d) * c_endpoint
    assert t_scale * n_endpoint + a3 * d_big == (
        2**m * 5**d * h0_endpoint
    )

    # Middle-branch quotient identity in (16.375)--(16.377).  This is
    # purely algebraic; the script does not search for saturating primes.
    prime_power = 7
    a3_local = (prime_power * 32 - 9 * t_scale) // 2
    c_local = prime_power * 29 - 6 * d_big
    s_local = (2 * a3_local + 9 * t_scale) // prime_power
    r_local = (6 * d_big + c_local) // prime_power
    middle = d_big * (3 * t_scale + 2 * a3_local) - t_scale * c_local
    assert middle == prime_power * (d_big * s_local - t_scale * r_local)
    assert d_big * s_local - t_scale * r_local == (
        2**m * 5**d * (g * s_local - 5 ** (m - d) * r_local)
    )

    # Mod-4 inert-carrier orientation (16.349)--(16.352).
    assert q0 % 4 == 1 and c_q % 4 == 3
    assert q % 4 == 3 and f_factor % 4 == 1
    for z_mod4, expected_delta in ((1, 1), (3, 0)):
        x_mod4 = (-z_mod4) % 4
        y_mod4 = (-z_mod4) % 4
        assert x_mod4 == y_mod4
        assert (x_mod4 == 3) == (expected_delta == 1)
        v_minus_mod4 = (-z_mod4) % 4
        v_plus_mod4 = z_mod4
        assert {v_minus_mod4, v_plus_mod4} == {1, 3}
        if expected_delta == 1:
            assert (v_minus_mod4 * pow(3, -1, 4)) % 4 == 1
            assert (v_plus_mod4 * pow(3, -1, 4)) % 4 == 3

    # Exhaust the residue computation in (16.305)--(16.310).  The
    # relation nu_5=m-3d is the only parity input.
    for m_local, d_local in ((5, 1), (6, 1), (8, 2)):
        nu_local = m_local - 3 * d_local
        assert nu_local >= 0
        for a2_mod3 in (0, 1, 2):
            for a3_mod3 in (0, 1, 2):
                s0_mod3 = (
                    a2_mod3**2 - a2_mod3 * a3_mod3 + 1
                ) % 3
                xy_mod3 = (
                    0 if a2_mod3 == 0 else (-1) ** nu_local
                )
                for q0_divisible_by_3 in (False, True):
                    q0_square = 0 if q0_divisible_by_3 else 1
                    hat_mod3 = (
                        (-1) ** m_local * s0_mod3
                        - q0_square * (-1) ** d_local * xy_mod3
                    ) % 3
                    expected = (
                        a2_mod3 != 0
                        and (
                            (
                                not q0_divisible_by_3
                                and a2_mod3 * a3_mod3 % 3 == 1
                            )
                            or (
                                q0_divisible_by_3
                                and a2_mod3 * a3_mod3 % 3 == 2
                            )
                        )
                    )
                    assert (hat_mod3 == 0) == expected

    # Complete mod-9 residue audit for (16.311)--(16.313).  Powers of
    # 2 and 5 have period 6 modulo 9, so these loops cover every local
    # unit class.  All 0,3,6 lifts genuinely remain possible after the
    # mod-3 contact condition.
    units_mod9 = (1, 2, 4, 5, 7, 8)
    for q0_divisible_by_3 in (False, True):
        lifts = set()
        for m_mod6 in range(6):
            for big_m_mod6 in range(6):
                five_big_m = pow(5, big_m_mod6, 9)
                for source_unit in units_mod9:
                    q0_mod9 = (
                        five_big_m
                        + pow(2, m_mod6, 9) * source_unit
                    ) % 9
                    if (q0_mod9 % 3 == 0) != q0_divisible_by_3:
                        continue
                    for a2_mod9 in units_mod9:
                        for a3_mod9 in units_mod9:
                            required_product = (
                                2 if q0_divisible_by_3 else 1
                            )
                            if a2_mod9 * a3_mod9 % 3 != required_product:
                                continue
                            s0_mod9 = (
                                a2_mod9**2
                                - 4 * a2_mod9 * a3_mod9
                                + 1
                            ) % 9
                            hat_mod9 = (
                                pow(2, m_mod6, 9)
                                * source_unit**2
                                * s0_mod9
                                - pow(5, m_mod6, 9)
                                * q0_mod9**2
                                * a2_mod9**2
                            ) % 9
                            lifts.add(hat_mod9)
        assert lifts == {0, 3, 6}

    # Additive CRT identity (16.258)--(16.262).
    d_big, c_small, l_scale = 100, 3, 20
    xi_center, delta_minus, delta_plus = 101, 14, 6
    xi_minus = xi_center - l_scale * delta_minus
    xi_plus = xi_center + l_scale * delta_plus
    f2 = -(d_big - c_small) * xi_minus
    f3 = c_small * xi_center
    f4 = (d_big + c_small) * xi_plus
    second_difference = (f4 - 2 * f3 + f2) // l_scale
    assert second_difference == (
        (d_big + c_small) * delta_plus
        + (d_big - c_small) * delta_minus
    )
    inv_minus = pow(2 * c_small, -1, d_big - c_small)
    inv_plus = pow(2 * c_small, -1, d_big + c_small)
    assert delta_plus % (d_big - c_small) == (
        inv_minus * second_difference
    ) % (d_big - c_small)
    assert delta_minus % (d_big + c_small) == (
        -inv_plus * second_difference
    ) % (d_big + c_small)


def main():
    check_q0_windows()
    check_remainder_windows()
    check_a9_endpoint()
    check_height_split()
    check_midline_high_rho_exclusion()
    check_eta_one_lattice()
    check_eta_one_correlated_bounds()
    check_prefix_barrier_r_bound()
    check_eta_one_norm_support()
    check_eta_one_exact_phases()
    check_quotient_angle_wedge()
    check_rational_root_cofactors()
    print("A2 endpoint-lattice exact checks: OK")


if __name__ == "__main__":
    main()
