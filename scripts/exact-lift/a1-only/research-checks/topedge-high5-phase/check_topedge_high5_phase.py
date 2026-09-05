#!/usr/bin/env python3
"""Exact certificate closing the A1 minimal-diagonal single-5 top-edge
branch v5(N)>B after the theorem-derived finite-height collapse.

The scan does NOT factor b1 or Q and does NOT enumerate all N0.  It counts
solutions on the two 5-adic Hensel progressions with an exact floor-sum
for the 2^(3k) phase-gap residue interval.
"""

TYPES = [(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)]
KMAX = {
    (1,1): 77,
    (1,2): 75,
    (1,3): 74,
    (1,4): 72,
    (3,1): 74,
    (3,2): 73,
}


def bmax(k: int) -> int:
    # Strict bound B < 2.293*k + 7.57.
    return (2293 * k + 7569) // 1000


def sqrt_minus_one_mod_5pow(m: int, cache={}) -> tuple[int, int]:
    if m in cache:
        return cache[m]
    assert m >= 1
    r = 2
    mod = 5
    for _ in range(1, m):
        target = mod * 5
        for t in range(5):
            cand = r + t * mod
            if (cand * cand + 1) % target == 0:
                r = cand
                break
        else:
            raise AssertionError("Hensel lift failed")
        mod = target
    out = (r, (-r) % mod)
    cache[m] = out
    return out


def floor_sum(n: int, m: int, a: int, b: int) -> int:
    """sum_{0<=i<n} floor((a*i+b)/m), exact ACL algorithm."""
    assert n >= 0 and m > 0 and a >= 0 and b >= 0
    ans = 0
    while True:
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y = a * n + b
        if y < m:
            return ans
        n = y // m
        b = y % m
        m, a = a, m


def count_lt(n: int, m: int, a: int, b: int, c: int) -> int:
    """Count i in [0,n) with (a*i+b) mod m < c."""
    if c <= 0:
        return 0
    if c >= m:
        return n
    f0 = floor_sum(n, m, a, b)
    f1 = floor_sum(n, m, a, b + m - c)
    ge_c = f1 - f0
    return n - ge_c


def count_positive_below(n: int, m: int, a: int, b: int, limit: int) -> int:
    """Count 0 < (a*i+b) mod m < limit, assuming 0<limit<=m."""
    assert 0 < limit <= m
    return count_lt(n, m, a, b, limit) - count_lt(n, m, a, b, 1)


def main() -> None:
    progression_count = 0
    raw_n0_count = 0
    phase_hits = 0

    for z, w in TYPES:
        alpha = 15 - z
        cphase = (339 - 40*w) if z == 1 else (237 - 20*w)

        for k in range(32, KMAX[(z,w)] + 1):
            T = 10**k
            low = 10**(k - 1)
            high = 10**k - 1

            c1 = 10 * (5 - z - w) + 1
            Aconst = 100 * T**3 + c1 * T - 1
            C0 = (10 * T**2 - z) * (10 * T**2 - w)

            mod2 = 2**(3*k)
            coeff_L = 10 * T**2 - alpha
            const_L = -cphase * T

            for B in range(k + 1, bmax(k) + 1):
                d = B - k
                mod5 = 5**(B + 1)
                eps_max = 6 * 5**d
                factor = -(5**(d - 1))

                for ii in sqrt_minus_one_mod_5pow(B + 1):
                    # v5(N)>B implies N=0 mod 5^(B+1), and
                    # N=(Aconst+N0)^2+C0^2.
                    root = (-Aconst + C0 * ii) % mod5

                    tmin = (low - root + mod5 - 1) // mod5
                    if tmin < 0:
                        tmin = 0
                    tmax = (high - root) // mod5
                    if tmax < tmin:
                        continue

                    n = tmax - tmin + 1
                    progression_count += 1
                    raw_n0_count += n

                    base_n0 = root + tmin * mod5

                    # From h*2^(3k)=5^(d-1)L+epsilon and h integer:
                    # epsilon == -5^(d-1)L (mod 2^(3k)),
                    # 0 < epsilon < 6*5^d.
                    step = (factor * coeff_L * mod5) % mod2
                    base = (factor * (coeff_L * base_n0 + const_L)) % mod2

                    if eps_max > mod2:
                        # In this very top d-strip every residue has some positive
                        # representative below eps_max, so this local phase test
                        # alone does not remove the progression.
                        cnt = n
                    else:
                        cnt = count_positive_below(n, mod2, step, base, eps_max)

                    phase_hits += cnt

    assert progression_count == 11335, progression_count
    assert raw_n0_count == 43351324312741023779405, raw_n0_count
    assert phase_hits == 0, phase_hits

    print("top-edge high-5 phase certificate")
    print("Hensel progressions:", progression_count)
    print("raw N0 states represented:", raw_n0_count)
    print("phase hits:", phase_hits)
    print("PASS")


if __name__ == "__main__":
    main()
