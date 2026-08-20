# DD canonical `t_2=1` recovery gcd 的 squarefree lock

> **依赖：** `core.md` 的 gap 定义、overlap 参数化、primitive recovery
> \(10^mQG_0=2\kappa\mu\nu\)，以及
> [`high-funnel-exact-small-factor-normalization.md`](high-funnel-exact-small-factor-normalization.md)
> 中对 source `q` / reduced `q_red` 的严格区分。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 本文显式恢复 reduced gap ratio `mu/nu`，并得到
> \[
> \boxed{
> h^2G_0=2\varepsilon^3Lc^4r_*^2a_0,
> }
> \]
> 其中
> \[
> h=(\varepsilon Lc^2r_*a_0,q_0).
> \]
> 因而
> \[
> \boxed{
> \operatorname{sqf}(G_0)
> =\operatorname{sqf}(2\varepsilon La_0).
> }
> \]
> pure common sheet上更化为
> \[
> \boxed{
> \operatorname{sqf}(G_0)=\operatorname{sqf}(\varepsilon a_0).
> }

---

## 1. gap ratio 的显式分数

整数球面提升给

\[
\mathcal R=H/q_{\rm lcm},
\qquad
r_3=y_3/q_{\rm lcm}.
\]

因此

\[
\mathcal R-r_3
=\frac{H-y_3}{q_{\rm lcm}}
=\frac{La}{q_{\rm lcm}}.
\]

unified quadratic中定义

\[
\boxed{
G(\mathcal R-r_3)=\frac\mu\nu,
\qquad (\mu,\nu)=1.
}
\tag{1.1}

primitive exact-lift parameterization为

\[
q_{\rm lcm}=Dq_0,
\qquad
D=Vc\lambda,
\]

而 overlap 参数化给

\[
G=\varepsilon Vc^2\lambda r_*,
\qquad
a=ca_0.
\]

所以

\[
\begin{aligned}
G(\mathcal R-r_3)
&=\frac{GLa}{Dq_0}\\
&=\frac{\varepsilon Vc^2\lambda r_*\,Lca_0}
{Vc\lambda q_0}\\
&=\boxed{
\frac{\varepsilon Lc^2r_*a_0}{q_0}.}
\end{aligned}
\tag{Gap-ratio-explicit}

定义

\[
\boxed{
N_\mu:=\varepsilon Lc^2r_*a_0,
\qquad
h:=(N_\mu,q_0).
}
\tag{1.2}

由于 `(1.1)` 已是最低项：

\[
\boxed{
\mu=\frac{N_\mu}{h},
\qquad
\nu=\frac{q_0}{h}.}
\tag{mu-nu-explicit}

---

## 2. canonical `t_2=1` 的 auxiliary identities

令

\[
r_0:=2\cdot5^T,
\qquad
s:=(r_0,q),
\]

其中 `Q=Uq` 是 S-unit phase 的 source factor。

`high-funnel-exact-small-factor-normalization.md` 已证明 gcd-normal reduced pair为

\[
L=\frac{r_0}{s},
\qquad
q_{\rm red}=\frac qs.
\]

另一方面 overlap 参数化有

\[
u=LQ_1,
\qquad Q=\eta Q_1,
\]

而 `t_2=1` 给

\[
u=r_0U,
\qquad Q=Uq.
\]

因此

\[
Q_1=sU,
\]

从而

\[
\boxed{q=s\eta,\qquad q_{\rm red}=\eta.}
\tag{2.1}

并且

\[
\boxed{\tau=\eta V.}
\]

此外

\[
G=\gamma V
=\varepsilon Vc^2\lambda r_*
\]

给

\[
\boxed{\gamma=\varepsilon c^2\lambda r_*.}
\tag{2.2}

primitive denominator参数为

\[
\boxed{q_0=\frac{\omega\eta\varepsilon}{\lambda}.}
\tag{2.3}

---

## 3. primitive recovery 把 `G_0` 完全展开

统一 primitive recovery为

\[
\boxed{
10^mQG_0=2\kappa\mu\nu.}
\tag{3.1}

在 canonical phase：

\[
Q=Us\eta,
\qquad
\kappa=\gamma r_0U.
\]

代入 `(3.1)` 并约去 `U`：

\[
10^ms\eta G_0
=2\gamma r_0\mu\nu.
\]

又

\[
\omega=10^m/L=10^ms/r_0,
\]

所以

\[
\boxed{
\omega\eta G_0=2\gamma\mu\nu.}
\tag{3.2}

使用 `(mu-nu-explicit)`：

\[
\mu\nu
=\frac{N_\mu q_0}{h^2}.
\]

再代入

\[
N_\mu=\varepsilon Lc^2r_*a_0,
\quad
q_0=\frac{\omega\eta\varepsilon}{\lambda},
\quad
\gamma=\varepsilon c^2\lambda r_*.
\]

则 `(3.2)` 右侧为

\[
\frac{
2\omega\eta\varepsilon^3Lc^4r_*^2a_0
}{h^2}.
\]

约去 `omega eta`，得到 exact identity

\[
\boxed{
 h^2G_0
=2\varepsilon^3Lc^4r_*^2a_0.
}
\tag{Recovery-square}

---

## 4. squarefree kernel 被完全锁死

对正整数 `N`，记 `sqf(N)` 为删去全部偶次 prime exponent后的平方自由核。

`(Recovery-square)` 两边相差的因子

\[
h^2,\quad c^4,\quad r_*^2
\]

全部是完全平方；而 `epsilon^3` 与 `epsilon` 的 prime-exponent parity相同。
因此逐素数 parity完全相等：

\[
\boxed{
\operatorname{sqf}(G_0)
=\operatorname{sqf}(2\varepsilon La_0).
}
\tag{G0-squarefree-lock}

这不是只有 radical inclusion，而是 squarefree kernel本身的精确相等。

---

## 5. pure common specialization

在 pure common / `mathfrak q=0` endpoint：

\[
q_5=n_5=0,
\quad m=4g_5,
\quad T=2g_5,
\quad s=1.
\]

所以

\[
L=2\cdot5^{2g_5}.
\]

于是

\[
2L=4\cdot5^{2g_5}
=(2\cdot5^{g_5})^2
\]

是完全平方。

`(G0-squarefree-lock)` 因而退化成

\[
\boxed{
\operatorname{sqf}(G_0)
=\operatorname{sqf}(\varepsilon a_0).
}
\tag{Pure-G0-squarefree}

这与 `high-funnel-gap-square-core.md` 的

\[
a_0G_0=\varepsilon\mu_0^2
\]

相容；本文进一步说明这种相容性来自 recovery 的 exact gcd normalization，
不是偶然的 5-adic parity coincidence。

---

## 6. 方法边界

本文把 `G_0` 的**平方自由 support**完全锁死，但没有给 `G_0` 的平方部分高度上界。
所以它不会单独关闭 pure common branch。

真正剩余自由从

\[
\text{arbitrary prime support of }G_0
\]

缩成

\[
\boxed{\text{square depth / Archimedean height inside a fixed support parity pattern}.}
\]

这提示后续不要继续做 radical chasing；应改为：

1. 控制 `h=(N_mu,q_0)` 的高度，或
2. 用 `(Recovery-square)` 比较 `G_0` 与 `epsilon,L,c,r_*,a_0` 的实际大小，或
3. 把 `mu=N_mu/h` 的平方高度送回 `F_-` / digit shell。

---

## 7. 状态摘要

- **`已严格完成`**：`Gap-ratio-explicit`、`mu-nu-explicit`、`q_red=eta`、
  `Recovery-square`、`G0-squarefree-lock`。
- **`结构压缩`**：pure common 中 `G_0` 不再有自由 squarefree support；只剩平方深度/高度。
- **`待证`**：`h` 的 height、`G_0` square depth、全 DD branch reoptimization、DD global closure。
