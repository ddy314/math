# A2 descendant-only external 的 unequal parent-depth branches 只剩 fixed projective gates

> **依赖：** `spontaneous-crt-descendant-linear-depth-reader.md`、`spontaneous-crt-descendant-transport-resonance.md`、`spontaneous-crt-descendant-quotient-gate.md`。
>
> **严格状态：**记 `a=v_p(Rstar_63)`、`b=v_p(Dhat_63)`。generic same-prime linear-tail recycling此前仍可能来自 transported error与 Euclidean quotient的 normalized cancellation。本文证明当 `a!=b` 时，parent descent已经把所有 normalized unit ratio固定：若 `a<b`，transport baseline只来自 additive error `L_proj`；若 `b<a`，exact normalization给 `F_0=K^2L_0`。因此 `M_63` overdepth分别等价于两个只依赖 `(K,zeta)` 的 coefficient gates `G_<,G_>`。每个 gate清分母后总次数6、28项；与 universal cubic消去 `zeta` 后各得到一个 irreducible degree-48 pure-K polynomial。projective forms在真实 `0<r,u<10^-3` box都严格为负，所以 unequal-depth recycling只能通过 p-adic wrapping。真正仍保留自由 normalized unit ratio的 generic parent branch因此只剩 `a=b`。本文没有排除两个 degree-48 modular gates，因此不关闭 A2。

---

## 1. exact normalizations of `L` and `F`

记

\[
a:=v_p(\mathscr R_{63}^\star),
\qquad
b:=v_p(\widehat{\mathscr D}_{63}),
\qquad
k:=\min(a,b).
\]

projective additive error满足 exact scaling

\[
\boxed{
\widehat{\mathcal T}_2
=\frac{5^mB^2K^2}{2^{2M+2}}\,L,}
\tag{1.1}

其中

\[
L:=\mathscr L_{\rm proj}.
\]

验证只需用

\[
K^2L=R_0-R,
\qquad
R=Q^2N_0/B^2,
\]
以及 `widehat(T)_2` 的 explicit formula。

另一方面 descendant error满足

\[
\boxed{
\widehat{\mathscr D}_{63}
=c_u^2gT\,F,}
\tag{1.2}

其中

\[
F:=F_\Delta.
\]

所有显示 scale在 genuine external odd prime上均为 units。

parent descent为

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\tag{1.3}

---

## 2. case `a<b`: `F` is deeper and `L` alone controls the baseline

若

\[
\boxed{a<b,}
\tag{2.1}

则由 (1.3)

\[
v_p(\widehat T_2)=a=k,
\]
所以

\[
v_p(L)=k,
\qquad
v_p(F)=b>k.
\]

transport theorem的一阶式因此模 `p^(k+1)` 只剩 `L` 项：

\[
\frac{E_{proj}}{p^k}
\equiv
C_<\,L_0
\pmod p,
\tag{2.2}

其中在 first-layer point

\[
J=J_0(K,\zeta),
\qquad
R=R_0(K,\zeta),
\]
有

\[
\boxed{
C_<
:=-\frac{65536(2K-9)^4}{K^6}
(J_0+\zeta)^2.}
\tag{2.3}

Euclidean division

\[
M=E-Q L
\]
给

\[
\frac M{p^k}
\equiv(C_<-Q_0)L_0\pmod p,
\tag{2.4}

其中

\[
Q_0:=Q_{63}(1/K,\zeta/K,R_0/K^2).
\]

所以

\[
\boxed{
a<b,\quad v_p(M)>k
\Longrightarrow
C_<-Q_0\equiv0\pmod p.}
\tag{2.5}

在 coefficient units成立时反向也成立。

---

## 3. case `b<a`: the two real errors have a fixed ratio

若

\[
\boxed{b<a,}
\tag{3.1}

则 (1.3) baseline由 descended quotient独占：

\[
\widehat T_2/p^b
\equiv
g2^m\widehat D_{63}/p^b
\pmod p.
\]

由 (1.1),(1.2) 比较 normalized units：

\[
\frac{L_0}{F_0}
=
\frac{2^{2M+2}}{5^mB^2K^2}
\cdot g2^m
\cdot c_u^2gT.
\]

使用

\[
B^2=2^{2M+2m+2}c_u^2g^2,
\qquad
T=2^m5^m,
\]
所有 source scales精确抵消：

\[
\boxed{L_0/F_0=1/K^2,}
\tag{3.2}

即

\[
\boxed{F_0=K^2L_0.}
\tag{3.3}

因此 transported first-order coefficient退化为纯几何量

\[
\boxed{
C_>
:=\frac{65536(2K-9)^3}{K^6}
\left[
\Phi_J(J_0,R_0)
-(2K-9)(J_0+\zeta)^2
\right].}
\tag{3.4}

于是

\[
\frac M{p^k}
\equiv(C_>-Q_0)L_0\pmod p,
\]
并有

\[
\boxed{
b<a,\quad v_p(M)>k
\Longrightarrow
C_>-Q_0\equiv0\pmod p.}
\tag{3.5}

所以第二个 unequal-depth branch也没有未知 residual-unit ratio。

---

## 4. two compact degree-6 coefficient gates

定义

\[
\boxed{
\mathcal G_<
:=\operatorname{pp}_{\mathbf Z[K,\zeta]}
\operatorname{num}(C_<-Q_0),}
\tag{4.1}

\[
\boxed{
\mathcal G_>
:=\operatorname{pp}_{\mathbf Z[K,\zeta]}
\operatorname{num}(C_>-Q_0).}
\tag{4.2}

exact audit给

\[
\boxed{
\deg\mathcal G_<
=\deg\mathcal G_>=6,}
\tag{4.3}

\[
\boxed{
\#\operatorname{supp}(\mathcal G_<)
=\#\operatorname{supp}(\mathcal G_>)=28.}
\tag{4.4}

两者 denominator只含 fixed `5^7 11^7 K^6`，在 genuine branch为 units。

---

## 5. eliminate `zeta`: two irreducible degree-48 `K` gates

与 universal cubic

\[
\mathcal E_{63}(K,\zeta)=0
\]
分别消去 `zeta`。exact resultants为

\[
\boxed{
\operatorname{Res}_{\zeta}(E_{63},G_<)
=-2^{54}3^3\,P_{48,<}(K),}
\tag{5.1}

\[
\boxed{
\operatorname{Res}_{\zeta}(E_{63},G_>)
=-2^{51}3^5\,P_{48,>}(K).}
\tag{5.2}

两个 primitive polynomials均满足

\[
\boxed{
\deg P_{48,<}=\deg P_{48,>}=48,}
\tag{5.3}

并且在 `Q[K]` 中均不可约。

正文不抄写两个49-coefficient大多项式；checker由 (4.1),(4.2) canonical 重建并核对 degree、content与不可约性。

因此每个 unequal-depth same-prime recycling candidate的 `K mod p` 都必须落入固定 degree-48 algebraic gate；不再存在自由 normalized unit。

---

## 6. projective real exclusion

令

\[
r=1/K,
\qquad
u=\zeta/K.
\]

将 (4.1),(4.2) projectivize：

\[
\boxed{
G_<^{proj}(r,u)
=r^6G_<(1/r,u/r),}
\tag{6.1}

\[
\boxed{
G_>^{proj}(r,u)
=r^6G_>(1/r,u/r).}
\tag{6.2}

primitive normalization后两者仍恰有28项、总次数6。

实际 endpoint满足远强于下列 box的条件：

\[
0<r<1/1000,
\qquad
0<u<1/1000.
\]

对两个 projective gates分别做 exact tensor Bernstein audit，全部49个 coefficients严格为负。

对 `G_<^proj`：

\[
\boxed{
-\frac{112029905407645176473437498709}
{976562500000000}
\le b_{ij}
\le-104415810491281<0.}
\tag{6.3}

对 `G_>^proj`：

\[
\boxed{
-\frac{9078214206708903545409301301679}
{1953125000000000}
\le b_{ij}
\le-4264617552904693<0.}
\tag{6.4}

所以真实 endpoint上

\[
\boxed{G_<^{proj}<0,\qquad G_>^{proj}<0.}
\tag{6.5}

unequal-depth gates没有 real degeneration；任何 surviving root只能是 p-adic wrapping。

---

## 7. updated generic frontier

parent-depth split现在变成：

- `a<b`：overdepth只能命中 fixed `G_<` / `P_48,<`；
- `b<a`：overdepth只能命中 fixed `G_>` / `P_48,>`；
- `a=b`：normalized parent sum允许真正的 free unit ratio，仍需单独 resonance analysis。

因此 generic same-prime recycling中，**唯一仍保留 valuation-unit自由的 parent branch已经严格缩成 equal depth `a=b`**。

这与早先 omega-height equal-depth bottleneck的结构非常相似，下一步应直接为 `a=b` 构造 canonical parent resonance tail，而不再继续扩大 unequal-depth fixed gates。

A2 仍为 `待证`。
