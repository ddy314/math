"""A2-F08: m3=3, odd b3, gcd(b2,b3)=1, arbitrary m2.

Full factor/expanded C++ readers and independent arbitrary-precision Python
orbits on every admissible label. Geometric exclusions and coverage counts
are independently recomputed. No bound on the exponent is used.
"""

import argparse
import subprocess
import tempfile
from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path

from sympy import divisors, factorint, mobius
from two_digit_tail import orbit, prime_data, propagate

U = 1000


def direct_periods(A, b, a, k, period, root):
    h = (k + U) ** 2 - (10 * U) ** 2
    C = A * A * b * b + a * a
    constraints = {period: {root}}
    for index, p in enumerate(
        p
        for p in range(3, 398)
        if p != 5 and all(p % d for d in range(2, isqrt(p) + 1))
    ):
        values, squares = prime_data(p)
        length = len(values)
        common = gcd(period, length)
        primitive = (a - A * b) % p == 0 and h % p and k % p and b % p
        allowed = {
            i
            for i, T in enumerate(values)
            if i % common == root % common
            and (k * k * b * b * (A * U * T + a) ** 2 - h * C * (U * T + b) ** 2) % p
            in squares
            and not (primitive and (U * T + b) % p == 0)
        }
        if length in constraints:
            allowed &= constraints[length]
        if not allowed:
            return True
        constraints[length] = allowed
        if index % 8 == 0 and propagate(constraints):
            return True
    return propagate(constraints)


def python_certificate():
    counts = Counter()
    keys = 0
    for b in range(501, 1000, 2):
        if b % 5 == 0:
            continue
        tails = {
            A: [
                a
                for a in range(1000, 2 * b)
                if gcd(a, b) == 1 and (a % 2 == 1 if A == 4 else a % 4 != 0)
            ]
            for A in (4, 8)
        }
        # Independent direct scan of every integer k, rather than C++ stepping.
        for k in range(U + 1, 10100):
            if gcd(k, 10 * b) != 1 or (k + U) % b:
                continue
            keys += 1
            values = orbit(k)
            roots = {i for i, T in enumerate(values) if (U * T + b) % k == 0}
            assert len(roots) <= 1
            for A in (4, 8):
                x = max(F(U, k), F(1, 10))
                cap = (A + 1) ** 2 / (1 + x) ** 2 - A * A - 1 / (100 * x * x)
                for a in tails[A]:
                    counts["tags"] += 1
                    if F(a * a, b * b) >= cap:
                        counts["geometry"] += 1
                        continue
                    if not roots:
                        counts["integrality"] += 1
                        continue
                    assert direct_periods(A, b, a, k, len(values), next(iter(roots)))
                    counts["periods"] += 1
    assert keys == 982
    assert counts == Counter(
        tags=476207, geometry=407864, integrality=42660, periods=25683
    )
    print(f"Python complete original label/orbit reader: keys={keys}; {dict(counts)}")
    return tuple(counts[key] for key in ("tags", "geometry", "integrality", "periods"))


def inventory():
    """Complete allowed tag census; this never asserts existence or emptiness."""
    labels, keys, states = Counter(), Counter(), Counter()
    for b in range(501, 1000, 2):
        if b % 5 == 0:
            continue
        tail_count = sum(
            gcd(a, b) == 1 and (a % 2 == 1 if A == 4 else a % 4 != 0)
            for A in (4, 8)
            for a in range(1000, 2 * b)
        )
        terms = [(int(d), int(mobius(d))) for d in divisors(10 * b)]
        for c in divisors(b):
            c = int(c)
            b0 = b // c
            if gcd(c, b0) != 1 or any(p % 4 == 3 for p in factorint(c)):
                continue
            low, high = U * c + 1, 10100 * c - 1
            count = 0
            for d, mu in terms:
                if mu == 0 or gcd(d, b0) != 1:
                    continue
                residue = (-c * U * pow(d, -1, b0)) % b0 if b0 > 1 else 0
                first, modulus = d * residue, d * b0
                count += mu * ((high - first) // modulus - (low - 1 - first) // modulus)
            name = "coprime" if c == 1 else "all-common" if c == b else "proper-common"
            states[name] += 1
            keys[name] += count
            labels[name] += count * tail_count
    assert states == Counter(coprime=200, **{"proper-common": 78, "all-common": 44})
    assert keys == Counter(
        coprime=982, **{"proper-common": 5782874, "all-common": 117120640}
    )
    assert labels == Counter(
        coprime=476207, **{"proper-common": 2559479281, "all-common": 77670247200}
    )
    for name in ("coprime", "proper-common", "all-common"):
        print(
            f"{name}: denominator supports={states[name]},keys={keys[name]},allowed labels={labels[name]}"
        )
    print("Projection inventory only; noncoprime classes remain open")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", action="store_true")
    if parser.parse_args().inventory:
        inventory()
        return
    counts = python_certificate()
    with tempfile.TemporaryDirectory(prefix="a2-odd-coprime-") as directory:
        binary = Path(directory) / "check"
        subprocess.run(
            [
                "g++",
                "-O2",
                "-std=c++20",
                "-Wall",
                "-Wextra",
                "-fsanitize=undefined",
                "-fno-sanitize-recover=all",
                str(Path(__file__).with_suffix(".cpp")),
                "-o",
                str(binary),
            ],
            check=True,
        )
        outputs = [
            subprocess.run(
                [str(binary), *args], check=True, capture_output=True, text=True
            ).stdout
            for args in ([], ["--expanded"])
        ]
    expected = "SUMMARY 1 " + " ".join(map(str, counts)) + " 0\n"
    assert outputs == [expected, expected]
    print(expected.strip())
    print("PASS: A2-F08 whole odd m3=3 coprime-denominator domain; no exponent cutoff")


if __name__ == "__main__":
    main()
