#!/usr/bin/env python3
"""Exact certificate for spontaneous-cross-sign-sphere.md."""

import sympy as sp

x,y,z=sp.symbols("x y z")
s=9+y
n=(2025*x**2+y**2)/100
d=225*x**2-y
Asp=4*d**2-x*y**2*(99*x-4)
W=sp.factor(Asp/(2*y**2*(x+2)))

S=sp.expand(
    x**2*W**2*(s+z)**2
    -(x+2+W)**2*(n*W**2+x**2*z**2)
)

disc=sp.factor(sp.discriminant(S,z))
H=202500*x**4-99*x**2*y**2-1800*x**2*y+4*x*y**2+4*y**2
Hv=sp.expand(H+2*y**2*(x+2)**2)
X=(
    205031250*x**6+2025*x**4*y**2-1822500*x**4*y
    +8100*x**3*y**2-99*x**2*y**4-1800*x**2*y**3
    +4050*x**2*y**2+4*x*y**4+4*y**4
)
expected=sp.factor(-x**2*H**2*Hv**2*X/(200*y**10*(x+2)**4))
assert sp.factor(disc-expected)==0

H2=(
    410062500*x**6-402975*x**4*y**2-7290000*x**4*y
    +8100*x**3*y**2+101*x**2*y**4+3600*x**2*y**3
    +40500*x**2*y**2+4*x*y**4+4*y**4
)
Dcross=2025*x**2-2*y**2-27*y
assert sp.factor(X-(H2-50*x**2*Dcross**2))==0
assert sp.factor(2*(X-H2)+100*x**2*Dcross**2)==0

# Exact coarse endpoint lower bound from the proof.
lb1=sp.Rational(459675,20000)
lb2=sp.Rational(2961,100)*sp.Rational(249,250)**2
lb3=4*sp.Rational(249,250)**4*sp.Rational(11,10)
lb=sp.factor(lb1+lb2+lb3)
assert lb==sp.Rational(2214350196669,39062500000)
assert lb>56

# Check the three-block decomposition of X.
Xsplit=sp.expand(
    x**4*(205031250*x**2-1822500*y+2025*y**2)
    +x**2*y**2*(8100*x-99*y**2-1800*y+4050)
    +4*y**4*(x+1)
)
assert sp.expand(X-Xsplit)==0

print("OK: A2 cross-sign sphere quadratic gate certified")
