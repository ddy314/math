# A2 repeated spontaneous 与 `f`-denominator overlap 审计

> **依赖：** `spontaneous-tangent-decimal.md`、`spontaneous-angle.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md` §§16.49–16.51。
>
> **严格状态：**本文处理 genuine repeated spontaneous prime 若同时回流到 `f`-denominator channel 的唯一剩余可能。首先由 tangent 与 `Psi_f` 把 prefix 固定到 `18K-29=0`，再利用 `f=0`、`Psi_f=0`、source scales 把 `R_{23,f}` 完全显式化。结论是：该 overlap 中 `f`-channel 必为 simple root，且其 curvature character 恰好自动等于旧 (16.320) 的 principal-square shadow；不能重复收费成新 obstruction。本文仍**不宣称 A2 全局关闭**。

---

## 1. repeated spontaneous + f-prefix 只剩 `18K-29=0`

`spontaneous-tangent-decimal.md` 已证明

\[
\mathcal R_{\rm tan}^{\rm int}+9\Psi_f
=B^2(2K-9)(18K-29).
\tag{1.1}
\]

对 genuine noncentral repeated prime：

\[
p\mid\mathcal R_{\rm tan}^{\rm int},
\qquad p\mid\Psi_f,
\qquad p\nmid B(2K-9),
\]
所以

\[
\boxed{18K-29\equiv0\pmod p.}
\tag{1.2}
\]

同时 repeated tangent 原始线为

\[
L_{\rm tan}=9(TK-a_3)-55T.
\]
故 `p|L_tan` 与 (1.2) 给

\[
\boxed{
K\equiv\frac{29}{18},
\qquad
\frac{a_3}{T}
\equiv K-\frac{55}{9}
=-\frac92
\pmod p.}
\tag{1.3}
\]

这里 `p` 为 non-`3` inert prime，所以 `p!=29`。

---

## 2. `已严格完成`：`f`-channel 自己绝不可能同时 double-root

旧 `f`-channel 的 double-root 条件为

\[
\boxed{
K\equiv9+2a_3T^{-1}\pmod p.}
\tag{2.1}
\]

代入 (1.3)：

\[
9+2\left(-\frac92\right)=0.
\]

所以若 `f`-channel 也 double-root，就必须

\[
K\equiv0\pmod p.
\]
但 (1.3) 又要求

\[
18K\equiv29.
\]
因此只能 `p=29`，而

\[
29\equiv1\pmod4
\]
不是 odd inert carrier。故

\[
\boxed{
\text{repeated spontaneous}\cap f\text{-denominator}
\Longrightarrow
f\text{-channel 本身为 simple root}.}
\tag{2.2}
\]

一个 inert prime 不可能在 spontaneous branch 与 denominator branch 两边同时发生 repeated degeneration。

---

## 3. `已严格完成`：固定线上的 `R_23` 只剩 `13T^2`

旧 numerator curvature form 为

\[
\mathscr R_{23}
=2a_3^2+9Ta_3+13T^2.
\tag{3.1}
\]

在 (1.3) 上：

\[
\begin{aligned}
\mathscr R_{23}
&=T^2\left(
2\frac{81}{4}
-\frac{81}{2}
+13
\right)\\
&=13T^2.
\end{aligned}
\]

因此

\[
\boxed{
\mathscr R_{23}\equiv13T^2\pmod p.}
\tag{3.2}
\]

---

## 4. `已严格完成`：`f=0` 与 `Psi_f=0` 完全消去 source scale

沿用 source formulas

\[
B=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}c_Qq,
\tag{4.1}
\]

\[
N_0=5^{\lambda-2d}XY,
\qquad
m=\lambda+d,
\tag{4.2}
\]
以及

\[
A_f:=2^m5^dg^2.
\tag{4.3}
\]

`f`-denominator 条件为

\[
f=5^\lambda q+2c_u\equiv0,
\]
所以

\[
\boxed{q^2\equiv\frac{4c_u^2}{5^{2\lambda}}.}
\tag{4.4}
\]

另一方面 `Psi_f=0` 给

\[
Q^2N_0=B^2(K^2-26).
\tag{4.5}
\]

在 `K=29/18`：

\[
K^2-26
=\frac{29^2-26\cdot18^2}{18^2}
=-\frac{7583}{324}.
\tag{4.6}
\]

把 (4.1)–(4.4) 代入 (4.5)：

\[
\begin{aligned}
c_Q^2XY
&=\frac{c_Q^2N_0}{5^{\lambda-2d}}\\
&=-\frac{7583}{1296}
\,2^{2m}5^{\lambda+2d}g^2.
\end{aligned}
\]

而

\[
A_fT
=(2^m5^dg^2)(2^m5^m)
=2^{2m}5^{\lambda+2d}g^2.
\]

所以得到完全 source-free 的比例：

\[
\boxed{
c_Q^2XY
=-\frac{7583}{1296}A_fT
\pmod p.}
\tag{4.7}
\]

---

## 5. `已严格完成`：`R_{23,f}` 精确塌成 square-times-`A_f`

旧 `f`-channel discriminant kernel 为

\[
\mathscr R_{23,f}
=A_f\mathscr R_{23}+2Tc_Q^2XY.
\tag{5.1}
\]

代入 (3.2)、(4.7)：

\[
\begin{aligned}
\mathscr R_{23,f}
&=A_fT^2
\left(
13-\frac{7583}{648}
\right)\\
&=\frac{841}{648}A_fT^2.
\end{aligned}
\]

即

\[
\boxed{
\mathscr R_{23,f}
=\frac{29^2}{2^3 3^4}A_fT^2
\pmod p.}
\tag{5.2}
\]

因为 genuine `p|f` 已有

\[
\gcd(p,10g)=1,
\]
且 `p!=3,29`，(5.2) 立即给

\[
\boxed{p\nmid\mathscr R_{23,f}.}
\tag{5.3}
\]

这从 discriminant kernel 本身再次证明 §2：`f`-channel 必为 simple root。

---

## 6. `已严格完成 / 降级`：curvature character 完全是旧 shadow

旧 simple `f`-channel character 为

\[
\left(\frac{\mathscr R_{23,f}}p\right)
=
\left(\frac2p\right)^{m+3}
\left(\frac5p\right)^d.
\tag{6.1}
\]

由 (5.2)，`29^2,T^2,3^4,g^2` 都是平方；而

\[
A_f=2^m5^dg^2.
\]
所以

\[
\begin{aligned}
\left(\frac{\mathscr R_{23,f}}p\right)
&=
\left(\frac{2^{-3}A_f}{p}\right)\\
&=
\left(\frac2p\right)^{m+3}
\left(\frac5p\right)^d,
\end{aligned}
\tag{6.2}
\]

其中指数 `-3` 与 `+3` 具有相同 parity。

因此 (6.1) 在 repeated spontaneous/f-overlap 中**自动恒等成立**。它不提供新的 independent character obstruction：

\[
\boxed{
\text{repeated-f curvature character}
=\text{旧 principal-square shadow}.}
\tag{6.3}
\]

所以后续不应再沿这条 Legendre 路线尝试闭环。

---

## 7. 更新后的 `f`-overlap 核

如果 genuine inert repeated spontaneous carrier 同时来自 `f` denominator，则已经严格固定为

\[
\boxed{
18K-29=0,
\qquad
\frac{a_3}{T}=-\frac92,
\qquad
\Delta_0=0,
}
\]

其中最后一式来自旧

\[
\operatorname{Res}_{r_s}(F_f,\Omega_{\rm sp})
=-200x^3\Delta_0.
\]

并且：

- `f`-channel 自身一定 simple；
- `R_{23,f}` 为显式单位；
- curvature character 自动耗尽，没有新矛盾。

因此真正剩余的 denominator-overlap 问题已降为固定的 pure-prefix 系统

\[
18K-29=0,
\qquad
\Delta_0=0,
\qquad
\mathscr R_{\rm tan}=0,
\]

而不是任意 source/curvature branch。下一步若继续此支，应直接对这三个 prefix 方程做 resultant / decimal-orbit 审计，而不是继续研究 `-23` character。
