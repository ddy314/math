# DD corrected Euclidean-failure denominator-gcd bootstrap

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-euclidean-failure-soft-norm-bootstrap-2026-09-06.md`](dd-corrected-euclidean-failure-soft-norm-bootstrap-2026-09-06.md)、[`dd-global-euclidean-block-folding-hard-source-lock-2026-09-06.md`](dd-global-euclidean-block-folding-hard-source-lock-2026-09-06.md)、[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected post-tail odd non-decimal source；Euclidean ordinary-lock failure branch）。**
>
> 前一 bootstrap把 failure residual压到 `h=0` support 的 soft prefix-norm layer `X_N^{soft}`。本文进一步利用**universal** Euclidean gcd-stripped source modulus，而不只使用其 hard-support restriction。逐 prime比较表明：soft prefix-norm depth若没有进入 Euclidean modulus，只可能来自 prefix denominator common depth
>
> \[
> E=v_p((b_1,b_2)).
> \]
>
> 因此所有 hard source + all but a denominator-common part of soft prefix norm可以同时放进同一个 Euclidean modulus；failure branch最终只剩
>
> \[
> \boxed{d_B:=(b_1,b_2)}
> \]
>
> 这一 denominator gcd。

---

## 1. universal Euclidean source modulus local depth

primitive prefix为

\[
C_Q=Q/d_B=u_1 10^{m_2}+u_2,
\qquad d_B=(b_1,b_2).
\]

Euclidean folding coefficient为

\[
C_E=q_{\rm lcm}A_{12}(-u_2)^{k_E},
\qquad
k_E=\lfloor n/m_2\rfloor.
\]

对任意 odd non-decimal `p|C_Q`，`u_2` 是 p-unit。写

\[
E=v_p(b_1)=v_p(b_2),
\quad j=v_p(b_3),
\quad M=\max(E,j),
\quad t=v_p(A_{12}),
\quad c=v_p(C_Q).
\]

则

\[
\boxed{v_p(C_E)=M+t.}
\]

所以 gcd-stripped Euclidean modulus `Q_E=C_Q/(C_Q,C_E)` 在 p 处 exponent为

\[
\boxed{r_E:=(c-M-t)_+.}
\tag{1.1}
\]

这是 universal statement，不要求 `h>0`。

---

## 2. soft prefix-norm support自动饱和 bottom/gap layers

corrected split定义

\[
e_B=\min(x,t),
\]

\[
e_a=\min(x-e_B,\alpha),
\]

\[
e_N=\min(x-e_B-e_a,n_0).
\]

若

\[
e_N>0,
\]

则进入 `e_N` 前的两个 remainders都严格为正，因此前两个 `min` 必须取满：

\[
\boxed{e_B=t,\qquad e_a=\alpha.}
\tag{2.1}
\]

若当前 prime是 soft support，即

\[
\boxed{h=0,}
\]

则 corrected local split还给

\[
\boxed{x=t+\alpha+e_N+e_3.}
\tag{2.2}
\]

其中

\[
e_3\le r=(j-E)_+.
\]

source excess identity为

\[
\boxed{x=c-j-\min(E,j)>0,}
\tag{2.3}
\]

所以

\[
\boxed{c=x+j+\min(E,j).}
\tag{2.4}
\]

---

## 3. case `j>E`: all soft norm depth enters Euclidean modulus

若

\[
j>E,
\]

则

\[
M=j,
\qquad
\min(E,j)=E.
\]

由 `(2.4)`：

\[
c=x+j+E.
\]

故

\[
\begin{aligned}
c-M-t
&=x+E-t\\
&=\alpha+e_N+e_3+E
\end{aligned}
\]

using `(2.2)`。右端非负，所以无需 positive part：

\[
\boxed{r_E=\alpha+e_N+e_3+E\ge e_N.}
\tag{3.1}
\]

因此该 sheet 的全部 soft prefix-norm exponent已包含在 `Q_E` 中。

---

## 4. case `E>=j`: only denominator-common depth can escape

若

\[
E\ge j,
\]

则

\[
M=E,
\qquad
\min(E,j)=j,
\qquad
r=(j-E)_+=0.
\]

故

\[
\boxed{e_3=0.}
\tag{4.1}
\]

由 `(2.4)`：

\[
c=x+2j.
\]

所以

\[
\begin{aligned}
r_E
&=(c-M-t)_+\\
&=(x+2j-E-t)_+\\
&=(\alpha+e_N+2j-E)_+.
\end{aligned}
\tag{4.2}
\]

定义未被 Euclidean modulus覆盖的 soft norm exponent

\[
\boxed{e_{N,D}:=e_N-\min(e_N,r_E).}
\tag{4.3}
\]

若括号 `(4.2)` 非负，则

\[
e_{N,D}
\le(E-2j-\alpha)_+.
\]

若括号为负，则

\[
\alpha+e_N+2j<E
\]

直接给

\[
e_N<E-2j-\alpha.
\]

两种情况统一为

\[
\boxed{
e_{N,D}
\le(E-2j-\alpha)_+
\le E.}
\tag{4.4}
\]

因此 soft norm 中任何未被 Euclidean modulus读取的 exponent都由 prefix denominator common depth `E` 支付。

---

## 5. global soft escape divides `d_B`

对所有 soft `e_N>0` primes定义

\[
e_{N,E}:=e_N-e_{N,D}=\min(e_N,r_E).
\]

令

\[
X_{N,E}^{soft}:=\prod p^{e_{N,E}},
\qquad
X_{N,D}:=\prod p^{e_{N,D}}.
\]

则

\[
\boxed{X_N^{soft}=X_{N,E}^{soft}X_{N,D}.}
\tag{5.1}
\]

由 `(3.1),(4.4)`：

\[
\boxed{X_{N,E}^{soft}\mid Q_E,}
\tag{5.2}
\]

以及

\[
\boxed{X_{N,D}\mid\operatorname{core}_{10}(d_B).}
\tag{5.3}
\]

这里 factors可在同一 prime上分 exponent layer，不要求互素。

---

## 6. combine hard and soft Euclidean-covered layers

在 hard support `h>0` 上，前一 theorem已经证明

\[
r_E=h+t+n_0+j.
\]

特别地

\[
\boxed{h+n_0\le r_E.}
\tag{6.1}
\]

令

\[
Y_E
:=
\left(\prod_{p\mid X_H}p^{h+n_0}\right)
X_{N,E}^{soft}.
\tag{6.2}
\]

hard 与 soft support互斥，所以 `(6.1),(5.2)`逐 prime给

\[
\boxed{Y_E\mid Q_E.}
\tag{6.3}
\]

而 `X_N` 在 hard support的 exponent恰为 `n_0`，因此 exact global factorization为

\[
\boxed{
X_NX_H=Y_EX_{N,D}.}
\tag{6.4}
\]

---

## 7. Euclidean failure leaves only denominator gcd

universal Euclidean ordinary lock若失败，则

\[
\boxed{Q_E\le10^{r_n},}
\qquad
0\le r_n<m_2.
\tag{7.1}
\]

由 `(6.3)`：

\[
Y_E\le Q_E\le10^{r_n}.
\]

由 `(5.3),(6.4)`：

\[
\boxed{
X_NX_H
\le10^{r_n}\operatorname{core}_{10}(d_B).}
\tag{7.2}
\]

前一 corrected third-gap bootstrap为

\[
3\log F_-+\log(X_NX_H)
\ge3S-o(S).
\]

代入 `(7.2)`：

\[
\boxed{
3\log F_-+\log\operatorname{core}_{10}(d_B)
\ge3S-r_n-o(S).}
\tag{Denominator-gcd-bootstrap}
\]

因为删除 2/5 part只会减小 gcd，若愿意使用 raw `d_B` 可写 weaker but simpler form

\[
\boxed{
3\log F_-+\log d_B
\ge3S-r_n-o(S).}
\tag{Denominator-gcd-bootstrap-raw}
\]

---

## 8. digit-only consequence

由于

\[
d_B=(b_1,b_2)<10^{\min(m_1,m_2)},
\]

且

\[
r_n<m_2,
\]

有

\[
r_n+\log d_B
<m_2+\min(m_1,m_2)+O(1)
\le S+O(1).
\]

所以 failure branch至少满足

\[
\boxed{
3\log F_-\ge2S-o(S).}
\tag{Failure-Fminus-basic}
\]

这条 basic lower主要是 bookkeeping sanity；真正后续应使用 stronger `(Denominator-gcd-bootstrap)` 与 denominator-overlap / multiplicative `F_-` lower联合，而不是先粗化到 `2S/3`。

---

## 9. dependency audit

本文只使用：

1. corrected split的定义与 safe source-excess identity；
2. universal Euclidean gcd-stripped folding；
3. hard sheet中已严格证明的 exact ledger；
4. previous corrected third-gap combined bootstrap。

不使用 old general-transfer max-payer、不使用 discriminant root、也不使用旧 two-sheet/angular collapse 的 invalid dependent portion。

---

## 10. 状态摘要

- **已严格完成：** universal Euclidean local depth `r_E=(c-M-t)_+`；
- **已严格完成：** soft norm support自动饱和 bottom/gap；
- **已严格完成：** `j>E` 时 `e_N<=r_E`；
- **已严格完成：** `E>=j` 时 escape `e_{N,D}<=E`；
- **已严格完成：** global escape `X_{N,D}|core_10(d_B)`；
- **已严格完成：** hard+soft covered layers combine into one `Y_E|Q_E`；
- **主结论：** Euclidean failure branch `3 log F_- + log core_10(d_B) >= 3S-r_n-o(S)`；
- **剩余 corrected post-tail failure residual：** only prefix denominator common gcd `d_B`；
- **未证明：** ordinary-lock branch impossible、denominator-gcd branch closes globally、DD strict gap/emptiness。
