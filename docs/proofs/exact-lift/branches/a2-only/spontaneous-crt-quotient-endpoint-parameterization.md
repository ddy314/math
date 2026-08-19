# A2 additive CRT quotient 的 endpoint-lattice parameterization

> **依赖：** `spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md`。
>
> **严格状态：**前一层把 `Q_Delta` 的全部无界尺度隔离为 `a_Delta=(c_u^2 5^lambda/g)K^2`。本文用真实第二/第三 denominator normal forms消去 `c_u/g`，把该尺度完全恢复成 endpoint-lattice 参数 `(M,m,lambda,d,c_Q)` 与窄 normalized variables `(x,s,w)`。其连续 coefficient严格落在 `(139,150)`，所以 `Q_Delta` 获得固定 normalized window。对固定 `(eta,d,c_Q)`，绝对 `Q_Delta` 仍指数增长，因此“证明 Q_Delta=O(1)”路线严格降级；正确后续接口是比较 normalized quotient 与 Gaussian/source Hensel 的离散 slot。本文不建立该最终比较，因此不关闭 A2。

---

## 1. normalized decimal variables

记

\[
x:=\frac{B}{N},
\qquad
s:=\frac{K}{N},
\qquad
w:=\frac{b_3}{T},
\qquad
N=10^M.
\]

当前 dangerous endpoint box给

\[
\boxed{
\frac1{10}<x<\frac2{19},
\qquad
\frac{2499}{250}<s<10,
\qquad
\frac{837}{1000}<w<\frac{843}{1000}.}
\tag{1.1}
\]

前一文件定义

\[
\boxed{
\mathfrak a_\Delta
:=\frac{c_u^25^\lambda}{g}K^2.}
\tag{1.2}
\]

并证明

\[
\boxed{
\frac{\mathfrak a_\Delta}{17}-1
<Q_\Delta
<\frac{\mathfrak a_\Delta}{14}.}
\tag{1.3}
\]

---

## 2. recover `c_u` from the third denominator

第三块 denominator normal form为

\[
\boxed{
b_3=2^{M+m+1}5^dc_Qc_u.}
\tag{2.1}
\]

又

\[
b_3=wT,
\qquad
T=2^m5^m,
\qquad
m=d+\lambda.
\]

所以

\[
w2^m5^m
=2^{M+m+1}5^dc_Qc_u.
\]

约去 `2^m5^d`：

\[
\boxed{
c_u
=\frac{w5^\lambda}{2^{M+1}c_Q}.}
\tag{2.2}
\]

---

## 3. recover `g` from the second denominator

第二块 denominator normal form为

\[
\boxed{B=2^{M+m+1}c_ug.}
\tag{3.1}
\]

另一方面

\[
B=xN=x2^M5^M.
\]

代入 (2.2)：

\[
\begin{aligned}
g
&=\frac{x2^M5^M}
{2^{M+m+1}c_u}\\
&=\frac{x2^M5^M c_Q}
{2^m w5^\lambda}.
\end{aligned}
\]

因此

\[
\boxed{
g
=\frac{x c_Q}{w}
2^{M-m}5^{M-\lambda}.}
\tag{3.2}
\]

所以 `c_u/g` 不再是一个额外 allocation parameter；它由真实 endpoint variables完全恢复。

---

## 4. exact endpoint formula for `a_Delta`

将 (2.2),(3.2) 代入 (1.2)，并使用

\[
K=sN=s2^M5^M.
\]

直接整理 `2,5` exponents：

\[
\boxed{
\mathfrak a_\Delta
=
\frac{s^2w^3}{4xc_Q^3}
2^{m-M}5^{4\lambda+M}.}
\tag{4.1}
\]

现在令 endpoint-lattice 的离散参数

\[
\boxed{\eta:=2m-M.}
\tag{4.2}
\]

因为

\[
m=\frac{M+\eta}{2},
\qquad
\lambda=m-d,
\]
所以

\[
m-M=\frac{\eta-M}{2},
\]

\[
4\lambda+M
=3M+2\eta-4d.
\]

故 (4.1) 等价为

\[
\boxed{
\mathfrak a_\Delta
=
\frac{s^2w^3}{4xc_Q^3}
2^{(\eta-M)/2}
5^{3M+2\eta-4d}.}
\tag{4.3}
\]

这已经把 CRT quotient主尺度完全接回原 Gaussian allocation lattice。

---

## 5. the continuous coefficient lies in `(139,150)`

定义

\[
\boxed{
\kappa_\Delta:=\frac{s^2w^3}{4x}.}
\tag{5.1}
\]

由 (1.1)，下界取 `s,w` 的下端与 `x` 的上端：

\[
\kappa_\Delta
>
\frac{(2499/250)^2(837/1000)^3}
{4(2/19)}
>139.
\tag{5.2}
\]

上界取 `s,w` 的上端与 `x` 的下端：

\[
\kappa_\Delta
<
\frac{10^2(843/1000)^3}
{4(1/10)}
<150.
\tag{5.3}
\]

所以

\[
\boxed{139<\kappa_\Delta<150.}
\tag{5.4}
\]

定义纯离散 scale

\[
\boxed{
\mathcal R_{\eta,d,M}
:=2^{(\eta-M)/2}5^{3M+2\eta-4d}
=2^{m-M}5^{4\lambda+M}.}
\tag{5.5}
\]

于是

\[
\boxed{
\frac{139}{c_Q^3}\mathcal R_{\eta,d,M}
<\mathfrak a_\Delta
<\frac{150}{c_Q^3}\mathcal R_{\eta,d,M}.}
\tag{5.6}
\]

---

## 6. fixed normalized window for `Q_Delta`

把 (5.6) 代入前层 (1.3)：

\[
Q_\Delta
>
\frac{139}{17c_Q^3}\mathcal R_{\eta,d,M}-1
>
\frac8{c_Q^3}\mathcal R_{\eta,d,M}-1,
\]

以及

\[
Q_\Delta
<
\frac{150}{14c_Q^3}\mathcal R_{\eta,d,M}
<
\frac{11}{c_Q^3}\mathcal R_{\eta,d,M}.
\]

所以

\[
\boxed{
\frac8{c_Q^3}\mathcal R_{\eta,d,M}-1
<Q_\Delta
<\frac{11}{c_Q^3}\mathcal R_{\eta,d,M}.}
\tag{6.1}
\]

换言之，normalized CRT quotient

\[
\boxed{
\mathcal Q_\Delta^{\rm norm}
:=
\frac{c_Q^3Q_\Delta}
{2^{m-M}5^{4\lambda+M}}
}
\tag{6.2}
\]

被困在一个固定常数带；忽略 floor 的 `-1` correction后，它始终在 `(8,11)` 内。

严格地由 (6.1)：

\[
8-\frac{c_Q^3}{\mathcal R_{\eta,d,M}}
<\mathcal Q_\Delta^{\rm norm}
<11.
\tag{6.3}
\]

---

## 7. constant-quotient strategy is impossible

固定任意允许的

\[
(\eta,d,c_Q).
\]

则

\[
\mathcal R_{\eta,d,M}
=2^{\eta/2}5^{2\eta-4d}
\left(\frac{125}{\sqrt2}\right)^M.
\tag{7.1}
\]

在 parity-compatible `M` subsequence上这是严格指数增长。由 (6.1)：

\[
\boxed{Q_\Delta\to\infty}
\]

随 `M` 增长。

因此后续不应再尝试证明

\[
Q_\Delta=O(1)
\]
或把它直接压成固定有限整数表；那与 exact endpoint scale不相容。

真正可比较的对象是 normalized quotient (6.2)。

---

## 8. revised global interface

`endpoint-lattice.md` 中 Gaussian allocation也按

\[
(\eta,d,c_Q,k_h,\text{slot})
\]
组织。

本文说明 additive CRT quotient使用**完全相同的离散参数**，而连续 endpoint dependence只剩

\[
\kappa_\Delta\in(139,150).
\]

所以最自然的下一步不是单独估计 `Q_Delta`，而是把

\[
\boxed{
\mathcal Q_\Delta^{\rm norm}}
\]
与 Gaussian/source-Hensel 一侧已经存在的 normalized slot scalar联立，寻找两个固定窄区间或离散 residue之间的不相容。

A2 仍为 `待证`。
