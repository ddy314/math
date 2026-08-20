#!/usr/bin/env python3
"""Audit the numerical safety constants in the A1 near-integer tail lemma.

This is not a finite-search proof.  The analytic proof is in
`docs/proofs/exact-lift/branches/a1-only/near-integer-tail.md`.
The script only checks, with exact rational arithmetic, that the decimal
coarsenings used there dominate the endpoint bounds for k>=3.
"""

from fractions import Fraction as F


def main() -> None:
    eps = F(1, 10**6)  # maximal epsilon = 10^(-2k) at k=3
    delta = F(1, 1000)  # maximal delta = 10^(-k) at k=3

    # Exact decimal constants used by the note.
    c001 = F(1, 100)
    x_max = F(2)
    sigma_max = F(1)

    # lambda/epsilon < 0.01(1 + 0.391 epsilon)
    lhs_factor = F(1, 1) / (F(1) - F(39, 100) * eps)
    rhs_factor = F(1) + F(391, 1000) * eps
    assert lhs_factor < rhs_factor

    # Lower first-source proxy:
    # 0.01 (X - 0.301 sigma eps) (2 - 0.3 eps)
    lower_proxy = (
        c001
        * (x_max - F(301, 1000) * sigma_max * eps)
        * (F(2) - F(3, 10) * eps)
    )
    lower_claim = F(1, 50) * x_max - F(121, 10000) * eps
    assert lower_proxy > lower_claim

    # Upper first-source proxy:
    # 0.01(1+0.391 eps)(X+0.869 eps)(2+0.868 eps)
    upper_proxy = (
        c001
        * (F(1) + F(391, 1000) * eps)
        * (x_max + F(869, 1000) * eps)
        * (F(2) + F(217, 250) * eps)
    )
    upper_claim = F(1, 50) * x_max + F(63, 1250) * eps
    assert upper_proxy < upper_claim

    # The remaining positive sources fit inside 0.958 eps + 1.189 eps^2,
    # so the full upper excess margin is safely < 1.009 eps.
    remainder = F(479, 500) * eps + F(1189, 1000) * eps * eps
    assert F(63, 1250) * eps + remainder < F(1009, 1000) * eps

    # u bounds from the note.
    lower_u_margin = (
        F(5) * F(121, 10000) + F(82, 1000) + F(8, 5)
    )
    upper_u_margin = F(5) * F(1009, 1000)
    assert lower_u_margin == F(697, 400)  # 1.7425
    assert upper_u_margin == F(1009, 200)  # 5.045

    # Scale back to q = j - 10^k - rho + 1 at the worst k=3 endpoint.
    lower_q = F(10) * lower_u_margin * eps / delta
    upper_q = F(10) * upper_u_margin * eps / delta
    assert lower_q < F(7, 400)  # 0.0175
    assert upper_q < F(101, 2000)  # 0.0505

    print("A1 near-integer constant audit OK")
    print(f"worst lower magnitude = {float(lower_q):.9f}")
    print(f"worst upper magnitude = {float(upper_q):.9f}")


if __name__ == "__main__":
    main()
