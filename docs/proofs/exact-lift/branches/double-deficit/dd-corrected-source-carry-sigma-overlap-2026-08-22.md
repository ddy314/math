# DD corrected terminal 的 source/carry transverse split 与 `Sigma` overlap

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-neighborhood-square-source-crt-2026-08-22.md`](dd-corrected-neighborhood-square-source-crt-2026-08-22.md)、[`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md`](dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md)、[`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md`](dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood）。**
>
> 前两文件分别得到：
>
> 1. source-square period `q_Q^2`，但其 fixed residue显式含 `a_3`；
> 2. pair-max period `v_2`，允许在 fixed gap fiber中让 `a_3` 随 `A_12` 变化。
>
> 本文把 source congruence 与 generic carry联立，消去 `a_3`。结果非常集中：`q_Q^2` 除了与 S-unit sum
>
> \[
> \Sigma=2^HZ+5^TU
> \]
>
> 的 same-prime overlap之外全部保留。定义
>
> \[
> D_\Sigma:=\gcd(q_Q^2,\Sigma).
> \]
>
> 则允许 `a_3` 移动后的 effective source period精确至少为
>
> \[
> q_Q^2/D_\Sigma.
> \]
>
> 因此下一 hard core 被压成一个单独的 **source-square / S-unit-sum overlap**。

---

## 1. 两个 canonical S-unit sums

写

\[
F:=5^T,
\qquad
Y:=FU,
\qquad
X:=2^HZ=Y+V,
\]

\[
\boxed{\Sigma:=X+Y=2FU+V.}
\tag{1.1}
\]

`core.md` §37 的 reduced-tail variables满足

\[
u=LQ_1=2FU,
\qquad
v=V,
\]

所以

\[
\boxed{u+v=\Sigma,}
\qquad
\boxed{u+2v=2X.}
\tag{1.2}
\]

另外

\[
L\omega=10^m=2FB.
\tag{1.3}
\]

---

## 2. generic source parent 与 carry 的 exact compatibility

上一 square-source文件定义 source parent

\[
\boxed{
S_Q
:=LV\omega10^dA_{12}
+a_3(LQ_1+2V).}
\tag{2.1}

并证明

\[
\boxed{q_Q^2\mid S_Q.}
\tag{2.2}
\]

利用 `(1.2)--(1.3)`：

\[
S_Q
=2FBV10^dA_{12}+2Xa_3
=2\left(FBV10^dA_{12}+Xa_3\right).
\tag{2.3}
\]

而 generic carry 为

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.}
\tag{Carry}
\]

将 `(2.3)` 乘 `g_0U` 并代入 `(Carry)`：

\[
\begin{aligned}
g_0US_Q/2
&=F g_0UBV10^dA_{12}+Xg_0Ua_3\\
&=g_0BV10^dA_{12}(FU+X)-X\Sigma R_0\\
&=\Sigma\left(
 g_0B10^dVA_{12}-XR_0
\right).
\end{aligned}
\]

因为 `FU+X=Sigma`。因此 exact identity 为

\[
\boxed{
 g_0U S_Q
=2\Sigma\left(
 g_0B10^dVA_{12}-XR_0
\right).}
\tag{Q-parent-carry}

在 equality terminal normalization 中，清掉 coefficient units后这正是旧 `Q-fixed` parent；本文证明它本来是 generic canonical identity。

---

## 3. 允许 `a_3` 移动后 source period只损失 `Sigma` overlap

固定 denominator/S-unit data以及同一个 gap fiber `(R_0,g_0)`。假设有两个合法候选

\[
(A_{12}^{(1)},a_3^{(1)}),
\qquad
(A_{12}^{(2)},a_3^{(2)}).
\]

记差

\[
\Delta A:=A_{12}^{(1)}-A_{12}^{(2)},
\qquad
\Delta a_3:=a_3^{(1)}-a_3^{(2)}.
\]

由 carry 相减：

\[
\boxed{U\Delta a_3=B10^dV\Delta A.}
\tag{3.1}
\]

由 source parent `(2.2)` 相减：

\[
q_Q^2\mid
LV\omega10^d\Delta A
+(LQ_1+2V)\Delta a_3.
\tag{3.2}
\]

将 `(3.2)` 乘 `U` 并用 `(3.1)`。和 §2 相同的 algebra给

\[
\boxed{
q_Q^2\mid2\Sigma B10^dV\Delta A.}
\tag{3.3}

上一文件已证明

\[
(q_Q,V)=1,
\]

且 `q_Q` 只含非十进制素数，所以

\[
(q_Q,2B10^dV)=1.
\tag{3.4}
\]

定义

\[
\boxed{D_\Sigma:=\gcd(q_Q^2,\Sigma),}
\tag{3.5}
\]

\[
\boxed{M_\Sigma:=\frac{q_Q^2}{D_\Sigma}.}
\tag{3.6}
\]

由 `(3.3)--(3.4)`：

\[
\boxed{M_\Sigma\mid\Delta A.}
\tag{Source-carry-period}
\]

所以即使不固定 `a_3`，同一个 `(R_0,g_0)` gap fiber 内全部 `A_12` 仍落在一个 residue class modulo `M_Sigma`。

---

## 4. 与 pair-max period 严格横截

因为

\[
M_\Sigma\mid q_Q^2
\]

且

\[
(q_Q,v_2)=1,
\]

所以

\[
\boxed{(M_\Sigma,v_2)=1.}
\tag{4.1}
\]

pair-max neighborhood theorem又给

\[
v_2\mid\Delta A.
\]

因此同 gap fiber中的 candidate differences满足

\[
\boxed{v_2M_\Sigma\mid\Delta A.}
\tag{Combined-moving-source-period}
\]

定义 normalized overlap height

\[
\boxed{
S_\Sigma:=\frac1S\log_{10}D_\Sigma.}
\tag{4.2}
\]

由

\[
\log q_Q/S\ge z_*-\delta-o(1),
\]

以及

\[
\log v_2/S\ge1-C_{\rm one}\delta-o(1),
\]

得到

\[
\boxed{
\frac1S\log_{10}(v_2M_\Sigma)
\ge
1+2z_*-(2+C_{\rm one})\delta-S_\Sigma-o(1).}
\tag{4.3}

即

\[
\boxed{
\frac1S\log_{10}(v_2M_\Sigma)
\ge
1.617767155236062\ldots
-4.335049992773302\ldots\delta
-S_\Sigma-o(1).}
\tag{4.4}

---

## 5. transverse source branch 立即给 uniqueness

合法 prefix满足

\[
0<A_{12}<10^{S+2}.
\]

因此若

\[
\boxed{
S_\Sigma
<2z_*-(2+C_{\rm one})\delta-o(1),}
\tag{5.1}
\]

则 `(4.3)` 的 combined period严格超过 `10^{S+2}`，同 gap fiber只能有一个 `A_12`。

数值阈值为

\[
\boxed{
S_\Sigma
<0.617767155236062\ldots
-4.335049992773302\ldots\delta-o(1).}
\tag{Transverse-threshold}
\]

所以 source-square period不需要完整保留；只要它没有几乎全部被 `Sigma` 吞掉，fixed-fiber uniqueness仍然成立。

---

## 6. 若 uniqueness 失败，`Sigma` overlap 必须近乎饱和

反过来，若同一个 fixed gap fiber中存在两个不同合法 prefixes，则 combined modulus不能超过其 difference window。因此 necessarily

\[
\boxed{
S_\Sigma
\ge
2z_*-(2+C_{\rm one})\delta-o(1).}
\tag{Sigma-hard-lower}
\]

当 `delta->0`：

\[
\boxed{
S_\Sigma\ge2z_*-o(1)
=0.617767155236\ldots-o(1).}
\tag{6.1}
\]

而 trivially

\[
D_\Sigma\mid q_Q^2.
\]

所以 equality-near multiple-candidate fiber只能出现在：

\[
\boxed{
\text{几乎整个 source square }q_Q^2
\text{ 又重新进入 }\Sigma.}
\tag{Sigma-saturation}
\]

这把此前模糊的 “source residue moving with `a_3`” 缺口压成一个单独 same-prime overlap。

---

## 7. `Sigma` overlap 是 denominator-only nested contact

reduced-tail definitions为

\[
t=(10^mQ,b_3),
\]

\[
u=\frac{10^mQ}{t},
\qquad
v=\frac{b_3}{t}.
\]

因此

\[
\boxed{
\Sigma=u+v
=\frac{10^mQ+b_3}{t}
=\frac\beta t.}
\tag{7.1}
\]

另一方面 canonical third-denominator factorization给

\[
\boxed{t=Bq.}
\tag{7.2}
\]

而 `q_Q|q`。所以

\[
\boxed{
D_\Sigma
=\gcd\left(q_Q^2,\frac\beta t\right),
\qquad q_Q\mid\frac tB.}
\tag{Nested-denominator-contact}
\]

这揭示 hard branch 的真正含义：

1. 同一 rough source prime-power先进入 common tail divisor `t`；
2. 除去 `t` 后，它又以近 square depth重现于 complementary denominator cofactor `beta/t`。

它不再是一个 numerator/carry 模糊量。

canonical S-unit phase还有

\[
\kappa+G=\gamma\Sigma,
\]

所以同一 hard overlap也可写成

\[
D_\Sigma\mid\frac{\kappa+G}{\gamma}.
\tag{7.3}
\]

因此下一步可从两个完全 denominator/S-unit 坐标攻击：

\[
\boxed{
q_Q\mid t/B,
\qquad
D_\Sigma\mid\beta/t
}
\]

或

\[
\boxed{
q_Q\mid q,
\qquad
D_\Sigma\mid(\kappa+G)/\gamma.
}
\]

---

## 8. 一般 candidate-count version

不要求 uniqueness时，`(Combined-moving-source-period)` 仍给同 gap fiber内

\[
\#\{A_{12}\}
\le
1+rac{10^{S+2}}{v_2M_\Sigma}.
\]

所以

\[
\boxed{
\#\{A_{12}\mid R_0,g_0,\text{fixed denominator data}\}
\le
10^{\left[(2+C_{\rm one})\delta+S_\Sigma-2z_*\right]_+S+o(S)}.}
\tag{8.1}
\]

这精确插值于：

- `S_Sigma=0` 的 full transverse uniqueness；
- `S_Sigma≈2z_*` 的 pairmax-only critical behavior。

---

## 9. 当前 frontier

经过本文，corrected terminal neighborhood 的 source/pairmax/fiber picture 可压缩为：

\[
\boxed{
\begin{array}{c}
q_Q^2\mid\text{generic source parent},\\
(q_Q,V)=1,\\
v_2\text{ gives a full fixed }A_{12}\text{ period},\\
\text{allowing }a_3\text{ to move loses only }D_\Sigma=(q_Q^2,\Sigma).
\end{array}}
\]

因此下一证明目标已经非常具体：

\[
\boxed{
\text{给 }D_\Sigma
=\gcd(q_Q^2,\beta/t)
\text{ 一个严格小于 }2\log q_Q
\text{ 的 uniform height bound，}
}
\]

或者证明 `Sigma-saturation` 会强迫一个第二独立 denominator/S-unit contact。

这条路线已经完全避开：

- 错误的 unified-root / gap-root 识别；
- equality-only `q_c` 命名；
- rational/genuine split；
- 再次把 sphere square-depth重复计费。

---

## 10. 状态摘要

- **已严格完成：** `Q-parent-carry` exact compatibility。
- **已严格完成：** moving `a_3` 后的 source period `M_Sigma=q_Q^2/D_Sigma`。
- **已严格完成：** 与 `v_2` 的 exact transverse product period。
- **已严格完成：** `Transverse-threshold` 与 `Sigma-hard-lower`。
- **已严格完成：** `Nested-denominator-contact`, 把 hard overlap改写成 `t` / `beta/t` 的 same-prime nested contact。
- **待证唯一 hard core：** `D_Sigma` 的 strict height bound / saturation contradiction。
- **仍未证明：** explicit strict slope gap、DD emptiness、effective absolute height bound。
