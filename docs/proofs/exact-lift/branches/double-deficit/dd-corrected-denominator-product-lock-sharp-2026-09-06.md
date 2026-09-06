# DD corrected denominator `qZ` product lock 的 shared-defect sharp threshold

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-denominator-product-lock-2026-09-06.md`](dd-corrected-denominator-product-lock-2026-09-06.md)、[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-rough-source-sharp-2026-08-22.md`](dd-corrected-terminal-rough-source-sharp-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood）。**
>
> 前一 denominator product-lock theorem 用已经粗化的 individual `U`、`Z`、`v_2` windows，得到安全阈值
> \[
> \delta<0.075150109396892\ldots.
> \]
> 本文保留这些 windows 粗化前共享的 quantitative-defect variables，重新做一次 no-double-count 消元。结果是两个非常简洁的 sharp bounds：
> \[
> \boxed{
> \frac{\log_{10}(qZ)}S
> \le2z_*+\delta+o(1),}
> \]
> \[
> \boxed{
> \frac{\log_{10}v_2}S
> \ge1-\delta-o(1).}
> \]
> 因而 `qZ<v_2` 的 product-lock neighborhood 扩大到
> \[
> \boxed{
> \delta<\delta_{qZ}^{\sharp}
> :=\frac12-z_*
> =0.191116422381969\ldots.}
> \]
> 前一文件的 exact congruence 与 downstream reconstruction 全部保持不变，只是 threshold 被本文严格替换为更宽范围。

---

## 1. constants 与 normalized defects

令

\[
a:=\log_{10}2,
\qquad b:=1-a=\log_{10}5,
\]

\[
A:=\frac{2(1+2a)}3,
\qquad
\lambda:=\frac{2+a}{1+2a},
\]

\[
M_*:=2.808883577618031\ldots,
\qquad
U_*:=0.691116422381969\ldots,
\]

\[
\boxed{z_*:=1-U_*=0.308883577618031\ldots.}
\tag{1.1}
\]

写

\[
\delta:=c_*-\frac nS,
\qquad
\mu:=M_*-\frac mS.
\]

使用 corrected defect variables

\[
\sigma_S,Q_2,N_2,Q_5,G_5,N_5,R\ge-o(1).
\]

`dd-corrected-terminal-rough-source-sharp-2026-08-22.md` 已记录由 Schmidt slack 定义直接得到的 exact normalized identity

\[
\boxed{
A\mu
=\sigma_S
+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R+o(1).}
\tag{Mu-budget}
\]

后续所有 sharpen 都使用同一份 `(Mu-budget)`，不允许每个 window 独立花一整份 `delta`。

---

## 2. short denominator 的未粗化 upper

quantitative digit-polarization proof 在丢掉正 defect 之前给

\[
\begin{aligned}
\frac{s+D_s}{S}
\ge{}&2-\delta
+\left(2-\frac{2b}{3}\right)\mu
+\frac{2b}{3}Q_5\\
&-\frac{2b}{3}G_5
+\frac b3N_5-R-o(1).
\end{aligned}
\tag{2.1}
\]

交换前两 prefix labels后取

\[
s_1=\max(s_1,s_2)
=\frac{s+D_s}{2}.
\]

又 `s=s_1+s_2<=2`，且 `n_2=m_2+s_2>=1`，所以

\[
\frac{m_1}{S}
\le1-\frac{s_1}{S}+o(1).
\tag{2.2}
\]

将 `(2.1)` 代入 `(2.2)`，得到比旧 `m_1<=kappa_dig delta S` 更适合联合优化的精确版本：

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

---

## 3. `G_2` 不需要单独支付一份 defect

`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md` 已证明 long denominator 的 2-depth满足

\[
v_2(b_2)=v_2(Q).
\]

因为

\[
G=b_1b_2,
\]

令 normalized 2-depth仍记为 `G_2,Q_2`，则

\[
G_2
\le\frac1a\frac{m_1}{S}+Q_2+o(1).
\]

等价地：

\[
\boxed{
aG_2
\le\frac{m_1}{S}+aQ_2+o(1).}
\tag{G2-via-m1}
\]

本文始终把 `(G2-via-m1)` 与 `(m1-sharp)` 同时使用；这正是旧 individual windows 中最主要的重复损失来源之一。

---

## 4. `qZ` 的 loss 精确压到 `delta`

canonical formulas在粗化前给 `U`：

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
\tag{4.1}
\]

prefix concat `Q` 恰有 `S` 位，因此

\[
\frac{\log_{10}Q}{S}=1+o(1).
\]

由 `Q=Uq`：

\[
\boxed{
\begin{aligned}
\frac{\log_{10}q}{S}-z_*
={}&-\frac{2b}{3}\mu
+aG_2
+\frac{2b}{3}Q_5\\
&+\frac b3G_5
+\frac b3N_5+R+o(1).
\end{aligned}}
\tag{4.2}
\]

同一 two-adic theorem 给 `Z` 的未粗化 identity

\[
\boxed{
\frac{\log_{10}Z}{S}-z_*
=2a\mu-2aQ_2-aN_2+aG_2-bG_5-R+o(1).}
\tag{4.3}
\]

将 `(4.2),(4.3)` 相加：

\[
\begin{aligned}
\frac{\log_{10}(qZ)}S-2z_*
={}&\left(2a-\frac{2b}{3}\right)\mu
+2aG_2-2aQ_2-aN_2\\
&+\frac{2b}{3}Q_5
-\frac{2b}{3}G_5
+\frac b3N_5+o(1).
\end{aligned}
\tag{4.4}
\]

这里 rough `R` 已经 **exact cancellation**。

使用 `(G2-via-m1)`：

\[
2aG_2
\le2\frac{m_1}{S}+2aQ_2+o(1),
\]

再代入 `(m1-sharp)`。`Q_2,Q_5,G_5,N_5` 全部发生精确 cancellation，得到

\[
\boxed{
\frac{\log_{10}(qZ)}S-2z_*
\le
\delta-2b\mu+R-aN_2+o(1).}
\tag{qZ-prebudget}
\]

现在使用 `(Mu-budget)`。令

\[
\boxed{
\theta:=\frac{2b}{A}
=\frac{3b}{1+2a}
=1.308883577618031\ldots.}
\tag{4.5}
\]

则

\[
2b\mu
=\theta\left[
\sigma_S+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)+2R
\right]+o(1).
\]

代回 `(qZ-prebudget)`：

\[
\boxed{
\begin{aligned}
\frac{\log_{10}(qZ)}S-2z_*
\le{}&\delta
-\theta\sigma_S
-2a\theta Q_2
-a(\theta+1)N_2\\
&-\frac{2b\theta}{3}Q_5
-\frac{4b\theta}{3}G_5
-\frac{b\theta}{3}N_5\\
&-(2\theta-1)R+o(1).
\end{aligned}}
\tag{qZ-sharp-full}
\]

`theta>1/2`，所有显示 correction 都非正。因此统一得到

\[
\boxed{
\frac{\log_{10}(qZ)}S
\le2z_*+\delta+o(1).}
\tag{qZ-sharp}
\]

注意：这个 upper 比旧

\[
2z_*+2.751208002477803\,\delta
\]

显著更强；改善完全来自 shared-budget cancellation，没有添加新 arithmetic hypothesis。

---

## 5. `v_2` 的 lower 精确改善到 `1-delta`

由

\[
G=\gamma V,
\qquad
\gamma=2^{G_2S}5^{G_5S}\gamma_0,
\]

以及 `log G/S=1+o(1)`：

\[
\boxed{
\frac{\log_{10}V}{S}
=1-aG_2-bG_5-R+o(1).}
\tag{5.1}
\]

`V=v_1v_2` 且 `v_1|b_1`，故

\[
\frac{\log_{10}v_1}{S}
\le\frac{m_1}{S}+o(1).
\]

所以

\[
\frac{\log_{10}v_2}{S}
\ge
1-aG_2-bG_5-R-\frac{m_1}{S}-o(1).
\tag{5.2}
\]

使用 `(G2-via-m1)`：

\[
\frac{\log_{10}v_2}{S}
\ge
1-\left[
2\frac{m_1}{S}+aQ_2+bG_5+R
\right]-o(1).
\tag{5.3}
\]

将 `(m1-sharp)` 代入方括号：

\[
\begin{aligned}
1-\frac{\log_{10}v_2}{S}
\le{}&\delta
-2\left(1-\frac b3\right)\mu
+aQ_2
-\frac{2b}{3}Q_5\\
&+\frac{5b}{3}G_5
-\frac b3N_5+2R+o(1).
\end{aligned}
\tag{5.4}
\]

关键恒等式是

\[
\boxed{
2\left(1-\frac b3\right)
=\frac{2(2+a)}3
=\lambda A.}
\tag{5.5}
\]

因此用 `(Mu-budget)` 消去 `mu` 后：

\[
\boxed{
\begin{aligned}
\frac{\log_{10}v_2}{S}
\ge{}&1-\delta
+\lambda\sigma_S
+a(2\lambda-1)Q_2
+a\lambda N_2\\
&+\frac{2b(\lambda+1)}3Q_5
+\frac{b(4\lambda-5)}3G_5\\
&+\frac{b(\lambda+1)}3N_5
+2(\lambda-1)R-o(1).
\end{aligned}}
\tag{v2-sharp-full}
\]

这里

\[
\lambda=1.436294525872677\ldots>\frac54,
\]

故 `4lambda-5>0`；所有显示 correction 都非负。于是：

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge1-\delta-o(1).}
\tag{v2-sharp}
\]

这把旧 one-channel 粗 bound

\[
1-2.335049992773302\,\delta
\]

在当前 shared-defect comparison 中严格改善为 coefficient `1`。

---

## 6. sharp `qZ<v_2` threshold

由 `(qZ-sharp)` 与 `(v2-sharp)`：

\[
\frac1S\log_{10}\frac{v_2}{qZ}
\ge
1-2z_*-2\delta-o(1).
\]

因此只要

\[
1-2z_*-2\delta>0,
\]

sufficiently large `S` 上就有

\[
\boxed{0<qZ<v_2.}
\]

定义

\[
\boxed{
\delta_{qZ}^{\sharp}
:=\frac{1-2z_*}{2}
=\frac12-z_*
=0.191116422381969\ldots.}
\tag{6.1}
\]

得到

\[
\boxed{
\delta<\delta_{qZ}^{\sharp}
\Longrightarrow
0<qZ<v_2
\quad\text{eventually}.}
\tag{Small-product-sharp}
\]

这个常数恰等于旧 frontier Gaussian Euclidean quotient 中出现的

\[
\rho_*:=\frac12-z_*.
\]

这里它有一个新的纯 denominator/S-unit 含义：正是 `qZ` baseline `2z_*` 与 one-channel baseline `1` 之间的一半 height margin。

---

## 7. exact product lock 与 downstream reconstruction 全部扩宽

前一 product-lock theorem 已严格证明 exact congruence

\[
\boxed{
2^HqZ
\equiv
5^Tb_1 10^{m_2}
\pmod{v_2}.}
\tag{7.1}
\]

并定义 least residue

\[
\rho_{v_2}
:=
\left[
2^{-H}5^Tb_1 10^{m_2}
\right]_{v_2},
\qquad0\le\rho_{v_2}<v_2.
\]

`(Small-product-sharp)` 现在允许在整个

\[
\delta<0.191116422381969\ldots
\]

中把 `(7.1)` 升级为 ordinary integer equality

\[
\boxed{qZ=\rho_{v_2}.}
\tag{qZ-product-lock-sharp}
\]

前一 theorem §§5--8 的后续 reconstruction只使用：

1. `qZ` 被 fixed `(v_2,b_1,H,T,m_2)` 唯一恢复；
2. `(q,Z)` 只来自 `qZ` 的 divisor pairs；
3. `v_1|b_1`；
4. S-unit identity恢复 `U`；
5. `Q=Uq` 与 decimal concat恢复 `b_2`；
6. `b_3=BVq`；
7. numerator collapse threshold `delta_UV=0.238062349248111...`。

而

\[
\delta_{qZ}^{\sharp}
=0.191116422381969\ldots
<\delta_{UV}.
\]

所以这些结论全部自动扩宽为：

\[
\boxed{
N_{\rm den/SU}\mid(v_2,b_1,\text{exponent layer})
=10^{o(S)}
\qquad(\delta<\delta_{qZ}^{\sharp}),}
\tag{7.2}
\]

\[
\boxed{
N_{\rm full}\mid v_2
\le
10^{\kappa_{\rm dig}\delta S+o(S)}
\qquad(\delta<\delta_{qZ}^{\sharp}).}
\tag{7.3}
\]

即 fixed-`v_2` full-fiber collapse 的有效宽度从

\[
0.075150109396892\ldots
\]

扩到

\[
\boxed{0.191116422381969\ldots.}
\]

---

## 8. 与 common-scale ray theorem 的关系

`dd-corrected-common-scale-ray-2026-09-06.md` 的 threshold为

\[
\delta_{\rm ray}=0.156961684731344\ldots.
\]

数值顺序现在是

\[
\boxed{
\delta_{\rm ray}
<\delta_{qZ}^{\sharp}
<\delta_{UV}.}
\]

因此整个 common-scale-ray neighborhood 自动位于 sharp product-lock neighborhood 内。也就是说，在

\[
\delta<0.156961684731344\ldots
\]

中可以同时使用：

- exact `qZ` ordinary product lock；
- cofactor projective ratio uniqueness；
- denominator common-scale ray；
- fixed-denominator numerator `10^{o(S)}` collapse。

terminal residual core因而比前一版本更集中：scale-quotiented后只剩 Farey/S-unit primitive phase；common scale `ell` 是 homogeneous direction。

---

## 9. 状态与方法边界

本文没有新增任何 local prime-depth payer。所有改进来自已有 corrected identities的联合使用，特别是：

- `R` 在 `qZ` 的 uncoarsened sum中先 exact cancellation；
- `G_2` 通过同一 short denominator `m_1` 读取；
- `m_1` 保留 `mu,Q_5,G_5,N_5,R` 的原始 signs；
- 最后只使用一次 `(Mu-budget)`。

所以旧 `0.07515...` 并非真实 arithmetic barrier，只是 individual-window coarse threshold。

本文仍没有证明

\[
\delta\ge\delta_0>0
\]

或 DD emptiness。它把 terminal near-frontier 的 denominator reconstruction显著扩宽，并把下一 uniform bottleneck进一步固定在 scale-quotiented Farey/projective primitive phase。

---

## 10. verification scope

配套机械审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_denominator_product_lock_sharp.py
```

脚本检查：

- `m1-sharp` 代入后 `qZ` 中 `Q_2,Q_5,G_5,N_5` 的 symbolic cancellation；
- `(Mu-budget)` 后 `qZ-sharp-full` 所有 correction 的 signs；
- `v2-sharp-full` 各 coefficient 的 signs，特别是 `4lambda-5>0`；
- sharp threshold `delta_qZ^sharp=1/2-z_*` 与 `delta_ray,delta_UV` 的顺序。

有限 symbolic checks只核对代数和常数；渐近 theorem来自正文引用的 corrected inequalities。

---

## 11. 状态摘要

- **已严格完成：** `qZ-sharp-full` 与 universal `qZ-sharp`。
- **已严格完成：** `v2-sharp-full` 与 universal `v2-sharp`。
- **threshold sharpen：**
  \[
  \delta_{qZ}:0.075150109396892\ldots
  \longrightarrow
  \delta_{qZ}^{\sharp}=0.191116422381969\ldots.
  \]
- **downstream sharpen：** fixed-`v_2` denominator/full-candidate collapse全部扩宽到 `delta<delta_qZ^sharp`。
- **仍待证：** scale-quotiented Farey/projective primitive phase exclusion；explicit strict slope gap；DD emptiness；更低 post-tail / non-canonical dominant states 的统一 simultaneous height bound。
