"""A2-G13/G14: complete decimal-head tables and fixed exponent certificates.

Python integers/Fraction have no fixed width. The head ranges are exhaustive
by G01, not numerical cutoffs on t or E. PROOF.md supplies the unbounded
gap reduction and the external Bugeaud bound; this program audits their
finite arithmetic consequences. The final residual family is not a solution.
"""

from fractions import Fraction as F
from math import comb, gcd

import sympy as sp
from decimal_divisor import exp_bounds

ROOTS = {
    (1, 7): 11278491,
    (1, 111): 4080162,
    (1, 23): 9812409,
    (1, 39): 9107639,
    (17, 39): 9988485,
    (1, 119): 10397645,
    (1, 31): 7123260,
    (1, 63): 6779384,
    (13, 3): 3170470,
    (1, 127): 6463984,
    (29, 43): 1037599,
    (29, 3): 10147948,
    (13, 139): 8546749,
    (1, 71): 5210195,
    (17, 31): 8004106,
    (17, 7): 12159337,
}


def vp(value, prime):
    assert value > 0
    depth = 0
    while value % prime == 0:
        value //= prime
        depth += 1
    return depth


def divisors(value):
    return [d for d in range(1, value + 1) if value % d == 0]


def allowed_common(value):
    return [
        d
        for d in divisors(value)
        if gcd(d, value // d) == 1 and all(p % 4 == 1 for p in sp.factorint(d))
    ]


def caps(B, r, h):
    x = F(r, 10**h)
    first = range(1, 9) if B == 1 else (5, 7, 9, 11, 13)
    return {
        A: F((A + 1) ** 2) / (B + x) ** 2 - F(A * A, B * B) - 1 / (100 * x * x)
        for A in first
    }


def normalized_window(kappa):
    """Exhaust all integer s with 1/2 < kappa*10**s < 1, without a cutoff."""
    rho, s = F(kappa), 0
    while rho >= 1:
        rho /= 10
        s -= 1
    while rho < F(1, 10):
        rho *= 10
        s += 1
    assert F(1, 10) <= rho < 1
    # Other s are <= rho/10 < 1/10 or >= 10*rho >= 1.
    return (rho, s) if rho > F(1, 2) else None


def head_certificate():
    # Independent full 1..99 rational scan, compared to the analytic intervals.
    actual = [
        (B, r, h)
        for h in (1, 2)
        for B in (1, 2)
        for r in range(10 ** (h - 1), 10**h)
        if r % 10 and max(caps(B, r, h).values()) > 1
    ]
    expected = [(1, 1, 1), (1, 2, 1), (1, 3, 1), (2, 1, 1)]
    expected += [(1, r, 2) for r in range(11, 40) if r % 10]
    expected += [(2, r, 2) for r in range(11, 19)]
    assert actual == expected and len(actual) == 39
    assert F(1) / (F(19, 100) * F(419, 100)) - F(100, 361) < 1
    # G13's sole new ray has C in {1,13}; its plus-word second term has depth 2.
    assert allowed_common(3) == [1] and divisors(13) == [1, 13]
    assert all(d % 4 == 1 for d in (1, 13))
    assert F(5, 2) ** 5 > 33 and F(5, 2) ** 7 > 429
    assert 2**6 < 4 * 10**3

    terminals = set()
    minus_heads, survivors = [], []
    projections = 0
    for B, r, h in actual:
        if h == 1:
            continue
        u, v = vp(r, 2), vp(r, 5)
        r0 = r // (2**u * 5**v)
        q0 = 100 * B + r
        r2, r5 = vp(q0, 2) - u, vp(q0, 5) - v
        W = q0 // (2 ** vp(q0, 2) * 5 ** vp(q0, 5))
        e = vp(B, 2)
        assert gcd(r0, W) == 1
        assert u - e - 4 <= 1  # second-denominator dominance would give m<=1
        assert -3 <= r2 <= 5 and r5 in (0, 1)
        assert (r5 == 1) == ((B, r) == (1, 25))
        assert (r2 > 2) == ((B, r) == (1, 28))
        if r2 > 2:
            assert r2 == 5 and u == 2
        if u < e + 2:  # low-tail remainder after F03
            assert r2 == 0
        common = allowed_common(r0)
        if (r2 + 1 - r5) % 3 == 0:
            assert common == [1]
            minus_heads.append((B, r))
        for cm in common:
            for cq in divisors(W):
                d = W // cq
                if (cm + d) % 8 == 0:
                    assert r5 == 0 and r2 >= -1
                    terminals.add((cm, d))
                else:
                    assert vp(cm + d, 2) <= 2
                if (r2 + 1 - r5) % 3 == 0:
                    z = (r2 + 1 - r5) // 3
                    kappa = F(2) ** (u + z) * 5**v * cm * cq
                    window = normalized_window(kappa)
                    if window is not None:
                        rho, s = window
                        allowed_A = tuple(
                            A for A, cap in caps(B, r, h).items() if 1 / rho**2 < cap
                        )
                        survivors.append((B, r, cq, rho, s - r5, allowed_A))
                # Exact substitution audits of the parameterized identities;
                # not asserted to be original candidates or a global search.
                for t in (3, 4, 9):
                    for E in (3, 4, 8):
                        m = 3 * E - r5
                        D = m + r2 - 1
                        assert D >= 2
                        U = 10**m
                        M, Q = r * 10**t, q0 * 10**t
                        b = 10**t * 2 ** (u + D) * 5 ** (v + E) * cm * cq
                        L = cm + 2 * d * 25**E
                        assert cm * (Q * U + b) == b * L
                        assert gcd(M, b) == 10**t * 2**u * 5**v * cm
                        assert (M * b // gcd(M, b)) == (r0 // cm) * b
                        projections += 1
    assert terminals == set(ROOTS)
    assert minus_heads == [(1, 12), (1, 24), (1, 25), (1, 28), (2, 16)]
    assert survivors == [
        (1, 12, 1, F(4, 5), -1, (2, 3, 4, 5, 6)),
        (1, 12, 7, F(14, 25), -2, (4,)),
        (1, 24, 1, F(4, 5), -1, (2,)),
    ]
    # Low-tail plus branch: exact depth 6, not merely divisibility by 64.
    residues = [d for d in range(1, 128, 2) if vp(1 + 625 * d, 2) == 6]
    assert residues == [47]
    assert all(d % 128 != 47 for d in [*range(111, 140), *range(211, 219)])
    for _, r, _, _, offset, _ in survivors:
        t = 4 + offset  # E=2
        assert t < 3 or (t + vp(r, 2) >= t + 2 and 3 * 2 <= 6)
    print(f"39 complete heads (35 two-digit); {projections} exact identity projections")
    print("Both-minus: five complete head rows, three intermediate families with E>=3")
    print("Plus: all m<=6 excluded; m>=7 reduces to 16 fixed coefficient pairs")


def exponent_certificate():
    assert exp_bounds(2)[1] < 8 < exp_bounds(3)[0]
    assert exp_bounds(1)[1] < 25 < exp_bounds(4)[0]
    assert exp_bounds(5)[0] > 139
    assert 3 * F("66.8") * 4 * 5 / 2**4 < 256
    assert exp_bounds(9)[1] < 1_000_001 < exp_bounds(14)[0]
    endpoint_bound = 256 * 17**2 + 3
    assert endpoint_bound == 73987 and endpoint_bound < 3_000_000
    modulus, period = 2**27, 2**24
    assert pow(25, period, modulus) == 1
    assert pow(25, period // 2, modulus) != 1
    for (cm, d), root in ROOTS.items():
        assert gcd(cm, d) == 1 and vp(cm + d, 2) >= 3
        assert max(8, cm, d) <= 139
        # Reader 1: exact modular binary exponentiation.
        assert (cm + d * pow(25, root, modulus)) % modulus == 0
        # Reader 2: every precision has precisely one successor exponent class.
        lifted = 0
        for precision in range(4, 28):
            options = (lifted, lifted + 2 ** (precision - 4))
            allowed = [
                x
                for x in options
                if (cm + d * pow(25, x, 2**precision)) % 2**precision == 0
            ]
            assert len(allowed) == 1
            lifted = allowed[0]
        assert lifted == root
        # Reader 3: independent finite binomial expression for (1+24)**root.
        truncated = sum(comb(root, j) * 24**j for j in range(9))
        assert 24**9 % modulus == 0
        assert (cm + d * truncated) % modulus == 0
        assert 1_000_000 < root < period
        assert all(vp(cm + d * 25**E, 2) < 3 * E for E in range(3, 9))
    # Preserve genuine small-index exceptions outside the stated lemma.
    exceptional_depth = vp(1 + 111 * 25**2, 2)
    assert exceptional_depth == 8 and exceptional_depth > 6
    assert vp(17 + 31 * 25**2, 2) == 6
    print("16 coefficient pairs: explicit E<1000000; three readers per full cycle")
    print("E>=9 has no class in the proved bound; all E=3..8 excluded exactly")


def symbolic_identities():
    H, V, a, cm, d, z, C0, U = sp.symbols("H V a cm d z C0 U")
    L, r0 = cm + 2 * d * z, V * cm
    alpha = C0 * U + a
    assert sp.expand(
        L * (H + V * a) - r0 * C0 * U - 2 * V * (cm + d * z) * a
    ) == sp.expand(L * H - r0 * alpha)
    b, Q = sp.symbols("b Q")
    beta = Q * U + b
    assert sp.expand(beta * (H - V * a) - V * U * (b * C0 - Q * a)) == sp.expand(
        beta * H - V * b * alpha
    )


def minus_unit_obstructions():
    z, A, N, a, k = sp.symbols("z A N a k")
    H = 3 * a + 2 * z**2 * k
    U = z**3
    for second in (False, True):
        if second:
            T, M, b = z**2, sp.Rational(3, 25) * z**2, sp.Rational(14, 25) * z**3
            word = (
                (1 + 2 * z**2) * k - sp.Rational(3, 2) * A * z**3 - 15 * N * z + 3 * a
            )
            sphere = (
                k * (3 * a + z**2 * k) - sp.Rational(441, 625) * A**2 * z**4 - 49 * N**2
            )
            sphere_scale = 4 * z**2
        else:
            T, M, b = 10 * z**2, sp.Rational(6, 5) * z**2, sp.Rational(4, 5) * z**3
            word = (1 + 14 * z**2) * k - 15 * A * z**3 - 15 * N * z + 21 * a
            sphere = k * (H + 3 * a) - sp.Rational(72, 25) * A**2 * z**4 - 2 * N**2
            sphere_scale = 2 * z**2
        alpha, beta = (A * T + 10 * N) * U + a, (T + M) * U + b
        assert sp.expand(beta * H - 3 * b * alpha - 2 * b * z**2 * word) == 0
        q = 3 * b
        original_sphere = H**2 - (q * A) ** 2 - (q * N / M) ** 2 - (3 * a) ** 2
        assert sp.expand(original_sphere - sphere_scale * sphere) == 0
    assert {a * a % 5 for a in range(1, 5)} == {1, 4}
    assert all((-a * a - 2 * N * N) % 5 for a in range(1, 5) for N in range(1, 5))
    assert all((-9 * a * a - N * N) % 8 for a in (1, 3, 5, 7) for N in (1, 3, 5, 7))
    print(
        "Two r=12 families: exact original word/sphere identities, mod5/mod8 contradictions"
    )
    print("Only necessary family left: B=1,A=2,M=24*10**(2E-1),b=8*10**(3E-1),E>=3")


def residual_family_identity():
    """Audit the open route's exact equations; no claim of emptiness."""
    z, N, a, k = sp.symbols("z N a k")
    T, M = 10 * z**2, sp.Rational(12, 5) * z**2
    U, b = z**3, sp.Rational(4, 5) * z**3
    q = 3 * b
    H = 3 * a + z**2 * k / 2
    alpha, beta = (2 * T + 10 * N) * U + a, (T + M) * U + b
    word = (1 + 31 * z**2 / 2) * k - 120 * z**3 - 60 * N * z + 93 * a
    sphere = k * (3 * a + z**2 * k / 4) - sp.Rational(576, 25) * z**4 - N**2
    assert sp.expand(beta * H - q * alpha - b * z**2 * word / 2) == 0
    assert (
        sp.expand(H**2 - (2 * q) ** 2 - (q * N / M) ** 2 - (3 * a) ** 2 - z**2 * sphere)
        == 0
    )
    conic = (
        31 * N**2
        - 60 * z * N * k
        + (1 + 31 * z**2 / 4) * k**2
        - 120 * z**3 * k
        + sp.Rational(17856, 25) * z**4
    )
    assert sp.expand(conic + 31 * sphere - k * word) == 0


def main():
    symbolic_identities()
    head_certificate()
    exponent_certificate()
    minus_unit_obstructions()
    residual_family_identity()
    print("PASS: A2-G13 empty; A2-G14 necessary classification, one family still open")


if __name__ == "__main__":
    main()
