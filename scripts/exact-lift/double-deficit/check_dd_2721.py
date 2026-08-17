#!/usr/bin/env python3
"""Check the exact constant inequalities in DD Section 27.21.

The Markdown proof excludes n3 = 8S for every S >= 4 by a symbolic split on
whether 5 divides b3 and on the three five-adic near-square states.  This
helper checks the integer-power comparisons and the three final 2-adic
residues in the 5-adic-unit tail case.  It is not a proof of the valuation
transfers and does not enumerate original DD candidates.
"""

from __future__ import annotations


EXPECTED_RESIDUES = {
    4: (177583, 8991),
    5: (16954995, 89991),
    6: (3528660519, 899991),
}


def main() -> None:
    # Gap lock for 5 | b3: 5^(2S-2) > 10^S from S=4 onward.
    assert 5 ** (2 * 4 - 2) > 10**4
    assert 5**2 > 10

    # If 5 does not divide b3, k5 <= 3S because the next power is too large.
    assert 5 ** (3 * 4 + 1) > 10 ** (2 * 4 + 1)
    assert 5**3 > 10**2

    # The tail multiplier is below 4 for S >= 4; below 2 for S >= 7.
    assert 4 * 5 ** (3 * 4) > 9 * 10 ** (2 * 4)
    assert 2 * 5 ** (3 * 7) > 9 * 10 ** (2 * 7)

    # The b3-dominant t2=1 position must be 2-adically resonant.
    assert 2 ** (8 * 4) > 11 * 10 ** (2 * 4)
    assert 2**8 > 10**2

    # The k5=g5 resonance product cannot fit its two factor heights.
    assert 5 ** (6 * 4) > 11 * 10 ** (3 * 4)
    assert 5**6 > 10**3

    residues = {
        S: (
            (-5 ** (3 * S)) % 2 ** (6 * S - 4),
            9 * (10 ** (S - 1) - 1),
        )
        for S in range(4, 7)
    }
    assert residues == EXPECTED_RESIDUES
    assert all(residue > G_max for residue, G_max in residues.values())

    print(f"unit-tail residues and G caps = {residues}")
    print("5-divisible state height comparisons: OK")
    print("DD 27.21 boundary reductions: OK")


if __name__ == "__main__":
    main()
