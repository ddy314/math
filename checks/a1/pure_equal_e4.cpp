// Exact finite certificate for g=0, b1=b2=10^4 and balanced b3.
// Compile: g++ -O3 -std=c++17 <this file> -o /tmp/check_a1_e4
// This only covers e=4; no assertion about unbounded prefix depth.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <numeric>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using I = __int128_t;
using U = __uint128_t;
using Big = boost::multiprecision::int256_t;

I pow10(int n) { I x=1; while(n--) x*=10; return x; }
I floor_div(I a,I b) { assert(b>0); I q=a/b,r=a%b; return q-(r<0); }
I ceil_div(I a,I b) { return -floor_div(-a,b); }
U sqrt128(U n) {
    if (!n) return 0;
    int bits=0; for(U t=n;t;t>>=1) ++bits;
    U x=U(1)<<((bits+1)/2);
    for (;;) { U y=(x+n/x)/2; if(y>=x) return x; x=y; }
}
Big sqrt_big(const Big& n) {
    assert(n>=0); if(n==0) return 0;
    Big x=Big(1)<<((boost::multiprecision::msb(n)+2)/2);
    for(;;) { Big y=(x+n/x)/2; if(y>=x) return x; x=y; }
}
I as_i(const Big& n) {
    const Big cap=(Big(1)<<127)-1;
    assert(n>=-cap && n<=cap);
    return n.convert_to<I>();
}
int mod(I x,int p) { int r=int(x%p); return r<0?r+p:r; }

struct Filter {
    int p;
    std::vector<unsigned char> table;
};
std::vector<Filter> filters(I M,I j,I Q0,I Z) {
    std::vector<Filter> out;
    for(int p:{17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}) {
        Filter f{p,std::vector<unsigned char>(p*p)};
        std::vector<unsigned char> square(p);
        for(int x=0;x<p;++x) square[x*x%p]=1;
        for(int a=0;a<p;++a) for(int J=0;J<p;++J) {
            I a2=mod(Z,p)*a-J;
            I n=I(a)*a+a2*a2;
            I w=mod(Q0,p)*mod(Z,p)*a-J;
            I D=mod(M*M,p)*(w*w-mod(Q0*Q0,p)*n)-mod(2*j*Q0,p)*n;
            f.table[a*p+J]=square[mod(D,p)];
        }
        out.push_back(std::move(f));
    }
    return out;
}

struct Count {
    uint64_t prefix=0,J=0,sieve=0,square=0,root=0,solution=0;
    Count& operator+=(const Count& r) {
        prefix+=r.prefix;J+=r.J;sieve+=r.sieve;square+=r.square;
        root+=r.root;solution+=r.solution;return *this;
    }
};

int main(int argc,char** argv) {
    assert(argc==1 || argc==2);
    std::ofstream dump;
    if(argc==2) { dump.open(argv[1]);assert(dump); }
    const int e=4;
    const I E=pow10(e),Q0=10*E+1,Q=E*Q0;
    Count total;
    for(auto state: {std::pair<int,int>{3,11}, {4,9091}}) {
        int delta=state.first; I j=state.second,M=pow10(delta);
        assert(Q0%j==0);
        I C=M*M*(Q0-1),F0=1+M*M*(Q0/j),qa=F0*F0-1;
        I q=E*M*j,tail_lo=M*M*M/10,tail_hi=M*M*M-1;
        for(int d:{0,1}) {
            int kmax=d==0?3*delta+1:e/2;
            for(int k=1;k<=kmax;++k) {
                I Z=pow10(k);
                // xi(1-lambda)=E(Q0-1)/(Q+1). Contact is strict.
                Big contact_n=Big(E)*E*(100*Big(Z)*Z+100)*(Q+1)*(Q+1);
                Big contact_d=Big(E)*E*(Q0-1)*(Q0-1)*Z*Z-Big(Q+1)*(Q+1);
                assert(contact_d>0);
                I a_lo=pow10(e+d),a_hi=pow10(e+d+1)-1;
                I left=a_lo-1,right=a_hi;
                while(left<right) {
                    I mid=(left+right+1)/2;
                    if(Big(mid)*mid*contact_d<contact_n) left=mid; else right=mid-1;
                }
                a_hi=left;
                auto ff=filters(M,j,Q0,Z);
                Count row;
                for(I a=a_lo;a<=a_hi;++a) {
                    if(std::gcd(int(a%10),10)!=1) continue;
                    ++row.prefix;
                    // True tail digits improve V: r3<M^2/(Ej),
                    // V<M(j^2 a1^2+M^4)/(2j a2).
                    I vn=M*(j*j*a*a+M*M*M*M);
                    I vmax=(vn-1)/(2*j*Z*E);
                    I base=M*j*Z*a,den=M*(C+j);
                    I Jlo=std::max({I(1),Z*a-(pow10(e+k+1)-1),ceil_div(base-tail_hi+F0,den)});
                    I Jhi=std::min(Z*a-pow10(e+k),floor_div(base-tail_lo+F0*vmax,den));
                    if(Jlo>Jhi) continue;
                    // Monotone refinement of the same strict V bound.
                    I derivative=M*(C+2*j)*Z*a-2*M*(C+j)*Jhi-tail_lo;
                    assert(derivative>=0);
                    auto possible=[&](I J) {
                        return 2*j*(Z*a-J)*(tail_lo-base+den*J)<F0*vn;
                    };
                    if(!possible(Jlo)) continue;
                    I lo=Jlo,hi=Jhi;
                    while(lo<hi) { I mid=(lo+hi+1)/2; if(possible(mid)) lo=mid; else hi=mid-1; }
                    Jhi=lo;
                    // Every heavy discriminant product fits signed 128 bits;
                    // the other cases fit the signed 256-bit backend.
                    Big norm_cap=Big(a)*a+Big(Z*a)*Z*a;
                    Big w_cap=Big(Q0)*Z*a+Jhi;
                    Big D_cap=Big(M)*M*(w_cap*w_cap+Big(Q0)*Q0*norm_cap)
                        +2*Big(j)*Q0*norm_cap;
                    assert(D_cap<(Big(1)<<(k<=3?127:255)));
                    std::vector<const unsigned char*> rows;
                    for(const auto& f:ff) rows.push_back(&f.table[mod(a,f.p)*f.p]);
                    for(int residue:{1,3,7,9}) {
                        I start=Jlo+mod(residue-mod(Jlo,10),10);
                        for(I J=start;J<=Jhi;J+=10) {
                            ++row.J;
                            bool pass=true;
                            for(size_t h=0;h<ff.size();++h) {
                                if(!rows[h][mod(J,ff[h].p)]) { pass=false;break; }
                            }
                            if(!pass) continue;
                            ++row.sieve;
                            I a2=Z*a-J,B=base-den*J,lin=F0*B-j*M*a2;
                            // D_original=M^4 D_normalized. For k<=3 all
                            // normalized intermediates are <2^127; k>=4
                            // uses fixed 256-bit integers (max magnitude <10^56).
                            Big D,rd;
                            if(k<=3) {
                                I n=a*a+a2*a2,w=Q0*Z*a-J;
                                I di=M*M*(w*w-Q0*Q0*n)-2*j*Q0*n;
                                D=di;
                            } else {
                                Big n=Big(a)*a+Big(a2)*a2,w=Big(Q0)*Z*a-J;
                                D=Big(M)*M*(w*w-Big(Q0)*Q0*n)-2*Big(j)*Q0*n;
                            }
                            if(dump.is_open()) dump<<delta<<' '<<int(j)<<' '<<d<<' '<<k<<' '
                                <<int(a)<<' '<<static_cast<long long>(J)<<' '<<D<<'\n';
                            if(D<0) continue;
                            if(k<=3) rd=I(sqrt128(U(as_i(D)))); else rd=sqrt_big(D);
                            if(rd*rd!=D) continue;
                            ++row.square;
                            I root_d=as_i(Big(M)*M*rd);
                            for(I numerator:{-lin+root_d,-lin-root_d}) {
                                if(numerator%qa) continue;
                                I V=numerator/qa;
                                if(V<1 || V>vmax) continue;
                                I a3=B+F0*V;
                                if(a3<tail_lo || a3>tail_hi) continue;
                                ++row.root;
                                I aa=a3,bb=q;while(bb) {I t=aa%bb;aa=bb;bb=t;}
                                if(aa!=1) continue;
                                I H=j*M*a2+V;
                                Big alpha=(Big(a)*pow10(e+1+k)+a2)*M*M*M+a3;
                                assert(Big(H)*H==Big(j*M*a)*j*M*a+Big(j*M*a2)*j*M*a2+Big(a3)*a3);
                                assert(alpha==Big(H)*F0);
                                ++row.solution;
                            }
                        }
                    }
                }
                total+=row;
                std::cout<<"delta="<<delta<<" j="<<int(j)<<" d="<<d<<" k="<<k
                    <<" prefix="<<row.prefix<<" J="<<row.J<<" sieve="<<row.sieve
                    <<" square="<<row.square<<" root="<<row.root<<" solution="<<row.solution<<std::endl;
            }
        }
    }
    std::cout<<"TOTAL prefix="<<total.prefix<<" J="<<total.J<<" sieve="<<total.sieve
        <<" square="<<total.square<<" root="<<total.root<<" solution="<<total.solution<<std::endl;
    assert(total.prefix==828814 && total.J==262115848 && total.sieve==1377);
    assert(total.square==0 && total.root==0 && total.solution==0);
    std::cout<<"PASS: complete finite e=4 certificate; no claim for unbounded e"<<std::endl;
}
