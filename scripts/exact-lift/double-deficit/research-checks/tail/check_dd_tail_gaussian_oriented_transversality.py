#!/usr/bin/env python3
"""Finite algebra/valuation audit for dd-gaussian-oriented-transversality-2026-08-21.md.

This is only a mechanical sanity check.  The unbounded coverage is supplied by the
proof document; this script does not replace the proof.
"""

from __future__ import annotations


def check_exact_algebra() -> None:
    # Small positive integer boxes are enough to audit the displayed polynomial identities.
    for aa in range(1, 8):
        for bb in range(1, 8):
            for B1 in range(1, 7):
                for B2 in range(1, 7):
                    for q2 in (1, 10, 100):
                        for r2 in (1, 10, 100, 1000):
                            A = aa * r2 + bb
                            # Z_num = (-aa*q2) + i*bb, represented by a pair.
                            zr, zi = -aa * q2, bb
                            # Z_ang = aa*B2 + i*bb*B1.
                            wr, wi = aa * B2, bb * B1
                            CQ = B1 * q2 + B2

                            # A + i Z_num = aa (r2 - i q2).
                            # i*(zr+i zi)=(-zi)+i*zr.
                            assert (A - zi, zr) == (aa * r2, -aa * q2)

                            # q2*A + r2*Z_num = bb(q2+i r2).
                            assert (q2 * A + r2 * zr, r2 * zi) == (
                                bb * q2,
                                bb * r2,
                            )

                            # B1*A + i Z_ang = aa(B1*r2+i B2).
                            assert (B1 * A - wi, wr) == (
                                aa * B1 * r2,
                                aa * B2,
                            )

                            # Z_ang - B1*Z_num = aa*C_Q.
                            assert (wr - B1 * zr, wi - B1 * zi) == (
                                aa * CQ,
                                0,
                            )

                            # B1(r2-iq2)+iC_Q = B1*r2+iB2.
                            assert (B1 * r2, -B1 * q2 + CQ) == (B1 * r2, B2)

                            # D_bot = B2*A - bb*C_Q.
                            dbot = aa * B2 * r2 - bb * B1 * q2
                            assert dbot == B2 * A - bb * CQ


def check_valuation_ledger(bound: int = 8) -> tuple[int, int, int]:
    """Enumerate abstract local valuations satisfying all pre-lock hypotheses.

    The gap quadratic is imposed only through the necessary ultrametric condition
    that its minimum term valuation occurs at least twice.  We then verify the
    exact lock alpha=t+(E-j)_+ and source ledger c=e+2t+g+E+j.

    For j>E non-third states we additionally impose the independent sphere
    two-sheet necessary condition.  None survive.
    """

    nonthird = 0
    third_to_gaussian = 0
    third_max_sphere_survivors = 0

    for E in range(bound + 1):
        for j in range(bound + 1):
            delta = max(E - j, 0)
            r = max(j - E, 0)
            for t in range(bound + 1):
                for g in range(t + 1):
                    for alpha in range(bound + 1):
                        for omega in range(1, 2 * bound + 2):
                            for c in range(1, 3 * bound + 4):
                                x = max(c - j - min(E, j), 0)
                                if x <= 0:
                                    continue
                                if x > max(t, 2 * g + omega, r):
                                    continue

                                Rstar = max(r - t - alpha, 0)
                                z = max(x - t - alpha, 0)

                                # Non-third final Gaussian residual.
                                if Rstar == 0 and z > g:
                                    e = z - g
                                    M = max(E, j)
                                    n0 = 2 * g + omega
                                    vals = (
                                        j + 2 * alpha,
                                        M + t + alpha,
                                        c - E + 2 * M + n0,
                                    )
                                    if vals.count(min(vals)) < 2:
                                        continue

                                    nonthird += 1
                                    assert alpha == t + delta
                                    assert e == x - 2 * t - delta - g
                                    assert c == e + 2 * t + g + E + j
                                    assert c >= e + (t - g)
                                    assert c > t - g

                                    if j > E:
                                        # Here H and y3 are p-units, so the gap
                                        # depth must be 0 or the full complementary
                                        # sphere depth 2(r+g)+omega.
                                        if alpha in (0, 2 * (r + g) + omega):
                                            third_max_sphere_survivors += 1

                                # Prior theorem's third -> Gaussian sheet.
                                if (
                                    Rstar > 0
                                    and t == 0
                                    and g == 0
                                    and alpha == 0
                                    and x > r
                                    and x <= omega
                                ):
                                    e = x
                                    third_to_gaussian += 1
                                    assert delta == 0
                                    assert c == e + E + j
                                    assert c == e + 2 * t + g + E + j

    return nonthird, third_to_gaussian, third_max_sphere_survivors


def main() -> None:
    check_exact_algebra()
    counts = check_valuation_ledger(8)
    expected = (94281, 3632, 0)
    assert counts == expected, (counts, expected)
    print("algebra identities: OK")
    print(f"non-third admissible valuation states: {counts[0]}")
    print(f"third->Gaussian prior-sheet states: {counts[1]}")
    print(f"j>E non-third states surviving sphere two-sheet: {counts[2]}")
    print("Gaussian gap lock/source ledger: OK")


if __name__ == "__main__":
    main()
