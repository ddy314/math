#!/usr/bin/env python3
"""Finite valuation audit for dd-gaussian-deep-core-2026-08-21.md.

The script checks the canonical square/deep split on an abstract valuation box.
It is a sanity certificate only; the proof document supplies the unbounded argument.
"""

from __future__ import annotations


def enumerate_states(bound: int = 8) -> tuple[int, int, int, int, int, int]:
    nonthird = 0
    third_to_gaussian = 0
    square = 0
    deep = 0
    deep_prefix = 0
    deep_third = 0

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
                                if x <= 0 or x > max(t, 2 * g + omega, r):
                                    continue

                                Rstar = max(r - t - alpha, 0)
                                z = max(x - t - alpha, 0)

                                # Non-third Gaussian residual.  Impose the gap
                                # quadratic minimum-twice condition, then the
                                # proved j>E sphere exclusion.
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
                                    if j > E:
                                        continue

                                    nonthird += 1
                                    assert alpha == t + delta
                                    assert c == e + 2 * t + g + E + j
                                    y = c - e
                                    assert y == 2 * t + g + E + j

                                    if 2 * e <= c:
                                        square += 1
                                        assert 2 * e <= c
                                    else:
                                        deep += 1
                                        deep_prefix += 1
                                        assert e > y
                                        assert e > 2 * t + g + E + j
                                        assert t - g < e / 2
                                        assert alpha < e
                                        assert E + t < e

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
                                    assert j > E
                                    assert delta == 0
                                    assert c == e + E + j
                                    y = c - e
                                    assert y == E + j

                                    if 2 * e <= c:
                                        square += 1
                                    else:
                                        deep += 1
                                        deep_third += 1
                                        assert e > E + j

    return (
        nonthird,
        third_to_gaussian,
        square,
        deep,
        deep_prefix,
        deep_third,
    )


def main() -> None:
    counts = enumerate_states(8)
    expected = (46908, 3632, 45451, 5089, 3289, 1800)
    assert counts == expected, (counts, expected)

    labels = (
        "non-third final Gaussian states",
        "third->Gaussian states",
        "source-square states",
        "deep states",
        "deep prefix-max/equal states",
        "deep third-max states",
    )
    for label, value in zip(labels, counts):
        print(f"{label}: {value}")
    print("Gaussian source-square/deep-core ledger: OK")


if __name__ == "__main__":
    main()
