#!/usr/bin/env python3

from math import gcd


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def ord10(p: int) -> int:
    assert gcd(10, p) == 1
    x = 10 % p
    o = 1
    while x != 1:
        x = (x * 10) % p
        o += 1
    return o


def b_classes(p: int):
    o = ord10(p)
    return tuple(k for k in range(o) if (pow(10, 2 * k + 1, p) - 2) % p == 0)


def q_classes(p: int):
    o = ord10(p)
    return tuple(k for k in range(o) if (pow(10, 2 * k + 2, p) - 19) % p == 0)


def sources(which: str, limit: int = 1000):
    out = []
    for p in range(3, limit + 1, 4):
        if not is_prime(p):
            continue
        cls = b_classes(p) if which == "b" else q_classes(p)
        if cls:
            out.append((p, ord10(p), cls))
    return out


def compatible(a, b) -> bool:
    _, oa, ca = a
    _, ob, cb = b
    g = gcd(oa, ob)
    return any((x - y) % g == 0 for x in ca for y in cb)


def jper(alpha: int, beta: int, bs, qs):
    best = None
    for bp in bs:
        p = bp[0]
        if alpha % p == 0:
            continue
        for qq in qs:
            q = qq[0]
            if beta % q == 0 or p == q:
                continue
            if not compatible(bp, qq):
                continue
            cand = (2 * p * q, p, q)
            if best is None or cand < best:
                best = cand
    assert best is not None
    return best


BS = sources("b")
QS = sources("q")

assert [(p, o, c) for p, o, c in BS[:6]] == [
    (19, 18, (8, 17)),
    (31, 15, (10,)),
    (59, 58, (12, 41)),
    (71, 35, (14,)),
    (131, 130, (41, 106)),
    (151, 75, (17,)),
]

assert [(p, o, c) for p, o, c in QS[:6]] == [
    (3, 1, (0,)),
    (31, 15, (12,)),
    (59, 58, (10, 39)),
    (67, 33, (22,)),
    (71, 35, (26,)),
    (107, 53, (23,)),
]

b19 = next(x for x in BS if x[0] == 19)
q31 = next(x for x in QS if x[0] == 31)
q59 = next(x for x in QS if x[0] == 59)
q67 = next(x for x in QS if x[0] == 67)
q71 = next(x for x in QS if x[0] == 71)

assert not compatible(b19, q31)
assert compatible(b19, q59)
assert not compatible(b19, q67)
assert compatible(b19, q71)

CASES = [
    (1, 1, (114, 19, 3)),
    (1, 3, (2242, 19, 59)),
    (19, 1, (186, 31, 3)),
    (19, 3, (3658, 31, 59)),
    (19 * 31, 3, (3658, 59, 31)),
    (19, 3 * 31, (3658, 31, 59)),
    (19 * 31, 3 * 31, (7906, 59, 67)),
    (1, 3 * 31 * 59, (2698, 19, 71)),
    (19, 3 * 31 * 59, (4154, 31, 67)),
]

for alpha, beta, expected in CASES:
    got = jper(alpha, beta, BS, QS)
    assert got == expected, (alpha, beta, got, expected)
    J, p, q = got
    print(
        f"alpha={alpha:<6} beta={beta:<6} "
        f"Jper={J:<5} pair=({p},{q}) D/T^2<{10001/J:.12f}"
    )

assert jper(1, 3, BS, QS)[0] == 2242
assert 10001 / 2242 < 4.461
assert jper(19, 3, BS, QS)[0] == 3658
assert 10001 / 3658 < 2.735
assert jper(19 * 31, 3 * 31, BS, QS)[0] == 7906
assert 10001 / 7906 < 1.265

print("CERTIFICATE OK: w=2 periodic source matching audited exactly.")
