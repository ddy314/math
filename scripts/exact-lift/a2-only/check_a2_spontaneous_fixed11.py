#!/usr/bin/env python3
"""Finite F_11 certificate for spontaneous-fixed11-audit.md."""

P=11

def inv(a):
    return pow(a%P,-1,P)

def asp(x,y):
    d=(225*x*x-y)%P
    return (4*d*d-x*y*y*(99*x-4))%P

def aminus(x,y):
    return (asp(x,y)-2*y*y*(x+2)*(x+2))%P

def cstar(x,y):
    return (
        164025*x**4+656100*x**3+2381*x*x*y*y+41400*x*x*y
        +842400*x*x+324*x*y*y+324*y*y
    )%P

def delta0(x,y):
    return (2025*x*x-18*y-y*y)%P

sol=[]
for tau in (1,10):
    for x in range(1,P):
        if (x+2)%P==0:
            continue
        for y in range(1,P):
            d=(225*x*x-y)%P
            A=asp(x,y)
            nbar=(2025*x*x+y*y)%P
            if d==0 or A==0 or nbar==0:
                continue
            wb=(-A*inv(2*y*y*(x+2)))%P
            if wb==0:
                continue
            rs=(x*inv(wb))%P
            phi=((99*x-4)*rs-2*x-4)%P
            fline=(rs*(x+2)+2*x)%P
            if phi==0 or fline==0:
                continue
            s=(9+y)%P
            den=(2*x*x*(2*s-9*tau))%P
            if den==0:
                continue
            num=(x*x*(s*s-18*s*tau+55*tau*tau)
                 -(x+2)*(x+2)*nbar*inv(100))%P
            zb=(num*inv(den))%P
            lhs=(x*x*wb*wb*(s+zb)*(s+zb))%P
            rhs=((x+2+wb)*(x+2+wb)
                 *((nbar*inv(100)*wb*wb+x*x*zb*zb)%P))%P
            if lhs!=rhs:
                continue
            if (s+zb)%P==0:
                continue
            D0=delta0(x,y)
            Am=aminus(x,y)
            Cs=cstar(x,y)
            if D0==0 or Am==0 or Cs==0:
                continue
            deriv=(110*tau+18*(zb-s))%P
            sol.append((tau,x,y,wb,zb,deriv))

expected=[
(1,1,2,7,8,1),
(1,5,2,3,9,8),
(1,7,9,5,5,8),
(1,8,6,7,3,4),
(1,10,10,7,2,2),
(10,1,2,7,3,10),
(10,2,6,3,5,7),
(10,4,7,2,2,1),
(10,4,9,3,10,10),
(10,5,2,3,2,3),
(10,6,10,6,7,4),
(10,7,4,5,8,9),
]
assert sol==expected
assert all(row[-1] for row in sol)

# The decimal exponent has order 2 mod 11 and lifts normally because
# v_11(10^2-1)=1.
assert pow(10,2,11)==1 and 10%11!=1
n=10**2-1
v=0
while n%11==0:
    n//=11
    v+=1
assert v==1

print("OK: A2 fixed 11 spontaneous audit certified (12 simple states)")
