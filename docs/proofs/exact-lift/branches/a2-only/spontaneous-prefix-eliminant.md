# A2 spontaneous carrier 的 pure-prefix 消元

> **依赖：** `spontaneous-angle.md`、`phase-and-defect.md`、`endpoint-lattice.md` 的 reflection endpoint shell，以及 `spontaneous-bad-primes.md` / `external-secant-center.md` 对 fully coupled external 子通道的后续审计。
>
> **严格状态：**本文处理 `spontaneous-angle.md` 留下的 generic common-prime 问题：同一个 non-`3` inert prime 同时接触 spontaneous angle polynomial `Omega_sp` 与 pure-decimal odd-cofactor polynomial `Theta_dec`。主要结果是把第三块 `a_3,b_3` 完全消去，得到两个只依赖第一、二块 prefix 与 `10^{-M}` 的二次 gate；再求两个 gate 的 exact resultant，得到单一 branch-collision kernel。本文仍**不宣称 A2 全局关闭**。

---

## 1. 原始 decimal 记号

固定当前最危险 reflection endpoint：

\[
a_1=9,
\qquad
N:=10^M,
\qquad
T:=10^m.
\]

记

\[
A:=a_2,
\qquad
B:=b_2,
\]

\[
Q:=2N+B,
\qquad
K:=9N+10A,
\]

\[
C_0:=\frac{9B}{2},
\qquad
N_0:=C_0^2+A^2.
\tag{1.1}
\]

对应的 scale-free prefix variables 为

\[
x=\frac BN,
\qquad
y=\frac{10A}{N}.
\tag{1.2}
\]

第三块写成

\[
w:=\frac{b_3}{T},
\qquad
\zeta:=\frac{a_3}{T}.
\tag{1.3}
\]

`spontaneous-angle.md` 的 source-normalized variable 满足

\[
r_s=\frac{Nx}{w}=\frac{B}{w}=\frac{BT}{b_3}.
\tag{1.4}
\]

---

## 2. `已严格完成`：`Omega_sp` 对第三分母其实是纯整数一次式

定义

\[
d:=225x^2-y,
\]

\[
\boxed{
A_{\rm sp}
:=4d^2-xy^2(99x-4).
}
\tag{2.1}
\]

则

\[
\Omega_{\rm sp}
=A_{\rm sp}r_s+2xy^2(x+2).
\tag{2.2}
\]

把 (1.2)、(1.4) 代回并清去 `N`、`b_3`，定义纯 prefix 整数

\[
\boxed{
\mathcal U_\Omega
:=(45B^2-2AN)^2-A^2B(99B-4N).
}
\tag{2.3}
\]

直接展开得到精确恒等式

\[
\boxed{
\Omega_{\rm sp}
=\frac{100B}{b_3N^4}
\left(
T\mathcal U_\Omega+2A^2Qb_3
\right).
}
\tag{2.4}
\]

因此对 genuine spontaneous prime，`p` 与 `2·5·ABQb_3N` 分离，故

\[
\boxed{
p\mid\Omega_{\rm sp}
\iff
p\mid T\mathcal U_\Omega+2A^2Qb_3.
}
\tag{2.5}
\]

换成 `w=b_3/T`：

\[
\boxed{
w\equiv-\frac{\mathcal U_\Omega}{2A^2Q}\pmod p.}
\tag{2.6}
\]

在 scale-free 坐标中同一式进一步变成

\[
\boxed{
\frac wN
\equiv
-\frac{A_{\rm sp}}
{2y^2(x+2)}
\pmod p.
}
\tag{2.7}
\]

也就是说，`Omega_sp` 不是只固定抽象 source ratio；它实际上唯一固定了真实 third denominator 的 normalized decimal phase。

注意

\[
45B^2-2AN=\frac{20}{9}D_{\rm src},
\]
所以 (2.3) 仍保留旧 source-Hensel 几何的来源；这里没有制造新的独立 source quantity。

---

## 3. `已严格完成`：`Theta_dec` 对第三分子也是纯整数一次式

`spontaneous-angle.md` 已定义

\[
\Theta_{\rm dec}
=B^2\mathscr S_0-TQ^2N_0,
\]

其中

\[
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T).
\]

定义

\[
\boxed{
\mathcal R_\Theta
:=B^2(K^2-18K+55)-Q^2N_0.
}
\tag{3.1}
\]

则完全展开后：

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal R_\Theta
-2B^2(2K-9)a_3.
}
\tag{3.2}
\]

所以在非中心退化通道

\[
p\nmid2K-9
\tag{3.3}
\]
上，任意 odd carrier `p|Theta_dec` 唯一固定

\[
\boxed{
\zeta=\frac{a_3}{T}
\equiv
\frac{\mathcal R_\Theta}
{2B^2(2K-9)}
\pmod p.
}
\tag{3.4}
\]

因此 generic `Omega_sp ∩ Theta_dec` common prime 同时唯一固定 `w` 与 `zeta`；第三块已经没有自由 residue。

边界 `p|2K-9` 必须单列。此时 (3.2) 退化为

\[
p\mid\mathcal R_\Theta.
\]

在 `2K=9` 下

\[
\mathcal R_\Theta
=-\frac{23}{4}B^2-Q^2N_0,
\tag{3.5}
\]

即一个纯 prefix central gate。本文的二次消元只声称覆盖 (3.3) 的 generic channel；(3.5) 不被偷偷除掉。

---

## 4. `已严格完成`：真正的 sphere equation 只需原始 decimal blocks

当前拼接值本身是

\[
\mathcal R
=\frac{TK+a_3}{TQ+b_3}.
\tag{4.1}
\]

而原三项平方和为

\[
\frac{81}{4}+\frac{A^2}{B^2}+\frac{a_3^2}{b_3^2}
=\frac{N_0}{B^2}+\frac{a_3^2}{b_3^2}.
\]

因此 exact lift 的 sphere condition 等价于纯整数恒等式

\[
\boxed{
B^2b_3^2(TK+a_3)^2
=(TQ+b_3)^2
\left(
N_0b_3^2+B^2a_3^2
\right).
}
\tag{4.2}
\]

这就是消去 (2.6)、(3.4) 所需的第三条方程；不需要再引入 Gaussian quotient、`W_q` 或 finite-defect quotient。

---

## 5. `已严格完成`：第三块完全消去，只剩两个 `10^{-M}` 二次 gate

令

\[
\tau:=10^{-M}=N^{-1}
\]
在任意 `p\ne2,5` 的有限域中理解为 `N` 的逆元。

继续记

\[
\mathcal N(x,y):=2025x^2+y^2.
\tag{5.1}
\]

由 (2.7)：

\[
\boxed{
\bar w:=\frac wN
=-\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{5.2}
\]

由 (3.4) 除以 `N`，得到

\[
\boxed{
\bar\zeta:=\frac{\zeta}{N}
=
\frac{
 x^2\bigl((9+y)^2-18(9+y)\tau+55\tau^2\bigr)
 -\frac1{100}(x+2)^2\mathcal N(x,y)
}
{2x^2\bigl(2(9+y)-9\tau\bigr)}.
}
\tag{5.3}
\]

把 (5.2)–(5.3) 代入 (4.2) 并约掉共同 `N`-尺度，sphere equation 变成

\[
 x^2\bar w^2(9+y+\bar\zeta)^2
=(2+x+\bar w)^2
\left(
\frac{\mathcal N(x,y)}{100}\bar w^2
+x^2\bar\zeta^2
\right).
\tag{5.4}
\]

清去分母后的 numerator 在 `Q[tau,x,y]` 中精确分解为两个 primitive 二次因子：

\[
\boxed{
\mathcal P_{\rm sph}(\tau,x,y)
=-\mathcal Q_1(\tau;x,y)\mathcal Q_2(\tau;x,y).
}
\tag{5.5}
\]

这里 `Q_1,Q_2` 以 `tau` 次数为 `2`，按首项唯一正规化：

\[
\boxed{
[\tau^2]\mathcal Q_1
=11000x^2y^3(x+2)^2,
}
\tag{5.6}
\]

\[
\boxed{
[\tau^2]\mathcal Q_2
=-11000x^2y^3(x+2)^2\Delta_0(x,y),
}
\tag{5.7}
\]

其中

\[
\boxed{
\Delta_0(x,y)=2025x^2-18y-y^2.
}
\tag{5.8}
\]

两个二次式的完整 expanded coefficients 作为 literal polynomial 放在

`check_a2_spontaneous_prefix_eliminant.py`

中；checker 直接从 (5.2)–(5.4) 重建 numerator 并核对 (5.5)，所以正文不重复塞入约八十项机械系数。

于是 generic genuine common carrier 必满足

\[
\boxed{
\mathcal Q_1(10^{-M};x,y)\equiv0
\quad\text{或}\quad
\mathcal Q_2(10^{-M};x,y)\equiv0
\pmod p.
}
\tag{5.9}
\]

这是真正的新降维：

\[
(r_s,w,\zeta,a_3,b_3,m)
\]
全部从 common-prime condition 中消失，只剩第一、二块 prefix 与 decimal length phase `10^{-M}`。

注意 (5.9) 仍只是必要条件；二次 gate 可以有 simple roots，不能因为“只有两个 branch”就宣称空性。

---

## 6. `已严格完成`：两个 prefix branch 的共同根由单一 kernel 控制

除了 `A_sp`，再定义

\[
\boxed{
A_-:=A_{\rm sp}-2y^2(x+2)^2
}
\tag{6.1}
\]

即

\[
A_-
=202500x^4-101x^2y^2-1800x^2y
-4xy^2-4y^2,
\tag{6.2}
\]

以及

\[
\boxed{
\begin{aligned}
C_*:={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}}
\tag{6.3}
\]

对两个二次 gate 关于 `tau` 求 exact resultant，得到惊人的完全因子化：

\[
\boxed{
\begin{aligned}
\operatorname{Res}_{\tau}(\mathcal Q_1,\mathcal Q_2)
={}&-7128000\,x^2y^6(x+2)^4(225x^2-y)^2\\
&\cdot A_-^2A_{\rm sp}^2C_*.
\end{aligned}}
\tag{6.4}
\]

而

\[
7128000=2^6\cdot3^4\cdot5^3\cdot11.
\tag{6.5}
\]

对 genuine non-`3` spontaneous cofactor carrier，旧分离条件与 `spontaneous-angle.md` 已给

\[
p\nmid 2\cdot3\cdot5\,x y(x+2)(225x^2-y)A_{\rm sp}.
\tag{6.6}
\]

因此对 `p\ne11`：

\[
\boxed{
\mathcal Q_1\equiv\mathcal Q_2\equiv0
\Longrightarrow
p\mid A_-C_*.
}
\tag{6.7}
\]

所以 two-branch collision 不再是一个未命名 resultant；它只有两个显式二维 kernel `A_-` 与 `C_*`，外加固定 coefficient prime `11`。

这并不说明 generic carrier 必须让两个 branch 同时消失；单独的一条 simple branch 仍然是当前开放核。

---

## 7. `已严格完成`：fully coupled external 子通道中 `A_-` 整支自动消失

若同一个 prime 还处于 `spontaneous-angle.md` §6 的 external discriminant-zero channel，则

\[
\boxed{
E_W(x,y)
:=220y^4(x+2)^4-49A_{\rm sp}^2
\equiv0\pmod p.
}
\tag{7.1}
\]

对 `A_-` 与 `E_W` 消去 `y`，exact resultant 为

\[
\boxed{
\operatorname{Res}_y(A_-,E_W)
=2^{14}3^{18}5^{16}x^{16}(x+2)^8.
}
\tag{7.2}
\]

因此在 genuine external channel

\[
p\nmid2\cdot3\cdot5\,x(x+2)
\]
中：

\[
\boxed{p\nmid A_-.}
\tag{7.3}
\]

结合 (6.7)，若 fully coupled external prime 同时落在两个 prefix quadratic branch 上，则（`p\ne11`）只能满足

\[
\boxed{p\mid C_*.}
\tag{7.4}
\]

这与此前 fixed `19/47` secant 分类的角色不同：这里 `C_*` 控制的是 **two-prefix-branch collision**，不是 secant cofactor 本身。

---

## 8. `已严格完成 / 结构解释`：`67` 与 `47` 从 branch-collision 判别式中自然出现

两个 collision kernel 自身又都是关于 `y` 的二次式。

首先

\[
\boxed{
\operatorname{disc}_y(A_-)
=900^2x^4(101x^2+4x+8).
}
\tag{8.1}
\]

而内层 quadratic 满足

\[
\boxed{
\operatorname{disc}_x(101x^2+4x+8)
=-16\cdot3\cdot67.
}
\tag{8.2}
\]

所以旧 fully coupled local audit 中出现的 fixed `67` 并非完全孤立：它正是 `A_-` collision kernel 的 nested ramification prime。

另一方面

\[
\boxed{
\operatorname{disc}_y(C_*)
=-810^2x^2(x+2)^2
(2381x^2+324x+416),
}
\tag{8.3}
\]

且

\[
\boxed{
\operatorname{disc}_x(2381x^2+324x+416)
=-16\cdot23\cdot47\cdot223.
}
\tag{8.4}
\]

因此 `47` 也在 pure-prefix branch-collision 几何中有独立来源：它是 `C_*` 的 nested ramification prime之一。这与 `external-secant-center.md` 中 `47` 作为 `Xi_C` center-cancellation prime 的出现相互吻合，但两者不是同一条公式，不能重复收费。

同样必须审计边界：`23`、`223` 也出现在 (8.4)，所以 (8.4) 不能被误写成“只有 47”；它只识别 bad-reduction support。

---

## 9. 实数侧审计：这些 gate 都不是真实零点下降

endpoint window 中

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
\]

`spontaneous-angle.md` 已证明

\[
A_{\rm sp}>\frac{8049}{1444}>5.
\]

同时 `C_*` 的全部显示项在 `x,y>0` 时为正，因此

\[
\boxed{C_*>0.}
\tag{9.1}
\]

所以 (6.7)、(7.4) 描述的是纯 modular / p-adic collision，而不是实数曲线真的穿过 endpoint box。这里同样不能从正性直接推出“没有素因子”。

---

## 10. 当前开放核

本层严格完成了下面的变量消去：

\[
\boxed{
\Omega_{\rm sp}=0,
\quad
\Theta_{\rm dec}=0,
\quad
\text{exact sphere}
}
\]

在 generic `p\nmid2K-9` 通道中推出

\[
\boxed{
\mathcal Q_1(10^{-M};x,y)
\mathcal Q_2(10^{-M};x,y)
\equiv0\pmod p.
}
\]

并进一步得到：

1. `Omega_sp` 唯一固定 `b_3/T`；
2. `Theta_dec` 唯一固定 `a_3/T`；
3. 第三块全部消去后只有两个 prefix quadratic branch；
4. 两 branch 的共同根只经过 `A_-`、`C_*` 或固定 `11`；
5. fully coupled external channel 中 `A_-` 被 exact resultant 完全排除，所以 branch collision 只剩 `C_*`；
6. `67` 与 `47` 分别作为 `A_-`、`C_*` 的 nested ramification prime 自然恢复。

**仍未完成：**单独一条 `Q_1` 或 `Q_2` 的 simple moving root 仍可以存在。所以下一步不应再研究第三块，而应直接研究这两个 prefix quadratic 对真实 decimal orbit

\[
\tau=10^{-M},
\qquad
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}}
\]

的 `p`-进同步；或者把 `Q_i` 与 `D_src / Delta_pref / C` 的 natural representative 做新的 resultant。中心退化线 `2K-9=0` 也需单列，不能被 generic 除法覆盖。
