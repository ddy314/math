#!/usr/bin/env python3
"""Exact certificate for external-secant-center.md.

The script uses only Python's standard library. It checks the universal
secant-center factorization, the inert/discriminant character filter, and the
three genuine simple mod-47 branches together with their decimal orbit data.
It is not a global A2 solver.
"""

from fractions import Fraction


def legendre(a: int, p: int) -> int:
    r = pow(a % p, (p - 1) // 2, p)
    if r == p - 1:
        return -1
    return r


def multiplicative_order(a: int, p: int) -> int:
    x = 1
    for k in range(1, p):
        x = x * a % p
        if x == 1:
            return k
    raise AssertionError("order not found")


# ---------------------------------------------------------------------------
# Universal rational secant center.
# ---------------------------------------------------------------------------
K = Fraction(55, 18)
a = -K
R = Fraction(-2695, 324)


def phi(j: int) -> Fraction:
    return j * (j + 2 * a) * (K - j) ** 2 - R * (j + a) ** 2


assert phi(2) == Fraction(19 * 19 * 31, 18**4)
assert phi(3) == Fraction(-7 * 47, 18**4)
assert phi(4) == Fraction(-(17**2) * 41, 18**4)

# After dividing by D-C=-19C and D+C=-17C, the common-scale cofactor
# coefficients are exactly 589, -329, 697.
xi_minus = 19 * 31
xi_center = -7 * 47
xi_plus = 17 * 41
assert (xi_minus, xi_center, xi_plus) == (589, -329, 697)
assert xi_center - xi_minus == -54 * 17
assert xi_plus - xi_center == 54 * 19

# Additive-center cancellation.
assert (-17) * (54 * 19) + (-19) * (-54 * 17) == 0

# Character filter on the fixed factors.
assert 19 % 4 == 3 and legendre(55, 19) == 1
assert 31 % 4 == 3 and legendre(55, 31) == -1
assert 7 % 4 == 3 and legendre(55, 7) == -1
assert 47 % 4 == 3 and legendre(55, 47) == 1
assert 17 % 4 == 1
assert 41 % 4 == 1

# ---------------------------------------------------------------------------
# Fully coupled spontaneous equations mod 47.
# ---------------------------------------------------------------------------
p = 47


def equations(s: int, x: int, r: int) -> tuple[int, int, int]:
    Y = (11 - 9 * s) % p
    N = ((x + 2) ** 2 * (2025 * s * s * x * x + Y * Y) + 10780 * x * x) % p
    A = (225 * s * x * x + 9 * s - 11) % p
    O = (
        r * (4 * A * A - x * Y * Y * (99 * x - 4))
        + 2 * x * Y * Y * (x + 2)
    ) % p
    G = (55 * r * r * (x + 2) ** 2 - 49 * x * x) % p
    return N, O, G


def jacobian_det(s: int, x: int, r: int) -> int:
    """Exact polynomial derivative determinant modulo 47."""
    Y = (11 - 9 * s) % p
    A = (225 * s * x * x + 9 * s - 11) % p
    B = (99 * x - 4) % p
    W = (2025 * s * s * x * x + Y * Y) % p

    N_s = ((x + 2) ** 2 * (4050 * s * x * x - 18 * Y)) % p
    N_x = (
        2 * (x + 2) * W
        + (x + 2) ** 2 * (4050 * s * s * x)
        + 21560 * x
    ) % p

    A_s = (225 * x * x + 9) % p
    A_x = (450 * s * x) % p
    O_s = (
        r * (8 * A * A_s + 18 * x * Y * B)
        - 36 * x * Y * (x + 2)
    ) % p
    O_x = (
        r * (8 * A * A_x - Y * Y * (198 * x - 4))
        + 4 * Y * Y * (x + 1)
    ) % p
    O_r = (4 * A * A - x * Y * Y * B) % p

    G_x = (110 * r * r * (x + 2) - 98 * x) % p
    G_r = (110 * r * (x + 2) ** 2) % p

    # Matrix rows are (N_s,N_x,0), (O_s,O_x,O_r), (0,G_x,G_r).
    return (N_s * (O_x * G_r - O_r * G_x) - N_x * O_s * G_r) % p


# Brute-force all unit solutions and apply genuine source/f-side boundaries.
solutions = []
for s in range(1, p):
    Y = (11 - 9 * s) % p
    if Y == 0:
        continue
    y = Y * pow(s, -1, p) % p
    for x in range(1, p):
        if (x + 2) % p == 0:
            continue
        for r in range(1, p):
            if equations(s, x, r) != (0, 0, 0):
                continue
            f_line = (r * (x + 2) + 2 * x) % p
            source_line = ((99 * x - 4) * r - 2 * x - 4) % p
            n0 = (2025 * x * x + y * y) % p
            dsrc = (2025 * x * x - 9 * y) % p
            delta0 = (2025 * x * x - 18 * y - y * y) % p
            if 0 in (f_line, source_line, n0, dsrc, delta0):
                continue
            solutions.append((s, x, y, r, f_line, source_line, n0, dsrc, delta0))

expected = [
    (6, 1, 32, 39, 25, 33, 41, 45, 2),
    (11, 34, 39, 40, 4, 35, 35, 43, 4),
    (46, 15, 27, 35, 14, 7, 31, 46, 14),
]
assert solutions == expected

assert [jacobian_det(s, x, r) for s, x, _y, r, *_ in solutions] == [21, 35, 35]

# Decimal multiplicative orbit.
assert multiplicative_order(10, 47) == 46
orbit_n = {}
value = 36 % 47
for n in range(46):
    orbit_n[value] = n
    value = value * 10 % 47

assert [orbit_n[s] for s, *_ in solutions] == [44, 23, 19]
assert [orbit_n[s] + 1 for s, *_ in solutions] == [45, 24, 20]

# Non-Wieferich first lift: 10 remains a generator on all 47^k levels.
assert pow(10, 46, 47 * 47) == 1 + 43 * 47

# Center allocation modulo 47 after removing the common unit scale.
assert xi_minus % 47 == 25
assert xi_center % 47 == 0
assert xi_plus % 47 == 39
assert (-25) % 47 != 0
assert 39 % 47 != 0
assert ((-17) * 39 + (-19) * (-25)) % 47 == 0

print("external secant center certificate: OK")
