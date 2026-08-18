#!/usr/bin/env python3
"""Exact arithmetic checks for decimal-discriminant.md."""


def check_square_rescaling_and_identities() -> None:
    for M in range(2, 6):
        for m in range(3, 7):
            for d in range(1, m):
                lam = m - d
                for c_q in (1, 3, 7):
                    for q in (1, 3, 11):
                        for u in (1, 5, 13):
                            T = 10**m
                            z = q * 5**lam
                            b3 = 2 ** (M + m + 1) * 5**d * c_q * u
                            Q = 2 ** (M + 1) * c_q * q
                            B3 = b3 // u
                            assert B3 * z == T * Q

                            for K in range(2, 50, 4):
                                F = 5 * K * K - 36 * K + 55
                                A_w = 5 * u * u + z * z
                                B_w = u * u * F + z * z * K * K
                                D_w = 55 * z * z - 49 * u * u

                                A = 5 * b3 * b3 + T * T * Q * Q
                                B = b3 * b3 * F + T * T * Q * Q * K * K
                                D = 55 * T * T * Q * Q - 49 * b3 * b3
                                L = A * K - 18 * b3 * b3

                                assert A == B3 * B3 * A_w
                                assert B == B3 * B3 * B_w
                                assert D == B3 * B3 * D_w
                                assert A * B == L * L + b3 * b3 * D
                                assert 55 * A - D == (18 * b3) ** 2
                                assert 55 * B - K * K * D == b3 * b3 * (18 * K - 55) ** 2


def check_discriminant() -> None:
    for b3 in range(2, 30):
        for T in range(b3 + 1, b3 + 20):
            for Q in range(2, 10):
                A = 5 * b3 * b3 + T * T * Q * Q
                D = 55 * T * T * Q * Q - 49 * b3 * b3
                disc = (-36 * b3 * b3) ** 2 - 4 * A * (55 * b3 * b3)
                assert D > 0
                assert disc == -4 * b3 * b3 * D


def check_linear_prefix_rewrite() -> None:
    for P in range(-100, 101):
        K = 10 * P
        assert 18 * K - 55 == 5 * (36 * P - 11)


def main() -> None:
    check_square_rescaling_and_identities()
    check_discriminant()
    check_linear_prefix_rewrite()
    print("A2 decimal-discriminant certificate: OK")


if __name__ == "__main__":
    main()
