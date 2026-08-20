#!/usr/bin/env python3
"""Mechanical checks for high-funnel-qz-projective-allocation.md."""

from __future__ import annotations


def local_projective_pay() -> None:
    # c <= r, z0=max(0,r+omega-alpha). Verify c<=z0+alpha.
    for c in range(0, 10):
        for r in range(c, 12):
            for omega in range(0, 8):
                for alpha in range(0, 14):
                    z0 = max(0, r + omega - alpha)
                    assert c <= z0 + alpha


def combined_allocation() -> None:
    # Abstract exponents: if 2s <= gamma+2c and c<=z0+alpha,
    # then 2s <= gamma+2z0+2alpha.
    for s in range(0, 10):
        for gamma in range(0, 20):
            for c in range(0, 10):
                if 2 * s > gamma + 2 * c:
                    continue
                for z0 in range(0, 10):
                    for alpha in range(0, 10):
                        if c <= z0 + alpha:
                            assert 2 * s <= gamma + 2 * z0 + 2 * alpha


def main() -> None:
    local_projective_pay()
    combined_allocation()
    print("DD high-funnel q-Z projective allocation checks passed")


if __name__ == "__main__":
    main()
