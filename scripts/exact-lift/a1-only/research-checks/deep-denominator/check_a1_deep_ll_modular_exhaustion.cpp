#include <bits/stdc++.h>
using namespace std; using i128=__int128_t;
struct Mask{uint64_t a[7];};
Mask fullmask(){Mask m{};for(int i=0;i<7;i++)m.a[i]=~0ULL; for(int b=420;b<448;b++)m.a[b>>6]&=~(1ULL<<(b&63));return m;}
bool nonempty(const Mask&m){for(auto x:m.a)if(x)return true;return false;}
void mand(Mask&x,const Mask&y){for(int i=0;i<7;i++)x.a[i]&=y.a[i];}
void setbit(Mask&m,int b){m.a[b>>6]|=1ULL<<(b&63);}
long long mpow(long long a,long long e,int p){long long r=1%p;a%=p;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;}
int inv(int a,int p){return (int)mpow((a%p+p)%p,p-2,p);} int ord10(int p){int x=1;for(int o=1;o<p;o++){x=1LL*x*10%p;if(x==1)return o;}return 0;}
struct Table{int p,o; vector<Mask> tab;};
int idx3(int r,int d,int g,int p){return (r*p+d)*p+g;}
Table build(int z,int w,int p){
 int o=ord10(p); vector<char> sq(p); vector<int> root(p,-1); for(int x=0;x<p;x++){int q=1LL*x*x%p;sq[q]=1;if(root[q]<0)root[q]=x;}
 vector<Mask> tab((size_t)p*p*p); long long C0=1LL*w*(10*w-1); int aa=C0%p;
 auto contact_ok=[&](int N,int gg,int dd,long long T)->bool{
   long long b1=(10*T%p*T-w)%p;if(b1<0)b1+=p; long long a2=(10*T%p*T-z)%p;if(a2<0)a2+=p;
   long long Q=(100*T%p*T-10*w+1)%p;if(Q<0)Q+=p; long long a1=(100*T%p*T%p*T+(10*(5-z-w)+1LL)*T+N-1)%p;if(a1<0)a1+=p;
   long long C=(10*T%p*T%p*a1+a2)%p; long long NN=(a1*a1+(a2*b1%p)*(a2*b1%p))%p; long long Dp=T*Q%p; long long K=(b1*b1%p*C%p*C-Dp*Dp%p*NN)%p;if(K<0)K+=p;
   long long rho=(N-1LL*gg*inv(dd,p)%p*inv((int)T,p))%p;if(rho<0)rho+=p; long long Rc=(K-2*rho%p*Dp%p*NN)%p;if(Rc<0)Rc+=p; return sq[Rc];
 };
 for(int rr=0;rr<p;rr++)for(int dd=1;dd<p;dd++)for(int gg=0;gg<p;gg++){
   Mask m{}; int di=inv(dd,p); int R=1LL*rr*di%p; long long u=(10LL*gg*(20*w-1)+1LL*dd*rr)%p;
   for(int kr=0;kr<o;kr++){long long T=mpow(10,kr,p),L=T*di%p; int bb=(int)((-u*L)%p);if(bb<0)bb+=p;int cc=(int)((1000LL%p*gg%p*gg%p*L%p*L+1LL*gg*R)%p); bool ok=false;
     if(aa==0){ if(bb!=0){int N=1LL*(p-cc)%p*inv(bb,p)%p;ok=contact_ok(N,gg,dd,T);} else if(cc==0){ for(int N=0;N<p&&!ok;N++)ok=contact_ok(N,gg,dd,T); } }
     else {int disc=(1LL*bb*bb-4LL*aa*cc)%p;if(disc<0)disc+=p;if(sq[disc]){int sd=root[disc],ia=inv(2*aa,p);int N1=1LL*(p-bb+sd)%p*ia%p;ok=contact_ok(N1,gg,dd,T);if(!ok&&sd){int N2=1LL*(p-bb-sd+p)%p*ia%p;ok=contact_ok(N2,gg,dd,T);}}}
     if(ok)for(int kk=kr;kk<420;kk+=o)setbit(m,kk);
   }
   tab[idx3(rr,dd,gg,p)]=m;
 }
 return {p,o,move(tab)};
}
struct Surv{long long r,D,gamma;Mask mask;};
vector<int> goodResiduesFull(int z,int w,long long r,long long D,long long gamma,int p){
 int o=ord10(p); vector<char> sq(p); vector<int> root(p,-1);for(int x=0;x<p;x++){int q=1LL*x*x%p;sq[q]=1;if(root[q]<0)root[q]=x;}
 int dd=D%p,di=inv(dd,p),rr=r%p,gg=gamma%p,R=1LL*rr*di%p; long long C0=1LL*w*(10*w-1),u=(10LL*gg*(20*w-1)+1LL*dd*rr)%p;int aa=C0%p;vector<int> good;
 auto contact=[&](int N,long long T)->bool{long long b1=(10*T%p*T-w)%p;if(b1<0)b1+=p;long long a2=(10*T%p*T-z)%p;if(a2<0)a2+=p;long long Q=(100*T%p*T-10*w+1)%p;if(Q<0)Q+=p;long long a1=(100*T%p*T%p*T+(10*(5-z-w)+1LL)*T+N-1)%p;if(a1<0)a1+=p;long long C=(10*T%p*T%p*a1+a2)%p;long long NN=(a1*a1+(a2*b1%p)*(a2*b1%p))%p;long long Dp=T*Q%p;long long K=(b1*b1%p*C%p*C-Dp*Dp%p*NN)%p;if(K<0)K+=p;long long rho=(N-1LL*gg*di%p*inv((int)T,p))%p;if(rho<0)rho+=p;long long Rc=(K-2*rho%p*Dp%p*NN)%p;if(Rc<0)Rc+=p;return sq[Rc];};
 for(int kr=0;kr<o;kr++){long long T=mpow(10,kr,p),L=T*di%p;int bb=(int)((-u*L)%p);if(bb<0)bb+=p;int cc=(int)((1000LL%p*gg%p*gg%p*L%p*L+1LL*gg*R)%p);bool ok=false;if(aa==0){if(bb){int N=1LL*(p-cc)%p*inv(bb,p)%p;ok=contact(N,T);}else if(cc==0){for(int N=0;N<p&&!ok;N++)ok=contact(N,T);}}else{int disc=(1LL*bb*bb-4LL*aa*cc)%p;if(disc<0)disc+=p;if(sq[disc]){int sd=root[disc],ia=inv(2*aa,p);int N1=1LL*(p-bb+sd)%p*ia%p;ok=contact(N1,T);if(!ok&&sd){int N2=1LL*(p-bb-sd+p)%p*ia%p;ok=contact(N2,T);}}}if(ok)good.push_back(kr);}return good;
}
bool compatMask(const Mask&m,const vector<int>&good,int o){int g=std::gcd(420,o);for(int a=0;a<420;a++)if((m.a[a>>6]>>(a&63))&1ULL)for(int b:good)if((a-b)%g==0)return true;return false;}
int main(int argc,char**argv){int z=1,w=1;if(argc>2){z=atoi(argv[1]);w=atoi(argv[2]);}
 vector<int> ps={3,7,11,13,29,31,37,41,43,61,71,101,127}; vector<Table> tabs; for(int p:ps){cerr<<"build p="<<p<<"\n";tabs.push_back(build(z,w,p));}
 long long rlo,rhi,Lnum,Lden,Unum,Uden;
 if(z==1&&w==1){rlo=761760;rhi=10885221;Lnum=276949968;Lden=10000000;Unum=3300225945LL;Uden=100000000;}
 else if(z==1&&w==2){rlo=542890;rhi=8400003;Lnum=234949936;Lden=10000000;Unum=2900225945LL;Uden=100000000;}
 else if(z==1&&w==3){rlo=361000;rhi=6236387;Lnum=192949904;Lden=10000000;Unum=2500225945LL;Uden=100000000;}
 else if(z==1&&w==4){rlo=216090;rhi=4394372;Lnum=150949872;Lden=10000000;Unum=2100225945LL;Uden=100000000;}
 else if(z==3&&w==1){rlo=384160;rhi=15204352;Lnum=196949978;Lden=10000000;Unum=3900225945LL;Uden=100000000;}
 else if(z==3&&w==2){rlo=299290;rhi=13677244;Lnum=174949956;Lden=10000000;Unum=3700225945LL;Uden=100000000;}
 else {cerr<<"unsupported type\n";return 2;}
 long long full_rlo=rlo,full_rhi=rhi;if(argc>4){rlo=stoll(argv[3]);rhi=stoll(argv[4]);}
 int e=__builtin_ctz(w),w0=w>>e; unsigned long long total=0,surv=0; array<unsigned long long,421> kres{}; vector<Surv> sv;
 for(long long r=rlo;r<=rhi;r++){
   long long tmp=r;int r2=0,r5=0;while(!(tmp&1)){r2++;tmp>>=1;}while(tmp%5==0){r5++;tmp/=5;}if(r5<1)continue;long long r10=tmp;
   for(int nu2=0;;nu2++){int A=r2-2*nu2-e;if(A<1)break;bool ok2=true,strict=false;
     if((w&1)==0){ok2=(A&1);strict=ok2;}
     else if(nu2==0){if(A==1){strict=false;}else{ok2=(A>=3&&(A&1));strict=ok2;}}
     else{if(A==1||A==2){strict=false;}else{ok2=(A>=4&&!(A&1));strict=ok2;}}
     if(!ok2)continue;int want=(w==3?3:1);if(strict&&(r10&3)!=want)continue;
     for(int nu5=0;;nu5++){int B=r5-2*nu5;if(B<1)break;long long D=(1LL<<A);for(int j=0;j<B;j++)D*=5;
       long long glo=(long long)(((i128)Lnum*D)/Lden)+1; long long ghi=(long long)((((i128)Unum*D)+Uden-1)/Uden)-1;
       long long Ccoef=-(long long)w0*(10*w-1)*r10;
       for(int gr=1;gr<40;gr+=2){if(gr%5==0)continue;int m8=(Ccoef*gr)%8;if(m8<0)m8+=8;if(m8!=1)continue;int m5=(Ccoef*gr)%5;if(m5<0)m5+=5;if(!(m5==1||m5==4))continue;
         long long first=gr;if(first<glo)first+=((glo-first+39)/40)*40;
         for(long long gamma=first;gamma<=ghi;gamma+=40){total++;Mask m=fullmask();for(auto&tb:tabs){int p=tb.p;mand(m,tb.tab[idx3(r%p,D%p,gamma%p,p)]);if(!nonempty(m))break;}if(nonempty(m)){surv++;sv.push_back({r,D,gamma,m});for(int kk=0;kk<420;kk++)if(m.a[kk>>6]>>(kk&63)&1ULL)kres[kk]++;}}
       }
     }
   }
 }
 cout<<"type="<<z<<","<<w<<" total="<<total<<" surv="<<surv<<"\n";unsigned long long bits=0;for(int k=0;k<420;k++)bits+=kres[k];cout<<"statebits="<<bits<<"\n";
 vector<int> extraPs={17,19,73,89,113,137,251,337,1009,4201};size_t alive=0;map<int,int> killed;vector<Surv> finalSv;
 for(auto&x:sv){bool ok=true;for(int p:extraPs){auto g=goodResiduesFull(z,w,x.r,x.D,x.gamma,p);int o=ord10(p);if(!compatMask(x.mask,g,o)){killed[p]++;ok=false;break;}}if(ok){alive++;finalSv.push_back(x);}}
 cout<<"after_extra="<<alive<<"\n";for(auto[p,c]:killed)cout<<"kill"<<p<<"="<<c<<" ";cout<<"\n";
 const int BIG=277200;size_t jointAlive=0,jointBefore=0;
 for(auto&x:finalSv){vector<int>st;for(int a=0;a<420;a++)if((x.mask.a[a>>6]>>(a&63))&1ULL)for(int k=a;k<BIG;k+=420)st.push_back(k);for(int p:extraPs){auto gg=goodResiduesFull(z,w,x.r,x.D,x.gamma,p);int o=ord10(p);vector<char>ok(o);for(int b:gg)ok[b]=1;size_t wr=0;for(int k:st)if(ok[k%o])st[wr++]=k;st.resize(wr);if(st.empty())break;}if(!st.empty()){
   jointBefore++;vector<int>divPs={67,151,181,199,211,239,241,271,281,421,631,661,1933,2161,2689};
   for(int p:divPs){auto gg=goodResiduesFull(z,w,x.r,x.D,x.gamma,p);int o=ord10(p);vector<char>ok(o);for(int b:gg)ok[b]=1;size_t wr=0;for(int k:st)if(ok[k%o])st[wr++]=k;st.resize(wr);if(st.empty())break;}
   if(!st.empty())jointAlive++;
 }}
 cout<<"joint_before="<<jointBefore<<" joint_after_extra_div="<<jointAlive<<"\n";
 if(jointAlive!=0){cerr<<"UNEXPECTED SURVIVORS\n";return 1;}
 if(rlo==full_rlo&&rhi==full_rhi){struct E{unsigned long long local,common,bits,after,joint;};map<pair<int,int>,E>ex={{{1,1},{57278520ULL,593553ULL,1016555ULL,93222ULL,6980ULL}},{{1,2},{19206685ULL,93027ULL,155388ULL,13674ULL,916ULL}},{{1,3},{25308717ULL,162735ULL,258880ULL,20743ULL,1530ULL}},{{1,4},{4331873ULL,18342ULL,28788ULL,2271ULL,154ULL}},{{3,1},{306099009ULL,3156352ULL,5421691ULL,500727ULL,37426ULL}},{{3,2},{110439962ULL,575335ULL,974681ULL,86545ULL,6020ULL}}};auto E0=ex[{z,w}];if(total!=E0.local||surv!=E0.common||bits!=E0.bits||alive!=E0.after||jointBefore!=E0.joint){cerr<<"COUNT MISMATCH\n";return 1;}}
 cout<<"CERTIFICATE OK type=("<<z<<","<<w<<") r=["<<rlo<<","<<rhi<<"] final=0\n";
}
