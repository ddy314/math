"""A2-F04: m3=3 and v5(b2)>0, arbitrary m2.

Independent coverage count by coprime interval inclusion-exclusion; direct
cyclic-orbit referee for every C++ stage-one residual; complete bounded
exception by two original quadratic readers. Arbitrary-precision integers.
"""

import argparse
import subprocess
import tempfile
from math import gcd, isqrt
from pathlib import Path

from short_prefix_even import product_reader, rational_roots, sphere_reader
from sympy import divisors, factorint, mobius
from two_digit_tail import orbit, propagate, valuation

U = 1000
EXPECTED = {1: 119936428, 2: 690140}


def coverage_counts(tail_unit_prefix=False):
    result = {}
    for B in (1, 2):
        total = 0
        for b in range(501, 1000):
            if B == 2 and (b % 2 or 6 * b <= 5000):
                continue
            J, g = valuation(b, 5), valuation(b, 2)
            if (J not in (1, 3)) if tail_unit_prefix else (J < 2):
                continue
            b0 = b // (2**g * 5**J)
            firsts = (4, 8) if b % 2 else range(1, 9) if B == 1 else (5, 7, 9, 11, 13)
            tail_count = sum(
                gcd(a, b) == 1
                and (
                    not b % 2
                    or (valuation(a, 2) == 0 if A == 4 else valuation(a, 2) <= 1)
                )
                and (b % 2 or a % 2 == 1)
                and (B == 1 or 5 * a < 6 * b)
                for A in firsts
                for a in range(1000, 2 * b)
            )
            radical = 1
            for p in factorint(10 * b0):
                radical *= p
            terms = [(int(d), int(mobius(d))) for d in divisors(radical)]
            for c in divisors(b):
                c = int(c)
                F, f = valuation(c, 5), valuation(c, 2)
                if (
                    (F != 0)
                    if tail_unit_prefix
                    else (not 0 < F < J or J - F not in (1, 3))
                ):
                    continue
                if b % 2 == 0:
                    if B == 1 and not (
                        (f == 0 and g in (1, 2)) or (f > 0 and g == f + 2)
                    ):
                        continue
                    if B == 2 and not (
                        (f == 1 and g in (2, 3))
                        or (tail_unit_prefix and f > 1 and g == f + 2)
                    ):
                        continue
                scale = 2**g * 5**J
                # k=scale*z with gcd(z,10*b0)=1; exact strict interval.
                low = B * U * c // scale
                high = ((100 * B + 1) * U * c // 10 - 1) // scale
                k_count = sum(mu * (high // d - low // d) for d, mu in terms)
                total += tail_count * k_count
        result[B] = total
    assert result == ({1: 2966809178, 2: 23500070} if tail_unit_prefix else EXPECTED)
    return result


def referee(tag, maximum=499):
    B, A, b, a, c, k = tag
    modulus = k
    for p in (2, 5):
        while modulus % p == 0:
            modulus //= p
    assert gcd(modulus, 10 * b * c) == 1
    values = orbit(modulus)
    roots = {i for i, T in enumerate(values) if (B * U * T + b) % modulus == 0}
    if not roots:
        return True
    period = len(values)
    constraints = {period: roots}
    h = (k + c * U) ** 2 - (10 * c * U) ** 2
    C = A * A * b * b + B * B * a * a
    for p in range(3, maximum + 1):
        if p == 5 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            continue
        powers = orbit(p)
        squares = {n * n % p for n in range(p)}
        length = len(powers)
        primitive = (
            (B * a - A * b) % p == 0 and h % p != 0 and k % p != 0 and b % p != 0
        )
        allowed = {
            i
            for i, T in enumerate(powers)
            if (
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
            return True
        constraints[length] = allowed
        if propagate(constraints):
            return True
    return propagate(constraints)


def bounded_exception():
    # J-F=2: only b=625,F=2,m2=2 remains, and C04 forces M=25.
    rows = 0
    for a in range(1000, 1250):
        if a % 2 == 0 or gcd(a, 625) != 1:
            continue
        rows += 1
        for reader in (product_reader, sphere_reader):
            assert not rational_roots(reader(4, 1, 100, U, 25, a, 625))
    assert rows == 100
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tail-five-unit-prefix", action="store_true")
    tail_unit_prefix = parser.parse_args().tail_five_unit_prefix
    counts = coverage_counts(tail_unit_prefix)
    rows = 0 if tail_unit_prefix else bounded_exception()
    with tempfile.TemporaryDirectory(prefix="a2-three-five-") as directory:
        binary = Path(directory) / "check"
        subprocess.run(
            [
                "g++",
                "-O2",
                "-std=c++20",
                "-Wall",
                "-Wextra",
                str(Path(__file__).with_suffix(".cpp")),
                "-o",
                str(binary),
            ],
            check=True,
        )
        result = subprocess.run(
            [str(binary), "--stage-one", "--expanded"]
            + (["--tail-five-unit-prefix"] if tail_unit_prefix else []),
            check=True,
            capture_output=True,
            text=True,
        )
    remaining = []
    summaries = {}
    for line in result.stdout.splitlines():
        fields = line.split()
        if fields and fields[0] == "RESIDUAL":
            remaining.append(tuple(map(int, fields[1:])))
        elif fields and fields[0] == "SUMMARY":
            summaries[int(fields[1])] = list(map(int, fields[2:]))
    assert {B: summary[0] for B, summary in summaries.items()} == counts
    assert len(remaining) == (117 if tail_unit_prefix else 4)
    if not tail_unit_prefix:
        assert set(remaining) == {
            (1, 4, 725, 1009, 145, 1149275),
            (1, 2, 850, 1311, 85, 581650),
            (1, 5, 850, 1523, 85, 783550),
            (1, 4, 925, 1033, 185, 1431725),
        }
    for tag in remaining:
        assert referee(tag, 601 if tail_unit_prefix else 499), tag
        print(f"independent complete-orbit exclusion: {tag}")
    print(f"coverage={counts}; bounded exceptional quadratics={rows}; legal roots=0")
    print(
        "PASS: "
        + (
            "A2-F07 m3=3,v5(b2)=0,v5(b3)>0"
            if tail_unit_prefix
            else "A2-F04 m3=3,v5(b2)>0"
        )
        + "; arbitrary m2, no exponent cutoff"
    )


if __name__ == "__main__":
    main()
