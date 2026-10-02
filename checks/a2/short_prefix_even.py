"""A2-G08/F03: effective bounds and complete bounded even-tail recovery.

The theorem bounds m2 for prefix binary dominance and for tail dominance
with v2(b2) >= v2(b1)+m2. The certificate covers m3=3..6 in precisely those
two classes, not all even tails. Python integers have arbitrary precision.
An integer product-denominator reader and an lcm-sphere reader independently
recover the original quadratic; every row and every rational root is compared.
"""

import argparse
import subprocess
import tempfile
from collections import Counter
from fractions import Fraction
from functools import cache
from math import gcd, isqrt, lcm
from pathlib import Path

from sympy import divisors, factorint, mobius


def vp(value, prime):
    assert value > 0
    depth = 0
    while value % prime == 0:
        value //= prime
        depth += 1
    return depth


def bounds(m3):
    U = 10**m3
    G = (U - 1).bit_length() - 1
    H = 0
    while 3 * 2 ** (H + 1) < 5**m3:
        H += 1
    assert 2**G <= U - 1 < 2 ** (G + 1)
    assert 3 * 2**H < 5**m3 <= 3 * 2 ** (H + 1)
    return G, H


def denominators(m3):
    U = 10**m3
    G, H = bounds(m3)
    result = []
    for B in (1, 2):
        e = vp(B, 2)
        for m2 in range(2, max(H - e, G - e - 2) + 1):
            T = 10**m2
            for b in range(U // 2 + 2, U, 2):
                if B == 2 and 6 * b <= 5 * U:
                    continue
                g = vp(b, 2)
                prefix = m2 <= H - e and g == e + m2 + m3
                high = m2 <= G - e - 2 and g >= e + m2 + 2
                if not (prefix or high):
                    continue
                # C04 is necessary: b2 divides lcm(B,b3,BTU+b3).
                for M in divisors(lcm(B, b, B * T * U + b)):
                    M = int(M)
                    if not T // 10 <= M < T:
                        continue
                    f = vp(M, 2)
                    is_prefix = prefix and f >= g + 2
                    is_high = high and f >= e + m2 and g >= f + 2
                    if not (is_prefix or is_high):
                        continue
                    E = max(e, f, g)
                    assert (e, f, g).count(E) == 1 and E >= 3
                    assert (e, f, g).count(E - 1) % 2 == 0
                    if vp((B * T + M) * U + b, 2) != E:
                        continue
                    F, J = vp(M, 5), vp(b, 5)
                    if not ((F, J) == (0, 0) or J > F):
                        continue
                    result.append((B, m2, M, b, is_prefix))
    assert len(result) == len(set(result))
    return result


def product_reader(A, B, T, U, M, a, b):
    beta = (B * T + M) * U + b
    D = (B * M * b) ** 2
    L = A * T * U + a
    return (
        beta**2 * (B * b) ** 2 - (10 * U) ** 2 * D,
        -2 * L * 10 * U * D,
        beta**2 * ((A * M * b) ** 2 + (a * B * M) ** 2) - L**2 * D,
    )


def sphere_reader(A, B, T, U, M, a, b):
    # beta^2 * sum(yi^2) = (q*alpha)^2, yi=q*ai/bi.
    q = lcm(B, M, b)
    beta = (B * T + M) * U + b
    h0 = q * (A * T * U + a)
    h1 = q * 10 * U
    y1, y3 = q * A // B, q * a // b
    return (
        (beta * (q // M)) ** 2 - h1**2,
        -2 * h0 * h1,
        beta**2 * (y1**2 + y3**2) - h0**2,
    )


def rational_roots(coefficients):
    c2, c1, c0 = coefficients
    assert c2 != 0
    discriminant = c1 * c1 - 4 * c2 * c0
    if discriminant < 0:
        return set()
    root = isqrt(discriminant)
    if root * root != discriminant:
        return set()
    return {Fraction(-c1 + sign * root, 2 * c2) for sign in (-1, 1)}


def tail_window(A, B, T, M, b, U):
    x = Fraction(M, T)
    cap = (A + 1) ** 2 / (B + x) ** 2 - Fraction(A * A, B * B) - 1 / (100 * x * x)
    if cap <= 0:
        return U - 1, 0, 1
    num, den = (cap * b * b).as_integer_ratio()
    upper = min(isqrt((num - 1) // den), 2 * b - 1 if B == 1 else (6 * b - 1) // 5)
    return upper, num, den


def certificate(m3):
    U = 10**m3
    states = denominators(m3)
    counts = Counter()
    projections = []
    for B, m2, M, b, prefix in states:
        T = 10**m2
        for A in range(1, 9) if B == 1 else (5, 7, 9, 11, 13):
            # G01: F increases on the entire legal 0<y<1 interval.
            upper, cap_num, cap_den = tail_window(A, B, T, M, b, U)
            for a in range(U | 1, upper + 1, 2):
                if gcd(a, b) != 1:
                    continue
                assert a * a * cap_den < cap_num
                counts["rows"] += 1
                counts["prefix" if prefix else "tail-high"] += 1
                left = product_reader(A, B, T, U, M, a, b)
                right = sphere_reader(A, B, T, U, M, a, b)
                scale = (B * M * b // lcm(B, M, b)) ** 2
                assert left == tuple(scale * coefficient for coefficient in right)
                roots = rational_roots(left)
                assert roots == rational_roots(right)
                if roots:
                    counts["square"] += 1
                    projections.append((A, B, m2, M, a, b, sorted(roots)))
                for root in roots:
                    if root.denominator != 1:
                        continue
                    N = root.numerator
                    if T // 100 <= N < T // 10 and gcd(N, M) == 1:
                        raise AssertionError((m3, A, B, N, M, a, b, m2))
    expected = {
        3: (114, 8, 16067, 643, 15424, (3, 1, 2, 12, 1203, 944)),
        4: (1814, 22, 2202520, 38013, 2164507, (1, 1, 2, 12, 11289, 9440)),
    }
    total, prefix_count, rows, prefix_rows, high_rows, projection = expected[m3]
    assert len(states) == total and sum(state[-1] for state in states) == prefix_count
    assert counts == Counter(
        rows=rows, prefix=prefix_rows, **{"tail-high": high_rows}, square=1
    )
    assert len(projections) == 1 and projections[0][:6] == projection
    assert all(root.denominator > 1 for root in projections[0][-1])
    print(
        f"m3={m3}: G,H={bounds(m3)}; denominator states={total} ({prefix_count} prefix)"
    )
    print(
        f"quadratics={rows}; prefix={prefix_rows}; tail-high={high_rows}; square=1; legal roots=0"
    )
    print(f"rational projection: {projections[0]}")


@cache
def interval_terms(b):
    radical = 1
    for p in factorint(b):
        radical *= p
    return [(int(d), int(mobius(d))) for d in divisors(radical)]


def large_certificate(m3=5, full_referee=True):
    U = 10**m3
    states = denominators(m3)
    records = []
    for B, m2, M, b, prefix in states:
        T = 10**m2
        for A in range(1, 9) if B == 1 else (5, 7, 9, 11, 13):
            upper, _, _ = tail_window(A, B, T, M, b, U)
            if upper < U:
                continue
            count = sum(mu * (upper // d - (U - 1) // d) for d, mu in interval_terms(b))
            records.append((A, B, T, M, b, U, upper, int(prefix), count))
    expected = {
        5: (23306, 85, 26581, 269940375, 607105, 269333270),
        6: (270385, 333, 297935, 29740339198, 17325104, 29723014094),
    }[m3]
    totals = (
        len(states),
        sum(s[-1] for s in states),
        len(records),
        sum(r[-1] for r in records),
        sum(r[-1] * r[-2] for r in records),
        sum(r[-1] * (1 - r[-2]) for r in records),
    )
    assert totals == expected
    with tempfile.TemporaryDirectory(prefix="a2-short-even-") as directory:
        data = Path(directory) / "rows.txt"
        data.write_text("".join(" ".join(map(str, r)) + "\n" for r in records))
        binary = Path(directory) / "check"
        subprocess.run(
            [
                "g++",
                "-O3",
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
            [str(binary), str(data)], check=True, capture_output=True, text=True
        )
    cpp_projections = []
    summary = None
    for line in result.stdout.splitlines():
        fields = line.split()
        if fields[0] == "SQUARE":
            cpp_projections.append(
                (
                    tuple(map(int, fields[1:7])),
                    {Fraction(*map(int, f.split("/"))) for f in fields[7:]},
                )
            )
        elif fields[0] == "SUMMARY":
            summary = tuple(map(int, fields[1:6]))
    assert summary[:4] == totals[2:] and summary[4] == len(cpp_projections)
    py_projections = []
    for A, B, T, M, b, U, upper, _, expected_rows in records:

        def discriminant(a, A=A, B=B, T=T, U=U, M=M, b=b):
            c2, c1, c0 = sphere_reader(A, B, T, U, M, a, b)
            return c1 * c1 - 4 * c2 * c0

        d0, d1, d2 = map(discriminant, (0, 1, 2))
        quadratic = (d2 - 2 * d1 + d0) // 2
        linear = d1 - d0 - quadratic
        # Independent lcm discriminant vs C++ Q(a); three coefficients
        # certify equality of these degree-two polynomials for every a.
        beta = (B * T + M) * U + b
        c2 = product_reader(A, B, T, U, M, 0, b)[0]
        scale = (B * M * b // lcm(B, M, b)) ** 2
        for a in (0, 1, 2):
            Q = B**4 * b**4 * (A * T * U + a) ** 2 - c2 * (
                A * A * b * b + B * B * a * a
            )
            assert discriminant(a) * scale**2 == 4 * beta**2 * M**2 * Q
        if not full_referee:
            continue
        rows = 0
        for a in range(U + 1, upper + 1, 2):
            if gcd(a, b) != 1:
                continue
            rows += 1
            D = (quadratic * a + linear) * a + d0
            if D < 0:
                continue
            root = isqrt(D)
            if root * root == D:
                roots = rational_roots(sphere_reader(A, B, T, U, M, a, b))
                py_projections.append(((A, B, T, M, a, b), roots))
        assert rows == expected_rows
    if full_referee:
        assert py_projections == cpp_projections
    for (A, B, T, M, a, b), roots in cpp_projections:
        assert roots == rational_roots(sphere_reader(A, B, T, U, M, a, b))
        assert not any(
            N.denominator == 1 and T // 100 <= N < T // 10 and gcd(N.numerator, M) == 1
            for N in roots
        )
    print(
        f"m3={m3}: complete bounds/census={totals}; square projections={len(cpp_projections)}; legal=0"
    )
    for projection in cpp_projections:
        print(f"rational projection: {projection}")
    print(
        f"independent lcm coefficient audit: all {len(records)} rows; full sphere referee={full_referee}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tail-digits", type=int, choices=(0, 6), default=0)
    tail_digits = parser.parse_args().tail_digits
    if tail_digits == 6:
        large_certificate(6, full_referee=False)
        return
    for m3 in (3, 4):
        certificate(m3)
    large_certificate(5)
    print(
        "PASS: A2-F03 complete bounded binary classes; ordinary unbounded class remains"
    )


if __name__ == "__main__":
    main()
