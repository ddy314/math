# A1 minimal diagonal: single-2 collapse by decimal-height synchronization

> 日期：2026-08-22。
>
> 依赖：`deep-denominator-ledger.md`、`global-squarefree-terminal.md`、`decimal-height-synchronization.md`。
>
> 范围：minimal diagonal，`k=g>=32`，single-2 deep sector
> \[
> D_{\rm gap}=2^A,\qquad A>k,
> \]
> 且 5-side 非 deep。

状态：**已严格完成；single-2 deep 全部为空。**

---

## 1. single-2 的 `(L,M)` 高度

令

\[
T=10^k,
\qquad
\lambda=5^{\lambda_5},
\qquad
\lambda_5=k+y\ge0.
\]

`deep-complement-height.md` 的统一 gap identity 给

\[
2^A T\rho=h5^{\lambda_5},
\qquad (h,10)=1.
\tag{1}
\]

把

\[
\rho=M/L,
\qquad (L,M)=1
\]

约到最低项。因为 `h` 与 `5^{lambda_5}` 都是 2-unit，2-side 不发生约分，所以

\[
\boxed{v_2(L)=A+k.}
\tag{2}
\]

5-side 则至多保留

\[
\boxed{v_5(L)=(k-\lambda_5)_+\le k.}
\tag{3}
\]

由于 single-2 deep 意味着

\[
A>k,
\]

故

\[
\boxed{v_2(L)=A+k>2k.}
\tag{4}
\]

exact decimal-height synchronization 因而要求归一化第三分子根 `x_sigma` 的 5-side reduced denominator 必须把 completion height 抬到同一个值 `A+k`。

---

## 2. `kappa` 的 5-adic depth

令 supply complement

\[
M_c:=QG/h.
\]

由 (1) 与全局定义

\[
\kappa=10^kLQG/M
\]

可写成

\[
\boxed{
\kappa=
\frac{2^A T^2M_c}{5^{\lambda_5}}.
}
\tag{5}
\]

minimal diagonal 中 `Q,G,h` 都是 5-units，所以

\[
\boxed{v_5(M_c)=0.}
\tag{6}
\]

因此 `kappa` 为整数首先强迫

\[
\boxed{0\le\lambda_5\le2k,}
\tag{7}
\]

并且

\[
\boxed{a_5:=v_5(\kappa)=2k-\lambda_5.}
\tag{8}
\]

特别地

\[
\boxed{a_5\le2k.}
\tag{9}
\]

---

## 3. `kappa` square 在 5-adic 上的统一上界

沿用

\[
D_c=10^kQ,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2,
\]

以及 exact square

\[
W^2
=\kappa^2G^2C^2
-\kappa D_c^2N(\kappa+2G).
\tag{10}
\]

minimal diagonal 有

\[
v_5(G)=v_5(C)=v_5(Q)=0,
\qquad
v_5(D_c)=k.
\tag{11}
\]

记

\[
n_5=v_5(N)\ge0.
\]

若 `a_5>0`，则

\[
v_5(\kappa+G)=v_5(\kappa+2G)=0.
\]

(10) 中两项的 5-adic depth 分别是

\[
2a_5,
\qquad
a_5+2k+n_5.
\]

因为

\[
a_5=2k-\lambda_5\le2k+n_5,
\]

第一项从不比第二项更深。

### strict case

若

\[
(\lambda_5,n_5)\ne(0,0),
\]

则

\[
a_5<2k+n_5,
\]

两项 valuation 严格不同，所以

\[
\boxed{v_5(W)=a_5.}
\tag{12}
\]

归一化根为

\[
x_\sigma
=\frac{
\kappa G^2C+\sigma(\kappa+G)W
}{
\kappa^2(\kappa+2G)
}.
\tag{13}
\]

其 numerator 的两个 summand 都至少含 `5^{a_5}`，而 denominator 恰含 `5^{2a_5}`。因此约分后

\[
\boxed{d_5(x_\sigma)\le a_5.}
\tag{14}
\]

### resonance case

唯一 valuation equality 是

\[
\lambda_5=0,
\qquad n_5=0.
\]

此时 cancellation 只会让 `W` 更深，即

\[
v_5(W)\ge a_5.
\]

所以 (13) 的 numerator 仍至少含 `5^{a_5}`，从而同样有

\[
\boxed{d_5(x_\sigma)\le a_5.}
\tag{15}
\]

若 `a_5=0`，raw denominator 本身就是 5-unit，结论 (15) 仍显然成立。

综上，对所有 single-2 candidates、两个 signs 均统一有

\[
\boxed{
d_5(x_\sigma)
\le2k-\lambda_5
\le2k.
}
\tag{16}
\]

---

## 4. decimal-height contradiction

5-side completion height 为

\[
H_5
=\max\bigl(v_5(L),d_5(x_\sigma)\bigr).
\]

由 (3)、(16)：

\[
\boxed{H_5\le2k.}
\tag{17}
\]

而 2-side completion height 至少为

\[
H_2\ge v_2(L)=A+k>2k.
\tag{18}
\]

exact decimal recovery 必须满足

\[
H_2=H_5.
\]

(17)-(18) 直接矛盾。因此

\[
\boxed{
\text{minimal-diagonal single-2 deep sector is empty.}
}
\tag{19}

---

## 5. deep frontier after this theorem

在当前 `k=g>=32` minimal diagonal：

- central denominator：旧证书已关闭；
- double-deep：`deep-2high-decimal-height-collapse.md` 已关闭；
- single-2：本文关闭；
- 因此 deep denominator 只剩 `deep-single5-decimal-height-collapse.md` 中三个异常 cells。

换言之，当前 deep frontier 已严格缩成 single-5：

\[
\boxed{
\begin{array}{ll}
\text{Cell I:}&w\in\{1,3\},\ \lambda_2=0,\ B=k+1,\\
\text{Cell II:}&w=4,\ \lambda_2=1,\ B=k+1,\\
\text{Cell III:}&\lambda_2=2k-1,\ v_2(\kappa+2G)=B+k+v_2(w)-1,
\end{array}}
\]

并且三格都还必须满足

\[
v_5(N)=B
\quad\text{or}\quad
v_5(N)\ge B+k.
\]
