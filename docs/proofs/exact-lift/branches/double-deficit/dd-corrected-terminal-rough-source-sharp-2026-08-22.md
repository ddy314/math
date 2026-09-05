# DD corrected terminal rough-source 的 sharp defect bound

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-terminal-rough-source-neighborhood-2026-08-22.md`](dd-corrected-terminal-rough-source-neighborhood-2026-08-22.md)、[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、统一尾权 `kappa=10^m QG/b_3` 与 canonical S-unit phase。
>
> **严格状态：已严格完成（corrected canonical terminal neighborhood）。**
>
> 本文改进前一文件 `Rough-source-lower`。关键是不用 `q=Q/U` 与 `U` 的粗 window单独估 source，而先恢复第三分母的 exact factorization；这样 `M_*-M` 与其它 defects 必须共用同一 Schmidt budget，rough-source loss 的最坏 coefficient从 `1.081669...` 降到 `0.6518819845...`。

## 1. exact third-denominator factorization

DD 统一尾权对 DD 分支满足

\[
\boxed{
\kappa=\frac{10^mQG}{b_3}.}
\tag{1.1}
\]

canonical `t_2=1` phase有

\[
\boxed{
\kappa=2\gamma5^TU,
\qquad Q=Uq,
\qquad G=\gamma V.}
\tag{1.2}
\]

代入 `(1.1)` 并约去 `gamma U`：

\[
b_3
=\frac{10^m Uq\gamma V}{2\gamma5^TU}
=\frac{10^m}{2\cdot5^T}Vq.
\]

定义 smooth integer

\[
\boxed{B:=\frac{10^m}{2\cdot5^T}.}
\tag{1.3}
\]

得到整个 canonical funnel 中的 exact identity

\[
\boxed{b_3=BVq.}
\tag{Third-factor}
\]

terminal 文献中的

\[
b_3=BJ C_0q_c\theta s,
\qquad
V=C_0s,
\qquad
q=J\theta q_c
\]

只是 `(Third-factor)` 的进一步 equality normalization。

## 2. source height 的第二个 exact reader

`b_3` 是 `m` 位整数，因此

\[
\log_{10}b_3=m+O(1).
\]

而

\[
\log_{10}B
=m-T\log_{10}5+O(1).
\]

令

\[
b:=\log_{10}5=1-\log_{10}2.
\]

由 `(Third-factor)`：

\[
\boxed{
\frac{\log(Vq)}S
=b\frac TS+o(1).}
\tag{Vq-plane}
\]

所以

\[
\boxed{
\frac{\log q}S
=b\frac TS-\frac{\log V}S+o(1).}
\tag{q-reader-2}
\]

这是 `q=Q/U` 之外的第二个 exact source-height reader。

## 3. 直接展开 `q_rough`

仍令

\[
a:=\log_{10}2,
\qquad b=1-a,
\]

\[
M_*:=2.808883577618031\ldots,
\qquad
z_*:=0.308883577618031\ldots,
\]

\[
\mu:=M_*-M\ge-o(1).
\]

canonical identities给

\[
\frac TS
=\frac{2M+2Q_5-2G_5+N_5}{3},
\]

以及

\[
\frac{\log V}{S}=1-aG_2-bG_5-R+o(1).
\]

由 `(q-reader-2)`：

\[
\begin{aligned}
\frac{\log q}{S}-z_*
={}&-\frac{2b}{3}\mu
+\frac{2b}{3}Q_5
+\frac b3G_5
+\frac b3N_5\\
&+aG_2+R+o(1).
\end{aligned}
\tag{3.1}
\]

定义

\[
q_{\rm rough}=\operatorname{core}_{10}(q).
\]

因为 `v_2(q)=v_2(Q)`, `v_5(q)=v_5(Q)`：

\[
\begin{aligned}
\frac{\log q_{\rm rough}}S-z_*
={}&-\frac{2b}{3}\mu
-aQ_2-\frac b3Q_5\\
&+\frac b3G_5+\frac b3N_5+aG_2+R+o(1).
\end{aligned}
\tag{3.2}

后三个显示的 `G_5,N_5,G_2,R` contributions均非负或由 positive terms包含；为了 lower bound，只需控制

\[
\mathcal L
:=\frac{2b}{3}\mu+aQ_2+\frac b3Q_5.
\tag{3.3}
\]

## 4. `mu` 与其它 defects 不能独立花费 `delta`

Schmidt slack定义为

\[
\sigma_S
=3-\left[
AM+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)+2R
\right],
\]

其中

\[
A=\frac{2(1+2a)}3.
\]

又 equality constant满足

\[
AM_*=3.
\]

所以不是只有 `mu<=delta`；实际有 exact normalized identity

\[
\boxed{
A\mu
=\sigma_S
+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R+o(1).}
\tag{mu-budget}
\]

将 `(mu-budget)` 代入 `(3.3)`，`mathcal L` 成为

\[
\sigma_S,Q_2,N_2,Q_5,G_5,N_5,R
\]

的非负线性组合。逐项除以 quantitative defect theorem 中对应 cost coefficient，最大 ratio恰来自 `Q_2`：

\[
\boxed{
\max\frac{\text{loss coefficient}}{\text{slope-defect coefficient}}
=
0.651881984514140\ldots.}
\tag{4.1}
\]

因此

\[
\boxed{
\mathcal L
\le0.651881984514141\,\delta+o(1).}
\tag{4.2}
\]

代回 `(3.2)`：

\[
\boxed{
\frac{\log q_{\rm rough}}S
\ge
z_*-0.651881984514141\,\delta-o(1).}
\tag{Sharp-rough-source}
\]

这严格加强前一文件的 coefficient `1.08166910947...`。

## 5. 与 one-channel core 的联合 rough budget

沿用

\[
\frac{\log v_2}{S}
\ge1-C_{\rm one}\delta-o(1),
\qquad
C_{\rm one}=2.335049992773302\ldots,
\]

以及 overlap bound

\[
\frac{\log\gcd(q_{\rm rough},v_2)}S
\le\kappa_{\rm dig}\delta+o(1),
\qquad
\kappa_{\rm dig}=0.767009998554660\ldots.
\]

故

\[
\boxed{
\frac1S\log\operatorname{lcm}(q_{\rm rough}^2,v_2)
\ge
1+2z_*-C_{\rm CRT}^{\sharp}\delta-o(1),}
\tag{5.1}
\]

其中

\[
\boxed{
C_{\rm CRT}^{\sharp}
=2(0.651881984514141)
+C_{\rm one}+2\kappa_{\rm dig}
=5.172833958910904\ldots.}
\tag{5.2}
\]

因此纯 height margin

\[
1+2z_*-1=2z_*=0.617767155236062\ldots
\]

仍为正，只要

\[
\boxed{
\delta<0.119425282184\ldots.}
\tag{5.3}
\]

再次强调：`(5.3)` 不是已经证明的 slope gap。它说明如果能把 neighborhood `q_rough^2` 真正升级为与 equality `q_c^2` 同性质的 fixed source period，则其与 `v_2` 的联合 modulus在相当宽的显式 neighborhood 内仍有足够 capacity 压过一个 `S`-height prefix window。

## 6. 当前桥接问题的最精确表述

旧 terminal normalization 有

\[
q=J\theta q_c,
\]

以及

\[
q_c^2L_{\rm clean}=g_0a_3+5^TR_0.
\]

本文说明 `q` 的 rough height本身已经足够大；剩余问题已经不再是 height：

\[
\boxed{
\text{需要证明 }q/q_c=J\theta
\text{ 在 terminal neighborhood 中只有 }O(\delta S)\text{ height，}
}
\]

或者绕过 `q_c`，直接从 generic exact lift构造一个读取 `q_rough^2` 大部分的 square-source divisor。

一旦得到任何形如

\[
\log q_{\rm sq}
\ge(z_*-C\delta)S-o(S),
\qquad
q_{\rm sq}^2\mid(g_0a_3+5^TR_0)
\]

的 neighborhood theorem，就可以立即与 quantitative one-channel `v_2` 以及 universal Pairmax-GCRT machinery联立，得到 explicit fixed-fiber prefix uniqueness neighborhood。

## 7. 状态摘要

- **已严格完成：** generic canonical `Third-factor`。
- **已严格完成：** `Vq-plane`。
- **已严格完成：** `mu-budget`。
- **已严格完成：** sharp rough-source coefficient `0.651881984514141...`。
- **capacity 改善：** potential square-source × pair-max threshold提升到 `delta<0.119425282184...`。
- **待证核心：** neighborhood square-source extraction，而非继续优化已有 heights。
