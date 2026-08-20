#!/usr/bin/env python3
"""Exact finite certificate for the A1 minimal diagonal slice k=g=3.

The proof is documented in
    docs/proofs/exact-lift/branches/a1-only/k3-certificate.md

The script uses only proved necessary conditions:
  * six minimal-surplus prefix types;
  * the near-integer j/tail theorem;
  * exact coprimality and K>0;
  * the strengthened odd-prime supply from the denominator prime graph;
  * exact 2/5 resonance and primitive cross-corridor bounds X0=Y0=3;
  * the partial-data rational-contact square sieve.

All arithmetic relevant to the certificate is exact.  There are no floating
point comparisons and no empirical exponent cutoffs.
"""

from __future__ import annotations

import bisect
import math
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

import sympy as sp


K = 3
GSHIFT = 3
LOW_RHO = Fraction(100)
HIGH_RHO = Fraction(1000)
NEAR_LOW = Fraction(101, 2000)   # 0.0505
NEAR_HIGH = Fraction(7, 400)     # 0.0175
SIX_TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))

EXPECTED_PREFIX_BY_TYPE = {
    (1, 1): 598,
    (1, 2): 451,
    (1, 3): 773,
    (1, 4): 300,
    (3, 1): 597,
    (3, 2): 451,
}
EXPECTED_STATES_BY_TYPE = {
    (1, 1): 58,
    (1, 2): 38,
    (1, 3): 23,
    (1, 4): 12,
    (3, 1): 61,
    (3, 2): 38,
}
EXPECTED_H_COUNTS = {1: 32, 2: 8, 3: 2, 4: 6}
EXPECTED_PREFIXES = 3170
EXPECTED_STATES = 230
EXPECTED_SQUARES = 0


@dataclass(frozen=True)
class Prefix:
    z: int
    w: int
    j: int
    a1: int
    b1: int
    a2: int
    b2: int
    Q: int
    G: int
    C: int
    N: int
    D: int
    Kdef: int


@dataclass(frozen=True)
class PadicData:
    k2: int
    k5: int
    d2: int
    d5: int
    g2: int
    g5: int
    c2: int
    c5: int
    n2: int
    n5: int
    x_star: int
    y_star: int
    X0: int
    Y0: int


@dataclass(frozen=True)
class TailState:
    h: int
    x: int
    y: int
    rho: Fraction


def vp(n: int, p: int) -> int:
    n = abs(n)
    if n == 0:
        raise ValueError("vp(0,p) is not used")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def ppow(p: int, e: int) -> Fraction:
    if e >= 0:
        return Fraction(p**e)
    return Fraction(1, p ** (-e))


def rho_value(h: int, x: int, y: int) -> Fraction:
    return Fraction(h) * ppow(2, x) * ppow(5, y)


def rational_square_root(q: Fraction) -> Fraction | None:
    if q < 0:
        return None
    sn = isqrt(q.numerator)
    sd = isqrt(q.denominator)
    if sn * sn == q.numerator and sd * sd == q.denominator:
        return Fraction(sn, sd)
    return None


def all_divisors(factors: dict[int, int]) -> list[int]:
    out = [1]
    for p, e in sorted(factors.items()):
        out = [d * p**j for d in out for j in range(e + 1)]
    return sorted(out)


def min_exp_ge(p: int, coeff: Fraction, target: Fraction) -> int:
    """Least integer e with coeff*p**e >= target, computed exactly."""
    e = 0
    value = coeff
    if value >= target:
        while value / p >= target:
            value /= p
            e -= 1
    else:
        while value < target:
            value *= p
            e += 1
    return e


def max_exp_lt(p: int, coeff: Fraction, target: Fraction) -> int:
    """Greatest integer e with coeff*p**e < target, computed exactly."""
    e = 0
    value = coeff
    if value < target:
        while value * p < target:
            value *= p
            e += 1
    else:
        while value >= target:
            value /= p
            e -= 1
    return e


def build_prefixes() -> list[Prefix]:
    """Enumerate the complete k=3 prefix box.

    near-integer-tail.md plus 100 <= rho < 1000 gives exactly
        1099 <= j <= 1999.
    """
    out: list[Prefix] = []
    b2 = 1
    n2_digits = 7

    for z, w in SIX_TYPES:
        c = 5 - z
        b1 = 10 ** (2 * K + 1) - w
        a2 = 10 ** (2 * K + 1) - z

        for j in range(1099, 2000):
            x_prefix = (c - w) * 10 ** (K + 1) + j
            a1 = 10 ** (3 * K + 2) + x_prefix

            if math.gcd(a1, b1) != 1:
                continue

            Q = 10 * b1 + b2
            G = b1
            C = a1 * 10**n2_digits + a2
            N = a1 * a1 + (a2 * b1) ** 2
            D = 10**GSHIFT * Q
            Kdef = G * G * C * C - D * D * N

            # Exact contact requires P > R > sqrt(S), hence Kdef>0.
            if Kdef <= 0:
                continue

            out.append(Prefix(z, w, j, a1, b1, a2, b2, Q, G, C, N, D, Kdef))

    return out


def odd_prime_supply(w: int) -> list[int]:
    """Construct all h allowed by the proved minimal-diagonal prime graph.

    Q-side: arbitrary divisor q|Q, with each exponent at most its Q exponent.
    b1-side: each odd 1 mod 4 prime-power block is selected whole or omitted.
    The two sides are coprime because gcd(Q,b1)=1.
    """
    b1 = 10 ** (2 * K + 1) - w
    Q = 10 * b1 + 1

    q_divisors = all_divisors(sp.factorint(Q))
    selectable_blocks: list[int] = []
    for p, e in sp.factorint(b1).items():
        if p not in (2, 5) and p % 4 == 1:
            selectable_blocks.append(p**e)

    selectors = [1]
    for block in selectable_blocks:
        selectors += [s * block for s in selectors]

    hs = sorted(q * s for q in q_divisors for s in selectors)
    if len(hs) != len(set(hs)):
        raise AssertionError("odd-prime supply unexpectedly contains duplicates")
    expected = EXPECTED_H_COUNTS[w]
    if len(hs) != expected:
        raise AssertionError(f"h supply changed for w={w}: {len(hs)} != {expected}")
    return hs


def padic_data(p: Prefix) -> PadicData:
    k2 = vp(p.Kdef, 2)
    k5 = vp(p.Kdef, 5)
    d2 = vp(p.D, 2)
    d5 = vp(p.D, 5)
    g2 = vp(p.G, 2)
    g5 = vp(p.G, 5)
    c2 = vp(p.C, 2)
    c5 = vp(p.C, 5)
    n2 = vp(p.N, 2)
    n5 = vp(p.N, 5)

    # Re-audit the k>=3 valuation normal form on every enumerated prefix.
    if k5 != 0:
        raise AssertionError(f"v5(K) != 0 for prefix {p}")
    if k2 != 2 * vp(p.w, 2):
        raise AssertionError(f"v2(K) normal form failed for prefix {p}")
    if (d2, d5) != (K, K):
        raise AssertionError(f"D valuation normal form failed for prefix {p}")
    if (c2, c5) != (0, 0):
        raise AssertionError(f"C valuation normal form failed for prefix {p}")

    x_star = k2 - (1 + d2 + n2)
    y_star = k5 - (d5 + n5)

    # Primitive cross-corridor bounds, evaluated from the general formula.
    if k2 % 2 == 0:
        X0 = max(
            0,
            d2,
            d2 + k2 // 2 - g2 - c2,
            d2 + g2 - k2 // 2,
        )
    else:
        X0 = x_star

    if k5 % 2 == 0:
        Y0 = max(
            0,
            d5,
            d5 + k5 // 2 - g5 - c5,
            d5 + g5 - k5 // 2,
        )
    else:
        Y0 = y_star

    if X0 != K or Y0 != K:
        raise AssertionError(f"cross-corridor cap changed: X0={X0}, Y0={Y0}")

    return PadicData(
        k2, k5, d2, d5, g2, g5, c2, c5, n2, n5,
        x_star, y_star, X0, Y0,
    )


def finite_xy_box(h: int, pd: PadicData) -> tuple[int, int, int, int]:
    """A conservative theorem-derived rectangle covering every feasible (x,y).

    Feasible rho obeys 100 <= h*2^x*5^y < 1000.  The two strict cross
    corridors have high-coordinate caps X0 and Y0; the ++/-- and resonance
    sectors are bounded by the decade strip after fixing the opposite side of
    the resonance line.  These are the same proved cases used by the k=1,2
    certificates.
    """
    xs = pd.x_star
    ys = pd.y_star

    if pd.k2 % 2:
        xmax = xs
    else:
        xmax = max(
            pd.X0,
            max_exp_lt(2, Fraction(h) * ppow(5, ys), HIGH_RHO),
        )

    y_cap_when_x_low = max(ys, pd.Y0)
    xmin = min_exp_ge(
        2,
        Fraction(h) * ppow(5, y_cap_when_x_low),
        LOW_RHO,
    )

    if pd.k5 % 2:
        ymax = ys
    else:
        ymax = max(
            pd.Y0,
            max_exp_lt(5, Fraction(h) * ppow(2, xs), HIGH_RHO),
        )

    x_cap_when_y_low = max(xs, pd.X0)
    ymin = min_exp_ge(
        5,
        Fraction(h) * ppow(2, x_cap_when_y_low),
        LOW_RHO,
    )

    return xmin, xmax, ymin, ymax


def sector_is_possible(x: int, y: int, pd: PadicData) -> bool:
    # Strict K-dominant high side with odd p-adic K valuation cannot be square.
    if x > pd.x_star and pd.k2 % 2:
        return False
    if y > pd.y_star and pd.k5 % 2:
        return False

    # Proved primitive caps on the two cross corridors.
    if x > pd.x_star and y < pd.y_star and x > pd.X0:
        return False
    if x < pd.x_star and y > pd.y_star and y > pd.Y0:
        return False

    return True


def tail_candidates_for_signature(
    pd: PadicData,
    hs: list[int],
) -> list[TailState]:
    """Enumerate the complete decade/resonance/corridor tail set for one signature."""
    out: list[TailState] = []
    for h in hs:
        xmin, xmax, ymin, ymax = finite_xy_box(h, pd)
        if xmin > xmax or ymin > ymax:
            continue
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                rho = rho_value(h, x, y)
                if not (LOW_RHO <= rho < HIGH_RHO):
                    continue
                if not sector_is_possible(x, y, pd):
                    continue
                out.append(TailState(h, x, y, rho))

    out.sort(key=lambda state: state.rho)
    return out


def run() -> None:
    prefixes = build_prefixes()

    prefix_by_type: dict[tuple[int, int], int] = defaultdict(int)
    for p in prefixes:
        prefix_by_type[(p.z, p.w)] += 1

    if len(prefixes) != EXPECTED_PREFIXES:
        raise AssertionError(f"prefix count changed: {len(prefixes)} != {EXPECTED_PREFIXES}")
    if dict(prefix_by_type) != EXPECTED_PREFIX_BY_TYPE:
        raise AssertionError(
            f"prefix type counts changed: {dict(prefix_by_type)} != {EXPECTED_PREFIX_BY_TYPE}"
        )

    h_by_w = {w: odd_prime_supply(w) for w in (1, 2, 3, 4)}

    # Only (w,v2(N),v5(N)) affects the resonance/corridor tail geometry.
    signature_representative: dict[tuple[int, int, int], PadicData] = {}
    prefix_padic: list[PadicData] = []
    for p in prefixes:
        pd = padic_data(p)
        prefix_padic.append(pd)
        key = (p.w, pd.n2, pd.n5)
        signature_representative.setdefault(key, pd)

    tails_by_signature: dict[tuple[int, int, int], list[TailState]] = {}
    rho_lists: dict[tuple[int, int, int], list[Fraction]] = {}
    for key, pd in signature_representative.items():
        tails = tail_candidates_for_signature(pd, h_by_w[key[0]])
        tails_by_signature[key] = tails
        rho_lists[key] = [state.rho for state in tails]

    states_by_type: dict[tuple[int, int], int] = defaultdict(int)
    squares_by_type: dict[tuple[int, int], int] = defaultdict(int)
    total_states = 0
    total_squares = 0

    for p, pd in zip(prefixes, prefix_padic):
        key = (p.w, pd.n2, pd.n5)
        tails = tails_by_signature[key]
        rhos = rho_lists[key]

        # N=j-10^k+1 = j-999 at k=3.
        center = Fraction(p.j - 10**K + 1)
        lower = center - NEAR_LOW
        upper = center + NEAR_HIGH

        # Strict near-integer interval; bisect keeps it exact and fast.
        lo = bisect.bisect_right(rhos, lower)
        hi = bisect.bisect_left(rhos, upper)
        surviving = tails[lo:hi]

        typ = (p.z, p.w)
        states_by_type[typ] += len(surviving)
        total_states += len(surviving)

        if not surviving:
            continue

        P = Fraction(p.C, p.D)
        S = Fraction(p.N, p.G * p.G)

        for state in surviving:
            theta = state.rho / p.D
            Xi = P * P - (1 + 2 * theta) * S
            if rational_square_root(Xi) is not None:
                squares_by_type[typ] += 1
                total_squares += 1

    if total_states != EXPECTED_STATES:
        raise AssertionError(f"tail state count changed: {total_states} != {EXPECTED_STATES}")
    if dict(states_by_type) != EXPECTED_STATES_BY_TYPE:
        raise AssertionError(
            f"tail type counts changed: {dict(states_by_type)} != {EXPECTED_STATES_BY_TYPE}"
        )
    if total_squares != EXPECTED_SQUARES:
        raise AssertionError(f"square count changed: {total_squares} != {EXPECTED_SQUARES}")

    print(f"prefixes={len(prefixes)}")
    print("h_supply=" + ",".join(f"w{w}:{len(h_by_w[w])}" for w in (1, 2, 3, 4)))
    for typ in SIX_TYPES:
        print(
            f"type={typ} prefixes={prefix_by_type[typ]} "
            f"tail_states={states_by_type[typ]} "
            f"rational_square_contacts={squares_by_type[typ]}"
        )
    print(f"tail_states={total_states}")
    print(f"rational_square_contacts={total_squares}")
    print("CERTIFICATE OK: k=g=3, r=s=1 minimal diagonal slice is empty.")


if __name__ == "__main__":
    run()
