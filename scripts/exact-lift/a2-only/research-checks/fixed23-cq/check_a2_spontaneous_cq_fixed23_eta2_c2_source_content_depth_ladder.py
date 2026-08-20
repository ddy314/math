#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-source-content-depth-ladder.md."""

from fractions import Fraction
import sympy as sp

p = 23


def source_interval(lam):
    lo = Fraction(837, 3174000) * Fraction(5, 4) ** lam
    hi = Fraction(843, 3174000) * Fraction(5, 4) ** lam
    lo_i = lo.numerator // lo.denominator + 1
    hi_i = hi.numerator // hi.denominator
    if hi.denominator == 1:
        hi_i -= 1
    return lo_i, hi_i


def allowed_source(n):
    if n <= 0 or n % 2 == 0 or n % 5 == 0:
        return False
    return all(r % 4 == 1 for r in sp.factorint(n))


def eval_system(lam, K, rho, cu, orient, exponent):
    mod = p ** exponent
    N = pow(10, 2 * lam, mod)
    T = pow(10, lam + 1, mod)
    chi = (
        3
        * pow(2, 2 * lam + 1, mod)
        * pow(pow(5, lam, mod), -1, mod)
    ) % mod
    q2 = (chi * rho * cu) % mod
    Q = (p * p * q2) % mod
    B = (Q - 2 * N) % mod
    A = ((K - 9 * N) * pow(10, -1, mod)) % mod

    D = (8181 * N * N - K * K + 2025 * Q * (Q - 4 * N)) % mod
    AK = (K * K - 18 * K + 55) % mod

    if orient == "-":
        G = (rho * AK - 2 * K * (2 * K - 9)) % mod
        H = (
            15 * B * B * rho * rho
            - 2 * B * K * T * T * q2
            - 2 * p * p * A * T * T * q2 * q2
        ) % mod
    else:
        G = (rho * AK + 2 * (3 * K * K - 27 * K + 55)) % mod
        H = (
            15 * B * B * rho * rho * (rho + 2)
            - 2 * B * rho * K * T * T * q2
            - 2 * p * p * A * T * T * q2 * q2 * (rho + 2)
        ) % mod

    return D, G, H


def branch_residues(lam, orient):
    # Prefix second layer uniquely fixes kappa.
    kappas = []
    for kappa in range(p):
        K = 16 + p * kappa
        D, _, _ = eval_system(lam, K, 1, 1, orient, 2)
        if D % p**2 == 0:
            kappas.append(kappa)
    assert len(kappas) == 1
    kappa = kappas[0]

    if kappa in (11, 18):
        return kappa, None

    K = 16 + p * kappa

    # Additive second layer uniquely fixes rho mod p.
    rho0s = []
    for rho0 in range(1, p):
        _, G, _ = eval_system(lam, K, rho0, 1, orient, 2)
        if G % p**2 == 0:
            rho0s.append(rho0)
    assert len(rho0s) == 1
    rho0 = rho0s[0]

    # Global high-2/source equation uniquely fixes c_u mod p.
    c1s = []
    for c0 in range(1, p):
        _, _, H = eval_system(lam, K, rho0, c0, orient, 1)
        if H % p == 0:
            c1s.append(c0)
    assert len(c1s) == 1
    C1 = c1s[0]

    # Lift K to p^3 from the prefix equation.
    K2s = []
    for digit in range(p):
        K2 = K + p**2 * digit
        D, _, _ = eval_system(lam, K2, rho0, C1, orient, 3)
        if D % p**3 == 0:
            K2s.append(K2)
    assert len(K2s) == 1
    K2 = K2s[0]

    # Lift rho to p^2 from the additive equation.
    rho2s = []
    for digit in range(p):
        rho2 = rho0 + p * digit
        _, G, _ = eval_system(lam, K2, rho2, C1, orient, 3)
        if G % p**3 == 0:
            rho2s.append(rho2)
    assert len(rho2s) == 1
    rho2 = rho2s[0]

    # Lift source content to p^2 from high-2.
    C2s = []
    for digit in range(p):
        C2 = C1 + p * digit
        _, _, H = eval_system(lam, K2, rho2, C2, orient, 2)
        if H % p**2 == 0:
            C2s.append(C2)
    assert len(C2s) == 1
    C2 = C2s[0]

    # One more triangular lift reaches the full c=2 square cap.
    K3s = []
    for digit in range(p):
        K3 = K2 + p**3 * digit
        D, _, _ = eval_system(lam, K3, rho2, C2, orient, 4)
        if D % p**4 == 0:
            K3s.append(K3)
    assert len(K3s) == 1
    K3 = K3s[0]

    rho3s = []
    for digit in range(p):
        rho3 = rho2 + p**2 * digit
        _, G, _ = eval_system(lam, K3, rho3, C2, orient, 4)
        if G % p**4 == 0:
            rho3s.append(rho3)
    assert len(rho3s) == 1
    rho3 = rho3s[0]

    C3s = []
    for digit in range(p):
        C3 = C2 + p**2 * digit
        _, _, H = eval_system(lam, K3, rho3, C3, orient, 3)
        if H % p**3 == 0:
            C3s.append(C3)
    assert len(C3s) == 1

    return kappa, (C1, C2, C3s[0])


expected = {
    52: (2, (11, 425, 8360), (12, 288, 11926)),
    63: (15, (15, 84, 2200), (8, 192, 1779)),
    74: (5, (22, 367, 3012), (1, 300, 7706)),
    85: (18, None, None),
    96: (8, (12, 518, 3163), (11, 471, 5232)),
    107: (21, (20, 411, 5701), (3, 486, 4189)),
    118: (11, None, None),
    129: (1, (13, 335, 7741), (10, 148, 11257)),
}

for lam, (kappa, minus_expected, plus_expected) in expected.items():
    km, minus = branch_residues(lam, "-")
    kp, plus = branch_residues(lam, "+")
    assert km == kp == kappa
    assert minus == minus_expected
    assert plus == plus_expected

# Source-window low levels.
assert source_interval(52) == (29, 29)
assert source_interval(63) == (337, 338)
assert source_interval(74) == (3913, 3940)

# lambda=96: depth >=3 leaves one valid source content, minus orientation only.
lo96, hi96 = source_interval(96)
minus96 = [n for n in range(lo96, hi96 + 1) if n % 529 == 518]
plus96 = [n for n in range(lo96, hi96 + 1) if n % 529 == 471]
assert minus96 == [530576, 531105, 531634, 532163, 532692, 533221, 533750]
assert plus96 == [530529, 531058, 531587, 532116, 532645, 533174, 533703]
assert [n for n in minus96 if allowed_source(n)] == [533221]
assert [n for n in plus96 if allowed_source(n)] == []
assert sp.factorint(533221) == {13: 1, 41017: 1}

# lambda=96 has no depth-4 representative at either orientation.
assert not [n for n in range(lo96, hi96 + 1) if n % 12167 in (3163, 5232)]

# lambda=107: every depth-4 residue representative violates source support.
lo107, hi107 = source_interval(107)
minus107 = [n for n in range(lo107, hi107 + 1) if n % 12167 == 5701]
plus107 = [n for n in range(lo107, hi107 + 1) if n % 12167 == 4189]
assert minus107 == [6174370, 6186537, 6198704, 6210871]
assert plus107 == [6185025, 6197192, 6209359]
assert not any(allowed_source(n) for n in minus107 + plus107)
assert sp.factorint(6210871) == {59: 1, 105269: 1}
assert sp.factorint(6209359) == {13: 1, 67: 1, 7129: 1}

# lambda=129 shows the source-content filter has reached its natural boundary.
lo129, hi129 = source_interval(129)
minus_witness = 836610661
plus_witness = 836760181
assert lo129 <= minus_witness <= hi129 and minus_witness % 12167 == 7741
assert lo129 <= plus_witness <= hi129 and plus_witness % 12167 == 11257
assert sp.factorint(minus_witness) == {617: 1, 1355933: 1}
assert sp.isprime(617) and sp.isprime(1355933)
assert sp.isprime(plus_witness)
assert allowed_source(minus_witness) and allowed_source(plus_witness)

print(
    "OK: A2 fixed-23 eta=2 c=2 source-content branch is unique through the square cap; "
    "depth>=2 requires lambda>=63, depth>=3 requires lambda>=96, depth=4 requires lambda>=129"
)
