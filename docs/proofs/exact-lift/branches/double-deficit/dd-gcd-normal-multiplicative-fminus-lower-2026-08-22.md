# DD gcd-normal form 的 universal multiplicative `F_-` lower

> 日期：2026-08-22
>
> 作用域：一般 DD gcd-normal form；不需要 canonical `t_2=1`、resonance、旧 `general-transfer-local` 或 discriminant-root identification。
>
> **严格状态：已严格完成。**

## 1. gcd-normal form

沿用 `core.md` 的 reduced tail normalization：

\[
\gamma=(\kappa,G),
\qquad
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1.
\]

尾关系给

\[
Q<\frac uv\le10Q.
\tag{1.1}
\]

exact identity为

\[
F_-Q(\kappa+G)=E\kappa(\kappa+2G).
\]

约去 `gamma`：

\[
\boxed{
F_-Q(u+v)=E\gamma u(u+2v).
}
\tag{1.2}
\]

由于

\[
(u,u+v)=1,
\qquad
(u+2v,u+v)=(v,u+v)=1,
\]

有

\[
\boxed{(u(u+2v),u+v)=1.}
\]

所以从 `(1.2)`：

\[
\boxed{u(u+2v)\mid F_-Q.}
\tag{1.3}
\]

## 2. 消去 source gcd

令

\[
d_0:=(u,Q),
\qquad
u=d_0r,
\qquad
Q=d_0q,
\qquad
(r,q)=1.
\]

由 `(1.3)`：

\[
d_0r(d_0r+2v)\mid d_0F_-q,
\]

故

\[
\boxed{
r(u+2v)\mid F_-q.}
\tag{2.1}
\]

所有量为正整数，因此

\[
F_-q\ge r(u+2v).
\tag{2.2}
\]

而 `(1.1)` 化为

\[
\boxed{
q<\frac rv\le10q.
}
\tag{2.3}
\]

于是

\[
\frac rq>v.
\]

从 `(2.2)`：

\[
F_-
\ge\frac rq(u+2v)
>v(u+2v).
\]

再由

\[
u=d_0r>d_0qv=Qv,
\]

得到

\[
\boxed{
F_->(Q+2)v^2.
}
\tag{Multiplicative-Fminus}
\]

特别地：

\[
\boxed{F_->Qv^2.}
\tag{2.4}
\]

## 3. 用 `G=gamma v` 改写

因为

\[
v=G/\gamma,
\]

所以

\[
\boxed{
F_->(Q+2)\left(\frac G\gamma\right)^2.
}
\tag{Gamma-form}
\]

这是一个只读取 denominator concat、prefix denominator product 与 common tail gcd 的 universal lower。

## 4. height consequence

前两 denominator blocks给

\[
10^{S-2}\le G<10^S,
\]

而

\[
10^{S-1}\le Q<10^S.
\]

因此 `(Gamma-form)` 给

\[
\boxed{
\log_{10}F_-
>3S-5-2\log_{10}\gamma.
}
\tag{4.1}
\]

若记

\[
\Gamma:=\frac{\log_{10}\gamma}{S},
\]

则渐近地

\[
\frac{\log_{10}F_-}{S}
\ge3-2\Gamma-o(1).
\tag{4.2}
\]

与 d-dominant Archimedean upper

\[
\log_{10}F_-<4S+2m-n+O(1)
\]

联立，得到条件 slope inequality

\[
\boxed{
\frac nS
\le1+2\frac mS+2\Gamma+o(1).
}
\tag{4.3}
\]

## 5. 与已有 small-factor lower 的关系

本文只使用 `(1.2)` 的整除性与 tail window，因此：

- 不依赖 corrected / old 5-adic branch tree；
- 不依赖 `general-transfer-local`；
- 不依赖 Gaussian/projective payer allocation；
- 可以安全反馈到 corrected post-tail hard-source branch。

`(Multiplicative-Fminus)` 未必在 canonical equality ray 上比 corrected S-unit lower更强；它的用途是控制 common gcd `gamma` 较小的 non-canonical / post-tail states，并给 corrected hard-source optimization一个独立 denominator-only lower。

## 6. 状态摘要

- **已严格完成：** `u(u+2v)|F_-Q` 到 `(Multiplicative-Fminus)` 的 exact 整除/大小推导。
- **可用接口：** `(Gamma-form)`、height bound `(4.3)`。
- **未证明：** 该 lower 单独改进 global `6.308883...`；需与 corrected hard-source allocation / Schmidt budget联合优化。
