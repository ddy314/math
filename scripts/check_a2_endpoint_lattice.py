#!/usr/bin/env python3
"""Exact rational checks for the A2 endpoint-lattice continuation.

This script intentionally uses only Python's standard library. It verifies the
finite rational inequalities and Sturm sign checks used in
`a2-endpoint-lattice-progress-2026-08-17.md`. It does not enumerate A2
candidates and it is not a global A2 certificate.
"""

from fractions import Fraction as F


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def deriv(p):
    return trim([F(i) * p[i] for i in range(1, len(p))] or [F(0)])


def divmod_poly(a, b):
    a = trim(a)
    b = trim(b)
    if b == [0]:
        raise ZeroDivisionError
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b) and r != [0]:
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] += c
        for i in range(len(b)):
            r[i + k] -= c * b[i]
        r = trim(r)
    return trim(q), trim(r)


def sturm(p):
    seq = [trim(p), deriv(p)]
    while seq[-1] != [0]:
        _, r = divmod_poly(seq[-2], seq[-1])
        if r == [0]:
            break
        seq.append(trim([-x for x in r]))
    return seq


def eval_poly(p, x):
    acc = F(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc


def sign(v):
    return (v > 0) - (v < 0)


def variations(seq, x):
    signs = [sign(eval_poly(p, x)) for p in seq]
    signs = [s for s in signs if s]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def roots_in(p, lo, hi):
    seq = sturm(p)
    return variations(seq, lo) - variations(seq, hi)


def q0sq(a, x, y):
    A = F(a) + y
    B = F(2) + x
    S = F(a * a, 4) + y * y / (100 * x * x)
    D = A * A - B * B * S
    assert D > 0
    return A * A / D


def check_q0_windows():
    # For a=5 and a=7, q0(x,1) stays above the desired rational threshold.
    # Polynomial coefficients are constant-first.
    p5 = [64, 64, -9484, 40000, 10000]
    p7 = [438244, 438244, -100231939, 536848900, 134212225]
    assert roots_in(p5, F(27, 250), F(3, 16)) == 0
    assert eval_poly(p5, F(3, 20)) > 0
    assert roots_in(p7, F(1, 10), F(7, 40)) == 0
    assert eval_poly(p7, F(3, 25)) > 0

    assert q0sq(9, F(1, 10), F(1)) == F(8000, 503)
    assert q0sq(11, F(1, 10), F(1)) == F(256, 11)
    assert q0sq(13, F(1, 10), F(1)) == F(1600, 43)
    assert F(8000, 503) > F(997, 250) ** 2
    assert F(256, 11) > F(603, 125) ** 2
    assert F(1600, 43) > F(609, 100) ** 2

    # q0<4 in (a,k)=(9,2) forces x<2/19 and y>249/250.
    assert q0sq(9, F(2, 19), F(1)) == F(9025, 564) > 16
    assert q0sq(9, F(1, 10), F(249, 250)) == F(708050, 44237) > 16


def check_remainder_windows():
    # Upper bounds: J < sqrt(1+Smax)-1 and R/D = J-k.
    tests = [
        (5, F(27, 250), 1, F(17, 20)),
        (7, F(1, 10), 2, F(31, 40)),
        (9, F(1, 10), 3, F(18, 25)),
        (11, F(1, 10), 4, F(17, 25)),
        (13, F(1, 10), 5, F(33, 50)),
    ]
    for a, x_min, k, upper in tests:
        smax = F(a * a, 4) + 1 / (100 * x_min * x_min)
        assert 1 + smax < (F(k + 1) + upper) ** 2

    assert F(8000, 503) > F(997, 250) ** 2


def check_a9_endpoint():
    qsq = F(8000, 503)

    # zeta < 251/250.
    assert qsq > F(1001, 251) ** 2

    # w lower bound.
    w2_lower = F(7497, 503) / F(85, 4)
    assert w2_lower == F(1764, 2515)
    assert F(1764, 2515) > F(837, 1000) ** 2

    # w upper bound.
    num = F(3) * (F(3) + 2 * F(251, 250))
    smin = F(81, 4) + F(249, 250) ** 2 / (100 * F(2, 19) ** 2)
    assert num / smin < F(843, 1000) ** 2

    # v = y w/(10x) > 99/125.
    assert F(1764, 2515) > F(1320, 1577) ** 2

    v_lo, v_hi = F(99, 125), F(843, 1000)
    z_lo, z_hi = F(1), F(251, 250)
    delta_hi = F(3, 250)
    minus_lo = F(3) + z_lo - delta_hi - v_hi
    minus_hi = F(3) + z_hi - v_lo
    plus_lo = F(3) + z_lo - delta_hi + v_lo
    plus_hi = F(3) + z_hi + v_hi
    assert minus_lo > F(393, 125)
    assert minus_hi < F(1607, 500)
    assert plus_lo > F(2389, 500)
    assert plus_hi < F(606, 125)


def check_height_split():
    assert 5 ** 3 < 2 ** 7
    assert 20 ** 6 > 5 ** 11
    assert F(9, 14) > F(6, 11)
    assert F(6, 11) - F(3, 7) == F(9, 77)

    assert 4 * F(3, 7) - 3 * F(6, 11) == F(6, 77)
    assert 3 * F(3, 7) - 2 * F(6, 11) == F(15, 77)

    # m+d < 51M/77; for M>=11 this is < M-3.
    assert F(51, 77) * 11 < 11 - 3
    assert F(25, 2) / F(3, 250) > 1000


def slot_intersects(lo, hi, slo, shi):
    return lo < shi and slo < hi


def check_midline_high_rho_exclusion():
    low_slot = (F(786, 125), F(1607, 250))
    high_slot = (F(2389, 250), F(1212, 125))

    # d>=3 is impossible already from c_Q>=3 and w<843/1000.
    lower_d3 = F(3) * 25 * F(500, 843)
    assert lower_d3 > high_slot[1]

    # d=1, c_Q in {3,7,11}; each continuous interval misses every odd slot.
    for cq in (3, 7, 11):
        lo = F(500 * cq, 843)
        hi = F(10000 * cq, 15903)
        for kh in range(1, 51, 2):
            assert not slot_intersects(lo, hi, low_slot[0] / kh, low_slot[1] / kh)
            assert not slot_intersects(lo, hi, high_slot[0] / kh, high_slot[1] / kh)
        assert high_slot[1] / 51 < lo

    # d=2 forces c_Q=3.
    lo = F(7500, 843)
    hi = F(150000, 15903)
    for kh in range(1, 51, 2):
        assert not slot_intersects(lo, hi, low_slot[0] / kh, low_slot[1] / kh)
        assert not slot_intersects(lo, hi, high_slot[0] / kh, high_slot[1] / kh)
    assert high_slot[1] / 51 < lo

    # Boundary arithmetic in the proof of m>(M-2)/2.
    assert F(20, 4) == 5


def main():
    check_q0_windows()
    check_remainder_windows()
    check_a9_endpoint()
    check_height_split()
    check_midline_high_rho_exclusion()
    print("A2 endpoint-lattice exact checks: OK")


if __name__ == "__main__":
    main()
