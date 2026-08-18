#!/usr/bin/env python3
"""Exact arithmetic checks for source-discriminant.md.

This verifies polynomial identities, fixed congruence classes and valuation
claims used in the A2 source-discriminant reduction. It is a certificate for
local algebra only, not a global A2 solver.
"""


def v_p(n: int, p: int) -> int:
    n = abs(n)
    if n == 0:
        return 10**9
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def check_denominator_identity() -> None:
    for M in range(2, 7):
        for m in range(3, 8):
            for d in range(1, m):
                lam = m - d
                for c_q in (1, 3, 7):
                    for q in (1, 3, 11):
                        for u in (1, 5, 13):
                            b3 = 2 ** (M + m + 1) * 5**d * c_q * u
                            Q = 2 ** (M + 1) * c_q * q
                            T = 10**m
                            z = q * 5**lam
                            assert b3 * z == T * u * Q


def check_discriminant_parity() -> None:
    for u in range(1, 50, 2):
        for z in range(u + 2, u + 100, 2):
            D = 55 * z * z - 49 * u * u
            assert D > 0
            assert D % 8 == 6
            assert (D // 2) % 4 == 3


def check_b_parity_and_identities() -> None:
    for u in range(1, 30, 2):
        for z in range(1, 30, 2):
            for K in range(2, 100, 4):
                F = 5 * K * K - 36 * K + 55
                B = u * u * F + z * z * K * K
                A = 5 * u * u + z * z
                D = 55 * z * z - 49 * u * u
                L = A * K - 18 * u * u
                assert F % 8 == 3
                assert B % 8 == 7
                assert A * B == L * L + u * u * D
                assert 55 * B - K * K * D == u * u * (18 * K - 55) ** 2
                assert 55 * A - D == (18 * u) ** 2


def check_fixed_overlap_depths() -> None:
    # q-overlap at 7 has exact D_W depth 2.
    for e in range(1, 5):
        for u in range(1, 35):
            if u % 7 == 0:
                continue
            for z0 in range(1, 25):
                if z0 % 7 == 0:
                    continue
                z = 7**e * z0
                D = 55 * z * z - 49 * u * u
                assert v_p(D, 7) == 2

    # c_u-overlap at 11 has exact D_W depth 1.
    for e in range(1, 5):
        for u0 in range(1, 25):
            if u0 % 11 == 0:
                continue
            u = 11**e * u0
            for z in range(1, 30):
                if z % 11 == 0:
                    continue
                D = 55 * z * z - 49 * u * u
                assert v_p(D, 11) == 1


def check_special_23_identity() -> None:
    for K in range(-150, 151):
        assert 25 * (K * K - 26) == (5 * K - 11) * (5 * K + 11) - 23**2
    assert 11 * 11 - 26 * 5 * 5 == -(23**2)


def check_double_root_linearization() -> None:
    primes = (7, 19, 23, 31, 43, 47, 59, 67, 71, 79)
    for p in primes:
        if p in (3, 5, 11):
            continue
        for u in range(1, p):
            for z in range(1, p):
                D = (55 * z * z - 49 * u * u) % p
                if D != 0:
                    continue
                for K in range(p):
                    F = 5 * K * K - 36 * K + 55
                    B = (u * u * F + z * z * K * K) % p
                    if B == 0:
                        assert (18 * K - 55) % p == 0


def main() -> None:
    check_denominator_identity()
    check_discriminant_parity()
    check_b_parity_and_identities()
    check_fixed_overlap_depths()
    check_special_23_identity()
    check_double_root_linearization()
    print("A2 source-discriminant certificate: OK")


if __name__ == "__main__":
    main()
