# DD tail-root `kappa+G` fixed-CRT route 的 exact collapse

> **依赖：** [`genuine-tail-root-orientation-lock.md`](genuine-tail-root-orientation-lock.md) 的 `Tail-root-original`、`frontier.md` 的 exact carry 与 terminal primitive overlap。
>
> **严格状态：** `失效/降级（已严格证明退化）`。将 tail-root linear identity 与 decimal carry联立，表面上会产生一个模 `kappa+G` 的 fixed `A_12` congruence。由于 `kappa+G` 具有约 `QG` 尺度，这看起来像一个潜在第三大 period。本文证明 terminal primitive overlap使其 coefficient **精确含整个 `kappa+G`**：
> \[
> \mathscr T BV-U\kappa G^2
> =U\kappa G(\kappa+G).
> \]
> 因此该 congruence 中 `A_12` 项模 `kappa+G` 恒为零，只剩旧 common-factor condition；effective `A_12` period 为零。

---

## 1. candidate congruence

沿用

\[
D:=10^d,
\qquad F:=5^T,
\qquad T_3:=10^{m_3}.
\]

全局 tail-root linear identity为

\[
\boxed{
\mathscr T a_3
=\kappa G^2D A_{12}
+\eta(\kappa+G)W,
}
\tag{1.1}

其中

\[
\boxed{
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{T_3}.
}
\tag{1.2}

exact carry为

\[
\boxed{
g_0Ua_3
=g_0BDVA_{12}-\Sigma R_0.}
\tag{1.3}

把 `(1.3)` 代入 `(1.1)` 并乘 `g_0U`：

\[
\mathscr T(g_0BDVA_{12}-\Sigma R_0)
=g_0U\kappa G^2DA_{12}
+\eta g_0U(\kappa+G)W.
\]

整理：

\[
\boxed{
g_0D(\mathscr T BV-U\kappa G^2)A_{12}
-\mathscr T\Sigma R_0
=\eta g_0U(\kappa+G)W.}
\tag{Candidate-exact}

所以形式上有

\[
\boxed{
g_0D(\mathscr T BV-U\kappa G^2)A_{12}
\equiv\mathscr T\Sigma R_0
\pmod{\kappa+G}.}
\tag{Candidate-CRT}

---

## 2. coefficient 的第一层化简

terminal smooth relation为

\[
\boxed{\frac{T_3}{B}=2F.}
\tag{2.1}

因此

\[
\begin{aligned}
\mathscr T BV-U\kappa G^2
&=\frac{\kappa^2(\kappa+2G)}{T_3}BV
-U\kappa G^2\\
&=\frac{\kappa}{2F}
\left[\kappa(\kappa+2G)V-2FUG^2\right].
\end{aligned}
\tag{2.2}

又

\[
\Sigma=V+2FU.
\]

故括号可写成

\[
\begin{aligned}
\kappa(\kappa+2G)V-2FUG^2
&=V\left[\kappa(\kappa+2G)+G^2\right]-G^2\Sigma\\
&=\boxed{V(\kappa+G)^2-G^2\Sigma}.
\end{aligned}
\tag{2.3}

所以

\[
\boxed{
\mathscr T BV-U\kappa G^2
=\frac{\kappa}{2F}
\left[V(\kappa+G)^2-G^2\Sigma\right].}
\tag{2.4}

仅看这一步，似乎 `kappa+G` 还可能留下大 period；terminal primitive overlap会把它完全消掉。

---

## 3. terminal primitive overlap

frontier 已有

\[
\gamma=(\kappa,G),
\qquad
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
\]

并在 terminal primitive overlap 中精确识别

\[
\boxed{u=2FU,\qquad v=V.}
\tag{3.1}

因此

\[
\boxed{
\kappa=2\gamma FU,
\qquad
G=\gamma V.}
\tag{3.2}

特别地

\[
\boxed{
\kappa+G
=\gamma(2FU+V)
=\gamma\Sigma.}
\tag{KplusG}

同理还顺带有

\[
\boxed{
\kappa+2G
=2\gamma(FU+V)
=2\gamma X,}
\tag{Kplus2G}

因为 `X=FU+V`。

这两式说明 unified tail factors本身就是 terminal S-unit phase的缩放，不是新的独立 moving moduli。

---

## 4. candidate coefficient 精确含整个 modulus

把 `(3.2)` 与 `(KplusG)` 代入 `(2.4)`。更直接地，从 `(2.2)`：

\[
\begin{aligned}
\frac{\kappa^2(\kappa+2G)}{T_3}BV
&=\kappa\frac{\kappa}{2F}(\kappa+2G)V\\
&=\kappa(\gamma U)(\kappa+2G)V\\
&=U\kappa G(\kappa+2G),
\end{aligned}
\]

因为

\[
\frac\kappa{2F}=\gamma U,
\qquad
\gamma V=G.
\]

所以

\[
\begin{aligned}
\mathscr T BV-U\kappa G^2
&=U\kappa G(\kappa+2G)-U\kappa G^2\\
&=\boxed{U\kappa G(\kappa+G).}
\end{aligned}
\tag{Coefficient-collapse}

这是 exact integer identity。

因此 `(Candidate-exact)` 其实为

\[
\boxed{
g_0DU\kappa G(\kappa+G)A_{12}
-\mathscr T\Sigma R_0
=\eta g_0U(\kappa+G)W.}
\tag{4.1}

模 `kappa+G` 后，`A_12` 项完全消失：

\[
\boxed{
\mathscr T\Sigma R_0
\equiv0\pmod{\kappa+G}.}
\tag{4.2}

所以 `(Candidate-CRT)` 对 `A_12` 的 effective period正好为

\[
\boxed{1.}
\tag{Zero-period}

---

## 5. 剩余 divisibility 只是 common-factor condition

由 `(KplusG)`：

\[
\kappa+G=\gamma\Sigma.
\]

于是 `(4.2)` 约去显式 `Sigma` 后只要求

\[
\boxed{\gamma\mid\mathscr T R_0}
\tag{5.1}

在相应 integer quotient意义下成立。

这不再含 `A_12`，只能作为已有 terminal common-factor ledger 的一部分；不能与 `C_L` / `q_c^2` CRT再叠加成第三 decimal period。

---

## 6. 方法含义

此前最诱人的第三 fixed modulus候选有：

\[
\kappa+G\asymp QG.
\]

若只看 `Tail-root-original` 与 carry，它似乎会给一个很大的 `A_12` period。但 exact terminal identification

\[
\kappa+G=\gamma\Sigma
\]

和 `(Coefficient-collapse)` 说明：

\[
\boxed{
\text{`kappa+G` 的全部 moving modulus
已经位于 coefficient 中；}
\text{它对 decimal prefix没有剩余 period。}}
\]

所以后续不得把 `(Candidate-CRT)` 计作第三 independent residue。

同时 `(KplusG)/(Kplus2G)` 解释了这个退化为何是结构性的：`kappa+G` 与 `kappa+2G` 分别就是 S-unit sum `Sigma` 与 `2X` 的 `gamma`-倍数。

---

## 7. 状态摘要

- **`已严格完成`**：`Candidate-exact`、coefficient 两级化简、`kappa+G=gamma Sigma`、`kappa+2G=2gamma X`、`Coefficient-collapse`。
- **`失效/降级`**：把 `kappa+G` 当作第三 fixed `A_12` period；其 effective prefix period为零。
- **`待证`**：split-independent `C_L q_c^2` unique lift的 Archimedean location；真正独立第三 residue若存在；DD frontier emptiness。
