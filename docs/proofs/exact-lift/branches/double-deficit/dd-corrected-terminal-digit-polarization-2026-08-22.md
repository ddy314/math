# DD corrected terminal 的 quantitative digit polarization

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-neighborhood-geometry-2026-08-22.md`](dd-corrected-terminal-neighborhood-geometry-2026-08-22.md)，以及 `high-funnel-ledger.md` 中不依赖旧 discriminant-root 误识别的 d-dominant small-factor Archimedean upper。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` high-funnel 的渐近 neighborhood consequence）。**
>
> 本文把 equality ray 上的 prefix digit polarization 定量化：若 `n/S` 距 corrected frontier `c_*` 只有 `delta`，则交换前两块后，两个短块的长度都至多为 `0.767010... delta S+o(S)`。

## 1. 记号

令

\[
a:=\log_{10}2,
\qquad b:=1-a,
\qquad
\lambda:=\frac{2+a}{1+2a},
\]

\[
c_*:=2+3\lambda
=6.308883577618031\ldots.
\]

沿 corrected canonical high-funnel sequence 写

\[
\mathcal N:=\frac nS,
\qquad
M:=\frac mS,
\qquad
\delta:=c_*-\mathcal N\ge0.
\]

前两 prefix surplus 为

\[
s_i=n_i-m_i,
\qquad
s:=s_1+s_2,
\qquad
D_s:=|s_1-s_2|.
\]

因此恒有

\[
\boxed{s+D_s=2\max(s_1,s_2).}
\tag{1.1}
\]

在 d-dominant sector，surplus simplex 给

\[
\boxed{s_1+s_2=s\le2.}
\tag{1.2}
\]

## 2. small-factor upper 与 corrected lower 联立

旧 d-dominant Archimedean upper 本身不依赖已撤销的 unified/gap discriminant-root identification：

\[
F_-<2\cdot10^{\,2S+s+D_s+2m-n+O(1)}.
\]

归一化：

\[
\frac{\log_{10}F_-}{S}
\le
2+\frac{s+D_s}{S}+2M-\mathcal N+o(1).
\tag{2.1}
\]

corrected exact-small-factor lower 为

\[
\frac{\log_{10}F_-}{S}
\ge
2+b\frac TS-R-o(1).
\tag{2.2}
\]

所以

\[
\boxed{
\frac{s+D_s}{S}
\ge
\mathcal N-2M+b\frac TS-R-o(1).
}
\tag{2.3}
\]

corrected 5-resonance 给

\[
\frac TS
=
\frac{2M+2Q_5-2G_5+N_5}{3}.
\tag{2.4}
\]

令

\[
M_*:=2.808883577618031\ldots,
\qquad
\mu:=M_*-M.
\]

由 `dd-corrected-terminal-neighborhood-geometry-2026-08-22.md`：

\[
0\le\mu\le\delta+o(1).
\tag{2.5}
\]

又因为 terminal constants 满足

\[
c_*-2M_*+\frac{2b}{3}M_*=2,
\tag{2.6}
\]

将 `(2.4)--(2.6)` 代入 `(2.3)`：

\[
\begin{aligned}
\frac{s+D_s}{S}
\ge{}&2-\delta
+\left(2-\frac{2b}{3}\right)\mu
+\frac{2b}{3}Q_5
-\frac{2b}{3}G_5
+\frac b3N_5
-R-o(1).
\end{aligned}
\tag{2.7}
\]

其中 `mu,Q_5,N_5` 三项均非负，可安全丢掉：

\[
\frac{s+D_s}{S}
\ge
2-\delta-\frac{2b}{3}G_5-R-o(1).
\tag{2.8}
\]

## 3. `G_5` 与 `R` 共用同一份 slope-defect budget

quantitative defect inequality 中

\[
\delta
\ge
c_GG_5+c_RR-o(1),
\]

其中

\[
c_G=\frac{2b(2\lambda-1)}3,
\qquad
c_R=2\lambda-1.
\]

注意两个坏方向的 cost/defect ratio 完全相同：

\[
\frac{(2b/3)}{c_G}
=
\frac1{c_R}
=
\frac1{2\lambda-1}.
\]

所以不能分别给 `G_5,R` 各花一整份 `delta`；联合最优化直接给

\[
\boxed{
\frac{2b}{3}G_5+R
\le
\frac{\delta}{2\lambda-1}+o(1).
}
\tag{3.1}
\]

代回 `(2.8)`：

\[
\boxed{
2-\frac{s+D_s}{S}
\le
\left(1+\frac1{2\lambda-1}\right)\delta+o(1).
}
\tag{Digit-defect}
\]

数值上

\[
2\lambda-1
=1.872589051745354\ldots,
\]

\[
\boxed{
1+\frac1{2\lambda-1}
=1.534019997109321\ldots.
}
\tag{3.2}
\]

这改进了逐 defect 分别粗估得到的更差常数。

## 4. surplus polarization

定义

\[
\boxed{
\kappa_{\rm dig}
:=\frac12\left(1+\frac1{2\lambda-1}\right)
=0.767009998554660\ldots.
}
\tag{4.1}
\]

由 `(1.1)` 与 `(Digit-defect)`：

\[
\boxed{
\frac{\max(s_1,s_2)}S
\ge
1-\kappa_{\rm dig}\delta-o(1).
}
\tag{4.2}
\]

交换前两块后可设

\[
s_1=\max(s_1,s_2).
\]

则

\[
\boxed{
s_1\ge(1-\kappa_{\rm dig}\delta)S-o(S).}
\tag{4.3}
\]

由 `s_1+s_2<=2`：

\[
\boxed{
s_2\le-(1-\kappa_{\rm dig}\delta)S+O(1)+o(S).}
\tag{4.4}
\]

## 5. block-length polarization

使用

\[
m_1+m_2=S,
\qquad
n_i=m_i+s_i\ge1.
\]

由 `n_2>=1` 与 `(4.4)`：

\[
m_2\ge1-s_2
\ge(1-\kappa_{\rm dig}\delta)S-o(S).
\]

故

\[
\boxed{
m_1\le\kappa_{\rm dig}\delta S+o(S),}
\tag{5.1}
\]

\[
\boxed{
m_2\ge(1-\kappa_{\rm dig}\delta)S-o(S).}
\tag{5.2}
\]

同时 `n_1=m_1+s_1>=s_1` 给

\[
\boxed{
n_1\ge(1-\kappa_{\rm dig}\delta)S-o(S).}
\tag{5.3}
\]

而

\[
n_1+n_2=S+s_1+s_2\le S+2
\]

所以

\[
\boxed{
n_2\le\kappa_{\rm dig}\delta S+o(S).}
\tag{5.4}
\]

因此交换前两块后，统一得到

\[
\boxed{
\begin{aligned}
&m_1,n_2\le0.767009998555\,\delta S+o(S),\\
&m_2,n_1\ge(1-0.767009998555\,\delta)S-o(S).
\end{aligned}}
\tag{Quantitative-prefix-polarization}
\]

当 `delta->0` 时恢复旧 equality terminal shape

\[
(m_1,m_2;n_1,n_2)
=(o(S),S-o(S);S-o(S),o(S))
\]

（允许交换 prefix labels）。

## 6. 数值含义

例如若

\[
\frac nS\ge c_*-0.01,
\]

则渐近上两个短 prefix blocks 的长度比例至多约为

\[
0.00767010,
\]

而两个长块至少占

\[
0.99232990
\]

的 `S` 尺度。

所以 digit polarization 对 slope defect 是线性稳定的，并且常数小于 `0.77`。

## 7. 下一接口

本文为 equality-only denominator/Farey machinery提供了一个可量化入口：在 `delta`-terminal neighborhood 中，选取长 denominator block 为第二块后，

\[
m_2=S+O(\delta S),
\qquad
n_2=O(\delta S).
\]

下一步需要重新审计 `R_2`、first source residue 与 Farey-cell width中所有原先写作 `10^{o(S)}` 的 coefficient，把它们改成 `10^{O(delta S)+o(S)}`；若 cell width 相对于 reduced-fraction spacing出现严格正线性 surplus，则可与 quantitative defect inequality闭合成显式 slope gap。

## 8. 状态摘要

- **已严格完成：** `Digit-defect`，常数 `1.534019997109321...`。
- **已严格完成：** `Quantitative-prefix-polarization`，短块常数 `kappa_dig=0.767009998554660...`。
- **未使用：** 旧 Five-dichotomy、Xi-slack、Final-5 denominator-max exhaustion、错误的 discriminant-root identification。
- **仍待证：** quantitative `R_2`/Farey neighborhood；uniform strict slope gap；DD 空性与 effective absolute height bound。
