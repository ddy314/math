"""Exact arithmetic check; scope and commands: CHECKS.md.

Original source: SRC-0504; see history/sources.json.
"""

from itertools import product

import sympy as sp


def main() -> None:
    d, t1, t2, t3, y1, y2, y3, h = sp.symbols("D t1 t2 t3 y1 y2 y3 H")
    tail_sum = h + y3
    delta = t1**2 + t2**2 + t3**2 - d**2
    norm = ((d + t3) * y1 - t1 * tail_sum) ** 2 + (
        (d + t3) * y2 - t2 * tail_sum
    ) ** 2
    residual = -(d + t3) ** 2 * (h**2 - y1**2 - y2**2 - y3**2) + (
        2 * (d + t3) * tail_sum * (d * h - t1 * y1 - t2 * y2 - t3 * y3)
    )
    assert sp.expand(norm - delta * tail_sum**2 - residual) == 0
    sphere = [
        (xyz, h)
        for xyz in product(range(9), repeat=3)
        for h in range(9)
        if (sum(x * x for x in xyz) - h * h) % 9 == 0
        and any(x % 3 for x in (*xyz, h))
    ]
    units = (1, 2, 4, 5, 7, 8)
    classes = excluded = admitted = 0
    for coeff in product(units, repeat=3):
        if len({c % 3 for c in coeff}) != 1:
            continue
        count = sum(
            (sum(c * x for c, x in zip(coeff, xyz)) - h * sum(coeff)) % 9
            == 0
            for xyz, h in sphere
        )
        norm_zero = sum(c * c for c in coeff) % 9 == 0
        # Admitted residue classes are only local points, not exact lifts.
        assert bool(count) == norm_zero, (coeff, count, norm_zero)
        sign = 1 if coeff[0] % 3 == 1 else -1
        assert norm_zero == ((sum(coeff) - 6 * sign) % 9 == 0)
        if len(set(coeff)) == 1:
            assert count == 0
        classes += 1
        excluded += not norm_zero
        admitted += norm_zero
    assert (len(sphere), classes, excluded, admitted) == (540, 54, 36, 18)
    general_classes = general_excluded = general_admitted = 0
    for coeff in product(range(9), repeat=3):
        if not any(c % 3 for c in coeff):
            continue
        pair_sum = sum(coeff[i] * coeff[j] for i, j in ((0, 1), (0, 2), (1, 2)))
        obstructed = pair_sum % 9 in (3, 6)
        local_point = any(
            (sum(c * x for c, x in zip(coeff, xyz)) - h * sum(coeff)) % 9 == 0
            for xyz, h in sphere
        )
        assert local_point == (not obstructed), (coeff, pair_sum, local_point)
        general_classes += 1
        general_excluded += obstructed
        general_admitted += local_point
    assert (general_classes, general_excluded, general_admitted) == (702, 144, 558)
    print(f"Primitive sphere residues mod 9: {len(sphere)}")
    print(f"Common-sign denominator classes: {classes}; excluded: {excluded}")
    print(f"Locally admitted: {admitted}; no assertion of exact-lift existence")
    print(f"General normalized classes: {general_classes}; excluded: {general_excluded}")
    print(f"General locally admitted: {general_admitted}; no existence assertion")
    print("PASS: denominator norm identity and mod-9 certificates")


if __name__ == "__main__":
    main()
