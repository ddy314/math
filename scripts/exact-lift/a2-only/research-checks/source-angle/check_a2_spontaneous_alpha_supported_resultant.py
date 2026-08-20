#!/usr/bin/env python3
"""Exact certificate for spontaneous-alpha-supported-resultant.md."""

import sympy as sp

A,B,N,T,b = sp.symbols("A B N T b")
x,y = sp.symbols("x y")
Q=B+2*N
K=9*N+10*A
N0=sp.Rational(81,4)*B**2+A**2
U=(45*B**2-2*A*N)**2-A**2*B*(99*B-4*N)
O=T*U+2*A**2*Q*b
Cw=sp.expand(U-2*A**2*Q**2)
HO=sp.expand(N0*U**2+4*A**4*B**2*Q**2*K**2)
Salpha=sp.expand((T*Q+b)**2*(N0*b**2+B**2*T**2*K**2))

# Global alpha-supported resultant.
res=sp.factor(sp.resultant(O,Salpha,b))
assert sp.factor(res-T**4*Cw**2*HO)==0

# Three normalized prefix sheets.
Am=sp.expand(202500*x**4-(101*x**2+4*x+4)*y**2-1800*x**2*y)
H1=sp.expand(202500*x**4+101*x**2*y**2+4*x*y**2+4*y**2)
H2=sp.expand(
    410062500*x**6-402975*x**4*y**2-7290000*x**4*y
    +8100*x**3*y**2+101*x**2*y**4+3600*x**2*y**3
    +40500*x**2*y**2+4*x*y**4+4*y**4
)
P=101*x**2+4*x+4
R=101*x**2+4*x+8
Qx=2500*x**4+101*x**2+4*x+4

assert sp.factor(sp.resultant(Am,H1,y)) == 164025000000*x**8*P*R
assert sp.factor(sp.resultant(Am,H2,y)) == 672605015625000000*x**12*(x+2)**4*P*R
assert sp.factor(sp.resultant(H1,H2,y)) == 10761680250000000000*x**12*P*R*Qx

# P is a sum of two squares.
assert sp.expand(P-((10*x)**2+(x+2)**2))==0
assert sp.discriminant(P,x)==-1600

# R-collision is exactly the source first layer y=225x^2.
assert sp.factor(sp.discriminant(Am,y)-810000*x**4*R)==0
assert sp.factor(Am.subs(y,225*x**2)+50625*x**4*R)==0
assert sp.factor(H1.subs(y,225*x**2)-50625*x**4*R)==0
assert sp.factor(H2.subs(y,225*x**2)-102515625*x**6*(25*x**2+1)*R)==0

# H1/H2 collision remainder and quartic branch.
rem=sp.factor(sp.rem(H2,H1,y))
expected=7290000*x**4*(22500*x**4-(201*x**2+4*x+4)*y-900*x**2)/P
assert sp.factor(rem-expected)==0
L=201*x**2+4*x+4
ylin=sp.cancel(900*x**2*(25*x**2-1)/L)
sub=sp.factor(sp.together(H1.subs(y,ylin)))
expected_sub=202500*x**4*R*Qx/L**2
assert sp.factor(sub-expected_sub)==0

# On Qx=0, H1 gives y^2=81. y=-9 is exactly K=0.
assert sp.factor(H1.subs(y,-9)-81*Qx)==0
assert sp.factor(H2.subs(y,-9)-6561*(25*x**2+1)*Qx)==0
assert sp.factor(H1.subs(y,9)-81*Qx)==0
# For y=+9, H2=0 on Qx additionally requires L=0 modulo Qx.
rem_plus=sp.factor(sp.rem(sp.Poly(H2.subs(y,9),x),sp.Poly(Qx,x),domain=sp.QQ).as_expr())
assert rem_plus==52488*L
res_QL=int(sp.resultant(Qx,L,x))
assert sp.factorint(abs(res_QL))=={2:8,3:1,5:4,107:1,281:1}
# The only non-3 inert coincidence is p=107, and it lies on R/source.
p=107
roots=[xx for xx in range(p) if int(Qx.subs(x,xx))%p==0 and int(L.subs(x,xx))%p==0]
assert roots==[43]
assert int(R.subs(x,43))%p==0
assert 225*43*43%p==9
assert all(int(f.subs({x:43,y:9}))%p==0 for f in (Am,H1,H2))

print("OK: A2 alpha-supported global resultant and sheet collisions certified")
