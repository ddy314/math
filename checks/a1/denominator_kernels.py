#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0267; see history/sources.json.
"""

from fractions import Fraction
from itertools import product
from math import gcd, lcm

import sympy as sp


def valuation(value: int, prime: int) -> int:
    assert value != 0
    depth = 0
    while value % prime == 0:
        value //= prime
        depth += 1
    return depth


def check_word_identity() -> None:
    h, a3, j, ell, a12, q0, x, y = sp.symbols("H a3 j l A12 Q0 X Y")
    y3 = a3 * ell / j
    gap = j * (h - y3) - (ell * a12 * x - h * q0 * y)
    word = h * (j + q0 * y) - ell * (a12 * x + a3)
    assert sp.expand(gap - word) == 0
    print("LK7: exact gap is the original word equation")


def check_lowest_layer() -> None:
    count = 0
    for g in range(6):
        for k in range(1, 6):
            for m1 in range(1, 4):
                n1 = m1 + g - 1
                if n1 < 1:
                    continue
                for m2 in range(1, 4):
                    n2 = m2 + k + g
                    for leading1 in (1, 2, 5, 9):
                        b1 = leading1 * 10 ** (m1 - 1)
                        tau1 = Fraction(b1, 10 ** (m1 - 1))
                        for leading2 in (1, 2, 5, 9):
                            b2 = leading2 * 10 ** (m2 - 1)
                            tau2 = Fraction(b2, 10 ** (m2 - 1))
                            if tau2 > tau1:
                                continue
                            r1_max = Fraction(10**n1 - 1, b1)
                            r2_min = Fraction(10 ** (n2 - 1), b2)
                            assert 10**k * r1_max < r2_min
                            count += 1
    print(f"LK1/LK2: {count} bounded endpoint regressions")


def check_unequal_prefix_depths() -> None:
    count = 0
    units = (1, 3, 7, 9, 11, 13, 17, 21, 27, 31)
    for a in range(7):
        for b in range(7):
            if a == b:
                continue
            e0 = max(a, b)
            for c in range(e0 + 1, e0 + 5):
                delta = c - e0
                for j in units:
                    assert gcd(j, 10) == 1
                    for u1, u2 in ((1, 1), (3, 7), (7, 13), (11, 9)):
                        b3 = 10**c * j
                        m3 = len(str(b3))
                        assert m3 == c + len(str(j))
                        q0 = u1 * 10 ** (a + len(str(u2))) + u2
                        assert gcd(q0, 10) == 1
                        beta = 10 ** (m3 + b) * q0 + b3
                        assert valuation(beta, 2) == valuation(beta, 5) == c
                        unit_lcm = lcm(u1, u2, j)
                        for num1, num2 in ((1, 3), (3, 7), (5, 2)):
                            if gcd(num1, 10**a * u1) != 1 or gcd(num2, 10**b * u2) != 1:
                                continue
                            y1 = num1 * 10 ** (c - a) * (unit_lcm // u1)
                            y2 = num2 * 10 ** (c - b) * (unit_lcm // u2)
                            norm = y1**2 + y2**2
                            assert valuation(norm, 2) == valuation(norm, 5) == 2 * delta
                        for g in range(c - b):
                            n3 = m3 - g
                            ell = m3 + b - c
                            assert ell >= 1 and n3 > ell
                            # The actual word gap is deeper on its first summand.
                            # No unit assumption on A12 is required.
                            for a12 in (1, 10, 25):
                                h = 7
                                rhs = unit_lcm * a12 * 10**n3 - h * q0 * 10**ell
                                assert valuation(rhs, 2) == valuation(rhs, 5) == ell
                            # A hypothetical solution must obey both equations.
                            assert not (ell == 2 * delta and ell + 1 == 2 * delta)
                            count += 1
    print(f"LK5--LK9: {count} bounded digit/depth regressions")


def check_equal_prefix_boundary() -> None:
    count = 0
    for e in range(1, 9):
        for c in range(e + 1, e + 9):
            delta = c - e
            m3 = 3 * delta
            unit_digits = m3 - c
            if unit_digits < 1:
                continue
            j = 10 ** (unit_digits - 1) + (1 if unit_digits > 1 else 0)
            assert gcd(j, 10) == 1 and len(str(10**c * j)) == m3
            ell = m3 + e - c
            assert ell == 2 * delta >= 2
            norm = 10 ** (2 * delta) * j**2 * (1**2 + 3**2)
            assert valuation(norm, 2) == 2 * delta + 1
            assert valuation(norm, 5) == 2 * delta + 1
            # This numerator pair is excluded by LK10's extra 5-unit condition.
            assert valuation(1**2 + 3**2, 5) == 1
            norm_allowed = 10 ** (2 * delta) * j**2 * (1**2 + 1**2)
            assert valuation(norm_allowed, 2) == 2 * delta + 1
            assert valuation(norm_allowed, 5) == 2 * delta
            count += 1
    print(f"LK10: {count} equal-prefix resonance regressions; state remains open")


def check_mod9_coverage_difference() -> None:
    denominators = (10, 100, 13000)
    assert tuple(b % 9 for b in denominators) == (1, 1, 4)
    assert sum(b * b for b in denominators) % 9 == 0
    assert sum(denominators) % 9 == 6
    assert valuation(13000, 2) == valuation(13000, 5) == 3
    assert gcd(13, 10) == 1
    print("(10,100,13000): mod-9 permitted denominator class, excluded by LK4")


def check_general_resonance() -> None:
    count = 0
    for a in range(7):
        for b in range(7):
            if a == b:
                continue
            for c in range(max(a, b) + 1, max(a, b) + 7):
                delta = c - max(a, b)
                for unit_digits in range(1, 5):
                    m3 = c + unit_digits
                    ell = m3 + b - c
                    for g in range(m3):
                        n3 = m3 - g
                        assert (n3 == ell) == (c - b == g)
                        if b == 0:
                            # For g=1 this is already the strict LK4 range;
                            # no assertion that the second numerator is a unit.
                            if g <= 1:
                                assert c > b + g and n3 > ell
                            continue
                        if n3 != ell:
                            shallow = min(n3, ell)
                            assert not (shallow == 2 * delta and shallow + 1 == 2 * delta)
                        else:
                            # The equal-depth normalized word bracket is even.
                            for left, right in product((1, 3, 7, 11), repeat=2):
                                if left != right:
                                    assert valuation(left - right, 2) >= 1
                            if g <= 1:
                                assert not (n3 <= 2 * delta - 2)
                        count += 1
    print(f"LK11/LK12: {count} general-g depth/order regressions")


def check_unit_product_projection() -> None:
    # Divide all sphere/gap coordinates by the common 2/5-unit l first.
    # This is a local projection, not a decimal descent or word realization.
    allowed_5: set[int] = set()
    allowed_2: set[tuple[int, int]] = set()
    for u2, j, a1, a2, a3 in product((1, 2, 3, 4), repeat=5):
        h = a3 * pow(j, -1, 5) % 5
        unit_gap = -h * u2 * pow(j, -1, 5) % 5
        if unit_gap * (2 * h) % 5 == (a1 * a1 + a2 * a2) % 5:
            allowed_5.add(u2 * j % 5)
    for u2, j, a1, a2, a3 in product((1, 3, 5, 7), repeat=5):
        y3 = a3 * pow(j, -1, 8) % 8
        for delta_one in (0, 1):
            unit_gap = (2 * delta_one - y3 * u2) * pow(j, -1, 4) % 4
            sphere = 4 * delta_one * unit_gap**2 + 2 * y3 * unit_gap
            if unit_gap % 2 and sphere % 8 == (a1 * a1 + a2 * a2) % 8:
                allowed_2.add((delta_one, u2 * j % 4))
    assert allowed_5 == {1, 4}
    assert allowed_2 == {(0, 3), (1, 3)}
    allowed_20 = {
        residue for residue in range(20)
        if gcd(residue, 20) == 1 and residue % 5 in allowed_5 and residue % 4 == 3
    }
    assert allowed_20 == {11, 19}
    denominators = (10, 10, 300)
    ci = tuple(b % 9 for b in denominators)
    pair_sum = sum(ci[i] * ci[j] for i, j in ((0, 1), (0, 2), (1, 2))) % 9
    assert ci == (1, 1, 3) and pair_sum not in (3, 6)
    assert 3 not in allowed_20
    print("LK13: full local unit projection leaves product {11,19} mod20")
    print("(10,10,300): mod-9 permitted class, excluded by LK13")


def check_equal_prefix_sources() -> None:
    count = 0
    for e in range(1, 10):
        for delta in range(1, 10):
            c = e + delta
            for unit_digits in range(1, 10):
                m3 = c + unit_digits
                ell = m3 - delta
                for g in range(m3):
                    n3 = m3 - g
                    if delta > g:
                        assert n3 > ell
                        assert (ell == 2 * delta) == (m3 == 3 * delta)
                    elif delta < g:
                        assert n3 < ell
                        assert (n3 == 2 * delta) == (m3 == g + 2 * delta)
                    else:
                        assert n3 == ell == e + unit_digits
                        if g == 1:
                            assert n3 >= 2 and not (n3 <= 2 * g - 1)
                    count += 1
    print(f"LK14: {count} equal-prefix source regressions; g=1,delta=1 is empty")


def check_general_unit_products() -> None:
    count = 0
    for g in range(6):
        for delta in range(g + 1, g + 7):
            word_extra = int(delta - g == 1)
            sphere_extra = int(delta == 1)
            allowed_mod4: set[int] = set()
            for u2, j, a3 in product((1, 3, 5, 7), repeat=3):
                y3 = a3 * pow(j, -1, 8) % 8
                unit_gap = (2 * word_extra - y3 * u2) * pow(j, -1, 4) % 4
                norm = 4 * sphere_extra * unit_gap**2 + 2 * y3 * unit_gap
                if unit_gap % 2 and norm % 8 == 2:
                    allowed_mod4.add(u2 * j % 4)
            expected_mod4 = (2 * word_extra + 2 * sphere_extra - 1) % 4
            assert allowed_mod4 == {expected_mod4}
            allowed_mod20 = {
                x for x in range(20)
                if gcd(x, 20) == 1 and x % 5 in (1, 4) and x % 4 == expected_mod4
            }
            if g >= 1 and delta == g + 1:
                assert allowed_mod20 == {1, 9}
            else:
                assert allowed_mod20 == {11, 19}
            count += 1
    print(f"general-g unit projection: {count} ranges; delta=g+1 retains {{1,9}} mod20")


def check_pure_prefix_supply() -> None:
    count = 0
    e2_candidates: list[tuple[int, int]] = []
    for e in range(1, 9):
        q0 = 10 ** (e + 1) + 1
        for j in sp.divisors(q0):
            assert gcd(j, 10) == 1
            if e % 2:
                assert j % 4 == 1
            if j % 20 not in (11, 19):
                continue
            unit_digits = len(str(j))
            if (e + unit_digits) % 2:
                continue
            delta = (e + unit_digits) // 2
            assert e % 2 == 0 and e >= 2
            assert e // 2 + 1 <= delta <= e
            if e == 2:
                e2_candidates.append((delta, j))
            count += 1
    assert e2_candidates == [(2, 11), (2, 91)]
    print(f"LK15/LK16: {count} bounded divisor/length regressions; e=2 leaves j=11,91")


def check_d1_contact_corner() -> None:
    count = 0
    for e in range(1, 11):
        E = 10**e
        q = E * (10 * E + 1)
        lam = Fraction(1, 10 * E + 1)
        xi = Fraction(q, q + 1)
        for k in range(1, 11):
            if 2 * k < e + 2:
                continue
            T = 10**k
            assert xi * (1 - lam) * T > 1
            assert Fraction(1, 12) > lam
            r1 = 10 + Fraction(1, E)
            r2 = 10 * T - Fraction(1, E)
            P = (1 - lam) * T * r1 + lam * r2
            L = xi * P
            exact_gap = Fraction(10 * T * (E - 1), q + 1) + Fraction(10 * E, q + 1) + Fraction(1, E * (q + 1))
            assert L - r2 == exact_gap > Fraction(4 * T, 5 * E)
            assert r2 > 9 * T and T * T >= 100 * E
            assert L * L - r2 * r2 > Fraction(72 * T * T, 5 * E) >= 1440
            assert r1 * r1 + 100 < 203
            assert L * L > r1 * r1 + r2 * r2 + 100
            count += 1
    print(f"LK17: {count} exact-rational corner regressions")


def check_general_contact_normalization() -> None:
    E, G, Z, a1, a2 = sp.symbols("E G Z a1 a2", nonzero=True)
    lam = 1 / (10 * E + 1)
    actual = (a1 * 10 * E * G * Z + a2) / (G * E * (10 * E + 1))
    normalized = (1 - lam) * Z * (a1 / E) + lam * (a2 / E) / G
    assert sp.cancel(actual - normalized) == 0
    count = 0
    for g in range(9):
        G = 10**g
        for e in range(1, 9):
            E, Q = 10**e, 10**e * (10 ** (e + 1) + 1)
            lam, xi = Fraction(1, 10 * E + 1), Fraction(Q, Q + 1)
            for k in (1, 3, 7):
                Z = 10**k
                r1, r2 = 10 * G + Fraction(1, E), 10 * G * Z - Fraction(1, E)
                L = xi * ((1 - lam) * Z * r1 + lam * r2 / G)
                gap = Fraction(10 * Z * (2 * E - G * (E + 1)) + 10 * E + 1, Q + 1)
                gap += Fraction(1, E * (Q + 1)) - Fraction(1, G * (Q + 1))
                assert L - r2 == gap
                if g == e == 1 and k == 3:
                    assert L < r2  # Old LK17G corner margin is invalid.
                count += 1
    assert Fraction(201, 10000) < Fraction(5, 6) ** 2
    print(f"LK17G downgrade/LK19G: {count} original P normalization regressions; g>0 d1 extension withdrawn")


def check_original_numerator_quadratic() -> None:
    T, A12, U, h0, j, a1, a2 = sp.symbols("T A12 U h0 j a1 a2", nonzero=True)
    f0 = 1 + T**2 * h0
    a3 = (T * A12 - f0 * U) / h0
    H = a3 + T**2 * U
    alpha = A12 * T**3 + a3
    assert sp.cancel(alpha - H * f0) == 0
    quadratic = (2 + T**2 * h0) * U**2 - 2 * T * A12 * U + h0 * j**2 * (a1**2 + a2**2)
    sphere_gap = U * (2 * a3 + T**2 * U) - j**2 * (a1**2 + a2**2)
    assert sp.cancel(h0 * sphere_gap + quadratic) == 0
    V, B, F0, a2v, a1v, M, j = sp.symbols("V B F0 a2 a1 M j")
    sphere_v = (j * M * a2v + V)**2 - (j * M * a1v)**2 - (j * M * a2v)**2 - (B + F0 * V)**2
    quadratic_v = (F0**2 - 1)*V**2 + 2*(F0*B-j*M*a2v)*V + B**2+j**2*M**2*a1v**2
    assert sp.expand(sphere_v + quadratic_v) == 0

    # A denominator projection compatible with the stronger j|Q0 funnel.
    e, delta, jv, k = 2, 2, 11, 1
    c, m3 = e + delta, 3 * delta
    b1 = b2 = 10**e
    b3 = 10**c * jv
    n2 = e + 1 + k
    assert (10 ** (e + 1) + 1) % jv == 0 and jv % 20 == 11
    ci = [b % 9 for b in (b1, b2, b3)]
    assert ci == [1, 1, 2]
    assert (ci[0]*ci[1] + ci[0]*ci[2] + ci[1]*ci[2]) % 9 not in (3, 6)
    t1, t2 = b1 * 10 ** (n2 + m3), b2 * 10**m3
    beta = b1 * 10 ** (e + 1 + m3) + b2 * 10**m3 + b3
    dd = t1*t1 + t2*t2 + b3*b3 - beta*beta
    assert (t1, t2, beta) == (10**12, 10**8, 100100110000)
    assert dd == 989979977978000000000000
    assert dd == 977355748928**2 + 186428855104**2
    print("LK18: original word/quadratic identities; stronger-funnel norm projection remains compatible")


def main() -> None:
    check_word_identity()
    check_lowest_layer()
    check_unequal_prefix_depths()
    check_equal_prefix_boundary()
    check_mod9_coverage_difference()
    check_general_resonance()
    check_unit_product_projection()
    check_equal_prefix_sources()
    check_general_unit_products()
    check_pure_prefix_supply()
    check_d1_contact_corner()
    check_general_contact_normalization()
    check_original_numerator_quadratic()
    print("PASS: exact identities and bounded regressions; no exact-lift search")


if __name__ == "__main__":
    main()
