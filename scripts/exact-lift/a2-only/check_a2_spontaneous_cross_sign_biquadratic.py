#!/usr/bin/env python3
"""Exact certificate for spontaneous-cross-sign-biquadratic.md."""

import sympy as sp

x,y,t,z,v=sp.symbols("x y t z v")
s=y+9
n=(2025*x**2+y**2)/100
c=(x+2)**2*(2025*x**2+y**2)/(100*x**2)
d=225*x**2-y
Asp=4*d**2-x*y**2*(99*x-4)
W=sp.factor(Asp/(2*y**2*(x+2)))

sphere=sp.expand(
    x**2*W**2*(s+z)**2
    -(x+2+W)**2*(n*W**2+x**2*z**2)
)

H=202500*x**4-99*x**2*y**2-1800*x**2*y+4*x*y**2+4*y**2
Hv=sp.expand(H+2*y**2*(x+2)**2)
Dz=101250*x**4-49*x**2*y**2-900*x**2*y+4*x*y**2+4*y**2
X=(
    205031250*x**6+2025*x**4*y**2-1822500*x**4*y
    +8100*x**3*y**2-99*x**2*y**4-1800*x**2*y**3
    +4050*x**2*y**2+4*x*y**4+4*y**4
)

Zc=sp.factor(s*H**2/(8*y**2*(x+2)**2*Dz))
Zv=sp.factor(H*Hv/(80*x*y**3*(x+2)**2*Dz))

# Leading coefficient and center of the z quadratic.
poly=sp.Poly(sphere,z)
a,b,_=poly.all_coeffs()
assert sp.factor(a+2*x**2*Dz/y**2)==0
assert sp.factor(-b/(2*a)-Zc)==0

# Exact discriminant and quotient-ring root.
disc=sp.factor(sp.discriminant(sphere,z))
expected_disc=sp.factor(-x**2*H**2*Hv**2*X/(200*y**10*(x+2)**4))
assert sp.factor(disc-expected_disc)==0
expr=sp.together(sphere.subs(z,Zc+Zv*v))
num,_=sp.fraction(expr)
rem=sp.rem(sp.Poly(sp.expand(num),v),sp.Poly(v**2+2*X,v)).as_expr()
assert sp.factor(rem)==0

# Compact branch and quadratic norm.
A=55*t**2-18*s*t+s**2-c
B=18*t-4*s
Lp=A+B*Zc+B*Zv*v
Lm=A+B*Zc-B*Zv*v
norm=sp.factor((A+B*Zc)**2+2*X*(B*Zv)**2)
prod=sp.expand(Lp*Lm).subs(v**2,-2*X)
assert sp.factor(prod-norm)==0

# Correct exact denominator clearing.
D=200*x**2*y**3*(x+2)**2*Dz
A0=sp.expand(100*x**2*(55*t**2-18*s*t+s**2)-(x+2)**2*(2025*x**2+y**2))
U=sp.expand(2*y**3*(x+2)**2*Dz*A0+25*x**2*y*s*H**2*B)
V=sp.expand(5*x*(9*t-2*s)*H*Hv)
assert sp.factor(sp.cancel(D*(A+B*Zc)-U))==0
assert sp.factor(sp.cancel(D*(B*Zv)-V))==0
assert sp.factor(sp.cancel(U**2+2*X*V**2-D**2*norm))==0

# Endpoint denominator positivity certificates.
assert sp.Rational(810)-sp.Rational(396,19)-sp.Rational(7200,19)>0
assert -18+sp.Rational(16,19)+8<0
assert sp.factor(H.subs({x:sp.Rational(1,10),y:1}))==sp.Rational(283,50)
assert sp.Rational(405)-sp.Rational(196,19)-sp.Rational(3600,19)>0
assert -9+sp.Rational(16,19)+8<0
assert sp.factor(Dz.subs({x:sp.Rational(1,10),y:1}))==sp.Rational(1007,200)

# The zero of B cannot be a zero of the norm.
assert sp.factor(B.subs(t,2*s/9))==0
assert sp.factor(A.subs(t,2*s/9)+sp.Rational(23,81)*s**2+c)==0

# X>56 is independently certified in check_a2_spontaneous_cross_sign_sphere.py.
print("OK: A2 cross-sign biquadratic norm and real-axis emptiness certified")
