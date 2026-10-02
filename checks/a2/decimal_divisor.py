"""A2-G12: all b2 dividing b1*10**m2, with no length cutoff.

The manuscript proves the unbounded reduction and applies Bugeaud's explicit
Theorem 2. This audit checks the resulting identities, exact constants and
the complete residual exponent certificate; it does not prove that external
theorem. Python integers and Fraction arithmetic have no fixed width.
"""

from fractions import Fraction as F
from math import comb, factorial

import sympy as sp


def vp(value, prime):
    assert value > 0
    depth = 0
    while value % prime == 0:
        value //= prime
        depth += 1
    return depth


def exp_bounds(x, terms=100):
    """Rational Taylor bounds, with a geometric majorant for the tail."""
    x = F(x)
    assert 0 <= x < terms + 2
    lower = sum((x**i / factorial(i) for i in range(terms + 1)), F(0))
    first = x ** (terms + 1) / factorial(terms + 1)
    upper = lower + first / (1 - x / (terms + 2))
    return lower, upper


def exponent_certificate():
    # Bounds used to weaken the explicit external logarithmic estimate.
    # They are certified by rational arithmetic, not floating point logs.
    assert exp_bounds(2)[1] < 8 < exp_bounds(3)[0]
    assert exp_bounds(1)[1] < 25 < exp_bounds(4)[0]
    assert exp_bounds(2)[0] > 3  # log(log(8)) < log(3) < 2
    assert 3 * F("66.8") * 4 / 2**3 < 128
    assert exp_bounds(9)[1] < 1_000_001 < exp_bounds(14)[0]
    endpoint_bound = 128 * 17**2 + 3
    assert endpoint_bound == 36_995 and endpoint_bound < 3_000_000
    # The monotonicity after 10**6 is proved by differentiation in PROOF.md.

    modulus = 2**27
    period = 2**24
    root = 11_278_491
    # Reader 1: Python's modular binary powering, including exact order.
    assert pow(25, period, modulus) == 1
    assert pow(25, period // 2, modulus) != 1
    assert (7 * pow(25, root, modulus) + 1) % modulus == 0

    # Reader 2: start at the unique class modulo order 1, then lift one bit.
    lifted = 0
    for precision in range(4, 28):
        next_modulus = 2**precision
        previous_period = 2 ** (precision - 4)
        candidates = (lifted, lifted + previous_period)
        allowed = [
            r
            for r in candidates
            if (7 * pow(25, r, next_modulus) + 1) % next_modulus == 0
        ]
        assert len(allowed) == 1
        lifted = allowed[0]
    assert lifted == root

    # Reader 3: a different finite expression, not a second pow call.
    truncated_binomial = sum(comb(root, j) * 24**j for j in range(9))
    assert 24**9 % modulus == 0
    assert (7 * truncated_binomial + 1) % modulus == 0
    assert 1_000_000 < root < period
    assert [vp(7 * 25**E + 1, 2) for E in range(2, 9)] == [3, 6, 3, 4, 3, 5, 3]
    assert all(vp(7 * 25**E + 1, 2) < 3 * E for E in range(2, 9))
    # E=1 is deliberately outside the lemma, and must not be silently dropped.
    exceptional_depth = vp(7 * 25 + 1, 2)
    assert exceptional_depth == 4 and exceptional_depth > 3
    print("Exponent certificate: explicit E<1000000; E>=9 excluded by")
    print(f"E={root} mod {period}; E=2..8 checked exactly; E=1 not covered")


def denominator_shapes():
    def smooth(n):
        for p in (2, 5):
            while n % p == 0:
                n //= p
        return n == 1

    rows = []
    for B in (1, 2):
        for K in range(1, 10 * B + 1):
            if not smooth(K):
                continue
            if (B == 1 and 2 * K <= 5) or (B == 2 and K <= 10):
                continue
            r2, r5 = vp(K + 1, 2), vp(K + 1, 5)
            W = (K + 1) // (2**r2 * 5**r5)
            rows.append((B, K, r2, r5, W))
    assert rows == [
        (1, 4, 0, 1, 1),
        (1, 5, 1, 0, 3),
        (1, 8, 0, 0, 9),
        (1, 10, 0, 0, 11),
        (2, 16, 0, 0, 17),
        (2, 20, 0, 0, 21),
    ]
    assert F(1, 1) / (F(2, 5) * F(12, 5)) - F(1, 16) == F(47, 48)
    assert F(1, 1) / (F(1, 5) * F(21, 5)) - F(1, 4) == F(79, 84)
    assert F(5, 2) ** 5 > 11

    remaining = []
    projections = 0
    for B, K, r2, r5, W in rows:
        # Both minus sheets coincide only for K=4, where b/U is a decimal
        # power divided by four. No integer decimal power lies in (2,4).
        assert ((r2 + 1 - r5) % 3 == 0) == (K == 4)
        divisors = [C for C in range(1, W + 1) if W % C == 0]
        for C in divisors:
            d = W // C
            if d % 8 == 7:
                remaining.append((B, K, C, d))
            else:
                assert d % 8 in (1, 3, 5)
                assert vp(1 + d, 2) <= 2
            # Regression projections: identities only, not exact lifts.
            for n in range(5, 10):
                T = 10**n
                M = B * T // K
                f, F5 = vp(M, 2), vp(M, 5)
                assert f > vp(B, 2) and F5 > 0
                Q = B * T + M
                assert Q == M * (K + 1)
                for E in range(2, 10):
                    m = 3 * E - r5
                    D = m + r2 - 1
                    U = 10**m
                    b = M * 2**D * 5**E * C
                    L = 1 + 2 * d * 25**E
                    assert Q * U + b == b * L
                    assert vp(Q, 2) == f + r2 and vp(Q, 5) == F5 + r5
                    projections += 1
    assert remaining == [(2, 20, 3, 7)]
    print(
        f"Six denominator shapes; {projections} identity projections; sole d=7 terminal"
    )


def symbolic_identities():
    b, Q, U, C0, a, H = sp.symbols("b Q U C0 a H")
    alpha, beta = C0 * U + a, Q * U + b
    assert (
        sp.expand(beta * (H - a) - U * (b * C0 - Q * a) - (beta * H - b * alpha)) == 0
    )
    L, d, z = sp.symbols("L d z")
    assert (
        sp.expand(L * (H + a) - C0 * U - 2 * (1 + d * z) * a - (L * H - alpha))
        .subs(L, 1 + 2 * d * z)
        .expand()
        == 0
    )
    x = sp.symbols("x", positive=True)
    f = (sp.log(x + 1) + 3) ** 2 / x
    # The bracket 2x/(x+1) - (log(x+1)+3) is negative for every x>0.
    assert (
        sp.simplify(
            sp.diff(f, x)
            - (sp.log(x + 1) + 3) / x**2 * (2 * x / (x + 1) - sp.log(x + 1) - 3)
        )
        == 0
    )


def main():
    symbolic_identities()
    denominator_shapes()
    exponent_certificate()
    print(
        "PASS: A2-G12 arithmetic audit; full unbounded proof and external input in PROOF.md"
    )


if __name__ == "__main__":
    main()
