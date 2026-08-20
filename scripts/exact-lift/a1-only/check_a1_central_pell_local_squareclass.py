#!/usr/bin/env python3
"""Audit central Pell degeneracy and 2/5-adic squareclass formulas.

This script is a constants/algebra audit for
`central-pell-local-squareclass.md`; it does not enumerate the huge U windows.
"""

from __future__ import annotations

from fractions import Fraction as F


CENTRAL = {
    (1, 1): (32, 34, 36, 38),
    (1, 3): (24, 26, 28, 30, 32, 34, 36, 38),
    (3, 1): (22, 24, 26, 28, 30, 32, 34, 36, 38),
    (1, 2): (30, 32, 38),
    (3, 2): (22, 30, 32, 38),
    (1, 4): (24, 26),
}


def vp(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def c_gamma(gamma: int) -> int:
    return 2 ** vp(gamma, 2) * 5 ** vp(gamma, 5)


def legendre5(a: int) -> int:
    a %= 5
    assert a != 0
    return 1 if a in (1, 4) else -1


def main() -> None:
    total = 0
    worst_abs_b = 0

    for (z, w), gaps in CENTRAL.items():
        C0 = w * (10 * w - 1)
        for gamma in gaps:
            total += 1
            c = c_gamma(gamma)
            r = gamma // c

            U0 = 10 * c * gamma * (20 * w - 1)
            V0 = 10 * c * gamma
            D = 4000 * C0 * c**4 * r**2
            assert U0 * U0 - V0 * V0 == D

            lower = c * (C0 + 1000 * gamma * gamma)
            upper = F(c) * (F(C0, 10) + 10000 * gamma * gamma) + 1
            assert lower > U0

            # B_U is affine and strictly decreasing for U>U0, so its largest
            # absolute value on the safe window occurs at the upper endpoint.
            # Use the integer just below the strict upper bound.
            hi = (upper.numerator - 1) // upper.denominator
            B_hi = -4 * C0 * r * (hi - U0)
            assert B_hi < 0
            worst_abs_b = max(worst_abs_b, -B_hi)

            # Minimal k=26 local exponents.
            e2 = 26 - vp(c, 2)
            e5 = 26 - vp(c, 5)
            assert e2 >= 21 and e5 >= 25

            # The whole B range lies far below the p-adic lifting depths, so
            # congruence-square implies genuine Q_p squareclass constraints.
            assert -B_hi < 2 ** (2 * e2)
            assert -B_hi < 5 ** (2 * e5)

            # Audit the squareclass CRT statement for all parity-compatible
            # valuation pairs in a representative bounded range.  For each
            # (a,b), exactly two reduced m classes mod 40 survive.
            alpha = vp(C0 * r, 2)
            beta = vp(C0 * r, 5)
            for a in range(0, 10):
                for b in range(0, 8):
                    if (a - alpha) % 2 or (b - beta) % 2:
                        continue

                    odd_cr_2 = (C0 * r) // (2**alpha)
                    target8 = pow((-odd_cr_2 * pow(5, b, 8)) % 8, -1, 8)
                    unit5 = -((C0 * r) // (5**beta)) * pow(2, a, 5)
                    target_leg = legendre5(unit5)

                    residues = []
                    for m in range(40):
                        if m % 2 == 0 or m % 5 == 0:
                            continue
                        if m % 8 != target8:
                            continue
                        if legendre5(m) != target_leg:
                            continue
                        residues.append(m)
                    assert len(residues) == 2

            print(
                f"type={(z,w)} gamma={gamma} c={c} r={r} "
                f"U0={U0} |B|max<{(-B_hi)+1}"
            )

    assert total == 30
    assert worst_abs_b < 400_000_000_000
    print(f"central combinations={total}")
    print(f"worst |B_U|={worst_abs_b}")
    print("A1 central Pell local-squareclass audit OK")


if __name__ == "__main__":
    main()
