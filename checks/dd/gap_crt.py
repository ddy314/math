#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0602; see history/sources.json.
"""

from __future__ import annotations

import math

import sympy as sp


def exact_normalization_toy() -> None:
    # Actual denominator-side gcd-normal data:
    # b1=1, b2=2, m2=1 => Q=12, G=2.
    # m=1, b3=16 => kappa=10*12*2/16=15.
    b1, b2, m2 = 1, 2, 1
    Q = b1 * 10**m2 + b2
    G = b1 * b2
    m, b3 = 1, 16
    kappa = 10**m * Q * G // b3
    gamma = math.gcd(kappa, G)
    u, v = kappa // gamma, G // gamma
    d0 = math.gcd(u, Q)
    L, q = u // d0, Q // d0
    omega = 10**m // L
    q_lcm = math.lcm(b1, b2, b3)
    c3 = q_lcm // b3

    assert (Q, G, kappa, gamma, u, v) == (12, 2, 15, 1, 15, 2)
    assert (d0, L, q, omega, q_lcm, c3) == (3, 5, 4, 2, 16, 1)
    assert math.gcd(d0, v) == 1
    assert math.gcd(L, v) == 1
    assert b3 == v * omega * q
    assert q_lcm == v * omega * q * c3
    assert kappa * b3 == 10**m * Q * G


def source_gap_toy() -> None:
    # Standalone exact source-gap algebra toy.
    # omega*c3*A12*10^d = a + d0*H0
    # v*H0 = a3*c3 + L*a
    d0, L, v = 3, 1, 2
    omega, c3, A12, d = 1, 1, 1, 1
    H0, a, a3 = 3, 1, 5

    assert math.gcd(d0, v) == 1
    assert math.gcd(L, v) == 1
    assert omega * c3 * A12 * 10**d == a + d0 * H0
    assert v * H0 == a3 * c3 + L * a

    rho_d0 = (omega * c3 * A12 * 10**d) % d0
    rho_v = (-a3 * c3 * pow(L, -1, v)) % v
    assert a % d0 == rho_d0
    assert a % v == rho_v

    # CRT modulus d0*v uniquely recovers 0<a<d0*v.
    candidates = [x for x in range(d0 * v) if x % d0 == rho_d0 and x % v == rho_v]
    assert candidates == [a]


def local_depth_symbolic() -> None:
    E, j, c, t = sp.symbols("E j c t", nonnegative=True, integer=True)

    # Case E >= j.
    d0_depth_1 = E + c - j
    c3_depth_1 = E - j
    raw_1 = sp.expand(d0_depth_1 - c3_depth_1 - t)
    assert sp.simplify(raw_1 - (c - t)) == 0

    # Case j > E.
    d0_depth_2 = E + c - j
    c3_depth_2 = 0
    raw_2 = sp.expand(d0_depth_2 - c3_depth_2 - t)
    assert sp.simplify(raw_2 - (c - t - (j - E))) == 0

    # Compare pre-positive-part expressions with old Euclidean depth.
    old_1 = c - E - t
    old_2 = c - j - t
    assert sp.simplify(raw_1 - old_1 - E) == 0
    assert sp.simplify(raw_2 - old_2 - E) == 0


def corrected_split_coverage() -> None:
    # Exhaust finite local ledgers satisfying the exact formulas and check
    # r_d0 >= h+n0 on hard support.
    for E in range(6):
        for j in range(6):
            for t in range(5):
                for n0 in range(5):
                    for h in range(1, 6):
                        M = max(E, j)
                        c = h + 2 * t + n0 + M + j
                        r = max(c - t - max(j - E, 0), 0)
                        assert r >= h + n0

    # Soft e_N support: use the corrected split identities directly.
    for E in range(6):
        for j in range(6):
            for t in range(5):
                for alpha in range(5):
                    for eN in range(1, 6):
                        if j > E:
                            for e3 in range(j - E + 1):
                                x = t + alpha + eN + e3
                                c = x + j + E
                                r = max(c - t - (j - E), 0)
                                assert r >= eN
                        else:
                            e3 = 0
                            x = t + alpha + eN
                            c = x + 2 * j
                            r = max(c - t, 0)
                            assert r >= eN


def large_gap_lower() -> None:
    # Pure algebra: a>=d0*v, u=d0*L, gstar/v>=1.
    for d0 in range(1, 8):
        for L in range(1, 8):
            for v in range(1, 8):
                u = d0 * L
                # Choose a at the threshold and the minimal overlap factor 1.
                a = d0 * v
                F_lower = L * (u + 2 * v) * a
                assert F_lower == u * v * (u + 2 * v)
                assert F_lower > u * u * v

                # Whenever u/v>Q, the claimed Q^2 v^3 lower follows.
                Q = max(0, (u - 1) // v)
                if Q > 0 and u > Q * v:
                    assert u * u * v > Q * Q * v**3


def circular_bound() -> None:
    # Verify the exact interval-to-nearest-multiple bound used after d0 stripping.
    for m2 in range(1, 30):
        for c10 in range(0, m2 + 3):
            for s10 in range(0, m2 + 3):
                for d in range(0, 2 * m2 + 1):
                    vals = []
                    for shift in range(-s10, c10 + 1):
                        z = d + shift
                        r = min(z % m2, (-z) % m2)
                        vals.append(r)
                    actual = min(vals)
                    bound = max(0, (m2 - c10 - s10) // 2)
                    assert actual <= bound
                    assert actual <= m2 // 2


def canonical_large_gap_shared_budget() -> None:
    """Check the full symbolic cancellation; use no candidate enumeration."""
    alpha = sp.symbols("alpha", positive=True)
    beta = 1 - alpha
    A = 2 * (1 + 2 * alpha) / 3
    C = (5 - beta) / A
    delta, mu = sp.symbols("delta mu", nonnegative=True)
    q2, n2, q5, g5, n5, rough, sigma, g2 = sp.symbols(
        "Q2 N2 Q5 G5 N5 R sigma G2", nonnegative=True
    )
    m1_upper = (
        delta / 2
        - (1 - beta / 3) * mu
        - beta * q5 / 3
        + beta * g5 / 3
        - beta * n5 / 6
        + rough / 2
    )

    # alpha*G2 <= m1/S+alpha*Q2.  Its coefficient is positive here,
    # so substituting the upper endpoint produces an upper bound.
    expr = 3 * (alpha * g2 + beta * g5 + rough) - 2 * mu + delta
    after_g2 = sp.expand(expr.subs(g2, (m1_upper + alpha * q2) / alpha))
    pre_budget = (
        5 * delta / 2
        - (5 - beta) * mu
        + 3 * alpha * q2
        - beta * q5
        + 4 * beta * g5
        - beta * n5 / 2
        + 9 * rough / 2
    )
    assert sp.simplify(after_g2 - pre_budget) == 0

    mu_budget = (
        sigma
        + 2 * alpha * q2
        + alpha * n2
        + beta * (2 * q5 + 4 * g5 + n5) / 3
        + 2 * rough
    ) / A
    after_mu = sp.expand(after_g2.subs(mu, mu_budget))
    target = (
        5 * delta / 2
        - C * sigma
        + alpha * (3 - 2 * C) * q2
        - alpha * C * n2
        - beta * (1 + 2 * C / 3) * q5
        + beta * (4 - 4 * C / 3) * g5
        - beta * (sp.Rational(1, 2) + C / 3) * n5
        + (sp.Rational(9, 2) - 2 * C) * rough
    )
    assert sp.simplify(after_mu - target) == 0

    # C>3 follows exactly from alpha<2/3; all correction signs then follow.
    assert sp.simplify(C - 3 - 3 * (2 - 3 * alpha) / (2 * (1 + 2 * alpha))) == 0
    assert 2**3 < 10**2  # log_10(2)<2/3.
    assert 2**4 > 10  # log_10(2)>1/4, hence M_*<3 and K_*>3/2.
    for coefficient in [
        -C,
        alpha * (3 - 2 * C),
        -alpha * C,
        -beta * (1 + 2 * C / 3),
        beta * (4 - 4 * C / 3),
        -beta * (sp.Rational(1, 2) + C / 3),
        sp.Rational(9, 2) - 2 * C,
    ]:
        # Numeric output is a sanity check; the exact sign proof above uses
        # 0<alpha<2/3, 0<beta, C>3 and nonnegative defects.
        assert float(coefficient.subs(alpha, math.log10(2))) < 0

    lam = (2 + alpha) / (1 + 2 * alpha)
    m_star = 3 / A
    c_star = 2 + 3 * lam
    k_star = c_star + 1 - 2 * m_star
    assert sp.simplify(k_star - (sp.Rational(9, 2) - m_star)) == 0
    delta_threshold = 2 * k_star / 5
    margin = k_star - sp.Rational(5, 4)
    assert float(delta_threshold.subs(alpha, math.log10(2))) > 0.5
    assert float(margin.subs(alpha, math.log10(2))) > 0.44
    single_reader_threshold = 2 * (k_star - 1) / 5
    assert sp.simplify(delta_threshold - single_reader_threshold - sp.Rational(2, 5)) == 0
    assert abs(float(single_reader_threshold.subs(alpha, math.log10(2))) - 0.276446568952787) < 1e-14

    # The location bound uses this exact factor ratio before any height limit.
    d0, L, v, a = sp.symbols("d0 L v a", positive=True)
    u = d0 * L
    assert sp.simplify(L * (u + 2 * v) * a - a * u * v * (u + 2 * v) / (d0 * v)) == 0

    # Eliminating H0 from the two exact parents gives the existing determinant
    # equation, not another independent height bound.
    H0, omega, c3, A12, decimal, a3 = sp.symbols(
        "H0 omega c3 A12 decimal a3", positive=True
    )
    parent_d0 = omega * c3 * A12 * decimal - a - d0 * H0
    parent_v = v * H0 - a3 * c3 - L * a
    elimination = c3 * (v * omega * A12 * decimal - d0 * a3) - (u + v) * a
    assert sp.simplify(v * parent_d0 + d0 * parent_v - elimination) == 0
    print(
        "Canonical large-gap necessary delta >= "
        f"{float(delta_threshold.subs(alpha, math.log10(2))):.15f}; "
        "delta<=1/2 uniform log-gap margin = "
        f"{float(margin.subs(alpha, math.log10(2))):.15f}"
    )


def single_digit_tail_source_dictionary() -> None:
    """Audit section 11 formulas; unbounded coverage is the valuation proof."""
    def depth(n: int, p: int) -> int:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        return e

    for p in (3, 7):
        assert all((x*x+y*y) % p != 0 for x in range(1, p) for y in range(1, p))
    count, forbidden = 0, 0
    for b1 in range(1, 100):
        for b2 in range(1, 100):
            m2 = len(str(b2))
            Q = b1 * 10**m2 + b2
            for b3 in range(1, 10):
                v = b3 // math.gcd(10*Q, b3)
                assert depth(v, 5) == 0
                if v > 1:
                    forbidden += 1
                    for p in (2, 3, 7):
                        if v % p:
                            continue
                        e1, e2, e3 = (depth(b, p) for b in (b1, b2, b3))
                        s = depth(Q, p)
                        word_depth = depth(10*Q+b3, p)
                        if p == 2:
                            assert word_depth == 1+s < e3
                        else:
                            assert word_depth == s < e3
                            if e1 == e2:
                                assert s >= e1 and e3 > e1
                            else:
                                assert s == min(e1, e2)
                            assert [e1, e2, e3].count(max(e1, e2, e3)) <= 2
                else:
                    count += 1
                    omega = math.gcd(10, b3)
                    L, tau = 10//omega, b3//omega
                    u = 10*Q//b3
                    d0 = math.gcd(u, Q)
                    assert Q % tau == 0 and math.gcd(L, tau) == 1
                    assert (d0, u//d0, Q//d0) == (Q//tau, L, tau)
    print(f"One-digit-tail source dictionary: {count} v=1 samples, {forbidden} v>1 depth-obstruction samples")

    # n3 >= 2 gives Aword=a3 mod25. The five-unit sphere projection
    # is therefore exact in these residue classes, not a numerical heuristic.
    projected = 0
    for Q in range(1, 1001):
        if Q % 5 == 0 or (2*Q+1) % 5 == 0:
            continue
        inverse = pow(2*Q+1, -1, 25)
        for a3 in range(1, 25):
            if a3 % 5 == 0:
                continue
            for c3 in range(1, 25):
                if c3 % 5 == 0:
                    continue
                y3 = c3*a3 % 25
                H = y3*inverse % 25
                allowed = (H*H-y3*y3) % 25 == 0
                assert allowed == (Q % 25 == 24)
                if allowed:
                    projected += 1
                    assert (H+y3) % 25 == 0 and (H-y3) % 5 != 0
    assert projected == 16_000
    print("Unique-five-tail exact mod25 projection: Q=24 mod25; permitted negative sheet retained")
    # Section 11.2 is an unbounded divisor proof, not a bounded candidate search.
    surviving_b1 = [b for b in range(1, 96) if 95 % b == 0 and math.gcd(b, 45) == 1 and b % 10 == 9]
    assert surviving_b1 == [19]
    assert depth(1995, 3) == 1 < depth(9, 3)
    assert 199 % 25 == 24
    print("Unique-five-tail, one-digit b2: exact divisor reduction to (19,9,5), excluded by three-depth")
    b1_divisors = [b for b in range(1, 100) if 99 % b == 0]
    assert b1_divisors == [1, 3, 9, 11, 33, 99]
    assert pow(20, -1, 49) == 27 and (-5*27) % 49 == 12
    assert all((20*b+5) % 49 for b in b1_divisors)
    assert [b for b in range(1, 996) if 995 % b == 0 and b % 5] == [1, 199]
    assert all((b+5) % 9 for b in (1, 199))
    print("Unique-five-tail, two-digit b2=49/99: exact divisor/7^2/3^2 projections exclude both states")


def main() -> None:
    exact_normalization_toy()
    source_gap_toy()
    local_depth_symbolic()
    corrected_split_coverage()
    large_gap_lower()
    circular_bound()
    canonical_large_gap_shared_budget()
    single_digit_tail_source_dictionary()
    print("DD gcd-normal d0 gap CRT dichotomy checks passed")


if __name__ == "__main__":
    main()
