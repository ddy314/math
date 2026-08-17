"""Finite certificate for the DD top layer at S_12 = 2 and 3.

The unbounded reductions used here are proved in Section 27.16.  This script
only checks the two finite top-layer slices

    S_12 in {2, 3},    n_3 = 8 S_12 + 1.

It does not enumerate a_3.  Instead it uses the exact unified discriminant,
whose being a square is necessary for an Exact Lift candidate.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from math import gcd, isqrt

import numpy as np
from sympy import factorint


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value) for a positive integer."""

    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def valuation_array(values: np.ndarray, prime: int) -> np.ndarray:
    """Vectorized exact p-adic valuation for a positive int64 array."""

    reduced = values.copy()
    exponents = np.zeros(values.shape, dtype=np.int16)
    divisible = reduced % prime == 0
    while np.any(divisible):
        exponents[divisible] += 1
        reduced[divisible] //= prime
        divisible = reduced % prime == 0
    return exponents


def bounded_divisors(value: int, extra_2_5: int, cap: int) -> list[int]:
    """Divisors of 10**extra_2_5 * value which do not exceed cap."""

    factors = dict(factorint(value))
    factors[2] = factors.get(2, 0) + extra_2_5
    factors[5] = factors.get(5, 0) + extra_2_5
    prime_powers = sorted(factors.items())
    result: list[int] = []

    def visit(index: int, current: int) -> None:
        if index == len(prime_powers):
            result.append(current)
            return
        prime, exponent = prime_powers[index]
        power = 1
        for _ in range(exponent + 1):
            visit(index + 1, current * power)
            if power > cap // prime or current * power > cap // prime:
                break
            power *= prime

    visit(0, 1)
    return result


def maximum_valuation_below(bound: int, prime: int) -> int:
    """Largest e for which prime**e is strictly below bound."""

    exponent = 0
    power = 1
    while power * prime < bound:
        power *= prime
        exponent += 1
    return exponent


@dataclass(frozen=True)
class Tail:
    m_3: int
    d_3: int
    kappa: int
    odd_denominators: bool
    required_n_2: int
    required_five_gap: int


@dataclass
class Counts:
    tail: int = 0
    all_odd: int = 0
    prefix_or_tie: int = 0
    b3_unique: int = 0
    position_failure: int = 0
    negative_two_requirement: int = 0
    five_box_failure: int = 0
    retained_tails: int = 0
    digit_pairs: int = 0
    coprime_pairs: int = 0
    two_adic_pairs: int = 0
    five_adic_pairs: int = 0
    squarefree_gap_pairs: int = 0
    square_discriminants: int = 0


def denominator_splits(S: int) -> tuple[tuple[int, int], ...]:
    if S == 2:
        return ((1, 1),)
    if S == 3:
        return ((1, 2), (2, 1))
    raise ValueError("this certificate only covers S = 2, 3")


def build_tail_kernel(
    S: int,
) -> tuple[
    dict[tuple[int, int, int, int], list[Tail]],
    Counts,
    Counter[int],
]:
    """Enumerate the exact denominator-tail kernel proved finite in 27.16."""

    n_3 = 8 * S + 1
    counts = Counts()
    by_denominator: dict[tuple[int, int, int, int], list[Tail]] = defaultdict(list)
    tail_by_m_3: Counter[int] = Counter()
    max_a_5 = maximum_valuation_below(10 ** (S + 2), 5)
    max_n_5 = maximum_valuation_below(2 * 10 ** (4 * S), 5)

    for m_1, m_2 in denominator_splits(S):
        for b_1 in range(10 ** (m_1 - 1), 10**m_1):
            for b_2 in range(10 ** (m_2 - 1), 10**m_2):
                Q = b_1 * 10**m_2 + b_2
                G = b_1 * b_2
                QG = Q * G
                e_1 = valuation(b_1, 2)
                e_2 = valuation(b_2, 2)
                q_2 = valuation(Q, 2)
                g_2 = valuation(G, 2)
                q_5 = valuation(Q, 5)
                g_5 = valuation(G, 5)

                for m_3 in range(n_3 - 5 * S, 6 * S + 4):
                    for kappa in bounded_divisors(QG, m_3, 10 * QG):
                        if kappa <= QG:
                            continue

                        k_2 = valuation(kappa, 2)
                        f_2 = valuation(kappa + 2 * G, 2)
                        k_5 = valuation(kappa, 5)
                        f_5 = valuation(kappa + 2 * G, 5)
                        if 2 * k_2 + f_2 < m_3 or 2 * k_5 + f_5 < m_3:
                            continue

                        counts.tail += 1
                        tail_by_m_3[m_3] += 1
                        b_3_two = m_3 + q_2 + g_2 - k_2
                        b_3_five = m_3 + q_5 + g_5 - k_5

                        # The finite tail kernel contains no 5-adic unit b_3.
                        assert b_3_five > 0
                        d_3 = n_3 - m_3
                        assert d_3 + b_3_five > q_5

                        odd_denominators = e_1 == e_2 == b_3_two == 0
                        if odd_denominators:
                            counts.all_odd += 1
                            required_n_2 = -1
                        else:
                            if b_3_two <= max(e_1, e_2):
                                counts.prefix_or_tie += 1
                                continue
                            counts.b3_unique += 1
                            if k_2 <= g_2:
                                counts.position_failure += 1
                                continue
                            required_n_2 = (
                                3 * k_2
                                + f_2
                                - 2 * m_3
                                - 2 * q_2
                                - 2 * g_2
                            )
                            if required_n_2 < 0:
                                counts.negative_two_requirement += 1
                                continue

                        h_5 = valuation(kappa + G, 5)
                        resonance_n_5 = (
                            3 * k_5
                            + f_5
                            - 2 * m_3
                            - 2 * q_5
                            - 2 * h_5
                        )
                        minus_a_5 = f_5 + k_5 - h_5 - g_5 - n_3
                        assert not 0 <= resonance_n_5 <= max_n_5
                        assert not 0 <= minus_a_5 <= max_a_5

                        required_five_gap = (
                            n_3
                            - 2 * m_3
                            - 2 * q_5
                            - h_5
                            + 2 * k_5
                            + g_5
                        )
                        if not -max_a_5 <= required_five_gap <= max_n_5:
                            counts.five_box_failure += 1
                            continue

                        by_denominator[(m_1, m_2, b_1, b_2)].append(
                            Tail(
                                m_3=m_3,
                                d_3=d_3,
                                kappa=kappa,
                                odd_denominators=odd_denominators,
                                required_n_2=required_n_2,
                                required_five_gap=required_five_gap,
                            )
                        )
                        counts.retained_tails += 1

    return by_denominator, counts, tail_by_m_3


def check_prefixes(
    S: int,
    by_denominator: dict[tuple[int, int, int, int], list[Tail]],
    counts: Counts,
) -> list[tuple[int, ...]]:
    """Check all bounded prefix blocks against the exact discriminant."""

    n_3 = 8 * S + 1
    final_nonsquares: list[tuple[int, ...]] = []

    for (m_1, m_2, b_1, b_2), tails in by_denominator.items():
        Q = b_1 * 10**m_2 + b_2
        G = b_1 * b_2

        for n_1 in range(1, S + 2):
            for n_2 in range(1, S + 3 - n_1):
                s_1 = n_1 - m_1
                s_2 = n_2 - m_2
                surplus_difference = abs(s_1 - s_2)
                relevant = [
                    tail
                    for tail in tails
                    if s_1 <= tail.d_3
                    and s_2 <= tail.d_3
                    and tail.d_3 <= 3 * S + surplus_difference + 2
                ]
                if not relevant:
                    continue

                a_1_values = np.arange(
                    10 ** (n_1 - 1), 10**n_1, dtype=np.int64
                )
                a_2_values = np.arange(
                    10 ** (n_2 - 1), 10**n_2, dtype=np.int64
                )
                a_1 = np.repeat(a_1_values, a_2_values.size)
                a_2 = np.tile(a_2_values, a_1_values.size)
                counts.digit_pairs += a_1.size

                coprime = (np.gcd(a_1, b_1) == 1) & (np.gcd(a_2, b_2) == 1)
                a_1 = a_1[coprime]
                a_2 = a_2[coprime]
                counts.coprime_pairs += a_1.size
                if a_1.size == 0:
                    continue

                A_12 = a_1 * 10**n_2 + a_2
                first_norm = a_1 * b_2
                second_norm = a_2 * b_1
                N_12 = first_norm * first_norm + second_norm * second_norm
                n_2_values = valuation_array(N_12, 2)
                n_5_values = valuation_array(N_12, 5)
                a_5_values = valuation_array(A_12, 5)

                for tail in relevant:
                    if tail.odd_denominators:
                        two_adic = n_2_values >= tail.m_3 + 1
                    else:
                        two_adic = n_2_values == tail.required_n_2
                    counts.two_adic_pairs += int(np.count_nonzero(two_adic))

                    five_adic = two_adic & (
                        n_5_values - a_5_values == tail.required_five_gap
                    )
                    surviving_indices = np.flatnonzero(five_adic)
                    counts.five_adic_pairs += surviving_indices.size

                    for index in surviving_indices:
                        a_1_value = int(a_1[index])
                        a_2_value = int(a_2[index])
                        A_12_value = int(A_12[index])
                        N_12_value = int(N_12[index])
                        if not (
                            10**tail.d_3 * A_12_value
                            < 40 * Q * Q * N_12_value
                        ):
                            continue
                        counts.squarefree_gap_pairs += 1

                        x_value = (
                            tail.kappa * G * A_12_value * 10**tail.d_3
                        )
                        discriminant = (
                            x_value * x_value
                            - tail.kappa
                            * (tail.kappa + 2 * G)
                            * Q
                            * Q
                            * N_12_value
                        )
                        if discriminant < 0:
                            continue
                        root = isqrt(discriminant)
                        if root * root == discriminant:
                            counts.square_discriminants += 1
                        else:
                            assert root * root < discriminant < (root + 1) ** 2
                            final_nonsquares.append(
                                (
                                    m_1,
                                    m_2,
                                    b_1,
                                    b_2,
                                    n_1,
                                    n_2,
                                    a_1_value,
                                    a_2_value,
                                    tail.m_3,
                                    tail.kappa,
                                    tail.required_n_2,
                                    tail.required_five_gap,
                                )
                            )

    return final_nonsquares


def run_slice(S: int) -> None:
    by_denominator, counts, tail_by_m_3 = build_tail_kernel(S)
    final_nonsquares = check_prefixes(S, by_denominator, counts)

    expected = {
        2: {
            "tail": 618,
            "tail_by_m_3": {7: 364, 8: 203, 9: 44, 10: 7},
            "all_odd": 6,
            "prefix_or_tie": 3,
            "b3_unique": 609,
            "position_failure": 118,
            "negative_two_requirement": 422,
            "five_box_failure": 0,
            "retained_tails": 75,
            "digit_pairs": 414801,
            "coprime_pairs": 204451,
            "two_adic_pairs": 133487,
            "five_adic_pairs": 114,
            "squarefree_gap_pairs": 2,
            "final_nonsquares": [
                (1, 1, 5, 5, 1, 3, 1, 818, 8, 4000, 0, 5),
                (1, 1, 5, 5, 1, 3, 1, 932, 8, 4000, 0, 5),
            ],
        },
        3: {
            "tail": 39710,
            "tail_by_m_3": {
                10: 22246,
                11: 9848,
                12: 5593,
                13: 1490,
                14: 481,
                15: 45,
                16: 5,
                17: 2,
            },
            "all_odd": 139,
            "prefix_or_tie": 165,
            "b3_unique": 39406,
            "position_failure": 3442,
            "negative_two_requirement": 30987,
            "five_box_failure": 0,
            "retained_tails": 5116,
            "digit_pairs": 103600944,
            "coprime_pairs": 46525686,
            "two_adic_pairs": 36089187,
            "five_adic_pairs": 27,
            "squarefree_gap_pairs": 8,
            "final_nonsquares": [
                (1, 2, 5, 65, 4, 1, 9944, 4, 12, 1600000, 4, 9),
                (1, 2, 5, 95, 3, 1, 991, 3, 12, 800000, 1, 9),
                (1, 2, 5, 95, 4, 1, 2973, 9, 12, 800000, 1, 9),
                (2, 1, 65, 5, 1, 4, 4, 9944, 12, 1600000, 4, 9),
                (2, 1, 90, 5, 1, 4, 7, 4793, 12, 800000, 0, 9),
                (2, 1, 90, 5, 1, 4, 7, 4793, 12, 2400000, 0, 9),
                (2, 1, 95, 5, 1, 3, 3, 991, 12, 800000, 1, 9),
                (2, 1, 95, 5, 1, 4, 9, 2973, 12, 800000, 1, 9),
            ],
        },
    }[S]

    assert counts.tail == expected["tail"]
    assert dict(sorted(tail_by_m_3.items())) == expected["tail_by_m_3"]
    assert counts.all_odd == expected["all_odd"]
    assert counts.prefix_or_tie == expected["prefix_or_tie"]
    assert counts.b3_unique == expected["b3_unique"]
    assert counts.position_failure == expected["position_failure"]
    assert (
        counts.negative_two_requirement
        == expected["negative_two_requirement"]
    )
    assert counts.five_box_failure == expected["five_box_failure"]
    assert counts.retained_tails == expected["retained_tails"]
    assert counts.digit_pairs == expected["digit_pairs"]
    assert counts.coprime_pairs == expected["coprime_pairs"]
    assert counts.two_adic_pairs == expected["two_adic_pairs"]
    assert counts.five_adic_pairs == expected["five_adic_pairs"]
    assert counts.squarefree_gap_pairs == expected["squarefree_gap_pairs"]
    assert final_nonsquares == expected["final_nonsquares"]
    assert counts.square_discriminants == 0

    print(
        f"S={S}: tail={counts.tail}, retained={counts.retained_tails}, "
        f"coprime-prefix={counts.coprime_pairs}, "
        f"two-adic={counts.two_adic_pairs}, "
        f"five-adic={counts.five_adic_pairs}, "
        f"squarefree-gap={counts.squarefree_gap_pairs}, squares=0"
    )
    for witness in final_nonsquares:
        print("  nonsquare witness:", witness)


def main() -> None:
    run_slice(2)
    run_slice(3)
    print("DD 27.16 S=2,3 top-layer certificate: OK")


if __name__ == "__main__":
    main()
