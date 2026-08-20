# A2 `H_24` coefficient singularity 的 projective elimination 与 real exclusion

> **依赖：** `spontaneous-crt-pure-coefficient-singular.md`、`spontaneous-crt-pure-h4-projective-center.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**`A_63=B_63=0` 的 coefficient-singular locus 已分成 projective gates `H_4(s,z)=0` 与 `H_24(s,z)=0`。低次 `H_4` 已进一步压成固定 projective norm center。本文处理高次 `H_24`：最后一次 subresultant 在 `H_24` component 上仍只有一次 `v=c/s^2` 自由，写成 `a_15(u)v+b_17(u)=0`；消去 `u=z/s` 得到一个 primitive irreducible degree-24 polynomial `P_24(v)`。精确 Sturm 计数证明 `P_24` 的四个实根分别落在 `(-7,-6),(-6,-5),(6/5,5/4),(16,17)`，因而真实 endpoint 的 `0<v<21/20` 完全不可能。该结论只排除实退化；模素数的 `p`-adic wrapping 仍可能存在，所以不关闭 A2。

---

## 1. projective variables

沿用 coefficient-singular remainder

\[
A_{63}(s,z,c)\tau+B_{63}(s,z,c).
\]

定义 projective ratios

\[
\boxed{
u:=\frac zs,\qquad v:=\frac c{s^2}.}
\tag{1.1}
\]

其中 genuine branch 中 `s` 为 unit。把 `s=1,z=u,c=v` 代入：

\[
\boxed{
A(u,v):=A_{63}(1,u,v),
\qquad
B(u,v):=B_{63}(1,u,v).}
\tag{1.2}
\]

已有

\[
\deg_v A=3,
\qquad
\deg_v B=4.
\tag{1.3}
\]

`spontaneous-crt-pure-coefficient-singular.md` 已证明

\[
\operatorname{Res}_v(A,B)
=\text{fixed content}\cdot h_4(u)h_{24}(u),
\tag{1.4}
\]

其中 `h_24` primitive irreducible，次数 `24`。

---

## 2. `H_24` component 上 `v` 仍只有一层自由

对 `A,B` 关于 `v` 取 subresultant sequence。最后一个正次数 subresultant 恰为一次式：

\[
\boxed{
S_1(u,v)=a_{15}(u)v+b_{17}(u).}
\tag{2.1}
\]

其中 primitive coefficient polynomials 满足

\[
\boxed{
\deg a_{15}=15,
\qquad
\deg b_{17}=17,}
\tag{2.2}
\]

并且二者在 `Q[u]` 中均不可约。

因此在任意 characteristic-zero `H_24` common point上，`v` 不会重新成为独立参数；若 `a_15(u)\ne0`，则

\[
\boxed{
v=-\frac{b_{17}(u)}{a_{15}(u)}.}
\tag{2.3}
\]

模素数时，`a_15` 与 `h_24` 的 fixed resultant support需要单列为 coefficient exceptions；这仍是固定 prime set，不产生 moving two-dimensional Hensel sheet。

---

## 3. eliminate `u`: a single degree-24 norm-ratio polynomial

定义 canonical projected polynomial

\[
\boxed{
\mathscr P_{24}(v)
:=\operatorname{pp}_{\mathbf Z[v]}
\operatorname{Res}_u
\bigl(h_{24}(u),a_{15}(u)v+b_{17}(u)\bigr),}
\tag{3.1}
\]

并取 leading coefficient为正的 primitive normalization。

checker 直接从 universal cubic、branch quadratic 与 subresultant sequence重建该对象。精确得到

\[
\boxed{
\deg\mathscr P_{24}=24,
\qquad
\#\operatorname{supp}(\mathscr P_{24})=25,}
\tag{3.2}
\]

以及

\[
\boxed{
\mathscr P_{24}\text{ 在 }\mathbf Q[v]\text{ 中不可约}.}
\tag{3.3}
\]

正文不抄写 25 个巨大 coefficient；(3.1) 是 canonical exact definition，而 checker验证 primitive normalization、次数、support与不可约性。

任何 real coefficient-singular point落在 `H_24` component时，都必须满足

\[
\boxed{\mathscr P_{24}(v)=0.}
\tag{3.4}
\]

---

## 4. exact Sturm audit

对 `P_24` 使用 exact rational Sturm root count，得到

\[
\boxed{
N_{\mathbf R}(\mathscr P_{24})=4.}
\tag{4.1}
\]

并且四个实根分别且唯一地位于

\[
\boxed{
(-7,-6),
\quad(-6,-5),
\quad\left(\frac65,\frac54\right),
\quad(16,17).}
\tag{4.2}
\]

四个区间已经贡献全部四个实根，因此不存在其它 real root。

特别地

\[
\boxed{
N_{(0,21/20)}(\mathscr P_{24})=0.}
\tag{4.3}
\]

这完全是整数/有理 Sturm certificate，不依赖 floating-point root approximation。

---

## 5. real endpoint exclusion

真实 dangerous endpoint 的 norm ratio为

\[
\boxed{
v_{\rm end}
=\frac c{s^2}
=\frac{(x+2)^2(2025x^2+y^2)}
{100x^2(9+y)^2}.}
\tag{5.1}
\]

`H_4` projective audit 已严格证明统一窗口

\[
\boxed{0<v_{\rm end}<\frac{21}{20}.}
\tag{5.2}
\]

结合 (4.3)：

\[
\boxed{
\text{真实 endpoint 上不存在 real }H_{24}
\text{ coefficient-singular point}.}
\tag{5.3}
\]

所以 `H_24` 与 `H_4` 一样，任何 surviving congruence都必须来自真正的 `p`-adic wrapping，而不可能来自实数 singular geometry。

注意 `H_24` 与 `H_4` 的刚性程度仍不同：`H_4` generic component把 `v` 压成固定常数 `3097/1296`，而 `H_24` 只给 algebraic degree-24 projection `P_24(v)=0`。

---

## 6. updated coefficient-singular frontier

coefficient-singular escape现分成：

1. `H_4`：统一 short degree-4 prefix carrier `V_4`，并有 primitive `7 mod 8` parity surcharge；
2. `H_24`：projective `v` 被 degree-24 irreducible `P_24` 控制，且 real endpoint interval完全无根。

两支都已经排除 real singular degeneration，也都没有重新长回自由 `(tau,c)` sheet。

因此后续不应继续对 `h_24` 做普通 discriminant hunting。更值得做的是：

- 把 `P_24(v)` 清回 compact pure-prefix natural carrier并估计其 primitive parity/height；或
- 回到 generic `A_63\ne0` 的 degree-16 pure-prefix carrier，和 `Lambda_tail` / descendant common gcd 做全局 depth-product budget。

A2 仍为 `待证`。
