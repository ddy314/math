#!/usr/bin/env python3
"""Exact certificate for spontaneous-pure-root-gap.md."""

import sympy as sp

x,y,t,u,v=sp.symbols("x y t u v")
s=y+9
d=225*x**2-y
Asp=4*d**2-x*y**2*(99*x-4)
Aminus=Asp-2*y**2*(x+2)**2
Delta=2025*x**2-18*y-y**2
Aplus=202500*x**4+99*x**2*y**2-4*x*y**2-4*y**2
Gstar=(
    410062500*x**6-407025*x**4*y**2-7290000*x**4*y-8100*x**3*y**2
    +99*x**2*y**4+3600*x**2*y**3+24300*x**2*y**2
    -4*x*y**4-4*y**4
)
den=400*x**2*y**3*(x+2)**2
z1=sp.cancel(-Aplus*Asp/den)
z2=sp.cancel(Asp*Gstar/(den*Delta))
c=(x+2)**2*(2025*x**2+y**2)/(100*x**2)

ztheta=(
    x**2*(s**2-18*s*t+55*t**2)
    -sp.Rational(1,100)*(x+2)**2*(2025*x**2+y**2)
)/(2*x**2*(2*s-9*t))

# Compact branch identity.
def L(z):
    return sp.expand(55*t**2+18*(z-s)*t+s**2-4*s*z-c)
for z in (z1,z2):
    assert sp.factor(L(z)-2*(2*s-9*t)*(ztheta-z))==0

# Known sphere-root ordering: z2-z1 has sign Aminus<0 on endpoint.
assert sp.factor(
    z2-z1-
    9*d*Aminus*Asp/(200*x**2*y**3*(x+2)**2*Delta)
)==0

# Gap at t=1.
ztheta1=sp.factor(ztheta.subs(t,1))
gap=sp.factor(ztheta1-z1)
assert sp.factor(gap.subs({x:sp.Rational(1,10),y:1})-sp.Rational(28283,3880800))==0
assert sp.factor(L(z1).subs({t:1,x:sp.Rational(1,10),y:1})-sp.Rational(28283,176400))==0

# Exact 2D Bernstein coefficient helper. If every coefficient is >0,
# the polynomial is >0 on the unit square.
def bernstein_coeffs(poly, xlo, xhi, ylo, yhi):
    mapped=sp.Poly(sp.expand(poly.subs({
        x:xlo+(xhi-xlo)*u,
        y:ylo+(yhi-ylo)*v,
    })),u,v)
    mx,my=mapped.degree(u),mapped.degree(v)
    a={(i,j):mapped.coeff_monomial(u**i*v**j)
       for i in range(mx+1) for j in range(my+1)}
    out=[]
    for k in range(mx+1):
        for l in range(my+1):
            val=sp.Rational(0)
            for i in range(k+1):
                for j in range(l+1):
                    val += a[(i,j)]*sp.Rational(sp.binomial(k,i),sp.binomial(mx,i))*sp.Rational(sp.binomial(l,j),sp.binomial(my,j))
            out.append(sp.factor(val))
    return mx,my,out

# Derivative denominators are positive on endpoint. Certify numerators.
dgx=sp.factor(sp.diff(gap,x))
dgy=sp.factor(sp.diff(gap,y))
numx,denx=sp.fraction(sp.together(dgx))
numy,deny=sp.fraction(sp.together(dgy))
assert sp.factor(denx-100*x**3*y**3*(x+2)**3*(2*y+9))==0
assert sp.factor(deny-400*x**2*y**4*(x+2)**2*(2*y+9)**2)==0

xmin,xmax=sp.Rational(1,10),sp.Rational(2,19)
ymin,ymax=sp.Rational(249,250),sp.Rational(1)
mx,my,bx=bernstein_coeffs(numx,xmin,xmax,ymin,ymax)
mx2,my2,by=bernstein_coeffs(-numy,xmin,xmax,ymin,ymax)
assert (mx,my)==(9,5)
assert (mx2,my2)==(8,6)
assert all(q>0 for q in bx)
assert all(q>0 for q in by)
assert min(bx)==sp.Rational(2307239659,400000)
assert min(by)==sp.Rational(121236551,2000)

# Therefore gap increases in x and decreases in y; boundary is global minimum.
assert sp.Rational(28283,3880800)>0

# At t=1: L_i = 2(2y+9)*(ztheta1-z_i), and z2<z1 in endpoint.
# The proof file combines this with the already-certified vertex > 12/5
# and positive discriminants from spontaneous-single-branch.md.
assert sp.factor(L(z1).subs(t,1)-2*(2*y+9)*(ztheta1-z1))==0
assert sp.factor(L(z2).subs(t,1)-2*(2*y+9)*(ztheta1-z2))==0

print("OK: A2 pure-spontaneous real roots are uniformly beyond tau=1")
