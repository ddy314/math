# DD full-rational Good 的 prefix CRT location audit

> **依赖：** [`good-prefix-polarization.md`](good-prefix-polarization.md) 与 [`frontier.md`](frontier.md) 的 `R0-A12`、clean source、`QCRT-exact`、axis factorization、`A12-second+`。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文审计上一文件留下的唯一 leading-block residue `a_1` 的 Archimedean location。结论是：`Prefix-QCRT` 与 `Prefix-GCRT` 都是真实且联合 period 超过 `a_1` 窗口的 congruence，但它们的 natural exact representatives 完全由已有 numerator reconstruction / clean-source / axis factorization重构；两条 prefix residual 之间还有一个 exact compatibility identity，其差值正是 `U q_c^2 L_clean`。因此现有 full-rational parent identities 本身不能把“至多一个 `a_1`”升级为 emptiness。
>
> 这封闭的是 **full-rational Good 中继续展开现有 Q/G CRT parents 以寻找短自然代表** 的路线；它不证明 `a_1` 不存在，也不关闭 DD。

---

## 1. 基线与 prefix 变量

沿用

\[
A_{12}=10^{n_2}a_1+a_2.
\]

为简洁记

\[
t:=10^{n_2},
\qquad
D:=10^d,
\qquad
F:=5^T.
\tag{1.1}
\]

并保留

\[
X=2^HZ,
\qquad
\Sigma=X+FU,
\qquad
V=X-FU.
\tag{1.2}
\]

因此

\[
\boxed{\Sigma-X=FU.}
\tag{1.3}
\]

numerator reconstruction 的 terminal form 为

\[
\boxed{
\Sigma R_0
=g_0(BDVA_{12}-Ua_3).
}
\tag{R0-A12}
\]

而 clean source 与 `a_3` bridge 分别为

\[
VA_0-FR_0=q_c^2L_{\rm clean},
\tag{1.4}
\]

\[
g_0a_3=VA_0-2FR_0.
\tag{1.5}
\]

两式相减立刻得到

\[
\boxed{
q_c^2L_{\rm clean}=g_0a_3+FR_0.
}
\tag{Source-a3}
\]

这条 exact identity 是下面 location audit 的关键。

---

## 2. Prefix-QCRT 的 natural representative

将

\[
A_{12}=ta_1+a_2
\]

代入 `(R0-A12)`：

\[
\begin{aligned}
g_0BDVt a_1
&=\Sigma R_0+g_0Ua_3-g_0BDVa_2.
\end{aligned}
\tag{2.1}
\]

定义 Q-side natural residual

\[
\boxed{
H_Q:=XR_0-g_0BDVa_2.
}
\tag{2.2}
\]

由于

\[
C_*:=\frac{g_0a_2B}{2},
\]

还可写成

\[
\boxed{
H_Q=XR_0-2DVC_*.
}
\tag{2.3}
\]

从 `(2.1)` 减去 `(2.2)`，使用 `(1.3)`：

\[
\begin{aligned}
g_0BDVt a_1-H_Q
&=(\Sigma-X)R_0+g_0Ua_3\\
&=U(FR_0+g_0a_3).
\end{aligned}
\]

最后用 `(Source-a3)`：

\[
\boxed{
g_0BDVt a_1-H_Q
=Uq_c^2L_{\rm clean}.}
\tag{Prefix-Q-exact}
\]

因此模 `q_c^2`：

\[
\boxed{
g_0BDVt a_1
\equiv
XR_0-2DVC_*
\pmod{q_c^2}.}
\tag{Prefix-Q-natural}
\]

删去 coefficient exceptional core 后，这就是上一文件的 `Prefix-QCRT`。

关键是 `(Prefix-Q-exact)` 已经精确告诉我们这个 residue 的 natural parent：它与真正的 `a_1` 项之间相差

\[
Uq_c^2L_{\rm clean},
\]

即已有 clean-source quotient 的整数倍。

所以若仅使用

- `R0-A12`；
- `Source-a3`；
- `QCRT-exact`

继续化简 `Prefix-QCRT`，不会产生一个独立短代表；所有 rearrangement 都只是 `(Prefix-Q-exact)` 的重写。

**状态：`失效/降级`，若把 `H_Q` 当作新的 independent short residue。**

---

## 3. Prefix-GCRT 的 exact parent同样完全显式

full rational-contact 中取

\[
\Gamma:=\Pi_+\overline{\Pi_-},
\qquad
N(\Gamma)=E,
\qquad
V=Ee_0,
\tag{3.1}
\]

以及 axis factorization

\[
\boxed{
C_*+iR_0=\Gamma\overline K.
}
\tag{3.2}
\]

已有

\[
\boxed{
M_+
:=
\frac{\Sigma C_*-ig_0Ua_3}{\Gamma}
\in\mathbf Z[i],
}
\tag{3.3}
\]

和 exact second-order identity

\[
\boxed{
\Sigma\overline K-M_+
=ig_0BDe_0\overline\Gamma A_{12}.
}
\tag{A12-second+}
\]

代入

\[
A_{12}=ta_1+a_2
\]

并定义 suffix-deleted Gaussian residual

\[
\boxed{
H_G
:=
\Sigma\overline K-M_+
-ig_0BDe_0\overline\Gamma a_2.
}
\tag{3.4}
\]

则直接得到

\[
\boxed{
H_G
=ig_0BDe_0\overline\Gamma t a_1.
}
\tag{Prefix-G-exact}
\]

模 `Gamma` 后正是 `Prefix-GCRT` 的 parent。

这里同样没有 hidden Archimedean saving：`H_G` 作为 natural exact representative 本身就等于 `a_1` 主项乘上完整 Gaussian coefficient。只有在模 `Gamma` 以后它才成为 residue class；仅靠 `(A12-second+)` 与 axis factorization不能把该 class 的最小代表压短。

---

## 4. 两条 prefix residual 的 exact compatibility

由于

\[
V=E e_0
=\Gamma\overline\Gamma e_0,
\]

从 `(Prefix-G-exact)` 得

\[
-i\Gamma H_G
=g_0BDVt a_1.
\tag{4.1}
\]

与 `(Prefix-Q-exact)` 联立，立即得到

\[
\boxed{
-i\Gamma H_G-H_Q
=Uq_c^2L_{\rm clean}.}
\tag{Prefix-QG-compat}
\]

这条 identity 很重要，因为它区分了两种“独立性”：

1. **period 独立性**：`q_c^2` 与 rational kernel `E=N(\Gamma)` 的 overlap 只有 `10^{o(S)}`，所以 `QCRT+GCRT` 的联合 period 确实达到
   \[
   10^{1.617767155236\ldots S+o(S)};
   \]
   因而 fixed slow data 下 `a_1` 至多一个。
2. **natural-representative 独立性**：`(Prefix-QG-compat)` 显示两条 exact parent residual 并非两个自由的短整数；它们之间的差恰由已有 clean source `Uq_c^2L_clean` 支付。

所以不能从“两个 periods 几乎互素”直接推成“两个 natural short representatives 独立”。

---

## 5. `QCRT-exact` 本身也可由同一两条 parent 恢复

已有 QCRT exact parent：

\[
\Sigma q_c^2L_{\rm clean}
=g_0(FBDVA_{12}+Xa_3).
\tag{5.1}
\]

将 `(Source-a3)` 代入左边：

\[
\Sigma(g_0a_3+FR_0)
=g_0(FBDVA_{12}+Xa_3).
\]

移项并使用

\[
\Sigma-X=FU
\]

后，约去 `F`，得到

\[
\Sigma R_0
=g_0(BDVA_{12}-Ua_3),
\]

正是 `(R0-A12)`。

因此：

\[
\boxed{
\text{`QCRT-exact`}
\Longleftrightarrow
\text{`R0-A12` + `Source-a3`}
}
\tag{Q-parent-equivalence}
\]

在当前 terminal identities 下成立。

这进一步说明 Q-side location不能从自己的 exact parent 中再榨出独立的 Archimedean约束。

---

## 6. G-side exact parent同样只是 axis quotient后的 reconstruction

由 `(3.2)`：

\[
\overline K=\frac{C_*+iR_0}{\Gamma}.
\]

把它和 `(3.3)` 代入 `(3.4)`：

\[
\begin{aligned}
\Gamma H_G
&=\Sigma(C_*+iR_0)
-(\Sigma C_*-ig_0Ua_3)
-i g_0BD e_0\Gamma\overline\Gamma a_2\\
&=i\left(
\Sigma R_0+g_0Ua_3-g_0BDVa_2
\right).
\end{aligned}
\]

由 `(2.1)`：

\[
\boxed{
\Gamma H_G
=i g_0BDVt a_1.
}
\tag{6.1}
\]

正好恢复 `(Prefix-G-exact)`。

所以 G-side 所谓 second-order parent，是把同一 numerator reconstruction 先沿 axis Gaussian factor `Gamma` 做一次 quotient 后再读取；它在 p-adic period 上是真实的新层，但 exact Archimedean representative 没有脱离 reconstruction algebra。

---

## 7. full-rational prefix location 的 no-go 边界

现在可以严格记录：

\[
\boxed{
\begin{array}{l}
\text{Prefix-QCRT natural parent}
\;\leftrightarrow\;
\text{reconstruction + clean source},\\[1mm]
\text{Prefix-GCRT natural parent}
\;\leftrightarrow\;
\text{axis quotient of the same reconstruction},\\[1mm]
-i\Gamma H_G-H_Q
=Uq_c^2L_{\rm clean}.
\end{array}}
\tag{7.1}
\]

所以已有 parents 足以给出：

\[
\boxed{\#\{a_1\}\le1}
\]

但不足以给出：

\[
\boxed{\#\{a_1\}=0.}
\]

任何声称从 `H_Q,H_G` 的“同时短”直接得到矛盾的证明，都必须先提供一个**不来自** `R0-A12` / `Source-a3` / axis factorization 的独立 Archimedean bound；否则会由 `(Prefix-QG-compat)` 重复计算同一 source payer。

**状态：当前 full-rational Q/G parent algebra 的 location route `失效/降级`。**

---

## 8. 方法切换

此前 continuation 已多次证明：

- first-order rational determinants critical；
- local higher Gaussian resultants退回 hidden square；
- short-residue local candidates退回 `C_L` carry / `N(Delta_1)` / axis baseline；
- 本文又证明 Q/G unique-lift 的 natural representatives退回 reconstruction / clean source。

因此 full-rational Good 的已知 local + prefix algebra 在当前变量系统下已经形成闭包。后续若没有真正外部的 Archimedean digit theorem，不应继续制造同一组 parent identities 的 eliminant。

下一主攻方向改为 frontier 中仍独立开放的

\[
\boxed{
\text{genuine-Gaussian split-prime / digit-shell branch}.}
\]

那里正线性 main core 不满足 rational sign degeneration，因而不会自动落回本文件的 Q/G rational-contact parent sheet。

---

## 9. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Source-a3`；`Prefix-Q-exact`；`Prefix-G-exact`；`Prefix-QG-compat`；`Q-parent-equivalence`；G-parent reconstruction audit。
- **`失效/降级`**：从现有 Q/G exact parents内部寻找第二个 independent short natural representative；把 period independence误当 natural-representative independence。
- **`待证`**：外部 Archimedean digit-window theorem 若存在；genuine-Gaussian split-prime / digit-shell closure；DD 全局空性。
