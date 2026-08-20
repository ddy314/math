#!/usr/bin/env python3
"""Exact residue audit for deep-gap-unit-square.md."""

from __future__ import annotations


SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))


def main() -> None:
    # High decimal powers vanish mod 8/4/5 in the k>=26 regime.
    for z, w in SIX_TYPES:
        b1_8 = (-w) % 8
        a2_8 = (-z) % 8
        Q_8 = (1 - 10 * w) % 8

        if w in (2, 4):
            # gcd(a1,b1)=1 forces a1 odd.  Check all odd a1 classes.
            vals = set()
            for a1_8 in (1, 3, 5, 7):
                N_8 = (a1_8 * a1_8 + (a2_8 * b1_8) ** 2) % 8
                vals.add((N_8, (Q_8 * N_8) % 8))

            if w == 2:
                assert vals == {(5, 1)}
            else:
                assert vals == {(1, 1)}

        else:
            # For odd w: Q=3 mod4 and N_2=1 mod4 in both n2 cases.
            assert Q_8 % 4 == 3

            # n2=0: a1 even and N odd.
            for a1_8 in (0, 2, 4, 6):
                N_8 = (a1_8 * a1_8 + (a2_8 * b1_8) ** 2) % 8
                if N_8 % 2 == 1:
                    assert N_8 % 4 == 1

            # n2=1: a1 odd gives N=2 mod8, hence N/2=1 mod4.
            for a1_8 in (1, 3, 5, 7):
                N_8 = (a1_8 * a1_8 + (a2_8 * b1_8) ** 2) % 8
                assert N_8 == 2
                assert (N_8 // 2) % 4 == 1

        # Q is always 1 mod5 in the deep 5-adic unit formula.
        assert (1 - 10 * w) % 5 == 1

        print(f"type={(z,w)} Q8={Q_8} residue audit OK")

    # Legendre facts used in the 5-adic reduction.
    squares5 = {1, 4}
    assert (-1) % 5 in squares5
    assert 2 not in squares5

    print("A1 deep-gap unit-square audit OK")


if __name__ == "__main__":
    main()
