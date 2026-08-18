# A2 pure-spontaneous repeated tangent 的原始 decimal 接口

> **依赖：** `spontaneous-single-branch.md`、`spontaneous-single-branch-syzygy.md`、`spontaneous-prefix-eliminant.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把两个 sphere orientation 的 repeated-root 条件统一消去，得到一个不含 `z_i,r_s,a_3,b_3` 的 pure-prefix tangent；随后将它乘回原始 decimal integers，并把它与 `Theta_dec`、拼接分子 `alpha`、`R_N`、`Psi_f`、`S_0` 做 exact syzygy。结果把 genuine pure repeated spontaneous prime 与 height/external、q-side contact 严格分离，并把 f-side overlap 压到单一线性 prefix target。最后给出 tangent integer 的精确 `2`-进本原化与 `mod 4` parity law。本文仍**不宣称 A2 全局关闭**。

---

## 1. 两个 sphere orientation 的 repeated tangent 实际是同一条曲线

沿用 compact branch

\[
\mathscr L_i(\tau)
=55\tau^2+18(z_i-s)\tau+s^2-4sz_i-c,
\tag{1.1}
\]

其中

\[
\tau=10^{-M},
\qquad s=9+y,
\qquad
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\tag{1.2}
\]

repeated root 满足

\[
\mathscr L_i(\tau)=0,
\qquad
\mathscr L_i'(\tau)=0.
\]

后者就是

\[
\boxed{55\tau=9(s-z_i).}
\tag{1.3}
\]

所以

\[
z_i=s-\frac{55}{9}\tau.
\]

代回 (1.1)，`z_i` 完全消失：

\[
\boxed{
\mathscr R_{\rm tan}(\tau;x,y)
:=495\tau^2-220s\tau+27s^2+9c
=0.
}
\tag{1.4}
\]

因此 `Q_1,Q_2` 的 repeated-root 风险并不是两套判别式：在 sphere-root denominator 为单位时，两支共享**同一个 pure-prefix tangent**。

---

## 2. `已严格完成`：tangent 与 `C_*` 是同一个正定平方恒等式

`spontaneous-single-branch-syzygy.md` 已证明

\[
23s^2+81c=\frac{C_*}{100x^2}.
\tag{2.1}
\]

对 (1.4) 围绕 central length

\[
\tau_c=\frac{2s}{9}
\]
完成平方：

\[
\begin{aligned}
\mathscr R_{\rm tan}
&=495\left(\tau-\frac{2s}{9}\right)^2
+\frac{23}{9}s^2+9c.
\end{aligned}
\]

结合 (2.1)：

\[
\boxed{
900x^2\mathscr R_{\rm tan}
=C_*+5500x^2(9\tau-2s)^2.
}
\tag{2.2}
\]

这同时解释：

- real endpoint 上 `C_*>0`，故 tangent 无真实根；
- repeated-root character 为 `(C_*/p)=(-55/p)`；
- central line `9tau-2s=0` 与 `C_*` 不是两套无关异常，而是同一 tangent 的两个组成部分。

---

## 3. `已严格完成`：乘回原始 decimal blocks 后只剩一个小整数

令

\[
N=10^M,
\qquad B=b_2,
\qquad A=a_2,
\]

\[
Q=2N+B,
\qquad
K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\tag{3.1}
\]

则

\[
x=\frac BN,
\qquad
y=\frac{10A}{N},
\qquad
s=\frac KN,
\qquad
\tau=\frac1N.
\]

并且

\[
c=\frac{Q^2N_0}{B^2N^2}.
\tag{3.2}
\]

所以 (1.4) 乘 `B^2N^2` 后恰得到整数

\[
\boxed{
\mathcal R_{\rm tan}^{\rm int}
:=B^2(27K^2-220K+495)+9Q^2N_0.
}
\tag{3.3}
\]

以及精确尺度关系

\[
\boxed{
B^2N^2\mathscr R_{\rm tan}
=\mathcal R_{\rm tan}^{\rm int}.
}
\tag{3.4}
\]

因此对 genuine odd prime `p`，`p∤BN` 时：

\[
\boxed{
p\mid\mathscr R_{\rm tan}
\iff
p\mid\mathcal R_{\rm tan}^{\rm int}.}
\tag{3.5}
\]

这就是 repeated moving root 的 source-free 原始 decimal 判据。

---

## 4. `已严格完成`：与 `C_*` 原始整数的精确桥

`spontaneous-cstar-audit.md` 定义

\[
\mathcal C_*^{\rm int}
=23B^2K^2+81Q^2N_0.
\tag{4.1}
\]

直接展开：

\[
\boxed{
9\mathcal R_{\rm tan}^{\rm int}
=
\mathcal C_*^{\rm int}
+55B^2(2K-9)^2.
}
\tag{4.2}
\]

这正是 normalized identity (2.2) 的原始整数版本。

---

## 5. `已严格完成`：原始 tangent line 与拼接分子完全同步

令

\[
T=10^m,
\qquad
\alpha=TK+a_3.
\]

把 compact derivative (1.3) 乘回 `TN`。因为

\[
z_i=\frac{a_3}{TN},
\qquad
s=\frac KN,
\]
其原始整数形式为

\[
\boxed{
L_{\rm tan}
:=9(TK-a_3)-55T.
}
\tag{5.1}
\]

并有 exact identity

\[
\boxed{
9\alpha+L_{\rm tan}
=T(18K-55).
}
\tag{5.2}
\]

所以若 `p∤3T` 且

\[
p\mid L_{\rm tan},
\]
则

\[
\boxed{
p\mid\alpha\iff p\mid18K-55.}
\tag{5.3}
\]

特别地，对本文真正的 pure-spontaneous channel

\[
p\nmid\alpha,
\]
任何 repeated prime 自动满足

\[
\boxed{p\nmid18K-55.}
\tag{5.4}
\]

所以 pure repeated branch 与 external double-root 的线性中心严格互斥；反之 repeated prime 一旦进入 `alpha=W_q omega`，立即回到旧 height/content 线，而不再属于 pure spontaneous。

---

## 6. `已严格完成`：`Theta_dec`、tangent 与 `R_tan` 的三项 syzygy

`spontaneous-prefix-eliminant.md` 已有

\[
\Theta_{\rm dec}
=T\mathcal R_\Theta
-2B^2(2K-9)a_3,
\]

其中

\[
\mathcal R_\Theta
=B^2(K^2-18K+55)-Q^2N_0.
\]

与 (3.3)、(5.1) 直接展开得到

\[
\boxed{
9\Theta_{\rm dec}
+T\mathcal R_{\rm tan}^{\rm int}
=2B^2(2K-9)L_{\rm tan}.
}
\tag{6.1}
\]

因此 genuine noncentral repeated carrier 满足

\[
p\mid\Theta_{\rm dec},
\qquad
p\mid L_{\rm tan},
\qquad
p\nmid2B(2K-9)T
\]
时，自动有

\[
\boxed{p\mid\mathcal R_{\rm tan}^{\rm int}.}
\tag{6.2}
\]

更一般地设

\[
\theta=v_p(\Theta_{\rm dec}),
\quad
r=v_p(L_{\rm tan}),
\quad
u=v_p(\mathcal R_{\rm tan}^{\rm int}).
\]

由 (6.1)，若 `theta != r`，则较浅的一项不能被另一项抵消，故

\[
\boxed{
\theta<r\Longrightarrow\nu=\theta,
\qquad
r<\theta\Longrightarrow\nu=r.
}
\tag{6.3}
\]

只有 `theta=r` 时可能发生等深 cancellation，使 `nu` 更深。

---

## 7. `已严格完成`：与 external prefix norm 的 exact bridge

`decimal-prefix-bridge.md` 定义

\[
\mathscr R_N=324Q^2N_0+2695B^2.
\]

从 (3.3) 消去 `Q^2N_0`：

\[
\boxed{
36\mathcal R_{\rm tan}^{\rm int}
=
\mathscr R_N
+B^2(18K-55)(54K-275).
}
\tag{7.1}
\]

因此 external center

\[
18K-55=0,
\qquad
\mathscr R_N=0
\]
确实自动落在 tangent center 上。这不是新的独立 singular obstruction，而是 (5.2) 所解释的 common-`alpha` / external shadow。

对 pure-spontaneous repeated prime，因为 (5.4) 已知 `18K-55` 为单位，所以 (7.1) 不能被误读成 external overlap。

---

## 8. `已严格完成`：q-side additive contact 在 repeated branch 上完全不可能

记

\[
P_{\rm tan}(K):=27K^2-220K+495.
\tag{8.1}
\]

旧 additive prefix polynomial 为

\[
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T).
\]

直接展开有

\[
\boxed{
9\mathscr S_0
+TP_{\rm tan}(K)
=2(2K-9)L_{\rm tan}.
}
\tag{8.2}
\]

设 `p` 为 genuine noncentral repeated spontaneous prime。若还假设

\[
p\mid\mathscr S_0,
\]
则由 `p|L_tan` 和 (8.2)：

\[
p\mid P_{\rm tan}(K).
\]

但 (3.3) 与 `p|R_tan^int` 立即给

\[
9Q^2N_0\equiv0\pmod p,
\]
与 genuine separation `p∤3QN_0` 矛盾。因此

\[
\boxed{
\text{genuine repeated spontaneous prime}
\Longrightarrow
p\nmid\mathscr S_0.
}
\tag{8.3}
\]

所以 repeated spontaneous carrier 不能回流成 q-side additive contact。

---

## 9. `已严格完成`：f-prefix overlap 只剩一条线性 target

纯 f-prefix polynomial 为

\[
\Psi_f=B^2(K^2-26)-Q^2N_0.
\]

与 (3.3) 相加：

\[
\boxed{
\mathcal R_{\rm tan}^{\rm int}+9\Psi_f
=B^2(2K-9)(18K-29).
}
\tag{9.1}
\]

所以 genuine noncentral repeated prime 若还进入 f-prefix contact

\[
p\mid\Psi_f,
\]
则

\[
\boxed{p\mid18K-29.}
\tag{9.2}
\]

central factor `2K-9` 已由 `spontaneous-prefix-branch-audit.md` 单列。

在 repeated tangent 上，(5.2) 还给

\[
9\alpha\equiv T(18K-55).
\]
若采用 (9.2)：

\[
\boxed{
9\alpha\equiv-26T\pmod p.
}
\tag{9.3}
\]

因此对 non-`3` inert prime（特别地 `p!=13`），该 f-overlap 仍满足 `p∤alpha`；它不会偷偷退回 height channel。真正的 repeated f-denominator overlap 从此只需研究固定线

\[
18K-29=0
\]
与旧 `f/Omega -> Delta_0` 边界，而不再需要一般 quadratic branch。

---

## 10. `已严格完成`：直接接入真实 `(H,e,M)` defect

endpoint `a=9,k=2` 已有

\[
b_2=10^{M-1}+2^{M-1}H,
\qquad
a_2=10^{M-1}-e,
\]

\[
0<H<\frac{5^{M-1}}{19},
\qquad
0<e<\frac{10^{M-1}}{250}.
\]

定义真实小参数

\[
\eta_H:=\frac{H}{5^{M-1}},
\qquad
\eta_e:=\frac{e}{10^{M-1}}.
\tag{10.1}
\]

则

\[
\boxed{
x=\frac{1+\eta_H}{10},
\qquad
y=1-\eta_e,
\qquad
s=10-\eta_e.}
\tag{10.2}
\]

而 (1.2) 的 `c` 精确变成

\[
\boxed{
c=
\frac{(\eta_H+21)^2
\bigl(4\eta_e^2-8\eta_e+81\eta_H^2+162\eta_H+85\bigr)}
{400(\eta_H+1)^2}.}
\tag{10.3}
\]

因此 repeated tangent 已被压成真正三变量 defect 方程

\[
\boxed{
\begin{aligned}
0={}&495\tau^2
-220(10-\eta_e)\tau
+27(10-\eta_e)^2\\
&+\frac{9(\eta_H+21)^2
\bigl(4\eta_e^2-8\eta_e+81\eta_H^2+162\eta_H+85\bigr)}
{400(\eta_H+1)^2},
\end{aligned}}
\tag{10.4}
\]

其中

\[
\tau=10^{-M},\qquad
0<\eta_H<\frac1{19},\qquad
0<\eta_e<\frac1{250}.
\]

这就是所需的 `(H,e,M)` 同步形式：没有 third block，也没有 source scale。实数上左侧严格为正；模 `p` 的 wrapping 是剩余唯一问题。

---

## 11. `已严格完成`：tangent integer 的精确 `2`-进本原化

已有 deep-even source 公式

\[
B=b_2=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\tag{11.1}
\]
其中 `Q_0=c_Qq` 为奇数。又因 `B` 为偶数且 `(A,B)=1`，`A` 为奇数；所以

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2\equiv1\pmod4.
\tag{11.2}
\]

(3.3) 的第二项恰有

\[
v_2(9Q^2N_0)=2M+2,
\]
而第一项满足

\[
v_2(B^2P_{\rm tan}(K))\ge2M+2m+2>2M+2,
\]
因为 `m>=1` 且 `P_tan(K)` 为奇数（`K=10P` 为偶数）。故

\[
\boxed{
v_2(\mathcal R_{\rm tan}^{\rm int})=2M+2.}
\tag{11.3}
\]

定义 odd primitive tangent integer

\[
\boxed{
\widehat{\mathcal R}_{\rm tan}
:=\frac{\mathcal R_{\rm tan}^{\rm int}}{2^{2M+2}}.}
\tag{11.4}
\]

由 (11.1)：

\[
\widehat{\mathcal R}_{\rm tan}
=2^{2m}c_u^2g^2P_{\rm tan}(K)
+9Q_0^2N_0.
\]
第一项被 `4` 整除，第二项为奇平方类，故

\[
\boxed{
\widehat{\mathcal R}_{\rm tan}\equiv1\pmod4.
}
\tag{11.5}
\]

于是其中所有 `3 mod 4` 素数的奇 valuation 总数必为偶数：

\[
\boxed{
\sum_{p\equiv3\ (4)}v_p(\widehat{\mathcal R}_{\rm tan})
\equiv0\pmod2.
}
\tag{11.6}
\]

这是 repeated tangent 自身的全局 inert-parity conservation。它尚未单独关闭 repeated carrier，但意味着任何以奇 tangent-depth 出现的 inert prime 必须由另一份 odd inert tangent-depth 配对。

---

## 12. 更新后的 repeated-spontaneous 开放核

本轮把 single-branch singularity 从“大判别式”改写成两条原始整数条件

\[
\boxed{
L_{\rm tan}\equiv0,
\qquad
\mathcal R_{\rm tan}^{\rm int}\equiv0.
}
\]

并严格得到：

1. pure repeated prime 与 `18K-55` external line 互斥；
2. q-side `S_0` overlap 不可能；
3. f-prefix overlap 只剩 `18K-29=0`；
4. tangent 已直接写成 `(H,e,M)` 三变量 defect 方程；
5. odd primitive tangent integer 恒为 `1 mod 4`，所以 inert tangent-depth 必成偶数总奇偶。

因此下一步不应再计算 `Q_1,Q_2` 的高次 discriminant。真正值得做的是：

- 审计 `18K-29` 与 `Delta_0=0` 的 repeated f-overlap；
- 对 pure moving repeated prime，把 (11.6) 与 `widehat(T)_2 == 3 mod 4` 的 odd-inert excess parity 联立；
- 或把 `L_tan` 与 finite-defect natural representative `C,D` 做 higher-depth CRT。
