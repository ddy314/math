#!/usr/bin/env python3
"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0619; see history/sources.json.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


def valuation_two(value: int) -> int:
    assert value != 0
    return (abs(value) & -abs(value)).bit_length() - 1


def single_digit_tail_modular_certificate() -> None:
    # b3=1: 10 is 1 modulo 9, so Delta_dec is always 3 modulo 9.
    assert (1 + 1 + 1 - 111**2) % 9 == 3
    # b3=3,6,9: the unique third three-adic depth is absent from the word.
    assert all((110 + b3) % 3 != 0 for b3 in (3, 6, 9))
    # b3=7: same unique-third argument at the inert prime 7.
    assert 117 % 7 != 0 and 7 % 4 == 3
    # Reduced even b3 makes a3 and the entire numerator word odd.  The
    # sphere and word then demand incompatible denominator two-depths.
    even_depths = {b3: (valuation_two(b3), valuation_two(110 + b3)) for b3 in (2, 4, 8)}
    assert all(sphere_depth != word_depth for sphere_depth, word_depth in even_depths.values())
    # b3=5: q_lcm=5, word=23*H, and word=a3 (mod 5).  Sphere demands
    # H^2=a3^2; word instead gives H=2*a3 and H^2=4*a3^2.
    inverse_23 = pow(23, -1, 5)
    assert inverse_23 == 2
    five_unit_residues = [a3 for a3 in range(1, 5) if ((inverse_23 * a3)**2 - a3**2) % 5 == 0]
    assert five_unit_residues == []
    covered = {1, 3, 6, 9, 7, 2, 4, 8, 5}
    assert covered == set(range(1, 10))
    print(f"All nine third denominators covered; even two-depths {even_depths}")
    print("Original-word b3=5 unit audit: 4 nonzero residue classes, 0 compatible sphere residues")
    print("Certificate uses no numerator-length cutoff or bounded integer search")


def exact_bound_audit() -> None:
    # The even third block is reduced, so its numerator and entire word are
    # odd.  Sphere and word therefore require the same denominator two-depth.
    even_depths = {b3: (valuation_two(b3), valuation_two(110 + b3)) for b3 in (2, 4, 6, 8)}
    assert all(tail_depth != word_depth for tail_depth, word_depth in even_depths.values())
    assert all((110 + b3) % 3 != 0 for b3 in (3, 6, 9))
    assert all((-2 * (1 + 2 * b3)) % 9 in (3, 6) for b3 in (1, 7))

    # The finite grid audits unbounded formulas already proved by comparing
    # two-depths; it is not their coverage argument.
    for n3 in range(1, 11):
        for n2 in range(1, 11):
            defect = 10 ** (2 * n3) * (10 ** (2 * n2) + 1) - 13200
            if n3 >= 3:
                assert valuation_two(defect) == 4 and (defect // 16) % 4 == 3
            elif n3 == 2:
                depth = valuation_two(defect)
                assert (defect // 2**depth) % 4 == (1 if n2 == 2 else 3)
            elif n2 == 1:
                assert defect == -3100

    # Exact geometric endpoints: increasing a1 strengthens both comparisons;
    # the second margin increases linearly with 10^(2*n2) for n2 >= 2.
    dd_margin = 4 * (Fraction(10000, 115) ** 2 - 1) - 99**2 - Fraction(99, 5) ** 2
    one_digit_margin = 144 * (Fraction(1000, 115) ** 2 - 1) - 10000 - Fraction(81, 25)
    assert dd_margin == Fraction(265144146, 13225) > 0
    assert one_digit_margin == Fraction(9802751, 13225) > 0
    assert Fraction(14400, 13225) - 1 > 0
    assert 25 * 11**2 + 9**2 == 3106
    assert Fraction(3106, 10) < 311
    assert 9885 - 15 * 99 - 22 * 99 == 6222 > 0
    print(f"Exact geometry endpoints: DD {dd_margin}; n3=1 {one_digit_margin}")


def residual(a1: int, a2: int, a3: int) -> int:
    n2, n3 = len(str(a2)), len(str(a3))
    word = a1 * 10 ** (n2 + n3) + a2 * 10**n3 + a3
    # q_lcm = 5, beta = 115, hence word = 23*H and
    # H^2 = 25*a1^2 + 25*a2^2 + a3^2.
    return word**2 - 529 * (25 * a1**2 + 25 * a2**2 + a3**2)


def bounded_dd_certificate() -> None:
    checked, hits, smallest_triangle_margin = 0, [], None
    for a2 in range(10, 100):
        for a3 in range(10, 100):
            if gcd(a3, 5) != 1:
                continue
            checked += 1
            if residual(1, a2, a3) == 0:
                hits.append((1, a2, a3))
            margin = 9885 - 15 * a2 - 22 * a3
            smallest_triangle_margin = margin if smallest_triangle_margin is None else min(smallest_triangle_margin, margin)
            assert margin > 0
    assert checked == 6480 and not hits and smallest_triangle_margin == 6222
    print(f"Redundant DD residual audit: {checked} triples, 0 hits; positive-sum margin >= {smallest_triangle_margin}")


def bounded_one_digit_numerator_certificate() -> None:
    checked, hits = 0, []
    for a1 in range(1, 12):
        for a2 in range(10, 311):
            for a3 in range(1, 10):
                if gcd(a3, 5) != 1:
                    continue
                checked += 1
                if residual(a1, a2, a3) == 0:
                    hits.append((a1, a2, a3))
    assert checked == 26488 and not hits
    print(f"Redundant n3=1 residual audit: {checked} triples, 0 hits (cross-branch slice)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--redundant-arithmetic-audit", action="store_true", help="also run earlier geometric and bounded residual checks; not proof dependencies")
    args = parser.parse_args()
    single_digit_tail_modular_certificate()
    if args.redundant_arithmetic_audit:
        exact_bound_audit()
        bounded_dd_certificate()
        bounded_one_digit_numerator_certificate()
    print("Unit-prefix / single-digit-tail modular certificate passed; arbitrary prefix denominators remain open")


if __name__ == "__main__":
    main()
