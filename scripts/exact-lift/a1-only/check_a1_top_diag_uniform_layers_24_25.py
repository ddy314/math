#!/usr/bin/env python3
"""Exact extension of the A1 fixed-layer certificate to k=24,25.

This reuses the generic theorem-derived machinery in
check_a1_top_diag_uniform_layers.py.  It deliberately checks the older,
wider one-sided gap window 5.09..50.45; zero hits there a fortiori excludes
the sharpened 15.09..39.003 window.
"""

import check_a1_top_diag_uniform_layers as base


EXTRA_EXPECTED = {
    24: ((256, 256, 32, 64),    -26, -59, (-298, 216, -114, 45), 188712),
    25: ((2048, 48, 16, 512),   -27, -61, (-316, 224, -122, 47), 796197),
}


def run() -> None:
    base.EXPECTED.update(EXTRA_EXPECTED)
    for k in (24, 25):
        base.certify_layer(k)
    print("CERTIFICATE OK: A1 minimal diagonal k=g=24,25 is empty.")


if __name__ == "__main__":
    run()
