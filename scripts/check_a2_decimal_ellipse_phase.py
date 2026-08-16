#!/usr/bin/env python3
"""Exact symbolic checks for A2 decimal ellipse phase compression.

The script verifies the scale-free identities and the five rational angle caps
recorded in docs/proofs/exact-lift/branches/a2-decimal-ellipse-phase.md.
"""

import sympy as sp


def main() -> None:
    x, y, z, a = sp.symbols("x y z a", positive=True)

    phi = (99*x - 4)*z - 2*x - 4
    gamma = z*(x + 2) + 2*x
    r = sp.factor(x*phi / ((x + 2)*gamma))
    r0 = sp.factor(x*(99*x - 4)/(x + 2)**2)

    err = sp.factor(r0 - r)
    expected_err = sp.factor(
        8*x*(25*x**2 + 1) / ((x + 2)**2 * gamma)
    )
    assert sp.factor(err - expected_err) == 0

    assert sp.expand(x*phi + (x + 2)*gamma - 4*z*(25*x**2 + 1)) == 0

    jratio = (25*a*x**2 - y)/(5*x*(a + y))
    H = sp.factor((r0 - jratio**2)/(1 + r0))
    H1 = sp.factor(H.subs(y, 1))
    expected_H1 = -(
        25*a**2*x**4 + 100*a**2*x**3
        - (200*a + 99)*x**2 + 4*x + 4
    ) / (100*x**2*(a + 1)**2)
    assert sp.factor(H1 - expected_H1) == 0

    dH1 = sp.factor(sp.diff(H1, x))
    expected_dH1 = -(x + 2)*(25*a**2*x**3 - 2)/(50*x**3*(a + 1)**2)
    assert sp.factor(dH1 - expected_dH1) == 0

    # Exact core windows and safe rational T/A caps.
    cores = {
        5:  (sp.Rational(27,250), sp.Rational(3,16), sp.Rational(3,8)),
        7:  (sp.Rational(1,10), sp.Rational(7,40), sp.Rational(31,100)),
        9:  (sp.Rational(1,10), sp.Rational(3,20), sp.Rational(13,50)),
        11: (sp.Rational(1,10), sp.Rational(1,8), sp.Rational(21,100)),
        13: (sp.Rational(1,10), sp.Rational(11,100), sp.Rational(1,6)),
    }

    for av, (lo, hi, cap) in cores.items():
        diff = sp.factor(cap**2 - H1.subs(a, av))
        num, den = sp.together(diff).as_numer_denom()
        P = sp.Poly(num, x, domain=sp.QQ)

        # No zero in the legal x interval; positivity at one endpoint then
        # proves the cap on the whole interval.
        roots = sp.polys.polytools.count_roots(P, lo, hi)
        assert roots == 0, (av, roots)
        assert sp.sign(P.eval(lo)) > 0
        assert den.subs(x, lo) > 0 and den.subs(x, hi) > 0

        eta = sp.factor((1-cap)/(1+cap))
        print(f"a={av}: T/A < {cap}, (A-T)/(A+T) > {eta}")

    print("A2 decimal ellipse phase identities: OK")


if __name__ == "__main__":
    main()
