# DD canonical `t_2=1` funnel 的 gap square-core identity

> **依赖：** [`high-funnel-exact-small-factor-normalization.md`](high-funnel-exact-small-factor-normalization.md)、
> `core.md` 的 `F_-` 定义、overlap 参数化与 `G_0|2G N_12`。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> exact small-factor quotient
> \[
> R=a\frac{g_*}{V}
> \]
> 与
> \[
> F_-=\frac{2(\kappa+2G)\mu^2}{G_0}
> \]
> 可以完全对齐。最终得到
> \[
> \boxed{
> a_0 5^T G_0=s\varepsilon\mu^2,
> \qquad
> s=(2\cdot5^T,q),
> }
> \]
> 其中 `c_3=epsilon c`、`a=ca_0`。
> 因此 `a_0 5^T G_0/(s epsilon)` 是一个**整数完全平方**。

---

## 1. 从 `F_-` 的二次式定义读取同一个 quotient

统一 near-square factors 中

\[
\boxed{
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0}.
}
\tag{1.1}

在 `t_2=1` phase：

\[
\kappa+2G
=\gamma(u+2v)
=2\gamma\,2^HZ.
\]

所以

\[
\boxed{
F_-
=2^{H+2}Z\frac{\gamma\mu^2}{G_0}.
}
\tag{1.2}

另一方面 `high-funnel-exact-small-factor-normalization.md` 已证明

\[
\boxed{
F_-=
\frac{2^{H+2}5^TZ}{s}
\;a\frac{g_*}{V},
\qquad
s=(2\cdot5^T,q).
}
\tag{1.3}

约去共同正因子 `2^{H+2} Z`：

\[
\boxed{
\frac{\gamma\mu^2}{G_0}
=
\frac{5^T}{s}
\;a\frac{g_*}{V}.
}
\tag{1.4}

等价地

\[
\boxed{
sa g_*G_0
=5^TV\gamma\mu^2.
}
\tag{1.5}

---

## 2. `gamma` 精确消失

denominator overlap 定义给

\[
\boxed{g_*=G/c_3.}
\tag{2.1}

而 gcd-normal form为

\[
\boxed{G=\gamma V.}
\tag{2.2}

所以

\[
\boxed{
\frac{g_*}{V}=\frac{\gamma}{c_3}.
}
\tag{2.3}

把 `(2.3)` 直接代入 `(1.4)`，约去 `gamma`：

\[
\frac{\mu^2}{G_0}
=
\frac{5^T}{s}\frac{a}{c_3}.
\]

因此

\[
\boxed{
saG_0=5^Tc_3\mu^2.
}
\tag{2.4}

注意这里的方向必须如此：从 `(1.4)` 有

\[
\gamma\mu^2/G_0
=(5^T/s)\,a\gamma/c_3,
\]

故

\[
s c_3\mu^2=5^T a G_0.
\]

所以整理后的标准形式是

\[
\boxed{
5^T a G_0=s c_3\mu^2.
}
\tag{Gap-square-raw}

---

## 3. primitive gap 形式

overlap 参数化还有

\[
\boxed{c_3=\varepsilon c,}
\qquad
\boxed{a=ca_0.}
\tag{3.1}

代入 `(Gap-square-raw)` 并约去 `c>0`：

\[
\boxed{
5^T a_0G_0
=s\varepsilon\mu^2.
}
\tag{Gap-square-core}

于是

\[
\boxed{
\frac{5^Ta_0G_0}{s\varepsilon}
=\mu^2
\in\mathbf Z_{>0}^2.
}
\tag{3.2}

特别地

\[
\boxed{s\varepsilon\mid5^Ta_0G_0.}
\tag{3.3}

并且对任意 prime `p`：

\[
v_p(a_0)+T\mathbf 1_{p=5}+v_p(G_0)
-v_p(s)-v_p(\varepsilon)
\]

必须是非负偶数。

---

## 4. squarefree-support consequence

若 prime `p` 不整除

\[
5s\varepsilon G_0,
\]

则 `(Gap-square-core)` 在 `p` 处给

\[
\boxed{v_p(a_0)=2v_p(\mu),}
\]

所以 `v_p(a_0)` 必为偶数。

因此 `a_0` 的 squarefree kernel没有新的自由 prime support：

\[
\boxed{
\operatorname{rad}(\operatorname{sqfree}(a_0))
\mid
\operatorname{rad}(5s\varepsilon G_0).
}
\tag{Squarefree-support}

这里 `sqfree(a_0)` 表示 `a_0` 的平方自由核；该结论只控制 prime support，
不把它误计成新的线性高度。

---

## 5. pure common-scale specialization

在 `Final-5-lock` 的 pure common mode：

\[
q_5=n_5=0,
\qquad
m=4g_5,
\qquad
T=2g_5.
\]

若同时位于 LP 的 2-adic worst face `mathfrak q=0`，则 source factor `q` 是
10-unit，因此

\[
\boxed{s=1.}
\]

`b_3` 为 5-adic maximum，故 `c_3=q_lcm/b_3` 为 5-unit；于是
`epsilon,c` 均为 5-units。`v_5(a)=0` 给 `a_0` 为 5-unit，而 high-funnel
recovery ledger给

\[
v_5(G_0)=n_5=0,
\qquad
v_5(\mu)=g_5.
\]

因此 `(Gap-square-core)` 除以 `5^{2g_5}` 后得到

\[
\boxed{
 a_0G_0
=\varepsilon
\left(\frac{\mu}{5^{g_5}}\right)^2.
}
\tag{Pure-gap-square}

这比单纯的 5-adic square-class Hensel 更强：它是一个**全局整数 square-core equation**。

---

## 6. 方法边界

`(Gap-square-core)` 本身还没有关闭 pure common-scale branch，因为
`G_0` 与 `epsilon` 可以携带补偿 squarefree support。

但它把下一问题从“继续做更深的 5-adic unit lifting”改写成一个明确的全局
factor-allocation 问题：

1. `G_0|2G N_12`，所以 recovery gcd 的 prime support受前缀 norm控制；
2. `epsilon=(c_3,u+v)`，所以另一份 squarefree support来自 denominator/projective overlap；
3. 除这两个载体外，`a_0` 的所有 prime exponent都必须为偶数。

下一步应研究 `G_0` 与 `epsilon` 的 common/exclusive support，或从
`Pure-gap-square` 构造一个 normalized squarefree divisor并与 digit/sphere
height联立。

---

## 7. 状态摘要

- **`已严格完成`**：`Gap-square-raw`、`Gap-square-core`、squarefree-support。
- **`结构压缩`**：pure common 的 gap quotient被压成 `a_0 G_0 = epsilon * square`。
- **`待证`**：`G_0 / epsilon` 的 squarefree allocation；`Final-5 + 2-short`；
  sector-to-global reoptimization；DD 全局空性。
