# DD corrected terminal 的 quantitative one-channel pair-max neighborhood

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、`frontier.md` 中 general reduced-tail moving-core decomposition。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood；固定 `delta<=1/2`）。**
>
> 目的：旧 one-channel theorem只在 equality frontier 中写成 `v_1=10^{o(S)}`, `v_2=10^{S+o(S)}`。本文把它定量化，不预先假设 terminal `C_L` normalization。

## 1. general moving-core decomposition

一般 DD reduced-tail moving odd core有 exact decomposition

\[
\boxed{V=v_1v_2,}
\tag{1.1}
\]

其中：

- `v_1` 对应 pair-max `(b_1,b_3)`；
- `v_2` 对应 pair-max `(b_2,b_3)`；
- canonical denominator normal form给 `v_1|b_1`, `v_2|b_2`。

在 canonical S-unit phase中

\[
G=\gamma V,
\qquad G=b_1b_2,
\qquad (V,10)=1.
\tag{1.2}
\]

交换前两 prefix labels后，quantitative digit polarization取长 denominator为 `b_2`。

## 2. 小 channel 的定量 upper

上一文件证明过程中有

\[
\frac{m_1}{S}
\le
\frac\delta2+\frac b3G_5+\frac R2+o(1),
\tag{2.1}
\]

其中

\[
a=\log_{10}2,
\qquad b=1-a,
\qquad
\lambda=\frac{2+a}{1+2a}.
\]

由 `v_1|b_1` 与 `b_1<10^{m_1}`：

\[
\frac{\log_{10}v_1}{S}
\le
\frac\delta2+\frac b3G_5+\frac R2+o(1).
\]

quantitative defect中

\[
c_{G_5}=\frac{2b(2\lambda-1)}3,
\qquad
c_R=2\lambda-1.
\]

两个 cost ratio相同：

\[
\frac{b/3}{c_{G_5}}
=
\frac{1/2}{c_R}
=
\frac1{2(2\lambda-1)}.
\]

故

\[
\boxed{
\frac{\log_{10}v_1}{S}
\le
\left(\frac12+\frac1{2(2\lambda-1)}\right)\delta+o(1).
}
\]

利用 `1/(2lambda-1)=(1+2a)/3`：

\[
\boxed{
\frac{\log_{10}v_1}{S}
\le
\frac{2+a}{3}\,\delta+o(1)
=0.767009998554660\ldots\,\delta+o(1).
}
\tag{Small-channel}
\]

这与短 digit-block constant恰好相同。

## 3. `gamma` height 的显式 upper

写

\[
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
\Gamma:=\frac{\log_{10}\gamma}{S}=aG_2+bG_5+R.
\]

`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md` 中更精确的中间式为

\[
aG_2
\le
\frac\delta2+aQ_2+\frac b3G_5+\frac R2+o(1).
\]

所以

\[
\Gamma
\le
\frac\delta2
+aQ_2
+\frac{4b}{3}G_5
+\frac{3R}{2}
+o(1).
\tag{3.1}
\]

后三项共用 quantitative-defect budget。其 cost ratios为

\[
\frac{a}{c_{Q_2}}=\frac1{2\lambda},
\]

\[
\frac{4b/3}{c_{G_5}}=\frac2{2\lambda-1},
\]

\[
\frac{3/2}{c_R}=\frac{3}{2(2\lambda-1)}.
\]

最大值为中间项，因此

\[
\boxed{
\Gamma
\le
\left(\frac12+\frac2{2\lambda-1}\right)\delta+o(1).
}
\tag{Gamma-window}
\]

即

\[
\boxed{
\frac{\log_{10}\gamma}{S}
\le
1.568039994218642\ldots\,\delta+o(1).
}
\tag{3.2}
\]

## 4. `V` 仍保持 near-`S` height

因为 `b_i` 分别是 `m_i` 位正整数：

\[
10^{m_i-1}\le b_i<10^{m_i}.
\]

所以

\[
10^{S-2}\le G=b_1b_2<10^S,
\]

即

\[
\frac{\log_{10}G}{S}=1+o(1).
\]

由 `G=gamma V` 与 `(Gamma-window)`：

\[
\boxed{
1-\left(\frac12+\frac2{2\lambda-1}\right)\delta-o(1)
\le
\frac{\log_{10}V}{S}
\le1+o(1).
}
\tag{V-window}
\]

数值 lower coefficient为 `1.568039994218642...`。

## 5. 大 one-channel core

由 `V=v_1v_2`：

\[
\frac{\log v_2}{S}
=
\frac{\log V}{S}-\frac{\log v_1}{S}.
\]

使用 `(Small-channel)` 与 `(V-window)`：

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge
1-C_{\rm one}\delta-o(1),
}
\tag{5.1}
\]

其中

\[
\begin{aligned}
C_{\rm one}
&=
\left(\frac12+\frac2{2\lambda-1}\right)
+\left(\frac12+\frac1{2(2\lambda-1)}\right)\\
&=1+\frac{5}{2(2\lambda-1)}.
\end{aligned}
\]

利用 `1/(2lambda-1)=(1+2a)/3`：

\[
\boxed{
C_{\rm one}
=1+\frac{5(1+2a)}6
=2.335049992773302\ldots.
}
\tag{5.2}
\]

所以

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge
1-2.335049992773302\,\delta-o(1).
}
\tag{Quantitative-one-channel}
\]

当 `delta->0` 时恢复 equality frontier 的 `log v_2=S+o(S)`。

## 6. Gaussian orientation continuation

对 `v_2` 的 odd moving primes，general denominator prime graph与integer sphere仍给：

\[
p\equiv1\pmod4,
\]

并在 `(b_2,b_3)` pair-max channel产生 square-depth Gaussian contact。删去只含 bounded/exceptional coefficient overlap的部分后，可选择 oriented Gaussian integer `Pi_delta` 使

\[
\boxed{
N(\Pi_\delta)=v_2,
\qquad
\Pi_\delta^2\mid y_2+i y_3.
}
\tag{6.1}
\]

因此 corrected terminal neighborhood中仍存在一个 norm height至少

\[
(1-2.335049992774\delta)S-o(S)
\]

的单一 moving Gaussian channel；另一 channel只有 `0.767010 delta S+o(S)` 高度。

## 7. 对 `b_2` 的 consequence

由 `v_2|b_2` 与 `b_2<10^{m_2}`：

\[
\log(b_2/v_2)
\le
m_2-\log v_2+O(1)
\le
C_{\rm one}\delta S+o(S),
\]

故按 logarithmic height：

\[
\boxed{
b_2=v_2\cdot10^{O(\delta S)+o(S)}.}
\tag{7.1}
\]

这就是 equality statement `b_2=C_L*10^{o(S)}` 的 quantitative neighborhood版本。

## 8. 下一接口

现在 one-channel machinery 不再需要先假设 exact equality normalization。后续可把 equality 中的

\[
C_L,\Pi
\]

替换为

\[
C_{L,\delta}:=v_2,
\qquad
\Pi_\delta,
\]

并把所有旧 `10^{o(S)}` coefficient overlap逐项审计为 `10^{O(delta S)+o(S)}`。

首选目标是：

1. quantitative sphere bridge / `Pairmax-GCRT0`；
2. quantitative denominator `R_2` triangle；
3. 判断 `q_c^2 * C_{L,delta}` 的 effective CRT period是否仍超过 prefix digit window一个正线性量。

如果第 3 项在某个固定 `delta_0>0` 仍成立，则 universal fixed-fiber prefix uniqueness会扩展到整个 `c_*-delta_0` neighborhood；再结合 Farey/source-lift counting，有机会产生真正 explicit slope gap。

## 9. 状态摘要

- **已严格完成：** `Small-channel`、`Gamma-window`、`V-window`。
- **已严格完成：** `Quantitative-one-channel`，constant `2.335049992773302...`。
- **结构推进：** equality one-channel `S-o(S)` core 已扩展成 explicit `1-O(delta)` core。
- **仍待证：** neighborhood `q_c` height / quantitative `Pairmax-GCRT0` / Farey strict gap；DD strict improvement、emptiness、effective absolute height。
