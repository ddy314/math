#!/usr/bin/env python3
"""Exact certificate for spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md."""

p = 23


def kappa_for_lambda(lam: int) -> int:
    M = 2 * lam
    assert (M - 16) % 22 == 0
    j = ((M - 16) // 22) % p
    hN = (5 + 3 * j) % p
    return ((16 * hN + 22) * pow(9, -1, p)) % p


def rho_plus(kappa: int):
    den = (1 + 14 * kappa) % p
    if den == 0:
        return None
    return (-11 * pow(den, -1, p)) % p


def rho_minus(kappa: int):
    den = (1 + 14 * kappa) % p
    if den == 0:
        return None
    return ((9 + 18 * kappa) * pow(den, -1, p)) % p


def required_cu(lam: int, orientation: str):
    kappa = kappa_for_lambda(lam)
    factor = (
        pow(5, lam, p)
        * pow(pow(2, 2 * lam + 2, p), -1, p)
    ) % p
    if orientation == "plus":
        rho = rho_plus(kappa)
        if rho is None or rho in (0, p - 2):
            return None
        return ((rho + 2) * factor) % p
    if orientation == "minus":
        rho = rho_minus(kappa)
        if rho is None or rho == 0:
            return None
        return (rho * factor) % p
    raise ValueError(orientation)


# Direct algebraic high-2/source relation check for all genuine kappa roots.
for lam in range(8, 8 + 11 * 46, 11):
    kappa = kappa_for_lambda(lam)
    for orientation in ("plus", "minus"):
        cu = required_cu(lam, orientation)
        if cu is None:
            continue
        rho = rho_plus(kappa) if orientation == "plus" else rho_minus(kappa)
        q = rho * cu * pow(pow(5, lam, p), -1, p) % p
        q2 = 3 * pow(2, 2 * lam + 1, p) * q % p
        if orientation == "plus":
            assert rho * (rho + 2) % p == 16 * q2 % p
        else:
            assert rho * rho % p == 16 * q2 % p

# Low-height exact table.
rows = [
    # lambda, c_u, kappa, required plus, required minus, actual c_u mod23
    (52, 29, 2, 12, 11, 6),
    (63, 337, 15, 8, 15, 15),
    (74, 3917, 5, 1, 22, 7),
    (74, 3929, 5, 1, 22, 19),
]
for lam, cu, want_k, want_plus, want_minus, want_actual in rows:
    assert kappa_for_lambda(lam) == want_k
    assert required_cu(lam, "plus") == want_plus
    assert required_cu(lam, "minus") == want_minus
    assert cu % p == want_actual

# Height conclusions.
assert 29 % p not in (required_cu(52, "plus"), required_cu(52, "minus"))
assert 337 % p != required_cu(63, "plus")
assert 337 % p == required_cu(63, "minus")
for cu in (3917, 3929):
    assert cu % p not in (required_cu(74, "plus"), required_cu(74, "minus"))

# Forced depth-1 progressions in lambda.
assert kappa_for_lambda(85) == 18
assert kappa_for_lambda(118) == 11

print("OK: A2 fixed-23 c2 high-2/source-content mod23 synchronization certified")
