# A2 equal-depth resonance 的 full decimal tail reader

> **依赖：** `spontaneous-height-equal-depth-resonance.md`、`spontaneous-height-equal-depth-square-core.md`、`spontaneous-height-equal-depth-global-decimal-gcd.md`、`source-discriminant.md`、`primitive-reduction.md`。
>
> **严格状态：**前面的 decimal pair `E_+` 只能给 `v_p(E_+) >= 2h+min(r_B,h,rho_p)`，因此当 resonance tail `rho_p` 超过 `h` 或 `r_B` 时会被截断。本文构造新的纯 decimal 正整数 `Lambda_dec=2 beta Delta_omega+TQ^2 alpha`，并利用 source ratio 的 exact decimal realization 证明对每个 equal-depth oversaturation prime 都有精确公式 `v_p(Lambda_dec)=2h+rho_p`。因此整个 resonance tail `rho_p` 被完整读取，不再有 `h`-cap 或 companion-depth cap。`Lambda_dec` 恰有 `2m+3M+2` 位，并与 `TQ^2 alpha` 只相差一个 `<36 T^2N^2` 的正整数。所有 equal-depth primes 的 weighted tail 可聚合为单一 global divisibility `G_eq^2 R_rho | Lambda_dec`。本文仍不排除这些 weighted primes 的存在，因此不关闭 A2。

---

## 1. equal-depth setting

沿用 genuine non-`3` inert equal-depth oversaturation prime `p`：

\[
\boxed{
v_p(\omega)=v_p(W_q)=h\ge1.}
\tag{1.1}
\]

定义 resonance tail

\[
\boxed{
\rho_p:=v_p(2DgK\omega_0-fqW_0),}
\tag{1.2}
\]

其中

\[
\omega=p^h\omega_0,
\qquad
W_q=p^hW_0.
\]

`spontaneous-height-equal-depth-resonance.md` 已证明

\[
\boxed{
v_p(L_{JB})=h+\rho_p,}
\tag{1.3}
\]

其中

\[
L_{JB}=2N(g\omega)+z(qW_q).
\tag{1.4}
\]

本文的目标是把 (1.3) 完全乘回真实 decimal integers。

---

## 2. source ratio 有两个 exact decimal realizations

`source-discriminant.md` 已证明

\[
\boxed{b_3z=Tc_uQ.}
\tag{2.1}
\]

又因为

\[
g\omega=z+c_u,
\qquad
\beta=TQ+b_3,
\]
所以把 (2.1) 加上 `b_3c_u`：

\[
\boxed{
b_3(g\omega)=c_u\beta.}
\tag{2.2}
\]

因此两个 source linear pieces 都能通过真实 denominator concatenation 读取：

\[
\boxed{
\frac{z}{c_u}=\frac{TQ}{b_3},
\qquad
\frac{g\omega}{c_u}=\frac{\beta}{b_3}.}
\tag{2.3}
\]

这一步是下面 full-tail decimalization 的关键。

---

## 3. `L_JB` 乘回 decimal plane 后得到一个极简单的正整数

沿用

\[
E_M:=2^{M+1}c_Q,
\qquad
Q=E_Mq,
\]

\[
\alpha=\omega W_q,
\qquad
\Delta_\omega=E_MN\omega=Kb_3-Qa_3,
\]

\[
\beta=TQ+b_3.
\]

定义

\[
\boxed{
\Lambda_{\rm dec}
:=2\beta\Delta_\omega+TQ^2\alpha.}
\tag{3.1}
\]

它完全由真实 decimal quantities 组成，而且严格为正。

现在从 (1.4) 出发。第一项：

\[
\begin{aligned}
b_3E_M\omega\,2N(g\omega)
&=2N(E_M\omega)\,b_3(g\omega)\\
&=2N(E_M\omega)c_u\beta\\
&=2c_u\beta\Delta_\omega.
\end{aligned}
\tag{3.2}
\]

第二项使用 (2.1)：

\[
\begin{aligned}
b_3E_M\omega\,z(qW_q)
&=(b_3z)(E_Mq)(\omega W_q)\\
&=(Tc_uQ)Q\alpha\\
&=c_uTQ^2\alpha.
\end{aligned}
\tag{3.3}
\]

相加得到核心 exact identity：

\[
\boxed{
b_3E_M\omega L_{JB}
=c_u\Lambda_{\rm dec}.}
\tag{3.4}
\]

这里没有 rational normalization，也没有 residual source quotient。

---

## 4. `Lambda_dec` 精确读取全部 resonance tail

当前 genuine height prime 与

\[
2\cdot5\cdot b_3\cdot E_M\cdot c_u
\]
分离；特别地

\[
p\nmid b_3E_Mc_u.
\]

由 (1.1)、(1.3)、(3.4)：

\[
\begin{aligned}
v_p(\Lambda_{\rm dec})
&=v_p(\omega)+v_p(L_{JB})\\
&=h+(h+\rho_p).
\end{aligned}
\]

所以得到本文最重要的精确公式：

\[
\boxed{
v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{4.1}
\]

这与旧 `E_+` bound 的差别是本质性的：

\[
\boxed{
\rho_p\text{ 无论多深，都被 }\Lambda_{\rm dec}\text{ 完整读取。}}
\tag{4.2}
\]

没有 `min(h,...)`，也没有 `min(r_B,...)`。

---

## 5. `Lambda_dec` 与 baseline square carrier 形成 near-equal pair

由定义：

\[
\boxed{
\Lambda_{\rm dec}-TQ^2\alpha
=2\beta\Delta_\omega>0.}
\tag{5.1}
\]

对 equal-depth prime，已有

\[
v_p(\alpha)=2h,
\qquad
v_p(\beta)=h,
\qquad
v_p(\Delta_\omega)=h.
\]
且 `p\nmid TQ`。因此

\[
\boxed{
v_p(TQ^2\alpha)=2h,}
\tag{5.2}
\]

\[
\boxed{
v_p(2\beta\Delta_\omega)=2h.}
\tag{5.3}
\]

而 (4.1) 给

\[
\boxed{
v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{5.4}
\]

所以 full resonance tail 正是两个 baseline-depth `2h` 正整数相加后的额外 p-adic cancellation。

---

## 6. `Lambda_dec` 恰有 `2m+3M+2` 位

写 endpoint normalized variables

\[
x=\frac BN,
\qquad
Q/N=x+2,
\]

并沿用

\[
\frac1{10}<x<\frac2{19},
\qquad
N=10^M\ge10^{11}.
\]

square-core 文件给

\[
\frac{2499}{250}
<\frac{\alpha}{TN}<10.
\tag{6.1}
\]

而 decimal-pair 文件给

\[
0<\frac{\Delta_\omega}{TN}<\frac{843}{100},
\tag{6.2}
\]

以及

\[
\frac\beta{TN}
=\frac QN+\frac{b_3/T}{N}
<\frac{211}{100}.
\tag{6.3}
\]

于是

\[
\frac{\Lambda_{\rm dec}}{T^2N^3}
=
\left(\frac QN\right)^2
\frac{\alpha}{TN}
+
\frac2N
\frac\beta{TN}
\frac{\Delta_\omega}{TN}.
\tag{6.4}
\]

下界直接忽略第二个正项：

\[
\frac{\Lambda_{\rm dec}}{T^2N^3}
>
\left(\frac{21}{10}\right)^2
\frac{2499}{250}
=44.08236>44.
\tag{6.5}
\]

上界使用 (6.2)、(6.3)：

\[
\frac{\Lambda_{\rm dec}}{T^2N^3}
<
\left(\frac{40}{19}\right)^2 10
+
\frac2{10^{11}}\frac{211}{100}\frac{843}{100}
<45.
\tag{6.6}
\]

因此

\[
\boxed{
44T^2N^3
<\Lambda_{\rm dec}
<45T^2N^3.}
\tag{6.7}
\]

因为 `T=10^m,N=10^M`：

\[
\boxed{
\Lambda_{\rm dec}
\text{ 恰有 }2m+3M+2\text{ 个十进制数字}.}
\tag{6.8}
\]

同时由 (5.1)、(6.2)、(6.3)：

\[
0<\Lambda_{\rm dec}-TQ^2\alpha
<36T^2N^2.
\tag{6.9}
\]

所以这两个约 `44T^2N^3` 规模的正整数，只在相对 `O(1/N)` 的尺度上分开。

---

## 7. 单个 prime 的 full-tail 高度界

由 (4.1)、(6.7)：

\[
\boxed{
p^{2h+\rho_p}
<45\cdot10^{2m+3M}.}
\tag{7.1}
\]

因此

\[
\boxed{
(2h+\rho_p)\log p
<\log45+(2m+3M)\log10.}
\tag{7.2}
\]

与旧 `p^{2h+1}|E_+` 相比，这条界读取的是**完整 rho_p**，不是只知道它至少为 `1`。

---

## 8. 所有 equal-depth primes 的 full weighted product

令 `E_eq` 为所有当前 equal-depth oversaturation primes，沿用

\[
G_{\rm eq}:=\prod_{p\in E_{\rm eq}}p^{h_p}.
\]

再定义 resonance-tail product

\[
\boxed{
R_\rho
:=\prod_{p\in E_{\rm eq}}p^{\rho_p}.}
\tag{8.1}
\]

其中允许 `rho_p=0`。

由 (4.1) 逐 prime 聚合：

\[
\boxed{
G_{\rm eq}^2R_\rho
\mid\Lambda_{\rm dec}.}
\tag{8.2}
\]

更精确地，对 target prime pool：

\[
\boxed{
\gcd\!\left(
\frac{\Lambda_{\rm dec}}{G_{\rm eq}^2},
\operatorname{SuppMod}(E_{\rm eq})
\right)
\text{ 的 p-depth 恰为 }\rho_p,}
\tag{8.3}
\]

其中 (8.3) 只表示逐 target prime 的 exact valuation，不把 `SuppMod` 当作新的仓库记号。

由 (6.7)：

\[
\boxed{
G_{\rm eq}^2R_\rho
<45\cdot10^{2m+3M}.}
\tag{8.4}
\]

即

\[
\boxed{
\sum_{p\in E_{\rm eq}}
(2h_p+\rho_p)\log p
<\log45+(2m+3M)\log10.}
\tag{8.5}
\]

这严格强化了前一文件只对 `rho_p>=1` 支付一份 radical 的 budget：现在每一层 resonance tail 都要真实支付。

---

## 9. composite tail modulus 上的 exact decimal synchronization

由 (5.1)，并且 `G_eq^2|TQ^2 alpha` 与 `G_eq^2|2 beta Delta_omega`：

\[
\frac{\Lambda_{\rm dec}}{G_{\rm eq}^2}
=
\frac{TQ^2\alpha}{G_{\rm eq}^2}
+
\frac{2\beta\Delta_\omega}{G_{\rm eq}^2}.
\tag{9.1}
\]

对于任一 `rho_p>0` 的 target prime，两项右侧都是 p-units，而左侧含 `p^{rho_p}`。因此若令

\[
R_\rho^+:=\prod_{\rho_p>0}p^{\rho_p},
\]
则有 canonical composite congruence

\[
\boxed{
\frac{TQ^2\alpha}{G_{\rm eq}^2}
\equiv
-\frac{2\beta\Delta_\omega}{G_{\rm eq}^2}
\pmod{R_\rho^+}.}
\tag{9.2}
\]

这就是原 projective source-unit synchronization 的 full decimal version，而且 modulus 读取完整 `rho_p` prime powers。

---

## 10. 当前 frontier

此前 equal-depth branch 的主要缺口是：`rho_p` 一旦超过 `h` 或 companion residual depth，就没有 natural integer 能完整读取。

本文已经消掉这个缺口：

\[
\boxed{
\Lambda_{\rm dec}=2\beta\Delta_\omega+TQ^2\alpha,
\qquad
v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{10.1}
\]

因此真正剩余的问题不再是“如何读取 rho_p”，而是：

1. 如何把 `Lambda_dec` 的 full weighted product bound 与更短的 `alpha` square-core bound 联立；
2. 如何利用 near-equality
   \[
   0<\Lambda_{\rm dec}-TQ^2\alpha<36T^2N^2
   \]
   和两边巨大的共同 square core；
3. 或把 (9.2) 与顶部 defect residue `10TN=C_alpha (mod G_eq^2)` 联立，得到对 `R_rho` 的独立 Archimedean/CRT 限制。

ordinary quadratic character 与 first-layer simple-root 条件已经不再是主要缺口。