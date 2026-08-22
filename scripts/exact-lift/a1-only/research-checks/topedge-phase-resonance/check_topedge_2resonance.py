#!/usr/bin/env python3
"""Exact finite certificate for A1 minimal-diagonal single-5 top-edge
2-adic resonance states with v5(N)>B.

No factorization of b1 or Q is used.
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


def v_p(n: int, p: int) -> int:
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def sqrt_minus_one_mod_5pow(m: int) -> tuple[int, int]:
    """Return the two roots of x^2=-1 mod 5^m by exact Hensel lifting."""
    assert m >= 1
    r = 2  # 2^2 = -1 mod 5
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
    return r, (-r) % mod


def bmax(k: int) -> int:
    # Strict theorem-derived bound B < 2.293*k + 7.57.
    # Largest integer B with 1000 B < 2293 k + 7570:
    return (2293 * k + 7569) // 1000


def phase_A(z: int, w: int, k: int, N0: int) -> int:
    T = 10**k
    if z == 1:
        return 14 * N0 + (339 - 40*w) * T
    assert z == 3
    return 12 * N0 + (237 - 20*w) * T


def main() -> None:
    hensel_resonance_hits = []
    phase_survivors = []

    root_cache = {}

    for z, w in TYPES:
        two_shift = 1 if z == 1 else 2
        for k in range(32, KMAX[(z,w)] + 1):
            T = 10**k
            c1 = 10 * (5 - z - w) + 1
            Aconst = 100 * T**3 + c1 * T - 1
            C = (10 * T**2 - z) * (10 * T**2 - w)

            # The only 2-adic resonance for A_{z,w}:
            # z=1: v2(N0)=k-1; z=3: v2(N0)=k-2.
            r2 = k - two_shift
            scale2 = 2**r2

            lo_m = (10**(k-1) + scale2 - 1) // scale2
            hi_m = (10**k - 1) // scale2

            for B in range(k + 1, bmax(k) + 1):
                m5 = B + 1
                mod5 = 5**m5
                roots_i = root_cache.get(m5)
                if roots_i is None:
                    roots_i = sqrt_minus_one_mod_5pow(m5)
                    root_cache[m5] = roots_i

                # hi_m < 5^(B+1) because B>=k+1:
                # z=1 gives hi_m<2*5^k, z=3 gives hi_m<4*5^k,
                # while mod5>=25*5^k.
                assert hi_m < mod5

                inv_scale2 = pow(scale2, -1, mod5)

                for ii in roots_i:
                    # N=(Aconst+N0)^2+C^2.
                    # N=0 mod 5^(B+1) iff
                    # N0=-Aconst +/- C*i mod 5^(B+1), i^2=-1.
                    root_N0 = (-Aconst + C * ii) % mod5
                    m_res = (root_N0 * inv_scale2) % mod5

                    if not (lo_m <= m_res <= hi_m):
                        continue
                    if m_res % 2 == 0:
                        continue  # exact v2(N0)=r2 requires odd multiplier

                    N0 = scale2 * m_res
                    a1 = Aconst + N0
                    N = a1*a1 + C*C
                    n5 = v_p(N, 5)
                    if n5 <= B:
                        continue

                    state = (z, w, k, B, N0, n5)
                    hensel_resonance_hits.append(state)

                    d = B - k
                    A = phase_A(z, w, k, N0)
                    modulus_E = 10 * 2**k
                    residue = (5**d * A) % modulus_E
                    first_positive = residue if residue else modulus_E
                    Emax = 30 * 5**d

                    if first_positive < Emax:
                        phase_survivors.append(
                            state + (first_positive, Emax)
                        )

    assert len(hensel_resonance_hits) == 33, len(hensel_resonance_hits)
    assert phase_survivors == [], phase_survivors

    print("top-edge 2-adic resonance certificate")
    print("Hensel/high-5 resonance states:", len(hensel_resonance_hits))
    print("phase-residue survivors:", len(phase_survivors))
    print("PASS")


if __name__ == "__main__":
    main()
