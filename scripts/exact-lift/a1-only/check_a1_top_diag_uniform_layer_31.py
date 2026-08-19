#!/usr/bin/env python3
"""Exact fixed-layer certificate for A1 minimal diagonal k=g=31.

This is the same theorem-derived finite (h,x,y) certificate used for k=6..30,
but it hard-codes the independently verified complete factorizations of b1,Q
at k=31.  It checks the OLD wider gap window

    5.09 < 10^31 (ceil(rho)-rho) < 50.45,

so zero hits is stronger than what the sharpened 15.09..39.003 theorem needs.

The y exponent is located by a floating proposal only for speed; exact integer
comparisons then normalize it to the first y with rho>=10^30, so no floating
comparison participates in the certificate.
"""

from __future__ import annotations

from math import ceil, log

K = 31
T = 10**K
LOW = 10 ** (K - 1)
HIGH = T
XLO, XHI, YLO, YHI = -321, 284, -120, 58
XFLOOR, YFLOOR = -33, -78
EXPECTED_H = (16384, 96, 16, 96)
EXPECTED_BY_W = (6066806, 36304, 6277, 37285)
EXPECTED_TOTAL = 6146672

BFACT = {
    1: {3: 4, 37: 1, 43: 1, 239: 1, 1933: 1, 4649: 1,
        10837: 1, 23311: 1, 45613: 1, 333667: 1, 10838689: 1,
        45121231: 1, 1921436048294281: 1},
    2: {2: 1, 286708827469: 1,
        1743929562315488233203353793595015722358410772661371: 1},
    3: {1346919923: 1, 259449246196264501631: 1,
        2861579460492886363697385972683569: 1},
    4: {2: 2, 3: 1, 563: 1, 6089: 1, 1140199765189932803: 1,
        21319815293589898298349080461849685173: 1},
}

QFACT = {
    1: {19: 1, 59: 1, 6271: 1, 4814471: 1, 36799991: 1,
        9566469711577703: 1, 839285264668608213245600047: 1},
    2: {3: 2, 229: 1, 590123: 1, 2905251589: 1,
        2830060496432818893873196008326791529212561543: 1},
    3: {13: 1, 32017831639834919: 1,
        24025073836472185097142619431263604193515060793: 1},
    4: {7: 2, 34673: 1, 7675984356934380436832851: 1,
        766793494003346313676638849083843: 1},
}


def divisors(factors: dict[int, int]) -> list[int]:
    ds = [1]
    for p, e in factors.items():
        old = ds
        ds = [d * p**j for d in old for j in range(e + 1)]
    return ds


def supply(w: int) -> list[int]:
    qs = divisors(QFACT[w])
    blocks = [
        p**e for p, e in BFACT[w].items()
        if p not in (2, 5) and p % 4 == 1
    ]
    selectors = [1]
    for block in blocks:
        selectors += [s * block for s in selectors]
    return sorted({q * s for q in qs for s in selectors})


def make_pair(h: int, x: int, y: int) -> tuple[int, int]:
    num, den = h, 1
    if x >= 0:
        num <<= x
    else:
        den <<= -x
    if y >= 0:
        num *= 5**y
    else:
        den *= 5 ** (-y)
    return num, den


def mul2(num: int, den: int) -> tuple[int, int]:
    if den % 2 == 0:
        return num, den // 2
    return 2 * num, den


def mul5(num: int, den: int) -> tuple[int, int]:
    if den % 5 == 0:
        return num, den // 5
    return 5 * num, den


def div5(num: int, den: int) -> tuple[int, int]:
    if num % 5 == 0:
        return num // 5, den
    return num, 5 * den


def scan_w(w: int, hs: list[int]) -> tuple[int, int]:
    states = 0
    hits = 0

    for h in hs:
        # Speed-only proposal.  The following while-loops exactly normalize it.
        y = ceil((log(LOW) - log(h) - XLO * log(2)) / log(5))
        num, den = make_pair(h, XLO, y)

        while num < LOW * den:
            y += 1
            num, den = mul5(num, den)
        while num >= 5 * LOW * den:
            y -= 1
            num, den = div5(num, den)

        # Invariant: y is exactly the first exponent with h*2^x*5^y >= LOW.
        for x in range(XLO, XHI + 1):
            for off in (0, 1):
                yy = y + off
                if not (YLO <= yy <= YHI):
                    continue

                n, d = (num, den) if off == 0 else mul5(num, den)
                if n >= HIGH * d:
                    continue
                if n < LOW * d:
                    raise AssertionError("lost decade lower bound")

                # Safe global consequences of the two cross corridors.
                if x > K and yy < YFLOOR:
                    continue
                if yy > K and x < XFLOOR:
                    continue

                states += 1
                n0 = (n + d - 1) // d
                rem = n0 * d - n

                # Exact OLD wide gap window:
                #   509/(100*T) < rem/d < 5045/(100*T).
                if (
                    rem
                    and 100 * T * rem > 509 * d
                    and 100 * T * rem < 5045 * d
                ):
                    hits += 1
                    print(
                        "NEAR HIT",
                        f"w={w} h={h} x={x} y={yy} N0={n0}",
                    )

            if x == XHI:
                break

            num, den = mul2(num, den)
            while num >= 5 * LOW * den:
                y -= 1
                num, den = div5(num, den)

    return states, hits


def main() -> None:
    hs_by_w = {w: supply(w) for w in (1, 2, 3, 4)}
    h_counts = tuple(len(hs_by_w[w]) for w in (1, 2, 3, 4))
    assert h_counts == EXPECTED_H, h_counts

    by_w = []
    total_hits = 0
    for w in (1, 2, 3, 4):
        states, hits = scan_w(w, hs_by_w[w])
        by_w.append(states)
        total_hits += hits
        print(f"w={w}: states={states}, hits={hits}")

    assert tuple(by_w) == EXPECTED_BY_W, tuple(by_w)
    assert sum(by_w) == EXPECTED_TOTAL
    assert total_hits == 0

    print(
        "CERTIFICATE OK: k=g=31; "
        f"H={h_counts}; floors=({XFLOOR},{YFLOOR}); "
        f"box=({XLO},{XHI},{YLO},{YHI}); "
        f"decade_states={EXPECTED_TOTAL}; old-wide hits=0"
    )


if __name__ == "__main__":
    main()
