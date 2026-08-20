#!/usr/bin/env python3
from __future__ import annotations

import sympy as sp


def main() -> None:
    gamma, mu, G0, fiveT, s, a, c3 = sp.symbols(
        "gamma mu G0 fiveT s a c3", nonzero=True
    )
    lhs = gamma * mu**2 / G0
    rhs = fiveT * a * gamma / (s * c3)
    cleared = sp.factor((lhs - rhs) * (s * c3 * G0 / gamma))
    assert cleared == s * c3 * mu**2 - fiveT * a * G0

    c, a0, eps = sp.symbols("c a0 eps", nonzero=True)
    raw = fiveT * (c * a0) * G0 - s * (eps * c) * mu**2
    primitive = fiveT * a0 * G0 - s * eps * mu**2
    assert sp.expand(raw - c * primitive) == 0
    print("DD gap square-core checks passed")


if __name__ == "__main__":
    main()
