#!/usr/bin/env python3
"""Exact symbolic checks for the A2 source-Hensel resultant collapse.

This script is a verifier for the algebra recorded in
`docs/proofs/exact-lift/branches/a2-only/hensel.md`.
It does not enumerate the unbounded A2 parameter space.
"""

import sympy as sp


def main() -> None:
    x, y, z, a = sp.symbols("x y z a")

    phi = (99 * x - 4) * z - 2 * x - 4
    psi = 400 * a * (z + 1) ** 2 - y * (99 * z - 2) ** 2

    expected = 163216 * (25 * a * x**2 - y)
    resultant = sp.factor(sp.resultant(phi, psi, z))
    assert sp.expand(resultant - expected) == 0

    A = 99 * x - 4
    quotient = (
        39600 * a * x * z
        + 80000 * a * x
        - 1600 * a * z
        - 1600 * a
        - 970299 * x * y * z
        + 19602 * x * y
        + 39204 * y * z
        - 40788 * y
    )
    bezout = sp.expand(A**2 * psi - expected - phi * quotient)
    assert bezout == 0

    # The only possible common odd prime divisor of A=99x-4 and B=2x+4
    # divides 99B-2A=404=4*101.  In particular no p == 3 (mod 4)
    # can divide both.
    B = 2 * x + 4
    assert sp.expand(99 * B - 2 * A) == 404
    assert sp.factorint(163216) == {2: 4, 101: 2}
    assert sp.factorint(404) == {2: 2, 101: 1}

    print("A2 §15.1 symbolic identities: OK")
    print(f"resultant = {resultant}")
    print("Bezout identity: OK")
    print("exceptional constants involve only 2 and 101")


if __name__ == "__main__":
    main()
