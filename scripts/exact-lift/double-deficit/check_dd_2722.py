"""Finite certificate for the remaining DD equality sizes S_12 = 2, 3.

This file is deliberately narrow: it starts from the exact denominator-tail
divisibility already proved in Sections 21 and 27.16 and investigates

    S_12 in {2, 3},    n_3 = 8 S_12.

It never treats the fact that S_12 is fixed as a bound on a non-dominant
prefix surplus.  That sector is closed first, using only its forced m_3 range
and the denominator-tail divisibility.  Only the genuinely bounded dominant
sector is sent to the exact discriminant check.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from math import isqrt
from random import Random

import numpy as np

from check_dd_2716 import bounded_divisors, valuation, valuation_array


LIMB_BASE = 1_000_000


def product_limbs(scalar: int, values: np.ndarray) -> list[np.ndarray]:
    """Return exact base-LIMB_BASE limbs of scalar * positive int64 values."""

    scalar_limbs: list[int] = []
    reduced_scalar = scalar
    while reduced_scalar:
        scalar_limbs.append(reduced_scalar % LIMB_BASE)
        reduced_scalar //= LIMB_BASE
    if not scalar_limbs:
        scalar_limbs.append(0)

    value_limbs: list[np.ndarray] = []
    reduced_values = values.copy()
    while np.any(reduced_values):
        value_limbs.append(reduced_values % LIMB_BASE)
        reduced_values //= LIMB_BASE
    if not value_limbs:
        value_limbs.append(np.zeros(values.shape, dtype=np.int64))

    result = [
        np.zeros(values.shape, dtype=np.int64)
        for _ in range(len(scalar_limbs) + len(value_limbs))
    ]
    for scalar_index, scalar_limb in enumerate(scalar_limbs):
        for value_index, value_limb in enumerate(value_limbs):
            result[scalar_index + value_index] += scalar_limb * value_limb

    for index in range(len(result) - 1):
        result[index + 1] += result[index] // LIMB_BASE
        result[index] %= LIMB_BASE
    while len(result) > 1 and not np.any(result[-1]):
        result.pop()
    return result


def product_less(
    left_scalar: int,
    left_values: np.ndarray,
    right_scalar: int,
    right_values: np.ndarray,
) -> np.ndarray:
    """Compare two nonnegative scalar-array products without int64 overflow."""

    left = product_limbs(left_scalar, left_values)
    right = product_limbs(right_scalar, right_values)
    width = max(len(left), len(right))
    zero = np.zeros(left_values.shape, dtype=np.int64)
    left.extend(zero.copy() for _ in range(width - len(left)))
    right.extend(zero.copy() for _ in range(width - len(right)))

    less = np.zeros(left_values.shape, dtype=bool)
    equal = np.ones(left_values.shape, dtype=bool)
    for index in range(width - 1, -1, -1):
        less |= equal & (left[index] < right[index])
        equal &= left[index] == right[index]
    return less


def check_product_comparison() -> None:
    """Cross-check the limb comparison against Python big integers."""

    random = Random(2722)
    for _ in range(1000):
        size = random.randrange(1, 100)
        left_scalar = random.randrange(1, 10**16)
        right_scalar = random.randrange(1, 10**10)
        left = np.array(
            [random.randrange(0, 10**12) for _ in range(size)],
            dtype=np.int64,
        )
        right = np.array(
            [random.randrange(0, 10**12) for _ in range(size)],
            dtype=np.int64,
        )
        actual = product_less(left_scalar, left, right_scalar, right)
        expected = np.array(
            [
                left_scalar * int(left_value)
                < right_scalar * int(right_value)
                for left_value, right_value in zip(left, right, strict=True)
            ]
        )
        assert np.array_equal(actual, expected)


@dataclass(frozen=True)
class Tail:
    m_1: int
    m_2: int
    b_1: int
    b_2: int
    m_3: int
    kappa: int

    @property
    def Q(self) -> int:
        return self.b_1 * 10**self.m_2 + self.b_2

    @property
    def G(self) -> int:
        return self.b_1 * self.b_2

    @property
    def b_3(self) -> int:
        return 10**self.m_3 * self.Q * self.G // self.kappa


def denominator_splits(S: int) -> tuple[tuple[int, int], ...]:
    return tuple((m_1, S - m_1) for m_1 in range(1, S))


def tail_kernel(S: int, m_3_values: range) -> list[Tail]:
    """Enumerate the exact primitive denominator-tail kernel."""

    tails: list[Tail] = []
    for m_1, m_2 in denominator_splits(S):
        for b_1 in range(10 ** (m_1 - 1), 10**m_1):
            for b_2 in range(10 ** (m_2 - 1), 10**m_2):
                Q = b_1 * 10**m_2 + b_2
                G = b_1 * b_2
                QG = Q * G
                for m_3 in m_3_values:
                    for kappa in bounded_divisors(QG, m_3, 10 * QG):
                        if kappa <= QG:
                            continue
                        if kappa * kappa * (kappa + 2 * G) % 10**m_3:
                            continue
                        tails.append(Tail(m_1, m_2, b_1, b_2, m_3, kappa))
    return tails


def position(tail: Tail) -> str:
    b_3_two = valuation(tail.b_3, 2)
    prefix_max = max(valuation(tail.b_1, 2), valuation(tail.b_2, 2))
    if b_3_two == prefix_max == 0:
        return "all-odd"
    if b_3_two > prefix_max:
        return "b3-unique"
    return "prefix-or-tie"


def state_requirements(
    tail: Tail, S: int, prime: int, n_3: int | None = None
) -> tuple[int, int]:
    """Return (resonance n_p, delta-plus n_p-a_p) under the gap lock."""

    if n_3 is None:
        n_3 = 8 * S
    Q = tail.Q
    G = tail.G
    k = valuation(tail.kappa, prime)
    q = valuation(Q, prime)
    g = valuation(G, prime)
    h = valuation(tail.kappa + G, prime)
    f = valuation(tail.kappa + 2 * G, prime)
    lambda_p = 1 if prime == 2 else 0
    return (
        3 * k + f - 2 * tail.m_3 - 2 * q - 2 * h,
        n_3 - 2 * tail.m_3 - 2 * q - h + 2 * k + g + lambda_p,
    )


def state_signature(
    tail: Tail, S: int, n_3: int | None = None
) -> tuple[int | str, ...]:
    """Encode every valuation condition which still needs a prefix value."""

    if n_3 is None:
        n_3 = 8 * S
    tail_position = position(tail)
    if tail_position == "b3-unique":
        if valuation(tail.kappa, 2) <= valuation(tail.G, 2):
            return ("impossible",)
        d_3 = n_3 - tail.m_3
        assert (
            d_3 + valuation(tail.b_3, 2) > valuation(tail.Q, 2)
        )
        two_resonance, two_plus = state_requirements(tail, S, 2, n_3)
        two_minus = (
            valuation(tail.kappa + 2 * tail.G, 2)
            + valuation(tail.kappa, 2)
            - valuation(tail.kappa + tail.G, 2)
            - valuation(tail.G, 2)
            - 1
            - n_3
        )
        two_signature: tuple[int | str, ...] = (
            "b3-unique",
            two_resonance,
            two_plus,
            two_minus,
        )
    elif tail_position == "all-odd":
        two_signature = ("all-odd", tail.m_3 + 1)
    else:
        return ("impossible",)

    if valuation(tail.b_3, 5) == 0:
        five_signature: tuple[int | str, ...] = ("five-unit",)
    else:
        d_3 = n_3 - tail.m_3
        assert (
            d_3 + valuation(tail.b_3, 5) > valuation(tail.Q, 5)
        )
        five_resonance, five_plus = state_requirements(tail, S, 5, n_3)
        five_minus = (
            valuation(tail.kappa + 2 * tail.G, 5)
            + valuation(tail.kappa, 5)
            - valuation(tail.kappa + tail.G, 5)
            - valuation(tail.G, 5)
            - n_3
        )
        five_signature = (
            "five-locked",
            five_resonance,
            five_plus,
            five_minus,
        )
    return two_signature + five_signature


def signature_accepts(
    signature: tuple[int | str, ...],
    n_2: np.ndarray,
    a_2: np.ndarray,
    n_5: np.ndarray,
    a_5: np.ndarray,
) -> np.ndarray:
    """Evaluate the exhaustive p-adic-state disjunction for one signature."""

    if signature[0] == "b3-unique":
        two_resonance = int(signature[1])
        two_plus = int(signature[2])
        two_minus = int(signature[3])
        accepted = (
            (n_2 == two_resonance)
            | (n_2 - a_2 == two_plus)
            | (a_2 == two_minus)
        )
        five_offset = 4
    else:
        assert signature[0] == "all-odd"
        accepted = n_2 >= int(signature[1])
        five_offset = 2

    if signature[five_offset] == "five-unit":
        return accepted

    assert signature[five_offset] == "five-locked"
    five_resonance = int(signature[five_offset + 1])
    five_plus = int(signature[five_offset + 2])
    five_minus = int(signature[five_offset + 3])
    return accepted & (
        (n_5 == five_resonance)
        | (n_5 - a_5 == five_plus)
        | (a_5 == five_minus)
    )


@dataclass
class PrefixCounts:
    digit_pairs: int = 0
    coprime_pairs: int = 0
    squarefree_pairs: int = 0
    valuation_tail_pairs: int = 0
    nonnegative_discriminants: int = 0
    square_discriminants: int = 0


def check_dominant_prefixes(
    S: int, dominant: list[Tail], n_3: int | None = None
) -> tuple[PrefixCounts, list[tuple[int, ...]]]:
    """Enumerate the genuinely finite dominant prefix box exactly."""

    if n_3 is None:
        n_3 = 8 * S
    by_denominator: dict[
        tuple[int, int, int, int], dict[int, list[Tail]]
    ] = defaultdict(lambda: defaultdict(list))
    for tail in dominant:
        signature = state_signature(tail, S, n_3)
        if signature == ("impossible",):
            continue
        by_denominator[(tail.m_1, tail.m_2, tail.b_1, tail.b_2)][
            tail.m_3
        ].append(tail)

    counts = PrefixCounts()
    squares: list[tuple[int, ...]] = []
    processed = 0

    for (m_1, m_2, b_1, b_2), by_m_3 in by_denominator.items():
        processed += 1
        if S == 3 and processed % 200 == 0:
            print(f"  checked {processed}/{len(by_denominator)} denominator pairs")

        Q = b_1 * 10**m_2 + b_2
        G = b_1 * b_2
        for n_1 in range(1, S + 2):
            for n_2_digits in range(1, S + 3 - n_1):
                s_1 = n_1 - m_1
                s_2 = n_2_digits - m_2
                relevant_m_3 = [
                    m_3
                    for m_3 in by_m_3
                    if n_3 - m_3 >= max(s_1, s_2)
                ]
                if not relevant_m_3:
                    continue

                a_1_values = np.arange(
                    10 ** (n_1 - 1), 10**n_1, dtype=np.int64
                )
                a_2_values = np.arange(
                    10 ** (n_2_digits - 1), 10**n_2_digits, dtype=np.int64
                )
                a_1 = np.repeat(a_1_values, a_2_values.size)
                a_2_value = np.tile(a_2_values, a_1_values.size)
                counts.digit_pairs += a_1.size

                coprime = (np.gcd(a_1, b_1) == 1) & (
                    np.gcd(a_2_value, b_2) == 1
                )
                a_1 = a_1[coprime]
                a_2_value = a_2_value[coprime]
                counts.coprime_pairs += a_1.size
                if a_1.size == 0:
                    continue

                A_12 = a_1 * 10**n_2_digits + a_2_value
                first_norm = a_1 * b_2
                second_norm = a_2_value * b_1
                N_12 = first_norm * first_norm + second_norm * second_norm
                n_2_values = valuation_array(N_12, 2)
                a_2_values_exact = valuation_array(A_12, 2)
                n_5_values = valuation_array(N_12, 5)
                a_5_values = valuation_array(A_12, 5)

                for m_3 in relevant_m_3:
                    d_3 = n_3 - m_3
                    squarefree = product_less(
                        10**d_3,
                        A_12,
                        40 * Q * Q,
                        N_12,
                    )
                    indices = np.flatnonzero(squarefree)
                    counts.squarefree_pairs += indices.size
                    if indices.size == 0:
                        continue

                    signatures: dict[tuple[int | str, ...], list[Tail]] = (
                        defaultdict(list)
                    )
                    for tail in by_m_3[m_3]:
                        signatures[state_signature(tail, S, n_3)].append(tail)

                    local_n_2 = n_2_values[indices]
                    local_a_2 = a_2_values_exact[indices]
                    local_n_5 = n_5_values[indices]
                    local_a_5 = a_5_values[indices]
                    for signature, tails in signatures.items():
                        accepted = signature_accepts(
                            signature,
                            local_n_2,
                            local_a_2,
                            local_n_5,
                            local_a_5,
                        )
                        accepted_indices = indices[np.flatnonzero(accepted)]
                        counts.valuation_tail_pairs += (
                            accepted_indices.size * len(tails)
                        )
                        for tail in tails:
                            for index in accepted_indices:
                                a_1_exact = int(a_1[index])
                                a_2_exact = int(a_2_value[index])
                                A_12_exact = int(A_12[index])
                                N_12_exact = int(N_12[index])
                                x_value = (
                                    tail.kappa
                                    * G
                                    * A_12_exact
                                    * 10**d_3
                                )
                                discriminant = (
                                    x_value * x_value
                                    - tail.kappa
                                    * (tail.kappa + 2 * G)
                                    * Q
                                    * Q
                                    * N_12_exact
                                )
                                if discriminant < 0:
                                    continue
                                counts.nonnegative_discriminants += 1
                                root = isqrt(discriminant)
                                if root * root == discriminant:
                                    counts.square_discriminants += 1
                                    squares.append(
                                        (
                                            m_1,
                                            m_2,
                                            b_1,
                                            b_2,
                                            n_1,
                                            n_2_digits,
                                            a_1_exact,
                                            a_2_exact,
                                            m_3,
                                            tail.kappa,
                                        )
                                    )

    return counts, squares


EXPECTED = {
    2: {
        "tail_rows": 7407,
        "by_m_3": {
            1: 418,
            2: 1163,
            3: 1459,
            4: 1702,
            5: 1138,
            6: 909,
            7: 364,
            8: 203,
            9: 44,
            10: 7,
        },
        "dominant": 1527,
        "positions": {
            "b3-unique": 1450,
            "all-odd": 32,
            "prefix-or-tie": 45,
        },
        "eligible": 1133,
        "denominator_pairs": 73,
        "prefix_counts": PrefixCounts(
            digit_pairs=1_898_073,
            coprime_pairs=796_260,
            squarefree_pairs=529_523,
            valuation_tail_pairs=703,
            nonnegative_discriminants=703,
            square_discriminants=0,
        ),
    },
    3: {
        "tail_rows": 518268,
        "by_m_3": {
            1: 8554,
            2: 27745,
            3: 48512,
            4: 74970,
            5: 80385,
            6: 86955,
            7: 64478,
            8: 54577,
            9: 32382,
            10: 22246,
            11: 9848,
            12: 5593,
            13: 1490,
            14: 481,
            15: 45,
            16: 5,
            17: 2,
        },
        "dominant": 72092,
        "positions": {
            "b3-unique": 70478,
            "prefix-or-tie": 998,
            "all-odd": 616,
        },
        "eligible": 63393,
        "denominator_pairs": 1574,
        "prefix_counts": PrefixCounts(
            digit_pairs=550_901_574,
            coprime_pairs=221_462_636,
            squarefree_pairs=162_971_443,
            valuation_tail_pairs=38_633,
            nonnegative_discriminants=38_633,
            square_discriminants=0,
        ),
    },
}


def check_slice(S: int) -> None:
    n_3 = 8 * S
    all_tails = tail_kernel(S, range(1, 6 * S + 4))
    by_m_3 = Counter(tail.m_3 for tail in all_tails)

    nondominant_minimum = n_3 - S
    nondominant = [
        tail for tail in all_tails if tail.m_3 >= nondominant_minimum
    ]
    dominant = [tail for tail in all_tails if tail.m_3 >= n_3 - 5 * S]
    positions = Counter(position(tail) for tail in dominant)
    eligible = [
        tail
        for tail in dominant
        if state_signature(tail, S) != ("impossible",)
    ]
    denominator_pairs = len(
        {(tail.m_1, tail.m_2, tail.b_1, tail.b_2) for tail in eligible}
    )

    expected = EXPECTED[S]
    assert len(all_tails) == expected["tail_rows"]
    assert dict(by_m_3) == expected["by_m_3"]
    assert nondominant == []
    assert len(dominant) == expected["dominant"]
    assert dict(positions) == expected["positions"]
    assert len(eligible) == expected["eligible"]
    assert denominator_pairs == expected["denominator_pairs"]

    prefix_counts, squares = check_dominant_prefixes(S, dominant)
    assert prefix_counts == expected["prefix_counts"]
    assert squares == []

    print(
        f"S={S}: tails={len(all_tails)}, non-dominant=0, "
        f"dominant={len(dominant)}, eligible={len(eligible)}, "
        f"valuation-discriminants={prefix_counts.valuation_tail_pairs}, "
        "squares=0"
    )


def main() -> None:
    check_product_comparison()
    print("exact limb product comparison: OK")
    check_slice(2)
    check_slice(3)
    print("DD 27.22 equality-layer certificate: OK")


if __name__ == "__main__":
    main()
