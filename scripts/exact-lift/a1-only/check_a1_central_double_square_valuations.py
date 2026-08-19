#!/usr/bin/env python3
"""Exact local audit for central-double-square-valuation-lock.md.

The script checks the contact-square residue tables modulo 2^12 and 5^6 and
translates them, using
    v2(N0)=(v2(t)-v2(C0))/2,
    v5(N0)=v5(t)/2,
into the claimed finite valuation sets.
"""

from __future__ import annotations


CENTRAL = {
    (1, 1): (32, 34, 36, 38),
    (1, 3): (24, 26, 28, 30, 32, 34, 36, 38),
    (3, 1): (22, 24, 26, 28, 30, 32, 34, 36, 38),
    (1, 2): (30, 32, 38),
    (3, 2): (22, 30, 32, 38),
    (1, 4): (24, 26),
}

EXPECTED_2 = {
    (1, 2, 30): (3, 7, 9),
    (1, 2, 38): (3, 7),
    (3, 2, 22): (3, 7),
    (3, 2, 30): (3, 5),
    (3, 2, 38): (3, 5),
    (1, 4, 24): (4, 6),
}

EXPECTED_5 = {
    (1, 1, 34): (0,),
    (1, 1, 36): (0, 2),
    (1, 1, 38): (0,),
    (3, 2, 38): (0,),
    (1, 4, 24): (0,),
    (1, 4, 26): (0, 2),
}


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("vp(0,p) handled separately")
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def contact_R(z: int, w: int, gamma: int, N0: int, modulus: int) -> int:
    return (
        (z * w) ** 2
        + 2
        * gamma
        * (1 - 10 * w)
        * ((N0 - 1) ** 2 + (z * w) ** 2)
    ) % modulus


def allowed_vp(z: int, w: int, gamma: int, p: int, depth: int) -> tuple[set[int], bool]:
    modulus = p**depth
    squares = {x * x % modulus for x in range(modulus)}
    vals: set[int] = set()
    zero_class_allowed = contact_R(z, w, gamma, 0, modulus) in squares

    for N0 in range(1, modulus):
        if contact_R(z, w, gamma, N0, modulus) in squares:
            vals.add(vp(N0, p))

    return vals, zero_class_allowed


def audit_2() -> None:
    depth = 12
    for (z, w, gamma), expected_t in EXPECTED_2.items():
        vals, zero_ok = allowed_vp(z, w, gamma, 2, depth)
        assert not zero_ok, (z, w, gamma, "unexpected deep 2-adic zero class")

        vC0 = vp(w * (10 * w - 1), 2)
        # even-w prefixes force N0 even.
        vals = {v for v in vals if v >= 1}
        t_vals = tuple(sorted(2 * v + vC0 for v in vals))
        assert t_vals == expected_t, ((z, w, gamma), t_vals, expected_t)
        print(f"2-adic {(z,w,gamma)}: v2(t)={t_vals}")

    # The three deliberately unbounded local families retain the zero class.
    for z, w, gamma in ((1, 2, 32), (3, 2, 32), (1, 4, 26)):
        _, zero_ok = allowed_vp(z, w, gamma, 2, depth)
        assert zero_ok


def audit_5() -> None:
    depth = 6
    for (z, w, gamma), expected_t in EXPECTED_5.items():
        vals, zero_ok = allowed_vp(z, w, gamma, 5, depth)
        assert not zero_ok, (z, w, gamma, "unexpected deep 5-adic zero class")
        t_vals = tuple(sorted(2 * v for v in vals))
        assert t_vals == expected_t, ((z, w, gamma), t_vals, expected_t)
        print(f"5-adic {(z,w,gamma)}: v5(t)={t_vals}")


def main() -> None:
    audit_2()
    audit_5()
    print("A1 central double-square valuation audit OK")


if __name__ == "__main__":
    main()
