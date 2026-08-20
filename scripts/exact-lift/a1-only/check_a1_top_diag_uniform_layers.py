#!/usr/bin/env python3
"""Generic exact fixed-k certificate for the A1 minimal diagonal.

The certificate removes the third-block digit length ell entirely.  For every
k in 6..23 it:
  1. constructs the complete odd-prime h supply;
  2. computes exact max v2(N), v5(N) by p-adic root lifting over the whole
     integer-center interval (without scanning all N0);
  3. derives a safe finite (x,y) box from cross-corridor + the rho decade;
  4. checks the exact one-sided near-integer gap for every decade state.

Every reported gap-hit count is zero.

See:
  docs/proofs/exact-lift/branches/a1-only/uniform-layer-finite-box.md
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))
LAYERS = tuple(range(6, 24))

# k: ((|H_1|,|H_2|,|H_3|,|H_4|), x*_floor, y*_floor,
#     (xmin,xmax,ymin,ymax), decade_states)
EXPECTED = {
    6:  ((64, 32, 2, 8),       -8,  -15, (-77, 54, -29, 12),   8679),
    7:  ((128, 12, 128, 32),    -9,  -19, (-81, 67, -31, 13),   27644),
    8:  ((128, 24, 16, 256),    -10, -22, (-111, 77, -43, 15),  46489),
    9:  ((16, 192, 32, 8),      -11, -23, (-112, 83, -43, 17),  29096),
    10: ((128, 24, 32, 24),     -12, -25, (-132, 91, -51, 19),  26685),
    11: ((32, 48, 48, 8),       -13, -28, (-122, 101, -46, 21), 18958),
    12: ((3072, 96, 4, 32),     -14, -32, (-157, 114, -60, 23), 497994),
    13: ((256, 192, 512, 16),   -15, -32, (-173, 117, -67, 25), 161213),
    14: ((256, 96, 128, 16),    -16, -36, (-178, 130, -68, 26), 86637),
    15: ((64, 128, 16, 32),     -17, -39, (-194, 140, -75, 28), 45800),
    16: ((32, 48, 128, 32),     -18, -41, (-209, 148, -81, 30), 50952),
    17: ((128, 24, 64, 256),    -19, -43, (-218, 156, -84, 32), 103730),
    18: ((4096, 20, 32, 128),   -20, -44, (-230, 161, -89, 34), 944083),
    19: ((1024, 384, 16, 8),    -21, -49, (-237, 176, -91, 36), 335288),
    20: ((32, 48, 64, 64),      -22, -50, (-255, 182, -98, 38), 54299),
    21: ((1024, 32, 256, 64),   -23, -54, (-247, 195, -94, 39), 366660),
    22: ((4096, 192, 32, 256),  -24, -55, (-280, 200, -108, 41), 1225045),
    23: ((128, 96, 128, 256),   -25, -58, (-292, 211, -112, 43), 177478),
}


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("vp(0,p) is not used")
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def ppow(p: int, e: int) -> Fraction:
    if e >= 0:
        return Fraction(p**e)
    return Fraction(1, p ** (-e))


def all_divisors(factors: dict[int, int]) -> list[int]:
    out = [1]
    for p, e in sorted(factors.items()):
        out = [d * p**j for d in out for j in range(e + 1)]
    return sorted(out)


def odd_prime_supply(k: int, w: int) -> list[int]:
    b1 = 10 ** (2 * k + 1) - w
    Q = 10 * b1 + 1

    q_divisors = all_divisors(sp.factorint(Q))
    blocks = [
        p**e
        for p, e in sp.factorint(b1).items()
        if p not in (2, 5) and p % 4 == 1
    ]

    selectors = [1]
    for block in blocks:
        selectors += [s * block for s in selectors]

    return sorted({q * s for q in q_divisors for s in selectors})


def prefix_AB(k: int, z: int, w: int) -> tuple[int, int]:
    """Return A,B such that N=(N0+A)^2+B^2."""
    A = (
        10 ** (3 * k + 2)
        + (5 - z - w) * 10 ** (k + 1)
        + 10**k
        - 1
    )
    b1 = 10 ** (2 * k + 1) - w
    a2 = 10 ** (2 * k + 1) - z
    B = a2 * b1
    return A, B


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def residue_intersects_interval(r: int, modulus: int, lo: int, hi: int) -> bool:
    first = r + ceil_div(lo - r, modulus) * modulus
    return first <= hi


def max_vp_by_root_lifting(k: int, z: int, w: int, p: int) -> int:
    """Exact max v_p(N) on 10^(k-1)<=N0<=10^k by congruence lifting."""
    A, B = prefix_AB(k, z, w)
    lo = 10 ** (k - 1)
    hi = 10**k

    residues = [0]
    modulus = 1
    depth = 0

    while True:
        new_modulus = modulus * p
        lifted: set[int] = set()

        for r in residues:
            for digit in range(p):
                rr = r + digit * modulus
                if ((rr + A) * (rr + A) + B * B) % new_modulus != 0:
                    continue
                if residue_intersects_interval(rr, new_modulus, lo, hi):
                    lifted.add(rr)

        if not lifted:
            return depth

        residues = sorted(lifted)
        modulus = new_modulus
        depth += 1


def valuation_floors(k: int) -> tuple[int, int]:
    x_floor: int | None = None
    y_floor: int | None = None

    for z, w in SIX_TYPES:
        max2 = max_vp_by_root_lifting(k, z, w, 2)
        max5 = max_vp_by_root_lifting(k, z, w, 5)

        xs = 2 * vp(w, 2) - 1 - k - max2
        ys = -k - max5

        x_floor = xs if x_floor is None else min(x_floor, xs)
        y_floor = ys if y_floor is None else min(y_floor, ys)

    assert x_floor is not None and y_floor is not None
    return x_floor, y_floor


def derive_box(k: int, hmax: int, x_floor: int, y_floor: int) -> tuple[int, int, int, int]:
    low = 10 ** (k - 1)
    high = 10**k

    # If x>k, cross-corridor forces y>=y_floor.
    x_hi = k
    while ppow(2, x_hi + 1) * ppow(5, y_floor) < high:
        x_hi += 1

    # If x<x_floor, cross-corridor forces y<=k.
    x_lo = x_floor
    while Fraction(hmax) * ppow(2, x_lo - 1) * ppow(5, k) >= low:
        x_lo -= 1

    # If y>k, cross-corridor forces x>=x_floor.
    y_hi = k
    while ppow(2, x_floor) * ppow(5, y_hi + 1) < high:
        y_hi += 1

    # If y<y_floor, cross-corridor forces x<=k.
    y_lo = y_floor
    while Fraction(hmax) * ppow(2, k) * ppow(5, y_lo - 1) >= low:
        y_lo -= 1

    return x_lo, x_hi, y_lo, y_hi


def rho_num_den(h: int, x: int, y: int) -> tuple[int, int]:
    num = h
    den = 1
    if x >= 0:
        num *= 2**x
    else:
        den *= 2 ** (-x)
    if y >= 0:
        num *= 5**y
    else:
        den *= 5 ** (-y)
    return num, den


def rho_ge_integer(h: int, x: int, y: int, target: int) -> bool:
    num, den = rho_num_den(h, x, y)
    return num >= target * den


def first_y_ge_target(
    h: int,
    x: int,
    target: int,
    y_lo: int,
    y_hi: int,
) -> int:
    """First y in [y_lo,y_hi+1] with h*2^x*5^y >= target."""
    lo = y_lo
    hi = y_hi + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if rho_ge_integer(h, x, mid, target):
            hi = mid
        else:
            lo = mid + 1
    return lo


def certify_layer(k: int) -> None:
    expected_h, expected_xf, expected_yf, expected_box, expected_decade = EXPECTED[k]

    hs_by_w = {w: odd_prime_supply(k, w) for w in (1, 2, 3, 4)}
    h_counts = tuple(len(hs_by_w[w]) for w in (1, 2, 3, 4))
    if h_counts != expected_h:
        raise AssertionError(f"k={k}: h counts changed: {h_counts} != {expected_h}")

    x_floor, y_floor = valuation_floors(k)
    if x_floor != expected_xf or y_floor != expected_yf:
        raise AssertionError(
            f"k={k}: valuation floors changed: {(x_floor,y_floor)} "
            f"!= {(expected_xf,expected_yf)}"
        )

    hmax = max(max(hs) for hs in hs_by_w.values())
    box = derive_box(k, hmax, x_floor, y_floor)
    if box != expected_box:
        raise AssertionError(f"k={k}: box changed: {box} != {expected_box}")

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
                # The decade has width factor 10, so only one or two y values
                # can occur. Find them by exact monotone binary search.
                first = first_y_ge_target(h, x, low_decade, y_lo, y_hi)
                stop = first_y_ge_target(h, x, high_decade, y_lo, y_hi)

                for y in range(first, stop):
                    if y > y_hi:
                        break

                    # Safe global consequences of the two cross-corridors.
                    if x > k and y < y_floor:
                        continue
                    if y > k and x < x_floor:
                        continue

                    num, den = rho_num_den(h, x, y)
                    rho = Fraction(num, den)
                    if not (low_decade <= rho < high_decade):
                        raise AssertionError("binary-search decade recovery failed")

                    decade_states += 1
                    N0 = (rho.numerator + rho.denominator - 1) // rho.denominator
                    gap = Fraction(N0) - rho

                    if low_gap < gap < high_gap:
                        near_hits += 1
                        print(
                            "NEAR HIT "
                            f"k={k} w={w} h={h} x={x} y={y} "
                            f"N0={N0} gap={gap}"
                        )

    if decade_states != expected_decade:
        raise AssertionError(
            f"k={k}: decade states changed: {decade_states} != {expected_decade}"
        )
    if near_hits != 0:
        raise AssertionError(f"k={k}: unexpected near-integer hits: {near_hits}")

    print(
        f"k={k} h_counts={h_counts} floors=({x_floor},{y_floor}) "
        f"box={box} decade_states={decade_states} near_hits=0"
    )


def run() -> None:
    for k in LAYERS:
        certify_layer(k)
    print("CERTIFICATE OK: A1 minimal diagonal k=g=6..23 is empty.")


if __name__ == "__main__":
    run()
