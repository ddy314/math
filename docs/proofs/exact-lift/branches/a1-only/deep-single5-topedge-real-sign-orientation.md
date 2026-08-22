# A1 minimal diagonal: single-5 top-edge real sign orientation

> 日期：2026-08-22。
>
> 依赖：`global-squarefree-terminal.md`、`decimal-height-synchronization.md`、minimal-diagonal digit bounds。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge。

状态：**本文严格证明真正 decimal third block 只能来自负号形式根 `sigma=-1`。** top edge 尚未整体关闭。

---

## 1. 统一 root formula

沿用

\[
P=\frac{C}{D_c},
\qquad
D_c=TQ,
\qquad
\theta=\frac G\kappa,
\]

其中 `T=10^k`，并且

\[
QG<\kappa\le10QG.
\]

所以

\[
\boxed{
\frac1{10Q}\le\theta<\frac1Q.
}
\tag{1}
\]

判别根记为 `z>=0`。两个形式第三根为

\[
r_\sigma
=\frac{\theta P+\sigma(1+\theta)z}{1+2\theta},
\qquad \sigma\in\{+1,-1\}.
\tag{2}
\]

normalized decimal numerator 是

\[
\boxed{x_\sigma=\rho r_\sigma,}
\qquad
\rho=\frac ML=TQ\theta.
\tag{3}
\]

合法第三块必须满足

\[
\boxed{\frac1{10}\le x_\sigma<1.}
\tag{4}
\]

---

## 2. 正号根无条件过大

因为 `z>=0`，由 (2)：

\[
r_+
\ge\frac{\theta P}{1+2\theta}.
\]

由 `Q>1` 与 (1)，有 `theta<1`，故安全地

\[
1+2\theta<3.
\]

因此

\[
r_+>rac{\theta P}{3}.
\]

乘以 `rho=TQ theta`：

\[
x_+
>\frac{TQ\theta^2P}{3}.
\]

再用 `theta>=1/(10Q)`：

\[
x_+
\ge\frac{TP}{300Q}.
\]

而 `P=C/(TQ)`，所以

\[
\boxed{
x_+>\frac{C}{300Q^2}.
}
\tag{5}
\]

minimal diagonal 中

\[
a_1
=100T^3+(5-z-w)10T+j
>100T^3,
\]

且第二分子为正，所以

\[
C=10T^2a_1+a_2>1000T^5.
\tag{6}
\]

同时

\[
Q=100T^2-(10w-1)<100T^2.
\tag{7}
\]

由 (5)-(7)：

\[
x_+
>\frac{1000T^5}{300\cdot10^4T^4}
=\frac{T}{3000}.
\tag{8}
\]

当前 `k>=32`，故 `T=10^k>3000`，于是

\[
\boxed{x_+>1.}
\tag{9}
\]

这与 decimal window (4) 矛盾。

因此任意真正 candidate 必须使用

\[
\boxed{\sigma=-1.}
\tag{10}
\]

注意本证明完全不需要判断 `z` 的大小；只用正号根中不可消失的 `theta P` 项。

---

## 3. 对 top-edge sign-allocation 的意义

此前 `deep-single5-decimal-height-collapse.md` 只证明两个 2-adic signs 中有一个 shallow、一个 high，但没有把 high sign 与代数符号 `+/-` 对齐。

本文说明真实 third block 必须是 `X_-`。因此若 top-edge candidate 存在，则必须有

\[
\boxed{
v_2(X_-)=n+3e+1,}
\tag{11}
\]

而

\[
\boxed{
v_2(X_+)=3e+2.}
\tag{12}
\]

这里使用 top-edge 已有

\[
v_2(Y)=n+3e+2
\]

以及 reduced 2-denominator depths `{1,n}`。

所以后续所有 5-adic `full/matching` 判断也必须针对同一个固定代数 sign `X_-`，不能再交换两根来分别满足 2-adic 与 5-adic 条件。