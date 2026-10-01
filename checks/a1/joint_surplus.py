"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0269; see history/sources.json.
"""

from fractions import Fraction as F
from math import gcd

import sympy as sp


def check_algebra() -> None:
    e, p, q, w, y, t, inv_h, delta, radius, zeta, lam = sp.symbols(
        "e p q w y t inv_h delta radius zeta lam"
    )
    bracket = 1 + e * p - inv_h * (1 - e * q) + delta * (radius - zeta)
    sphere_residual = (
        radius**2 - (1 - e * q) ** 2 - e * (1 + e * p) ** 2 - zeta**2
    )
    contact_residual = 1 + e * p - radius - lam * bracket
    f = 2 * p + q**2 - p**2
    excess_residual = (
        e * (2 * (p + q) - 1)
        - lam * bracket * (1 + e * p + radius)
        - zeta**2
        - e**2 * f
        - e**3 * p**2
    )
    assert sp.expand(
        excess_residual
        - sphere_residual
        - contact_residual * (1 + e * p + radius)
    ) == 0

    # JS10 after substituting the exact excess decomposition.
    excess, contact, rad = sp.symbols("excess contact rad")
    b0 = 1 - inv_h + delta
    normalized_k = excess / 2 + e * (y * q - w * p) - t + t * inv_h
    normalized_k = normalized_k.subs(
        excess, 2 * t * contact + rad + e * f + e**2 * p**2
    )
    expected = t * (contact - b0) + e * (f / 2 + y * q - w * p) + e**2 * p**2 / 2
    assert sp.expand(normalized_k - t * delta - rad / 2 - expected) == 0

    normalized_lambda = (1 + e * y) / (1 - e * w + t * e * (1 + e * y))
    expected_difference = e * (y + w - t - t * e * y) / (
        1 - e * w + t * e * (1 + e * y)
    )
    assert sp.cancel(normalized_lambda - 1 - expected_difference) == 0

    u = sp.symbols("u", positive=True)
    coupled_slack = sp.Rational(51, 100) - u / 10 - 1 / (200 * u**2)
    factored_slack = (10 * u - 1) * (-2 * u**2 + 10 * u + 1) / (200 * u**2)
    assert sp.cancel(coupled_slack - factored_slack) == 0

    h, tail_y, lcm_q, prefix, tail_t, a3, b3, prefix_q, denom_t = sp.symbols(
        "h tail_y lcm_q prefix tail_t a3 b3 prefix_q denom_t"
    )
    alpha = prefix * tail_t + a3
    beta = prefix_q * denom_t + b3
    word_residual = h * beta - lcm_q * alpha
    third_residual = lcm_q * a3 - tail_y * b3
    gap_residual = (h - tail_y) * beta - (lcm_q * prefix * tail_t - tail_y * prefix_q * denom_t)
    plus_residual = (h + tail_y) * beta - (lcm_q * prefix * tail_t + tail_y * prefix_q * denom_t + 2 * lcm_q * a3)
    assert sp.expand(gap_residual - word_residual - third_residual) == 0
    assert sp.expand(plus_residual - word_residual + third_residual) == 0

    c5, a12, ten_n, beta_a, beta_b, tail_a = sp.symbols("c5 a12 ten_n beta_a beta_b tail_a")
    normalized_plus_word = c5 * a12 * ten_n + tail_y * beta_a + 2 * c5 * tail_a
    normalized_resonance_word = c5 * a12 * ten_n + tail_y * (beta_a + 2 * beta_b)
    assert sp.expand(normalized_plus_word - normalized_resonance_word - 2 * (c5 * tail_a - tail_y * beta_b)) == 0


def check_uniform_constants() -> None:
    eps = F(1, 10000)
    cap = F(267, 500)
    y_cap = F(107, 200)
    t_cap = F(1, 100)
    assert cap / (1 - eps * cap) < y_cap
    lambda_error = (y_cap + cap + t_cap * (1 + eps * y_cap)) / (1 - eps * cap)
    assert lambda_error < F(11, 10)
    assert cap * (1 + F(1, 10) + F(1, 100)) + F(1, 10) < F(7, 10)
    contact_error = (
        F(11, 10) * (F(101, 100) + F(7, 10) * eps) * (1 + cap * eps)
        + F(7, 10) * (1 + cap * eps)
        + F(101, 100) * cap
    )
    assert contact_error < 4
    # For p>=1/2 the quadratic is decreasing; for p<1/2 use
    # 1/4+p-2*p^2 = 1/4+p*(1-2*p) >= 1/4.
    assert 2 * cap - 3 * cap**2 > F(21, 100)
    assert F(1, 4) > F(21, 100)
    assert F(21, 200) - 4 * t_cap == F(13, 200) > 0
    remainder_cap = 4 * t_cap + cap + cap**2 / 2 + y_cap * cap + eps * cap**2 / 2
    assert remainder_cap < 2
    assert F(1, 10) + F(1, 2) + F(1, 5) == F(4, 5) < 1
    assert F(1, 100) + F(1, 500) == F(3, 250)
    assert 5 + F(3, 250) < 6
    # Joint p+q<cap: a convex quadratic is bounded by its endpoints.
    joint_quadratic = F(1, 2) + 1 / (1 - eps * cap)
    assert joint_quadratic - F(1, 2) > 0
    endpoint_cap = max(joint_quadratic * cap**2, cap - cap**2 / 2)
    joint_remainder_cap = 4 * t_cap + endpoint_cap + eps * cap**2 / 2
    assert joint_remainder_cap < F(47, 100)
    # u in [1/10,1]: 10u-1>=0, -2u^2+10u+1>=9u+1>0.
    assert F(51, 100) + F(47, 100) == F(49, 50) < 1
    assert F(1, 100) + F(47, 100000) == F(1047, 100000)
    shell_error = F(47, 100000)
    shell_caps = [F(28, 125), F(791, 5000), F(323, 2500), F(1119, 10000), F(20003, 200000)]
    for shell_k, u in enumerate(shell_caps, 1):
        assert u / 100 + 1 / (20 * u**2) + shell_error < shell_k
        assert F(1, 100) + F(1, 20) + shell_error < shell_k
    assert shell_caps[0] / 100 + 1 / (20 * shell_caps[0] ** 2) + shell_error == F(9792183, 9800000)
    # Derivative of 20u^2*(5-u/100-shell_error) is positive on [.1,1].
    assert 40 * (5 - shell_error) - F(3, 5) > 0
    eta_square_floor = F(1, 5) * (5 - F(1, 1000) - shell_error)
    assert eta_square_floor == F(499853, 500000) > F(99985, 100000) ** 2
    assert F(999, 1000) < F(99985, 100000)
    assert F(1, 9) + F(81, 200) == F(929, 1800) < F(13, 25)
    assert F(1, 2) + F(1, 50) == F(13, 25)
    assert F(13, 25) + F(47, 100) == F(99, 100) < 1
    assert F(529, 1000) + F(47, 100) + F(1, 2 * 10**12) < 1
    assert 1 + F(47, 100) + F(1, 2 * 10**12) < 2
    print("first contact wall: 1/10<=u<=529/1000 excluded; exact budget verified")
    print("first radius shell: upper u>=28/125 excluded; all five typewise caps verified")
    print(f"joint remainder coefficient: {joint_remainder_cap} < 47/100")
    print(f"uniform contact-error coefficient: {contact_error} < 4")
    print(f"uniform remainder coefficient: {remainder_cap} < 2")


def valuation(value: int, prime: int) -> int:
    assert value > 0
    depth = 0
    while value % prime == 0:
        value //= prime
        depth += 1
    return depth


def check_5adic_contact_depth() -> None:
    units = (1, 2, 3, 4)
    two_unit_squares = {(a * a + b * b) % 5 for a in units for b in units}
    assert two_unit_squares == {0, 2, 3}
    assert two_unit_squares.isdisjoint({1, 4})
    # The exponent inequality is unbounded in the proof; this is a grid check.
    for r in range(1, 25):
        g, k = 3 * r + 2, 2 * r + 2
        assert 5 ** (3 * r + 3) > 10**r
        assert 2 * k + r >= 5 * r + 4 > 3 * r + 3
        power = 1
        while power * 5 < 10**r:
            power *= 5
        for w in (1, 10**r - 1, power):
            assert valuation(10 ** (2 * k + r) - w, 5) == valuation(w, 5)
            assert valuation(w, 5) < g + 1
    # Equality at the upper depth retains a minus-sign resonance:
    # B = -(A+B), i.e. A+2B=0; A+B=-B is a unit.
    for a in units:
        admitted = [b for b in units if (a + 2 * b) % 5 == 0]
        assert len(admitted) == 1
        assert (a + admitted[0]) % 5 != 0
        assert not any((b - (a + b)) % 5 == 0 for b in units)
    for g in range(1, 25):
        for d5 in range(1, 25):
            for n3 in range(1, 49):
                m3 = n3 + g
                if not d5 < m3:
                    continue
                first_depth, second_depth, lhs_depth = d5 + n3, m3, 3 * d5
                if d5 < g:
                    assert first_depth < second_depth
                    assert (lhs_depth == first_depth) == (n3 == 2 * d5)
                elif d5 > g:
                    assert second_depth < first_depth
                    assert (lhs_depth == second_depth) == (m3 == 3 * d5)
                else:
                    assert first_depth == second_depth
                    assert (lhs_depth >= first_depth) == (n3 <= 2 * g)
                    if n3 <= 2 * g:
                        assert lhs_depth - first_depth == 2 * g - n3
    print("5-adic actual gap: n3=2d5 / m3=3d5 / balanced cancellation shapes verified")
    print("5-adic contact endpoint: e3<=nu excluded; upper equality resonance retained")


def check_2adic_contact_depth() -> None:
    assert F(2**39, 10**12) > F(267, 500)
    for r in range(1, 25):
        k = 2 * r + 2
        bound = (267 * 10**r - 1) // 500
        power = 1
        while power * 2 <= bound:
            power *= 2
        for w in (1, bound, power):
            assert valuation(10 ** (2 * k + r) - w, 2) == valuation(w, 2)
        if r <= 12:
            assert 2 ** (3 * r + 3) > F(267, 500) * 10**r
    for odd1 in (1, 3, 5, 7):
        for odd2 in (1, 3, 5, 7):
            assert (odd1**2 - odd2**2) % 8 == 0
            assert (odd1**2 + odd2**2) % 4 == 2
    for a in (1, 3, 5, 7):
        for b in (1, 3, 5, 7):
            assert (a + b) % 2 == 0  # equal-depth beta cancellation
    for g in range(1, 25):
        for d2 in range(2, 25):
            for n3 in range(3, 49):
                m3 = n3 + g
                if d2 >= m3:
                    continue
                if d2 < g:
                    assert (n3 + 1 == 2 * d2) == (n3 == 2 * d2 - 1)
                elif d2 == g:
                    assert (n3 <= 2 * d2 - 1) == (n3 <= 2 * g - 1)
                elif m3 - d2 >= 2:
                    assert (m3 - d2 + 1 == 2 * d2) == (m3 == 3 * d2 - 1)
                else:
                    assert d2 == m3 - 1
            for d5 in range(1, 25):
                if d2 < g and d5 < g:
                    assert 2 * d2 - 1 != 2 * d5
                if d2 > g and d5 > g:
                    assert 3 * d2 - 1 != 3 * d5
    for g in range(1, 17):
        for d2 in range(2, 17):
            for d5 in range(1, 17):
                for n3 in range(3, 33):
                    m3 = g + n3
                    if d2 >= m3 - 1 or d5 >= m3:
                        continue
                    shape2 = n3 == 2 * d2 - 1 if d2 < g else n3 <= 2 * g - 1 if d2 == g else m3 == 3 * d2 - 1
                    shape5 = n3 == 2 * d5 if d5 < g else n3 <= 2 * g if d5 == g else m3 == 3 * d5
                    if shape2 and shape5:
                        assert d2 <= g and d5 <= g and max(d2, d5) == g
    assert F(47, 100) + F(1, 2 * 10**9) < 1
    for r in range(1, 9):
        for g in range(3 * r + 2, 65):
            for nu in range(g + 1, 2 * g - 3 * r):
                scale = nu + 3 * r + 1 - 2 * g
                assert scale <= 0
                for d in range(1, g):
                    gap = g - d
                    a2, b2 = max(2 * d - nu, 0), max(g + d - nu, 0)
                    assert scale + a2 == max(scale, 3 * r + 1 - 2 * gap)
                    assert scale + b2 == max(scale, 3 * r + 1 - gap)
                    if gap >= 3 * r + 1:
                        assert scale + a2 <= 0 and scale + b2 <= 0
                        if b2 > 0:
                            assert nu + r + 1 - 4 * g + b2 == r + 1 - 2 * g - gap <= -9
                    a5, b5 = max(g + d - 1 - nu, 0), max(2 * d - 1 - nu, 0)
                    assert scale + a5 == max(scale, 3 * r - gap)
                    assert scale + b5 == max(scale, 3 * r - 2 * gap)
                    if gap >= 3 * r:
                        assert scale + a5 <= 0 and scale + b5 <= 0
                        if a5 > 0:
                            assert nu + r + 1 - 4 * g + a5 == r - 2 * g - gap <= -9
                for n3 in range(nu + 1, 2 * g):
                    c = 2 * g - n3
                    assert scale + n3 - nu == 3 * r + 1 - c
                    assert nu + r + 1 - 4 * g + n3 - nu == r + 1 - 2 * g - c <= -9
    print("regular high sectors excluded; balanced relative-gap decimal-grid bounds verified")
    print("2-adic shallower-first endpoint: depth bounds and double-low / regular double-high exclusions verified")


def check_general_2adic_and_5beta() -> None:
    for r in range(1, 25):
        assert 6 * r + 6 > 4 * r
    # Two normalized odd squares add to valuation exactly one.
    for a in (1, 3, 5, 7):
        for b in (1, 3, 5, 7):
            assert (a * a + b * b) % 4 == 2
    for t in range(-8, 9):
        for d2 in range(max(2, t + 2), 25):
            sphere_depth = 2 * d2 if t < 0 else 2 * d2 + 1 if t == 0 else 2 * (d2 - t)
            low_word_height = sphere_depth - 1
            if t != 0:
                assert low_word_height % 2 == 1
            else:
                assert low_word_height == 2 * d2
            high_word_height = d2 + sphere_depth - 1
            if t < 0:
                assert high_word_height % 3 == 2
            elif t == 0:
                assert high_word_height == 3 * d2
            else:
                assert (high_word_height % 3 == 0) == (t % 3 == 1)
    assert F(5, 2)**9 > 2000
    assert 5**15 > 2**34 and 5**69 > 2**158
    assert 2**10 > 10**3 and 2**500 < 10**151
    log_two_cap = F(151, 500)
    coefficient = F(11, 3) * log_two_cap * (2 - log_two_cap)
    assert coefficient == F(470063, 250000) < 2
    assert 3 - 26 * (2 - coefficient) == -F(14181, 125000)
    assert F(49, 100) - 6 * (2 - coefficient) == -F(28561, 125000)
    assert 1 - 26 * (4 - coefficient) == -F(6764181, 125000)
    assert F(49, 100) - 6 * (4 - coefficient) == -F(1528561, 125000)
    assert -F(6764181 + 1528561, 125000) < -9
    assert F(1) + log_two_cap == F(1953, 1500)
    assert F(11, 3) * log_two_cap - 1 == F(161, 1500)
    assert F(1953, 161) > 12
    for g in range(5, 65):
        for d2 in range(g + 1, 3 * g):
            # Avoid fractional exponents: raise BP to the sixth power.
            ratio_num = 5 ** (6 * (3 * d2 - g - 1))
            ratio_den = 2 ** (6 * (2 * d2 - 2)) * 10 ** (12 * g)
            if 6 * d2 >= 11 * g:
                assert ratio_num > ratio_den
    print("5-beta under 2S: exact cross-prime height gives 13<=g<26r+6 and d2<11g/6")
    for g in range(5, 49):
        assert F(400**g, 16) + 1 < 400**g
        assert 2 ** (2 * g - 1) < 10 ** (g + 1)
        for nu in range(g + 1, 2 * g - 3):
            assert 2**nu <= F(2 ** (2 * g), 16)
            assert 2**nu * 10 ** (2 * g) + F(2, 5**nu) < 400**g
            for n3 in range(1, 2 * g + 1):
                m3 = n3 + g
                assert F(2**m3, 5**nu) < 5**n3
    assert F(47, 100) * 2 + F(1, 2 * 10**8) < 1
    assert 25**6 > 10**8
    assert F(529, 500) > 1
    for r in range(1, 13):
        for delta in range(1, 3 * r + 1):
            max_h = 9 * r + 1 - 3 * delta
            assert max_h == 3 * (3 * r + 1 - delta) - 2
            assert 12 * r + 5 + 4 * max_h - 3 * delta == 48 * r + 9 - 15 * delta
            assert 48 * r + 9 - 15 * delta <= 48 * r - 6
        for c in range(3 * r + 1):
            max_h = 9 * r + 1 - 3 * c
            assert 12 * r + 5 + 4 * max_h - 3 * c == 48 * r + 9 - 15 * c
            assert 48 * r + 9 - 15 * c <= 48 * r + 9
    for r in range(1, 9):
        for g in range(3 * r + 2, 65):
            for nu in range(g + 1, 2 * g - 3 * r):
                h = 2 * g - 3 * r - 1 - nu
                assert h >= 0
                for d5 in range(1, g):
                    delta = g - d5
                    b = g + d5 - nu
                    assert b == 3 * r + 1 + h - delta
                    assert nu + r + 1 - 4 * g + b == r + 1 - 2 * g - delta <= -9
                    assert nu + 3 * (2 * g - r) + 2 <= 8 * g - 6 * r + 1
                for n3 in range(3, 2 * g + 1):
                    c = 2 * g - n3
                    b = n3 - nu
                    assert b == 3 * r + 1 + h - c
                    assert nu + r + 1 - 4 * g + b == r + 1 - 2 * g - c <= -8
    print("2-near-beta low/balanced boxes and non-2S low-balanced decimal recovery verified")
    print("general first-2-depth split verified; 5-beta exact cancellation and m3<9g bound checked")


def check_phase_compatibility_boundary() -> None:
    # A reduced real decimal tail fits every necessary phase inequality.
    # The full exact-lift equation still fails; this is NOT a counterexample.
    a3, b3 = 5591, 12511
    u, eta, psi = F(b3, 100000), F(a3, 10000), F(a3, b3)
    assert gcd(a3, b3) == 1
    assert len(str(a3)) == 4 and len(str(b3)) == 5
    assert F(1, 10) <= u < F(28, 125) and F(1, 10) <= eta < 1
    remainder = 1 - u / 100 - 5 * psi**2
    assert F(13, 200000) < remainder < F(47, 100000)
    a1, b1, a2, b2 = 10**13 + 11310, 10**11 - 287, 10**9 - 1, 1000
    assert gcd(a1, b1) == gcd(a2, b2) == 1
    assert len(str(a1)) - len(str(b1)) == 3
    assert len(str(a2)) - len(str(b2)) == 5
    # g=1,k=4,r=3,s=1,N=5,t=1/10000,H=10.
    joint_integer = 10**5 * (F(40010, 10**5) + F(1, 10) - F(1, 2) - F(1, 10000) + F(1, 100000))
    assert joint_integer == 1
    alpha = a1 * 10**13 + a2 * 10**4 + a3
    beta = b1 * 10**9 + b2 * 10**5 + b3
    ratios = [F(a1, b1), F(a2, b2), F(a3, b3)]
    assert F(alpha, beta) ** 2 != sum(ratio**2 for ratio in ratios)
    print("reduced decimal phase-compatible point verified; full exact-lift equation fails")

    # Contact endpoint: the common mod-9 filter and next mod-27 square
    # congruence both allow a class. No exact-lift existence is claimed.
    a1, b1 = 10**15, 10**9 - 3
    a2, b2, a3, b3 = 10**16 - 20999991, 10**6, 1, 599974
    assert gcd(a1, b1) == gcd(a2, b2) == gcd(a3, b3) == 1
    assert (b1 % 9, b2 % 9, b3 % 9) == (7, 1, 7)
    assert (b1**2 + b2**2 + b3**2) % 9 == 0
    assert b3 % 9 == (3 + 4) % 9
    assert 20999991 % 9 == (6 - 0 - 3) % 9
    assert len(str(a1)) - len(str(b1)) == 7
    assert len(str(a2)) - len(str(b2)) == 9
    assert len(str(a3)) == 1 and len(str(b3)) == 6
    assert 10 * (3000000 + 1) + 20999991 - 5 * 10**7 - 10**6 == 1
    u, psi = F(b3, 10**6), F(10**4 * a3, b3)
    assert F(529, 1000) < u < 1
    phase_remainder = 1 - u - F(1, 2 * 10**12) * psi**2
    assert F(13, 200) < phase_remainder < F(47, 100)
    alpha = a1 * 10**17 + a2 * 10 + a3
    beta = b1 * 10**13 + b2 * 10**6 + b3
    full_r, ratios = F(alpha, beta), [F(a1, b1), F(a2, b2), F(a3, b3)]
    mod_27_r = full_r.numerator * pow(full_r.denominator, -1, 27) % 27
    mod_27_ratios = [ratio.numerator * pow(ratio.denominator, -1, 27) % 27 for ratio in ratios]
    assert mod_27_r == 0 and mod_27_ratios == [13, 25, 4]
    assert sum(ratio**2 for ratio in mod_27_ratios) % 27 == 0
    assert full_r**2 != sum(ratio**2 for ratio in ratios)
    assert valuation(b3, 5) == 0 < 6
    print("contact endpoint: mod-9/mod-27 class passes, then the new 5-depth rule excludes it")


def stable(g: int, k: int, r: int, s: int) -> bool:
    n = max(r + g + 1, s)
    return (
        k + s >= 2 * g + 2
        and k + r >= g + 1
        and n <= 4 * g
        and n <= 2 * k
    )


def check_regions() -> None:
    stable_count = interior_count = original_count = added_count = 0
    for g in range(1, 25):
        for k in range(1, 25):
            for r in range(1, 25):
                for s in range(1, 25):
                    n = max(r + g + 1, s)
                    contact_exponent = n - r - k + g - s
                    assert contact_exponent == max(2 * g + 1 - k - s, g - r - k)
                    assert (contact_exponent <= -1) == (
                        k + s >= 2 * g + 2 and k + r >= g + 1
                    )
                    if k >= 2 * g + 1 and r <= 3 * g - 1 and s <= 4 * g:
                        assert stable(g, k, r, s)
                    if k >= 2 * g and s >= 2 and r <= 3 * g - 1 and s <= 4 * g:
                        assert stable(g, k, r, s)
                    if k + r == g and k + s >= 2 * g + 2 and n <= 2 * k:
                        assert s >= g + r + 2 and n == s
                        assert g >= 3 * r + 2 and g + r >= 6
                        assert n - 4 * g <= -2 * (g + r) <= -12
                        assert k >= 4 and contact_exponent == 0
                        assert s <= k + g and s - r - g - 1 >= 1
                        nu = s - r - 1
                        assert nu >= g + 1 >= 3 * r + 3
                        assert 5**nu > 10**r and 2 * k + r > 3 * r + 3
                        assert k - g + s - 1 == n - r - 1
                        assert 10 ** (s - r - g - 1) % 10 == 0
                        assert (10**n // 2) % 10 == 0 and 10 ** (n - r - 1) % 10 == 0
                    if k + r == g and g >= 3 * r + 2 and g + r + 2 <= s <= 2 * g - 2 * r:
                        assert n == s and k >= 2
                        assert k + s >= 2 * g + 2 and n <= min(4 * g, 2 * k)
                        assert contact_exponent == 0
                        assert not stable(g, k, r, s)
                    if k >= 2 * g + 2 and n == 4 * g + 1:
                        assert k + s >= 2 * g + 2
                        assert contact_exponent <= -2 and n - 2 * k <= -3
                    if not stable(g, k, r, s):
                        continue
                    stable_count += 1
                    interior_count += r >= 2 and s >= 2
                    original_count += n <= 2 * k - 1
                    added_count += n == 2 * k
                    assert k >= 2 and k - g + s >= 1
                    assert contact_exponent <= -1 and n - 4 * g <= 0
                    assert n - 2 * k <= 0
    assert original_count == 69417
    assert stable_count == original_count + added_count
    assert stable(1, 2, 2, 2) and max(2 + 1 + 1, 2) == 2 * 2
    print(f"regression grid 1..24: {stable_count} stable tuples, {interior_count} interior")
    print(f"original region: {original_count}; newly covered N=2k tuples: {added_count}")

    # Failure of the old estimate, NOT an exact-lift counterexample.
    g, k, r, s = 10, 8, 1, 14
    n = max(g + 2, s)
    assert k + s >= 2 * g + 2 and n <= 4 * g and n <= 2 * k - 2
    assert not stable(g, k, r, s)
    h, rho, b2 = 10**g, F(10**g, 2), 10 ** (k - g + s - 1)
    contact_phase = 10 ** (n - r - 1) * rho / (h * b2)
    assert contact_phase == 5
    print("old missing-condition witness (g,k,r,s)=(10,8,1,14): contact phase = 5")


def main() -> None:
    check_algebra()
    check_uniform_constants()
    check_regions()
    check_phase_compatibility_boundary()
    check_5adic_contact_depth()
    check_2adic_contact_depth()
    check_general_2adic_and_5beta()
    print("PASS: symbolic identities, exact constants, region regressions")
    print("No enumeration of exact-lift candidates; unbounded coverage is in the proof.")


if __name__ == "__main__":
    main()
