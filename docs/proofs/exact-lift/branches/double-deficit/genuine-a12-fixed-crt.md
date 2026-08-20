# DD genuine-Gaussian 的 W-free fixed `A_12` CRT

> **依赖：** [`genuine-elliptic-collapse.md`](genuine-elliptic-collapse.md)、[`genuine-a12-second-order-crt.md`](genuine-a12-second-order-crt.md)、`frontier.md` 的 exact carry。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。上一文件从 `Psi_G` 直接读取了模 `C_G` 的 `A_12` period，但 coefficient / quotient仍含 discriminant root `W`。本文进一步使用已经证明 sphere-paid 的 W-free carrier
> \[
> \Theta=(\kappa+G)A_c\beta+\mathscr T a_3^2,
> \qquad C_G^2\mid\Theta,
> \]
> 再代入 exact carry。由于 `V=C_G e_G`，平方展开中的 `A_12^2` 项自动含 `C_G^2`，线性项恰含一层 `C_G`。除去一层后得到一个 coefficients 完全独立于 `A_12,a_3,W` 的 fixed linear CRT：
> \[
> 2\mathscr T g_0B10^d e_G\Sigma R_0 A_{12}
> \equiv M_{G,0}\pmod{C_G}.
> \]
>
> 这是真正适合与 `q_c^2` / rational-contact periods 做跨分支 CRT 的 genuine decimal reader。

---

## 1. W-free surviving carrier

沿用

\[
A_c=Qa_2^2b_1^2,
\]

\[
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^{m_3}},
\]

以及 orientation-locked genuine main core `C_G`。

`genuine-elliptic-collapse.md` 定义

\[
\boxed{
\Theta
=(\kappa+G)A_c\beta+\mathscr T a_3^2
}
\tag{1.1}

并证明

\[
\boxed{C_G^2\mid\Theta.}
\tag{1.2}

虽然该 square-depth由 sphere carrier支付，仍可用于 decimal-variable extraction。

---

## 2. exact carry 的平方展开

exact carry为

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.
}
\tag{2.1}

平方得到

\[
\begin{aligned}
g_0^2U^2a_3^2
&=g_0^2B^2 10^{2d}V^2A_{12}^2
-2g_0B10^dV\Sigma R_0A_{12}
+\Sigma^2R_0^2.
\end{aligned}
\tag{2.2}

将 `(2.2)` 代入 `g_0^2U^2 Theta`：

\[
\begin{aligned}
g_0^2U^2\Theta
={}&g_0^2U^2(\kappa+G)A_c\beta
+\mathscr T\Sigma^2R_0^2\\
&-2\mathscr T g_0B10^dV\Sigma R_0A_{12}\\
&+\mathscr T g_0^2B^2 10^{2d}V^2A_{12}^2.
\end{aligned}
\tag{2.3}

定义 constant part

\[
\boxed{
H_{G,0}
:=g_0^2U^2(\kappa+G)A_c\beta
+\mathscr T\Sigma^2R_0^2.
}
\tag{2.4}

注意 `H_{G,0}` 只依赖 denominator/source/prefix-small data 与 `kappa`；它不含

\[
A_{12},\quad a_3,\quad W.
\]

---

## 3. constant part 自动含第一层 `C_G`

写

\[
\boxed{V=C_Ge_G.}
\tag{3.1}

由 `(1.2)`：

\[
C_G^2\mid g_0^2U^2\Theta.
\]

在 `(2.3)` 中：

- linear `A_12` 项含显式 `V`，故至少含一层 `C_G`；
- quadratic `A_12^2` 项含 `V^2`，故至少含两层 `C_G`。

因此模 `C_G` 观察 `(2.3)`，只能剩 constant part；故

\[
\boxed{C_G\mid H_{G,0}.}
\tag{3.2}

定义整数

\[
\boxed{
M_{G,0}
:=\frac{H_{G,0}}{C_G}.
}
\tag{3.3}

---

## 4. 除去第一层后得到 fixed linear `A_12` residue

把 `(2.3)` 除以 `C_G`，使用 `(3.1)`：

\[
\begin{aligned}
\frac{g_0^2U^2\Theta}{C_G}
={}&M_{G,0}
-2\mathscr T g_0B10^d e_G\Sigma R_0A_{12}\\
&+C_G\,\mathscr T g_0^2B^2 10^{2d}e_G^2A_{12}^2.
\end{aligned}
\tag{4.1}

左边仍被 `C_G` 整除，最后一项也显式被 `C_G` 整除。因此模 `C_G` 得到

\[
\boxed{
2\mathscr T g_0B10^d e_G\Sigma R_0A_{12}
\equiv M_{G,0}
\pmod{C_G}.
}
\tag{GCRT-G0}

这就是 W-free fixed genuine CRT。

与上一文件 `(GCRT-G)` 相比，新式的关键改进是：

\[
\boxed{
M_{G,0}\text{ 与 coefficient 都不含 }A_{12},a_3,W.
}
\tag{4.2}

所以它可在固定 denominator/source fiber 中真正作为一个不随待求 prefix 变化的 period 使用。

---

## 5. effective period 精确为 `C_G`

固定

\[
p^h\Vert C_G.
\]

main unit ledger给

\[
p\nmid g_0B10R_0e_G.
\]

还需检查 `mathscr T` 与 `Sigma`。

### 5.1 `mathscr T` 是 target p-unit

`genuine-tail-root-orientation-lock.md` 的 exact identity为

\[
\mathscr T a_3
=\kappa G^2C_{\rm DD}+\eta(\kappa+G)W.
\]

模 `p`：

\[
\mathscr T a_3
\equiv\eta\kappa W\not\equiv0\pmod p,
\]

因为 `a_3,kappa,W` 都是 p-units。因此

\[
\boxed{p\nmid\mathscr T.}
\tag{5.1}

### 5.2 `Sigma` 是 target p-unit

由

\[
V=X-Y\equiv0\pmod p,
\]

且 `X,Y` 为 p-units，

\[
\Sigma=X+Y\equiv2Y\not\equiv0\pmod p
\]

（`p` 为 odd main split prime）。故

\[
\boxed{p\nmid\Sigma.}
\tag{5.2}

综上 `(GCRT-G0)` 的 `A_12` coefficient在每个 main target prime上都是 unit。因此

\[
\boxed{
\text{effective period of `(GCRT-G0)`}
=C_G/10^{o(S)}.
}
\tag{5.3}

---

## 6. 与 sphere-pay no-go 的兼容性

`Theta` 的 `C_G^2` depth 已被 `Sphere-pay-identity` 证明完全由 original sphere carrier支付。

本文没有把它重新解释成一份新的 p-adic height。做的只是：

\[
\boxed{
\text{在同一已知 square-depth内，利用 }V=C_Ge_G
\text{ 把 second layer 读取成 fixed decimal residue。}
}

这和 A2 / full-rational 中“同一 depth 可以作为 CRT period，但不能重复计入 height surplus”完全一致。

---

## 7. 下一步接口

现在 genuine main core提供一个固定 period

\[
C_G,
\]

而 rational-contact core已有 second-order period

\[
E=D_+D_-.
\]

rational/genuine split满足

\[
EC_G=C_L\cdot10^{o(S)}.
\]

因此下一步应证明 partial rational `GCRT+` 在 `E` 未占满 `C_L` 时仍保持 effective period `E`，然后与 `(GCRT-G0)` 合并成 split-independent `C_L` period。

---

## 8. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：W-free carry square expansion、`C_G|H_{G,0}`、fixed `GCRT-G0`、`mathscr T/Sigma` unit audit、effective period `C_G`。
- **`失效/降级`**：把 fixed period `C_G` 当作 sphere carrier之外的新 height obstruction。
- **`待证`**：partial-rational GCRT extension；hybrid full-`C_L` decimal period；unique lift location；DD frontier emptiness。
