#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-theta-p3-filter.md."""

p = 23
p3 = p**3


def plus_rho(kappa):
    den = (1 + 14 * kappa) % p
    if den == 0:
        return None
    return (-11 * pow(den, -1, p)) % p


def minus_rho(kappa):
    den = (1 + 14 * kappa) % p
    if den == 0:
        return None
    return ((9 + 18 * kappa) * pow(den, -1, p)) % p


def data(lam, cu):
    M = 2 * lam
    j = ((M - 16) // 22) % p
    hN = (5 + 3 * j) % p
    kappa = ((16 * hN + 22) * pow(9, -1, p)) % p
    assert kappa not in (11, 18)

    g0 = (
        -pow(5, 2 * lam, p)
        * pow((pow(2, lam + 1, p) * (cu % p)) % p, -1, p)
    ) % p
    L = (pow(2, lam + 1, p3) * pow(5, lam, p3) * (cu % p3)) % p3

    rows = []
    for name, rho in (("plus", plus_rho(kappa)), ("minus", minus_rho(kappa))):
        assert rho is not None
        if name == "plus":
            assert rho not in (0, p - 2)
        else:
            assert rho != 0
        omega0 = (cu * (rho + 1) * pow(g0, -1, p)) % p
        theta0 = (-L + 3 * p * p * omega0) % p3
        # Exact source-only alternative formula for omega0.
        omega_alt = (
            -pow(2, lam + 1, p)
            * (cu % p) ** 2
            * (rho + 1)
            * pow(pow(5, 2 * lam, p), -1, p)
        ) % p
        assert omega0 == omega_alt
        rows.append((name, rho, omega0, theta0))
    return kappa, rows

expected = {
    (52, 29): (2, {"plus": 2713, "minus": 6945}),
    (63, 337): (15, {"plus": 9053, "minus": 3763}),
    (74, 3917): (5, {"plus": 731, "minus": 202}),
    (74, 3929): (5, {"plus": 5444, "minus": 10734}),
}

for key, (want_kappa, want_theta) in expected.items():
    kappa, rows = data(*key)
    assert kappa == want_kappa
    got = {name: theta0 for name, rho, omega0, theta0 in rows}
    assert got == want_theta

# Simultaneous-gate source ratio rho=-1 makes omega0=0 and theta=-L mod p^3.
lam, cu = 151, 1  # M=302 mod506; source-content value is synthetic for identity check.
M = 2 * lam
j = ((M - 16) // 22) % p
hN = (5 + 3 * j) % p
kappa = ((16 * hN + 22) * pow(9, -1, p)) % p
assert kappa == 4
assert plus_rho(kappa) == minus_rho(kappa) == p - 1

print("OK: A2 fixed-23 c2 theta mod23^3 source/orientation filter certified")
