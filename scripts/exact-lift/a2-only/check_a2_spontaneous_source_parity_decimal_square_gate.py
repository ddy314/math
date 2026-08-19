#!/usr/bin/env python3
"""Certificate for spontaneous-source-parity-decimal-square-gate.md."""

import math

# Local exponent recovery after deleting b3^2 common square scale.
for ell in range(0,8):
    for k in range(0,8):
        vG=2*ell+k
        vb=2*ell
        vfree=vG-min(vG,vb)
        assert vfree==k

# Ceiling half-depth shape.
for k in range(1,20):
    assert 2*((k+1)//2)>=k

print("OK: A2 decimal G_free exactly recovers generic source common depth")
