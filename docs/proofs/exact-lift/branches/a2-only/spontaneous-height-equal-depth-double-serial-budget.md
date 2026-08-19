# A2 double-serial resonance 的 weighted global budget

> **依赖：** `spontaneous-height-equal-depth-serial-gcd-selectors.md`、`spontaneous-height-equal-depth-serial-conjugates.md`、`spontaneous-height-equal-depth-middle-near-pair.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`spontaneous-height-equal-depth-tail-reader.md`。
>
> **严格状态：**canonical selector `Sigma_double` 精确标记两级 serial nodes 都发生 strict-extra 的 genuine targets。本文把这些 primes 的逐素数深度聚合成 global divisibility。double-serial prime满足 `r_B=h<c_p=rho_p<r_+`，因此在 short middle carrier、full tail、actual `E_+` 与 second conjugate `D_E` 中分别承担 `>=2h+1`, `=2h+c_p>=3h+1`, `>=3h+2`, `=2h+c_p` 层。全局得到 `G_dbl^3 rad(G_dbl)^2 | E_+`，以及 exact weighted core `W_dbl | D_E`, `W_dbl rad(G_dbl)|E_+`。本文给出强高度预算但不证明 `G_dbl=1`，因此不关闭 A2。

---

## 1. double-serial prime data

固定 genuine target prime属于 `Sigma_double`。serial gcd selector theorem给

\[
\boxed{
r_B=h<c_p=\rho_p<r_+.}
\tag{1.1}
\]

所有量均为正整数，所以

\[
\boxed{c_p\ge h+1,}
\tag{1.2}
\]

\[
\boxed{r_+\ge c_p+1\ge h+2.}
\tag{1.3}
\]

---

## 2. four carrier depths

middle near-pair给

\[
v_p(C_+)=h+c_p,
\qquad
v_p(C_-)=h.
\]

因此由 (1.2)：

\[
\boxed{v_p(C_+)\ge2h+1.}
\tag{2.1}
\]

full-tail reader给

\[
\boxed{v_p(\Lambda_{\rm dec})=2h+\rho_p=2h+c_p\ge3h+1.}
\tag{2.2}
\]

second serial conjugate在 strict tie上精确满足

\[
\boxed{v_p(D_E)=2h+c_p.}
\tag{2.3}
\]

actual decimal companion则有

\[
v_p(E_+)=2h+r_+.
\]

由 (1.3)：

\[
\boxed{v_p(E_+)\ge2h+c_p+1\ge3h+2.}
\tag{2.4}
\]

所以 double-serial target在 actual sheet上比 exact conjugate还必多至少一层。

---

## 3. baseline/radical aggregate

设所有 genuine double-serial primes组成集合 `E_dbl`。写

\[
\boxed{
G_{\rm dbl}:=\prod_{p\in E_{\rm dbl}}p^{h_p},}
\tag{3.1}
\]

\[
\boxed{
R_{\rm dbl}:=\operatorname{rad}(G_{\rm dbl})
=\prod_{p\in E_{\rm dbl}}p.}
\tag{3.2}
\]

由 (2.4)，逐 prime 有

\[
p^{3h_p+2}\mid E_+.
\]

不同 primes互素，所以

\[
\boxed{
G_{\rm dbl}^3R_{\rm dbl}^2\mid E_+.}
\tag{3.3}
\]

利用 decimal-pair window

\[
0<E_+<1053TN^3,
\]
得到

\[
\boxed{
G_{\rm dbl}^3R_{\rm dbl}^2
<1053TN^3
=1053\cdot10^{m+3M}.}
\tag{3.4}
\]

这比 ordinary deep equal-depth pool 的 `G^2 rad(G)` surcharge严格多出一份 baseline与一份 radical。

---

## 4. immediate corollaries

因为

\[
R_{\rm dbl}\le G_{\rm dbl},
\]
(3.4) 至少给

\[
\boxed{G_{\rm dbl}^3<1053TN^3,}
\tag{4.1}
\]

以及

\[
\boxed{R_{\rm dbl}^5<1053TN^3.}
\tag{4.2}
\]

所以

\[
\boxed{
G_{\rm dbl}< (1053TN^3)^{1/3},}
\tag{4.3}
\]

\[
\boxed{
R_{\rm dbl}< (1053TN^3)^{1/5}.}
\tag{4.4}
\]

第二式特别说明 double-serial distinct-prime support的增长速度只能是总 decimal height的五分之一幂量级。

---

## 5. exact weighted core

更精确地定义

\[
\boxed{
W_{\rm dbl}
:=\prod_{p\in E_{\rm dbl}}p^{2h_p+c_p}.}
\tag{5.1}
\]

second conjugate exact-depth (2.3) 给

\[
\boxed{W_{\rm dbl}\mid D_E.}
\tag{5.2}
\]

actual sheet (2.4) 则逐 prime至少再多一层：

\[
\boxed{W_{\rm dbl}R_{\rm dbl}\mid E_+.}
\tag{5.3}
\]

serial-conjugate window为

\[
0<D_E<1339T^2N^4,
\]
所以

\[
\boxed{W_{\rm dbl}<1339T^2N^4.}
\tag{5.4}
\]

而由 (5.3)：

\[
\boxed{W_{\rm dbl}R_{\rm dbl}<1053TN^3.}
\tag{5.5}
\]

虽然 `D_E` 是 exact weighted baseline reader，actual `E_+` 的更短 Archimedean scale加上 extra radical通常给更强高度约束。

---

## 6. middle/tail companion budgets

由 (2.1)：

\[
\boxed{G_{\rm dbl}^2R_{\rm dbl}\mid C_+.}
\tag{6.1}
\]

middle window给

\[
\boxed{G_{\rm dbl}^2R_{\rm dbl}<843TN^3.}
\tag{6.2}
\]

由 (2.2)：

\[
\boxed{G_{\rm dbl}^3R_{\rm dbl}\mid\Lambda_{\rm dec},}
\tag{6.3}
\]

所以

\[
\boxed{G_{\rm dbl}^3R_{\rm dbl}<45T^2N^3.}
\tag{6.4}
\]

这些是 (3.4) 的 companion budgets；它们可在未来不同 `m/M` cone 中择优使用。

---

## 7. weighted log form

(3.4) 等价于

\[
\boxed{
\sum_{p\in E_{\rm dbl}}(3h_p+2)\log p
<\log1053+(m+3M)\log10.}
\tag{7.1}
\]

而 exact weighted core给

\[
\boxed{
\sum_{p\in E_{\rm dbl}}(2h_p+c_p)\log p
<\log1339+(2m+4M)\log10.}
\tag{7.2}
\]

以及 actual surcharge

\[
\boxed{
\sum_{p\in E_{\rm dbl}}(2h_p+c_p+1)\log p
<\log1053+(m+3M)\log10.}
\tag{7.3}
\]

---

## 8. current role

`Sigma_double` 现在不仅是 canonical support selector，而且其 prime support必须支付三重 baseline加双 radical的 short-decimal成本：

\[
\boxed{G_{\rm dbl}^3R_{\rm dbl}^2<1053TN^3.}
\]

因此 double-serial pool 已不再是可无代价增长的 moving-prime family。后续若能从 global inert parity、square-core residue或 top-defect得到对 `R_dbl` / `G_dbl` 的独立下界，就有机会直接关闭 `Sigma_double`。

A2 仍为 `待证`。
