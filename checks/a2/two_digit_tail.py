"""A2-F02: independent arbitrary-precision referee and bounded recovery.

C++ enumerates every bounded tail label with complete exponent periods.
Python independently recomputes the coverage counts and referees every
stage-one residual using direct cyclic orbits, primitive recovery, and
exact original quadratics. All executables/output remain in /tmp.
"""

import subprocess
import tempfile
from collections import Counter
from functools import cache, reduce
from math import gcd, isqrt, lcm
from pathlib import Path

from sympy import divisors

U = 100
EXPECTED = {0: 33683610, 1: 13541128, 2: 207750}


def valuation(value, prime):
    depth = 0
    while value % prime == 0:
        value //= prime
        depth += 1
    return depth


def orbit(modulus):
    assert gcd(modulus, 10) == 1
    first = 100 % modulus
    values = [first]
    value = first * 10 % modulus
    while value != first:
        values.append(value)
        value = value * 10 % modulus
    return values


@cache
def prime_data(prime):
    return orbit(prime), {n * n % prime for n in range(prime)}


def primes():
    return [
        p
        for p in range(3, 398)
        if p != 5 and all(p % d for d in range(2, isqrt(p) + 1))
    ]


def propagate(constraints):
    changed = True
    while changed:
        changed = False
        for period, allowed in list(constraints.items()):
            for other_period, other in constraints.items():
                common = gcd(period, other_period)
                possible = {n % common for n in other}
                reduced = {n for n in allowed if n % common in possible}
                if len(reduced) < len(allowed):
                    changed = True
                    allowed = reduced
                    constraints[period] = reduced
                    if not reduced:
                        return True
    return False


def primitive_coefficients(tag):
    B, A, b, a, c, k = tag
    lam = k + c * U
    h = lam**2 - (10 * c * U) ** 2
    C = A * A * b * b + B * B * a * a
    coefficients = [
        B * B * k * k * b * b * h,
        -20 * k * k * b * b * c * c * B * B * A * U * U,
        -20 * k * k * b * b * c * c * B * B * U * a,
        c * c * B * B * U * U * (lam * lam * C - k * k * b * b * A * A),
        2 * lam * lam * C * c * c * B * U * b
        - 2 * k * k * b * b * c * c * B * B * A * U * a,
        lam * lam * C * c * c * b * b - k * k * b * b * c * c * B * B * a * a,
    ]
    content = reduce(gcd, coefficients)
    return [coefficient // content for coefficient in coefficients]


def binary_fallback(tag):
    B, _, b, _, c, k = tag
    if any(c * (B * U * 10**m2 + b) % k == 0 for m2 in range(2, 6)):
        return False
    coefficients = primitive_coefficients(tag)
    return all(
        (coefficients[0] * n * n + coefficients[2] * n + coefficients[5]) % 64
        for n in range(64)
    )


def referee(tag):
    B, A, b, a, c, k = tag
    modulus = k
    for p in (2, 5):
        assert valuation(c, p) + valuation(b, p) >= valuation(k, p)
        while modulus % p == 0:
            modulus //= p
    assert gcd(c, modulus) == 1
    values = orbit(modulus)
    roots = {i for i, value in enumerate(values) if (B * U * value + b) % modulus == 0}
    if not roots:
        return "integrality"
    assert len(roots) == 1
    period = len(values)
    root = next(iter(roots))
    constraints = {period: roots}
    h = (k + c * U) ** 2 - (10 * c * U) ** 2
    C = A * A * b * b + B * B * a * a
    for index, p in enumerate(primes()):
        values, squares = prime_data(p)
        length = len(values)
        common = gcd(period, length)
        primitive = (
            (B * a - A * b) % p == 0 and h % p != 0 and k % p != 0 and b % p != 0
        )
        allowed = {
            i
            for i, T in enumerate(values)
            if i % common == root % common
            and (
                k * k * B * B * b * b * (A * U * T + a) ** 2
                - h * C * (B * U * T + b) ** 2
            )
            % p
            in squares
            and not (primitive and (B * U * T + b) % p == 0)
        }
        if length in constraints:
            allowed &= constraints[length]
        if not allowed:
            return "periods-and-reducedness"
        constraints[length] = allowed
        if index % 8 == 0 and propagate(constraints):
            return "periods-and-reducedness"
    if propagate(constraints):
        return "periods-and-reducedness"
    return "binary-recovery" if binary_fallback(tag) else None


def coverage_counts():
    result = {}
    for group in range(3):
        B = 2 if group == 2 else 1
        tails = (
            range(51, 100, 2)
            if group == 0
            else range(54, 100, 4)
            if group == 1
            else (84, 92)
        )
        firsts = (
            (2, 4, 6, 8)
            if group == 0
            else range(1, 9)
            if group == 1
            else (5, 7, 9, 11, 13)
        )
        total = 0
        for b in tails:
            J = valuation(b, 5)
            nondecimal = b // (2 ** valuation(b, 2) * 5**J)
            tail_count = sum(
                gcd(a, b) == 1
                and (
                    valuation(a, 2) == (1 if A == 4 else 2 if A == 8 else 0)
                    if group == 0
                    else a % 2 == 1
                )
                and (group != 2 or 5 * a < 6 * b)
                for A in firsts
                for a in range(100, 2 * b)
            )
            for c in range(1, b + 1):
                if b % c or (J and valuation(c, 5) >= J):
                    continue
                if (group == 1 and c % 2 == 0) or (group == 2 and valuation(c, 2) != 1):
                    continue
                wanted_two = 0 if group == 0 else 1 if group == 1 else 2
                k_count = sum(
                    valuation(k, 2) == wanted_two
                    and valuation(k, 5) == J
                    and gcd(k, nondecimal) == 1
                    for k in range(B * U * c + 1, (100 * B + 1) * U * c // 10)
                )
                total += tail_count * k_count
        result[group] = total
    assert result == EXPECTED
    return result


def bounded_even_recovery():
    denominators = []
    for B in (1, 2):
        e = int(B == 2)
        for m2 in range(2, 5 - e):
            T = 10**m2
            for b in range(52, 100, 2):
                if (B == 2 and 6 * b <= 500) or valuation(b, 2) < e + m2 + 2:
                    continue
                for middle in divisors(lcm(B, b, B * T * U + b)):
                    middle = int(middle)
                    if T // 10 <= middle < T and valuation(middle, 2) == e + m2:
                        denominators.append((B, m2, middle, b))
    denominators.extend([(1, 3, 256, 96), (1, 3, 768, 96)])
    assert len(denominators) == 18 and len(set(denominators)) == 18
    rows = 0
    for B, m2, middle, b in denominators:
        T = 10**m2
        beta = (B * T + middle) * U + b
        product = (B * middle * b) ** 2
        for A in range(1, 9) if B == 1 else (5, 7, 9, 11, 13):
            for a in range(100, 2 * b if B == 1 else (6 * b + 4) // 5):
                if gcd(a, b) != 1:
                    continue
                rows += 1
                constant_word = A * T * U + a
                c2 = beta**2 * (B * b) ** 2 - (10 * U) ** 2 * product
                c1 = -2 * constant_word * (10 * U) * product
                c0 = (
                    beta**2 * ((A * middle * b) ** 2 + (a * B * middle) ** 2)
                    - constant_word**2 * product
                )
                assert c2 != 0
                discriminant = c1 * c1 - 4 * c2 * c0
                if discriminant >= 0:
                    root = isqrt(discriminant)
                    assert root * root != discriminant, (B, m2, middle, b, A, a)
    assert rows == 3366
    return rows


def main():
    counts = coverage_counts()
    rows = bounded_even_recovery()
    cpp = Path(__file__).with_suffix(".cpp")
    with tempfile.TemporaryDirectory(prefix="a2-two-tail-") as directory:
        binary = Path(directory) / "check"
        subprocess.run(
            [
                "g++",
                "-O2",
                "-std=c++20",
                "-Wall",
                "-Wextra",
                str(cpp),
                "-o",
                str(binary),
            ],
            check=True,
        )
        result = subprocess.run(
            [str(binary), "--stage-one", "--expanded"],
            check=True,
            capture_output=True,
            text=True,
        )
    summaries = {}
    remaining = []
    for line in result.stdout.splitlines():
        fields = line.split()
        if fields and fields[0] == "SUMMARY":
            summaries[int(fields[1])] = list(map(int, fields[2:]))
        elif fields and fields[0] == "RESIDUAL":
            remaining.append(tuple(map(int, fields[1:])))
    assert set(summaries) == set(EXPECTED)
    for group, summary in summaries.items():
        assert summary[0] == counts[group]
        actual = sum(
            (0 if tag[2] % 2 else 1 if tag[0] == 1 else 2) == group for tag in remaining
        )
        assert summary[5] == actual
    reasons = Counter()
    for tag in remaining:
        reason = referee(tag)
        assert reason is not None, f"uncovered original-tag supermodel: {tag}"
        reasons[reason] += 1
    print("OK: A2-F02 all two-digit tails: complete label counts", counts)
    print(
        "Independent arbitrary-precision referee:",
        len(remaining),
        "stage-one tags",
        dict(reasons),
    )
    print(
        "Bounded even source/prefix:",
        rows,
        "exact original quadratics, zero square discriminants",
    )
    print(
        "All m2>=2 covered by complete periods and proved bounded/source splits; no exponent cutoff"
    )


if __name__ == "__main__":
    main()
