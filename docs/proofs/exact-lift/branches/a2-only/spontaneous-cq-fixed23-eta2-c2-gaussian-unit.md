# A2 fixed `23` `eta=2` `c=2` 的 Gaussian quotient unit collapse

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`endpoint-lattice.md` §§16.8–16.14。
>
> **严格状态：**唯一 `v_23(c_Q)=2` high-2 类型 `(d,c_Q,k_h,slot)=(1,1587,1,+)` 具有 `k_h=1`。将这一固定值代入 endpoint 的共同 Gaussian divisor reduction，立即强迫 `delta=0` 且 quotient `G_5` 为 Gaussian unit。于是抽象的 `B_5,G_5` composition 完全具体化：原 prefix Gaussian integer `a_2+iC_0` 精确分解为 `(r_-+iR_3)(r_++iR_1)`；同时 Gaussian Hensel kernel化成一个显式随 `lambda` 增长的 linear form `c_u-c_+omega(r_++iR_1)`。本文尚未证明该 linear form不可能具有所需的不对称 `(1,lambda-1)` Gaussian depth，因此不关闭 A2，但删除了该类型中剩余的 abstract quotient-factor freedom。

---

## 1. endpoint Gaussian reduction

沿用 `endpoint-lattice.md`。reflection high-2 中定义

\[
Z_r:=r_-+i\varepsilon R_3,
\qquad
Z_a:=a_2+iC_0.
\]

令

\[
\nu_5:=\lambda-2d.
\]

存在 `pi_iota in {2+i,2-i}` 使

\[
Z_r=\pi_\iota^{\nu_5}\mathcal R_5,
\qquad
Z_a=\pi_\iota^{\nu_5}\mathcal A_5,
\]
且

\[
N(\mathcal R_5)=k_hX,
\qquad
N(\mathcal A_5)=XY.
\tag{1.1}

endpoint §16.12 再定义

\[
\delta:=v_3(X)\bmod2\in\{0,1\}
\]
及共同 Gaussian divisor `alpha_X^sharp`，满足

\[
\mathcal A_5=\alpha_X^\sharp\mathcal B_5,
\qquad
\mathcal R_5=\alpha_X^\sharp\mathcal G_5,
\tag{1.2}

\[
N(\alpha_X^\sharp)=3^\delta X,
\]

\[
\boxed{
N(\mathcal B_5)=\frac{Y}{3^\delta},
\qquad
N(\mathcal G_5)=\frac{k_h}{3^\delta}.}
\tag{1.3}

composition identity 为

\[
\boxed{
\varepsilon r_+-iR_1
=3^\delta\mathcal G_5\overline{\mathcal B_5}.}
\tag{1.4}

---

## 2. `k_h=1` 强迫 `delta=0`

当前 fixed-`23` type 为

\[
\boxed{
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1).}
\tag{2.1}

由 (1.3)：

\[
N(\mathcal G_5)=3^{-\delta}.
\]

左边是 Gaussian integer 的非负整数 norm，而 `mathcal G_5` 非零。因此 `delta=1` 会给 `1/3`，不可能。故

\[
\boxed{\delta=0.}
\tag{2.2}

于是

\[
\boxed{N(\mathcal G_5)=1.}
\tag{2.3}

Gaussian 整数中 norm `1` 的元素只有 units：

\[
\boxed{
\mathcal G_5=:u\in\{\pm1,\pm i\}.}
\tag{2.4}

所以该 type 中 endpoint §16.12 的 quotient `G_5` 没有任何非平凡 prime content。

---

## 3. 原 prefix Gaussian integer得到精确二因子分解

由 (1.2) 与 (2.4)：

\[
\mathcal R_5=\alpha_X^\sharp u,
\qquad
\mathcal A_5=\alpha_X^\sharp\mathcal B_5.
\]
因此

\[
\frac{\mathcal A_5}{\mathcal R_5}
=u^{-1}\mathcal B_5.
\tag{3.1}

另一方面 (1.4) 在 `delta=0` 时为

\[
\varepsilon r_+-iR_1
=u\overline{\mathcal B_5}.
\]
取共轭：

\[
\varepsilon r_++iR_1
=\bar u\mathcal B_5
=u^{-1}\mathcal B_5.
\tag{3.2}

与 (3.1) 比较：

\[
\boxed{
\mathcal A_5
=\mathcal R_5(\varepsilon r_++iR_1).}
\tag{3.3}

乘回共同的 `pi_iota^{nu_5}`：

\[
\boxed{
Z_a=Z_r(\varepsilon r_++iR_1).}
\tag{3.4}

当前 `varepsilon=+1`，所以得到完全显式的整数 Gaussian factorization

\[
\boxed{
 a_2+iC_0
=(r_-+iR_3)(r_++iR_1).}
\tag{3.5}

展开两坐标：

\[
\boxed{
a_2=r_-r_+-R_3R_1,}
\tag{3.6a}

\[
\boxed{C_0=r_-R_1+r_+R_3.}
\tag{3.6b}

取范数则恢复

\[
N_0
=(r_-^2+R_3^2)(r_+^2+R_1^2)
=5^{\nu_5}XY,
\]
与已有 norm transfer一致。

(3.5) 的意义在于：此前 endpoint 中“共同 divisor约去后 quotient 是否仍有复杂 Gaussian prime allocation”的问题，在该 fixed type 上完全消失。quotient 已经是显式向量 `r_++iR_1`。

---

## 4. abstract Gaussian Hensel kernel具体化

endpoint §16.13 有

\[
\boxed{
\pi_\iota^d\bar\pi_\iota^{\nu_5+d}
\mid
c_u\mathcal G_5
-\varepsilon c_+\omega\mathcal B_5.}
\tag{4.1}

当前

\[
d=1,
\qquad
\nu_5=\lambda-2,
\qquad
\varepsilon=+1,
\qquad
\mathcal G_5=u.
\]

由 (3.2)：

\[
\mathcal B_5=u(r_++iR_1).
\tag{4.2}

代入 (4.1) 并约去 Gaussian unit `u`：

\[
\boxed{
\pi_\iota\bar\pi_\iota^{\lambda-1}
\mid
c_u-c_+\omega(r_++iR_1).}
\tag{4.3}

其 modulus norm 为

\[
\boxed{
N\!\left(\pi_\iota\bar\pi_\iota^{\lambda-1}\right)
=5^\lambda.}
\tag{4.4}

因此原来的 abstract quotient-Hensel condition 被压成一个明确 Gaussian linear form：

\[
\boxed{
\mathcal L_5
:=c_u-c_+\omega(r_++iR_1).}
\tag{4.5}

它必须具有不对称 Gaussian depth

\[
v_{\pi_\iota}(\mathcal L_5)\ge1,
\qquad
v_{\bar\pi_\iota}(\mathcal L_5)\ge\lambda-1.
\tag{4.6}

而 endpoint §16.14 的短 orientation 精确性进一步给

\[
\boxed{v_{\pi_\iota}(\mathcal L_5)=1.}
\tag{4.7}

所以所有随高度增长的额外 depth 全部集中到 `bar pi_iota` 一侧。

---

## 5. exact quotient form

endpoint §16.14 还给

\[
\mathcal M_5
=\pi_\iota^d\bar\pi_\iota^{\nu_5+d}\mathcal W_5.
\]

在当前 unit collapse 后可吸收 `u` 到 `mathcal W_5`，得到某个

\[
\mathcal W_5^\sharp\in\mathbb Z[i]
\]
使

\[
\boxed{
 c_u-c_+\omega(r_++iR_1)
=
\pi_\iota\bar\pi_\iota^{\lambda-1}
\mathcal W_5^\sharp,}
\tag{5.1}

并且

\[
\boxed{\pi_\iota\nmid\mathcal W_5^\sharp.}
\tag{5.2}

取 norm：

\[
\boxed{
(c_u-c_+\omega r_+)^2
+(c_+\omega R_1)^2
=5^\lambda N(\mathcal W_5^\sharp).}
\tag{5.3}

这已经不含 `alpha_X^sharp,G_5,B_5` 等抽象共同-divisor变量。

---

## 6. 更新后的 closure target

对 `(1,1587,1,+)`，已有两条 local no-go：

1. fixed `23` 的 prefix/additive/high-2 blow-up 在第二层后 smooth；
2. fixed `23^4` orientation residue相对于 `C` 实区间太短，单独没有排除力。

本文进一步把 growing Gaussian modulus压成具体 linear form (4.5)。所以该 type 后续真正的统一目标可写成：

\[
\boxed{
\pi_\iota\bar\pi_\iota^{\lambda-1}
\mid
c_u-c_+\omega(r_++iR_1),
\qquad
v_{\pi_\iota}=1.}
\tag{6.1}

要继续推进，应把 (6.1) 与下面至少一项联立：

- `r_+,R_1` 的 exact endpoint / decimal expressions；
- `c_Q=1587` 对 `c_+` 的有限 divisor choices；
- source Hensel 的 `omega` natural representative；
- 或 (3.5) 的 exact Gaussian factorization 与 prefix digit window。

这里已经没有剩余的 abstract Gaussian quotient prime allocation；开放项是一个显式、随 `lambda` 线性增深的 Gaussian approximation problem。