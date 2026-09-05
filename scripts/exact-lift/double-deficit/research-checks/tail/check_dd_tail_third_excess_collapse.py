#!/usr/bin/env python3
"""Finite sanity audit for dd-third-excess-collapse-2026-08-21.md.

This script is NOT the proof.  It exhausts a bounded box of the local valuation
ledger and verifies that the hypotheses used in the handwritten proof force the
claimed unit-triple and third/Gaussian dichotomy.

The unbounded argument is in the markdown proof; this checker only guards
against algebra/sign mistakes in the case split.
"""

from __future__ import annotations

from dataclasses import dataclass


BOUND = 14


@dataclass(frozen=True)
class State:
    E: int
    j: int
    c: int
    t: int
    g: int
    omega: int
    alpha: int
    x: int
    r: int


def vdiff_possible(v_a: int, v_b: int, v_rhs: int) -> bool:
    """Necessary valuation condition for A-B=R.

    If v(A) != v(B), ultrametricity fixes v(A-B)=min(v(A),v(B)).
    If the two depths agree, cancellation may only increase the depth.
    """

    if v_a != v_b:
        return v_rhs == min(v_a, v_b)
    return v_rhs >= v_a


def states():
    for E in range(BOUND + 1):
        for j in range(BOUND + 1):
            r = max(j - E, 0)
            for c in range(BOUND + 1):
                x = max(c - j - min(E, j), 0)
                if x == 0:
                    continue
                for t in range(BOUND + 1):
                    for g in range(t + 1):  # existing Common-paid: g <= t
                        for omega in range(BOUND + 1):
                            # Sphere two-sheet values when r>0.
                            sphere_depths = {0, 2 * (r + g) + omega}
                            for alpha in sphere_depths:
                                z = max(x - t - alpha, 0)
                                R_star = max(r - t - alpha, 0)
                                z3 = min(z, R_star)
                                if z3 == 0:
                                    continue

                                # General-transfer refinement.
                                if x > max(t, 2 * g + omega, r):
                                    continue

                                # r>0 follows from z3>0, hence j>E and H is a p-unit.
                                assert r > 0 and j > E

                                # Exact DD coefficient plane M-QH=tau*a:
                                # v(M)=j+t, v(QH)=E+c, v(tau*a)=j+alpha.
                                if not vdiff_possible(j + t, E + c, j + alpha):
                                    continue

                                yield State(E, j, c, t, g, omega, alpha, x, r)


def main() -> None:
    total = 0
    third_dominant = 0
    gaussian_dominant = 0

    for s in states():
        total += 1

        # The two exact identities should force the unit triple.
        assert s.alpha == 0, s
        assert s.t == 0, s
        assert s.g == 0, s

        # Source formula in the j>E sheet.
        assert s.x == s.c - s.j - s.E, s
        assert s.c == s.x + 2 * s.E + s.r, s

        # General transfer is now a pure third/Gaussian dichotomy.
        assert s.x <= max(s.r, s.omega), s

        if s.x <= s.r:
            third_dominant += 1
            # p^(2x) | C_Q is the local square-source charge.
            assert 2 * s.x <= s.c, s
        else:
            gaussian_dominant += 1
            # Orientation transfer has v_p(N_num) >= min(c,omega).
            assert s.x <= s.omega, s
            assert s.x <= min(s.c, s.omega), s

    assert total > 0
    assert third_dominant > 0
    assert gaussian_dominant > 0

    print("DD third-excess finite valuation audit: PASS")
    print(f"bound={BOUND}")
    print(f"admissible third-excess states={total}")
    print(f"third-dominant states={third_dominant}")
    print(f"Gaussian-dominant states={gaussian_dominant}")


if __name__ == "__main__":
    main()
