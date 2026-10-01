#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0264; see history/sources.json.
"""

from pathlib import Path
from math import gcd, isqrt
import subprocess
import tempfile

import sympy as sp

PRIMES = (17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


def check_identity_and_funnel() -> None:
    M, j, Q0, Z, a1, J = sp.symbols("M j Q0 Z a1 J", nonzero=True)
    a2 = Z * a1 - J
    F0 = 1 + M**2 * Q0 / j
    B = M * (j * Z * a1 - (M**2 * (Q0 - 1) + j) * J)
    discriminant = (F0 * B - j * M * a2) ** 2 - (F0**2 - 1) * (
        B**2 + j**2 * M**2 * a1**2
    )
    normalized = M**2 * ((Q0 * Z * a1 - J) ** 2 - Q0**2 * (a1**2 + a2**2)) - (
        2 * j * Q0 * (a1**2 + a2**2)
    )
    assert sp.expand(discriminant - M**4 * normalized) == 0
    assert sp.factorint(100001) == {11: 1, 9091: 1}
    states = []
    for delta in range(3, 5):
        for divisor in sp.divisors(100001):
            if len(str(divisor)) == 2 * delta - 4 and divisor % 20 in (11, 19):
                states.append((delta, divisor))
    assert states == [(3, 11), (4, 9091)]


def check_survivors(path: Path) -> None:
    count = 0
    square_classes = {p: {x * x % p for x in range(p)} for p in PRIMES}
    for line in path.read_text().splitlines():
        delta, j, d, k, a1, J, reported = map(int, line.split())
        E, M, Z, Q0 = 10**4, 10**delta, 10**k, 100001
        assert (delta, j) in ((3, 11), (4, 9091))
        assert 1 <= k <= (3 * delta + 1 if d == 0 else 2)
        assert E * 10**d <= a1 < E * 10 ** (d + 1)
        a2 = Z * a1 - J
        assert E * Z <= a2 < 10 * E * Z
        assert J >= 1 and gcd(a1, E) == gcd(a2, E) == 1
        F0, C = 1 + M**2 * (Q0 // j), M**2 * (Q0 - 1)
        B = M * (j * Z * a1 - (C + j) * J)
        normalized = M**2 * ((Q0 * Z * a1 - J) ** 2 - Q0**2 * (a1**2 + a2**2)) - (
            2 * j * Q0 * (a1**2 + a2**2)
        )
        original = (F0 * B - j * M * a2) ** 2 - (F0**2 - 1) * (
            B**2 + j**2 * M**2 * a1**2
        )
        assert normalized == reported and original == M**4 * normalized
        assert all(normalized % p in square_classes[p] for p in PRIMES)
        assert normalized < 0 or isqrt(normalized) ** 2 != normalized
        count += 1
    assert count == 1377
    print("PASS: independent Python arithmetic for all 1377 sieve survivors")


def certify() -> None:
    check_identity_and_funnel()
    source = Path(__file__).with_suffix(".cpp")
    with tempfile.TemporaryDirectory(prefix="a1-pure-e4-") as temporary:
        executable = Path(temporary) / "certificate"
        survivors = Path(temporary) / "survivors.txt"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)], check=True
        )
        subprocess.run([str(executable), str(survivors)], check=True)
        check_survivors(survivors)
    print("PASS: symbolic normalization and exact divisor funnel")


if __name__ == "__main__":
    certify()
