#!/usr/bin/env python3
"""Exact residue-cycle audit for the coefficient-sensitive 2-high source notes.

This script checks only finite modular facts:

* the first 3 mod 4 prime sources that can divide Q_w(k);
* the first 3 mod 4 prime sources that can divide b_1(k) for w=2;
* the coefficient-sensitive lower-bound examples;
* the joint w=2 source matching bounds using gcd(b_1,Q)=1.

It is an arithmetic audit, not a search over k and not a proof that A1 is closed.
"""

from __future__ import annotations


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def multiplicative_order_10(p: int) -> int:
    assert is_prime(p) and p not in (2, 5)
    x = 1
    for n in range(1, p):
        x = (10 * x) % p
        if x == 1:
            return n
    raise AssertionError("order not found")


def source_possible(w: int, side: str, p: int) -> bool:
    """Whether p divides the indicated decimal source for some k>=0.

    The condition is periodic in k modulo ord_p(10), so one complete residue
    cycle is exact.
    """

    order = multiplicative_order_10(p)
    for k in range(order):
        if side == "Q":
            value = pow(10, 2 * k + 2, p) - (10 * w - 1)
        elif side == "b":
            value = pow(10, 2 * k + 1, p) - w
        else:
            raise ValueError(side)
        if value % p == 0:
            return True
    return False


def source_primes(w: int, side: str, bound: int = 1000) -> list[int]:
    out: list[int] = []
    for p in range(3, bound + 1):
        if p % 4 != 3 or not is_prime(p) or p == 5:
            continue
        if source_possible(w, side, p):
            out.append(p)
    return out


def first_not_dividing(primes: list[int], coefficient: int) -> int:
    for p in primes:
        if coefficient % p != 0:
            return p
    raise AssertionError("increase audit prime bound")


def joint_w2_min(
    b_sources: list[int], q_sources: list[int], alpha: int, beta: int
) -> tuple[int, tuple[int, int]]:
    """Return J_2(alpha,beta) and the minimizing distinct source pair."""

    best: int | None = None
    pair: tuple[int, int] | None = None
    for p in b_sources:
        if alpha % p == 0:
            continue
        for q in q_sources:
            if beta % q == 0 or p == q:
                continue
            value = 2 * p * q
            if best is None or value < best:
                best = value
                pair = (p, q)
    if best is None or pair is None:
        raise AssertionError("increase audit prime bound")
    return best, pair


def main() -> None:
    expected_q = {
        1: [7, 19, 23, 31, 43, 47, 59, 67, 71, 83, 103, 107],
        2: [3, 31, 59, 67, 71, 107, 127, 151, 167, 179, 211, 223],
        3: [7, 23, 59, 67, 71, 83, 107, 151, 167, 179, 199, 223],
        4: [7, 19, 23, 31, 67, 107, 131, 151, 163, 179, 191, 223],
    }
    expected_b2 = [19, 31, 59, 71, 131, 151, 179, 191, 199, 251, 311, 359]

    q_sources: dict[int, list[int]] = {}
    for w in range(1, 5):
        q_sources[w] = source_primes(w, "Q")
        assert q_sources[w][: len(expected_q[w])] == expected_q[w]

    b2_sources = source_primes(2, "b")
    assert b2_sources[: len(expected_b2)] == expected_b2

    # Q-side coefficient-sensitive minima.
    assert first_not_dividing(q_sources[2], 3) == 31
    assert first_not_dividing(q_sources[3], 7) == 23
    assert first_not_dividing(q_sources[4], 7) == 19
    assert first_not_dividing(q_sources[4], 7 * 19) == 23
    assert first_not_dividing(q_sources[1], 7 * 19 * 23) == 31

    # w=2 b_1-side coefficient-sensitive minima.
    assert first_not_dividing(b2_sources, 1) == 19
    assert first_not_dividing(b2_sources, 19) == 31
    assert first_not_dividing(b2_sources, 19 * 31) == 59

    # Independent product bounds and safe integer denominator caps.
    examples = [
        # name, M_min, safe integer C with 10001/M_min < C
        ("w2_beta3", 2 * 19 * 31, 9),
        ("w2_alpha19", 2 * 31 * 3, 54),
        ("w3_beta7", 23, 435),
        ("w4_beta7", 12 * 19, 44),
        ("w4_beta7_19", 12 * 23, 37),
        ("w1_beta7_19_23", 27 * 31, 12),
    ]
    for name, m_min, cap in examples:
        assert 10001 < cap * m_min, name

    # Joint w=2 source matching: p|b1 and q|Q must satisfy p != q.
    joint_examples = [
        # alpha, beta, expected J_2, expected minimizing pair, safe cap
        (1, 1, 114, (19, 3), 88),
        (19, 1, 186, (31, 3), 54),
        (1, 3, 1178, (19, 31), 9),
        (19, 3, 3658, (31, 59), 3),
        (19 * 31, 3, 3658, (59, 31), 3),
        (19, 3 * 31, 3658, (31, 59), 3),
        (19 * 31, 3 * 31, 7906, (59, 67), 2),
    ]
    for alpha, beta, expected, pair, cap in joint_examples:
        got, got_pair = joint_w2_min(b2_sources, q_sources[2], alpha, beta)
        assert got == expected, (alpha, beta, got, expected)
        assert got_pair == pair, (alpha, beta, got_pair, pair)
        assert 10001 < cap * got, (alpha, beta, cap, got)

    print("Q source starts:")
    for w in range(1, 5):
        print(f"  w={w}: {q_sources[w][:12]}")
    print(f"w=2 b1 source start: {b2_sources[:12]}")
    print("Joint w=2 examples:")
    for alpha, beta, expected, pair, _ in joint_examples:
        print(f"  alpha={alpha} beta={beta}: J2={expected} via {pair}")
    print("CERTIFICATE OK: coefficient-sensitive and joint source minima audited.")


if __name__ == "__main__":
    main()
