#!/usr/bin/env python3
"""Check the boundary reductions in DD Section 27.17.

The Markdown proof handles the unbounded reductions at n3 = 8S.  This helper
checks two sharply separated pieces:

* the integer arithmetic leading to the eight constant cores in the
  entrance-above t2 >= 2 equality layer;
* the finite t2 = 1 size/valuation kernel for S >= 11, including an exact
  modular count of all admissible decimal cofactors.

It does not enumerate the original DD numerators or denominators, and it does
not cover S <= 10 or the eight unbounded t2 >= 2 core families.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from random import Random


EXPECTED_BY_S: dict[int, list[tuple[int, int]]] = {
    11: [(36, 6636), (37, 3665), (38, 1788), (39, 1233), (40, 428), (41, 112), (42, 48), (43, 3)],
    12: [(40, 5673), (41, 3006), (42, 2186), (43, 903), (44, 306), (45, 161), (46, 25), (47, 0)],
    13: [(44, 4155), (45, 3090), (46, 1386), (47, 531), (48, 306), (49, 66), (50, 3), (51, 0)],
    14: [(49, 2433), (50, 1074), (51, 681), (52, 204), (53, 30), (54, 8)],
    15: [(53, 1955), (54, 1325), (55, 489), (56, 118), (57, 50), (58, 3)],
    16: [(57, 1955), (58, 800), (59, 237), (60, 118), (61, 16), (62, 0)],
    17: [(61, 1518), (62, 558), (63, 322), (64, 75), (65, 7), (66, 1)],
    18: [(66, 715), (67, 225), (68, 42), (69, 14)],
    19: [(70, 407), (71, 100), (72, 42), (73, 1)],
    20: [(74, 279), (75, 145), (76, 16), (77, 0)],
    21: [(79, 50), (80, 3), (81, 0)],
    22: [(83, 29), (84, 8)],
    23: [(87, 48), (88, 3)],
    24: [(91, 14), (92, 0)],
    25: [(96, 0)],
}


def expected_kernel() -> list[tuple[int, int]]:
    return [
        (S, m3)
        for S, values in EXPECTED_BY_S.items()
        for m3, _ in values
    ]


def expected_counts() -> list[int]:
    return [
        count
        for values in EXPECTED_BY_S.values()
        for _, count in values
    ]


def rational_kernel() -> list[tuple[int, int]]:
    """Apply the exact rational m3 window proved for t2 = 1."""

    kernel: list[tuple[int, int]] = []
    compatibility_cap = Fraction(22547, 850)
    for S in range(11, compatibility_cap.numerator // compatibility_cap.denominator + 1):
        lower = Fraction(1000 * S - 2801, 233)
        upper = Fraction(1000 * S + 661, 267)
        for m3 in range(3 * S, 6 * S + 4):
            if lower < m3 < upper:
                kernel.append((S, m3))
    return kernel


def valuation_tuples(S: int, m3: int) -> list[tuple[int, int, int, int, int, int]]:
    """Return the exact bounded valuation rows surviving all height tests."""

    tuples: list[tuple[int, int, int, int, int, int]] = []
    combined_rhs = 2**6 * 11**3 * 10 ** (12 * S + 3)

    # Q,G < 10^S and N12 < 2*10^(4S) give the first three finite boxes.
    # Since k5 <= 3S+1 and m3 >= 3S at this layer,
    # A5 = 3*k5-2*m3 is at most 3S+3.
    for q2 in range(4 * S):
        if 2**q2 >= 10**S:
            continue
        for n2 in range(14 * S + 1):
            if 2**n2 >= 2 * 10 ** (4 * S):
                continue
            for A5 in range(3 * S + 4):
                if (2 * m3 + A5) % 3:
                    continue

                combined_lhs = (
                    10 ** (2 * m3)
                    * 2 ** (4 * m3 + 6 * q2 + 3 * n2)
                    * 5**A5
                )
                if combined_lhs >= combined_rhs:
                    continue

                k5 = (2 * m3 + A5) // 3
                for g2 in range(4 * S):
                    if 2**g2 >= 10**S:
                        continue
                    f2 = 2 * m3 + 2 * q2 + n2 - g2 - 3
                    if f2 < 0:
                        continue
                    if 2 ** (g2 + 1) * 5**k5 >= 10 ** (2 * S + 1):
                        continue
                    if 2**f2 >= 11 * 10 ** (2 * S):
                        continue
                    tuples.append((q2, n2, A5, g2, f2, k5))

    return tuples


def floor_sum(n: int, modulus: int, multiplier: int, offset: int) -> int:
    """Return sum(floor((multiplier*i+offset)/modulus), i=0..n-1)."""

    if n < 0 or modulus <= 0 or multiplier < 0 or offset < 0:
        raise ValueError("floor_sum expects n,a,b >= 0 and modulus > 0")

    answer = 0
    while True:
        if multiplier >= modulus:
            answer += (n - 1) * n * (multiplier // modulus) // 2
            multiplier %= modulus
        if offset >= modulus:
            answer += n * (offset // modulus)
            offset %= modulus

        top = multiplier * n + offset
        if top < modulus:
            return answer
        n = top // modulus
        offset = top % modulus
        modulus, multiplier = multiplier, modulus


def count_residue_lt(bound: int, multiplier: int, modulus: int, limit: int) -> int:
    """Count 1 <= u <= bound with multiplier*u mod modulus < limit."""

    if bound <= 0 or limit <= 0:
        return 0
    if limit >= modulus:
        return bound
    above_or_equal = floor_sum(
        bound,
        modulus,
        multiplier,
        multiplier + modulus - limit,
    ) - floor_sum(bound, modulus, multiplier, multiplier)
    return bound - above_or_equal


def count_cyclic_residues(
    bound: int,
    multiplier: int,
    modulus: int,
    start: int,
    length: int,
) -> int:
    """Count residues in the cyclic interval [start,start+length)."""

    if bound <= 0 or length <= 0:
        return 0
    if length >= modulus:
        return bound

    start %= modulus
    end = start + length
    if end <= modulus:
        return count_residue_lt(bound, multiplier, modulus, end) - count_residue_lt(
            bound, multiplier, modulus, start
        )
    return (
        bound
        - count_residue_lt(bound, multiplier, modulus, start)
        + count_residue_lt(bound, multiplier, modulus, end - modulus)
    )


def coprime_cofactor_count(
    bound: int,
    k5: int,
    h2: int,
    interval_length: int,
) -> int:
    """Count admissible u without iterating through the decimal cofactor box."""

    if bound <= 0 or h2 < 1 or interval_length <= 0:
        return 0

    half_period = 2**h2
    period = 2 * half_period
    multiplier = 5**k5
    length = min(interval_length, period)
    start = (half_period - length) % period

    def unrestricted(divisor: int) -> int:
        return count_cyclic_residues(
            bound // divisor,
            multiplier * divisor,
            period,
            start,
            length,
        )

    # Inclusion-exclusion removes u divisible by 2 or 5.
    return unrestricted(1) - unrestricted(2) - unrestricted(5) + unrestricted(10)


def interval_contains_odd_multiple(lo: int, hi: int, half_period: int) -> bool:
    """Whether [lo,hi] contains half_period times a positive odd integer."""

    first = (lo + half_period - 1) // half_period
    if first % 2 == 0:
        first += 1
    return first * half_period <= hi


def brute_cofactor_count(bound: int, k5: int, h2: int, length: int) -> int:
    """Small reference implementation used only to test the modular counter."""

    multiplier = 5**k5
    half_period = 2**h2
    return sum(
        gcd(u, 10) == 1
        and interval_contains_odd_multiple(
            multiplier * u + 1,
            multiplier * u + length,
            half_period,
        )
        for u in range(1, bound + 1)
    )


def cofactor_survivor_count(
    S: int,
    tuples: list[tuple[int, int, int, int, int, int]],
) -> int:
    """Count all valuation/cofactor pairs surviving the v2 interval."""

    G_max = 10**S - 1
    kappa_max = 10 * (10**S - 1) * G_max
    total = 0
    for _, _, _, g2, f2, k5 in tuples:
        h2 = f2 - g2 - 1
        if h2 < 1:
            continue
        base = 2 ** (g2 + 1) * 5**k5
        bound = kappa_max // base
        interval_length = G_max // 2**g2
        total += coprime_cofactor_count(bound, k5, h2, interval_length)
    return total


def main() -> None:
    # Exact entrance and position comparisons used before the finite kernel.
    assert 5**33 > 10**23
    assert 5**30 < 10**21
    assert Fraction(29, 4) * 9 + Fraction(20, 3) < 8 * 9
    assert Fraction(22547, 850) < 27
    assert 5 ** (3 * 2 + 2) > 10 ** (2 * 2 + 1)

    # At t2 >= 2 equality, m3=3S+1 would force A5=0 but make
    # 3*k5=6S+2 impossible.  The remaining m3=3S core has c<9.
    assert all((6 * S + 2) % 3 for S in range(2, 20))
    core_data = {
        c: (1 + 3 * valuation(c, 2), 3 * valuation(c, 5))
        for c in range(1, 9)
    }
    assert core_data == {
        1: (1, 0),
        2: (4, 0),
        3: (1, 0),
        4: (7, 0),
        5: (1, 3),
        6: (4, 0),
        7: (1, 0),
        8: (10, 0),
    }

    # Validate the logarithmic modular counter against direct enumeration.
    random = Random(2717)
    for _ in range(1000):
        bound = random.randrange(0, 121)
        k5 = random.randrange(0, 7)
        h2 = random.randrange(1, 10)
        length = random.randrange(1, 700)
        assert coprime_cofactor_count(bound, k5, h2, length) == brute_cofactor_count(
            bound, k5, h2, length
        )

    kernel = rational_kernel()
    assert kernel == expected_kernel()

    counts: list[int] = []
    survivor_count = 0
    for index, (S, m3) in enumerate(kernel, start=1):
        tuples = valuation_tuples(S, m3)
        counts.append(len(tuples))
        survivor_count += cofactor_survivor_count(S, tuples)
        if index % 10 == 0 or index == len(kernel):
            print(
                f"checked {index}/{len(kernel)} sizes; survivors = {survivor_count}",
                flush=True,
            )

    assert counts == expected_counts()
    assert len(kernel) == 70
    assert sum(counts) == 51828
    assert sum(count > 0 for count in counts) == 63
    assert survivor_count == 0

    print(f"t2=1 size pairs = {len(kernel)}")
    print(f"valuation rows = {sum(counts)} ({sum(count > 0 for count in counts)} nonempty sizes)")
    print(f"cofactor-interval survivors = {survivor_count}")
    print(f"t2>=2 constant cores = {core_data}")
    print("DD 27.17 boundary checks: OK")


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value) for a positive integer."""

    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


if __name__ == "__main__":
    main()
