"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0506; see history/sources.json.
"""

import argparse
from fractions import Fraction
from functools import partial
from math import gcd, lcm

from single_digits import positive_roots, record_candidate

EXPECTED_STATES = (
    (11, 1, 1), (5, 1, 5), (15, 1, 5), (7, 2, 8), (33, 3, 3),
    (5, 5, 1), (15, 5, 1), (85, 5, 1), (255, 5, 1), (265, 5, 3),
    (1, 5, 5), (11, 5, 5), (55, 5, 5), (40, 5, 6), (280, 5, 6),
    (1, 6, 8), (15, 7, 5), (77, 7, 7), (99, 9, 9),
)
EXPECTED_COUNTS = (
    3015, 784, 1456, 515, 1344, 360, 630, 5481, 10863, 10824,
    112, 608, 2160, 339, 2460, 40, 384, 2296, 1344,
)


def valuation(n, p):
    assert n > 0
    depth = 0
    while n % p == 0:
        n //= p
        depth += 1
    return depth


def prime_factors(n):
    result = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def denominator_states():
    states = []
    original_count = 0
    for b2 in range(1, 10):
        for b3 in range(1, 10):
            for b1 in divisors(lcm(b2, b3, 10*b2+b3)):
                original_count += 1
                bs = (b1, b2, b3)
                qprefix = 10*b1+b2
                denominator = 10*qprefix+b3
                if (10*qprefix) % b3:
                    continue
                depths = [valuation(b, 2) for b in bs]
                maximum = max(depths)
                if maximum and (depths.count(maximum) != 1 or b3 % 2
                                or valuation(denominator, 2) != maximum):
                    continue
                if maximum >= 2 and depths.count(maximum-1) == 1:
                    continue
                incompatible = False
                for p in prime_factors(lcm(*bs)):
                    depths = [valuation(b, p) for b in bs]
                    maximum = max(depths)
                    if ((depths.count(maximum) == 1
                         or (depths.count(maximum) == 2 and p % 4 == 3))
                            and valuation(denominator, p) < maximum):
                        incompatible = True
                        break
                if incompatible:
                    continue
                minimum3 = min(valuation(b, 3) for b in bs)
                cs = [b//3**minimum3 for b in bs]
                if sum(cs[i]*cs[j] for i, j in ((0, 1), (1, 2), (2, 0))) % 9 in (3, 6):
                    continue
                # Universal mod-5 condition; the DD-only mod-25 version is
                # intentionally not used for the n3=1 certificate.
                if b3 == 5 and b1*b2 % 5 and qprefix % 5 != 4:
                    continue
                states.append(bs)
    assert original_count == 994, original_count
    assert tuple(states) == EXPECTED_STATES, states
    return states


def strict_cap(bound):
    """Largest integer strictly below a positive rational bound."""
    return (bound.numerator-1)//bound.denominator


def certificate(reader):
    hits = set()
    counts = []
    for bs in denominator_states():
        b1, b2, b3 = bs
        d = 100*b1+10*b2+b3
        q = lcm(*bs)
        cs = [q//b for b in bs]
        uniform = strict_cap((Fraction(100, b2)+Fraction(9, b3))
                             / (Fraction(1000, d)-Fraction(1, b1)))
        a2cap = strict_cap(Fraction(q*b2, 2)
                          * (Fraction(uniform, b1)**2+Fraction(9, b3)**2))
        n2cap = len(str(a2cap))
        assert uniform <= 823 and n2cap <= 5
        count = 0

        record = partial(record_candidate, y=10, denominators=bs,
                         coefficients=cs, q2=q*q, d=d, hits=hits)

        for n2 in range(2, n2cap+1):
            x = 10**n2
            a1cap = strict_cap((Fraction(x, b2)+Fraction(9, b3))
                              / (Fraction(10*x, d)-Fraction(1, b1)))
            for a1 in range(1, a1cap+1):
                if gcd(a1, b1) != 1:
                    continue
                for a3 in range(1, 10):
                    if gcd(a3, b3) != 1:
                        continue
                    count += 1
                    roots = positive_roots(q*q, d, 10, a1*x*10+a3, cs[1],
                                           (cs[0]*a1)**2+(cs[2]*a3)**2, reader)
                    for a2 in roots:
                        record((a1, a2, a3), x)
        # This solves for every positive a1, without a height cutoff.
        for a2 in range(1, 10):
            if gcd(a2, b2) != 1:
                continue
            for a3 in range(1, 10):
                if gcd(a3, b3) != 1:
                    continue
                count += 1
                roots = positive_roots(q*q, d, 100, 10*a2+a3, cs[0],
                                       (cs[1]*a2)**2+(cs[2]*a3)**2, reader)
                for a1 in roots:
                    record((a1, a2, a3), 10)
        print(f"{bs}: a1cap={uniform}; n2cap={n2cap}; rows={count}")
        counts.append(count)
    assert tuple(counts) == EXPECTED_COUNTS, counts
    assert not hits, sorted(hits)
    return sum(counts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reader", choices=("standard", "factored"), default="standard")
    args = parser.parse_args()
    count = certificate(args.reader)
    assert count == 45_015
    print(f"PASS: reader={args.reader}; 19 denominator states; {count} rows; 0 exact hits")
    print("Scope: n3=1 single-digit denominator suffix; DD companion covers n3>=2.")


if __name__ == "__main__":
    main()
