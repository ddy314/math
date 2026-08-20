#!/usr/bin/env python3
"""Mechanical checks for genuine-tail-root-orientation-lock.md.

This script certifies only finite symbolic / valuation bookkeeping used in the
proof note.  It is not an emptiness proof for DD.
"""

from __future__ import annotations

import sympy as sp


def symbolic_tail_discriminant() -> None:
    k, G, L, Q, C, N, tau, W = sp.symbols(
        "k G L Q C N tau W", nonzero=True
    )

    A = -k * (k + 2 * G)
    B = 2 * G**2 * L * C
    C3 = G**2 * L**2 * C**2 - N * (L * Q + tau) ** 2
    disc = sp.expand(B**2 - 4 * A * C3)

    W2 = k**2 * G**2 * C**2 - k * Q**2 * N * (k + 2 * G)
    tau_sub = L * Q * G / k

    target = (2 * L * (k + G) * W / k) ** 2
    err = sp.expand(disc.subs(tau, tau_sub) - target)
    err = sp.factor(err.subs(W**2, W2))
    assert err == 0


def symbolic_root_linearization() -> None:
    k, G, L, Q, C, N, tau, W, eta = sp.symbols(
        "k G L Q C N tau W eta", nonzero=True
    )

    A = -k * (k + 2 * G)
    B = 2 * G**2 * L * C
    C3 = G**2 * L**2 * C**2 - N * (L * Q + tau) ** 2
    W2 = k**2 * G**2 * C**2 - k * Q**2 * N * (k + 2 * G)

    z = L * (k * G**2 * C + eta * (k + G) * W) / (
        k**2 * (k + 2 * G)
    )
    poly = sp.expand(A * z**2 + B * z + C3)
    poly = poly.subs(tau, L * Q * G / k)
    poly = sp.expand(poly).subs(eta**2, 1)
    poly = sp.factor(poly.subs(W**2, W2))
    assert poly == 0


def finite_orientation_ledger() -> None:
    # Abstract the last step: A and B are p-units.  Sphere gives
    # p^(2h) | A^2+B^2; a hypothetical hyperbolic relative sign would give
    # p^h | A^2-B^2.  Enumerate small odd p/h and unit residues and verify
    # that the pair of congruences is impossible.
    for p in (3, 5, 7, 11, 13, 17, 19):
        for h in range(1, 4):
            mod_h = p**h
            mod_2h = p ** (2 * h)
            for a in range(1, min(mod_2h, 200)):
                if a % p == 0:
                    continue
                for b in range(1, min(mod_2h, 200)):
                    if b % p == 0:
                        continue
                    sphere = (a * a + b * b) % mod_2h == 0
                    hyp = (a * a - b * b) % mod_h == 0
                    assert not (sphere and hyp)


def main() -> None:
    symbolic_tail_discriminant()
    symbolic_root_linearization()
    finite_orientation_ledger()
    print("DD genuine tail-root orientation-lock checks passed")


if __name__ == "__main__":
    main()
