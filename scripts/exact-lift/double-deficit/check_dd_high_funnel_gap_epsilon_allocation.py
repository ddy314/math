#!/usr/bin/env python3
"""Mechanical valuation checks for gap-epsilon allocation."""

from __future__ import annotations


def common_to_lambda() -> None:
    # t=min(A,E), lambda_depth + H_depth >= t.
    # If lambda_depth<t then H_depth>0. Meanwhile q0 has depth
    # eta+E-lambda_depth >0, contradicting gcd(H0,q0)=1.
    for A in range(12):
        for E in range(12):
            t = min(A, E)
            for lam in range(12):
                for hp in range(12):
                    if lam + hp < t:
                        continue
                    for eta in range(8):
                        q0 = eta + E - lam
                        if q0 < 0:
                            continue
                        primitive_ok = not (hp > 0 and q0 > 0)
                        if primitive_ok:
                            assert lam >= t


def exclusive_to_g0() -> None:
    # From A*G0 = E*mu0^2 with gcd(A,E)=1, E|G0 primewise.
    for a in range(10):
        for e in range(10):
            if min(a, e) != 0:
                continue
            for vm in range(10):
                # valuation equality a+g=e+2vm
                g = e + 2 * vm - a
                if g < 0:
                    continue
                assert g >= e


def main() -> None:
    common_to_lambda()
    exclusive_to_g0()
    print("DD gap-epsilon allocation checks passed")


if __name__ == "__main__":
    main()
