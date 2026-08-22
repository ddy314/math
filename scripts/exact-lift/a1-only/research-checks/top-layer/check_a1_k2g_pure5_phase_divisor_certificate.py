#!/usr/bin/env python3
"""Exact finite certificate for the A1 k=2g, J=0, pure-5 terminal.

No factorization and no floating point are used.

Input theorems:
  * w=1: 299/10 < t < 305/10
  * w=3: 219/10 < t < 225/10
  * L=5^b, b>=2 even
  * exact high-2 resonance:
        v2(m + 5^(2g+b) Q0) = 2g + 3b/2 - 1
  * finite-height resultant bounds:
        g<=56 for w=1, g<=54 for w=3
  * m | b1*Q0

The script enumerates the exact arithmetic residue classes for the gap integer
'a' and checks the final divisor condition.
"""


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def admissible_b_values(g: int, w: int):
    H = 10**g
    b1 = 10 * H**4 - w
    Q0 = 100 * H**4 - (10 * w - 1)
    P = b1 * Q0

    b = 2
    while True:
        # rho>H/2 gives m>(5/2)^g 5^b, while m<=P.
        # Therefore 5^(g+b) < 2^g P is necessary.
        if 5 ** (g + b) >= (2**g) * P:
            break

        # ultrathin gap gave L=5^b > H^2/95.
        if 95 * 5**b > H**2:
            yield b
        b += 2


def exact_a_candidates(g: int, w: int, b: int):
    H = 10**g
    Q0 = 100 * H**4 - (10 * w - 1)

    if w == 1:
        alpha, beta = 299, 305
    elif w == 3:
        alpha, beta = 219, 225
    else:
        raise AssertionError(w)

    # t = 2^(3g) 5^(2g-b) a.
    # alpha/10 < t < beta/10 becomes
    # alpha 5^b < 10*2^(3g)*5^(2g)*a < beta 5^b.
    scale = 10 * 2 ** (3 * g) * 5 ** (2 * g)
    p5b = 5**b
    amin = (alpha * p5b) // scale + 1
    amax = (beta * p5b - 1) // scale
    if amin > amax:
        return []

    # a = 5^(g+b) - 2^(g-1)m.
    # Put c=5^(2g+b).  Then
    # B0-a = 2^(g-1)(m+cQ0),
    # and exact high-2 resonance says
    # v2(B0-a)=3g+3b/2-2.
    e = 3 * g + 3 * b // 2 - 2
    mod = 2**e
    mod2 = 2 * mod
    B0 = 5 ** (g + b) + 2 ** (g - 1) * 5 ** (2 * g + b) * Q0

    # Exact valuation e is equivalent to
    # a == B0 + 2^e (mod 2^(e+1)).
    residue = (B0 + mod) % mod2
    first = residue
    if first < amin:
        first += ((amin - first + mod2 - 1) // mod2) * mod2
    if first > amax:
        return []
    return list(range(first, amax + 1, mod2))


def main():
    gmax = {1: 56, 3: 54}

    state_count = 0
    a_candidate_count = 0
    divisor_survivors = []
    audit_rows = []

    for w in (1, 3):
        for g in range(1, gmax[w] + 1):
            H = 10**g
            b1 = 10 * H**4 - w
            Q0 = 100 * H**4 - (10 * w - 1)
            P = b1 * Q0

            for b in admissible_b_values(g, w):
                state_count += 1
                cands = exact_a_candidates(g, w, b)
                a_candidate_count += len(cands)

                for a in cands:
                    numerator = 5 ** (g + b) - a
                    denominator = 2 ** (g - 1)
                    assert numerator > 0
                    assert numerator % denominator == 0
                    m = numerator // denominator

                    c = 5 ** (2 * g + b)
                    resonance = 2 * g + 3 * b // 2 - 1
                    assert v2(m + c * Q0) == resonance

                    remainder = P % m
                    audit_rows.append((g, w, b, a, m, remainder))
                    if remainder == 0:
                        divisor_survivors.append((g, w, b, a, m, P // m))

    print(f"states={state_count}")
    print(f"gap_a_candidates={a_candidate_count}")
    print(f"divisor_survivors={len(divisor_survivors)}")
    print("candidate_rows:")
    for row in audit_rows:
        print(row)

    assert state_count == 12738
    assert a_candidate_count == 12
    assert divisor_survivors == []


if __name__ == "__main__":
    main()
