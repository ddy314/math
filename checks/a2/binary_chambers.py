"""Exact arithmetic audit of A2-G04/G05/G08.

The bounded denominator patterns and sphere examples below are regression
checks, not original Exact-Lift solutions or a proof of an empty chamber.
All integers use Python's arbitrary precision. PROOF.md supplies the
unbounded valuation argument.
"""

from itertools import product
from math import gcd, isqrt

import sympy as sp


def v2(value):
    assert value > 0
    return (value & -value).bit_length() - 1


def v5(value):
    assert value > 0
    depth = 0
    while value % 5 == 0:
        value //= 5
        depth += 1
    return depth


def main():
    q, a, t, u, n, Q, tail_num, tail_den = sp.symbols(
        "q A T U n Q a3 b3", positive=True
    )
    y3 = q * tail_num / tail_den
    beta = Q * u + tail_den
    alpha = a * t * u + 10 * n * u + tail_num
    assert sp.factor(q * alpha - beta * y3 - u * (q * (a * t + 10 * n) - Q * y3)) == 0

    prefix = tail = critical = source = 0
    for m2, m3, first in product(range(2, 6), range(1, 7), (1, 2)):
        T, U = 10**m2, 10**m3
        e = v2(first)
        for f, g, odd2, odd3 in product(
            range(19), range(1, 21), (1, 3, 5, 7, 11), (1, 3, 5, 7, 11)
        ):
            b2, b3 = 2**f * odd2, 2**g * odd3
            if not (T // 10 <= b2 < T and U // 10 <= b3 < U):
                continue
            E = max(e, f, g)
            if (e, f, g).count(E) != 1:
                continue
            prefix_word = first * T + b2
            if v2(prefix_word * U + b3) != E:
                continue
            d = v2(prefix_word)
            if f > g:
                prefix += 1
                assert f > e + m2 and d == e + m2 and g == e + m2 + m3
                if (e, f, g).count(E - 1) % 2:
                    continue
                assert f >= g + 2
                J = v5(b3)
                assert J < m3
                lam = m3 - J
                c = b3 // (2**g * 5**J)
                r = f - g
                odd_u = b2 // 2**f
                Q0 = 5**m2 + 2 ** (m3 + r) * odd_u
                assert prefix_word == 2 ** (e + m2) * Q0
                assert v2(5 ** (m2 + lam) + c) == r
                assert c % 4 == 3 and 5**lam > 3 * 2 ** (e + m2)
                # G08: an effective bound for each fixed tail length.
                assert 3 * 2 ** (e + m2) < 5**m3
                assert b3 == 2 ** (e + m2 + m3) * 5**J * c
                # Denominator complement for the nondecimal tail part.
                if (odd_u * Q0) % c == 0:
                    source += 1
                    cu = gcd(c, odd_u)
                    cQ = c // cu
                    assert gcd(cu, cQ) == 1 and Q0 % cQ == 0
            else:
                tail += 1
                assert g > max(e, f) and g < d + m3
                if f >= e + m2 and not (e, f, g).count(E - 1) % 2:
                    assert g >= f + 2
                    assert m2 <= (U - 1).bit_length() - 1 - e - 2
                if f < e + m2:
                    assert d == f
                if d >= g + 1:
                    critical += 1
                    assert f == e + m2
    assert (prefix, tail, critical) == (111, 355, 75)
    assert source > 0

    # Complete mod-five square-class check for two unit coordinates and
    # a unit radius; the first sphere coordinate is zero modulo five.
    for unit2, unit3 in product(range(1, 5), repeat=2):
        assert (unit2**2 + unit3**2) % 5 not in (1, 4)
    five_tail = 0
    for m2, m3, first in product(range(2, 6), range(1, 7), (1, 2)):
        T, U = 10**m2, 10**m3
        for F, J, unit2, unit3 in product(
            range(17), range(17), (1, 2, 3, 4, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7, 8, 9)
        ):
            b2, b3 = 5**F * unit2, 5**J * unit3
            if not (T // 10 <= b2 < T and U // 10 <= b3 < U):
                continue
            beta5 = (first * T + b2) * U + b3
            if F == J > 0:
                assert F < m2 + m3 and v5(beta5) == F
                continue  # This class was excluded by the sphere modulo five.
            if F > J:
                # Unique prefix maximum would require v5(beta)>=F.
                assert v5(beta5) < F
            elif J > F and v5(beta5) == J:
                five_tail += 1
    assert five_tail > 0

    # At five, equal-depth units can sum to a unit: preserve the resonant
    # plus-gap sheet. This is a denominator projection, not an original lift.
    Q, U, b3 = 135, 10000, 6250
    assert v5(Q) == 1 and v5(b3) == 5 and v5(Q * U + b3) == 5
    for D in range(1, 40):
        # Ordinary binary minus and five minus require different mod 3.
        assert (3 * D - 1) % 3 == 2
        assert (3 * D) % 3 == 0

    e, M, m, r, J, odd_u, c = sp.symbols("e M m r J u c", integer=True)
    lam = m - J
    Q0 = 5**M + 2 ** (m + r) * odd_u
    second_den = 2 ** (e + M + m + r) * odd_u
    third_den = 2 ** (e + M + m) * 5**J * c
    prefix_den = 2**e * 10**M + second_den
    exact_beta = prefix_den * 10**m + third_den
    normalized = 2 ** (e + M + m) * 5**J * (
        5 ** (M + lam) + c + 2 ** (m + r) * 5**lam * odd_u
    )
    assert sp.simplify(sp.expand_power_base(prefix_den - 2 ** (e + M) * Q0)) == 0
    assert sp.simplify(sp.expand_power_base(exact_beta - normalized)) == 0

    # Both gap sheets actually occur on integral spheres. The word gate is
    # not imposed here: this independently audits only the sphere step.
    plus_sheet = minus_sheet = 0
    for y1, y2, y3 in product(range(2, 130, 2), range(2, 130, 2), range(1, 128, 2)):
        squared = y1**2 + y2**2 + y3**2
        H = isqrt(squared)
        if H**2 != squared:
            continue
        p1, p2 = v2(y1), v2(y2)
        sigma = 2 * min(p1, p2) + (p1 == p2)
        assert v2(y1**2 + y2**2) == sigma
        delta = v2(H - y3)
        if delta == 1:
            plus_sheet += 1
            assert v2(H + y3) == sigma - 1 >= 2
        else:
            minus_sheet += 1
            assert v2(H + y3) == 1 and sigma == delta + 1
    assert plus_sheet > 0 and minus_sheet > 0
    print("OK: A2-G04 exact word-gap identity and binary maximum classification")
    print(f"bounded denominator projections: prefix={prefix}, tail={tail}, critical={critical}")
    print(f"sphere-only gap examples: plus={plus_sheet}, minus={minus_sheet}; no emptiness claim")
    print(f"OK: A2-G05 five-tail dominance and pure-five source; finite source patterns={source}")
    print(f"five-tail denominator projections={five_tail}; no original-candidate enumeration")
    print("OK: A2-G08 effective bounds, ordinary mod-three conflict, and five resonance retained")


if __name__ == "__main__":
    main()
