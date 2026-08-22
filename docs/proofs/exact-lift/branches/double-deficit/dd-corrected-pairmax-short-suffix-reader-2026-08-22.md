# DD corrected terminal 的 pair-max short-suffix reader

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md`](dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md)、[`dd-corrected-carry-u-pairmax-crt-2026-08-22.md`](dd-corrected-carry-u-pairmax-crt-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood；fixed denominator/S-unit + gap fiber）。**
>
> quantitative pair-max core 不只给 `A_12 mod v_2`。保留 Gaussian orientation后，它还直接给 short numerator block `a_2 mod v_2`。由于 `a_2` 的 digit height只有 `kappa_dig delta S`，而 `v_2` 保持 `(1-C_one delta)S` 高度，所以在
> \[
> \boxed{
> \delta<0.322366428371977\ldots}
> \]
> 时，每个 orientation fiber至多一个 `a_2`。所有 orientation choices总数只有 `10^{o(S)}`。结合上一文件的 `U × v_2` uniqueness，在 `delta<0.238062...` 内 fixed denominator/S-unit data 下 numerator entropy因此进一步降为
> \[
> \boxed{N_{\rm num}\le10^{\delta S+o(S)},}
> \]
> 只剩 sphere-gap fiber。

---

## 1. generic double reconstruction

上一文件已经证明 generic carry

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0,}
\tag{1.1}
\]

其中

\[
\Sigma=2\cdot5^TU+V,
\qquad
(R_0,g_0)=1.
\]

模 `U` 时

\[
\Sigma\equiv V\pmod U.
\]

由 `(U,V)=1`，`(1.1)` 给

\[
U\mid g_0B10^dA_{12}-R_0.
\]

因此定义整数

\[
\boxed{
A_0:=\frac{g_0B10^dA_{12}-R_0}{U}.}
\tag{1.2}
\]

于是 exact reconstruction第一式为

\[
\boxed{
UA_0+R_0=g_0B10^dA_{12}.}
\tag{Rec-1}
\]

把 `(Rec-1)` 乘 `V` 并代回 `(1.1)`：

\[
\begin{aligned}
g_0Ua_3
&=V(UA_0+R_0)-\Sigma R_0\\
&=UVA_0-(\Sigma-V)R_0\\
&=U\left(VA_0-2\cdot5^TR_0\right).
\end{aligned}
\]

约去正整数 `U`：

\[
\boxed{
VA_0-g_0a_3=2\cdot5^TR_0.}
\tag{Rec-2}
\]

所以 equality frontier 中常用的 double reconstruction `(Rec-1),(Rec-2)` 本来就是整个 canonical funnel 的 exact identities；equality 只额外给各 cofactor 的高度信息。

---

## 2. pair-max prime 上 `a_3` 的 fixed residue

固定

\[
p^h\Vert v_2.
\]

上一 pair-max theorem已经证明 target `p` 为 odd split prime，并且在 low denominator baseline `r` 下

\[
p\nmid g_0R_0 10.
\tag{2.1}
\]

因为

\[
p^h\mid V,
\]

对 `(Rec-2)` 模 `p^h`：

\[
\boxed{
g_0a_3\equiv-2\cdot5^TR_0\pmod{p^h}.}
\tag{a3-p}
\]

由 `(2.1)`，`g_0` 是 p-unit，所以 `a_3 mod p^h` 被 fixed gap fiber `(R_0,g_0)` 唯一确定。

---

## 3. Gaussian orientation 把该 residue 转给 `a_2`

在 `(b_2,b_3)` pair-max channel，写

\[
q_{\rm lcm}=\operatorname{lcm}(b_1,b_2,b_3),
\]

\[
c_2:=q_{\rm lcm}/b_2,
\qquad
c_3:=q_{\rm lcm}/b_3.
\tag{3.1}
\]

因为 `b_2,b_3` 在 p 处并列最大：

\[
\boxed{p\nmid c_2c_3.}
\tag{3.2}
\]

sphere coordinates为

\[
y_2=a_2c_2,
\qquad
y_3=a_3c_3.
\]

quantitative one-channel Gaussian carrier可选择 orientation `Pi_delta` 使

\[
N(\Pi_\delta)=v_2,
\qquad
\Pi_\delta^2\mid y_2+i y_3.
\]

对当前 `p^h||v_2`，这意味着存在 `-1` modulo `p^{2h}` 的某一 Hensel root `iota_p`，满足

\[
\boxed{
y_2+\iota_p y_3\equiv0\pmod{p^{2h}}.}
\tag{3.3}
\]

本文只需要降到 `p^h`：

\[
a_2c_2+\iota_p a_3c_3\equiv0\pmod{p^h}.
\]

代入 `(a3-p)`：

\[
\boxed{
 a_2
\equiv
2\cdot5^T\,\iota_p\,
 c_3c_2^{-1}\,R_0g_0^{-1}
\pmod{p^h}.}
\tag{a2-p}
\]

所有 inverse都存在，因为 `(2.1),(3.2)`。

因此固定 denominator/S-unit data、gap fiber与一个 Gaussian orientation后，`a_2` 在每个 `p^h||v_2` 上有唯一 residue。

---

## 4. 聚合 orientation fibers

对奇 split prime `p`，方程

\[
x^2\equiv-1\pmod{p^h}
\]

恰有两个 Hensel lifts，对应 conjugate Gaussian orientations。因此对整个

\[
v_2=\prod p^h
\]

最多有

\[
2^{\omega(v_2)}
\]

个 orientation vectors。

固定一个 orientation vector后，Chinese remainder theorem把 `(a2-p)` 聚合成

\[
\boxed{a_2\equiv\rho_{2,\Omega}\pmod{v_2}.}
\tag{a2-v2}
\]

其中 `Omega` 表示 orientation vector。

还需说明 orientation 数量在 exponential-height 记账中可忽略。若 `k=omega(v_2)`，则 `v_2` 至少含 `k` 个不同奇素数，故

\[
v_2\ge3\cdot5\cdots p_k\ge k!,
\]

对 sufficiently large `k`：

\[
k\log k-k\le\log v_2=O(S).
\]

所以

\[
k=O(S/\log S),
\]

从而

\[
\boxed{2^{\omega(v_2)}=10^{o(S)}.}
\tag{Orientation-entropy}
\]

不需要固定 global Gaussian orientation 才能得到 subexponential fiber count。

---

## 5. short suffix 比 `v_2` 更短的显式 neighborhood

quantitative digit polarization给

\[
\boxed{
 n_2\le\kappa_{\rm dig}\delta S+o(S),
\qquad
\kappa_{\rm dig}=0.767009998554660\ldots.}
\tag{5.1}
\]

而 quantitative one-channel给

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge1-C_{\rm one}\delta-o(1),
\qquad
C_{\rm one}=2.335049992773302\ldots.}
\tag{5.2}
\]

若

\[
1-C_{\rm one}\delta>\kappa_{\rm dig}\delta,
\]

则 sufficiently large `S` 时

\[
v_2>10^{n_2}>a_2.
\]

阈值为

\[
\boxed{
\delta<\delta_{a_2}:=
\frac1{C_{\rm one}+\kappa_{\rm dig}}.}
\tag{5.3}
\]

利用

\[
C_{\rm one}=1+\frac{5(1+2a)}6,
\qquad
\kappa_{\rm dig}=\frac{2+a}{3},
\qquad a=\log_{10}2,
\]

可化成

\[
\boxed{
C_{\rm one}+\kappa_{\rm dig}
=\frac52+2a
=3.102059991327962\ldots,}
\]

故

\[
\boxed{
\delta_{a_2}
=0.322366428371977\ldots.}
\tag{5.4}
\]

在该范围内，每个 orientation vector 的 residue class `(a2-v2)` 在合法 short-digit interval 中至多包含一个 `a_2`。因此

\[
\boxed{
\#\{a_2\mid\text{fixed denominator/S-unit/gap data}\}
\le10^{o(S)}
\quad(\delta<\delta_{a_2}).}
\tag{Short-suffix-collapse}
\]

---

## 6. numerator entropy 只剩 gap fiber

上一 gap-fiber theorem给

\[
\boxed{
\#\{(R_0,g_0)\}
\le10^{\delta S+o(S)}.}
\tag{6.1}
\]

而 carry-`U` × pair-max theorem已经证明，在

\[
\delta<\delta_{UV}=0.238062349248111\ldots
\]

时，固定 `(R_0,g_0,a_2)` 后 `A_12` 至多一个，并进而唯一恢复 `a_1,a_3`。

由于

\[
\delta_{UV}<\delta_{a_2},
\]

在整个 `U × v_2` uniqueness neighborhood内，`a_2` 只有 `10^{o(S)}` orientation entropy。因此：

\[
\boxed{
N_{\rm num}(S;\delta)
\le10^{\delta S+o(S)}
\qquad
(\delta<0.238062349248111\ldots),}
\tag{Numerator-gap-only}
\]

对固定 denominator/S-unit data成立。

这把此前 `1.76700999855 delta S` 的 numerator entropy再次降低，真正剩下的正线性 numerator freedom只有 primitive sphere-gap fiber。

---

## 7. 方法边界与下一目标

`Short-suffix-collapse` 使用的是 pair-max sphere orientation已经支付过的 depth，只做 candidate counting / residue extraction，不把它再次计作 local height surplus。

当前 numerator picture因此进一步变成：

1. `(R_0,g_0)`：至多 `10^{delta S+o(S)}` gap fibers；
2. 每个 gap fiber：`a_2` 只有 `10^{o(S)}` orientation choices；
3. 对 `delta<0.238...`，每个 `(gap,a_2)` fiber 的完整 numerator triple至多一个。

所以下一步最值得攻击的是 gap fiber本身。已有

\[
\frac{R_0}{g_0}
=\frac{H-y_3}{2\cdot5^Tc_3},
\qquad
R_0g_0=10^{\le\delta S+o(S)},
\]

而本文 `(a2-p)` 还给每个 pair-max orientation一个 ratio congruence

\[
g_0a_2c_2
\equiv
2\cdot5^T\iota_p c_3R_0
\pmod{p^h}.
\]

这提供了一个直接连接 small gap fiber 与 near-`S` pair-max modulus 的二维 lattice 接口。若能把该 congruence 的 multiple-solution rays进一步用 reducedness / digit shell切断，gap entropy有机会从 `delta S` 再降到 `o(S)`。

---

## 8. 状态摘要

- **已严格完成：** generic double reconstruction `(Rec-1),(Rec-2)`。
- **已严格完成：** pair-max `a_3 mod p^h` reader。
- **已严格完成：** oriented `a_2 mod p^h` reader与 aggregate `a_2 mod v_2`。
- **已严格完成：** orientation entropy `2^{omega(v_2)}=10^{o(S)}`。
- **已严格完成：** suffix collapse threshold `delta<0.322366428371977...`。
- **已严格完成：** 在 `delta<0.238062...` 内 numerator entropy降为 `delta S+o(S)`，只剩 gap fiber。
- **仍待证：** gap-fiber lattice closure；denominator/S-unit entropy；unique-lift digit-shell exclusion；explicit strict slope gap；DD emptiness与有效绝对高度界。
