# A2 pure-spontaneous 单 branch 的 compact quadratic

> **依赖：** `spontaneous-sphere-roots.md`。
>
> **严格状态：**本文不再使用展开后的几十项 `Q_1,Q_2`，而把每一支写成 `Theta` root 与对应 sphere root 相交得到的统一小二次式。由此 single-branch repeated root 有显式临界长度 `tau_i^*`，并证明其真实 Archimedean 临界点统一大于 `12/5`，而实际 `10^{-M}<10^{-11}`。这说明 single-branch singularity 只能是纯 p-adic wrapping，不是实数临界退化。本文仍**不宣称 A2 全局关闭**。

---

## 1. 两个 sphere orientation

沿用

\[
\tau=10^{-M},
\qquad
s:=9+y,
\]

以及 `spontaneous-sphere-roots.md` 的两个有理函数根

\[
z_i:=\bar\zeta_i,
\qquad i=1,2.
\]

再记

\[
\boxed{
c(x,y):=
\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.}
\tag{1.1}
\]

`Theta_dec=0` 的 normalized root 为

\[
\bar\zeta_\Theta(\tau)
=
\frac{
 x^2(s^2-18s\tau+55\tau^2)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2s-9\tau)}.
\tag{1.2}
\]

---

## 2. `已严格完成`：每个 `Q_i` 只是同一个小二次模板

令

\[
\bar\zeta_\Theta(\tau)=z_i.
\]

从 (1.2) 直接清分母，除以 `x^2`，得到

\[
\boxed{
\mathscr L_i(\tau)
:=55\tau^2
+18(z_i-s)\tau
+s^2-4sz_i-c
=0.
}
\tag{2.1}

因此 `spontaneous-prefix-eliminant.md` 的 `Q_1,Q_2` 只是

\[
\boxed{
\mathcal Q_i
=\text{(sphere-root denominator)}\times\mathscr L_i
}
\tag{2.2}

的 primitive integer clearing。真正的长度几何完全由 (2.1) 读取，不必反复展开几十项系数。

---

## 3. `已严格完成`：single-branch repeated root 的唯一临界长度

(2.1) 对 `tau` 求导：

\[
\mathscr L_i'(\tau)
=110\tau+18(z_i-s).
\]

所以 repeated root 若存在，临界点唯一：

\[
\boxed{
\tau_i^*
=\frac{9(s-z_i)}{55}.
}
\tag{3.1}

相应 discriminant 为

\[
\boxed{
\begin{aligned}
\mathscr D_i
&:=\operatorname{disc}_\tau(\mathscr L_i)\\
&=324z_i^2+232sz_i+104s^2+220c.
\end{aligned}}
\tag{3.2}

完成平方：

\[
\boxed{
\mathscr D_i
=324\left(z_i+\frac{29s}{81}\right)^2
+\frac{5060}{81}s^2
+220c.
}
\tag{3.3}

其中

\[
5060=2^2\cdot5\cdot11\cdot23.
\]

因此在真实 endpoint `x,y>0` 上

\[
\boxed{\mathscr D_i>0.}
\tag{3.4}

这不是模素数排除；它只是证明真实二次式没有重根。模 `p` 的 repeated-root channel 仍可由 `D_i≡0` 产生。

---

## 4. `已严格完成`：真实临界长度远离 decimal orbit

endpoint box 中

\[
y>\frac{249}{250}
\quad\Longrightarrow\quad
s>\frac{2499}{250}.
\]

`spontaneous-sphere-roots.md` 又给

\[
z_i<-rac{1223295069}{256000000}
\qquad(i=1,2).
\]

代入 (3.1)：

\[
\tau_i^*
>
\frac9{55}
\left(
\frac{2499}{250}
+rac{1223295069}{256000000}
\right)
=
\frac{34040439621}{14080000000}.
\]

因此

\[
\boxed{
\tau_i^*>2.4176>\frac{12}{5}.
}
\tag{4.1}

另一方面当前无界核 `M>=11`，所以实际 decimal length phase 为

\[
\boxed{
0<\tau=10^{-M}\le10^{-11}.
}
\tag{4.2}

于是实数轴上：

\[
\boxed{
\tau_i^*-\tau>\frac{12}{5}-10^{-11}.
}
\tag{4.3}

single-branch singularity 的临界位置甚至不在 `[0,1]` 内，而真实 decimal orbit 已贴近 `0`。

---

## 5. `已严格完成`：modular singular branch 只剩一条线性 length target

若某个 odd prime `p` 使 `Q_i` 在真实 `tau=10^{-M}` 处成为 repeated root，则在所有 sphere-root denominator 为单位的 genuine channel：

\[
\boxed{
55\tau\equiv9(s-z_i)\pmod p,
}
\tag{5.1}

并且

\[
\boxed{
\mathscr D_i\equiv0\pmod p.
}
\tag{5.2}

反过来，(5.1) 与 `L_i(tau)=0` 等价于 (5.2)。所以 single-branch bad reduction 不再需要一个 degree-16/20 的未命名判别多项式；它就是 sphere orientation `z_i` 与一条显式 length tangent 的交点。

如果清去 `z_i` 的分母，(5.1) 对每一支都只给一个关于 `tau` 的**一次** pure-prefix polynomial。这是后续与 `tau=10^{-M}` 的 multiplicative orbit 做 Hensel 同步时应使用的规范形式。

---

## 6. 证明边界与下一步

本文件严格证明：

1. `Q_1,Q_2` 各自是统一 quadratic template (2.1)；
2. 每支 repeated root 只有唯一临界长度 (3.1)；
3. 真实 endpoint 的临界长度统一 `>12/5`，实际 `tau<=10^-11`；
4. modular bad reduction 可改写为一次 length tangent (5.1)。

但 (4.3) 仍只是 Archimedean separation；`p | Q_i`、`p | D_i` 可以通过取模绕回。因此尚不能据此关闭 moving simple/singular prime。

下一步应把 (5.1) 清分母后与：

- external discriminant line `E_W=0`；
- `D_src / Delta_pref`；
- 或真实 `10^{-M}` multiplicative orbit

做 resultant / Hensel 同步。若能证明 singular tangent 的 required prime-power depth 超过清分母整数高度，才可把这条实数远离转成真正空性。
