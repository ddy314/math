#!/usr/bin/env python3
"""Exact certificate for the A1 k=2g-1 pure-5 terminal, g>=4.

No factorization and no floating point are used.

Input theorems / reductions:
  * d=2, r=s=1, k=2g-1, J in {0,...,9};
  * pure-5 L=5^b has b>=3 odd;
  * the off-diagonal phase shell
        0 < (J+1)10^(g-1) - rho < 400/10^(2g);
  * pure-5 low-2 resonance
        v2(m + 5^(2g+b-1) Q0) = 2g + (3b-5)/2,
    where M=2^(2g-2)m and m | b1*Q0;
  * phase/divisor height gives g<=10.

For every exact state in the resulting finite box the script enumerates the
possible positive gap integer a, recovers m, checks the exact resonance, and
finally checks the necessary divisor condition m | b1*Q0.
"""

TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def admissible_b_values(g: int, w: int):
    H = 10**g
    b1 = 10 ** (4 * g - 1) - w
    Q0 = 10 * b1 + 1
    P = b1 * Q0

    # Pure-5 high branch has b>=3 odd.  The phase gap gives
    # 5^b > H^2/400.  Also rho>H/11, m<=P and
    # M=2^(2g-2)m imply
    #     H*5^b < 11*2^(2g-2)*P.
    b = 3
    while H * 5**b < 11 * 2 ** (2 * g - 2) * P:
        if 400 * 5**b > H**2:
            yield b
        b += 2


def exact_a_candidates(g: int, w: int, J: int, b: int):
    H = 10**g
    b1 = 10 ** (4 * g - 1) - w
    Q0 = 10 * b1 + 1

    # Put
    #   a=(J+1)5^(g+b-1)-2^(g-1)m > 0.
    # Then A_J=2^(g-1)a and
    #   t=A_J H^2/5^b = 2^(3g-1)5^(2g-b)a.
    # The phase shell only needs 0<t<400.
    scale = 2 ** (3 * g - 1) * 5 ** (2 * g)
    amax = (400 * 5**b - 1) // scale
    if amax < 1:
        return []

    # Exact low-2 resonance:
    #   r=v2(m+5^(2g+b-1)Q0)=2g+(3b-5)/2.
    # Since
    #   2^(g-1)(m+cQ0)=B0-a,
    # exact valuation becomes
    #   v2(B0-a)=e=r+g-1.
    r = 2 * g + (3 * b - 5) // 2
    e = r + g - 1
    mod = 2**e
    mod2 = 2 * mod
    B0 = (
        (J + 1) * 5 ** (g + b - 1)
        + 2 ** (g - 1) * 5 ** (2 * g + b - 1) * Q0
    )

    # v2(B0-a)=e iff a == B0+2^e mod 2^(e+1).
    residue = (B0 + mod) % mod2
    first = residue
    if first < 1:
        first += ((1 - first + mod2 - 1) // mod2) * mod2
    if first > amax:
        return []
    return range(first, amax + 1, mod2)


def main():
    state_count = 0
    gap_a_candidates = 0
    divisor_survivors = []

    for z, w in TYPES:
        for g in range(4, 11):
            H = 10**g
            b1 = 10 ** (4 * g - 1) - w
            Q0 = 10 * b1 + 1
            P = b1 * Q0

            for J in range(10):
                for b in admissible_b_values(g, w):
                    state_count += 1
                    for a in exact_a_candidates(g, w, J, b):
                        gap_a_candidates += 1

                        numerator = (J + 1) * 5 ** (g + b - 1) - a
                        denominator = 2 ** (g - 1)
                        assert numerator > 0
                        assert numerator % denominator == 0
                        m = numerator // denominator
                        assert m > 0 and m % 2 == 1 and m % 5 != 0

                        c = 5 ** (2 * g + b - 1)
                        resonance = 2 * g + (3 * b - 5) // 2
                        assert v2(m + c * Q0) == resonance

                        if P % m == 0:
                            divisor_survivors.append((z, w, g, J, b, a, m, P // m))

    print(f"states={state_count}")
    print(f"gap_a_candidates={gap_a_candidates}")
    print(f"divisor_survivors={len(divisor_survivors)}")
    for row in divisor_survivors:
        print(row)

    assert state_count == 12420
    assert gap_a_candidates == 1457
    assert divisor_survivors == []


if __name__ == "__main__":
    main()
