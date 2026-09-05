# DD corrected terminal 的 rough source quotient neighborhood

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、corrected canonical `t_2=1` phase `Q=Uq`。
>
> **严格状态：已严格完成（corrected canonical terminal neighborhood，固定 `delta<=1/2`）。**
>
> 本文不预先使用 equality-only clean source notation `q_c`。它先从整个 canonical funnel 中始终存在的整数 quotient `q=Q/U` 抽取真正 rough source core，并量化其高度与 large pair-max channel 的 overlap。

## 1. source quotient `q`

canonical high funnel 有

\[
\boxed{Q=Uq,\qquad q\in\mathbf Z_{>0},}
\tag{1.1}
\]

且 `(U,10)=1`。prefix denominator concat `Q` 为 `S` 位整数：

\[
10^{S-1}\le Q<10^S,
\]

所以

\[
\frac{\log_{10}Q}{S}=1+o(1).
\tag{1.2}
\]

令

\[
a=\log_{10}2,
\qquad b=1-a,
\]

\[
U_*:=0.691116422381969\ldots,
\qquad
z_*:=1-U_*=0.308883577618031\ldots.
\]

上一文件给

\[
U_*-(1+a)\delta-o(1)
\le\frac{\log U}{S}
\le U_*+\frac{2b}{3}\delta+o(1).
\]

因此 `(1.1)--(1.2)` 直接给

\[
\boxed{
z_*-\frac{2b}{3}\delta-o(1)
\le
\frac{\log q}{S}
\le
z_*+(1+a)\delta+o(1).}
\tag{q-window}
\]

数值上：

\[
0.308883577618031-0.465980002890679\delta-o(1)
\le\frac{\log q}{S}
\]

且 upper coefficient 为 `1.301029995663981`。

## 2. 删除 decimal primes

定义

\[
\boxed{q_{\rm rough}:=\operatorname{core}_{10}(q).}
\tag{2.1}
\]

因为 `(U,10)=1` 且 `Q=Uq`：

\[
v_2(q)=v_2(Q),
\qquad
v_5(q)=v_5(Q).
\]

故

\[
\frac{\log q_{\rm rough}}S
=
\frac{\log q}S-aQ_2-bQ_5.
\tag{2.2}
\]

quantitative defect中

\[
c_{Q_2}=2a\lambda,
\qquad
c_{Q_5}=\frac{2b(\lambda+1)}3,
\]

其中

\[
\lambda=\frac{2+a}{1+2a}.
\]

所以 smooth loss `aQ_2+bQ_5` 在同一 defect budget 下满足

\[
aQ_2+bQ_5
\le
\max\left(
\frac{a}{c_{Q_2}},
\frac{b}{c_{Q_5}}
\right)\delta+o(1).
\]

两个 ratios 是

\[
\frac1{2\lambda},
\qquad
\frac{3}{2(\lambda+1)},
\]

后者较大。因此

\[
\boxed{
aQ_2+bQ_5
\le
\frac{3}{2(\lambda+1)}\delta+o(1).}
\tag{2.3}
\]

与 `q-window` 合并：

\[
\boxed{
\frac{\log q_{\rm rough}}S
\ge
z_*-C_q\delta-o(1),}
\tag{Rough-source-lower}
\]

其中

\[
\boxed{
C_q:=\frac{2b}{3}+\frac{3}{2(\lambda+1)}
=1.081669109470559\ldots.}
\tag{2.4}
\]

所以 equality source height `z_*S` 在 corrected neighborhood中至少保留为

\[
(0.308883577618031-1.081669109471\delta)S-o(S)
\]

的真实 non-decimal rough core。

## 3. 与 large pair-max channel 的 overlap

令 `v_2` 表示 `(b_2,b_3)` pair-max channel（不是 2-adic valuation）。general denominator normal form给

\[
v_2\mid b_2,
\]

而其 prime support均避开 `10`。

prefix concat

\[
Q=b_1 10^{m_2}+b_2
\]

模 `v_2` 给

\[
Q\equiv b_1 10^{m_2}\pmod{v_2}.
\]

因此

\[
\gcd(Q,v_2)\mid b_1.
\tag{3.1}
\]

又 `q|Q`，故

\[
\boxed{\gcd(q_{\rm rough},v_2)\mid b_1.}
\tag{3.2}
\]

quantitative digit polarization的 refined bound为

\[
\frac{\log b_1}{S}
\le
\frac\delta2+\frac b3G_5+\frac R2+o(1).
\]

联合 defect optimization给

\[
\boxed{
\frac{\log\gcd(q_{\rm rough},v_2)}S
\le
\kappa_{\rm dig}\delta+o(1),}
\tag{Source-pairmax-overlap}
\]

其中

\[
\kappa_{\rm dig}=\frac{2+a}{3}
=0.767009998554660\ldots.
\]

因此整个 terminal neighborhood仍然保留两个几乎横截的 rough objects：

\[
\log q_{\rm rough}
\ge(z_*-1.081670\delta)S-o(S),
\]

\[
\log v_2
\ge(1-2.335050\delta)S-o(S),
\]

而二者 overlap只有 `0.767010 delta S+o(S)`。

## 4. 一个可用于未来 CRT 的联合高度预算

虽然本文尚未证明 equality clean-source congruence中的 `q_c^2` 可直接替换成 `q_rough^2`，但纯高度上已经有

\[
\log\operatorname{lcm}(q_{\rm rough}^2,v_2)
\ge
2\log q_{\rm rough}+\log v_2
-2\log\gcd(q_{\rm rough},v_2).
\]

因此

\[
\boxed{
\frac1S\log\operatorname{lcm}(q_{\rm rough}^2,v_2)
\ge
1+2z_*-C_{\rm CRT}\delta-o(1),}
\tag{4.1}
\]

其中

\[
C_{\rm CRT}
=2C_q+C_{\rm one}+2\kappa_{\rm dig}
=6.032408208823740\ldots.
\]

terminal value为

\[
1+2z_*=1.617767155236062\ldots.
\]

所以在纯 height budget 上，这个联合 rough modulus仍超过一个 `S`-height prefix window，只要 roughly

\[
\delta<\frac{2z_*}{C_{\rm CRT}}
=0.1024\ldots.
\]

**重要边界：** `(4.1)` 目前只是容量/高度结论，不能直接宣称 `A_12` CRT uniqueness。还需证明 neighborhood clean-source square congruence真正读取 `q_rough^2` 的相应有效部分，或证明 equality `q_c` 与 `q_rough` 的 quotient只有 `O(delta S)` height。

## 5. Schmidt slack 的精确 rough-product解释

从 corrected S-unit formulas可直接相加得到

\[
\frac{\log U+\log Z}{S}
=1+\sigma_S+o(1),
\tag{5.1}
\]

其中 `sigma_S` 是 quantitative defect中定义的 Schmidt slack：

\[
\sigma_S
=3-\left[
AM+2aQ_2+aN_2+
\frac b3(2Q_5+4G_5+N_5)+2R
\right].
\]

所以

\[
\boxed{
1-o(1)
\le
\frac{\log(UZ)}S
\le
1+\frac\delta\lambda+o(1).}
\tag{UZ-product-window}
\]

这说明 Farey reduced-fraction spacing的 product height也只以 `O(delta)` 速度偏离 equality critical scale。

## 6. 状态摘要

- **已严格完成：** `q-window` 与 `Rough-source-lower`。
- **已严格完成：** `Source-pairmax-overlap`。
- **已严格完成：** `UZ-product-window`。
- **新 quantitative pool：** rough source `q_rough` + large pair-max `v_2` 在整个 corrected neighborhood中同时保持正线性高度并近似横截。
- **当前桥接缺口：** 将 `q_rough` 的高度真正送入 equality-style `q_c^2` clean-source CRT，或直接构造一个 neighborhood-valid square-source reader。
- **仍未证明：** explicit strict slope gap、DD emptiness、effective absolute height bound。
