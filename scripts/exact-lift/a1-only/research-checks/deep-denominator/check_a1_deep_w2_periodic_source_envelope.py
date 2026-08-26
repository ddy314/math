#!/usr/bin/env python3

from collections import Counter
from math import gcd, lcm


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
    x = 10 % p
    o = 1
    while x != 1:
        x = x * 10 % p
        o += 1
    return o


def classes(p: int, side: str):
    o = ord10(p)
    if side == "b":
        return tuple(k for k in range(o) if (pow(10, 2 * k + 1, p) - 2) % p == 0)
    return tuple(k for k in range(o) if (pow(10, 2 * k + 2, p) - 19) % p == 0)


def source_list(side: str, limit: int = 1000):
    out = []
    for p in range(3, limit + 1, 4):
        if not is_prime(p):
            continue
        c = classes(p, side)
        if c:
            out.append((p, ord10(p), c))
    return out


def occurs(ent, k: int) -> bool:
    p, o, c = ent
    return k % o in c


BS = source_list("b")
QS = source_list("q")

assert [x[0] for x in BS[:5]] == [19, 31, 59, 71, 131]
assert [x[0] for x in QS[:6]] == [3, 31, 59, 67, 71, 107]

B_KNOWN = BS[:4]
Q_KNOWN = QS[1:5]  # 3 is absorbed by beta
B_SENTINEL = 131
Q_SENTINEL = 107

L = 1
for ent in B_KNOWN + Q_KNOWN:
    L = lcm(L, ent[1])
assert L == 200970


def envelope(k: int) -> int:
    ps = [ent[0] for ent in B_KNOWN if occurs(ent, k)]
    qs = [ent[0] for ent in Q_KNOWN if occurs(ent, k)]

    # Any unlisted actual source is at least the next source prime.
    p_options = ps + [B_SENTINEL]
    q_options = qs + [Q_SENTINEL]

    best = None
    for p in p_options:
        for q in q_options:
            if p == q:
                continue
            cand = 2 * p * q
            if best is None or cand < best:
                best = cand
    assert best is not None
    return best


counts = Counter(envelope(k) for k in range(L))
expected = {
    2242: 770,
    2698: 616,
    3658: 924,
    4066: 20944,
    4154: 1176,
    6634: 11760,
    7906: 168,
    8122: 12936,
    8378: 346,
    9514: 162,
    12626: 4898,
    15194: 4590,
    15458: 5060,
    17554: 4374,
    18602: 4590,
    28034: 127656,
}
assert counts == expected, (counts, expected)
assert sum(counts.values()) == L

assert sum(c for j, c in counts.items() if j >= 3658) == 199584
assert sum(c for j, c in counts.items() if j >= 4154) == 177716
assert sum(c for j, c in counts.items() if j >= 7906) == 164780
assert counts[28034] == 127656

assert 10001 / 28034 < 0.357

print(f"period L={L}")
for j in sorted(counts):
    c = counts[j]
    print(f"J={j:<5} count={c:<6} fraction={c/L:.12f}")

print("ge3658", 199584 / L)
print("ge4154", 177716 / L)
print("ge7906", 164780 / L)
print("eq28034", 127656 / L)
print("CERTIFICATE OK: w=2, 3|beta periodic source envelope audited exactly.")
