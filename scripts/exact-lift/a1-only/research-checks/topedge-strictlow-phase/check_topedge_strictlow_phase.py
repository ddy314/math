#!/usr/bin/env python3
"""Exact certificate closing the A1 minimal-diagonal single-5 top-edge
strict-5-low branch v5(N)<B.

The exact v5(N) value need not be enumerated.  Strict-low parity implies
B-v5(N)>=2, hence the weakest possible decimal height is n=B+2k+1.
If even that weaker high-sign 2-adic divisibility has no phase-gap hit,
all deeper strict-low cases are impossible.
"""

TYPES=[(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)]
KMAX={(1,1):77,(1,2):75,(1,3):74,(1,4):72,(3,1):74,(3,2):73}


def bmax(k:int)->int:
    return (2293*k+7569)//1000


def floor_sum(n:int,m:int,a:int,b:int)->int:
    a%=m; b%=m
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
    assert 0<limit<=m
    return count_lt(n,m,a,b,limit)-count_lt(n,m,a,b,1)


def main()->None:
    combo_count=0
    phase_hits=0

    for z,w in TYPES:
        alpha=15-z
        cphase=(339-40*w) if z==1 else (237-20*w)

        for k in range(32,KMAX[(z,w)]+1):
            T=10**k
            low=10**(k-1)
            n_values=9*10**(k-1)
            Q=100*T**2-(10*w-1)
            coeffL=10*T**2-alpha
            constL=-cphase*T

            for B in range(k+1,bmax(k)+1):
                d=B-k
                epsmax=6*5**d

                # Strict-low has B-n5 positive even, hence B-n5>=2.
                # d5=2k+(3B-n5)/2, so weakest n is attained at n5=B-2:
                # n_min=B+2k+1.
                # High-sign divisibility h+cQ == 0 mod 2^(n-1), combined with
                # h*2^(3k)=5^(d-1)L+epsilon, therefore forces
                # epsilon == -(5^(d-1)L+cQ*2^(3k)) mod 2^(B+5k).
                mod=2**(B+5*k)
                ctail=5**(B+2*k)
                factor=-(5**(d-1))

                step=(factor*coeffL)%mod
                base=(
                    -5**(d-1)*(coeffL*low+constL)
                    -ctail*Q*2**(3*k)
                )%mod

                assert epsmax<=mod
                cnt=count_positive_below(n_values,mod,step,base,epsmax)
                combo_count+=1
                phase_hits+=cnt

    assert combo_count==19613, combo_count
    assert phase_hits==0, phase_hits

    print("top-edge strict-5-low phase certificate")
    print("(type,k,B) combinations:",combo_count)
    print("phase hits:",phase_hits)
    print("PASS")


if __name__=="__main__":
    main()
