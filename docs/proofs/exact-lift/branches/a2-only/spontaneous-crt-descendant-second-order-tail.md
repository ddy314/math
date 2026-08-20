# A2 descendant recycling 的 canonical second-order tail

> **依赖：** `spontaneous-crt-descendant-balance-tail.md`、`spontaneous-crt-descendant-balance-gcd-ladder.md`、`spontaneous-crt-descendant-second-order-balance.md`。
>
> **严格状态：**first-order balance tail `B_63` 已读取一个完整 common baseline 以内的全部 recycling depth；此前唯一 generic unit 自由停在 `rho=v_p(B_63)=h=v_p(G_Delta)`。本文把 exact linear 与 quadratic transported terms一起清分母，构造 ordinary integer `N_63^(2)`。令 `S_bal=gcd(G_Delta,B_63)`，则 `G_Delta S_bal | N_63^(2)` 全局成立；正 quotient `C_63^(2)` 精确选择“balance 已至少饱和一个 baseline 且 actual remainder 越过 `2h`”的 common primes。于是 `rho=h` 的 normalized second-order cancellation不再是手工 p-adic unit equation，而由普通 gcd `gcd(G_Delta,C_63^(2))` canonical 读取。本文还证明 parent numerator严格为负，其正相反数的 primitive 2-adic orientation为 `1 mod 8`。本文没有关闭 `rho=h` 的 modular roots，因此不关闭 A2。

---

## 1. parent notation

沿用 fully primitive parent coordinates

\[
X:=5^\lambda\mathscr R_{63}^\star,
\qquad
Y:=g2^m\widehat{\mathscr D}_{63},
\]

\[
G_\Delta:=\gcd(X,Y)
=\gcd(\mathscr R_{63}^\star,\widehat{\mathscr D}_{63}).
\]

first-order fixed gates清 third denominator后记为

\[
\mathfrak G_<:=T^6\mathcal G_<(K,a_3/T),
\qquad
\mathfrak G_>:=T^6\mathcal G_>(K,a_3/T).
\]

真实 endpoint上已有

\[
\boxed{\mathfrak G_<<0,\qquad \mathfrak G_><0.}
\tag{1.1}
\]

balance tail为

\[
\boxed{
\mathscr B_{63}
=-\frac{81X\mathfrak G_<+2Y\mathfrak G_>}{G_\Delta}
>0.}
\tag{1.2}
\]

定义 truncated saturation gcd

\[
\boxed{
S_{bal}:=\gcd(G_\Delta,\mathscr B_{63}).}
\tag{1.3}
\]

逐 genuine common prime `p`，写

\[
h:=v_p(G_\Delta)\ge1,
\qquad
\rho:=v_p(\mathscr B_{63}),
\]
则

\[
\boxed{v_p(S_{bal})=\min(h,\rho).}
\tag{1.4}
\]

---

## 2. primitive quadratic transported numerator

`spontaneous-crt-descendant-second-order-balance.md` 定义 exact quadratic coefficient

\[
\mathcal Q_2(K,\zeta;\chi)
\]
使 equal-parent normalization中的 quadratic term为

\[
s_L^2Y^2\mathcal Q_2(K,\zeta;X/Y).
\]

对 `X,Y` 齐次化。exact denominator audit给唯一 primitive polynomial

\[
\boxed{
\mathcal H_2(X,Y;K,\zeta)\in\mathbf Z[X,Y,K,\zeta]}
\tag{2.1}
\]
满足

\[
\boxed{
Y^2\mathcal Q_2(K,\zeta;X/Y)
=
\frac{256\,\mathcal H_2(X,Y;K,\zeta)}
{5^5 11^6 K^4}.}
\tag{2.2}
\]

其结构为

\[
\boxed{
\deg_{X,Y}\mathcal H_2=2,
\qquad
\deg_\zeta\mathcal H_2=4,
\qquad
\#\operatorname{supp}=45.}
\tag{2.3}
\]

`H_2` 的完整 coefficients由 checker从 exact Taylor formula canonical 重建，正文不抄机械 45 项。

---

## 3. clear the linear and quadratic terms simultaneously

first-order exact term为

\[
M^{(1)}
=
\frac{64s_L}{5^7 11^7K^6T^6}
\left(81X\mathfrak G_<+2Y\mathfrak G_>\right).
\tag{3.1}
\]

quadratic exact term为

\[
M^{(2)}=s_L^2Y^2\mathcal Q_2(K,\zeta;X/Y).
\tag{3.2}
\]

定义 ordinary integer

\[
\boxed{
\begin{aligned}
\mathscr N_{63}^{(2)}:={}&
64\,5^mB^2
\left(81X\mathfrak G_<+2Y\mathfrak G_>\right)\\
&+2^{2M+10}5^2\cdot11\,T^6
\mathcal H_2(X,Y;K,a_3/T).
\end{aligned}}
\tag{3.3}
\]

`T^6 H_2(K,a_3/T)` 为整数，因为 `deg_zeta H_2<=4`。

令

\[
D_0:=5^7 11^7K^6.
\]

直接代

\[
s_L=\frac{2^{2M+2}}{5^mB^2K^2}
\]
与 (2.2)，得到 exact rational scaling

\[
\boxed{
\mathscr N_{63}^{(2)}
=
\frac{5^mB^2D_0T^6}{s_L}
\left(M^{(1)}+M^{(2)}\right).}
\tag{3.4}
\]

右侧 prefactor在 genuine non-`2,5,11`, noncentral external prime上是 p-unit，因此 `N_63^(2)` 无损读取 linear+quadratic remainder depth。

---

## 4. a global integer divisor `G_Delta S_bal`

由 (1.2)：

\[
81X\mathfrak G_<+2Y\mathfrak G_>
=-G_\Delta\mathscr B_{63}.
\]

所以 (3.3) 第一项被

\[
G_\Delta S_{bal}
\]
整除，因为 `S_bal|B_63`。

另一方面 `H_2` 对 `(X,Y)` 齐次二次，而

\[
G_\Delta\mid X,
\qquad
G_\Delta\mid Y.
\]
故第二项被 `G_Delta^2` 整除。又 `S_bal|G_Delta`，所以同样被 `G_Delta S_bal` 整除。

因此得到全局 ordinary divisibility：

\[
\boxed{
G_\Delta S_{bal}\mid\mathscr N_{63}^{(2)}.}
\tag{4.1}
\]

---

## 5. real sign: both first and quadratic pieces are negative

第一项 bracket由 (1.1) 与 `X,Y>0` 立即严格为负。

对 quadratic piece，projectivize

\[
r=1/K,
\qquad
u=\zeta/K,
\qquad
\chi=X/Y.
\]

真实 endpoint已有

\[
0<r<10^{-3},
\qquad
0<u<10^{-3},
\qquad
0<\chi<1/23.
\]

将 (2.2) 的 numerator projectivize后，是 bidegree `(4,4)`、`chi` 次数 2 的 45 项 polynomial。checker在 box

\[
[0,10^{-3}]\times[0,10^{-3}]\times[0,1/23]
\]
上做 exact tensor Bernstein audit，全部 `5*5*3=75` 个 coefficients严格为负；其中

\[
\boxed{
-\frac{1094168903517053204517852672}{129150390625}
\le b
\le
-\frac{14436349673818491223824}{1953125}<0.}
\tag{5.1}
\]

所以

\[
\boxed{
\mathcal H_2(X,Y;K,a_3/T)<0.}
\tag{5.2}
\]

因此 (3.3) 两项同号：

\[
\boxed{
\mathscr N_{63}^{(2)}<0.}
\tag{5.3}
\]

定义 canonical positive second-order tail

\[
\boxed{
\mathscr C_{63}^{(2)}
:=-\frac{\mathscr N_{63}^{(2)}}{G_\Delta S_{bal}}
\in\mathbf Z_{>0}.}
\tag{5.4}
\]

---

## 6. exact second-order support law

exact transport/Euclidean expansion可写

\[
M=M^{(1)}+M^{(2)}+M^{(\ge3)},
\]
其中每个 omitted monomial对 parent errors `(F,L)` 的总次数至少 3。因此在 common baseline `h` 上

\[
\boxed{v_p(M^{(\ge3)})\ge3h.}
\tag{6.1}
\]

### unsaturated balance: `rho<h`

此时

\[
v_p(M^{(1)})=h+\rho<2h,
\]
而 quadratic/higher terms至少 `2h`。所以 linear term唯一最浅；结合 (3.4),(4.1)：

\[
\boxed{p\nmid\mathscr C_{63}^{(2)}.}
\tag{6.2}
\]

### saturated balance: `rho>=h`

此时

\[
v_p(G_\Delta S_{bal})=2h.
\]
又 `3h>=2h+1`。因此由 (3.4)：

\[
\boxed{
p\mid\mathscr C_{63}^{(2)}
\Longleftrightarrow
v_p(M^{(1)}+M^{(2)})>2h
\Longleftrightarrow
v_p(M)>2h.}
\tag{6.3}

合并两支得到 canonical exact selector：

\[
\boxed{
p\mid\mathscr C_{63}^{(2)}
\Longleftrightarrow
\rho\ge h
\ \text{and}\ 
v_p(M)>2h.}
\tag{6.4}

这正是此前 `rho=h` normalized second-order cancellation所缺的 ordinary integer reader。

---

## 7. canonical second-order recycling gcd

定义

\[
\boxed{
\Sigma_{rec}^{(2)}
:=\gcd(G_\Delta,\mathscr C_{63}^{(2)}).}
\tag{7.1}
\]

则 genuine regular common prime满足

\[
\boxed{
p\mid\Sigma_{rec}^{(2)}
\Longleftrightarrow
\rho\ge h
\ \text{and}\ 
v_p(M)>2h.}
\tag{7.2}

已有 second-order theorem进一步说明：

- 若 `rho>h` 且 `p|Sigma_rec^(2)`，则 genuine noncentral prime必须命中 fixed irreducible `P_110(K)`；
- 因此 generic 未固定化分支只剩
  \[
  \boxed{\rho=h,\quad p\mid\Sigma_{rec}^{(2)}.}
  \tag{7.3}
  \]

所以 second-order normalized unit已从“手工 congruence”降成普通 gcd support。

---

## 8. exact binary orientation of the parent numerator

`G_Delta,S_bal` 都是 odd，因此先审计 `-N_63^(2)` 的完整二进 content。

### first-order block is safely deeper

checker对 `T^6 G_<`、`T^6 G_>` 的所有 terms给 uniform lower bounds

\[
v_2(\mathfrak G_<)\ge18,
\qquad
v_2(\mathfrak G_>)\ge17
\]
在 `m>=5` 成立。

又

\[
v_2(B)=M+m+t,
\qquad
v_2(Y)=m+t-1,
\qquad t\ge3.
\]
所以 (3.3) 第一行至少有

\[
\boxed{
v_2(\text{first line})
\ge2M+2m+2t+24.}
\tag{8.1}

### quadratic block has a unique shallowest term

primitive `H_2` 中唯一最低 2-adic monomial为

\[
\boxed{
18283339035648\,X^2\zeta^4
=2^{10}3^{14}\cdot3733\,X^2\zeta^4.}
\tag{8.2}

清 `T^6` 后成为

\[
2^{10}3^{14}\cdot3733\,X^2a_3^4T^2.
\]

checker对全部45项验证：在最小 `(m,t)=(5,3)` 已是唯一 minimum，下一层至少高 4；每项相对 baseline 的 `m,t` slopes均非负。因此对所有 dangerous endpoint

\[
\boxed{
v_2(\text{quadratic line})
=2M+2m+20.}
\tag{8.3}

由 (8.1)，第一行至少再深 `2t+4>=10` 层，所以不会干扰。

于是

\[
\boxed{
v_2(\mathscr N_{63}^{(2)})
=2M+2m+20.}
\tag{8.4}

除去该幂后模 `8` 仍只剩 (8.2)。因为

\[
5^2\cdot11\equiv3\pmod8,
\qquad
3^{14}\cdot3733\equiv5\pmod8,
\]
而所有 odd square/fourth powers为 `1 mod8`，故

\[
\boxed{
\frac{\mathscr N_{63}^{(2)}}{2^{2M+2m+20}}
\equiv7\pmod8.}
\tag{8.5}

结合 `N_63^(2)<0`：

\[
\boxed{
\frac{-\mathscr N_{63}^{(2)}}{2^{2M+2m+20}}
\equiv1\pmod8.}
\tag{8.6}

所以二阶 parent numerator的 positive primitive orientation是 parity-neutral `1 mod8`；它不会凭空再制造一份 odd-inert surcharge。

对 quotient本身：

\[
\boxed{
\frac{\mathscr C_{63}^{(2)}}{2^{2M+2m+20}}
\equiv(G_\Delta S_{bal})^{-1}\pmod8.}
\tag{8.7}

---

## 9. revised frontier

现在 descendant same-prime recycling已有两层 ordinary gcd ladder：

1. first order:
   \[
   \Sigma_{rec}=\gcd(G_\Delta,B_{63});
   \]
2. second order:
   \[
   \Sigma_{rec}^{(2)}=\gcd(G_\Delta,C_{63}^{(2)}).
   \]

其中 second-order selector严格排除 `rho<h`，并在 saturated branch上等价读取 `v_p(M)>2h`。

`rho>h` 的 second-order escape已被 `P_110` 固定化，因此真正 generic frontier进一步缩成

\[
\boxed{
\rho=h,
\qquad
p\mid\Sigma_{rec}^{(2)}.}
\]

下一步应对该 branch构造 third-order normalized balance，或者利用 `C_63^(2)` 与 parent coordinates / `P_63` 的 gcd support做新的 cross-reuse audit；不应再返回 first-order prime-source枚举。

A2 仍为 `待证`。
