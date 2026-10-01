#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0613; see history/sources.json.
"""

from argparse import ArgumentParser
from fractions import Fraction
from math import gcd, isqrt, lcm
from time import monotonic

import sympy as sp


def verify_reader_parent_algebra() -> None:
    """Derive both readers directly from q*Aword=D*H and the integer sphere."""
    q, d, cx, weight, known, other, x, h = sp.symbols("q d cx weight K S x H")
    word = weight*x+known
    square_sum = cx*cx*x*x+other
    residual = q*q*word*word-d*d*square_sum
    word_parent = q*word-d*h
    sphere_parent = h*h-square_sum
    assert sp.expand(residual-word_parent*(q*word+d*h)-d*d*sphere_parent) == 0
    aa = q*q*weight*weight-d*d*cx*cx
    bb = 2*q*q*weight*known
    cc = q*q*known*known-d*d*other
    assert sp.expand(residual-aa*x*x-bb*x-cc) == 0
    w = q*q*cx*cx*known*known+aa*other
    assert sp.expand(bb*bb-4*aa*cc-4*d*d*w) == 0
    print("Both quadratic readers derived symbolically from original q*Aword=D*H and sphere")


def verify_bounds() -> None:
    """Exact endpoint arithmetic; the inequalities are proved in the text."""
    assert Fraction(998) + Fraction(999, 1000) < 1000
    assert Fraction(998000, 9001) < 111
    assert Fraction(198801, 9001) < 23
    assert Fraction(6561 * (110**2 + 99**2), 2) < 10**8
    assert Fraction(6561 * (22**2 + 99**2), 2) < 10**8


def standard_roots(q: int, d: int, cx: int, weight: int, known: int,
                   other_squares: int) -> set[int]:
    """Integer positive roots of the original quadratic, including both signs."""
    aa = q*q*weight*weight - d*d*cx*cx
    bb = 2*q*q*weight*known
    cc = q*q*known*known - d*d*other_squares
    assert aa != 0
    disc = bb*bb - 4*aa*cc
    if disc < 0:
        return set()
    z = isqrt(disc)
    if z*z != disc:
        return set()
    return {num // (2*aa) for num in (-bb-z, -bb+z)
            if num % (2*aa) == 0 and num // (2*aa) > 0}


SQUARES = {m: {i*i % m for i in range(m)} for m in (64, 63, 65)}


def factored_roots(q: int, d: int, cx: int, weight: int, known: int,
                   other_squares: int) -> set[int]:
    """Independent reader from disc = 4*d^2*W, using a smaller radicand."""
    aa = q*q*weight*weight - d*d*cx*cx
    assert aa != 0
    w = q*q*cx*cx*known*known + aa*other_squares
    if w < 0 or any(w % m not in residues for m, residues in SQUARES.items()):
        return set()
    z = isqrt(w)
    if z*z != w:
        return set()
    middle = q*q*weight*known
    return {num // aa for num in (-middle-d*z, -middle+d*z)
            if num % aa == 0 and num // aa > 0}


def two_depth(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def denominator_possible(b1: int, b2: int, b3: int, d: int) -> bool:
    depths = [two_depth(b) for b in (b1, b2, b3)]
    e = max(depths)
    # core section 27.7: a positive maximum is unique. An odd tail
    # gives an odd word denominator/numerator and rules out an even prefix.
    return e == 0 or (depths.count(e) == 1 and b3 % 2 == 0 and two_depth(d) == e)


def norm_possible(delta: int) -> bool:
    # Optional only: global-framework section 10.2 Gaussian norm criterion.
    if delta < 0:
        return False
    if delta == 0:
        return True
    if (delta >> two_depth(delta)) % 4 != 1:
        return False
    for p in (3, 7, 11, 19, 23, 31, 43):
        e, reduced = 0, delta
        while reduced % p == 0:
            reduced //= p
            e += 1
        if e % 2:
            return False
    return True


def audit(*, reader_name: str, prune: bool) -> None:
    reader = standard_roots if reader_name == "standard" else factored_roots
    counts = [0, 0, 0]
    denominator_states = 0
    length_states = 0
    start = monotonic()

    def accept(b1: int, b2: int, b3: int, a1: int, a2: int, a3: int,
               n2: int, n3: int, q: int, d: int) -> None:
        assert a1 > 0 and 10**(n2-1) <= a2 < 10**n2
        assert 10**(n3-1) <= a3 < 10**n3
        assert all(gcd(a, b) == 1 for a, b in zip((a1, a2, a3), (b1, b2, b3)))
        word = a1*10**(n2+n3) + a2*10**n3 + a3
        ghosts = (q*a1//b1, q*a2//b2, q*a3//b3)
        assert q*q*word*word == d*d*sum(y*y for y in ghosts)
        raise AssertionError(f"Exact solution found: {(b1, b2, b3, a1, a2, a3)}")

    for b1 in range(1, 10):
        for b2 in range(1, 10):
            for b3 in range(1, 10):
                q = lcm(b1, b2, b3)
                c1, c2, c3 = q//b1, q//b2, q//b3
                d = 100*b1 + 10*b2 + b3
                if prune and not denominator_possible(b1, b2, b3, d):
                    continue
                denominator_states += 1

                def length_allowed(n2: int, n3: int) -> bool:
                    nonlocal length_states
                    x, y = 10**n2, 10**n3
                    delta = b1*b1*x*x*y*y + b2*b2*y*y + b3*b3 - d*d
                    if prune and not norm_possible(delta):
                        return False
                    length_states += 1
                    return True

                # n3 >= 3: a1 <= 110, n2 <= 2, n3 <= 8. Recover a3.
                for n3 in range(3, 9):
                    y = 10**n3
                    for n2 in (1, 2):
                        x = 10**n2
                        if not length_allowed(n2, n3):
                            continue
                        for a1 in range(1, 111):
                            if gcd(a1, b1) != 1:
                                continue
                            for a2 in range(x//10, x):
                                if gcd(a2, b2) != 1:
                                    continue
                                counts[0] += 1
                                known = (a1*x+a2)*y
                                other = c1*c1*a1*a1 + c2*c2*a2*a2
                                for a3 in reader(q, d, c3, 1, known, other):
                                    if y//10 <= a3 < y and gcd(a3, b3) == 1:
                                        accept(b1, b2, b3, a1, a2, a3, n2, n3, q, d)

                # n3 = 2, n2 >= 2: a1 <= 22, n2 <= 8. Recover a2.
                n3, y = 2, 100
                for n2 in range(2, 9):
                    x = 10**n2
                    if not length_allowed(n2, n3):
                        continue
                    for a1 in range(1, 23):
                        if gcd(a1, b1) != 1:
                            continue
                        for a3 in range(10, 100):
                            if gcd(a3, b3) != 1:
                                continue
                            counts[1] += 1
                            known = a1*x*y+a3
                            other = c1*c1*a1*a1 + c3*c3*a3*a3
                            for a2 in reader(q, d, c2, y, known, other):
                                if x//10 <= a2 < x and gcd(a2, b2) == 1:
                                    accept(b1, b2, b3, a1, a2, a3, n2, n3, q, d)

                # n3 = 2, n2 = 1: recover every positive a1, with no cutoff.
                n2, x = 1, 10
                if length_allowed(n2, n3):
                    for a2 in range(1, 10):
                        if gcd(a2, b2) != 1:
                            continue
                        for a3 in range(10, 100):
                            if gcd(a3, b3) != 1:
                                continue
                            counts[2] += 1
                            known = a2*y+a3
                            other = c2*c2*a2*a2 + c3*c3*a3*a3
                            for a1 in reader(q, d, c1, x*y, known, other):
                                if gcd(a1, b1) == 1:
                                    accept(b1, b2, b3, a1, a2, a3, n2, n3, q, d)

    if not prune:
        assert counts == [20_104_038, 4_258_548, 259_380]
        assert denominator_states == 729 and length_states == 14_580
    else:
        assert sum(counts) == 1_916_425
        assert denominator_states == 153 and length_states == 878
    print(f"reader={reader_name}, prune={prune}: {denominator_states} denominator states, "
          f"{length_states} length states")
    print(f"quadratic rows={counts}, total={sum(counts)}, exact hits=0; "
          f"seconds={monotonic()-start:.3f}")
    print("All single-digit-denominator DD states closed after proved global bounds; general DD remains open")


def third_two_dominant_tail_certificate(reader_name: str) -> None:
    """Exact extra box after the unbounded denominator reduction in 27.7.4."""
    # E>=2: exactly one nonmaximum denominator at E-1 gives ghost
    # squares 1+4+0=5 mod8. Positive denominator depth makes its numerator odd.
    patterns = 0
    for e1 in range(5):
        for e2 in range(5):
            for e3 in range(5):
                depths = (e1, e2, e3)
                e = max(depths)
                if e < 2 or depths.count(e) != 1 or depths.count(e-1) != 1:
                    continue
                ghosts = [2**(e-ei) for ei in depths]
                assert sum(y*y for y in ghosts) % 8 == 5
                patterns += 1

    # Audits only: the actual unbounded denominator reduction is in the text.
    for b1 in range(1, 200):
        for b2 in range(1, 1000):
            e1, e2 = two_depth(b1), two_depth(b2)
            m2 = len(str(b2))
            Q = b1*10**m2+b2
            for b3 in (2, 4, 6, 8):
                e3 = two_depth(b3)
                if e3 <= max(e1, e2) or two_depth(10*Q+b3) != e3:
                    continue
                if e3 >= 2 and (e1, e2).count(e3-1) == 1:
                    continue
                assert b3 == 8 and b1 % 2 and b2 in (2, 6) and Q % 8 == 0
    assert [b for b in range(1, 29, 2) if 28 % b == 0] == [1, 7]
    assert [b for b in range(1, 69, 2) if 68 % b == 0] == [1, 17]

    # Remaining (17,6,8): q=408, D=1768=8*221, Q=176.
    # n3>=3 gives H=5*y3 mod8, while sphere H^2=y3^2 mod16.
    assert pow(221, -1, 8) == 5
    assert all(((5*y)**2-y*y) % 16 == 8 for y in range(1, 16, 2))
    cap_a1 = (Fraction(10, 6)+Fraction(99, 8))/(Fraction(1000, 1768)-Fraction(1, 17))
    cap_a2 = 1224*(Fraction(27, 17)**2+Fraction(99, 8)**2)
    assert cap_a1 == Fraction(74477, 2688) < 28
    assert cap_a2 == Fraction(25912305, 136) < 10**6

    reader = standard_roots if reader_name == "standard" else factored_roots
    count = 0
    for n2 in range(1, 7):
        x = 10**n2
        for a1 in range(1, 28):
            if gcd(a1, 17) != 1:
                continue
            for a3 in range(10, 100):
                if gcd(a3, 8) != 1:
                    continue
                count += 1
                known = 100*x*a1+a3
                other = 24**2*a1*a1+51**2*a3*a3
                for a2 in reader(408, 1768, 68, 100, known, other):
                    if x//10 <= a2 < x and gcd(a2, 6) == 1:
                        word = 100*x*a1+100*a2+a3
                        assert 408**2*word**2 == 1768**2*(other+68**2*a2*a2)
                        raise AssertionError(f"Exact (17,6,8) solution: {(a1, a2, a3)}")
    assert count == 7020
    print(f"Third-two-dominant tail: {patterns} forbidden mod8 depth patterns audited; "
          f"(17,6,8), n3=2: {count} quadratic rows, exact hits=0, reader={reader_name}")
    print("All one-digit even tails with third two-dominance closed in DD; prefix two-dominance remains open")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--reader", choices=("standard", "factored"), default="standard")
    parser.add_argument("--prune", action="store_true", help="use optional proved local necessary conditions")
    parser.add_argument("--third-two-dominant-only", action="store_true",
                        help="audit only the section 27.7.4 extension (uses the already saved 27.7.3 certificate)")
    args = parser.parse_args()
    verify_reader_parent_algebra()
    verify_bounds()
    if not args.third_two_dominant_only:
        audit(reader_name=args.reader, prune=args.prune)
    third_two_dominant_tail_certificate(args.reader)
