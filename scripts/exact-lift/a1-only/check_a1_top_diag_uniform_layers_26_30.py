#!/usr/bin/env python3
"""Exact fixed-layer certificates for A1 minimal diagonal k=g=26..30.

This extends check_a1_top_diag_uniform_layers.py.  The third-block length ell
is absent: each layer is reduced to the theorem-derived finite (h,x,y) box,
and every exact rational decade state is checked against the older, wider
near-integer window [5.09,50.45]*10^-k.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import runpy


BASE = runpy.run_path(str(Path(__file__).with_name("check_a1_top_diag_uniform_layers.py")))

odd_prime_supply = BASE["odd_prime_supply"]
valuation_floors = BASE["valuation_floors"]
derive_box = BASE["derive_box"]
first_y_ge_target = BASE["first_y_ge_target"]
rho_num_den = BASE["rho_num_den"]


# k: (H counts, x_floor, y_floor, box, decade_states)
EXPECTED = {
    26: ((128, 24, 32, 256), -28, -66, (-329, 239, -126, 49), 146580),
    27: ((12288, 160, 32, 512), -29, -67, (-339, 245, -130, 51), 4238867),
    28: ((256, 768, 16, 64), -30, -70, (-330, 255, -126, 52), 390688),
    29: ((64, 96, 128, 256), -31, -72, (-343, 263, -131, 54), 196277),
    30: ((32768, 128, 64, 64), -32, -75, (-378, 273, -145, 56), 11672944),
}


def certify_layer(k: int) -> None:
    expected_h, expected_xf, expected_yf, expected_box, expected_states = EXPECTED[k]

    hs_by_w = {w: odd_prime_supply(k, w) for w in (1, 2, 3, 4)}
    h_counts = tuple(len(hs_by_w[w]) for w in (1, 2, 3, 4))
    assert h_counts == expected_h, (k, h_counts, expected_h)

    x_floor, y_floor = valuation_floors(k)
    assert (x_floor, y_floor) == (expected_xf, expected_yf)

    hmax = max(max(hs) for hs in hs_by_w.values())
    box = derive_box(k, hmax, x_floor, y_floor)
    assert box == expected_box, (k, box, expected_box)

    x_lo, x_hi, y_lo, y_hi = box
    low_decade = 10 ** (k - 1)
    high_decade = 10**k
    low_gap = Fraction(509, 100 * 10**k)
    high_gap = Fraction(5045, 100 * 10**k)

    decade_states = 0
    near_hits = 0

    for w, hs in hs_by_w.items():
        for h in hs:
            for x in range(x_lo, x_hi + 1):
                first = first_y_ge_target(h, x, low_decade, y_lo, y_hi)
                stop = first_y_ge_target(h, x, high_decade, y_lo, y_hi)

                for y in range(first, stop):
                    if y > y_hi:
                        break

                    if x > k and y < y_floor:
                        continue
                    if y > k and x < x_floor:
                        continue

                    num, den = rho_num_den(h, x, y)
                    rho = Fraction(num, den)
                    assert low_decade <= rho < high_decade

                    decade_states += 1
                    N0 = (num + den - 1) // den
                    gap = Fraction(N0) - rho
                    if low_gap < gap < high_gap:
                        near_hits += 1
                        print(
                            "NEAR HIT "
                            f"k={k} w={w} h={h} x={x} y={y} "
                            f"N0={N0} gap={gap}"
                        )

    assert decade_states == expected_states, (k, decade_states, expected_states)
    assert near_hits == 0, (k, near_hits)

    print(
        f"k={k} h_counts={h_counts} floors=({x_floor},{y_floor}) "
        f"box={box} decade_states={decade_states} wide_gap_hits=0"
    )


def main() -> None:
    for k in range(26, 31):
        certify_layer(k)
    print("CERTIFICATE OK: A1 minimal diagonal k=g=26..30 is empty.")


if __name__ == "__main__":
    main()
