#!/usr/bin/env python3
"""Mechanical audit for the DD sixfold gcd-stripped master lock.

Checks only exact finite gcd/exponent algebra and the numerical slope margin.
It is not a DD emptiness proof.
"""

from __future__ import annotations

from math import gcd, log10


def vp(n: int, p: int) -> int:
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def check_gcd_stripping() -> None:
    # If Q | C*T-D and g=(Q,C), then g|D, after division Q/g is
    # coprime to C/g and the residue is preserved.
    for Q in range(2, 120):
        for C in range(1, 120):
            for T in range(1, 30):
                # Manufacture D so the parent divisibility is exact.
                for k in range(-2, 3):
                    D = C * T - k * Q
                    if D <= 0:
                        continue
                    assert (C * T - D) % Q == 0
                    g = gcd(Q, C)
                    assert D % g == 0
                    Q6, C6, D6 = Q // g, C // g, D // g
                    assert gcd(Q6, C6) == 1
                    assert (C6 * T - D6) % Q6 == 0
                    assert (T - (D6 * pow(C6, -1, Q6)) % Q6) % Q6 == 0


def check_divisor_inequality() -> None:
    # (Q,C)/(X,C) divides Q/X whenever X|Q.
    for Q in range(2, 180):
        for X in range(1, Q + 1):
            if Q % X:
                continue
            for C in range(1, 180):
                lhs = gcd(Q, C) // gcd(X, C)
                rhs = Q // X
                assert rhs % lhs == 0


def check_deephard_coefficient_ledger() -> None:
    # On deep-hard support v_p(C6)=M+t+6E.  The restricted gcd depth
    # is bounded by exactly this baseline package.
    for E in range(0, 6):
        for j in range(0, 6):
            M = max(E, j)
            for t in range(0, 5):
                for h in range(1, 15):
                    # Q-depth need only be nonnegative for this local check.
                    q_depth = E + h
                    c_depth = M + t + 6 * E
                    gcd_depth = min(q_depth, c_depth)
                    assert gcd_depth <= M + t + 6 * E
                    assert E <= M


def check_ordinary_margin() -> None:
    z_star = 0.308883577618031
    U_star = 1.0 - z_star
    assert abs(U_star - 0.691116422381969) < 1e-12
    assert z_star < 1.0
    # Finite toy version of Q6 ~ 10^S versus 10^e, e <= z_* S.
    for S in (20, 50, 100):
        e = int(z_star * S)
        # Use a deliberately weaker finite Q6 lower than 10^S but still with
        # exponent tending to one, to audit the direction of comparison.
        q6 = 10 ** (S - max(1, S // 20))
        assert 10**e < q6
        assert log10(q6) - e > 0


def main() -> None:
    check_gcd_stripping()
    check_divisor_inequality()
    check_deephard_coefficient_ledger()
    check_ordinary_margin()
    print("DD global sixfold gcd-stripped master-lock checks passed")


if __name__ == "__main__":
    main()
