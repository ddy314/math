#!/usr/bin/env python3
"""Finite residue audit for central-gap-2adic.md.

The proof is local modulo powers of two and is independent of factorization.
"""

SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))
GAPS = tuple(range(16, 40))

EXPECTED = {
    (1, 1): tuple(range(16, 40, 2)),
    (1, 2): (16, 22, 30, 32, 38),
    (1, 3): tuple(range(16, 40, 2)),
    (1, 4): (24, 26),
    (3, 1): tuple(range(16, 40, 2)),
    (3, 2): (16, 22, 30, 32, 38),
}


def square_residues(modulus: int) -> set[int]:
    return {x * x % modulus for x in range(modulus)}


def allowed_gaps(z: int, w: int, modulus: int) -> tuple[int, ...]:
    squares = square_residues(modulus)
    A = (z * w) ** 2
    Q = (1 - 10 * w) % modulus
    out: list[int] = []

    for gamma in GAPS:
        ok = False
        for N0 in range(modulus):
            if w % 2 == 0 and N0 % 2 != 0:
                continue
            N = ((N0 - 1) ** 2 + A) % modulus
            R = (A + 2 * gamma * Q * N) % modulus
            if R in squares:
                ok = True
                break
        if ok:
            out.append(gamma)

    return tuple(out)


def main() -> None:
    for typ in SIX_TYPES:
        z, w = typ
        modulus = 256 if w == 4 else 64
        got = allowed_gaps(z, w, modulus)
        expected = EXPECTED[typ]
        if got != expected:
            raise AssertionError(f"type={typ}: {got} != {expected}")
        print(f"type={typ} modulus={modulus} allowed={got}")

    total = sum(len(v) for v in EXPECTED.values())
    assert total == 48
    print("central type-gap combinations = 48")
    print("A1 central-gap 2-adic audit OK")


if __name__ == "__main__":
    main()
