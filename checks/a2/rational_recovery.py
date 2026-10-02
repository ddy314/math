#!/usr/bin/env python3
"""Exact audit for A2-G16.  This does not prove that A2 is empty."""
from fractions import Fraction as Q
from math import gcd
import sympy as s


def need(ok: bool, msg: str) -> None:
    if not ok:
        raise AssertionError(msg)


def polynomial(n, k, z):
    return (31*n*n - 60*z*n*k + (1 + Q(31,4)*z*z)*k*k
            - 120*z**3*k + Q(17856,25)*z**4)


def recovery(n, k, z):
    return 120*z**3 + 60*n*z - (1 + Q(31,2)*z*z)*k


def e13_witness() -> None:
    z=10**13
    r0,s0=83674539967313,273127390353400
    S=816*z*z-31
    need(r0*r0+s0*s0==S,"E=13 sum of squares")
    t=Q(-4,9)
    rho=(r0*(1-t*t)-2*s0*t)/(1+t*t)
    sigma=(s0*(1-t*t)+2*r0*t)/(1+t*t)
    need(rho*rho+sigma*sigma==S,"rational rotation")
    D=2639*z*z-124; V=Q(2976,5)*z*z
    X=sigma*V/(50*z-4*rho); Y=rho*V-4*sigma*X
    k=(Y-7440*z**3)/D; n=(X+30*z*k)/31
    a=recovery(n,k,z)/93
    need(polynomial(n,k,z)==0,"elimination polynomial")
    need(Q(24,25)*z*z<n<z*z,"N window")
    need(5*z<k<Q(174,31)*z,"k window")
    need(z**3<a<Q(21,20)*z**3,"a window")
    need(n.denominator>1 and k.denominator>1 and a.denominator>1,"noninteger witness")
    M=Q(12,5)*z*z; b=Q(4,5)*z**3
    alpha=20*z**5+10*n*z**3+a; beta=Q(62,5)*z**5+Q(4,5)*z**3
    need((alpha/beta)**2==4+(n/M)**2+(a/b)**2,"original numerical word/sphere")
    r2=n/M; r3=a/b
    need(len(str(r2.numerator))-len(str(r2.denominator))==0,"reduced s2")
    need(len(str(r3.numerator))-len(str(r3.denominator))==0,"reduced s3")
    aa=int("2"+str(r2.numerator)+str(r3.numerator))
    bb=int("1"+str(r2.denominator)+str(r3.denominator))
    need(Q(aa,bb)**2!=4+r2*r2+r3*r3,"reduction is not an original solution")


def symbolic() -> None:
    beta,t1,t2,t3,x,y=s.symbols("beta t1 t2 t3 x y")
    C=beta+t3; delta=t1*t1+t2*t2+t3*t3-beta*beta
    need(s.expand((C*x-t1)**2+(C*y-t2)**2-delta
                  -C*(C*(x*x+y*y)-2*t1*x-2*t2*y+beta-t3))==0,"rational circle")
    z,n,k,v=s.symbols("z N k v")
    P=31*n*n-60*z*n*k+(1+s.Rational(31,4)*z*z)*k*k-120*z**3*k+s.Rational(17856,25)*z**4
    L=120*z**3+60*n*z-(1+s.Rational(31,2)*z*z)*k
    need(s.expand(k*(3*L/93+z*z*k/4)-s.Rational(576,25)*z**4-n*n+P/31)==0,"integer recovery")
    D=2639*z*z-124; S=816*z*z-31
    X=31*n-30*z*k; Y=D*k+7440*z**3; V=s.Rational(2976,5)*z*z
    need(s.expand(Y*Y+(50*z*X)**2-S*(V*V+(4*X)**2)+124*D*P)==0,"ray norm")
    actual=(10*z**5)**2+(24*z**5)**2+(s.Rational(4,5)*z**3)**2-(s.Rational(62,5)*z**5+s.Rational(4,5)*z**3)**2
    need(s.expand(actual-s.Rational(16,25)*z**8*S)==0,"denominator norm factor")
    R=5*((20+10*s.Rational(49,50))*z*z+v)/(2*(31*z*z+2))
    F=R*R-4-s.Rational(49,120)**2-(5*v/4)**2
    f1=(640139*z**4-4866124*z*z-240004)/(14400*(31*z*z+2)**2)
    f2=-(6304669*z**4+19535596*z*z+960016)/(57600*(31*z*z+2)**2)
    df=-5*z*z*(4805*v*z*z+620*v-596)/(8*(31*z*z+2)**2)
    need(s.factor(F.subs(v,1)-f1)==0,"real arc lower")
    need(s.factor(F.subs(v,s.Rational(21,20))-f2)==0,"real arc upper")
    need(s.factor(s.diff(F,v)-df)==0,"real arc derivative")
    need(s.Poly(100*P-100*k*(k+2*z*n+4*z**3),n,k,z,modulus=31).is_zero,"mod31 P")
    need(s.Poly(2*L+2*(k+2*z*n+4*z**3),n,k,z,modulus=31).is_zero,"mod31 L")
    w=s.symbols("w")
    need(s.Poly(s.expand(2*L).subs(z,3*w+1),n,k,w,modulus=3).is_zero,"mod3 L")
    q=s.Poly(s.expand((L+k).subs(z,10*w)),n,k,w)
    need(all(int(c)%10==0 for c in q.coeffs()),"mod10 unit preservation")


if __name__ == "__main__":
    e13_witness(); symbolic()
    print("PASS: A2-G16 rational circle, strict real arc, E=13 noninteger witness, integer recovery")
    print("STATUS: full A2 emptiness remains open")
