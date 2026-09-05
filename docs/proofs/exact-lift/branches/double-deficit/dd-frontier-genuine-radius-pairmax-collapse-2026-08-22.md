# DD frontier: genuine-Gaussian radius carrier 与 pair-max 的 exact collapse

> 日期：2026-08-22
>
> 作用域：假想 `6.308883577618...` frontier 的 one-channel moving core。本文不要求进入 rational sign degeneration；因此特别覆盖 `C_G` genuine-Gaussian main primes。
>
> 结论是一条 **same-prime no-go**：radius repeat 产生的 numerator-shell Gaussian carrier与原始 pair-max Gaussian carrier并非两个独立方向，它们由 terminal denominator ratio精确对齐。

## 1. terminal denominator identities

terminal denominator concat 已写成

\[
Q=J\bigl(s\widetilde w10^{m_2}+C_0\widetilde r\bigr),
\]

所以

\[
\boxed{b_2=JC_0\widetilde r.}
\tag{1.1}
\]

另一方面

\[
b_3=BJC_0q_c\theta s.
\]

令

\[
A=s\theta q_c,
\qquad
b=5^T\widetilde r,
\]

则

\[
\boxed{b_3=ABJC_0.}
\tag{1.2}
\]

因此

\[
\boxed{
\frac{b_3}{b_2}=\frac{AB}{\widetilde r}.}
\tag{Den-ratio}
\]

同时

\[
\boxed{10^m=2\cdot5^TB.}
\tag{1.3}
\]

## 2. derivative orientation 给出的 uniform radius digital carrier

已有

\[
D_{\rm der}
=2\widetilde rL_{\rm clean}q_c-iP_0,
\qquad
P_0=g_0a_2B\theta s.
\]

固定 main

\[
p^h\Vert C_L,
\qquad p=\pi\bar\pi,
\qquad \pi^h\mid D_{\rm der},
\]

并删去 coefficient exceptional core。

clean source

\[
VA_0-5^TR_0=q_c^2L_{\rm clean}
\]

在 `p^h|V` 上给

\[
q_c^2L_{\rm clean}
\equiv-5^TR_0
\pmod{p^h}.
\]

因此

\[
q_cD_{\rm der}
\equiv
-2bR_0-i g_0a_2BA
\pmod{\pi^h}.
\tag{2.1}
\]

若同一 prime 有 radius repeat

\[
p^r\mid A_0,
\qquad 0<r\le h,
\]

numerator reconstruction

\[
UA_0+R_0=g_0B10^dA_{12}
\]

给

\[
R_0\equiv g_0B10^dA_{12}\pmod{p^r}.
\]

代回 `(2.1)`，约去 main units，得到不需要 rational sign 的统一 carrier

\[
\boxed{
\pi^r\mid
2b10^dA_{12}+i a_2A.
}
\tag{Genuine-radius-digital}
\]

当 `A congruent +/- b` 时，这正好 specialization 为旧 full-rational `Radius-G±`。

## 3. radius repeat 同时给 pair-max numerator-shell carrier

one-channel main prime在 `(b_2,b_3)` 上 pair-max。令整数球面 lcm denominator 为 `q_lcm`，并写

\[
\beta_2=\frac{q_{\rm lcm}}{b_2},
\qquad
\beta_3=\frac{q_{\rm lcm}}{b_3}.
\]

在 main prime上两者都是 `p`-units，而且

\[
\boxed{
\frac{\beta_2}{\beta_3}
=\frac{b_3}{b_2}.}
\tag{3.1}
\]

chosen pair-max orientation满足

\[
\pi^{2h}\mid y_2+i y_3
=a_2\beta_2+i a_3\beta_3.
\]

另一方面 `Radius=Concat` 给

\[
p^r\mid\alpha,
\qquad
\alpha=A_{12}10^{m+d}+a_3,
\]

所以

\[
a_3\equiv-A_{12}10^{m+d}\pmod{p^r}.
\]

因 `r<=h`，可代入 chosen Gaussian orientation：

\[
\boxed{
\pi^r\mid
 a_2\beta_2
-iA_{12}10^{m+d}\beta_3.
}
\tag{Pairmax-radius-digital}
\]

## 4. 两个 Gaussian digit directions 的 determinant 恒等为零

记

\[
G_R:=2b10^dA_{12}+i a_2A,
\]

\[
G_P:=a_2\beta_2-iA_{12}10^{m+d}\beta_3.
\]

若把它们视为关于 `A_12,a_2` 的两条 Gaussian linear forms，则消去 `a_2` 的标准组合为

\[
A G_P+i\beta_2G_R.
\]

直接展开：

\[
\begin{aligned}
A G_P+i\beta_2G_R
&=i10^dA_{12}
\left(
2b\beta_2-A10^m\beta_3
\right).
\end{aligned}
\tag{4.1}
\]

现在使用 `(3.1)`、`(Den-ratio)`：

\[
\begin{aligned}
2b\beta_2-A10^m\beta_3
&=A\beta_3
\left(
\frac{2bB}{\widetilde r}-10^m
\right).
\end{aligned}
\]

而

\[
\frac{2bB}{\widetilde r}
=2\cdot5^TB
=10^m.
\]

所以得到 exact identity

\[
\boxed{
2b\beta_2-A10^m\beta_3=0,
}
\tag{Pairmax-digit-alignment}
\]

以及

\[
\boxed{A G_P+i\beta_2G_R=0.}
\tag{Genuine-radius-collapse}
\]

这不是模 `p^r` 的 coincidence，而是 terminal denominator algebra 的普通整数/有理恒等式。

## 5. 解释

因此 genuine-Gaussian main prime上的 radius repeat同时进入

1. derivative-normalized digital carrier `(Genuine-radius-digital)`；
2. original pair-max + concat digit carrier `(Pairmax-radius-digital)`；

但二者线性相关，比例恰由 `b_3/b_2=AB/rtilde` 与 `10^m=2*5^T B` 固定。

所以不能从这两个 carriers构造新的 resultant 去强迫

\[
p^r\mid A^2-b^2
\]

或把 genuine mass送回 rational sign channels。正确结论是更强的 no-go：resultant **恒等为零**。

## 6. frontier 更新

结合 `dd-frontier-good-digit-shell-local-closure-2026-08-22.md`：

\[
\boxed{
\text{full-rational 与 genuine 两侧的 radius same-prime digit algebra均已闭包。}
}
\]

因此继续寻找

- derivative × pair-max；
- radius × pair-max；
- radius × second-order `A12` CRT；
- 同 prime 的第三 Gaussian Hensel/resultant；

不会产生 strict positive-linear surplus。

真正剩余问题必须保留多个 prime 的全局 split orientation / decimal location信息，尤其是

\[
V=2^HZ-5^TU=C_Lv_0,
\qquad
Ua_3\bmod10^d
=10^d-R_{\rm dec},
\]

以及 unique `(QCRT)+(GCRT)` lift 的 Archimedean digit window。
