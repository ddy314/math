# DD corrected Schmidt slack = Farey criticality defect

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、canonical `t_2=1` S-unit phase。
>
> **严格状态：已严格完成（corrected canonical high funnel）。**
>
> 本文识别 quantitative Schmidt slack 的直接 Diophantine 意义：它恰好测量 `Z/U` 对 smooth rational `5^T/2^H` 的逼近相对于临界 `U^{-2}` 尺度有多宽。因此 equality Farey argument 的临界性不再只是 exponent coincidence，而是一个 exact normalized identity。

## 1. S-unit rational approximation

canonical phase为

\[
\boxed{2^HZ-5^TU=V,}
\tag{1.1}
\]

其中

\[
(U,V)=(U,Z)=(V,Z)=1.
\]

所以

\[
\boxed{
\left|\frac ZU-\frac{5^T}{2^H}\right|
=\frac{V}{2^HU}.}
\tag{1.2}
\]

相对于 reduced fraction denominator `U` 的 natural Farey scale `U^{-2}`，比例因子为

\[
\boxed{
\mathfrak F:=
U^2\left|\frac ZU-\frac{5^T}{2^H}\right|
=\frac{VU}{2^H}.}
\tag{1.3}
\]

## 2. `log mathfrak F` 恰等于 Schmidt slack

写

\[
a=\log_{10}2,
\qquad b=1-a,
\]

\[
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
G_2=\mathfrak g/S,
\quad G_5=g_5/S,
\quad R=\log_{10}\gamma_0/S.
\]

因为

\[
G=\gamma V,
\qquad
\log_{10}G=S+O(1),
\]

有

\[
\frac{\log V}{S}
=1-aG_2-bG_5-R+o(1).
\tag{2.1}
\]

第一条 S-unit pinning

\[
\kappa=2\gamma5^TU,
\qquad
\log\kappa=2S+O(1)
\]

给

\[
\frac{\log U}{S}
=2-aG_2-bG_5-R-b\frac TS+o(1).
\tag{2.2}
\]

2-resonance给

\[
\frac HS=2M+2Q_2+N_2-2G_2+o(1),
\tag{2.3}
\]

5-resonance给

\[
\frac TS=\frac{2M+2Q_5-2G_5+N_5}{3}.
\tag{2.4}
\]

将 `(2.1)--(2.4)` 代入

\[
\frac1S\log\mathfrak F
=
\frac{\log V}{S}+rac{\log U}{S}-a\frac HS
\]

并整理：

\[
\begin{aligned}
\frac1S\log\mathfrak F
={}&3
-\frac{2(1+2a)}3M
-2aQ_2-aN_2\\
&-\frac b3(2Q_5+4G_5+N_5)
-2R+o(1).
\end{aligned}
\]

令

\[
A:=\frac{2(1+2a)}3.
\]

quantitative defect 文件定义 Schmidt slack

\[
\boxed{
\sigma_S
:=3-\left[
AM+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R
\right]\ge-o(1).}
\tag{2.5}
\]

所以得到 exact normalized identification：

\[
\boxed{
\frac1S\log_{10}\frac{VU}{2^H}
=\sigma_S+o(1).}
\tag{Farey-slack}
\]

等价地

\[
\boxed{
\left|\frac ZU-\frac{5^T}{2^H}\right|
=
\frac{10^{\sigma_SS+o(S)}}{U^2}.}
\tag{Farey-critical-form}
\]

## 3. 与 `UZ` rough product 的同一个 slack

两条 S-unit height公式直接相加也给

\[
\boxed{
\frac{\log(UZ)}S=1+\sigma_S+o(1).}
\tag{UZ-slack}
\]

所以同一 `sigma_S` 同时测量：

1. `UZ` 超过 Schmidt critical rough product `10^S` 的高度；
2. `Z/U` Farey cell 相对于 `U^{-2}` spacing被放宽的指数。

这两件事不是两份 defect，而是同一个 projective slack的两个坐标图。

## 4. slope neighborhood 中的显式上界

quantitative defect theorem给

\[
\delta:=c_*-\frac nS
\ge\lambda\sigma_S-o(1),
\]

其中

\[
\lambda=\frac{2+a}{1+2a}=1.436294525872677\ldots.
\]

所以

\[
\boxed{
0\le\sigma_S\le\frac\delta\lambda+o(1).}
\tag{4.1}
\]

数值上

\[
\frac1\lambda
=0.696236\ldots.
\]

故

\[
\boxed{
1-o(1)
\le\frac{\log(UZ)}S
\le1+\frac\delta\lambda+o(1),}
\]

以及

\[
\boxed{
\left|\frac ZU-\frac{5^T}{2^H}\right|
\le
\frac{10^{(\delta/\lambda)S+o(S)}}{U^2}.}
\tag{4.2}
\]

## 5. quantitative Farey counting consequence

在 equality ray `delta->0` 时，`sigma_S->0`，所以 cell width与 reduced fractions 的 critical spacing同指数，恢复旧

\[
N_{\rm frontier}(S)=10^{o(S)}.
\]

对于固定正 `delta`，Farey cell相对 `U^{-2}` spacing最多宽

\[
10^{\sigma_SS+o(S)}
\le10^{(\delta/\lambda)S+o(S)}.
\]

因此纯 Farey separation至多给 neighborhood candidate count

\[
\boxed{
N_{\rm Farey}(S,\delta)
\le
10^{(\delta/\lambda)S+o(S)}.}
\tag{Farey-count}
\]

这里不宣称该 bound 已计入所有 slow-data fibers；它表达 fixed corresponding smooth/exponent fiber内的 projective rational count。

## 6. 方法边界

`Farey-critical-form` 说明一个重要方向判断：当 `delta>0` 时，Schmidt slack使 approximation cell变宽，而不是变窄。于是单纯把 equality Farey argument做 quantitative continuation不会产生 strict slope contradiction。

若要把 `c_*` 改进成显式更小常数，必须有第二个 arithmetic mechanism消耗这份 `sigma_S` entropy，例如：

- large one-channel Gaussian orientation；
- rough source / pair-max transverse modulus；
- 一个 neighborhood-valid square-source CRT；
- 或其它真正独立于 S-unit/Farey projective slack 的条件。

换言之，下一目标可精确表述为：

\[
\boxed{
\text{证明 terminal moving arithmetic 强迫 }
\sigma_S\le c\,\delta
\text{ 之外的额外 positive cost，或直接迫使 }\sigma_S=0.}
\]

## 7. 状态摘要

- **已严格完成：** `Farey-slack`、`Farey-critical-form`、`UZ-slack`。
- **已严格完成：** `sigma_S<=delta/lambda+o(1)`。
- **计数解释：** pure Farey neighborhood最多留下 `10^{(delta/lambda)S+o(S)}` projective candidates。
- **no-go：** quantitative Farey 自身不会产生 strict gap，因为 `delta>0` 使临界 cell变宽。
- **仍待证：** Gaussian/source mechanism 对 `sigma_S` 的额外消耗；explicit strict gap；DD emptiness / effective absolute bound。
