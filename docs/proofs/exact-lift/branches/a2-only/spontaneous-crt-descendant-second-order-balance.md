# A2 descendant balance saturation 的 second-order coefficient 与 fixed degree-110 gate

> **依赖：** `spontaneous-crt-descendant-balance-gcd-ladder.md`、`spontaneous-crt-descendant-balance-tail.md`、`spontaneous-crt-descendant-transport-resonance.md`。
>
> **严格状态：**balance gcd ladder 已证明：若 `h=v_p(G_Delta)`、`rho=v_p(B_63)`，则 `rho<h` 时 linear remainder depth精确为 `h+rho`；只有 `rho>=h` 时 quadratic transport才可能参与。本文把 exact rational-root transport与 Euclidean quotient展开到二阶，并在 first-order recycling ratio `chi=chi_geom` 上化简。second-order coefficient的 denominator只含 `81 K^4 G_<^2`，numerator是 primitive total-degree-16 polynomial `S_2(K,zeta)`。它与 universal cubic消去 `zeta` 后精确只剩 central `(2K-9)^8` 与一个 irreducible degree-110 pure-K gate `P_110(K)`。因此当 `rho>h` 时，若 actual remainder还要越过 `2h`，genuine noncentral prime必须命中 `P_110`；没有新的 moving second-order unit。`rho=h` 时 linear balance unit与 quadratic coefficient恰同处 `2h`，仍留下一个 normalized second-order cancellation，这成为下一层唯一 generic自由。本文不排除 `P_110` 的 modular roots，也未关闭 `rho=h` cancellation，因此不关闭 A2。

---

## 1. exact quadratic transported term

沿用 first-layer point

\[
J_0=J+F/U,
\qquad
R_0=R+K^2L,
\qquad
U=2K-9,
\]

其中

\[
F=F_\Delta,
\qquad
L=\mathscr L_{\rm proj}.
\]

写

\[
C_{tr}:=\frac{65536U^4}{K^8}.
\]

exact transported error为

\[
E_{proj}
=C_{tr}
\left[
\Phi(J_0,R_0)-\Phi(J_0-F/U,R_0-K^2L)
\right].
\]

Euclidean remainder满足

\[
M=E_{proj}-Q(r,u,v_0-L)L,
\]
其中 `v_0=R_0/K^2`。

在 `(F,L)` 中取 total degree 2 的 homogeneous part，直接 Taylor 展开得到

\[
\boxed{
\begin{aligned}
M^{(2)}={}&C_{tr}
\left[
-\frac{\Phi_{JJ}(J_0,R_0)}{2U^2}F^2
+\frac{2(J_0+\zeta)K^2}{U}FL
\right]\\
&+Q_v(r,u,v_0)L^2.
\end{aligned}}
\tag{1.1}

这里 `Phi` 对 `R` 仅一次，所以没有 transported `L^2` 项；最后的 `L^2` 完全来自 Euclidean quotient对 `v` 的变化。

---

## 2. normalize by the homogeneous parent coordinates

balance-tail chain给 exact parent errors

\[
F=K^2s_LY,
\qquad
L=s_L(X+Y),
\]
其中

\[
X=5^\lambda Rstar,
\qquad
Y=g2^mDhat,
\]
且 `s_L` 为 genuine p-unit scale。

在 equal parent depth处写

\[
\chi:=X/Y.
\]

从 (1.1) 抽出 `s_L^2Y^2` 后，quadratic coefficient为

\[
\boxed{
\begin{aligned}
\mathcal Q_2(K,\zeta;\chi):={}&
C_{tr}\left[
-\frac{\Phi_{JJ,0}}{2U^2}K^4
+\frac{2(J_0+\zeta)K^4}{U}(\chi+1)
\right]\\
&+Q_{v,0}(\chi+1)^2,
\end{aligned}}
\tag{2.1}

其中

\[
\Phi_{JJ,0}=\Phi_{JJ}(J_0,R_0),
\]

\[
Q_{v,0}
=\partial_vQ_{63}(1/K,\zeta/K,R_0/K^2).
\]

first-order same-prime recycling已经唯一固定

\[
\boxed{
\chi_{geom}
=-\frac{2\mathcal G_>}{81\mathcal G_<}.}
\tag{2.2}

---

## 3. second-order coefficient has no new denominator gate

将 (2.2) 代入 (2.1)。exact simplification给

\[
\boxed{
\mathcal Q_2(K,\zeta;\chi_{geom})
=
\frac{256\,\mathcal S_2(K,\zeta)}
{81K^4\mathcal G_<^2}.}
\tag{3.1}

其中 `S_2` 取 primitive integer normalization，满足

\[
\boxed{
\deg_{total}\mathcal S_2=16,
\qquad
\deg_\zeta\mathcal S_2=14,}
\tag{3.2}

\[
\boxed{
\#\operatorname{supp}(\mathcal S_2)=150.}
\tag{3.3}

所以二阶 normalization没有产生第三张 denominator sheet；唯一 denominator正是 first-order gate `G_<` 的平方，加上 genuine unit `K`。

---

## 4. eliminate `zeta`: only a central factor and one degree-110 gate

对 `S_2` 与 universal cubic

\[
\mathcal E_{63}(K,\zeta)=0
\]
关于 `zeta` 求 exact resultant。得到

\[
\boxed{
\operatorname{Res}_{\zeta}
(\mathcal E_{63},\mathcal S_2)
=-2^{140}3^{11}(2K-9)^8P_{110}(K).}
\tag{4.1}

其中

\[
\boxed{\deg P_{110}=110,}
\tag{4.2}

并且

\[
\boxed{P_{110}\text{ 在 }\mathbf Q[K]\text{ 中不可约}.}
\tag{4.3}

`P_110` 有111个 nonzero coefficients。正文不抄写巨大系数；checker从 (2.1)--(3.1) canonical 重建 `S_2` 与 resultant，并验证 fixed content、degree与不可约性。

因此 genuine noncentral second-order coefficient若消失，只能进入

\[
\boxed{P_{110}(K)\equiv0\pmod p.}
\tag{4.4}

---

## 5. the second-order coefficient has no real endpoint zero

定义 projective form

\[
\boxed{
\mathcal S_2^{proj}(r,u)
:=r^{16}\mathcal S_2(1/r,u/r).}
\tag{5.1}

它仍有150个 monomials，bidegrees为

\[
\boxed{\deg_r=16,\qquad\deg_u=14.}
\tag{5.2}

真实 endpoint满足

\[
0<r<10^{-3},
\qquad
0<u<10^{-3}.
\]

把 (5.1) 仿射搬到 `[0,1]^2` 并转成 tensor Bernstein basis，共

\[
17\cdot15=255
\]
个 exact rational coefficients。checker验证全部严格为正；其中

\[
\boxed{
\min b_{ij}
=
\frac{198730569009592634141902074605524422074200621380891689557678786752875433}
{3725290298461914062500000000000000000000}>0,}
\tag{5.3}

\[
\boxed{
\max b_{ij}
=162937721250850407546364808657801>0.}
\tag{5.4}

所以

\[
\boxed{
\mathcal S_2(K,\zeta)>0}
\tag{5.5}

在整个真实 dangerous endpoint成立。second-order gate没有 real degeneration；任何 modular root只能来自 p-adic wrapping。

---

## 6. depth trichotomy at the saturated balance layer

继续固定 common baseline

\[
h=v_p(G_\Delta),
\]
及 balance depth

\[
\rho=v_p(B_{63}).
\]

前一 gcd-ladder theorem已证明：

\[
M=M^{(1)}+M^{(\ge2)},
\qquad
v_p(M^{(1)})=h+\rho,
\qquad
v_p(M^{(\ge2)})\ge2h.
\]

### `rho<h`

已有 exact law

\[
\boxed{v_p(M)=h+\rho.}
\tag{6.1}

### `rho>h`

此时

\[
v_p(M^{(1)})>2h.
\]

quadratic term独占可能的 `2h` 层。若 coefficient regular，即

\[
p\nmid K\mathcal G_<,
\]
则

\[
\boxed{
p\nmid\mathcal S_2
\Longrightarrow
v_p(M)=2h.}
\tag{6.2}

因此若

\[
\boxed{\rho>h,\qquad v_p(M)>2h,}
\tag{6.3}

则 genuine noncentral prime必须满足

\[
\boxed{p\mid P_{110}(K).}
\tag{6.4}

### `rho=h`

此时 linear balance term与 quadratic transported term都恰可能处在 `2h` 层。因此还留下一个 normalized second-order cancellation：

\[
\boxed{
\frac{M^{(1)}}{p^{2h}}
+rac{M^{(2)}}{p^{2h}}
\equiv0\pmod p.}
\tag{6.5}

这是当前唯一仍含一个新 normalized unit的 generic second-order branch。

---

## 7. revised second-order frontier

balance saturation现在进一步分成：

- `rho<h`：depth已完全读取；
- `rho>h`：越过 `2h` 只能命中 fixed irreducible `P_110`；
- `rho=h`：恰一整个 baseline 的 balance saturation，留下唯一 second-order normalized cancellation。

因此真正无界 unit自由已经从

\[
\rho\ge h
\]
进一步缩成

\[
\boxed{\rho=h.}
\]

这与 earlier equal-depth bottlenecks再次同型：**过深反而固定化，恰等深才保留 normalized resonance。**

下一步应为 `rho=h` 定义 canonical second-order balance unit / tail，而不再扩大 `P_110` 的 ordinary discriminant分析。

A2 仍为 `待证`。
