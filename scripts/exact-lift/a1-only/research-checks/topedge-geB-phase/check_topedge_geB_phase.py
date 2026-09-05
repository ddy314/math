#!/usr/bin/env python3
"""Exact certificate closing all A1 minimal-diagonal single-5 top-edge
states with v5(N)>=B after the theorem-derived finite-height collapse.

No factorization of b1 or Q is used.  The two 5-adic Hensel progressions
are counted against the exact 2^(3k) phase-gap interval by floor-sum.
"""

TYPES=[(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)]
KMAX={(1,1):77,(1,2):75,(1,3):74,(1,4):72,(3,1):74,(3,2):73}


def bmax(k:int)->int:
    return (2293*k+7569)//1000


def sqrt_minus_one_mod_5pow(m:int, cache={}):
    if m in cache:
        return cache[m]
    r=2; mod=5
    for _ in range(1,m):
        target=mod*5
        for t in range(5):
            cand=r+t*mod
            if (cand*cand+1)%target==0:
                r=cand; break
        else:
            raise AssertionError("Hensel lift failed")
        mod=target
    out=(r,(-r)%mod)
    cache[m]=out
    return out


def floor_sum(n:int,m:int,a:int,b:int)->int:
    ans=0
    while True:
        if a>=m:
            ans+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            ans+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:
            return ans
        n=y//m
        b=y%m
        m,a=a,m


def count_lt(n:int,m:int,a:int,b:int,c:int)->int:
    if c<=0: return 0
    if c>=m: return n
    return n-(floor_sum(n,m,a,b+m-c)-floor_sum(n,m,a,b))


def count_positive_below(n:int,m:int,a:int,b:int,limit:int)->int:
    if limit>m:
        return n
    return count_lt(n,m,a,b,limit)-count_lt(n,m,a,b,1)


def main()->None:
    progression_count=0
    raw_n0_count=0
    phase_hits=0

    for z,w in TYPES:
        alpha=15-z
        cphase=(339-40*w) if z==1 else (237-20*w)
        for k in range(32,KMAX[(z,w)]+1):
            T=10**k
            low=10**(k-1)
            high=10**k-1
            c1=10*(5-z-w)+1
            Aconst=100*T**3+c1*T-1
            C0=(10*T**2-z)*(10*T**2-w)
            mod2=2**(3*k)
            coeffL=10*T**2-alpha
            constL=-cphase*T

            for B in range(k+1,bmax(k)+1):
                d=B-k
                mod5=5**B
                epsmax=6*5**d
                factor=-(5**(d-1))

                for ii in sqrt_minus_one_mod_5pow(B):
                    # v5(N)>=B iff N=0 mod 5^B, with
                    # N=(Aconst+N0)^2+C0^2.
                    root=(-Aconst+C0*ii)%mod5
                    tmin=(low-root+mod5-1)//mod5
                    if tmin<0: tmin=0
                    tmax=(high-root)//mod5
                    if tmax<tmin: continue
                    n=tmax-tmin+1
                    progression_count+=1
                    raw_n0_count+=n

                    baseN=root+tmin*mod5
                    step=(factor*coeffL*mod5)%mod2
                    base=(factor*(coeffL*baseN+constL))%mod2

                    cnt=count_positive_below(n,mod2,step,base,epsmax)
                    phase_hits+=cnt

    assert progression_count==11853, progression_count
    assert raw_n0_count==216756621563705118896955, raw_n0_count
    assert phase_hits==0, phase_hits

    print("top-edge v5(N)>=B phase certificate")
    print("Hensel progressions:",progression_count)
    print("raw N0 states represented:",raw_n0_count)
    print("phase hits:",phase_hits)
    print("PASS")


if __name__=="__main__":
    main()
