# A1 minimal diagonal: third-digit window selects the large conjugate factor

> 日期：2026-08-22。
>
> 依赖：`decimal-height-synchronization.md`、`sharp-positive-tail-window`、`diagonal.md`、`global-squarefree-terminal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge。

状态：**本文结论已严格完成；top edge 尚未整体关闭。**

---

## 1. normalized third-numerator roots

令

\[
T=10^k,
\qquad
\rho:=\frac{b_3}{10^n}.
\]

minimal diagonal 中

\[
D=TQ,
\qquad
G=b_1.
\]

`decimal-height-synchronization.md` 的两个 normalized roots 为

\[
\boxed{
x_\pm
=\frac{
\kappa G^2C\pm(\kappa+G)W
}{
\kappa^2(\kappa+2G)
}.}
\tag{1}
\]

真实第三块若存在，则

\[
\boxed{x=\frac{a_3}{10^n}}
\tag{2}
\]

并且第三分子恰有 `n` 位，所以

\[
\boxed{\frac1{10}\le x<1.}
\tag{3}
\]

另一方面 A1 tail normalization 给

\[
\kappa=\frac{DG}{\rho}.
\tag{4}
\]

因此由 (1) 两根相加：

\[
\boxed{
x_++x_-
=\frac{2G^2C}{\kappa(\kappa+2G)}
=\frac{2\rho^2C}{D(D+2\rho)}.}
\tag{5}
\]

---

## 2. root sum 在当前 frontier 上远大于 2

sharp positive-tail window 写成

\[
\Gamma=T(N_0-\rho),
\qquad
0<\Gamma<39.003.
\]

而 `N0` 是 `k` 位整数：

\[
N_0\ge T/10.
\]

所以

\[
\rho
=N_0-\Gamma/T
>\frac T{10}-\frac{39.003}{T}.
\]

对当前 `T>=10^32`，安全地有

\[
\boxed{\rho>T/11.}
\tag{6}
\]

minimal diagonal 显式式为

\[
a_1
=100T^3+(5-z-w)10T+j
\]

其中 `j>=0`，故

\[
a_1\ge100T^3.
\]

又

\[
C=10T^2a_1+a_2,
\qquad a_2>0,
\]

所以

\[
\boxed{C>1000T^5.}
\tag{7}
\]

同时

\[
Q=100T^2-(10w-1)<100T^2,
\]

故

\[
\boxed{D<100T^3.}
\tag{8}
\]

因为 `rho<N0<T`：

\[
D+2\rho<100T^3+2T<101T^3.
\tag{9}
\]

代入 (5)：

\[
\begin{aligned}
x_++x_-
&>\frac{2(T/11)^2(1000T^5)}{(100T^3)(101T^3)}\\
&=\frac{2000}{1\,222\,100}T.
\end{aligned}
\tag{10}
\]

当前 `T>=10^32`，右端显然严格大于 `2`。因此

\[
\boxed{x_++x_->2.}
\tag{11}
\]

---

## 3. 实际 decimal root 必是较小根

若 `W=0`，则两个 roots 相等；由 (11) 每个都大于 1，与 (3) 矛盾。所以任意真实 candidate 必有

\[
W>0,
\]

从而

\[
x_-<x_+.
\]

若真实 root 是 `x_+`，则由 `x_- >0`（真实 sphere/contact candidate 的两个 tail-gap roots 为正）以及 (11) 并不能单独排除；更直接地，假设某一 root `x_sigma` 满足 (3)。另一 root 为

\[
x_{-\sigma}=(x_++x_-)-x_\sigma>2-1=1.
\]

因此**至多较小的一个 root**可以落入 `[1/10,1)`。由于 `x_-<x_+`，实际 root 必为

\[
\boxed{x=x_-.}
\tag{12}
\]

（如果另一个形式 root 非正，则结论更直接；(12) 只使用候选 root 自身满足 (3) 与 root ordering。）

---

## 4. 翻回 squarefree conjugate factor：实际必取 `V`

写 squarefree decomposition

\[
\boxed{\kappa=s_0r^2,}
\qquad s_0\text{ squarefree},
\tag{13}
\]

并由 square terminal 写

\[
W=s_0r w_0.
\]

定义

\[
U=GCr-w_0,
\qquad
V=GCr+w_0,
\qquad0<U<V.
\tag{14}
\]

定理 11.54 / `global-squarefree-terminal.md` 中 tail-gap

\[
t:=G(H_r-r_3)=\frac\mu\nu
\]

的两个 roots 为

\[
\boxed{
t_\pm
=\frac{G\kappa C\pm W}{D(\kappa+2G)}
=\frac{s_0r\,(GCr\pm w_0)}{D(s_0r^2+2G)}.}
\tag{15}
\]

而

\[
r_3
=\frac CD-t\left(\frac1\kappa+\frac1G\right).
\tag{16}
\]

所以 `t` 越大，`r3` 越小。由 (15)，`t_+>t_-`，故较小的第三根 `r3`、也就是较小 normalized root `x_-`, 恰对应 `t_+`。

因此实际共轭因子不是 `U`，而被 digit window 全局固定为

\[
\boxed{J=V=GCr+w_0.}
\tag{17}
\]

因为 `0<w0<GCr`，立即有

\[
\boxed{GCr<J<2GCr.}
\tag{18}
\]

---

## 5. consequence

此前 local terminal theorems 11.57--11.61 只说“实际选中的 `J in {U,V}`”满足逐素数赋值律。本文把这一自由度删除：在当前 top edge，所有 prime allocations 必须同时发生在同一个大共轭因子

\[
\boxed{J=V.}
\]

后续应把：

1. `J=V` 的实高度窗 (18)；
2. theorem 11.60 对 `p|b1` 的 complete cancellation；
3. theorem 11.61 对 `p|Q` 的三支赋值；
4. exact decimal recovery equation
   \[
   10^nG_0D_J^2=2s_0^2r^3J(s_0r^2+2G)
   \]

联立，寻找实际 `V` 上不能同时承载的 prime mass。