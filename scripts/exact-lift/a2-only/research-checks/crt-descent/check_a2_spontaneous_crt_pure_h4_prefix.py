#!/usr/bin/env python3
"""Certificate for spontaneous-crt-pure-h4-prefix.md."""

import sympy as sp

x,y,u=sp.symbols('x y u')
d=225*x**2-y
Asp=4*d**2-x*y**2*(99*x-4)
Aminus=Asp-2*y**2*(x+2)**2
Aplus=202500*x**4+99*x**2*y**2-4*x*y**2-4*y**2
Delta0=2025*x**2-18*y-y**2
Gstar=(410062500*x**6-407025*x**4*y**2-7290000*x**4*y-8100*x**3*y**2
       +99*x**2*y**4+3600*x**2*y**3+24300*x**2*y**2-4*x*y**4-4*y**4)
Cstar=(164025*x**4+656100*x**3+2381*x**2*y**2+41400*x**2*y
       +842400*x**2+324*x*y**2+324*y**2)
den=400*x**2*y**3*(x+2)**2
z1=-Aplus*Asp/den
z2=Asp*Gstar/(den*Delta0)
s=9+y
h4=(-29520930816*u**4-46902675456*u**3+90353275489*u**2
    +114775877404*u+31476144004)

polys=[]
for zi,degree,terms in [(z1,32,137),(z2,40,272)]:
    num=sp.together(h4.subs(u,zi/s)).as_numer_denom()[0]
    content,prim=sp.primitive(sp.Poly(num,x,y).as_expr(),x,y)
    assert abs(int(content))==1
    P=sp.Poly(prim,x,y)
    assert P.total_degree()==degree
    assert len(P.terms())==terms
    fl=sp.factor_list(prim,x,y)
    assert fl[0] in (1,-1)
    assert len(fl[1])==1 and fl[1][0][1]==1
    assert sp.Poly(fl[1][0][0],x,y).total_degree()==degree
    for old in (d,Asp,Aminus,Aplus,Delta0,Cstar):
        assert sp.gcd(P,sp.Poly(old,x,y)).total_degree()==0
    polys.append(P)

# Source-line sanity: the full universal prefix resultant is not identically
# source-supported.  At the sphere-root level both z_i coincide there.
zsrc=9*x**2*(99*x-4)**2/(16*(x+2)**2)
assert sp.simplify((z1-zsrc).subs(y,225*x**2))==0
assert sp.simplify((z2-zsrc).subs(y,225*x**2))==0

# The low h4 source restriction is not identically zero either.
for P in polys:
    q=sp.Poly(P.as_expr().subs(y,225*x**2),x)
    assert not q.is_zero

print('OK: h4 gives two new irreducible pure-prefix curves, coprime to all principal old gates')
