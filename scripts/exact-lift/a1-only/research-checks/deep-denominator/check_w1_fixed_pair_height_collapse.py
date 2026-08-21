#!/usr/bin/env python3
"""Audit the height collapse forced by the w=1 fixed pair (u,v)=(27,23).

Written proof skeleton (all variables are those of the A1 2-high master):

    54*beta - 23*alpha = 5**d,
    alpha = 7*5**d + 54*m,
    beta  = 3*5**d + 23*m,

and, with s=b1/27 and

    R=(5*s+3)/23=(50*T**2+76)/621,

we have

    5**d*R + m = 2**c*n0.                      (1)

On the top endpoint delta=D/T**2 >= 12, while B<=Y<k+1.  Hence eta>k,
so c=k+1+eta+nu2 > 2*k+1.  Multiplying (1) by 621 gives

    621*m + 76*5**d
      = 621*2**c*n0 - 50*5**d*T**2.

The two terms on the right have 2-adic valuations c and 2*k+1,
respectively.  Therefore

    v2(621*m + 76*5**d) = 2*k+1.               (2)

The endpoint scale identity

    r10/25**d = (7+54*x)*(3+23*x),  x=m/5**d,
    delta*xi = 200*r10/25**d,

combined with delta<10001/621 and xi<15_214_000 gives x<32.  Thus (2)
implies

    2**(2*k+1) < 19948*5**d.

Since d=k+1-Y,

    Y < (1-2*log_5(2))*k
        + 1-log_5(2)+log_5(19948)
      < 0.139*k + 7,

and hence

    d > 0.861*k - 6.

This is an unbounded analytic reduction.  The computations below only audit
the numerical constants and short identities; they are not the proof itself.
"""

from __future__ import annotations

from decimal import Decimal, getcontext

getcontext().prec = 80


def log_decimal(x: Decimal, base: Decimal) -> Decimal:
    return x.ln() / base.ln()


def main() -> None:
    # The normalized product is increasing for x>=0.
    def product(x: Decimal) -> Decimal:
        return (Decimal(7) + Decimal(54) * x) * (
            Decimal(3) + Decimal(23) * x
        )

    delta_cap = Decimal(10001) / Decimal(621)
    xi_cap = Decimal(15_214_000)
    normalized_cap = delta_cap * xi_cap / Decimal(200)

    assert product(Decimal(32)) > normalized_cap

    # A very weak lower scale already puts x on the positive branch.
    normalized_floor = Decimal(12) * Decimal(196_000) / Decimal(200)
    assert product(Decimal(0)) < normalized_floor

    bracket_constant = 621 * 32 + 76
    assert bracket_constant == 19_948

    log5_2 = log_decimal(Decimal(2), Decimal(5))
    coeff_y = Decimal(1) - Decimal(2) * log5_2
    const_y = (
        Decimal(1)
        - log5_2
        + log_decimal(Decimal(bracket_constant), Decimal(5))
    )

    assert coeff_y < Decimal("0.139")
    assert const_y < Decimal(7)

    # Clean consequence used in the written frontier.
    for k in (32, 52, 118, 500, 1000):
        sharp = coeff_y * Decimal(k) + const_y
        clean = Decimal("0.139") * Decimal(k) + Decimal(7)
        assert sharp < clean

    # The top strip automatically lies on the eta>0 / pure-2 side:
    # delta>=12 and B<=k imply 2^eta >= 1.5*5^k, hence eta>k.
    for k in range(1, 80):
        assert Decimal("1.5") * (Decimal(5) ** k) > Decimal(2) ** k

    print("w=1 fixed-pair height-collapse audit: OK")
    print("normalized product cap:", normalized_cap)
    print("P(32):", product(Decimal(32)))
    print("Y coefficient:", coeff_y)
    print("Y constant:", const_y)
    print("clean theorem: Y < 0.139*k + 7; d > 0.861*k - 6")


if __name__ == "__main__":
    main()
