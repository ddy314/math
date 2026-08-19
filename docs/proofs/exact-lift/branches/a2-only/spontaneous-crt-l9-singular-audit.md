# A2 descent singular gate `L_9` 的 support audit

> **依赖：** `spontaneous-crt-descent-overlap-nogo.md`、`spontaneous-crt-f1270-source-audit.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`。
>
> **严格状态：**`Rstar_63/D_63` overlap 的 `K`-resultant除 `F_1270` 外还留下 singular linear gate `L_9=TK-9T-2a_3`。本文证明 `L_9=alpha-3(3T+a_3)`，所以任何 non-3 alpha-supported prime进入该 gate都会强迫 `3T+a_3=0`；这与 target third carrier `R_3=6(3T+a_3)^2+T^2` 立即矛盾。因此整个 genuine equal-depth target support与 `L_9` singular branch完全分离。对 source-common、central、q/height supports，`L_9` 的 resultants均为极短 positive linear carriers。本文仍不排除 generic alpha-free external `L_9` roots，因此不关闭 A2。

---

## 1. the singular linear form

定义

\[
\boxed{L_9:=TK-9T-2a_3.}
\tag{1.1}
\]

真实 concatenated numerator为

\[
\alpha=TK+a_3.
\]

令

\[
\boxed{A_3:=3T+a_3.}
\tag{1.2}
\]

则有 exact identity

\[
\boxed{L_9=\alpha-3A_3.}
\tag{1.3}
\]

所以该 singular gate不是新的任意 third linear form；它直接测量 concatenated numerator与 shifted third coordinate的差。

---

## 2. any alpha-supported non-3 prime is forced into `A_3`

固定 odd prime `p\ne3`。若

\[
p\mid\alpha,
\qquad
p\mid L_9,
\]
由 (1.3)：

\[
\boxed{p\mid A_3=3T+a_3.}
\tag{2.1}
\]

这与 `endpoint-lattice.md` 旧 mixed/saturation audit中的唯一 zero-factor `A_3` 完全一致：`L_9` 在 alpha-supported sector没有产生新的 prime source，只回流到已知 shifted-third saturation。

---

## 3. equal-depth target support is impossible on `L_9`

真正 equal-depth target prime满足

\[
p\mid\omega W_q=\alpha
\]
并且进入 short third carrier

\[
\boxed{
R_3:=6(a_3+3T)^2+T^2
=6A_3^2+T^2.}
\tag{3.1}
\]

若同时 `p|L_9`，由 §2：

\[
p\mid A_3.
\]

于是

\[
R_3\equiv T^2\pmod p.
\]

所有 genuine target prime与 `10` 分离，所以 `p∤T`。故

\[
\boxed{p\nmid R_3,}
\]
与 target condition矛盾。

因此

\[
\boxed{
\operatorname{Supp}_{\rm target}^{\rm gen}
\cap
\operatorname{Supp}(L_9)
=\varnothing.}
\tag{3.2}
\]

这对 entire equal-depth target pool成立，不留 fixed exception。

结合 `spontaneous-crt-f1270-source-audit.md`：descent-overlap的两个 singular branches在 target sector已经完全分类为

\[
\boxed{
L_9:\ \varnothing,
\qquad
F_{1270}:\ \{7,79,107,199\}.}
\tag{3.3}
\]

所以 moving equal-depth target不能藏在 descent overlap的 singular locus中。

---

## 4. source-common overlap pays `107T+36a_3`

source-common linear sheet为

\[
18K-55.
\]

直接 resultant：

\[
\boxed{
\operatorname{Res}_K(L_9,18K-55)
=107T+36a_3.}
\tag{4.1}
\]

定义

\[
\boxed{L_9^{src}:=107T+36a_3.}
\tag{4.2}
\]

endpoint给

\[
1<a_3/T<251/250,
\]
所以

\[
\boxed{
143T<L_9^{src}<144T.}
\tag{4.3}
\]

因此 singular `L_9` 若与 source-common pool复用 prime，要支付给一个只有 `m+3` 位量级的 positive third-block linear integer。

---

## 5. central overlap pays `9T+4a_3`

与 central additive gate

\[
2K-9
\]
消元：

\[
\boxed{
\operatorname{Res}_K(L_9,2K-9)
=9T+4a_3.}
\tag{5.1}
\]

定义

\[
\boxed{L_9^{cen}:=9T+4a_3.}
\tag{5.2}
\]

则

\[
\boxed{
13T<L_9^{cen}<14T.}
\tag{5.3}
\]

所以 central/singular reuse同样由一个极短 positive third integer读取；不存在 free central overlap。

---

## 6. q/height overlap pays `CT+2DA_3`

source/height linear equation为

\[
DK-(3D-C)=0.
\]

resultant：

\[
\boxed{
\operatorname{Res}_K(
L_9,DK-(3D-C))
=CT+6DT+2Da_3.}
\tag{6.1}
\]

使用 `A_3=3T+a_3`：

\[
\boxed{
L_9^{H}:=CT+2DA_3.}
\tag{6.2}
\]

它显然 positive。归一化：

\[
\frac{L_9^{H}}{DT}
=\frac CD+2\left(3+\frac{a_3}{T}\right).
\]

所以

\[
\boxed{
8<\frac{L_9^{H}}{DT}<\frac{201}{25}.}
\tag{6.3}
\]

即 `q` denominator或 `W_q` height support若命中 `L_9`，完整 first-layer contact被压到一个约 `8DT` 的 source/third natural carrier。

---

## 7. target quadratic resultant is only the old `sqrt(-6)` shadow

若只把 `L_9` 与 target prefix quadratic

\[
P(K)=6K^2-36K+55
\]
消元，得到

\[
\boxed{
\operatorname{Res}_K(P,L_9)
=217T^2+144Ta_3+24a_3^2.}
\tag{7.1}
\]

其关于 `a_3` 的 discriminant为

\[
\boxed{-96T^2=-6(4T)^2.}
\tag{7.2}
\]

所以 ordinary quadratic character只重复 target已有 `sqrt(-6)` shadow。真正排除 target的是 §3 的 exact `alpha/A_3/R_3` argument，而不是这个 Legendre condition。

---

## 8. revised singular frontier

对 descent-overlap singular locus：

- `L_9` 与 entire genuine target pool完全分离；
- `L_9` 与 source-common、central、q/height support的 intersections分别进入约 `143T`、`13T`、`8DT` 的短 carriers；
- alpha-supported overlap只回到 old `A_3` saturation channel；
- target quadratic resultant本身只是旧 `sqrt(-6)` character。

所以 singular moving difficulty现在只剩 **generic alpha-free, source-free, noncentral external `L_9` roots**，以及 `F_1270` 的 generic external roots。它们不再能免费复用 equal-depth target pool。

A2 仍为 `待证`。
