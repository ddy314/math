#!/usr/bin/env python3
"""Finite valuation certificate for good-excess-gcd-ladder.md."""


def vp_gcd(a: int, b: int) -> int:
    return min(a, b)


for h in range(1, 9):
    for n in range(9):
        for eps in range(9):
            c = max(h - n, 0)

            # First layer = G_exc depth.
            x = min(c, eps)
            assert vp_gcd(c, eps) == x

            # Ladder and successive quotients.
            prev = None
            for k in range(1, 9):
                dk = min(k * c, eps)
                if prev is not None:
                    ek = dk - prev
                    assert ek >= 0
                    assert ek == min(k * c, eps) - min((k - 1) * c, eps)
                prev = dk

            # Stable value on C_N support.
            stable = eps if c > 0 else 0
            if c == 0:
                assert all(min(k * c, eps) == 0 for k in range(1, 9))
            else:
                k_big = eps // c + 2
                assert min(k_big * c, eps) == stable

            # Deficit / overflow split after first layer.
            c_rem = c - x
            over = stable - x
            assert c_rem == max(c - eps, 0)
            assert over == max(eps - c, 0) if c > 0 else over == 0
            assert min(c_rem, over) == 0

print("OK: DD Good excess gcd ladder certified")
