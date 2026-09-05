#!/usr/bin/env python3
"""Finite period audit for the w=1 joint top-endpoint lemma.

This script only checks the short modular arithmetic used in the proof:

* v_3(2k+1)=1  <=>  k mod 9 is 1 or 7;
* 23 | (10^(2k+2)-9)  <=>  k mod 11 is 8;
* combining them gives k mod 99 in {19, 52};
* on v_3(2k+1)=1, the smaller Q-side 3 mod 4 candidates
  3, 7, 11, 19 are unavailable.

It is a research check, not a replacement for the unbounded proof.
"""

from __future__ import annotations


def vp(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def q_mod(k: int, m: int) -> int:
    return (pow(10, 2 * k + 2, m) - 9) % m


def main() -> None:
    r3_classes = {k for k in range(9) if vp(2 * k + 1, 3) == 1}
    assert r3_classes == {1, 7}, r3_classes

    q23_classes = {k for k in range(11) if q_mod(k, 23) == 0}
    assert q23_classes == {8}, q23_classes

    joint = {
        k
        for k in range(99)
        if vp(2 * k + 1, 3) == 1 and q_mod(k, 23) == 0
    }
    assert joint == {19, 52}, joint

    for k in range(99):
        if vp(2 * k + 1, 3) != 1:
            continue
        assert q_mod(k, 3) != 0
        assert q_mod(k, 7) != 0
        assert q_mod(k, 11) != 0
        assert q_mod(k, 19) != 0

    # Direct period facts quoted in the proof.
    assert pow(10, 18, 23) == 9
    assert pow(10, 22, 23) == 1

    print("w=1 joint endpoint period audit: OK")
    print("v3(2k+1)=1 classes mod 9:", sorted(r3_classes))
    print("23 | Q classes mod 11:", sorted(q23_classes))
    print("joint classes mod 99:", sorted(joint))


if __name__ == "__main__":
    main()
