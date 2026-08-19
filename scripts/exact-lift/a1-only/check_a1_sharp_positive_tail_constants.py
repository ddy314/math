#!/usr/bin/env python3
"""Exact rational audit for sharp-positive-tail-window.md.

This is only a constant audit.  The analytic proof is the markdown note.
"""

from fractions import Fraction as F


TYPES = ((1, 1), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2))


def main() -> None:
    eps = F(1, 10**6)  # maximal epsilon for k>=3
    x_upper = F(2)     # strict X<2, safe endpoint for lower estimates

    lower_values: dict[tuple[int, int], F] = {}
    upper_values: dict[tuple[int, int], F] = {}

    phi1_upper = F(217, 500)

    for z, w in TYPES:
        c = 5 - z

        curvature_min = F(65, 100) if z == 1 else F(45, 100)
        lower_E_margin = curvature_min - F(121, 10000)

        # From
        # (10u-X)/eps > 50a_z-cw-0.1wX-5wa_z eps,
        # evaluated at the safe endpoints X=2 and eps=1e-6.
        lower = (
            F(50) * lower_E_margin
            - c * w
            - F(1, 10) * w * x_upper
            - F(5) * w * lower_E_margin * eps
        )
        lower_values[(z, w)] = lower

        phi2 = F(z, 10)
        curvature_max = (
            F(2) * phi1_upper
            + phi2 * phi2
            - phi1_upper * phi1_upper
        )
        upper_E_margin = F(63, 1250) + curvature_max

        # Drop all negative corrections in the exact residual formula.
        upper = (
            F(50) * upper_E_margin
            + F(50) * F(1189, 1000) * eps
            - c * w
        )
        upper_values[(z, w)] = upper

    global_lower = min(lower_values.values())
    global_upper = max(upper_values.values())

    assert global_lower > F(1509, 100)   # 15.09
    assert global_upper < F(39003, 1000) # 39.003

    assert min(lower_values, key=lower_values.get) == (1, 4)
    assert max(upper_values, key=upper_values.get) == (3, 1)

    for typ in TYPES:
        print(
            f"type={typ} lower>{float(lower_values[typ]):.9f} "
            f"upper<{float(upper_values[typ]):.9f}"
        )

    print(f"global lower > {float(global_lower):.9f} > 15.09")
    print(f"global upper < {float(global_upper):.9f} < 39.003")
    print("A1 sharpened positive-tail constant audit OK")


if __name__ == "__main__":
    main()
