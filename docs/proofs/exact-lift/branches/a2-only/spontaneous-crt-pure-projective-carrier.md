# A2 generic pure-spontaneous descendant kernel 的 dimensionless projective carrier

> **依赖：** `spontaneous-crt-pure-prefix-elimination.md`、`spontaneous-sphere-roots.md`、`spontaneous-crt-universal-descendant-cubic.md`。
>
> **严格状态：**此前 generic branch用 `(s,z,c,tau)` 表示，并在 branch quadratic上把 descendant compatibility降成 `A_63 tau+B_63`，最终得到 degree-16 pure-prefix carrier。本文进一步除去无意义的 overall scale：令 `r=tau/s=1/K`、`u=z/s=a_3/(TK)`、`v=c/s^2=Q^2N_0/(B^2K^2)`，则 branch quadratic与 universal descendant cubic都变成完全 dimensionless 的 `(r,u,v)` 系统。消去 `r` 得到 primitive irreducible total-degree-11 projective carrier `X_63^proj(u,v)`，只有59项。对第一张 sphere orientation，exact rational Bernstein certificate证明真实 endpoint映入 `-0.93<u<-0.54`、`0.937<v<0.939`，而 `X_63^proj` 在整个该 rectangle严格为负。因此 branch 1 的最终 descendant compatibility在实 endpoint上完全无根；任何 surviving congruence只能来自 p-adic wrapping。本文不排除 modular roots，也不证明 branch 2 的 real emptiness，因此不关闭 A2。

---

## 1. remove the scale `s`

沿用

\[
s=9+y,
\qquad z=z_i(x,y),
\qquad c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2},
\qquad \tau=10^{-M}.
\]

定义 dimensionless variables

\[
\boxed{
r:=\frac{\tau}{s}=\frac1K,}
\tag{1.1}
\]

\[
\boxed{
u:=\frac zs=\frac{a_3}{TK},}
\tag{1.2}
\]

\[
\boxed{
v:=\frac c{s^2}
=\frac{Q^2N_0}{B^2K^2}.}
\tag{1.3}
\]

最后一个 exact identity已在 `H_24` projective文件中证明。

---

## 2. branch quadratic becomes universal

原 compact branch equation为

\[
55\tau^2+18(z-s)\tau+s^2-4sz-c=0.
\]

除以 `s^2`，得到

\[
\boxed{
\mathscr L_{\rm proj}(r;u,v)
:=55r^2+18(u-1)r+1-4u-v=0.}
\tag{2.1}

这里没有任何 `M,N,s`。

universal descendant cubic同样只依赖

\[
K=1/r,
\qquad
\zeta=u/r.
\]

定义

\[
\boxed{
\mathscr E_{\rm proj}(r,u)
:=r^8\mathcal E_{63}(1/r,u/r).}
\tag{2.2}

它是 degree-8 polynomial in `r`。

所以 generic descendant common condition本质上就是

\[
\boxed{
\mathscr L_{\rm proj}=0,
\qquad
\mathscr E_{\rm proj}=0.}
\tag{2.3}

---

## 3. eliminate `r`: a compact projective carrier

对 (2.1),(2.2) 关于 `r` 取 resultant。全部 coefficient gcd恰为

\[
\boxed{5^7 11^7.}
\tag{3.1}

除去该 fixed content并取 primitive normalization，定义

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u,v)
:=\operatorname{pp}
\operatorname{Res}_r
(\mathscr L_{\rm proj},\mathscr E_{\rm proj}).}
\tag{3.2}

exact audit给

\[
\boxed{
\deg_{\rm total}\mathscr X_{63}^{\rm proj}=11,}
\tag{3.3}
\]

\[
\boxed{
\deg_u\mathscr X_{63}^{\rm proj}
=\deg_v\mathscr X_{63}^{\rm proj}=8,}
\tag{3.4}
\]

\[
\boxed{
\#\operatorname{supp}(\mathscr X_{63}^{\rm proj})=59,}
\tag{3.5}

并且

\[
\boxed{
\mathscr X_{63}^{\rm proj}\text{ 在 }\mathbf Q[u,v]\text{ 中不可约}.}
\tag{3.6}

这就是 degree-16 branch-specific prefix carrier背后的 scale-free核心。

任何 genuine generic pure-spontaneous descendant common prime，除固定 `5,11` 外，都必须满足

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u_i,v)\equiv0\pmod p.}
\tag{3.7}

---

## 4. exact real window for `v`

由

\[
v(x,y)
=\frac{(x+2)^2(2025x^2+y^2)}{100x^2(9+y)^2},
\]
直接求导：

\[
\boxed{
\frac{\partial v}{\partial x}
=\frac{(x+2)(2025x^3-2y^2)}{50x^3(y+9)^2}>0,}
\tag{4.1}
\]
因为

\[
2025x^3-2y^2
>\frac{2025}{1000}-2
=\frac1{40}.
\]

另有

\[
\boxed{
\frac{\partial v}{\partial y}
=-\frac{9(x+2)^2(225x^2-y)}{50x^2(y+9)^3}<0,}
\tag{4.2}
\]
因为 endpoint上

\[
225x^2-y>\frac94-1=\frac54.
\]

所以真实 box

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1
\]
给精确 extremal values

\[
\boxed{
\frac{7497}{8000}
<v
<\frac{234947716}{250493929}.}
\tag{4.3}

特别地

\[
\boxed{
\frac{937}{1000}<v<\frac{939}{1000},}
\tag{4.4}

因为左差恰为 `1/8000`，而

\[
\frac{939}{1000}
-\frac{234947716}{250493929}
=\frac{266083331}{250493929000}>0.
\]

---

## 5. branch 1 maps into a fixed rational `u` interval

第一张 sphere root为

\[
\boxed{
 z_1
=-\frac{A_+A_{sp}}
{400x^2y^3(x+2)^2},}
\tag{5.1}

所以

\[
 u_1
=-\frac{A_+A_{sp}}
{400x^2y^3(x+2)^2(9+y)}.
\tag{5.2}

记正 denominator

\[
D_1:=400x^2y^3(x+2)^2(9+y),
\]

\[
N_1:=A_+A_{sp}>0.
\]

要证明

\[
-\frac{93}{100}<u_1< -\frac{27}{50},
\]
等价于

\[
93D_1-100N_1>0,
\tag{5.3}
\]

\[
50N_1-27D_1>0.
\tag{5.4}

checker把 `(x,y)` box仿射搬到 `[0,1]^2`，对两个 polynomial使用 exact rational Bernstein basis。全部 Bernstein coefficients严格为正；其中最小系数分别为

\[
\boxed{
\frac{1041285803156808768}{6634204312890625}>0,}
\tag{5.5}

\[
\boxed{
\frac{73}{25}>0.}
\tag{5.6}

因此

\[
\boxed{
-\frac{93}{100}<u_1< -\frac{27}{50}.}
\tag{5.7}

---

## 6. exact Bernstein exclusion for branch 1

定义 rational rectangle

\[
\boxed{
\mathcal R_1
=
\left[-\frac{93}{100},-\frac{27}{50}\right]
\times
\left[\frac{937}{1000},\frac{939}{1000}\right].}
\tag{6.1}

由 (4.4),(5.7)，真实 branch-1 image严格位于其内部。

将 `X_63^proj(u,v)` 仿射搬到 unit square，并转成 bidegree `(8,8)` Bernstein basis。checker逐一验证全部

\[
9\times9=81
\]
个 exact rational Bernstein coefficients都严格为负。

其中最大的 coefficient仍为

\[
\boxed{
-\frac{77096177819298948415154163591507164734582999}
{7450580596923828125}<0.}
\tag{6.2}

因此 Bernstein convex-hull property给

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u,v)<0
\qquad((u,v)\in\mathcal R_1).}
\tag{6.3}

于是整个真实 endpoint上

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u_1,v)<0.}
\tag{6.4}

特别地 branch 1 没有任何 real descendant-compatible point。

---

## 7. interpretation

(6.4) 不是 modular empty theorem：prime divisibility只要求

\[
\mathscr X_{63}^{\rm proj}(u_1,v)\equiv0\pmod p,
\]
仍可通过 p-adic wrapping实现。

但它比此前“sphere modular root在负侧、真实 third digit为正”的中间 sign gap更接近最终对象：这里被证明严格离开 real zero的已经是**最终 universal descendant projective carrier本身**。

因此 branch 1 后续若继续，应直接把这个固定负 natural representative与所需 prime-power depth联立，而不应再做 local discriminant stacking。

本文没有对 branch 2 给出同样结论；其 projective carrier在粗 real box上确实可能改变符号，因此 branch 2需另行处理。

---

## 8. updated generic frontier

现在 generic pure-spontaneous descendant-only external sector有统一 compact reader

\[
\mathscr X_{63}^{\rm proj}(u,v).
\]

- branch 1：真实 endpoint上严格负，只有 p-adic wrapping；
- branch 2：仍需独立 global audit；
- coefficient singular `H_4/H_24` 已分别有 short/compact parity carriers。

所以最直接的下一步是给 branch 1 的 negative projective value做 integer clearing与 2-adic/depth budget，同时单独定位 branch 2 的 real zero locus。

A2 仍为 `待证`。
