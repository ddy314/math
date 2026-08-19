# DD genuine-Gaussian 的 second-order `A_12` residue

> **依赖：** [`genuine-tail-root-orientation-lock.md`](genuine-tail-root-orientation-lock.md)、[`genuine-full-concat-carrier.md`](genuine-full-concat-carrier.md)、`frontier.md` 的 exact decimal remainder identity。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。前两文件已经证明 genuine main core只有一个 surviving elliptic orientation，并有
> \[
> C_G^2\mid A_c\beta+\eta Wa_3,
> \qquad A_c=Qa_2^2b_1^2.
> \]
> 本文不再尝试把该 square-depth当成独立 height；`genuine-elliptic-collapse.md` 已证明它由 sphere carrier支付。本文改做 **digit extraction**：把 exact carry 中 `a_3` 对 `A_12` 的一次依赖代入，利用 `V` 只贡献一层 `C_G`，从 square-depth quotient 中得到一个有效模 `C_G` 的线性 `A_12` residue。
>
> 这给 genuine branch 一个与 full-rational `GCRT+` 平行的 second-order decimal period。

---

## 1. surviving genuine carrier

orientation lock 后记 genuine main core为

\[
\boxed{C_G=C_{\rm ell}}
\]

（以下均默认删除 `10^{o(S)}` exceptional overlap）。

全局 tail-root sign为

\[
\eta\in\{\pm1\}.
\]

定义

\[
A_c:=Qa_2^2b_1^2.
\]

surviving full-concat carrier为

\[
\boxed{
\Psi_G
:=A_c\beta+\eta Wa_3,
\qquad
C_G^2\mid\Psi_G.
}
\tag{1.1}

main unit ledger给

\[
\boxed{
(C_G,g_0UB10W)=1
}
\tag{1.2}

按 main prime-power理解；`2,5` 与 coefficient overlaps均已进入 exceptional core。

---

## 2. exact decimal carry

沿用

\[
X=2^HZ,
\qquad
Y=5^TU,
\qquad
V=X-Y,
\qquad
\Sigma=X+Y.
\]

frontier decimal remainder文件已经证明

\[
\boxed{
\Sigma R_0
=g_0\bigl(B10^dVA_{12}-Ua_3\bigr).
}
\tag{Carry-exact}

等价地

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.
}
\tag{2.1}

同时

\[
V=C_Lv_0.
\]

对 genuine main core定义

\[
\boxed{e_G:=\frac{V}{C_G}.}
\tag{2.2}

因为 `C_G` 使用每个 target rational prime的完整 `p^h` main depth，而 `V/C_L=v_0` 与 main core只有 `10^{o(S)}` overlap，所以删除 exceptional core后

\[
\boxed{(C_G,e_G)=1.}
\tag{2.3}

这条 unit condition保证下面的 `A_12` coefficient不会丢失 genuine period。

---

## 3. 把 carry 代入 genuine square carrier

将 `(1.1)` 乘以 `g_0U`：

\[
g_0U\Psi_G
=g_0UA_c\beta+\eta Wg_0Ua_3.
\]

代入 `(2.1)`：

\[
\begin{aligned}
g_0U\Psi_G
&=g_0UA_c\beta
+\eta W\left(
 g_0B10^dVA_{12}-\Sigma R_0
\right)\\
&=\left(
 g_0UA_c\beta-\eta W\Sigma R_0
\right)
+\eta g_0B10^dWVA_{12}.
\end{aligned}
\tag{3.1}

定义 first quotient numerator

\[
\boxed{
H_G
:=g_0UA_c\beta-\eta W\Sigma R_0.
}
\tag{3.2}

于是

\[
\boxed{
g_0U\Psi_G=H_G+\eta g_0B10^dWVA_{12}.}
\tag{3.3}

---

## 4. `H_G` 自动含第一层 `C_G`

由

\[
C_G^2\mid\Psi_G
\]

知左边 `(3.3)` 被 `C_G^2` 整除。

另一方面

\[
V=C_Ge_G,
\]

所以 `(3.3)` 的第二项至少被 `C_G` 整除。因此

\[
\boxed{C_G\mid H_G.}
\tag{4.1}

定义整数

\[
\boxed{
M_G:=\frac{H_G}{C_G}
=\frac{g_0UA_c\beta-\eta W\Sigma R_0}{C_G}.
}
\tag{4.2}

将 `(3.3)` 除以 `C_G`：

\[
\frac{g_0U\Psi_G}{C_G}
=M_G
+\eta g_0B10^dW e_G A_{12}.
\tag{4.3}

左边仍被 `C_G` 整除，因为原 `Psi_G` 有 square depth。因此得到 genuine second-order residue：

\[
\boxed{
\eta g_0B10^dW e_G A_{12}
\equiv-M_G
\pmod{C_G}.
}
\tag{GCRT-G}

这是 exact ordinary-integer congruence。

---

## 5. effective period 正好是 `C_G`

固定 genuine main

\[
p^h\Vert C_G.
\]

main unit ledger与 `(2.3)` 给

\[
p\nmid \eta g_0B10^dW e_G.
\]

因此 `(GCRT-G)` 对 `A_12` 的有效 `p`-period正好是

\[
p^h.
\]

聚合所有 genuine main prime-powers：

\[
\boxed{
\text{effective rational period of `(GCRT-G)`}
=C_G/10^{o(S)}.
}
\tag{5.1}

所以 genuine square-depth的两层在 decimal extraction 中具有清楚分工：

1. 第一层 `C_G` 被 `V=C_G e_G` 自动支付；
2. 第二层留下一个真正作用于 `A_12` 的模 `C_G` linear residue。

注意这只是 **period / counting information**。它不与 `genuine-elliptic-collapse.md` 冲突：后者说明该 depth不是新的独立 p-adic height；本文只是利用同一 depth读取 decimal variable。

---

## 6. 与 full-rational `GCRT+` 的平行性

full-rational rational-contact core `E=D_+D_-` 已有 second-order Gaussian quotient identity，给 `A_12` 一个有效 period

\[
E/10^{o(S)}.
\]

本文给 genuine complement一个平行 period

\[
C_G/10^{o(S)}.
\]

而 terminal rational/genuine split满足

\[
\boxed{
E\,C_G=C_L\cdot10^{o(S)},
\qquad
(E,C_G)=10^{o(S)}.
}
\tag{6.1}

所以两类 second-order decimal readers正好覆盖整个 moving pair-max main core。

下一文件可据此把 partial-rational `GCRT+` 与 `(GCRT-G)` 拼成一个 **split-independent full-`C_L` A_12 period**。

---

## 7. no-double-count 边界

必须区分两件事：

- `genuine-elliptic-collapse.md`：证明 `C_G^2|Psi_G` 的 p-adic depth由 sphere carrier支付，不能再算作一份新的 height surplus；
- 本文：在已存在的 square-depth中读取 `A_12` 的 second-order residue，得到 period `C_G`。

因此本文允许用于：

- CRT uniqueness；
- candidate counting；
- digit-shell location。

但不能把 `C_G` period再当作 sphere carrier之外的额外 modulus height来证明同一局部矛盾。

---

## 8. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`H_G` first-layer divisibility、integer quotient `M_G`、genuine second-order `GCRT-G`、effective period `C_G`。
- **`失效/降级`**：把 `GCRT-G` 当作 sphere square-depth之外的新 p-adic收费。
- **`待证`**：rational/genuine hybrid `C_L`-period CRT；unique lift 的 Archimedean location；DD frontier emptiness。
