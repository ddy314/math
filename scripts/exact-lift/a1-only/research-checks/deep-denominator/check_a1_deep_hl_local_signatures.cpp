#include <bits/stdc++.h>
using namespace std;

struct Type { int z,w,lo,hi; long long expect; };
static const Type TYPES[] = {
 {1,1, 973440,10885221,579692},
 {1,2, 734410, 8400003,255519},
 {1,3, 529000, 6236387,328609},
 {1,4, 357210, 4394372,134570},
 {3,1, 519840,15204352,863426},
 {3,2, 428490,13677244,441624},
};

int vp(int n,int p){ int e=0; while(n%p==0){n/=p;++e;} return e; }
int chi5(int a){ a%=5; if(a<0)a+=5; if(a==1||a==4)return 1; if(a==2||a==3)return -1; return 0; }
int powmod(int a,long long e,int m){ long long r=1%m; a%=m; while(e){if(e&1)r=r*a%m;a=1LL*a*a%m;e>>=1;}return (int)r; }

// For odd w, alpha,beta must both be 3 mod 4.  Since alpha*beta=r10
// and prime-power blocks cannot split, this is possible iff at least two
// p^e || r10 blocks themselves are 3 mod 4.
bool odd_block_partition_ok(int n,const vector<int>&spf){
 int cnt=0;
 while(n>1){
   int p=spf[n], e=0;
   while(n%p==0){n/=p;++e;}
   if((p&3)==3 && (e&1)) ++cnt;
 }
 return cnt>=2;
}

int main(){
 const int MAXR=15204352;
 vector<int> spf(MAXR+1);
 for(int i=2;i<=MAXR;i++) if(!spf[i]){
   spf[i]=i;
   if(1LL*i*i<=MAXR) for(long long j=1LL*i*i;j<=MAXR;j+=i) if(!spf[j]) spf[j]=i;
 }

 const int P5=15625;          // 5^6
 const int MOD=16*P5;         // CRT container for mod 16 and mod 5^6
 long long grand_initial=0, grand_final=0;

 for(auto tp:TYPES){
   // feasible[a2 parity][nu5(N0)=0..4][B parity][r10 mod8][chi(r10) index]
   bool feasible[2][5][2][8][2]{};

   for(int N0=0;N0<MOD;N0++){
     int tmp=N0, nu=0;
     if(tmp==0) continue; // actual v5(N0)>=6, impossible here since nu<=4
     while(tmp%5==0){tmp/=5;++nu;}
     if(nu>4) continue;

     long long c=1LL*tp.z*tp.w;
     int n16=(int)(((1LL*(N0-1)*(N0-1)+c*c)%16+16)%16);
     int n2, N2;
     if(tp.w&1){
       if(n16&1){ n2=0; N2=n16&7; }
       else if((n16&3)==2){ n2=1; N2=(n16/2)&7; }
       else continue;
     } else {
       n2=0;
       N2=(int)(((1LL*(N0-1)*(N0-1)+c*c)%8+8)%8);
     }

     int n5=(int)(((1LL*(N0-1)*(N0-1)+c*c)%P5+P5)%P5);
     vector<int> chiN;
     if(n5==0) chiN={-1,1}; // safe tail: next unit may have either symbol
     else {
       while(n5%5==0)n5/=5;
       chiN={chi5(n5)};
     }

     for(int apar=0;apar<2;apar++){
       // This parity is a proved master condition.  The historical expected
       // counts accidentally came from omitting this even-w line, although
       // the checker itself already contained it.
       if((tp.w&1)==0){ if(apar) continue; } // even w => eta=-a2 even
       else { if(apar!=n2) continue; }       // odd w => eta parity=n2

       int Apar=(1-apar)&1; // A=2k+3-a2 in moderate HL
       int rhs=Apar ? -1:1;
       int Q8=(1-10*tp.w)%8; if(Q8<0)Q8+=8;

       for(int Bpar=0;Bpar<2;Bpar++){
         int r8=(-powmod(5,Bpar+1,8)*Q8*N2)%8; if(r8<0)r8+=8;
         for(int cn:chiN){
           int req=rhs*chi5(tp.w)*cn; // chi(r10)=rhs/(chi(w)chi(N5))
           int ci=(req==1);
           feasible[apar][nu][Bpar][r8][ci]=true;
         }
       }
     }
   }

   long long initial=0, finalc=0;
   int first=(tp.lo+4)/5*5;
   for(int r=first;r<=tp.hi;r+=5){
     int x=r, a2=0,a5=0;
     while((x&1)==0){x>>=1;++a2;}
     while(x%5==0){x/=5;++a5;}
     if(a5<1) continue;
     ++initial;
     int r10=x;
     int cr=chi5(r10), ci=(cr==1);
     bool ok=false;
     for(int nu=0;nu<=(a5-1)/2;nu++){
       int B=a5-2*nu;
       if(feasible[a2&1][nu][B&1][r10&7][ci]){ ok=true; break; }
     }
     if(!ok) continue;
     if((tp.w&1) && !odd_block_partition_ok(r10,spf)) continue;
     ++finalc;
   }

   cout << "("<<tp.z<<","<<tp.w<<") initial="<<initial
        <<" final="<<finalc<<"\n";
   if(finalc!=tp.expect){ cerr<<"COUNT MISMATCH\n"; return 1; }
   grand_initial+=initial; grand_final+=finalc;
 }

 cout << "TOTAL initial="<<grand_initial<<" final="<<grand_final<<"\n";
 if(grand_initial!=11051041LL || grand_final!=2603440LL) return 1;
 cout << "CERTIFICATE OK: moderate HL local r signatures reduced to 2,603,440.\n";
}
