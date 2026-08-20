#!/usr/bin/env python3
"""Deterministic auditor for the final A2 fixed-23 eta=2 c=2 type.

This script NEVER factors S_lambda(c_u) or c_u. A caller supplies a proposed
source factor theta after the source-content prime-support certificate, plus
the two finite orientation choices. The script reconstructs all remaining
integers and either rejects the tuple or prints the unique candidate together
with its actual 23-common depth.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

CQ = 1587
P23SQ = 23**2
ALLOCATIONS = {(1, 1587), (3, 529), (529, 3), (1587, 1)}


def fail(msg: str) -> None:
    raise ValueError(msg)


def v_p(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    if math.gcd(m, n) != 1:
        fail(f"CRT moduli not coprime: {m}, {n}")
    a %= m
    b %= n
    k = ((b - a) * pow(m, -1, n)) % n
    mod = m * n
    return (a + m * k) % mod, mod


def sqrt_minus_one_mod_5_power(exp: int, sign: int) -> int:
    """Return one of the two roots of x^2=-1 modulo 5^exp."""
    if exp < 1:
        return 0
    if sign not in (-1, 1):
        fail("Gaussian sign must be +1 or -1")
    r = 2 if sign == 1 else 3
    mod = 5
    for _ in range(1, exp):
        next_mod = mod * 5
        step = mod
        lifts = [r + d * step for d in range(5)
                 if ((r + d * step) ** 2 + 1) % next_mod == 0]
        if len(lifts) != 1:
            fail("unexpected 5-adic sqrt lifting failure")
        r = lifts[0] % next_mod
        mod = next_mod
    assert (r * r + 1) % mod == 0
    return r


def centered_binary_root(lam: int, cu: int) -> int:
    """Unique odd u solving u^2+c*u+S^2/4=0 mod 2^(lambda+1)."""
    m = lam + 1
    c = CQ * cu
    S = 5 ** (3 * lam) + c
    const = S * S // 4
    r = 1
    mod = 2
    if (r * r + c * r + const) % mod:
        fail("centered binary polynomial has no mod-2 root")
    for _ in range(1, m):
        next_mod = mod * 2
        candidates = (r, r + mod)
        lifts = [x for x in candidates
                 if (x * x + c * x + const) % next_mod == 0]
        if len(lifts) != 1:
            fail("unexpected binary Hensel branching")
        r = lifts[0] % next_mod
        mod = next_mod
    return r


@dataclass
class Candidate:
    lam: int
    cu: int
    theta: int
    gaussian_sign: int
    cminus: int
    cplus: int
    g: int
    omega: int
    b3: int
    a3: int
    a2: int
    b2: int
    q: int
    C: int
    D: int
    X: int
    Y: int
    depth23: int
    sigma: str


def audit(lam: int, cu: int, theta: int, gaussian_sign: int,
          cminus: int) -> Candidate:
    if lam < 1 or (lam - 8) % 11:
        fail("lambda must be positive and congruent to 8 mod 11")
    if cu <= 0 or cu % 2 == 0 or cu % 5 == 0 or cu % 4 != 1:
        fail("c_u must be a positive odd 5-unit with c_u=1 mod 4")
    # Full prime-support certification for c_u belongs to the source-content
    # stage. This reconstruction auditor intentionally performs no factorization.

    if CQ % cminus:
        fail("c_- must divide 1587")
    cplus = CQ // cminus
    if (cminus, cplus) not in ALLOCATIONS:
        fail("invalid canonical prime-power allocation")

    M = 2 * lam
    m = lam + 1
    T = 10**m
    N = 10**M
    L = 2**m * 5**lam * cu
    S = 5**(3 * lam) + CQ * cu

    if theta <= 0 or theta % 2 == 0:
        fail("theta must be positive and odd")
    if S % theta:
        fail("theta does not divide S_lambda(c_u)")
    if not (2 * theta > 39 * L and 4 * theta < 79 * L):
        fail("theta is outside the centered 19.5--19.75 L_* slot")

    varrho = 20 * L - theta
    if not (4 * varrho > L and 2 * varrho < L):
        fail("varrho is outside (L_*/4,L_*/2)")
    if math.gcd(varrho, L) != 1:
        fail("gcd(varrho,L_*) != 1")

    g = S // theta
    if g % 4:
        fail("g must be divisible by 4")
    if math.gcd(g, cu) != 1 or math.gcd(g, CQ) != 1:
        fail("source primitive gcd for g failed")

    # Exact third denominator and its strict endpoint window.
    b3 = 2 ** (3 * lam + 2) * 5 * CQ * cu
    if not (1000 * b3 > 837 * T and 1000 * b3 < 843 * T):
        fail("b3/T is outside the certified source/endpoint window")

    # Hensel quotient omega.
    if (theta + L) % CQ:
        fail("omega=(theta+L_*)/c_Q is not integral")
    omega = (theta + L) // CQ

    # --- Full a3 CRT -----------------------------------------------------
    A2 = 2**m
    B5 = 5 ** (lam - 1)
    u2 = centered_binary_root(lam, cu)
    a2_res = (u2 * pow(varrho, -1, A2)) % A2

    iota = sqrt_minus_one_mod_5_power(lam - 1, gaussian_sign)
    inv2_B = pow(2, -1, B5)
    c = CQ * cu
    a5_res = (
        -c * inv2_B * pow(varrho, -1, B5)
        -45 * c * inv2_B * iota * pow(2, 3 * lam + 2, B5)
    ) % B5

    half_g = g // 2
    if cminus == 1:
        aq_minus, mod_minus = 0, 1
    else:
        aq_minus, mod_minus = half_g % cminus, cminus
    if cplus == 1:
        aq_plus, mod_plus = 0, 1
    else:
        aq_plus, mod_plus = (-half_g) % cplus, cplus
    aq_res, aq_mod = crt_pair(aq_minus, mod_minus, aq_plus, mod_plus)
    if aq_mod != CQ:
        fail("canonical CRT did not recover modulus 1587")

    r25, mod25 = crt_pair(a2_res, A2, a5_res, B5)
    rfull, mfull = crt_pair(r25, mod25, aq_res, CQ)
    if mfull != CQ * A2 * B5:
        fail("unexpected full a3 CRT modulus")

    h = (rfull - T) % mfull
    if not (0 < 250 * h < T):
        fail("full canonical a3 representative misses the 1/15870 cell")
    a3 = T + h
    if math.gcd(a3, b3) != 1:
        fail("gcd(a3,b3) != 1")

    # --- Deterministic reconstruction ----------------------------------
    a2_num = g * g - 4 * a3 * a3 - 81 * b3 * b3
    a2_den = 20 * CQ
    if a2_num <= 0 or a2_num % a2_den:
        fail("a2 reconstruction is non-positive or non-integral")
    a2 = a2_num // a2_den
    scale_a2 = 10 ** (M - 1)
    if not (250 * a2 > 249 * scale_a2 and a2 < scale_a2):
        fail("a2 misses the certified 249/250--1 digit window")

    b2 = 2 ** (M + m + 1) * cu * g
    if not (b2 > 10 ** (M - 1) and 19 * b2 < 2 * N):
        fail("b2 misses the certified (1/10,2/19) prefix window")
    if math.gcd(a2, b2) != 1:
        fail("gcd(a2,b2) != 1")

    Q = b2 + 2 * N
    qden = 2 ** (M + 1) * CQ
    if Q % qden:
        fail("q reconstruction is non-integral")
    q = Q // qden
    if q <= 0 or q % 23 == 0:
        fail("q must be positive and a 23-unit in the pure-c_Q type")

    z = q * 5**lam
    f = z + 2 * cu
    if g * omega != z + cu:
        fail("source triangle g*omega=z+c_u failed")

    D = g * T // 5**lam
    if D != 5 * 2**m * g:
        fail("finite-defect D identity failed")

    norm_star = (g - 2 * a3) ** 2 + 81 * b3 * b3
    if norm_star % 4:
        fail("third-block Gaussian norm is not divisible by 4")
    Cnum = 3 * g * T - norm_star // 4
    if Cnum % 5**lam:
        fail("finite-defect C reconstruction is non-integral")
    C = Cnum // 5**lam
    if not (C > 0 and 250 * C < 3 * D):
        fail("C misses the certified top-defect interval")
    if math.gcd(C, D) != 1:
        fail("gcd(C,D) != 1")

    xnum = 3 * D - C
    if xnum <= 0 or xnum % (cminus * cminus):
        fail("X reconstruction is non-integral")
    X = xnum // (cminus * cminus)

    if g * g % 2:
        fail("g^2/2 is non-integral")
    H0 = g * g // 2 - 5 * CQ * a2
    ynum = H0 + g * a3
    if ynum <= 0 or ynum % (cplus * cplus):
        fail("Y reconstruction is non-integral")
    Y = ynum // (cplus * cplus)

    if H0 - g * a3 != 5**lam * cminus * cminus * X:
        fail("minus canonical factor identity failed")
    if H0 + g * a3 != cplus * cplus * Y:
        fail("plus canonical factor identity failed")

    N0 = (9 * b2 // 2) ** 2 + a2 * a2
    if N0 != 5 ** (lam - 2) * X * Y:
        fail("N0=5^(lambda-2)XY failed")
    if math.gcd(X * Y, CQ) != 1:
        fail("XY is not primitive to c_Q")

    # --- Actual fixed-23 common depth ----------------------------------
    K = 9 * N + 10 * a2
    if K % 23 != 16:
        fail("fixed-23 first-layer K residue failed")
    Dpref = 2025 * b2 * b2 + 81 * N * N - K * K
    AK = K * K - 18 * K + 55
    EK = K * (2 * K - 9)
    Gplus = f * AK + 2 * cu * EK
    Gminus = z * AK - 2 * cu * EK

    if cminus % P23SQ == 0:
        sigma = "minus"
        gate = Gminus
    elif cplus % P23SQ == 0:
        sigma = "plus"
        gate = Gplus
    else:
        fail("canonical allocation does not carry the 23^2 block")

    depth23 = min(v_p(Dpref, 23), v_p(gate, 23), 4)
    if depth23 < 1:
        fail("candidate does not even enter the fixed-23 common first layer")

    return Candidate(
        lam=lam, cu=cu, theta=theta, gaussian_sign=gaussian_sign,
        cminus=cminus, cplus=cplus, g=g, omega=omega, b3=b3,
        a3=a3, a2=a2, b2=b2, q=q, C=C, D=D, X=X, Y=Y,
        depth23=depth23, sigma=sigma,
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lambda", dest="lam", type=int, required=True)
    ap.add_argument("--cu", type=int, required=True)
    ap.add_argument("--theta", type=int, required=True)
    ap.add_argument("--gaussian-sign", type=int, choices=(-1, 1), required=True)
    ap.add_argument("--cminus", type=int, choices=(1, 3, 529, 1587), required=True)
    args = ap.parse_args()

    try:
        cand = audit(args.lam, args.cu, args.theta,
                     args.gaussian_sign, args.cminus)
    except ValueError as exc:
        print(f"REJECT: {exc}")
        raise SystemExit(1)

    print("ACCEPT: deterministic A2 fixed-23 c=2 candidate")
    for field, value in cand.__dict__.items():
        print(f"{field}={value}")


if __name__ == "__main__":
    main()
