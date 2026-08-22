# DD corrected terminal neighborhood 的 gap-fiber entropy

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md`](dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md)、[`dd-corrected-neighborhood-square-source-crt-2026-08-22.md`](dd-corrected-neighborhood-square-source-crt-2026-08-22.md)、[`dd-corrected-high-funnel-schmidt-2026-08-22.md`](dd-corrected-high-funnel-schmidt-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood；固定 denominator/S-unit data 的计数结论）。**
>
> 上一文件把 equality-only pair-max fixed CRT扩展到整个 quantitative terminal neighborhood，但 fixed primitive/source fiber仍包含 `R_0,g_0,a_2`。本文证明：`R_0/g_0` 恰是 sphere gap除掉全部 forced decimal baseline后的 10-unit quotient；其 numerator/denominator 的联合高度由同一 slope defect直接控制。结合 short numerator block与 full `v_2` period，得到 fixed denominator/S-unit data 下 numerator family 的显式 entropy bound
>
> \[
> \boxed{
> N_{\rm num}(S;\delta)
> \le
> 10^{C_{\rm ent}\delta S+o(S)},
> \qquad
> C_{\rm ent}=4.102059991327962\ldots.}
> \]
>
> 当 `delta->0` 时恢复 terminal `10^{o(S)}` entropy collapse 的 quantitative 版本。

---

## 1. `R_0/g_0` 的 exact gap quotient

上一文件从 general overlap equations定义

\[
\frac{R_0}{g_0}
=\frac{La_0}{2\cdot5^T\varepsilon}
\]

为最低项。`core.md` §37 有

\[
c_3=\varepsilon c,
\]

而 §38 给

\[
H_{\rm sph}-y_3=cLa_0.
\]

因此 exact 地

\[
\boxed{
\frac{R_0}{g_0}
=
\frac{H_{\rm sph}-y_3}
{2\cdot5^T c_3}.}
\tag{Gap-fiber-ratio}
\]

这个式子不依赖 equality frontier。

---

## 2. denominator 的 2/5-part恰好全部约掉

canonical `t_2=1` funnel 中 `b_3` 是二进 unique maximum。已有 exact shallow-gap theorem

\[
\boxed{v_2(H_{\rm sph}-y_3)=1,}
\tag{2.1}
\]

并且

\[
\boxed{v_2(c_3)=0.}
\tag{2.2}
\]

所以 `(Gap-fiber-ratio)` 在 2-adic place 的 numerator/denominator深度都恰为 `1`。

corrected 5-adic gap ledger记

\[
\delta_5:=E_5-B_5=v_5(c_3),
\]

并严格给

\[
\boxed{v_5(H_{\rm sph}-y_3)=T+\delta_5.}
\tag{2.3}
\]

因此 `(Gap-fiber-ratio)` denominator 的 5-depth为

\[
T+v_5(c_3)=T+\delta_5,
\]

与 numerator完全相同。

把 `(Gap-fiber-ratio)` 约成最低项后：

\[
\boxed{(R_0g_0,10)=1.}
\tag{Gap-fiber-10-unit}
\]

而且若记

\[
G_-:=\operatorname{core}_{10}(H_{\rm sph}-y_3),
\qquad
C_3:=\operatorname{core}_{10}(c_3),
\]

则 ordinary fraction reduction直接给

\[
\boxed{R_0\mid G_-,\qquad g_0\mid C_3.}
\tag{2.4}

---

## 3. `R_0` 与 `g_0` 分别由两个已有 defect 支付

定义上一文件的 rough-gap normalized height

\[
P_{\rm gap}
:=\frac1S\log_{10}G_-.
\]

于是 `(2.4)` 给

\[
\boxed{
\frac{\log_{10}R_0}{S}
\le P_{\rm gap}.}
\tag{3.1}
\]

另一方面 exact normalized overlap为

\[
\widehat g=\frac\gamma{c_3}\in\mathbf Z_{>0}.
\]

所以

\[
\boxed{c_3\mid\gamma.}
\tag{3.2}
\]

删除 2/5-parts后：

\[
C_3\mid\gamma_0,
\]

其中

\[
R:=\frac1S\log_{10}\gamma_0.
\]

因此

\[
\boxed{
\frac{\log_{10}g_0}{S}
\le R.}
\tag{3.3}

上一文件已把 `P_gap` 加回 corrected quantitative defect：

\[
\delta
\ge
(2\lambda_*-1)R+P_{\rm gap}
+\text{其它非负项}-o(1),
\]

其中

\[
\lambda_*=\frac{2+\log_{10}2}{1+2\log_{10}2},
\qquad
2\lambda_*-1=1.872589051745\ldots>1.
\]

所以

\[
\boxed{
P_{\rm gap}+R\le\delta+o(1).}
\tag{3.4}

由 `(3.1),(3.3)`：

\[
\boxed{
\frac{\log_{10}(R_0g_0)}S
\le\delta+o(1).}
\tag{Gap-fiber-height}
\]

这比单独使用 `R_0=10^{O(delta S)}`、`g_0=10^{O(delta S)}` 后相加更强，因为二者共用同一 quantitative-defect budget。

---

## 4. `(R_0,g_0)` pair 的计数

由 `(Gap-fiber-height)`：

\[
R_0g_0
\le10^{\delta S+o(S)}.
\]

正整数 pairs满足 `xy<=X` 的数量为

\[
\sum_{x\le X}\left\lfloor\frac Xx\right\rfloor
\le X(1+\log X).
\]

因此

\[
\boxed{
\#\{(R_0,g_0)\}
\le10^{\delta S+o(S)}.}
\tag{Gap-fiber-count}
\]

这里还没有使用 `R_0/g_0` 必须来自同一个 exact sphere gap；所以这是安全的粗 upper。

---

## 5. short numerator suffix `a_2` 的 entropy

quantitative digit polarization在交换 prefix labels后给

\[
\boxed{
n_2\le\kappa_{\rm dig}\delta S+o(S),}
\qquad
\kappa_{\rm dig}
=\frac{2+\log_{10}2}{3}
=0.767009998554660\ldots.
\tag{5.1}

因为 `a_2` 恰有 `n_2` 位：

\[
\boxed{
\#\{a_2\}
\le10^{\kappa_{\rm dig}\delta S+o(S)}.}
\tag{5.2}

`n_2` 本身只有 `O(S)` 种可能，吸收进 `10^{o(S)}`。

---

## 6. fixed `(a_2,R_0,g_0)` fiber 中 pair-max period控制 `A_12`

上一文件证明，对 fixed primitive/source data，`A_12` 落在一个 fixed residue class modulo整个 quantitative one-channel core

\[
v_2.
\]

并且

\[
\frac{\log_{10}v_2}{S}
\ge1-C_{\rm one}\delta-o(1),
\]

\[
C_{\rm one}=2.335049992773302\ldots.
\tag{6.1}

`d_3`-dominant surplus simplex给

\[
n_1+n_2=S+s_1+s_2\le S+2,
\]

所以

\[
0<A_{12}<10^{S+2}.
\]

一个 residue class modulo `v_2` 在该区间内至多包含

\[
1+\frac{10^{S+2}}{v_2}
\]

个整数。因此

\[
\boxed{
\#\{A_{12}\mid a_2,R_0,g_0,\text{ denominator/S-unit data}\}
\le
10^{C_{\rm one}\delta S+o(S)}.}
\tag{6.2}

注意这里没有使用 source-square `q_Q^2` period；因此也不需要额外固定 `a_3`。

---

## 7. `a_3` 在 fixed carry fiber 中唯一恢复

exact generic carry为

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.}
\tag{7.1}

固定 denominator/S-unit data、`A_12,R_0,g_0` 后，右边完全固定。因此合法正整数 `a_3` 若存在则至多一个。

而 `A_12=a_1 10^{n_2}+a_2` 在 fixed `(a_2,n_2)` 后也唯一恢复 `a_1`。

所以 numerator triple 的自由度已经全部被

\[
(a_2,R_0,g_0,A_{12})
\]

覆盖。

---

## 8. quantitative numerator entropy collapse

将 `(Gap-fiber-count)`、`(5.2)`、`(6.2)` 相乘：

\[
\boxed{
N_{\rm num}(S;\delta)
\le
10^{C_{\rm ent}\delta S+o(S)},}
\tag{8.1}

其中

\[
\boxed{
C_{\rm ent}
:=1+\kappa_{\rm dig}+C_{\rm one}
=4.102059991327962\ldots.}
\tag{8.2}

也就是

\[
\boxed{
N_{\rm num}(S;\delta)
\le
10^{4.102059991328\,\delta S+o(S)}.}
\tag{Neighborhood-numerator-entropy}
\]

对 `delta->0` 的任何 sequence：

\[
\boxed{N_{\rm num}(S;\delta)=10^{o(S)}.}
\]

因此旧 equality terminal 的 numerator entropy collapse并不只存在于一条极限射线；它有一个显式 Lipschitz quantitative continuation。

---

## 9. 与 source-square CRT 的关系

`dd-corrected-neighborhood-square-source-crt-2026-08-22.md` 还给出高度

\[
\log q_Q\ge(z_*-\delta)S-o(S)
\]

的 square-source period。

若进一步固定 `a_3`，它与 `v_2` 在

\[
\delta<0.142505197463905\ldots
\]

时把 `A_12` 直接压到至多一个。本文的 `(Neighborhood-numerator-entropy)` 更弱，但固定 data更少：它允许 `a_3` 随 `A_12` 通过 carry自动变化。

下一步若能把 source-square congruence与 carry联立后保留一份大 transverse period，就可以把 coefficient `C_ent` 明显继续压低。

---

## 10. 状态边界

`Neighborhood-numerator-entropy` 仍不产生 DD emptiness或 explicit global slope gap。它固定 denominator/S-unit data；这些 denominator data 自身仍可能拥有指数级 family。

当前两个最自然的 continuation 是：

1. **source/carry transverse split**：量化 `q_Q^2` 在消去 `a_3` 后损失到 `Sigma` 的部分；
2. **denominator entropy**：使用 `Q=Uq`、`b_3=BVq`、one-channel `v_2` 与 Farey slack，量化满足同一 canonical phase 的 denominator/S-unit data 数量。

前者更接近获得新的独立 period；后者更接近全 family counting。

---

## 11. 状态摘要

- **已严格完成：** `Gap-fiber-ratio`。
- **已严格完成：** 2/5-parts exact cancellation，故 `(R_0g_0,10)=1`。
- **已严格完成：** `R_0|core10(H-y3)`、`g_0|core10(c_3)`。
- **已严格完成：** `Gap-fiber-height`, `log(R_0g_0)<=delta S+o(S)`。
- **已严格完成：** `(R_0,g_0)` entropy `<=10^{delta S+o(S)}`。
- **已严格完成：** fixed denominator/S-unit data 下 `Neighborhood-numerator-entropy`，coefficient `4.102059991327962...`。
- **待证：** source/carry transverse period；denominator/S-unit entropy；explicit strict gap；DD emptiness与有效绝对高度界。
