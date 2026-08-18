# A2 repeated spontaneous 与 `Psi_f` pure-prefix overlap

> **依赖：** `spontaneous-tangent-decimal.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md` §§16.49–16.51。
>
> **严格状态：**本文只处理 repeated spontaneous prime 同时满足 `Psi_f=0` 的 **pure-prefix overlap**。这不是一般 `f`-denominator carrier 的同义词；一般 denominator contact 仍由 `f` 与 `R_f` 控制，另见 `spontaneous-tangent-f-denominator.md`。在 `Psi_f` overlap 上，prefix 被固定到 `18K-29=0`。若再额外假设同一个 prime 也整除 `f`，则旧 `f`-curvature kernel 可完全显式化，并证明 curvature character 只是旧 principal-square shadow。本文仍**不宣称 A2 全局关闭**。

---

## 1. repeated spontaneous + `Psi_f` 只剩 `18K-29=0`

已有 exact identity

\[
\mathcal R_{\rm tan}^{\rm int}+9\Psi_f
=B^2(2K-9)(18K-29).
\tag{1.1}
\]

若 genuine noncentral repeated prime `p` 满足

\[
p\mid\mathcal R_{\rm tan}^{\rm int},
\qquad p\mid\Psi_f,
\qquad p\nmid B(2K-9),
\]
则

\[
\boxed{18K-29\equiv0\pmod p.}
\tag{1.2}
\]

repeated tangent line

\[
L_{\rm tan}=9(TK-a_3)-55T
\]
随后给

\[
\boxed{
K\equiv\frac{29}{18},
\qquad
\frac{a_3}{T}\equiv-\frac92
\pmod p.}
\tag{1.3}
\]

并且

\[
9\alpha\equiv T(18K-55)\equiv-26T,
\]
所以 non-`3` inert prime `p!=13` 时仍有

\[
\boxed{p\nmid\alpha.}
\tag{1.4}
\]

因此这一 overlap 不会偷偷退回 height/common-`alpha` channel。

---

## 2. 若再额外进入 `f` denominator，则 `f`-channel 自身不能 double-root

本节额外加入

\[
p\mid f.
\tag{2.1}
\]

旧 `f`-channel double-root 必须满足

\[
K\equiv9+2a_3T^{-1}.
\tag{2.2}
\]

由 (1.3)，右边等于

\[
9+2(-9/2)=0.
\]

若 (2.2) 与 `18K=29` 同时成立，只能 `p=29`；但

\[
29\equiv1\pmod4.
\]

故对 odd inert prime：

\[
\boxed{
\text{repeated}+\Psi_f+f
\Longrightarrow
f\text{-channel 为 simple root}.}
\tag{2.3}
\]

注意这只是 triple overlap 的结论，不是对所有 `f`-denominator repeated spontaneous 状态的证明。

---

## 3. triple overlap 上 `R_23=13T^2`

旧 form

\[
\mathscr R_{23}=2a_3^2+9Ta_3+13T^2
\]
在 (1.3) 上给

\[
\boxed{\mathscr R_{23}=13T^2\pmod p.}
\tag{3.1}
\]

---

## 4. `f=0` 与 `Psi_f=0` 的 source-scale 消元

沿用

\[
B=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}c_Qq,
\]

\[
N_0=5^{\lambda-2d}XY,
\qquad
m=\lambda+d,
\qquad
A_f=2^m5^dg^2.
\]

`p|f` 给

\[
5^\lambda q\equiv-2c_u,
\qquad
q^2\equiv\frac{4c_u^2}{5^{2\lambda}}.
\tag{4.1}
\]

而 `Psi_f=0` 给

\[
Q^2N_0=B^2(K^2-26).
\]
在 `K=29/18`：

\[
K^2-26=-\frac{7583}{324}.
\]

逐项代入并用 `m=lambda+d`：

\[
\boxed{
c_Q^2XY
=-\frac{7583}{1296}A_fT
\pmod p.}
\tag{4.2}
\]

---

## 5. `R_{23,f}` 塌成 square-times-`A_f`

旧 discriminant kernel

\[
\mathscr R_{23,f}
=A_f\mathscr R_{23}+2Tc_Q^2XY.
\]

由 (3.1)、(4.2)：

\[
\boxed{
\mathscr R_{23,f}
=\frac{841}{648}A_fT^2
=\frac{29^2}{2^3 3^4}A_fT^2
\pmod p.}
\tag{5.1}
\]

在 genuine `p|f` 下有 `p∤10g`，且 inert `p!=29`，故

\[
\boxed{p\nmid\mathscr R_{23,f}.}
\tag{5.2}
\]

所以 triple overlap 中的 `f` root 确实 simple。

---

## 6. curvature character 是旧 principal-square shadow

因为

\[
A_f=2^m5^dg^2,
\]
而 `29^2,T^2,3^4,g^2` 都是平方，(5.1) 给

\[
\boxed{
\left(\frac{\mathscr R_{23,f}}p\right)
=
\left(\frac2p\right)^{m+3}
\left(\frac5p\right)^d.
}
\tag{6.1}
\]

这与旧 simple `f`-channel character 完全相同。因此在

\[
\text{repeated spontaneous}+\Psi_f+f
\]
子通道中，curvature character 不提供独立 obstruction：

\[
\boxed{
\text{new-looking curvature condition}
=\text{old principal-square shadow}.}
\tag{6.2}
\]

---

## 7. 证明边界

本文严格完成的是：

1. repeated + `Psi_f` overlap 固定 `18K-29=0`；
2. 若再加入 `p|f`，则 `f`-channel 只能 simple；
3. triple overlap 的 `R_{23,f}` 与 character 完全显式化并降级。

**没有**证明一般 `p|f` 的 repeated spontaneous carrier 必满足 `Psi_f=0`。一般 denominator overlap 必须从 `F_f/Omega -> Delta_0` 直接处理，不能把本文件结果外推。
