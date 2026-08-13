"""Mechanical checks for the DD 7S+3 and 8S-1 boundary reductions.

The unbounded arguments are written in Section 27.23.  This script checks the
only small denominator-tail layer not already covered by Sections 25 and
27.22, the exact entrance/t_2=1 inequalities, and the finite constant-core
table used to eliminate t_2 >= 2 for S >= 18.
"""

from __future__ import annotations

from fractions import Fraction
from random import Random

from check_dd_2716 import valuation
from check_dd_2717 import (
    brute_cofactor_count,
    cofactor_survivor_count,
    coprime_cofactor_count,
    valuation_tuples,
)
from check_dd_2722 import tail_kernel


EXPECTED_T2_ONE: dict[int, list[tuple[int, int]]] = {
    18: [(64, 2635), (65, 1125), (66, 715), (67, 225), (68, 42), (69, 14)],
    19: [(68, 1689), (69, 1125), (70, 407), (71, 100), (72, 42), (73, 1)],
    20: [(72, 2040), (73, 861), (74, 279), (75, 145), (76, 16), (77, 0)],
    21: [(76, 1325), (77, 489), (78, 279), (79, 50), (80, 3), (81, 0)],
    22: [(81, 630), (82, 170), (83, 29), (84, 8)],
    23: [(85, 428), (86, 112), (87, 48), (88, 3)],
    24: [(89, 225), (90, 112), (91, 14), (92, 0)],
    25: [(94, 66), (95, 3), (96, 0)],
    26: [(98, 30), (99, 8)],
    27: [(102, 30), (103, 1)],
    28: [(107, 0)],
    29: [(111, 1)],
}


def check_small_tail_layer() -> None:
    tails = tail_kernel(4, range(27, 28))
    assert tails == []
    print("S=4, m_3=27 primitive tail rows = 0")


def check_monotone_power_inequalities() -> None:
    # Section 25: 5**(-S) >= 20 * 10**(-S) once 2**S >= 20.
    assert 2**5 > 20

    # The 5-adic entrance for n_3 = 8S-1 starts at S=18.  The ratio
    # 5**(3S-1) / 10**(2S+1) then grows by 125/100 at every next S.
    assert 5**53 > 10**37

    # Rational logarithm bounds for the exact t_2=1 size window.
    assert 2**1000 > 10**301
    assert 11**500 < 10**521
    compatibility_cap = Fraction(51769, 1700)
    assert 30 < compatibility_cap < 31

    # The coarser prefix-max/all-odd estimate is already below 8S-1 at S=18.
    assert Fraction(29, 4) * 18 + Fraction(20, 3) < 8 * 18 - 1
    print("monotone entrance and two-adic-position inequalities: OK")


def t2_one_kernel() -> list[tuple[int, int]]:
    kernel: list[tuple[int, int]] = []
    for S in range(18, 31):
        lower = Fraction(1000 * S - 3301, 233)
        upper = Fraction(1000 * S + 661, 267)
        for m_3 in range(3 * S - 1, 6 * S + 3):
            if lower < m_3 < upper:
                kernel.append((S, m_3))
    return kernel


def check_t2_one_certificate() -> None:
    expected_kernel = [
        (S, m_3)
        for S, rows in EXPECTED_T2_ONE.items()
        for m_3, _ in rows
    ]
    expected_counts = [
        count for rows in EXPECTED_T2_ONE.values() for _, count in rows
    ]
    kernel = t2_one_kernel()
    assert kernel == expected_kernel
    assert all(m_3 >= 3 * S for S, m_3 in kernel)

    random = Random(2723)
    for _ in range(1000):
        bound = random.randrange(0, 121)
        k_5 = random.randrange(0, 7)
        h_2 = random.randrange(1, 10)
        length = random.randrange(1, 700)
        assert coprime_cofactor_count(
            bound, k_5, h_2, length
        ) == brute_cofactor_count(bound, k_5, h_2, length)

    counts: list[int] = []
    survivors = 0
    for S, m_3 in kernel:
        rows = valuation_tuples(S, m_3)
        counts.append(len(rows))
        survivors += cofactor_survivor_count(S, rows)

    assert counts == expected_counts
    assert len(kernel) == 45
    assert sum(counts) == 15525
    assert survivors == 0
    print("t_2=1 sizes = 45, valuation rows = 15,525, survivors = 0")


def core_rows(j: int) -> list[tuple[int, ...]]:
    """Enumerate the constant c cores forced by double resonance."""

    xi_cap = 2 * 10 ** (5 - 2 * j)
    rows: list[tuple[int, ...]] = []
    for c in range(1, 20):
        u = valuation(c, 2)
        remaining = c // 2**u
        v = valuation(remaining, 5)
        w = remaining // 5**v
        A_2 = 3 * u - 2 * j
        A_5 = 3 * v - 2 * j + 2
        if A_2 < 0 or A_5 < 0:
            continue
        Xi = 2**A_2 * 5**A_5
        if Xi >= xi_cap:
            continue
        gamma_cap = 2**A_2 * 5**A_5 * w
        rows.append((c, u, v, w, A_2, A_5, Xi, gamma_cap))
    return rows


def check_constant_cores() -> None:
    rows_by_j = {j: core_rows(j) for j in range(3)}
    assert [row[0] for row in rows_by_j[0]] == list(range(1, 20))
    assert [row[0] for row in rows_by_j[1]] == list(range(2, 20, 2))
    assert rows_by_j[2] == []

    rho_caps = {0: 4000, 1: 400000}
    expected_gamma_ratios = {0: Fraction(6400), 1: Fraction(64)}
    large_divisor_caps: dict[int, Fraction] = {}
    for j in (0, 1):
        gamma_ratio = max(
            Fraction(gamma_cap, c)
            for c, _, _, _, _, _, _, gamma_cap in rows_by_j[j]
        )
        assert gamma_ratio == expected_gamma_ratios[j]
        large_divisor_caps[j] = 2 * rho_caps[j] * gamma_ratio

    assert large_divisor_caps == {
        0: Fraction(51_200_000),
        1: Fraction(51_200_000),
    }
    assert max(large_divisor_caps.values()) < 10**8
    print(
        "double-resonance cores =",
        {j: len(rows) for j, rows in rows_by_j.items()},
    )
    print("uniform large-divisor cap = 51,200,000 < 10^8")


def main() -> None:
    check_small_tail_layer()
    check_monotone_power_inequalities()
    check_constant_cores()
    check_t2_one_certificate()
    print("DD 27.23 boundary compactification checks: OK")


if __name__ == "__main__":
    main()
