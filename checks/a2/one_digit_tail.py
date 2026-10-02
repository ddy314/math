"""A2-F01: finite periodic obstruction for every odd one-digit tail.

All integers have arbitrary precision. Exponents are represented by their
complete periods, starting with T=10**2; there is no exponent cutoff.
The independent C++ reader expands the square polynomial into coefficients.
The analytic even-tail part and tag bounds are proved in PROOF.md.
"""

from collections import Counter
from functools import cache
from math import gcd, isqrt


def primes_through(limit):
    return [
        n
        for n in range(3, limit + 1)
        if n != 5 and all(n % d for d in range(2, isqrt(n) + 1))
    ]


@cache
def orbit(modulus):
    assert gcd(modulus, 10) == 1
    first = 100 % modulus
    values = [first]
    value = first * 10 % modulus
    while value != first:
        values.append(value)
        value = value * 10 % modulus
    return tuple(values)


def square_polynomial(tag, value):
    A, b, a, c, k = tag
    h = (k + 10 * c) ** 2 - (100 * c) ** 2
    return k**2 * b**2 * (10 * A * value + a) ** 2 - h * (
        A**2 * b**2 + a**2
    ) * (10 * value + b) ** 2


def empty_by_periods(tag, prime_data):
    _, b, _, _, k = tag
    values = orbit(k)
    allowed = {i for i, value in enumerate(values) if (10 * value + b) % k == 0}
    if not allowed:
        return "integrality"
    constraints = [(len(values), allowed)]
    for p, values, squares in prime_data:
        allowed = {
            i
            for i, value in enumerate(values)
            if square_polynomial(tag, value) % p in squares
        }
        if not allowed:
            return f"single-prime-{p}"
        constraints.append((len(values), allowed))

    # If a common exponent exists, its residues agree modulo every gcd of
    # two periods. Removing incompatible residues is always sound; a
    # nonempty fixed point would not assert an original candidate.
    changed = True
    while changed:
        changed = False
        for i, (period_i, allowed_i) in enumerate(constraints):
            for period_j, allowed_j in constraints:
                common = gcd(period_i, period_j)
                projection = {r % common for r in allowed_j}
                reduced = {r for r in allowed_i if r % common in projection}
                if len(reduced) < len(allowed_i):
                    changed = True
                    allowed_i = reduced
                    constraints[i] = (period_i, reduced)
                    if not reduced:
                        return "joint-periods"
    return None


def main():
    primes = primes_through(241)
    prime_data = [(p, orbit(p), {i * i % p for i in range(p)}) for p in primes]
    counts = Counter()
    tags = 0
    for A in (2, 4, 6, 8):
        for b in (7, 9):
            for a in range(10, 2 * b):
                if gcd(a, b) != 1:
                    continue
                for c in range(1, b + 1):
                    if b % c:
                        continue
                    for k in range(10 * c + 1, 101 * c, 2):
                        if gcd(k, 10 * b) != 1:
                            continue
                        tag = (A, b, a, c, k)
                        tags += 1
                        obstruction = empty_by_periods(tag, prime_data)
                        assert obstruction is not None, f"uncovered tag: {tag}"
                        counts[obstruction] += 1
    assert tags == 11544 and sum(counts.values()) == tags
    print("OK: A2-F01 odd one-digit tail: 11544 / 11544 tags excluded")
    print("All m2>=2 represented by complete exponent periods; primes 3..241 except 5")
    print("Python arbitrary-precision reader:", dict(sorted(counts.items())))
    print("Even one-digit tails are excluded analytically by A2-G04/G05 in PROOF.md")


if __name__ == "__main__":
    main()
