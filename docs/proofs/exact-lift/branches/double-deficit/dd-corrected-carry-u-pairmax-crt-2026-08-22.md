# DD corrected terminal 的 carry-`U` CRT 与 `U × v_2` neighborhood uniqueness

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md`](dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md)、[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-terminal-rough-source-sharp-2026-08-22.md`](dd-corrected-terminal-rough-source-sharp-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood；fixed gap/suffix fiber）。**
>
> generic carry 本身给出一个此前没有单独抽出的完整 rational period `U`。由于 `(U,V)=1` 且 quantitative one-channel `v_2|V`，`U` 与 pair-max period `v_2` 严格互素。进一步联合优化两者的 height，而不是分别使用各自最坏 defect，得到
>
> \[
> \boxed{
> \frac{\log_{10}(Uv_2)}S
> \ge
> 1+U_*-(2+3\log_{10}2)\delta-o(1),}
> \]
>
> 其中
> \[
> U_*=0.691116422381969\ldots.
> \]
> 因而 fixed `(R_0,g_0,a_2)` fiber 的 `A_12` uniqueness 可扩展到
> \[
> \boxed{
> \delta<0.238062349248\ldots,}
> \]
> 明显宽于 `q_Q^2 × v_2` 的 `0.142505...` neighborhood。

---

## 1. generic carry 强迫 `g_0 | Sigma`

上一 pair-max neighborhood theorem 已从 general overlap normalization恢复 exact carry

\[
\boxed{
 g_0Ua_3
 =g_0B10^dVA_{12}-\Sigma R_0,}
\tag{Carry}
\]

其中

\[
(R_0,g_0)=1,
\qquad
\Sigma=2^HZ+5^TU.
\]

移项：

\[
\Sigma R_0
=g_0\left(B10^dVA_{12}-Ua_3\right).
\]

右边被 `g_0` 整除，而 `(R_0,g_0)=1`，故 Euclid lemma 直接给

\[
\boxed{g_0\mid\Sigma.}
\tag{g0-Sigma}
\]

定义整数

\[
\boxed{\Sigma_0:=\Sigma/g_0.}
\tag{1.1}
\]

则 `(Carry)` 可以除以 `g_0`：

\[
\boxed{
Ua_3
=B10^dVA_{12}-\Sigma_0R_0.}
\tag{Carry-primitive}
\]

这条 divisibility 不需要 equality frontier 的 slow-height 结论。

---

## 2. 模 `U` 得到 full fixed `A_12` period

对 `(Carry-primitive)` 模 `U`：

\[
\boxed{
B10^dV A_{12}
\equiv
\Sigma_0R_0
\pmod U.}
\tag{U-CRT-raw}
\]

canonical phase已有

\[
(U,10)=1,
\qquad
(U,V)=1.
\]

而

\[
B=\frac{10^m}{2\cdot5^T}
\]

只含 `2,5` 素因子。因此

\[
\boxed{(U,B10^dV)=1.}
\tag{2.1}
\]

所以 `(U-CRT-raw)` 对 rational integer `A_12` 给完整 effective period `U`：

\[
\boxed{
A_{12}\equiv\rho_U\pmod U.}
\tag{U-CRT}
\]

在固定 denominator/S-unit data 与 gap fiber `(R_0,g_0)` 后，右边 residue 完全固定；不需要固定 `a_3`。

---

## 3. `U` 与 pair-max `v_2` 严格互素

quantitative one-channel decomposition为

\[
V=v_1v_2,
\]

故

\[
v_2\mid V.
\]

canonical S-unit phase有

\[
(U,V)=1.
\]

于是 exact 地

\[
\boxed{(U,v_2)=1.}
\tag{U-v2-transverse}
\]

上一 pair-max fixed CRT theorem给 fixed `(R_0,g_0,a_2)` fiber 中

\[
\boxed{A_{12}\equiv\rho_V\pmod{v_2}.}
\tag{3.1}
\]

所以 `(U-CRT)` 与 `(3.1)` 的联合 period是 exact product

\[
\boxed{M_{UV}:=Uv_2.}
\tag{3.2}
\]

---

## 4. 不分别花两次 defect budget

若只把既有

\[
\log U/S\ge U_*-(1+a)\delta-o(1)
\]

与

\[
\log v_2/S\ge1-C_{\rm one}\delta-o(1)
\]

相加，会重复允许同一 defect 在两条 bound 中各自达到最坏值。这里重新做联合 ledger。

记

\[
a:=\log_{10}2,
\qquad
b:=1-a,
\qquad
\lambda:=\frac{2+a}{1+2a},
\]

\[
A:=\frac{2(1+2a)}3,
\qquad
\mu:=M_*-M.
\]

individual `U` identity为

\[
\frac{\log U}{S}-U_*
=
\frac{2b}{3}\mu
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1).
\tag{4.1}
\]

one-channel proof在粗化前给

\[
\frac{\log v_1}{S}
\le
\frac\delta2+\frac b3G_5+\frac R2+o(1),
\tag{4.2}
\]

而

\[
\frac{\log V}{S}
=1-aG_2-bG_5-R+o(1).
\tag{4.3}
\]

所以

\[
\begin{aligned}
\frac{\log v_2}{S}
\ge{}&1-rac\delta2
-aG_2-rac{4b}{3}G_5-rac{3R}{2}-o(1).
\end{aligned}
\tag{4.4}
\]

把 `(4.1)` 与 `(4.4)` 相加：

\[
\begin{aligned}
\frac{\log(Uv_2)}S-(1+U_*)
\ge{}&-rac\delta2+rac{2b}{3}\mu
-2aG_2-rac{2b}{3}Q_5\\
&-\frac{5b}{3}G_5-rac b3N_5-rac{5R}{2}-o(1).
\end{aligned}
\tag{4.5}
\]

`G_2` 的未粗化 upper 为

\[
aG_2
\le
\frac\delta2+aQ_2+rac b3G_5+rac R2+o(1).
\tag{4.6}
\]

故

\[
\begin{aligned}
\frac{\log(Uv_2)}S-(1+U_*)
\ge{}&-rac{3\delta}{2}+rac{2b}{3}\mu\\
&-2aQ_2-rac{2b}{3}Q_5
-\frac{7b}{3}G_5-rac b3N_5-rac{7R}{2}-o(1).
\end{aligned}
\tag{4.7}
\]

---

## 5. 用 exact `mu` budget 回收正项

corrected Schmidt slack identity给

\[
\boxed{
A\mu
=\sigma_S+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)+2R+o(1).}
\tag{mu-budget}
\]

令

\[
\boxed{
c_\mu:=\frac{2b}{3A}=\frac{b}{1+2a}.}
\tag{5.1}
\]

把 `(mu-budget)` 代入 `(4.7)`。忽略有利的 `sigma_S,N_2` 正贡献后，剩余 loss coefficients 为

\[
\begin{array}{c|c}
\text{variable}&\text{loss coefficient}\\ \hline
Q_2&2a(1-c_\mu)\\
Q_5&\frac{2b}{3}(1-c_\mu)\\
G_5&\frac b3(7-4c_\mu)\\
N_5&\frac b3(1-c_\mu)\\
R&\frac72-2c_\mu.
\end{array}
\tag{5.2}
\]

quantitative-defect costs分别为

\[
2a\lambda,
\qquad
\frac{2b(\lambda+1)}3,
\qquad
\frac{2b(2\lambda-1)}3,
\qquad
\frac{b(\lambda+1)}3,
\qquad
2\lambda-1.
\tag{5.3}
\]

逐项 loss/cost ratios化简为

\[
\begin{array}{c|c}
Q_2&0.392472061943\ldots\\
Q_5&0.231378213160\ldots\\
G_5&\frac12+3a\\
N_5&0.231378213160\ldots\\
R&\frac12+3a.
\end{array}
\tag{5.4}
\]

最大 ratio由 `G_5` 与 `R` 同时达到：

\[
\boxed{
\rho_{UV}=\frac12+3a
=1.403089986991944\ldots.}
\tag{5.5}
\]

所有 variables 共用同一份 slope-defect budget，所以 `(4.7)` 最终给

\[
\boxed{
\frac{\log_{10}(Uv_2)}S
\ge
1+U_*-C_{UV}\delta-o(1),}
\tag{UV-height}
\]

其中

\[
\boxed{
C_{UV}
=\frac32+\rho_{UV}
=2+3a
=2.903089986991944\ldots
=\log_{10}800.}
\tag{5.6}
\]

这严格优于把 individual `U` 与 `v_2` lower bounds直接相加所得的 coefficient `3.636079988...`。

---

## 6. 显式 `U × v_2` uniqueness neighborhood

`d_3`-dominant surplus simplex给

\[
n_1+n_2=S+s_1+s_2\le S+2.
\]

因此

\[
0<A_{12}<10^{S+2}.
\tag{6.1}
\]

由 `(UV-height)`，若

\[
1+U_*-C_{UV}\delta>1,
\]

即

\[
\boxed{
\delta<\delta_{UV}:=\frac{U_*}{2+3a},}
\tag{6.2}
\]

则 sufficiently large `S` 时

\[
Uv_2>10^{S+2}.
\]

数值上

\[
\boxed{
\delta_{UV}
=0.238062349248111\ldots.}
\tag{6.3}
\]

固定 denominator/S-unit data 与 `(R_0,g_0,a_2)` 后，`A_12` 同时落在一个 residue modulo `U` 与一个 residue modulo `v_2`；由于二者互素，若有两个不同合法 candidates，其差被 `Uv_2` 整除，却绝对值小于 `Uv_2`，矛盾。

因此

\[
\boxed{
\delta<0.238062349248111\ldots
\Longrightarrow
\#\{A_{12}\text{ in fixed }(R_0,g_0,a_2)\text{ fiber}\}\le1.}
\tag{UV-fixed-fiber-unique}
\]

carry `(Carry-primitive)` 再唯一恢复 `a_3`；固定 `(n_2,a_2)` 后也唯一恢复 `a_1`。

---

## 7. 对 numerator entropy 的直接更新

已有 gap-fiber entropy：

\[
\#\{(R_0,g_0)\}
\le10^{\delta S+o(S)},
\]

以及 short suffix entropy：

\[
\#\{a_2\}
\le10^{\kappa_{\rm dig}\delta S+o(S)},
\qquad
\kappa_{\rm dig}=0.767009998554660\ldots.
\]

因此在更宽的

\[
\delta<\delta_{UV}
\]

范围内：

\[
\boxed{
N_{\rm num}(S;\delta)
\le
10^{(1+\kappa_{\rm dig})\delta S+o(S)}
=10^{1.767009998554660\ldots\delta S+o(S)}.}
\tag{7.1}
\]

此前 source-square theorem只在 `delta<0.142505...` 范围内得到同一个 entropy coefficient；本文把该低 numerator entropy window扩展到 `0.238062...`。

更一般地，单个 `(R_0,g_0,a_2)` fiber 中由 `Uv_2` period得到

\[
\#\{A_{12}\}
\le
10^{[C_{UV}\delta-U_*]_+S+o(S)},
\]

所以

\[
\boxed{
N_{\rm num}(S;\delta)
\le
10^{\left[
(1+\kappa_{\rm dig})\delta
+[C_{UV}\delta-U_*]_+
\right]S+o(S)}.}
\tag{7.2}
\]

---

## 8. 方法边界与下一核心

`U-CRT` 来自 generic carry，本质上是已有 exact reconstruction 的一个 rational projection；它可用于 fixed-fiber residue/uniqueness，但不应再被解释成 independent local height surplus。

本文同样尚未给出 neighborhood emptiness，因为 denominator/S-unit data 本身仍可移动。现在 numerator side 的主要问题已进一步简化：

- source-square period `q_Q^2` 仍提供额外结构，但 fixed-fiber uniqueness 已不依赖它；
- `D_Sigma` 已由上一文件消掉；
- `U × v_2` 已足以在宽度 `0.238...` neighborhood 内唯一化完整 numerator triple（除去 `R_0,g_0,a_2` 的已量化 entropy）。

因此下一主目标应集中在 denominator/S-unit side：

\[
\boxed{
Q=Uq,
\quad
b_3=BVq,
\quad
2^HZ-5^TU=V,
\quad
V=v_1v_2
}
\]

这些 exact equations 如何限制 `(H,T,U,Z,V,q)` 的总移动 entropy，或者如何让唯一 numerator lift与 digit shell发生 Archimedean 冲突。

---

## 9. 状态摘要

- **已严格完成：** `g0-Sigma` 与 primitive carry。
- **已严格完成：** full `U-CRT`，effective period为整个 `U`。
- **已严格完成：** `(U,v2)=1`，联合 period exact 为 `Uv2`。
- **已严格完成：** joint defect optimization，`C_UV=2+3 log10 2=log10 800`。
- **已严格完成：** fixed-fiber uniqueness window `delta<0.238062349248111...`。
- **已严格完成：** numerator entropy `1.767009998554660... delta S` 的适用窗口同步扩展到 `delta<0.238062...`。
- **仍待证：** denominator/S-unit entropy或 unique-lift digit-shell exclusion；explicit strict slope gap；DD emptiness；effective absolute height bound。
