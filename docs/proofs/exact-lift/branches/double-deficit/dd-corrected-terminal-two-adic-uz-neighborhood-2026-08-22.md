# DD corrected terminal 的 two-adic overlap 与 `U/Z` neighborhood

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-high-funnel-schmidt-2026-08-22.md`](dd-corrected-high-funnel-schmidt-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` high-funnel 的渐近 terminal neighborhood；下文固定 `delta<=1/2`，这已经覆盖 strict-gap 所需的小邻域）。**
>
> 目的：corrected Schmidt dual没有直接出现 `G_2=v_2(G)/S`，所以此前只能控制 `U+Z` 的总 Schmidt budget，不能逐个量化 `U,Z`。本文利用 quantitative digit polarization 与 prefix concat `Q=b_1 10^{m_2}+b_2`，把 `G_2` 也压成 `O(delta)`，进而得到显式 `U/Z` height windows。

## 1. 记号

令

\[
a:=\log_{10}2,
\qquad b:=1-a,
\qquad
\lambda:=\frac{2+a}{1+2a},
\]

\[
c_*:=2+3\lambda,
\qquad
\delta:=c_*-\frac nS.
\]

quantitative defect inequality 中需要的 coefficients 为

\[
c_{Q_2}=2a\lambda,
\]

\[
c_{G_5}=\frac{2b(2\lambda-1)}3,
\qquad
c_R=2\lambda-1.
\]

又

\[
2\lambda-1=\frac3{1+2a}.
\tag{1.1}
\]

`dd-corrected-terminal-digit-polarization-2026-08-22.md` 允许交换前两 prefix labels，使长 denominator 为第二块，并给

\[
m_1,n_2\le\kappa_{\rm dig}\delta S+o(S),
\]

\[
m_2,n_1\ge(1-\kappa_{\rm dig}\delta)S-o(S),
\]

其中

\[
\boxed{
\kappa_{\rm dig}
=\frac{2+a}{3}
=0.767009998554660\ldots.
}
\tag{1.2}
\]

## 2. long denominator 的 2-depth 等于 `v_2(Q)`

prefix concat 为

\[
\boxed{Q=b_1 10^{m_2}+b_2.}
\tag{2.1}
\]

记

\[
\mathfrak q:=v_2(Q),
\qquad
Q_2:=\mathfrak q/S.
\]

quantitative defect给

\[
Q_2\le\frac{\delta}{2a\lambda}+o(1).
\tag{2.2}
\]

另一方面

\[
v_2(b_1 10^{m_2})=v_2(b_1)+m_2\ge m_2.
\]

若固定 `delta<=1/2`，则

\[
\frac{\delta}{2a\lambda}
<1-\kappa_{\rm dig}\delta
\]

有统一正 margin；更一般地该比较在

\[
\delta<
\left(\kappa_{\rm dig}+\frac1{2a\lambda}\right)^{-1}
=0.519903730696\ldots
\]

时成立。

所以 sufficiently large `S` 上：

\[
v_2(Q)<v_2(b_1 10^{m_2}).
\]

两项 valuation 不等时和的 valuation取较小者，因此 necessarily

\[
\boxed{v_2(b_2)=v_2(Q)=\mathfrak q.}
\tag{Long-2-depth}
\]

这把 long denominator 的 2-adic depth直接放回 quantitative defect ledger。

## 3. `G_2` 的显式 upper

全局 notation 有

\[
G=b_1b_2.
\]

令

\[
G_2:=\frac{v_2(G)}S.
\]

短 denominator 满足

\[
b_1<10^{m_1},
\]

所以

\[
v_2(b_1)<m_1\log_2 10=\frac{m_1}{a}.
\tag{3.1}
\]

先保留 digit defect 中尚未粗化的版本。上一文件证明过程给

\[
2-\frac{s+D_s}{S}
\le
\delta+\frac{2b}{3}G_5+R+o(1).
\]

而选定 `s_1=max(s_1,s_2)` 后

\[
\frac{m_1}{S}
\le
1-\frac{s_1}{S}+o(1)
=
\frac12\left(2-\frac{s+D_s}{S}\right)+o(1),
\]

故

\[
\boxed{
\frac{m_1}{S}
\le
\frac\delta2+rac b3G_5+\frac R2+o(1).
}
\tag{3.2}
\]

由 `(Long-2-depth)` 与 `(3.1)`：

\[
G_2
\le
\frac1a\frac{m_1}{S}+Q_2+o(1),
\]

从而

\[
G_2
\le
\frac{\delta}{2a}
+Q_2
+\frac{b}{3a}G_5
+\frac{R}{2a}
+o(1).
\tag{3.3}
\]

quantitative defect 给联合 budget

\[
c_{Q_2}Q_2+c_{G_5}G_5+c_RR\le\delta+o(1).
\]

对 `(3.3)` 最后三项作一次线性优化。三个 cost ratio 为

\[
\frac1{c_{Q_2}}=\frac1{2a\lambda},
\]

\[
\frac{b/(3a)}{c_{G_5}}
=
\frac1{2a(2\lambda-1)},
\]

\[
\frac{1/(2a)}{c_R}
=
\frac1{2a(2\lambda-1)}.
\]

因为 `2lambda-1>lambda`，最大者为第一项。因此

\[
\boxed{
G_2
\le
\left(\frac1{2a}+\frac1{2a\lambda}\right)\delta+o(1).
}
\tag{G2-window}
\]

即

\[
\boxed{
G_2
\le
\frac{3(1+a)}{2a(2+a)}\,\delta+o(1)
=2.817387063422592\ldots\,\delta+o(1).
}
\tag{3.4}
\]

所以 corrected equality 中隐含的 `G_2->0` 现在也获得显式线性 stability。

## 4. `U` 的显式 window

canonical S-unit phase为

\[
\kappa=2\gamma5^TU,
\qquad
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\]

且 decimal pinning给

\[
\log_{10}\kappa=2S+O(1).
\]

因此

\[
\frac{\log_{10}U}{S}
=2-aG_2-bG_5-R-b\frac TS+o(1).
\tag{4.1}
\]

又

\[
\frac TS=\frac{2M+2Q_5-2G_5+N_5}{3}.
\]

所以

\[
\frac{\log_{10}U}{S}
=2-\frac{2b}{3}M
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1).
\tag{4.2}
\]

令

\[
M_*:=2.808883577618031\ldots,
\]

\[
\boxed{
U_*:=2-\frac{2b}{3}M_*
=0.691116422381969\ldots.
}
\tag{4.3}
\]

并写

\[
\mu:=M_*-M,
\qquad 0\le\mu\le\delta+o(1).
\]

则

\[
\frac{\log U}{S}-U_*
=
\frac{2b}{3}\mu
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1).
\tag{4.4}
\]

### upper

丢掉全部负项：

\[
\boxed{
\frac{\log U}{S}
\le
U_*+\frac{2b}{3}\delta+o(1).
}
\tag{U-upper}
\]

数值 coefficient为

\[
\frac{2b}{3}=0.465980002890679\ldots.
\]

### lower

使用 `(3.3)` 而非先使用粗 `(3.4)`：

\[
aG_2
\le
\frac\delta2
+aQ_2+\frac b3G_5+\frac R2+o(1).
\]

于是 `(4.4)` 中全部负项至多为

\[
\frac\delta2
+aQ_2
+\frac{2b}{3}Q_5
+\frac{2b}{3}G_5
+\frac b3N_5
+\frac{3R}{2}
+o(1).
\]

这些 variables 共用同一 quantitative-defect budget。对应 cost ratio最大值为

\[
\frac{3/2}{c_R}
=
\frac{3}{2(2\lambda-1)}
=\frac{1+2a}{2}.
\]

所以

\[
\boxed{
\frac{\log U}{S}
\ge
U_*-\left[\frac12+\frac{1+2a}{2}\right]\delta-o(1).
}
\]

即

\[
\boxed{
U_*-(1+a)\delta-o(1)
\le
\frac{\log_{10}U}{S}
\le
U_*+\frac{2b}{3}\delta+o(1).
}
\tag{U-window}
\]

数值为

\[
\boxed{
U_*-1.301029995663981\,\delta-o(1)
\le
\frac{\log_{10}U}{S}
\le
U_*+0.465980002890679\,\delta+o(1).
}
\]

## 5. `Z` 的显式 window

第二条 S-unit phase为

\[
\kappa+2G=2\gamma2^HZ,
\]

且

\[
\log_{10}(\kappa+2G)=2S+O(1).
\]

2-resonance给

\[
\frac HS=2M+2Q_2+N_2-2G_2+o(1).
\]

因此

\[
\begin{aligned}
\frac{\log_{10}Z}{S}
&=2-aG_2-bG_5-R-a\frac HS+o(1)\\
&=2-2aM-2aQ_2-aN_2+aG_2-bG_5-R+o(1).
\end{aligned}
\tag{5.1}
\]

令

\[
\boxed{
Z_*:=2-2aM_*
=0.308883577618031\ldots.
}
\tag{5.2}
\]

于是

\[
\frac{\log Z}{S}-Z_*
=2a\mu-2aQ_2-aN_2+aG_2-bG_5-R+o(1).
\tag{5.3}
\]

### lower

丢掉正项 `2a mu+aG_2`，其余负项共用 defect budget。最大 cost ratio为

\[
\frac{b}{c_{G_5}}
=\frac{1+2a}{2}.
\]

所以

\[
\boxed{
\frac{\log Z}{S}
\ge
Z_*-rac{1+2a}{2}\delta-o(1).
}
\tag{Z-lower}
\]

即 coefficient

\[
\frac{1+2a}{2}=0.801029995663981\ldots.
\]

### upper

由 `(3.3)`：

\[
aG_2
\le
\frac\delta2+aQ_2+\frac b3G_5+\frac R2+o(1).
\]

代入 `(5.3)` 并丢掉所有负项，可得

\[
\frac{\log Z}{S}-Z_*
\le
2a\delta+\frac\delta2
+aQ_2+\frac b3G_5+\frac R2+o(1).
\]

后三项共用 defect budget，最大 cost ratio为

\[
\frac{a}{c_{Q_2}}=\frac1{2\lambda}.
\]

因此

\[
\boxed{
\frac{\log Z}{S}
\le
Z_*+\left(2a+\frac12+\frac1{2\lambda}\right)\delta+o(1).
}
\tag{Z-upper}
\]

数值 coefficient为

\[
2a+\frac12+\frac1{2\lambda}
=1.450178006813822\ldots.
\]

综上

\[
\boxed{
Z_*-0.801029995663981\,\delta-o(1)
\le
\frac{\log_{10}Z}{S}
\le
Z_*+1.450178006813822\,\delta+o(1).
}
\tag{Z-window}
\]

## 6. 结构意义

corrected dual原本只控制

\[
\log U+\log Z\ge S-o(S)
\]

以及若干 2/5-adic defect，但 `G_2` 在消元中消失。本文利用 prefix digit polarization重新读取 `G_2`，因而首次在 corrected proof tree中得到 individual `U` 与 `Z` 的显式 terminal-neighborhood windows。

这为 quantitative Farey continuation提供四个关键输入：

1. `m_2/S=1+O(delta)`；
2. `v_2(Q)/S=O(delta)`；
3. `log U/S=U_*+O(delta)`；
4. `log Z/S=Z_*+O(delta)`。

下一步应把 equality `R_2`/Farey proof 中的 source-lift cell width 与 reduced-fraction spacing分别改写成这些窗口的线性函数，检查二者在 `delta>0` 时谁先损失。

## 7. 状态摘要

- **已严格完成：** `Long-2-depth`，在固定 `delta<=1/2` 的 terminal neighborhood中 `v_2(b_2)=v_2(Q)`。
- **已严格完成：** `G2-window`，coefficient `2.817387063422592...`。
- **已严格完成：** `U-window` 与 `Z-window`。
- **未使用：** old Final-5 lock / Xi-slack / discriminant-root misidentification。
- **仍待证：** quantitative Farey width-vs-spacing comparison；uniform strict slope gap；DD emptiness / effective absolute height。
