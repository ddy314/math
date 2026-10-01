#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0612; see history/sources.json.
"""

from argparse import ArgumentParser
from fractions import Fraction as F
from math import gcd, isqrt, lcm
from time import monotonic

from single_digits import (
    factored_roots,
    norm_possible,
    standard_roots,
    verify_reader_parent_algebra,
)


EXPECTED_STATES = (
    (11, 1, 1), (5, 1, 5), (15, 1, 5), (7, 2, 8), (33, 3, 3),
    (5, 5, 1), (15, 5, 1), (85, 5, 1), (255, 5, 1), (265, 5, 3),
    (1, 5, 5), (11, 5, 5), (55, 5, 5), (40, 5, 6), (280, 5, 6),
    (1, 6, 8), (15, 7, 5), (77, 7, 7), (99, 9, 9),
)
EXPECTED_COUNTS = (
    (10_836, 123_570), (648, 1944), (972, 21_816), (80, 990),
    (5688, 56_160), (1280, 5310), (7840, 10_080), (59_200, 738_090),
    (255_128, 1_471_860), (78_200, 558_480), (48, 0), (936, 2592),
    (7776, 80_568), (1440, 1470), (23_280, 67_830), (12, 0),
    (870, 2232), (8644, 91_761), (5688, 56_160),
)


def valuation(n: int, p: int) -> int:
    assert n > 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def prime_factors(n: int) -> list[int]:
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def divisors(n: int) -> list[int]:
    small, large = [], []
    for k in range(1, isqrt(n)+1):
        if n % k == 0:
            small.append(k)
            if k*k != n:
                large.append(n//k)
    return small + large[::-1]


def denominator_states() -> list[tuple[int, int, int]]:
    """Each filter is a necessary condition proved in core section 27.7.5."""
    rows = []
    divisor_count = 0
    max_b1 = 0
    for b2 in range(1, 10):
        for b3 in range(1, 10):
            for b1 in divisors(lcm(b2, b3, 10*b2+b3)):
                divisor_count += 1
                max_b1 = max(max_b1, b1)
                Q = 10*b1+b2
                D = 10*Q+b3
                if 10*Q % b3:
                    continue  # General one-digit-tail source lemma.
                depths = [valuation(b, 2) for b in (b1, b2, b3)]
                e = max(depths)
                if e and (depths.count(e) != 1 or b3 % 2 or valuation(D, 2) != e):
                    continue
                if e >= 2 and depths.count(e-1) == 1:
                    continue
                bad = False
                for p in prime_factors(lcm(b1, b2, b3)):
                    depths = [valuation(b, p) for b in (b1, b2, b3)]
                    e = max(depths)
                    count_max = depths.count(e)
                    if count_max == 1 or (count_max == 2 and p % 4 == 3):
                        if valuation(D, p) < e:
                            bad = True
                            break
                if bad:
                    continue
                r = min(valuation(b, 3) for b in (b1, b2, b3))
                c1, c2, c3 = (b//3**r for b in (b1, b2, b3))
                if (c1*c2+c2*c3+c3*c1) % 9 in (3, 6):
                    continue  # Original denominator Gaussian norm.
                if b3 == 5 and b1*b2 % 5 and Q % 25 != 24:
                    continue  # Unique-five-tail, n3>=2.
                rows.append((b1, b2, b3))
    assert divisor_count == 994 and max_b1 == 6408
    assert tuple(rows) == EXPECTED_STATES
    print(f"Complete divisor domain: {divisor_count} triples, max b1={max_b1}; "
          f"proved filters leave {len(rows)} states, max b1={max(b[0] for b in rows)}")
    return rows


def strict_integer_cap(x: F) -> int:
    """Largest integer strictly below x, preserving exact endpoint behavior."""
    return (x.numerator-1)//x.denominator


def high_plan(b1: int, b2: int, b3: int) -> dict[str, int]:
    D, q = 100*b1+10*b2+b3, lcm(b1, b2, b3)
    N = 2
    while 10**N*b2 <= D:
        N += 1
    Y0 = 10**N
    n2cap = 0
    bound_x = F(D, b3)+F(D, b1*Y0)
    while 10**(n2cap+1) < bound_x:
        n2cap += 1
    a1cap = strict_integer_cap(F(D, b3)/(10-F(D, b1*Y0)))
    a2cap = 10**n2cap-1
    a3cap = strict_integer_cap(F(b3*q, 2)*(F(a1cap, b1)**2+F(a2cap, b2)**2))
    return dict(N=N, n2cap=n2cap, a1cap=a1cap, a2cap=a2cap,
                a3cap=a3cap, n3cap=len(str(a3cap)) if a3cap > 0 else 0)


def low_plan(b1: int, b2: int, b3: int, n3: int) -> dict[str, int]:
    D, q, Y = 100*b1+10*b2+b3, lcm(b1, b2, b3), 10**n3
    assert F(10*Y, D)-F(1, b1) > 0
    a1cap = strict_integer_cap((F(10, b2)+F(Y-1, b3))/(F(10*Y, D)-F(1, b1)))
    a2cap = strict_integer_cap(F(b2*q, 2)*(F(a1cap, b1)**2+F(Y-1, b3)**2))
    return dict(n3=n3, a1cap=a1cap, a2cap=a2cap,
                n2cap=len(str(a2cap)) if a2cap > 0 else 0)


def certificate(reader_name: str, show_bounds: bool) -> None:
    reader = standard_roots if reader_name == "standard" else factored_roots
    start, total = monotonic(), 0
    rows = denominator_states()
    for index, (b1, b2, b3) in enumerate(rows):
        D, q = 100*b1+10*b2+b3, lcm(b1, b2, b3)
        c1, c2, c3 = q//b1, q//b2, q//b3
        high = high_plan(b1, b2, b3)
        lows = [low_plan(b1, b2, b3, n3) for n3 in range(2, high["N"])]
        if show_bounds:
            print((b1, b2, b3), "high", high, "low", lows)
        counts = [0, 0]

        def accept(a1: int, a2: int, a3: int, n2: int, n3: int) -> None:
            word = a1*10**(n2+n3)+a2*10**n3+a3
            assert q*q*word*word == D*D*(c1*c1*a1*a1+c2*c2*a2*a2+c3*c3*a3*a3)
            raise AssertionError(f"Exact solution: {(b1, b2, b3)}, {(a1, a2, a3)}")

        for n3 in range(high["N"], high["n3cap"]+1):
            Y = 10**n3
            for n2 in range(1, high["n2cap"]+1):
                X = 10**n2
                a1cap = strict_integer_cap(F(D, b3)/(X-F(D, b1*Y)))
                for a1 in range(1, a1cap+1):
                    if gcd(a1, b1) != 1:
                        continue
                    for a2 in range(X//10, X):
                        if gcd(a2, b2) != 1:
                            continue
                        counts[0] += 1
                        known = (a1*X+a2)*Y
                        other = c1*c1*a1*a1+c2*c2*a2*a2
                        for a3 in reader(q, D, c3, 1, known, other):
                            if Y//10 <= a3 < Y and gcd(a3, b3) == 1:
                                accept(a1, a2, a3, n2, n3)

        for low in lows:
            n3 = low["n3"]
            Y = 10**n3
            for n2 in range(1, low["n2cap"]+1):
                X = 10**n2
                a1cap = strict_integer_cap((F(X, b2)+F(Y-1, b3))/(F(X*Y, D)-F(1, b1)))
                for a1 in range(1, a1cap+1):
                    if gcd(a1, b1) != 1:
                        continue
                    for a3 in range(Y//10, Y):
                        if gcd(a3, b3) != 1:
                            continue
                        counts[1] += 1
                        known = a1*X*Y+a3
                        other = c1*c1*a1*a1+c3*c3*a3*a3
                        for a2 in reader(q, D, c2, Y, known, other):
                            if X//10 <= a2 < X and gcd(a2, b2) == 1:
                                accept(a1, a2, a3, n2, n3)
        assert tuple(counts) == EXPECTED_COUNTS[index]
        total += sum(counts)
        print((b1, b2, b3), "quadratic rows high/low", counts, "exact hits=0")
    assert total == 3_759_479
    print(f"TOTAL {total} quadratic rows, exact hits=0, reader={reader_name}, seconds={monotonic()-start:.3f}")
    print("Entire DD layer m2=m3=1 closed after proved global bounds; general DD remains open")


TWO_DIGIT_EIGHT_STATES = (
    (288, 28, 8), (448, 44, 8), (160, 60, 8), (3040, 60, 8), (3, 64, 8),
)
TWO_DIGIT_EIGHT_COUNTS = (
    (107846, 6787125, 84410, 6776775),
    (262360, 13535280, 228475, 13528980),
    (39248, 453150, 29648, 414900),
    (1436264, 80925525, 1271144, 8925525),
    (1165, 225, 880, 225),
)


def two_digit_eight_states(tail: int = 8) -> list[tuple[int, int, int]]:
    """Same public word/sphere filters, now with m2=2 and b3=4/8."""
    assert tail in (4, 8)
    rows, count, max_b1 = [], 0, 0
    for b2 in range(10, 100):
        for b1 in divisors(lcm(b2, tail, 10*b2+tail)):
            count += 1
            max_b1 = max(max_b1, b1)
            bs, Q = (b1, b2, tail), 100*b1+b2
            D = 10*Q+tail
            if 10*Q % tail:
                continue
            depths = [valuation(b, 2) for b in bs]
            e = max(depths)
            if depths.count(e) != 1 or valuation(D, 2) != e:
                continue
            if e >= 2 and depths.count(e-1) == 1:
                continue
            bad = False
            for p in prime_factors(lcm(*bs)):
                depths = [valuation(b, p) for b in bs]
                e, multiplicity = max(depths), depths.count(max(depths))
                if ((multiplicity == 1 or (multiplicity == 2 and p % 4 == 3))
                        and valuation(D, p) < e):
                    bad = True
                    break
            if bad:
                continue
            r = min(valuation(b, 3) for b in bs)
            c1, c2, c3 = (b//3**r for b in bs)
            if (c1*c2+c2*c3+c3*c1) % 9 in (3, 6):
                continue
            rows.append(bs)
    if tail == 8:
        assert count == 3369 and max_b1 == 395208
        assert tuple(rows) == TWO_DIGIT_EIGHT_STATES
    else:
        assert count == 2818 and max_b1 == 196812
        assert tuple(rows) == ((144, 14, 4), (224, 22, 4), (80, 30, 4), (1520, 30, 4))
    print(f"Two-digit/tail-{tail} domain: {count} divisor triples, max b1={max_b1}; "
          f"proved filters leave {len(rows)} states")
    return rows


def verify_four_tail_scaling() -> None:
    """Transfer the entire tail-4 projection to already-certified tail-8."""
    for bs in two_digit_eight_states(4):
        doubled = tuple(2*b for b in bs)
        assert doubled in TWO_DIGIT_EIGHT_STATES
        assert all(b % 2 == 0 for b in bs)
        assert all(prime_factors(b) == prime_factors(2*b) for b in bs)
        assert len(str(bs[1])) == len(str(doubled[1])) == 2
        assert len(str(bs[2])) == len(str(doubled[2])) == 1
        q, new_q = lcm(*bs), lcm(*doubled)
        d, new_d = 1000*bs[0]+10*bs[1]+bs[2], 1000*doubled[0]+10*doubled[1]+doubled[2]
        assert new_d == 2*d and new_q == 2*q
        assert tuple(q//b for b in bs) == tuple(new_q//b for b in doubled)
    print("PASS: all tail-4 states transfer exactly to tail-8; word parent scales by 2, sphere unchanged")


def two_digit_eight_plans(bs: tuple[int, int, int]) -> tuple[dict, list[dict]]:
    b1, b2, b3 = bs
    D, q, N = 1000*b1+10*b2+b3, lcm(*bs), 3
    while 10**N*b2 <= D:
        N += 1
    Y0, J = 10**N, 0
    while 10**(J+1) < F(D, b3)+F(D, b1*Y0):
        J += 1
    A = strict_integer_cap(F(D, b3)/(10-F(D, b1*Y0)))
    tail = strict_integer_cap(F(b3*q, 2)*(F(A, b1)**2+F(10**J-1, b2)**2))
    high = dict(N=N, n2cap=J, a1cap=A, a3cap=tail, n3cap=len(str(tail)))
    lows = []
    for n3 in range(2, N):
        Y, first_n2 = 10**n3, max(1, 4-n3)
        X0 = 10**first_n2
        assert F(X0*Y, D)-F(1, b1) > 0
        A = strict_integer_cap((F(X0, b2)+F(Y-1, b3))/(F(X0*Y, D)-F(1, b1)))
        second = strict_integer_cap(F(b2*q, 2)*(F(A, b1)**2+F(Y-1, b3)**2))
        lows.append(dict(n3=n3, first_n2=first_n2, a1cap=A,
                         a2cap=second, n2cap=len(str(second))))
    return high, lows


def two_digit_eight_certificate(reader_name: str, show_bounds: bool,
                               prune: bool) -> None:
    """Bounded certificate; the full unbounded reduction is core §27.7.6."""
    reader = standard_roots if reader_name == "standard" else factored_roots
    verify_four_tail_scaling()
    start, total, raw_total = monotonic(), 0, 0
    for index, bs in enumerate(two_digit_eight_states()):
        b1, b2, b3 = bs
        D, q = 1000*b1+10*b2+b3, lcm(*bs)
        c1, c2, c3 = (q//b for b in bs)
        high, lows = two_digit_eight_plans(bs)
        if show_bounds:
            print(bs, "high", high, "low", lows, flush=True)
        counts, raw_counts = [0, 0], [0, 0]

        def accept(a1: int, a2: int, a3: int, X: int, Y: int) -> None:
            assert X*Y > 1000 and Y >= 100
            word = a1*X*Y+a2*Y+a3
            assert q*q*word*word == D*D*(c1*c1*a1*a1+c2*c2*a2*a2+c3*c3*a3*a3)
            raise AssertionError(f"Exact solution: {bs}, {(a1, a2, a3)}")

        for n3 in range(high["N"], high["n3cap"]+1):
            Y = 10**n3
            for n2 in range(1, high["n2cap"]+1):
                X = 10**n2
                A = strict_integer_cap(F(D, b3)/(X-F(D, b1*Y)))
                aa1 = [a for a in range(1, A+1) if gcd(a, b1) == 1]
                aa2 = [a for a in range(X//10, X) if gcd(a, b2) == 1]
                raw_counts[0] += len(aa1)*len(aa2)
                delta = b1*b1*X*X*Y*Y+b2*b2*Y*Y+b3*b3-D*D
                if prune and not norm_possible(delta):
                    continue
                for a1 in aa1:
                    for a2 in aa2:
                        counts[0] += 1
                        for a3 in reader(q, D, c3, 1, (a1*X+a2)*Y,
                                         c1*c1*a1*a1+c2*c2*a2*a2):
                            if Y//10 <= a3 < Y and gcd(a3, b3) == 1:
                                accept(a1, a2, a3, X, Y)
        for low in lows:
            Y = 10**low["n3"]
            aa3 = [a for a in range(Y//10, Y) if gcd(a, b3) == 1]
            for n2 in range(low["first_n2"], low["n2cap"]+1):
                X = 10**n2
                A = strict_integer_cap((F(X, b2)+F(Y-1, b3))/(F(X*Y, D)-F(1, b1)))
                aa1 = [a for a in range(1, A+1) if gcd(a, b1) == 1]
                raw_counts[1] += len(aa1)*len(aa3)
                delta = b1*b1*X*X*Y*Y+b2*b2*Y*Y+b3*b3-D*D
                if prune and not norm_possible(delta):
                    continue
                for a1 in aa1:
                    for a3 in aa3:
                        counts[1] += 1
                        for a2 in reader(q, D, c2, Y, a1*X*Y+a3,
                                         c1*c1*a1*a1+c3*c3*a3*a3):
                            if X//10 <= a2 < X and gcd(a2, b2) == 1:
                                accept(a1, a2, a3, X, Y)
        expected = TWO_DIGIT_EIGHT_COUNTS[index]
        assert tuple(raw_counts) == expected[:2]
        assert tuple(counts) == (expected[2:] if prune else expected[:2])
        raw_total += sum(raw_counts)
        total += sum(counts)
        print(bs, "raw rows", raw_counts, "tested rows", counts, "exact hits=0", flush=True)
    assert raw_total == 103_548_188
    assert total == (31_260_962 if prune else raw_total)
    print(f"TOTAL {total} quadratic rows after {raw_total} bounded rows; "
          f"exact hits=0, reader={reader_name}, length_prune={prune}, "
          f"seconds={monotonic()-start:.3f}")
    print("Scope: m2=2,b3=8,n3>=2,n2+n3>3; general DD remains open")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--reader", choices=("standard", "factored"), default="standard")
    parser.add_argument("--show-bounds", action="store_true")
    parser.add_argument("--tail-eight-second-two", action="store_true")
    parser.add_argument("--no-length-prune", action="store_true")
    parser.add_argument("--four-tail-scaling-only", action="store_true")
    args = parser.parse_args()
    verify_reader_parent_algebra()
    if args.four_tail_scaling_only:
        verify_four_tail_scaling()
    elif args.tail_eight_second_two:
        two_digit_eight_certificate(args.reader, args.show_bounds, not args.no_length_prune)
    else:
        assert not args.no_length_prune, "--no-length-prune belongs to the two-digit/eight mode"
        certificate(args.reader, args.show_bounds)
