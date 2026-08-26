#include <bits/stdc++.h>
using namespace std;

struct Type {
  int z,w,lo,hi;
  long long expect_r;
  int Lnum, UnumStar;       // Gamma_L=Lnum/10000, Gamma_U+1e-4=UnumStar/10000
  int old_lo, old_hi;       // existing normalized-shell typewise slots
  long long expect_slots;   // exact new (r,m) pair count
};

static const Type TYPES[] = {
 {1,1, 973440,10885221,579692,300399,330031,6240,65988, 1881136022LL},
 {1,2, 734410, 8400003,255519,260399,290031,5420,57968,  821624445LL},
 {1,3, 529000, 6236387,328609,220399,250031,4600,49948, 1060138361LL},
 {1,4, 357210, 4394372,134570,180399,210031,3780,41927,  429109928LL},
 {3,1, 519840,15204352,863426,218199,390031,4560,77989,15361714596LL},
 {3,2, 428490,13677244,441624,198199,370031,4140,73969, 7802825159LL},
};

int chi5(int a){
  a%=5; if(a<0)a+=5;
  if(a==1||a==4)return 1;
  if(a==2||a==3)return -1;
  return 0;
}

int powmod(int a,long long e,int m){
  long long r=1%m; a%=m;
  while(e){
    if(e&1)r=r*a%m;
    a=1LL*a*a%m;
    e>>=1;
  }
  return (int)r;
}

bool odd_block_partition_ok(int n,const vector<int>&spf){
  int cnt=0;
  while(n>1){
    int p=spf[n],e=0;
    while(n%p==0){n/=p;++e;}
    if((p&3)==3 && (e&1)) ++cnt;
  }
  return cnt>=2;
}

string str128(__int128 v){
  if(v==0)return "0";
  string s;
  while(v){s.push_back(char('0'+v%10));v/=10;}
  reverse(s.begin(),s.end());
  return s;
}

// F0(x)=r(x+20w-1)/(5(x^2-1)) is strictly decreasing for x>1.
// A candidate satisfies
//   Gamma_L < F0(y) < Gamma_U+1e-4,
// y=R/5^d and m=floor(y).
// Therefore:
//   m_min = smallest m with F0(m+1)<Gamma_U+1e-4;
//   m_max = largest  m with F0(m)>Gamma_L.
// All tests below are exact integer inequalities; there is no floating point.
pair<int,int> contact_slots(int r,int w,int Lnum,int UnumStar){
  const long long SCALE=10000;
  const long long a=20LL*w-1;

  auto lower_ok=[&](long long m){
    long long x=m+1;
    __int128 lhs=(__int128)SCALE*r*(x+a);
    __int128 rhs=(__int128)5*UnumStar*(x*x-1);
    return lhs<rhs;
  };

  auto upper_ok=[&](long long m){
    long long x=m;
    __int128 lhs=(__int128)SCALE*r*(x+a);
    __int128 rhs=(__int128)5*Lnum*(x*x-1);
    return lhs>rhs;
  };

  int lo=1,hi=200000;
  while(lo<hi){
    int md=(lo+hi)/2;
    if(lower_ok(md))hi=md; else lo=md+1;
  }
  int mmin=lo;

  lo=1;hi=200000;
  while(lo<hi){
    int md=(lo+hi+1)/2;
    if(upper_ok(md))lo=md; else hi=md-1;
  }
  int mmax=lo;
  return {mmin,mmax};
}

int main(){
  const int MAXR=15204352;
  vector<int> spf(MAXR+1);
  for(int i=2;i<=MAXR;i++) if(!spf[i]){
    spf[i]=i;
    if(1LL*i*i<=MAXR)
      for(long long j=1LL*i*i;j<=MAXR;j+=i)
        if(!spf[j])spf[j]=i;
  }

  const int P5=15625;      // 5^6
  const int MOD=16*P5;

  long long grand_r=0;
  __int128 grand_new=0,grand_old=0;

  for(auto tp:TYPES){
    bool feasible[2][5][2][8][2]{};

    // Reproduce the corrected safe local-r certificate exactly.
    for(int N0=0;N0<MOD;N0++){
      int tmp=N0,nu=0;
      if(tmp==0)continue;
      while(tmp%5==0){tmp/=5;++nu;}
      if(nu>4)continue;

      long long c=1LL*tp.z*tp.w;
      int n16=(int)(((1LL*(N0-1)*(N0-1)+c*c)%16+16)%16);
      int n2,N2;
      if(tp.w&1){
        if(n16&1){n2=0;N2=n16&7;}
        else if((n16&3)==2){n2=1;N2=(n16/2)&7;}
        else continue;
      }else{
        n2=0;
        N2=(int)(((1LL*(N0-1)*(N0-1)+c*c)%8+8)%8);
      }

      int n5=(int)(((1LL*(N0-1)*(N0-1)+c*c)%P5+P5)%P5);
      vector<int> chiN;
      if(n5==0)chiN={-1,1};
      else{
        while(n5%5==0)n5/=5;
        chiN={chi5(n5)};
      }

      for(int apar=0;apar<2;apar++){
        if((tp.w&1)==0){if(apar)continue;} // even w => eta=-a2 even
        else if(apar!=n2)continue;

        int Apar=(1-apar)&1;
        int rhs=Apar?-1:1;
        int Q8=(1-10*tp.w)%8; if(Q8<0)Q8+=8;

        for(int Bpar=0;Bpar<2;Bpar++){
          int r8=(-powmod(5,Bpar+1,8)*Q8*N2)%8;
          if(r8<0)r8+=8;
          for(int cn:chiN){
            int req=rhs*chi5(tp.w)*cn;
            feasible[apar][nu][Bpar][r8][req==1]=true;
          }
        }
      }
    }

    long long rcount=0;
    __int128 slots=0;
    int first=(tp.lo+4)/5*5;

    for(int r=first;r<=tp.hi;r+=5){
      int x=r,a2=0,a5=0;
      while((x&1)==0){x>>=1;++a2;}
      while(x%5==0){x/=5;++a5;}
      if(a5<1)continue;

      int r10=x;
      int ci=(chi5(r10)==1);
      bool ok=false;
      for(int nu=0;nu<=(a5-1)/2;nu++){
        int B=a5-2*nu;
        if(feasible[a2&1][nu][B&1][r10&7][ci]){ok=true;break;}
      }
      if(!ok)continue;
      if((tp.w&1) && !odd_block_partition_ok(r10,spf))continue;

      ++rcount;
      auto [mn,mx]=contact_slots(r,tp.w,tp.Lnum,tp.UnumStar);
      mn=max(mn,tp.old_lo);
      mx=min(mx,tp.old_hi);
      if(mn>mx){
        cerr<<"unexpected empty slot interval at type ("<<tp.z<<","<<tp.w
            <<") r="<<r<<"\n";
        return 1;
      }
      slots+=(long long)(mx-mn+1);
      grand_old+=(long long)(tp.old_hi-tp.old_lo+1);
    }

    if(rcount!=tp.expect_r){
      cerr<<"r-count mismatch at type ("<<tp.z<<","<<tp.w<<") got "
          <<rcount<<" expect "<<tp.expect_r<<"\n";
      return 1;
    }
    if(slots!=(__int128)tp.expect_slots){
      cerr<<"slot-count mismatch at type ("<<tp.z<<","<<tp.w<<") got "
          <<str128(slots)<<" expect "<<tp.expect_slots<<"\n";
      return 1;
    }

    grand_r+=rcount;
    grand_new+=slots;
    cout<<"("<<tp.z<<","<<tp.w<<") r="<<rcount
        <<" slots="<<str128(slots)<<"\n";
  }

  if(grand_r!=2603440LL)return 1;
  if(grand_new!=(__int128)27356548511LL)return 1;
  if(grand_old!=(__int128)162338926240LL)return 1;

  cout<<"TOTAL r="<<grand_r
      <<" new_slots="<<str128(grand_new)
      <<" old_slots="<<str128(grand_old)<<"\n";
  cout<<"CERTIFICATE OK: contact/remainder coupling leaves 27,356,548,511 "
        "safe moderate (r,m) pairs.\n";
  return 0;
}
