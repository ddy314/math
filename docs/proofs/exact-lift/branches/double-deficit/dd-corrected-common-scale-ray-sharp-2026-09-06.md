# DD corrected common-scale ray 的 `UV` shared-defect sharp extension

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-common-scale-ray-2026-09-06.md`](dd-corrected-common-scale-ray-2026-09-06.md)、[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-rough-source-sharp-2026-08-22.md`](dd-corrected-terminal-rough-source-sharp-2026-08-22.md)。
>
> **严格状态：已严格完成（整个 corrected canonical `t_2=1` quantitative one-channel neighborhood；该输入文件固定 `delta<=1/2`）。**
>
> 前一 common-scale theorem 逐个使用 `tau_1,tau_2,U` 的粗 height window，得到
> \[
> \delta<0.156961684731344\ldots
> \]
> 的 projective cofactor lock。本文观察到 fixed factor split 中更自然的 determinant box其实是
> \[
> \boxed{|\Delta_\tau|<2\,10^S/V,}
> \]
> 而同一 shared-defect ledger 精确给
> \[
> \boxed{
> \frac{\log_{10}(UV)}S
> \ge1+U_*-\delta-o(1).}
> \]
> 因为 `U_*=0.691116422381969...`，理论 comparison只要求 `delta<U_*`；这严格覆盖 one-channel theorem 本身的完整作用域 `delta<=1/2`。所以 common-scale ray 不再只是 near-frontier 小邻域结论，而是 **整个 corrected one-channel neighborhood 的统一 denominator-shape theorem**。

---

## 1. fixed factor split 的 determinant box只读取 decimal widths

沿前一 theorem notation：

\[
V=v_1v_2,
\qquad
\tau_1=b_1/v_1,
\qquad
\tau_2=b_2/v_2,
\]

且同一 fixed phase/factor fiber 中

\[
U\mid
\Delta_\tau
:=\tau_2\tau_1'-\tau_2'\tau_1.
\tag{1.1}
\]

因为 `b_1,b_1'` 都是 `m_1` 位正整数：

\[
0<\tau_1,\tau_1'<\frac{10^{m_1}}{v_1}.
\]

同理

\[
0<\tau_2,\tau_2'<\frac{10^{m_2}}{v_2}.
\]

于是两个 cross products都有 exact decimal-box upper

\[
\tau_2\tau_1'
<\frac{10^{m_1+m_2}}{v_1v_2}
=\frac{10^S}{V},
\]

\[
\tau_2'\tau_1
<\frac{10^S}{V}.
\]

所以若 determinant非零：

\[
\boxed{
0<|\Delta_\tau|
<\frac{2\,10^S}{V}.}
\tag{Det-box-sharp}
\]

这比前一 theorem 的

\[
10^{(\kappa_{\rm dig}+C_{\rm one})\delta S+o(S)}
\]

严格更自然：它不把两个 candidates 的 individual cofactor maxima独立相乘，而直接使用固定 decimal widths 与固定 factor split。

---

## 2. `UV` 的 uncoarsened lower

仍令

\[
a:=\log_{10}2,
\qquad b:=1-a,
\]

\[
A:=\frac{2(1+2a)}3,
\qquad
\lambda:=\frac{2+a}{1+2a},
\]

\[
U_*:=0.691116422381969\ldots,
\qquad
\mu:=M_*-M.
\]

已有 uncoarsened `U` identity

\[
\boxed{
\frac{\log_{10}U}{S}-U_*
=
\frac{2b}{3}\mu
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1).}
\tag{2.1}
\]

由

\[
G=\gamma V,
\qquad
\frac{\log_{10}G}{S}=1+o(1),
\]

有

\[
\boxed{
\frac{\log_{10}V}{S}
=1-aG_2-bG_5-R+o(1).}
\tag{2.2}
\]

相加：

\[
\begin{aligned}
\frac{\log_{10}(UV)}S-(1+U_*)
={}&\frac{2b}{3}\mu
-2aG_2
-\frac{2b}{3}Q_5\\
&-\frac{4b}{3}G_5
-\frac b3N_5-2R+o(1).
\end{aligned}
\tag{2.3}
\]

---

## 3. 用同一个 short denominator读取 `G_2`

前一 sharp product-lock continuation已经恢复了 digit theorem 中未粗化的 short-denominator upper：

\[
\boxed{
\begin{aligned}
\frac{m_1}{S}
\le{}&\frac\delta2
-\left(1-\frac b3\right)\mu
-\frac b3Q_5
+\frac b3G_5\\
&-\frac b6N_5
+\frac R2+o(1).
\end{aligned}}
\tag{m1-sharp}
\]

同时 two-adic theorem给

\[
\boxed{
aG_2
\le\frac{m_1}{S}+aQ_2+o(1).}
\tag{G2-via-m1}
\]

在 `(2.3)` 中使用

\[
-2aG_2
\ge
-2\frac{m_1}{S}-2aQ_2-o(1),
\]

再代入 `(m1-sharp)`。`Q_5,N_5` 精确 cancellation，得到

\[
\boxed{
\frac{\log_{10}(UV)}S-(1+U_*)
\ge
-\delta+2\mu-2aQ_2-2bG_5-3R-o(1).}
\tag{UV-prebudget}
\]

---

## 4. `(Mu-budget)` 后所有 correction 都变成正项

沿用 exact normalized identity

\[
\boxed{
A\mu
=\sigma_S
+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R+o(1).}
\tag{Mu-budget}
\]

代入 `(UV-prebudget)`。利用

\[
\frac2A=2\lambda-1,
\]

整理得到

\[
\boxed{
\begin{aligned}
\frac{\log_{10}(UV)}S
\ge{}&1+U_*-\delta
+(2\lambda-1)\sigma_S\\
&+4a(\lambda-1)Q_2
+a(2\lambda-1)N_2\\
&+\frac{2b(2\lambda-1)}3Q_5
+\frac{2b(4\lambda-5)}3G_5\\
&+\frac{b(2\lambda-1)}3N_5
+(4\lambda-5)R-o(1).
\end{aligned}}
\tag{UV-sharp-full}
\]

corrected constant满足

\[
\lambda=1.436294525872677\ldots>\frac54,
\]

所以

\[
4\lambda-5>0.
\]

所有显示 correction 均非负，于是得到 universal sharp lower

\[
\boxed{
\frac{\log_{10}(UV)}S
\ge1+U_*-\delta-o(1).}
\tag{UV-sharp}
\]

---

## 5. cofactor projective ratio在整个 one-channel neighborhood 唯一

由 `(Det-box-sharp)`，若两个 cofactor ratios不同，则

\[
0<|\Delta_\tau|<2\,10^S/V.
\]

若

\[
UV>2\,10^S,
\]

则右侧严格小于 `U`，与 `U|Delta_tau` 矛盾。

`(UV-sharp)` 给

\[
\frac1S\log_{10}\frac{UV}{10^S}
\ge U_*-\delta-o(1).
\]

因此对任意 fixed

\[
\boxed{\delta<U_*}
\tag{5.1}
\]

sufficiently large `S` 上都有 `UV>2*10^S`，从而

\[
\boxed{
\tau_2/\tau_1
\text{ 在 fixed phase/factor fiber 中至多一个}.}
\tag{Projective-cofactor-lock-sharp}
\]

数值上

\[
U_*=0.691116422381969\ldots.
\]

但 quantitative one-channel theorem 的现行作用域已经固定

\[
\delta\le\frac12.
\]

所以在当前证明树中可以直接写成：

\[
\boxed{
\text{整个 corrected quantitative one-channel neighborhood }
(\delta\le1/2)
\text{ 都满足 cofactor projective uniqueness}.}
\tag{One-channel-ray-global}
\]

---

## 6. common-scale ray 与 entropy sharpen 全部扩展到 `delta<=1/2`

前一 common-scale theorem §§5--8 在 projective ratio唯一之后只使用 exact algebra：

1. 取 primitive ratio `s/r`；
2. 写 `tau_1=kr,tau_2=ks`；
3. 从 `Uq=kD` 抽出 `k=U_0 ell`；
4. 得到
   \[
   (b_1,b_2,b_3,q,\gamma)
   =(\ell\bar b_1,\ell\bar b_2,\ell\bar b_3,
   \ell\bar q,\ell^2\bar\gamma);
   \]
5. common scale `ell` 对 padded-width Exact-Lift equality 是 homogeneous direction；
6. fixed `(sigma_S,R)` layer 中 scale multiplicity至多 `10^{(R/2)S+o(S)}`。

这些步骤不再需要原 `delta_ray=0.15696...` 的额外假设。因此它们全部扩展到 one-channel 的完整现行范围：

\[
\boxed{
N_{\rm den/SU}
\le
10^{(\sigma_S+R/2)S+o(S)}
\qquad(\delta\le1/2).}
\tag{Ray-refined-den-entropy-sharp}
\]

注意 uniform worst-case coarse bound依然可能由 `sigma_S` 支配，故本文仍不单独给出 strict slope gap；但 rough `gamma` 作为独立 projective shape 的解释现在已经在整个 one-channel neighborhood 中被撤销。

---

## 7. 与 sharp `qZ` lock 的覆盖关系

sharp product-lock theorem作用于

\[
\delta<0.191116422381969\ldots,
\]

而 common-scale ray现在作用于整个

\[
\delta\le1/2.
\]

所以 product-lock neighborhood 自动拥有 scale-ray structure。特别地，在

\[
\delta<0.191116422381969\ldots
\]

内同时有：

- `qZ` ordinary least-residue lock；
- fixed-`v_2` denominator reconstruction；
- common-scale-ray quotient；
- fixed-denominator numerator collapse。

这使 terminal 小邻域的非齐次 denominator shape residual只剩 Farey/S-unit primitive phase与 `V` 的 divisor split。

---

## 8. 状态与下一核心

本文没有添加新 prime-depth payer；`UV-sharp` 完全来自已经存在的 corrected formulas 与一次 shared-defect substitution。

新的严格结构是：

\[
\boxed{
\text{rough }\gamma\text{ 的 denominator-shape freedom在整个 one-channel neighborhood中退化为 common scale}.}
\]

因此后续 terminal 攻击应停止把 `gamma_0` 与 Farey slack并列当作两个 projective moving cores。scale quotient 后的真正 primitive residual是

\[
\boxed{
(U,Z,V)
\text{ 的 Farey/S-unit phase}
\quad+\quad
V=v_1v_2\text{ 的 divisor assignment}.}
\]

后者只有 divisor entropy；所以 uniform projective obstruction已进一步集中到 Farey/S-unit phase本身。

---

## 9. verification scope

配套机械审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_common_scale_ray_sharp.py
```

脚本检查：

- fixed digit box 给 `|Delta_tau|<2*10^S/V`；
- `m1-sharp + G2-via-m1` 代入 `log(UV)` 后的 cancellation；
- `(Mu-budget)` 后 `UV-sharp-full` 全部 correction coefficients非负；
- `delta<=1/2<U_*` 的覆盖关系。

有限 checks只核对 algebra/constants；渐近 theorem由正文引用的 corrected inequalities承担。

---

## 10. 状态摘要

- **determinant sharpen：** `|Delta_tau|` 从 individual cofactor box改为 exact fixed-width box `2*10^S/V`。
- **已严格完成：** `UV-sharp-full` 与 universal `UV-sharp`。
- **coverage sharpen：** cofactor projective lock / common-scale ray 从 `delta<0.1569616847...` 扩展到整个现行 one-channel neighborhood `delta<=1/2`。
- **entropy sharpen coverage：** `sigma_S+R/2` bound 同样扩展到 `delta<=1/2`。
- **仍待证：** scale-quotiented Farey/S-unit primitive phase exclusion；explicit strict slope gap；DD emptiness；更低 post-tail / non-canonical dominant states 的统一 simultaneous height bound。
