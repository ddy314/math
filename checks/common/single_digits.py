"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0505; see history/sources.json.
"""

import argparse
from functools import partial
from math import gcd, isqrt, lcm


def positive_roots(q2, denominator, coefficient, known, ghost_coefficient, rest, reader):
    """Solve q²(Cx*x+K)² = D²(cx²*x²+S) in positive integers."""
    a = q2 * coefficient**2 - denominator**2 * ghost_coefficient**2
    b = 2 * q2 * coefficient * known
    c = q2 * known**2 - denominator**2 * rest
    if a == 0:
        assert b > 0  # positive coefficient and nonempty positive known prefix
        return {-c // b} if (-c) % b == 0 and -c // b > 0 else set()
    if reader == "standard":
        discriminant = b*b - 4*a*c
        if discriminant < 0:
            return set()
        root = isqrt(discriminant)
        if root*root != discriminant:
            return set()
        numerators, divisor = (-b-root, -b+root), 2*a
    else:
        # B²-4AC = 4D² [q² cx² K² + A S], without floating point.
        square = q2 * ghost_coefficient**2 * known**2 + a * rest
        if square < 0:
            return set()
        root = isqrt(square)
        if root*root != square:
            return set()
        center = -q2 * coefficient * known
        numerators, divisor = (center-denominator*root, center+denominator*root), a
    return {n//divisor for n in numerators if n % divisor == 0 and n//divisor > 0}


def record_candidate(values, x, y, *, denominators, coefficients, q2, d, hits):
    a1, a2, a3 = values
    if not (x//10 <= a2 < x and y//10 <= a3 < y):
        return
    if any(gcd(a, b) != 1 for a, b in zip(values, denominators)):
        return
    alpha = (a1*x+a2)*y+a3
    sphere = sum((c*a)**2 for c, a in zip(coefficients, values))
    assert q2*alpha**2 == d*d*sphere
    b1, b2, b3 = denominators
    hits.add((a1, b1, a2, b2, a3, b3))


def certificate(reader="standard", tail_one_only=False):
    counts = {"tail>=3": 0, "tail=2,second>=2": 0,
              "tail=2,second=1": 0, "tail=1,second>=3": 0,
              "tail=1,second<=2": 0}
    hits = set()
    for b1 in range(1, 10):
        for b2 in range(1, 10):
            for b3 in range(1, 10):
                q = lcm(b1, b2, b3)
                q2 = q*q
                c1, c2, c3 = q//b1, q//b2, q//b3
                d = 100*b1 + 10*b2 + b3

                check = partial(record_candidate, denominators=(b1, b2, b3),
                                coefficients=(c1, c2, c3), q2=q2, d=d, hits=hits)

                if not tail_one_only:
                    for n3 in range(3, 9):
                        y = 10**n3
                        for n2 in (1, 2):
                            x = 10**n2
                            for a1 in range(1, 111):
                                if gcd(a1, b1) != 1:
                                    continue
                                for a2 in range(x//10, x):
                                    if gcd(a2, b2) != 1:
                                        continue
                                    counts["tail>=3"] += 1
                                    for a3 in positive_roots(q2, d, 1, (a1*x+a2)*y,
                                            c3, (c1*a1)**2+(c2*a2)**2, reader):
                                        check((a1, a2, a3), x, y)
                    y = 100
                    for n2 in range(2, 9):
                        x = 10**n2
                        for a1 in range(1, 23):
                            if gcd(a1, b1) != 1:
                                continue
                            for a3 in range(10, 100):
                                if gcd(a3, b3) != 1:
                                    continue
                                counts["tail=2,second>=2"] += 1
                                for a2 in positive_roots(q2, d, y, a1*x*y+a3,
                                        c2, (c1*a1)**2+(c3*a3)**2, reader):
                                    check((a1, a2, a3), x, y)
                    x = 10
                    for a2 in range(1, 10):
                        if gcd(a2, b2) != 1:
                            continue
                        for a3 in range(10, 100):
                            if gcd(a3, b3) != 1:
                                continue
                            counts["tail=2,second=1"] += 1
                            for a1 in positive_roots(q2, d, x*y, a2*y+a3,
                                    c1, (c2*a2)**2+(c3*a3)**2, reader):
                                check((a1, a2, a3), x, y)

                y = 10
                for n2 in range(3, 9):
                    x = 10**n2
                    for a1 in range(1, 112):
                        if gcd(a1, b1) != 1:
                            continue
                        for a3 in range(1, 10):
                            if gcd(a3, b3) != 1:
                                continue
                            counts["tail=1,second>=3"] += 1
                            for a2 in positive_roots(q2, d, y, a1*x*y+a3,
                                    c2, (c1*a1)**2+(c3*a3)**2, reader):
                                check((a1, a2, a3), x, y)
                for n2 in (1, 2):
                    x = 10**n2
                    for a2 in range(x//10, x):
                        if gcd(a2, b2) != 1:
                            continue
                        for a3 in range(1, 10):
                            if gcd(a3, b3) != 1:
                                continue
                            counts["tail=1,second<=2"] += 1
                            for a1 in positive_roots(q2, d, x*y, a2*y+a3,
                                    c1, (c2*a2)**2+(c3*a3)**2, reader):
                                check((a1, a2, a3), x, y)
    return counts, hits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reader", choices=("standard", "factored"), default="standard")
    parser.add_argument("--tail-one-only", action="store_true",
                        help="Only certify n3=1; the DD companion certifies n3>=2.")
    args = parser.parse_args()
    # Exact checks of the global sphere-gap bounds used to cut off the loops.
    assert 6561*(110**2+99**2) < 2*10**8
    assert 6561*(22**2+99**2) < 2*10**8
    assert 6561*(111**2+9**2) < 2*10**8
    counts, hits = certificate(args.reader, args.tail_one_only)
    expected = {"tail>=3": 20_104_038, "tail=2,second>=2": 4_258_548,
                "tail=2,second=1": 259_380, "tail=1,second>=3": 1_927_530,
                "tail=1,second<=2": 286_605}
    if args.tail_one_only:
        expected.update({name: 0 for name in expected if name.startswith(("tail>=", "tail=2"))})
    assert counts == expected, counts
    for name, count in counts.items():
        print(f"{name}: {count} quadratic rows")
    print(f"reader={args.reader}; total={sum(counts.values())}; exact hits={len(hits)}")
    assert not hits, sorted(hits)
    scope = "n3=1 single-digit denominator subdomain" if args.tail_one_only else (
        "complete single-digit denominator subdomain"
    )
    print(f"PASS: {scope}; no full-branch closure")


if __name__ == "__main__":
    main()
