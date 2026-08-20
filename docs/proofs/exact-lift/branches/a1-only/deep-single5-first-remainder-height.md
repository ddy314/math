# A1 minimal diagonal: strict single-5-deep first-remainder height bound

> 日期：2026-08-20。依赖 `deep-first-complement-remainder.md`、`deep-gap-valuation-normal-form.md` 与 cross-corridor theorem。当前剩余 fixed frontier 从 `k>=32` 开始；本文结论实际只需远小于此的 k。

本文处理 single-5-deep：

\[
A=0,
\qquad B>0,
\]

并首先关闭其“过深”方向。在 strict 5-low 子区得到线性斜率上界

\[
\boxed{B+v_5(N_0)<2.3k+8.}
\]

状态：**strict 5-low 高度压缩已严格完成；single-5 尚未整体关闭。**

---

## 1. single-5 的 non-deep 2-side

因为 `A=0`，2-side 留在 numerator 的指数为

\[
\lambda_2=k+x\ge0,
\qquad
\lambda=2^{\lambda_2}.
\]

若当前位于 strict 5-low：

\[
B>n_5:=v_5(N),
\]

则

\[
y=-k-B<y_*=-k-n_5.
\]

cross-corridor 已证明：`y<y_*` 时不能同时有 `x>k`。所以

\[
\boxed{x\le k.}
\]

因此

\[
\boxed{0\le\lambda_2\le2k.}
\tag{1}

这一步把 non-deep 2-side 的 numerator compensation 限制在最多 `2k` 层。

---

## 2. first remainder

沿用 universal complement first remainder：

\[
MDN_0=1000\lambda T^3+R_1,
\]

\[
\boxed{0<R_1<390100\lambda T,}
\tag{2}

其中

\[
D=5^B,
\qquad v_5(M)=0.
\]

记

\[
\nu:=v_5(N_0),
\qquad Y:=B+\nu.
\]

左侧的 5-adic valuation 为

\[
\boxed{v_5(MDN_0)=Y.}
\tag{3}

主项因为 `lambda` 只含 2：

\[
\boxed{v_5(1000\lambda T^3)=3k+3.}
\tag{4}

---

## 3. `Y>=3k+3` 不可能

若

\[
Y>3k+3,
\]

则两项赋值不同，故

\[
v_5(R_1)=3k+3.
\]

若

\[
Y=3k+3,
\]

则 cancellation 只会让 `R_1` 更深，因此仍有

\[
5^{3k+3}\mid R_1.
\]

结合 (1)-(2)：

\[
5^{3k+3}
<R_1
<390100\,2^{2k}10^k
=390100\,2^{3k}5^k.
\]

于是必须有

\[
125\left(\frac{25}{8}\right)^k<390100.
\]

当前 `k>=32` 时左侧远大于右侧，矛盾。

所以

\[
\boxed{Y<3k+3.}
\tag{5}

---

## 4. strict slope bound

由 (5)，(3) 与 (4) 赋值严格不同，所以现在

\[
\boxed{v_5(R_1)=Y.}
\tag{6}

因此

\[
5^Y\le R_1
<390100\,2^{2k}10^k
=390100\,2^{3k}5^k.
\]

使用安全数值

\[
390100<5^8,
\qquad
2^3=8<5^{1.3},
\]

得到

\[
5^Y<5^{8+1.3k+k}.
\]

所以

\[
\boxed{
B+v_5(N_0)=Y<2.3k+8.}
\tag{7}

这是 strict single-5-deep 的统一 first-remainder height bound。

---

## 5. 与 resonance parity 联立

strict 5-low 原本还有

\[
B>n_5,
\qquad
B\equiv n_5\pmod2.
\]

现在再加 (7)。因此 single-5 的 strict-low lattice 从无界 half-plane 压成

\[
\boxed{
\begin{aligned}
&B>n_5,\\
&B\equiv n_5\pmod2,\\
&B+v_5(N_0)<2.3k+8,\\
&0\le\lambda_2\le2k.
\end{aligned}}
\]

并仍受 mod-5 unit Legendre lock。

---

## 6. 当前边界

本文没有处理：

- 5-adic resonance `B=n_5`；
- high-side `0<B<n_5`。

这些层需要与 prefix `v_5(N)` 的 Hensel branches 联用。

但 strict single-5 的“任意深 B”已经消失；其最大斜率严格低于 `2.3k`，后续可以再与 prefix 5-adic root lifting / contact sign 合并。
