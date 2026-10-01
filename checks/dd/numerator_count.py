#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0591; see history/sources.json.
"""

from __future__ import annotations

from math import gcd, log10

import sympy as sp


def symbolic_uv2_sharp() -> None:
    a = sp.symbols("a", positive=True)
    b = 1 - a
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q2, n2, q5, g5, n5, rough, g2 = sp.symbols(
        "Q2 N2 Q5 G5 N5 R G2", nonnegative=True
    )

    u_dev = (
        2 * b * mu / 3
        - a * g2
        - 2 * b * q5 / 3
        - b * g5 / 3
        - b * n5 / 3
        - rough
    )
    v_dev = -a * g2 - b * g5 - rough
    m1 = (
        delta / 2
        - (1 - b / 3) * mu
        - b * q5 / 3
        + b * g5 / 3
        - b * n5 / 6
        + rough / 2
    )

    # log(U v2) - (1+U*) >= u_dev + v_dev - m1.
    expr = sp.expand(u_dev + v_dev - m1)

    # a*G2 <= m1 + a*Q2.
    expr = sp.expand(expr.subs(g2, (m1 + a * q2) / a))
    target = sp.expand(
        -3 * delta / 2
        + (3 - b / 3) * mu
        - 2 * a * q2
        + b * q5 / 3
        - 7 * b * g5 / 3
        + b * n5 / 6
        - 7 * rough / 2
    )
    assert sp.simplify(expr - target) == 0


def budget_coefficients() -> None:
    a = log10(2)
    b = 1 - a
    A = 2 * (1 + 2 * a) / 3
    eta = (3 - b / 3) / A

    assert abs(eta - 2.590736314681693) < 1e-12
    assert eta > 7 / 4

    coeffs = {
        "sigma": eta,
        "Q2": 2 * a * (eta - 1),
        "N2": a * eta,
        "Q5": b * (2 * eta + 1) / 3,
        "G5": b * (4 * eta - 7) / 3,
        "N5": b * (2 * eta + 1) / 6,
        "R": 2 * eta - 7 / 2,
    }
    assert all(value > 0 for value in coeffs.values())


def thresholds() -> None:
    a = log10(2)
    u_star = 0.691116422381969
    z_star = 1 - u_star
    kappa_dig = (2 + a) / 3

    delta_uv = 2 * u_star / 3
    delta_a2 = 1 / (1 + kappa_dig)
    delta_qv = 2 * z_star / 3

    assert abs(delta_uv - 0.460744281587979) < 1e-12
    assert abs(delta_a2 - 0.565927754125872) < 1e-12
    assert abs(delta_qv - 0.205922385078687) < 1e-12

    assert delta_qv < delta_uv < 0.5 < delta_a2

    # gap determinant: v2 height 1-delta beats delta-height determinant iff delta<1/2.
    for delta in (0.0, 0.1, 0.3, 0.49):
        assert 1 - delta > delta
    assert not (1 - 0.5 > 0.5)


def ordinary_gap_full_word_dictionary() -> None:
    U, V, F, B, xi, c3, A12, a3, a, decimal = sp.symbols(
        "U V F B xi c3 A12 a3 a decimal", positive=True
    )
    u, d0, L, omega = 2 * F * U, U * xi, 2 * F / xi, B * xi
    Sigma = u + V
    fraction = a / (xi * c3)
    elimination = c3 * (V * omega * A12 * decimal - d0 * a3) - (u + V) * a
    carry_residual = B * V * A12 * decimal - U * a3 - Sigma * fraction
    assert sp.simplify(elimination / (xi * c3) - carry_residual) == 0

    # Full-word residual equals the normalized gap residual, with no extra
    # polynomial parent left after H-y3=L*a and the actual block lengths.
    Q, tau = sp.symbols("Q tau", positive=True)
    b3 = omega * tau
    q_lcm = b3 * c3
    H = a3 * c3 + L * a
    power_m = omega * L
    word_a = A12 * power_m * decimal + a3
    word_b = Q * power_m + b3
    normalized = q_lcm * A12 * decimal - Q * H - tau * a
    assert sp.simplify(q_lcm * word_a - H * word_b - power_m * normalized) == 0

    # An ordinary/primitive gap ratio toy; no sphere is claimed here.
    gap, xi_value, c3_value = 110, 10, 63
    common = gcd(gap, xi_value * c3_value)
    R0, g0 = gap // common, xi_value * c3_value // common
    assert (R0, g0) == (11, 63)
    assert gcd(R0, g0) == gcd(R0 * g0, 10) == 1
    assert R0 * xi_value * c3_value == g0 * gap


def lift_minus_one_root(p: int, h: int) -> int:
    root = next(x for x in range(p) if (x * x + 1) % p == 0)
    modulus = p
    for _ in range(1, h):
        root = next(root + k * modulus for k in range(p) if ((root + k * modulus) ** 2 + 1) % (modulus * p) == 0)
        modulus *= p
    assert (root * root + 1) % modulus == 0
    return root


def two_sheet_unit_coefficients() -> None:
    # Only local coefficient depths are checked.  The global factor split and
    # asymptotic UV height are hypotheses proved in the corresponding topics.
    U, c1, c3, B, d, n2 = 7, 3, 1, 2, 1, 2
    for p in (13, 17, 29):
        for h in range(1, 4):
            V, modulus = p**h, p ** (2 * h)
            iota = lift_minus_one_root(p, 2 * h)
            first = U * c1 + iota * c3 * B * V * 10 ** (d + n2)
            second = iota * c3 * B * V * 10**d
            assert gcd(first, modulus) == 1
            assert gcd(second, modulus) == p**h
            assert first * p**h % modulus != 0
            assert first * p ** (2 * h) % modulus == 0
            assert second * p**h % modulus == 0
            assert second % modulus != 0


def decimal_norm_selected_sheet_projection() -> None:
    H, y1, y2, y3, D, t1, t2, t3 = sp.symbols("H y1 y2 y3 D t1 t2 t3", real=True)
    s = H + y3
    real = (D + t3) * y1 - t1 * s
    imag = (D + t3) * y2 - t2 * s
    defect = t1**2 + t2**2 + t3**2 - D**2
    identity = (
        -(D + t3)**2 * (H**2 - y1**2 - y2**2 - y3**2)
        + 2 * (D + t3) * s * (D * H - t1 * y1 - t2 * y2 - t3 * y3)
    )
    assert sp.expand(real**2 + imag**2 - defect * s**2 - identity) == 0

    def truncated_depth(value: int, p: int, h: int) -> int:
        for depth in range(h):
            if value % p != 0:
                return depth
            value //= p
        return h

    # These are local models of a stripped denominator pattern and chosen
    # sphere sheet, not full Exact-Lift solutions.  Only the congruences and
    # their exact truncated depths are asserted.
    samples = 0
    for p in (13, 17, 29):
        for h in range(1, 4):
            power, modulus = p**h, p**(2 * h)
            iota = lift_minus_one_root(p, 2 * h)
            for exponent in (1, 2, 3, 6, p - 1, p * (p - 1)):
                unit, Y, ghost_H, other = 3, 7, 5 * power, 2 * power
                assert gcd(unit * Y * 10, p) == 1

                # v2: weights t1/unit = 10^(m2+m+k12), with m2=m=1;
                # t2,t3 have exactly p^h in the stripped chart.
                b1, b2, b3 = unit, 2 * power, 4 * power
                den = (10 * b1 + b2) * 10 + b3
                coeff1, coeff2 = b1 * 10 ** (2 + exponent), b2 * 10
                selected_y2 = (-iota * Y) % modulus
                real_part = (den + b3) * other - coeff1 * (ghost_H + Y)
                imag_part = (den + b3) * selected_y2 - coeff2 * (ghost_H + Y)
                chosen = real_part + iota * imag_part
                conjugate = real_part - iota * imag_part
                assert (chosen - (den - coeff1) * Y) % power == 0
                assert (conjugate + (den + coeff1) * Y) % power == 0
                assert truncated_depth(chosen, p, h) == truncated_depth(10**exponent - 1, p, h)
                assert truncated_depth(conjugate, p, h) == truncated_depth(10**exponent + 1, p, h)

                # v1: t2/unit = 10^(m+d), m=1; sheet y1+i*y3=0.
                b1, b2, b3 = 2 * power, unit, 4 * power
                den = (10 * b1 + b2) * 10 + b3
                coeff1, coeff2 = b1 * 10 ** (2 + exponent), b2 * 10 ** (1 + exponent)
                selected_y1 = (-iota * Y) % modulus
                real_part = (den + b3) * selected_y1 - coeff1 * (ghost_H + Y)
                imag_part = (den + b3) * other - coeff2 * (ghost_H + Y)
                chosen = real_part + iota * imag_part
                conjugate = real_part - iota * imag_part
                assert (chosen + iota * (den + coeff2) * Y) % power == 0
                # The Gaussian i evaluates to -iota on the conjugate sheet.
                assert (conjugate + iota * (den - coeff2) * Y) % power == 0
                assert truncated_depth(chosen, p, h) == truncated_depth(10**exponent + 1, p, h)
                assert truncated_depth(conjugate, p, h) == truncated_depth(10**exponent - 1, p, h)
                samples += 1
    print(f"Decimal norm identity and two-sheet cyclotomic projections: {samples} local models")


def all_odd_decimal_norm_mod_four() -> None:
    # Finite formula verification, not an enumeration of Exact-Lift solutions.
    # The unbounded result is the valuation proof in core.md section 27.7.1.
    samples = 0
    for b1 in (1, 3, 11, 13, 27, 49):
        for b2 in (1, 3, 11, 13, 27, 49):
            m2 = len(str(b2))
            Q = b1 * 10**m2 + b2
            assert Q % 2 == 1
            for m in range(2, 7):
                for offset in (1, 3, 7, 9):
                    b3 = 10 ** (m - 1) + offset
                    assert len(str(b3)) == m and b3 % 2 == 1
                    for n in (m + 1, m + 3):
                        for n2 in (1, 2, 5):
                            t1, t2, D = b1 * 10 ** (n2 + n), b2 * 10**n, Q * 10**m + b3
                            defect = t1**2 + t2**2 + b3**2 - D**2
                            assert defect % 2 ** (m + 1) == 0
                            unit = defect // 2 ** (m + 1)
                            assert unit % 2 == 1
                            expected = -Q * b3 - (2 if m == 2 else 0)
                            assert (unit - expected) % 4 == 0
                            allowed = (Q * b3) % 4 == (1 if m == 2 else 3)
                            assert (unit % 4 == 1) == allowed
                            samples += 1
    print(f"All-odd decimal norm mod-four valuation formulas: {samples} bounded samples")

    states = {"early": 0, "one_before": 0, "one_after": 0, "late": 0, "tie": 0}
    for b1 in range(1, 40, 2):
        for b2 in range(1, 100, 2):
            Q = b1 * 10 ** len(str(b2)) + b2
            for b3 in (1, 3, 5, 7, 9):
                content = 5 * Q + b3
                w = (content & -content).bit_length() - 1
                c = content // 2**w
                for n in range(2, 9):
                    t1, t2 = b1 * 10 ** (1 + n), b2 * 10**n
                    D = 10 * Q + b3
                    defect = t1**2 + t2**2 + b3**2 - D**2
                    if w == 2 * n - 2:
                        states["tie"] += 1
                        continue
                    if w <= 2 * n - 4:
                        state, depth, expected = "early", w + 2, -Q * c
                    elif w == 2 * n - 3:
                        state, depth, expected = "one_before", 2 * n - 1, 2 - Q * c
                    elif w == 2 * n - 1:
                        state, depth, expected = "one_after", 2 * n, 3
                    else:
                        assert w >= 2 * n
                        state, depth, expected = "late", 2 * n, 1
                    unit = defect // 2**depth
                    assert defect % 2**depth == 0 and unit % 2 == 1
                    assert (unit - expected) % 4 == 0
                    states[state] += 1
    assert all(count > 0 for count in states.values())
    print(f"All-odd one-digit-tail depth formulas: {states}; tie states intentionally retained")


def canonical_decimal_norm_two_unit() -> None:
    F, U, V, B, source, t1, t2 = sp.symbols("F U V B source t1 t2", positive=True)
    b3, D = B * V * source, B * source * (2 * F * U + V)
    defect = t1**2 + t2**2 + b3**2 - D**2
    expansion = t1**2 + t2**2 - 4 * B**2 * source**2 * F * U * (F * U + V)
    assert sp.expand(defect - expansion) == 0

    n, m, length2, r1, depthq, depthN = sp.symbols("n m length2 r1 depthq depthN", integer=True)
    H = 2 * m + depthN - 2 * r1 - 4
    ell = 2 * m + 2 * depthq + H
    margin1, margin2 = 2 * n + 2 * length2 + 2 * r1 - ell, 2 * n + 2 * depthq - ell
    assert sp.expand(margin1 - (2 * n - 4 * m + 2 * length2 + 4 * r1 - 2 * depthq - depthN + 4)) == 0
    assert sp.expand(margin2 - (2 * n - 4 * m + 2 * r1 - depthN + 4)) == 0

    alpha = sp.symbols("alpha", positive=True)
    A = 2 * (1 + 2 * alpha) / 3
    assert sp.simplify(4 - A / alpha - (8 * alpha - 2) / (3 * alpha)) == 0
    actual_alpha = log10(2)
    M_star = 3 / float(A.subs(alpha, actual_alpha))
    lam = (2 + actual_alpha) / (1 + 2 * actual_alpha)
    c_star = 2 + 3 * lam
    u_star = 2 - 2 * (1 - actual_alpha) * M_star / 3
    kappa = (2 + actual_alpha) / 3
    assert abs(2 * c_star - 4 * M_star - 2 * u_star) < 1e-12
    assert actual_alpha > 1 / 4
    assert 2 * u_star - 1 > 0.38
    assert 2 * M_star - (2 + 2 * kappa / actual_alpha) / 2 > 2

    def valuation_two(value: int) -> int:
        assert value != 0
        return (abs(value) & -abs(value)).bit_length() - 1

    samples, z_three = 0, 0
    # Prefix blocks and tail denominators are exact integers with their stated
    # decimal lengths.  Source phase/Long-2-depth/finite norm criterion hold;
    # no numerator or sphere solution is asserted in these local models.
    for first in (1, 3, 7, 11):
        for second in (11, 12, 13, 14, 17, 19, 21, 22, 23, 29):
            width2 = len(str(second))
            prefix = first * 10**width2 + second
            depthq_value = valuation_two(prefix)
            if valuation_two(second) != depthq_value:
                continue
            U_value, source_value = prefix, 1
            while U_value % 2 == 0:
                U_value //= 2
                source_value *= 2
            while U_value % 5 == 0:
                U_value //= 5
                source_value *= 5
            for V_value in (1, 13, 17, 29):
                if gcd(U_value, V_value) != 1:
                    continue
                T, F_value = 0, 1
                while 2 * F_value <= V_value * source_value:
                    T, F_value = T + 1, F_value * 5
                # Minimal such F gives 0.1 <= b3/10^m < 1.
                m_value = max(2, T + 2)
                B_value = 10**m_value // (2 * F_value)
                tail = B_value * V_value * source_value
                assert len(str(tail)) == m_value
                phase_sum = F_value * U_value + V_value
                H_value = valuation_two(phase_sum)
                Z_value = phase_sum // 2**H_value
                if H_value < 2:
                    continue
                assert U_value % 4 == 3 and Z_value % 2 == 1
                n_value, length2_value = m_value + H_value + 3, 1
                coeff1 = first * 10 ** (length2_value + n_value)
                coeff2 = second * 10**n_value
                den = prefix * 10**m_value + tail
                ell_value = 2 * m_value + 2 * depthq_value + H_value
                assert min(valuation_two(coeff1**2), valuation_two(coeff2**2)) >= ell_value + 2
                defect_value = coeff1**2 + coeff2**2 + tail**2 - den**2
                assert valuation_two(defect_value) == ell_value
                assert (defect_value // 2**ell_value + U_value * Z_value) % 4 == 0
                assert (defect_value // 2**ell_value) % 4 == (1 if Z_value % 4 == 1 else 3)
                samples += 1
                z_three += Z_value % 4 == 3
    assert samples > 0 and z_three > 0
    print(f"Canonical decimal two-unit criterion: {samples} denominator local models, {z_three} norm-forbidden Z=3 states")


def conditional_uniqueness_countermodel() -> None:
    p, h, F, c3, g0 = 13, 2, 5, 1, 1
    modulus = p**h
    iota = lift_minus_one_root(p, h)
    K = 2 * F * iota * c3 % modulus
    c2 = K
    values = [x for x in range(10, 100) if gcd(x, 10 * modulus) == 1]
    hits = [(a2, R0) for a2 in values for R0 in values if (K * R0 - a2 * c2 * g0) % modulus == 0]
    assert len(hits) == len(values) > 1
    assert all(a2 == R0 for a2, R0 in hits)
    for fixed in values:
        assert sum(a2 == fixed for a2, _ in hits) == 1
        assert sum(R0 == fixed for _, R0 in hits) == 1
    # Both one-variable fibers are unique, while the joint family is not.
    print(f"Conditional-uniqueness countermodel: {len(hits)} joint modular pairs; not Exact-Lift solutions")


def joint_entropy_shared_budget() -> None:
    alpha = sp.symbols("alpha", positive=True)
    beta = 1 - alpha
    A = 2 * (1 + 2 * alpha) / 3
    lam = (2 + alpha) / (1 + 2 * alpha)
    delta, mu, sigma, q2, n2, q5, g5, n5, rough = sp.symbols(
        "delta mu sigma Q2 N2 Q5 G5 N5 R", nonnegative=True
    )
    suffix = (
        delta / 2
        - (1 - beta / 3) * mu
        - beta * q5 / 3
        + beta * g5 / 3
        - beta * n5 / 6
        + rough / 2
    )
    joint = sigma + rough / 2 + suffix
    mu_budget = (
        sigma + 2 * alpha * q2 + alpha * n2
        + beta * (2 * q5 + 4 * g5 + n5) / 3 + 2 * rough
    ) / A
    assert sp.simplify((1 - beta / 3) / A - lam / 2) == 0
    after = sp.expand(joint.subs(mu, mu_budget))
    corrections = (
        -alpha * lam * q2 - alpha * lam * n2 / 2
        - beta * (1 + lam) * q5 / 3
        + beta * (1 - 2 * lam) * g5 / 3
        - beta * (1 + lam) * n5 / 6
        + (1 - lam) * rough
    )
    target = delta / 2 + (1 - lam / 2) * sigma + corrections
    assert sp.simplify(after - target) == 0
    assert sp.simplify(target - (delta / lam + (1 - lam / 2) * (sigma - delta / lam) + corrections)) == 0
    for coefficient in [
        -alpha * lam, -alpha * lam / 2,
        -beta * (1 + lam) / 3, beta * (1 - 2 * lam) / 3,
        -beta * (1 + lam) / 6, 1 - lam,
    ]:
        assert float(coefficient.subs(alpha, log10(2))) < 0
    assert 0 < float((1 - lam / 2).subs(alpha, log10(2))) < 1
    assert 2**3 < 10**2 and 2**4 > 10
    u_star = 0.691116422381969
    assert 1 + u_star - 0.5 > 1


def main() -> None:
    symbolic_uv2_sharp()
    budget_coefficients()
    thresholds()
    ordinary_gap_full_word_dictionary()
    two_sheet_unit_coefficients()
    decimal_norm_selected_sheet_projection()
    all_odd_decimal_norm_mod_four()
    canonical_decimal_norm_two_unit()
    conditional_uniqueness_countermodel()
    joint_entropy_shared_budget()
    print("DD corrected sharp numerator collapse audit passed")


if __name__ == "__main__":
    main()
