#!/usr/bin/env python3
"""Exact certificate for the A1 k=2g-2 pure-5 terminal, g>=5.

No factorization and no floating point are used.

Inputs:
  * J in {0,...,108};
  * 0 < (J+1)10^(g-2)-rho < 4000/10^(2g);
  * pure-5 L=5^b has b>=4 even;
  * M=2^(2g-3)m, m | b1*Q0;
  * exact low-2 resonance
        v2(m + 5^(2g+b-2) Q0) = 2g-4 + 3b/2;
  * phase/divisor height gives g<=16.
"""

TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def admissible_b_values(g: int, w: int):
    H = 10**g
    b1 = 10 ** (4 * g - 3) - w
    Q0 = 10 * b1 + 1
    P = b1 * Q0

    b = 4
    while H * 5**b < 101 * 2 ** (2 * g - 3) * P:
        if 4000 * 5**b > H**2:
            yield b
        b += 2


def exact_a_candidates(g: int, w: int, J: int, b: int):
    H = 10**g
    b1 = 10 ** (4 * g - 3) - w
    Q0 = 10 * b1 + 1

    # a=(J+1)5^(g+b-2)-2^(g-1)m and
    # t=A_J H^2/5^b=2^(3g-2)5^(2g-b)a.
    scale = 2 ** (3 * g - 2) * 5 ** (2 * g)
    amax = (4000 * 5**b - 1) // scale
    if amax < 1:
        return []

    resonance = 2 * g - 4 + 3 * b // 2
    e = resonance + g - 1
    mod = 2**e
    mod2 = 2 * mod
    B0 = (
        (J + 1) * 5 ** (g + b - 2)
        + 2 ** (g - 1) * 5 ** (2 * g + b - 2) * Q0
    )

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
        for g in range(5, 17):
            b1 = 10 ** (4 * g - 3) - w
            Q0 = 10 * b1 + 1
            P = b1 * Q0

            for J in range(109):
                for b in admissible_b_values(g, w):
                    state_count += 1
                    for a in exact_a_candidates(g, w, J, b):
                        gap_a_candidates += 1

                        numerator = (J + 1) * 5 ** (g + b - 2) - a
                        denominator = 2 ** (g - 1)
                        assert numerator > 0
                        assert numerator % denominator == 0
                        m = numerator // denominator
                        assert m > 0 and m % 2 == 1 and m % 5 != 0

                        c = 5 ** (2 * g + b - 2)
                        resonance = 2 * g - 4 + 3 * b // 2
                        assert v2(m + c * Q0) == resonance

                        if P % m == 0:
                            divisor_survivors.append((z, w, g, J, b, a, m, P // m))

    print(f"states={state_count}")
    print(f"gap_a_candidates={gap_a_candidates}")
    print(f"divisor_survivors={len(divisor_survivors)}")
    for row in divisor_survivors:
        print(row)

    assert state_count == 328308
    assert gap_a_candidates == 23554
    assert divisor_survivors == []


if __name__ == "__main__":
    main()
