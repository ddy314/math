# DD gap/recovery square identities 的 no-double-pay 审计

> **依赖：** [`high-funnel-gap-square-core.md`](high-funnel-gap-square-core.md)、
> [`high-funnel-recovery-squarefree-lock.md`](high-funnel-recovery-squarefree-lock.md)、
> `global-framework.md` 的 `G_0|2G N_12`。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 两条看似不同的平方结构
> \[
> 5^Ta_0G_0=s\varepsilon\mu^2
> \]
> 与
> \[
> h^2G_0=2\varepsilon^3Lc^4r_*^2a_0
> \]
> **不是两份独立高度**。结合
> \[
> L=2\cdot5^T/s
> \]
> 后，它们恰好退化为 `mu=N_mu/h` 的定义平方。
>
> 真正可从第二式继续提取的新信息来自全局 recovery gcd bound
> `G_0|2G N_12`，它给出新的 exact divisor
> \[
> \boxed{
> \varepsilon^2Lc^2r_*a_0
> \mid
> V\lambda\mathcal N_{12}h^2,
> }
> \]
> 等价地
> \[
> \boxed{
> \mu^2
> \mid
> V\lambda Lc^2r_*a_0\mathcal N_{12}.
> }
> \]

---

## 1. 两条 square identity

已有

\[
\boxed{
5^Ta_0G_0=s\varepsilon\mu^2,
}
\tag{Gap-square}

以及

\[
\boxed{
h^2G_0=2\varepsilon^3Lc^4r_*^2a_0.}
\tag{Recovery-square}

这里

\[
N_\mu=\varepsilon Lc^2r_*a_0,
\qquad
h=(N_\mu,q_0),
\qquad
\mu=N_\mu/h,
\]

且 canonical `t_2=1` normalization给

\[
\boxed{L=\frac{2\cdot5^T}{s}.}
\tag{1.1}

---

## 2. 两式联立只恢复 `h mu = N_mu`

把 `(Recovery-square)` 中的 `G_0` 代入 `(Gap-square)`：

\[
5^Ta_0
\frac{2\varepsilon^3Lc^4r_*^2a_0}{h^2}
=s\varepsilon\mu^2.
\]

由 `(1.1)`，

\[
2\cdot5^T=sL.
\]

所以

\[
\frac{s\varepsilon^3L^2c^4r_*^2a_0^2}{h^2}
=s\varepsilon\mu^2.
\]

约去 `s epsilon`：

\[
\left(
\frac{\varepsilon Lc^2r_*a_0}{h}
\right)^2
=\mu^2.
\]

所有量均为正，因此

\[
\boxed{
h\mu=\varepsilon Lc^2r_*a_0=N_\mu.}
\tag{2.1}

这正是 `mu=N_mu/h` 的定义，不是新的 obstruction。

因此禁止如下 double-count：

> 不能把 `Gap-square` 与 `Recovery-square` 的 squarefree / square-depth
> 看成两份独立约束再相加高度。

它们是同一 primitive recovery algebra 的两个 reader。

---

## 3. 真正的新输入：`G_0|2G N_12`

全局 primitive recovery 已证明

\[
\boxed{G_0\mid2G\mathcal N_{12}.}
\tag{3.1}

而 overlap 参数化给

\[
\boxed{G=\varepsilon Vc^2\lambda r_*.}
\tag{3.2}

令

\[
K:=\frac{2G\mathcal N_{12}}{G_0}\in\mathbf Z_{>0}.
\]

将 `(Recovery-square)` 与 `(3.2)` 代入：

\[
\begin{aligned}
K
&=
\frac{2\varepsilon Vc^2\lambda r_*\mathcal N_{12}}
{2\varepsilon^3Lc^4r_*^2a_0/h^2}\\
&=
\boxed{
\frac{V\lambda\mathcal N_{12}h^2}
{\varepsilon^2Lc^2r_*a_0}.}
\end{aligned}
\tag{3.3}

因为 `K` 是整数，得到 exact divisor

\[
\boxed{
\varepsilon^2Lc^2r_*a_0
\mid
V\lambda\mathcal N_{12}h^2.
}
\tag{Recovery-divisor-h}

---

## 4. 等价的 `mu^2` divisor

由 `(2.1)`：

\[
h^2\mu^2
=\varepsilon^2L^2c^4r_*^2a_0^2.
\]

将 `(3.3)` 中的 `h^2` 改写，也可得到

\[
K
=
\frac{V\lambda Lc^2r_*a_0\mathcal N_{12}}{\mu^2}.
\]

因此

\[
\boxed{
\mu^2
\mid
V\lambda Lc^2r_*a_0\mathcal N_{12}.
}
\tag{Recovery-divisor-mu}

这条比 squarefree-kernel parity强：它控制的是 `mu` 的**完整平方深度**。

---

## 5. primewise allocation

对任意 prime `p`，令 `v_p` 简写为 valuation。`Recovery-divisor-mu` 给

\[
\boxed{
2v_p(\mu)
\le
v_p(V)+v_p(\lambda)+v_p(L)
+2v_p(c)+v_p(r_*)+v_p(a_0)+v_p(\mathcal N_{12}).
}
\tag{5.1}

所以任何 `mu` 的正线性 square depth必须由以下真实 payer承担：

- moving imbalance `V`；
- primitive common scale `lambda`；
- decimal smooth tail `L`；
- overlap common factor `c^2 r_*`；
- gap quotient `a_0`；
- prefix Gaussian norm `N_12`。

但本文不把这些 payer视为相互独立；它们之间仍有 overlap 参数化与
scale-free quadratic 的关系，下一步必须继续做 no-double-pay。

---

## 6. pure common 的 5-adic consistency

在 pure common sheet：

\[
T=2g_5,
\quad v_5(\mu)=g_5,
\quad v_5(V)=v_5(a_0)=v_5(\mathcal N_{12})=0.
\]

`Recovery-divisor-mu` 的 5-adic 左边为 `2g_5`，而 `L` 本身已经恰有

\[
v_5(L)=2g_5.
\]

所以该 prime 上 divisor完全由 forced decimal baseline `L` 支付，没有额外
5-adic contradiction。这再次说明 pure common 的真正下一自由度不是继续做
same-prime 5-adic lifting，而是 rough/square-height allocation。

---

## 7. 状态摘要

- **`已严格完成`**：square-identities no-double-pay、`Recovery-divisor-h`、
  `Recovery-divisor-mu`。
- **`失效/降级`**：把 `Gap-square` 与 `Recovery-square` 当两条独立 square
  obstruction进行高度相加。
- **`待证`**：rough prime 下 `mu^2` payer 的进一步互斥；post-tail side-branch
  reoptimization；DD global explicit slope / absolute height。
