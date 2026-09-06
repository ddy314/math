# DD corrected Euclidean-failure soft-norm bootstrap

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)、[`dd-global-euclidean-block-folding-hard-source-lock-2026-09-06.md`](dd-global-euclidean-block-folding-hard-source-lock-2026-09-06.md)、[`tail-rough-z0-angular-only-collapse.md`](tail-rough-z0-angular-only-collapse.md) §1 的 `Third-reader-charge`。
>
> **严格状态：已严格完成（corrected post-tail odd rough source；Euclidean ordinary-lock failure branch）。**
>
> 旧 `tail-rough-z0-angular-only-collapse` 的后续 two-sheet/gaussian 部分依赖后来被撤销的 old general-transfer max-payer inequality，不能整体直接移植到 corrected proof tree。但它的 §1 `a R Q<F_-` 只使用 exact small-factor normalization、tail window与 `R|tau`，不依赖失效的 discriminant-root transfer，因此仍是安全 input。
>
> 把这条 exact third-gap charge与 corrected split、Euclidean hard-source reader联立后，failure branch 的 second-Schmidt residual从
>
> \[
> X_NX_3X_H
> \]
>
> 压成仅剩 **non-hard / soft support 的 prefix-norm layer** `X_N^{soft}`。

---

## 1. corrected source split

corrected hard-source theorem给

\[
\boxed{X_Q=X_BX_aX_NX_3X_H.}
\tag{1.1}
\]

并有 exact readers

\[
X_B\mid C_{12}:=(A_{12},Q),
\qquad
X_a\mid a,
\]

\[
X_N\mid\operatorname{core}_{10}(N_0),
\qquad
X_3\mid\operatorname{core}_{10}(R_3^{\rm den}),
\]

以及 hard residual `X_H`。

second fixed-target Schmidt 的 corrected form为

\[
\boxed{
\log F_-
\ge
S-\log X_Q-o(S).}
\tag{1.2}
\]

---

## 2. bottom charge

已有 exact bottom small-factor charge对任意 `X_B|C_{12}` 给

\[
\boxed{X_BG<F_-.}
\tag{2.1}
\]

且 first denominator product满足

\[
10^{S-2}\le G<10^S.
\]

所以

\[
\boxed{
\log X_B\le\log F_--S+O(1).}
\tag{2.2}
\]

---

## 3. corrected third-gap combined charge

令

\[
R:=\operatorname{core}_{10}(R_3^{\rm den}).
\]

`tail-rough-z0-angular-only-collapse.md` §1 的证明只使用

\[
F_-=a\,g_*\,L\frac{LQ+2\tau}{\tau},
\qquad R\mid\tau,
\qquad \tau<L,
\]

从而严格得到

\[
\boxed{aRQ<F_-.}
\tag{Third-reader-charge}
\]

该 proof不使用旧 `x<=max(t,N_0,R_3)` general-transfer input。

corrected split给

\[
X_a\mid a,
\qquad
X_3\mid R.
\]

因此 prime overlap也无需分 support：作为正整数直接有

\[
X_aX_3\mid aR.
\]

故

\[
\boxed{X_aX_3Q<F_-.}
\tag{Corrected-third-gap-charge}
\]

又

\[
10^{S-1}\le Q<10^S,
\]
所以

\[
\boxed{
\log(X_aX_3)
\le\log F_--S+O(1).}
\tag{3.1}
\]

这严格优于 corrected split中只单独使用 `X_aQ<F_-` 的 bookkeeping；third-denominator layer `X_3` 被同一 exact gap/third reader一起支付。

---

## 4. sharpen corrected bootstrap

将 `(1.1)` 展开进 `(1.2)`：

\[
\log F_-
\ge
S-\log X_B-\log(X_aX_3)-\log X_N-\log X_H-o(S).
\]

使用 `(2.2)` 与 `(3.1)`：

\[
\log F_-
\ge
S-2(\log F_--S)-\log X_N-\log X_H-o(S).
\]

于是

\[
\boxed{
3\log F_-+\log(X_NX_H)
\ge3S-o(S).}
\tag{Corrected-soft-bootstrap-pre}
\]

相较 2026-08-22 的

\[
3\log F_-+\log(X_NX_3X_H)\ge3S-o(S),
\]

`X_3` 已从 independent residual 中消失。

---

## 5. hard-support part of `X_N`

在 hard prime `h>0` 上，corrected split的四个 `min` 在到达 hard residual之前全部取满，因此

\[
\boxed{e_N=n_0.}
\tag{5.1}
\]

定义

\[
\boxed{N_H:=\prod_{p\mid X_H}p^{n_0(p)}.}
\tag{5.2}
\]

则 exact 地

\[
\boxed{N_H\mid X_N.}
\tag{5.3}
\]

令

\[
\boxed{X_N^{\rm soft}:=X_N/N_H.}
\tag{5.4}
\]

因为 `N_H` 只取 hard support，`X_N^{soft}` 正是 prefix-norm payer在 `h=0` support上的剩余 exponent layer。

---

## 6. Euclidean failure absorbs all hard source + hard norm depth

Euclidean hard-source theorem构造

\[
\boxed{
\mathfrak C_E=X_HT_HN_HJ_H.}
\tag{6.1}
\]

在 ordinary-lock failure branch有

\[
\boxed{
\log\mathfrak C_E\le r_n,}
\qquad
r_n=n-\left\lfloor\frac n{m_2}\right\rfloor m_2,
\qquad0\le r_n<m_2.
\tag{6.2}
\]

所有 factors为正整数，所以特别地

\[
\boxed{
X_HN_H\le\mathfrak C_E\le10^{r_n}.}
\tag{6.3}
\]

由 `X_N=N_HX_N^{soft}`：

\[
\boxed{
X_NX_H
\le10^{r_n}X_N^{\rm soft}.}
\tag{6.4}

---

## 7. failure branch只剩 soft prefix norm

把 `(6.4)` 代入 `(Corrected-soft-bootstrap-pre)`。若

\[
3\log F_-+\log(X_NX_H)\ge3S-o(S)
\]

且

\[
\log(X_NX_H)\le r_n+\log X_N^{\rm soft},
\]

则必有

\[
\boxed{
3\log F_-+\log X_N^{\rm soft}
\ge3S-r_n-o(S).}
\tag{Soft-norm-bootstrap}
\]

由 `r_n<m_2` 还得到 weaker but digit-only form

\[
\boxed{
3\log F_-+\log X_N^{\rm soft}
>3S-m_2-o(S).}
\tag{Soft-norm-bootstrap-digit}
\]

因此 corrected Euclidean failure branch的唯一 residual height已经缩成：

\[
\boxed{X_N^{\rm soft}\mid\operatorname{core}_{10}(N_0),
\qquad\operatorname{supp}(X_N^{\rm soft})\subseteq\{h=0\}.}
\]

---

## 8. dependency audit

本文**不使用** old two-sheet theorem的

\[
x\le\max(t,N_0,R_3^{\rm den}),
\]

也不使用 discriminant/gap-root identification。

从旧 `angular-only` 文件只复用 §1 的 exact `aRQ<F_-`，其证明在该文件内独立完成并只依赖 exact small-factor normalization。后续 `Sheet T/N`、`X_{Z,A}` 等依赖 old general-transfer 的部分一律不作为本文输入。

---

## 9. 下一目标

post-tail failure branch现在不再需要同时控制 `X_N/X_3/X_H`。只需处理

\[
\boxed{X_N^{\rm soft}}
\]

这一层。

可行方向：

1. 在 `h=0` support上把 `N_0=g_n^2N_{ang}` 分成 common numerator scale与 primitive Gaussian angle；
2. 用 exact denominator-prefix norm resultant连接 `N_{ang}` 与 pure numerator norm；
3. 对 common numerator part使用 bottom/cyclotomic digit relation；
4. ordinary Euclidean-lock branch另行寻找 second decimal parent。

---

## 10. 状态摘要

- **已严格完成：** corrected `X_aX_3Q<F_-` combined charge；
- **已严格完成：** bootstrap sharpen `3 log F_- + log(X_NX_H) >= 3S-o(S)`；
- **已严格完成：** hard-support `N_H|X_N`；
- **已严格完成：** Euclidean failure吸收 `X_HN_H`；
- **主结论：** failure branch `3 log F_- + log X_N^{soft} >= 3S-r_n-o(S)`；
- **剩余 post-tail failure residual：** only soft prefix norm `X_N^{soft}`；
- **不宣称：** ordinary-lock branch排除、global strict slope gap、DD emptiness。
