# DD global sixfold primitive hard-source lock

> 日期：2026-09-06
>
> 依赖：[`dd-global-sixfold-decimal-folding-source-lock-2026-09-06.md`](dd-global-sixfold-decimal-folding-source-lock-2026-09-06.md)、[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)、[`dd-global-sixfold-gcd-stripped-master-lock-2026-09-06.md`](dd-global-sixfold-gcd-stripped-master-lock-2026-09-06.md)。
>
> **严格状态：已严格完成（整个 corrected odd non-decimal hard-source sheet）。**
>
> 前一 sixfold master直接在 raw prefix `Q=b_1 10^{m_2}+b_2` 上工作，因此 coefficient 中保留 `b_2^6` 的 denominator-common baseline。本文先做 denominator-prefix primitive normalization，再 folding。结果是：对 corrected hard sheet 的每个 odd non-decimal hard prime，sixfold coefficient 与右端拥有**完全相同**的 baseline depth `M+t`；约掉后剩余 modulus depth恒为
>
> \[
> \boxed{r_p^{\rm prim}=h+t+n_0+j>0.}
> \]
>
> 因此不再存在 previous primewise theorem 中的 `r_p<=0` bad support，也不需要 full-height hypothesis。整个 corrected hard source天然携带一个 coefficient-unit global decimal-power modulus。

---

## 1. primitive denominator prefix

令

\[
\boxed{d_B:=(b_1,b_2),}
\]

\[
\boxed{u_1:=b_1/d_B,\qquad u_2:=b_2/d_B.}
\]

则

\[
(u_1,u_2)=1
\]

且

\[
Q=d_B C_Q,
\qquad
\boxed{C_Q=u_1 10^{m_2}+u_2.}
\tag{1.1}
\]

因此对任意 odd non-decimal prime `p|C_Q`：

\[
\boxed{p\nmid u_1u_2.}
\tag{1.2}
\]

确实，若 `p|u_2`，由 `(1.1)` 有 `p|u_1 10^{m_2}`；因 `p\nmid10`，得到 `p|u_1`，与 `(u_1,u_2)=1` 矛盾。`u_1` 同理。

---

## 2. primitive sixfold folding

设

\[
S=m_1+m_2,
\qquad
6S<n<7S,
\qquad
\boxed{e:=n-6S.}
\]

full exact lift modulo `C_Q|Q` 给

\[
q_{\rm lcm}A_{12}10^n
\equiv
D_3
\pmod{C_Q},
\tag{2.1}
\]

其中

\[
D_3:=H_{\rm sph}b_3-q_{\rm lcm}a_3.
\]

由 `(1.1)`：

\[
u_1 10^{m_2}\equiv-u_2\pmod{C_Q}.
\]

六次幂后符号消失：

\[
u_1^6 10^{6m_2}\equiv u_2^6\pmod{C_Q}.
\]

把 `(2.1)` 乘 `u_1^6`，并用

\[
10^n=10^{6m_1}10^{6m_2}10^e,
\]
得到

\[
\boxed{
C_Q\mid
C_{6,\rm prim}10^e-D_{6,\rm prim},}
\tag{Primitive-sixfold}
\]

其中

\[
\boxed{
C_{6,\rm prim}
:=q_{\rm lcm}A_{12}u_2^6 10^{6m_1},}
\tag{2.2}
\]

\[
\boxed{
D_{6,\rm prim}
:=u_1^6D_3.}
\tag{2.3}
\]

这条 identity 对任意 DD candidate 都成立；下面只在 corrected hard source support上做 valuation stripping。

---

## 3. corrected hard-prime ledger

固定 odd non-decimal hard prime `p`。沿 corrected notation：

\[
E=v_p(b_1)=v_p(b_2),
\qquad
j=v_p(b_3),
\]

\[
M:=\max(E,j),
\qquad
t:=v_p(A_{12}),
\qquad n_0:=v_p(N_0),
\]

\[
c:=v_p(C_Q),
\qquad h>0.
\]

corrected hard-source theorem给 exact ledger

\[
\boxed{
c=h+2t+n_0+M+j.}
\tag{Hard-ledger}
\]

因为 `d_B` 吸收了 `E`，由 `(1.2)`：

\[
v_p(u_1)=v_p(u_2)=0.
\tag{3.1}
\]

又 `q_lcm` 的 denominator-lcm valuation为

\[
\boxed{v_p(q_{\rm lcm})=M.}
\tag{3.2}
\]

因此 primitive sixfold coefficient满足

\[
\boxed{
v_p(C_{6,\rm prim})=M+t.}
\tag{3.3}
\]

---

## 4. right side拥有完全相同 baseline depth

hard sheet已有 gap baseline

\[
\boxed{v_p(a)=t+(E-j)_+.}
\tag{4.1}
\]

并且

\[
D_3
=b_3(H_{\rm sph}-y_3)
=b_3La.
\]

对 odd non-decimal `p`，`L` 是 `2/5`-smooth，故

\[
\begin{aligned}
v_p(D_3)
&=j+v_p(a)\\
&=j+t+(E-j)_+\\
&=t+\max(E,j)\\
&=\boxed{M+t}.
\end{aligned}
\tag{4.2}
\]

由 `u_1` 为 p-unit：

\[
\boxed{
v_p(D_{6,\rm prim})=M+t.}
\tag{4.3}
\]

所以 `(Primitive-sixfold)` 的 coefficient 与 right side在每个 hard prime上 baseline depth完全一致。

---

## 5. exact primitive stripping

由 `(Hard-ledger)` 与 `(3.3)`：

\[
\begin{aligned}
r_p^{\rm prim}
&:=c-(M+t)\\
&=h+t+n_0+j.
\end{aligned}
\]

因此

\[
\boxed{
r_p^{\rm prim}=h+t+n_0+j>0.}
\tag{Primitive-depth}
\]

对该 prime把 `(Primitive-sixfold)` 精确除以 `p^{M+t}`。得到模

\[
p^{r_p^{\rm prim}}
\]

的 congruence，且除后的 coefficient与 right side都是 p-units。

这一步没有 `good/bad` split：只要 `h>0`，就自动有 strictly positive primitive modulus depth。

---

## 6. global primitive hard modulus

在全部 hard-source support上定义

\[
X_H:=\prod p^h,
\qquad
T_H:=\prod p^t,
\qquad
N_H:=\prod p^{n_0},
\qquad
J_H:=\prod p^j.
\]

并定义 primitive sixfold hard modulus

\[
\boxed{
\mathfrak C_6
:=\prod_{p\mid X_H}p^{r_p^{\rm prim}}.}
\tag{6.1}
\]

由 `(Primitive-depth)`：

\[
\boxed{
\mathfrak C_6=X_HT_HN_HJ_H.}
\tag{Primitive-global-modulus}
\]

逐 prime stripping后存在整数 `\widehat C_6,\widehat D_6`，使

\[
\boxed{
\mathfrak C_6\mid
\widehat C_6 10^e-\widehat D_6,}
\tag{6.2}
\]

且

\[
\boxed{(\widehat C_6,\mathfrak C_6)=1,\qquad
(\widehat D_6,\mathfrak C_6)=1.}
\tag{6.3}
\]

所以

\[
\boxed{
10^e\equiv
\widehat D_6\widehat C_6^{-1}
\pmod{\mathfrak C_6}.}
\tag{Primitive-hard-residue}
\]

---

## 7. ordinary-lock dichotomy

若

\[
\boxed{
\log_{10}\mathfrak C_6>e,}
\tag{7.1}
\]

则 `0<10^e<\mathfrak C_6`，于是

\[
\boxed{
10^{n-6S}
=
[\widehat D_6\widehat C_6^{-1}]_{\mathfrak C_6}.}
\tag{Primitive-hard-lock}
\]

反之，若 ordinary lock criterion失败，则 necessarily

\[
\boxed{
\log_{10}(X_HT_HN_HJ_H)
\le n-6S.}
\tag{Primitive-failure-charge}
\]

normalized 写成

\[
\boxed{
\frac{\log X_H+\log T_H+\log N_H+\log J_H}{S}
\le\frac nS-6.}
\tag{7.2}
\]

这是一条新的 hard-source dichotomy：

- modulus超过 decimal excess -> pure-power ordinary reconstruction；
- 否则 hard source + coefficient/prefix/third-denominator baselines的**总高度**被 slope excess `n/S-6` 直接控制。

在 safe global upper `n/S<=c_*+o(1)` 下，失败侧至多

\[
\boxed{
\log(X_HT_HN_HJ_H)
\le z_*S+o(S),
\qquad
z_*=0.308883577618\ldots.}
\tag{7.3}
\]

---

## 8. 对 previous sixfold theorems 的 sharpen

raw sixfold coefficient包含 `b_2^6`，因此旧 local stripping remainder有 `-5E` term并需要区分 `r_p>0` / `r_p<=0`。本文先除 denominator prefix common gcd `d_B` 后：

\[
\boxed{
(M+t+6E)\longrightarrow(M+t),}
\]

从而

\[
\boxed{
h+t+n_0+j-5E
\longrightarrow
h+t+n_0+j>0.}
\]

所以：

1. previous raw master仍正确；
2. previous baseline-stripped full-height theorem仍正确；
3. 但对 corrected hard-source analysis，本文 primitive formulation严格更强，且覆盖整个 hard sheet，不再只覆盖 full-height dangerous endpoint。

后续 post-tail LP 应优先使用 `(Primitive-failure-charge)`。

---

## 9. 边界

本文仍未证明 hard sheet为空。

`(Primitive-hard-lock)` 本身只是 deterministic reconstruction；一个 specific residue完全可能恰好是 `10^e`。而 `(Primitive-failure-charge)` 要转成 global slope improvement，还需要与 corrected second-Schmidt bootstrap、`X_N/X_3` readers及 `F_-` lower做统一优化。

但它解决了 corrected hard-source ledger长期缺失的一件事：**每个 hard source prime现在都有一个来自 full exact lift、与 local gap/tail-root valuation不同 parent 的 coefficient-unit global decimal reader。**

---

## 10. 状态摘要

- **已严格完成：** primitive prefix `C_Q=u_1 10^{m_2}+u_2`；
- **已严格完成：** primitive sixfold folding；
- **已严格完成：** hard prime coefficient/right-side common baseline恰为 `M+t`；
- **已严格完成：** residual depth `r_p^{prim}=h+t+n_0+j>0`；
- **已严格完成：** global modulus `mathfrak C_6=X_HT_HN_HJ_H`；
- **已严格完成：** ordinary-lock / failure-charge dichotomy；
- **下一步：** 把 `log(X_HT_HN_HJ_H)<=n-6S` failure branch代回 corrected post-tail LP；ordinary-lock branch继续寻找第二 pure-power reader / order obstruction。
- **不宣称：** explicit global strict gap 或 DD emptiness。
