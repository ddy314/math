# A1 minimal diagonal: central Pell degeneracy and local squareclasses

> 日期：2026-08-19。依赖 `central-supply-pell-normal-form.md`。当前范围为 `k=g>=26`，central core 已压成 30 个 `(z,w,Gamma)` 组合及其绝对有限 `U` 窗。

本文继续研究

\[
Y^2=A_U L^2+B_U,
\qquad L=10^k/c,
\]

其中

\[
c=2^{v_2(\Gamma)}5^{v_5(\Gamma)},
\qquad r=\Gamma/c,
\qquad C_0=w(10w-1),
\]

\[
A_U=U^2-4000C_0c^4r^2,
\]

\[
B_U=-4C_0rU+40C_0c^2r^2(20w-1).
\]

核心结论：

1. 所有允许 `U` 都满足 `A_U>0`、`B_U<0`；
2. 若 `A_U` 是整数平方，则该 Pell family 在 `k>=26` **统一无解**；
3. 对任何尚存 nonsquare family，`B_U` 必须同时是 `Q_2` 与 `Q_5` 中的平方，因此 `U-U_0` 被压入显式 2/5-adic squareclasses。

状态：**已严格完成。**

---

## 1. 天然平方点 `(U_0,V_0)`

定义

\[
\boxed{U_0:=10c\Gamma(20w-1),}
\]

\[
\boxed{V_0:=10c\Gamma.}
\]

因为 `Gamma=cr`，有

\[
\begin{aligned}
U_0^2-V_0^2
&=100c^2\Gamma^2\bigl((20w-1)^2-1\bigr)\\
&=4000w(10w-1)c^2\Gamma^2\\
&=4000C_0c^4r^2.
\end{aligned}
\]

所以

\[
\boxed{
A_U=U^2-(U_0^2-V_0^2).
}
\tag{1}
\]

另一方面

\[
40C_0c^2r^2(20w-1)
=4C_0rU_0,
\]

故

\[
\boxed{
B_U=-4C_0r(U-U_0).
}
\tag{2}
\]

这两个恒等式揭示了 Pell 系数的真正中心。

---

## 2. 所有允许 `U` 都严格位于平方点右侧

已有 `U` 下界

\[
U>c(C_0+1000\Gamma^2).
\]

而

\[
U_0=10c\Gamma(20w-1).
\]

六类型中 `w<=4`，故 `20w-1<=79`。于是

\[
1000\Gamma^2
>790\Gamma
\]

对当前 `Gamma>=16` 显然成立。因此

\[
\boxed{U>U_0.}
\tag{3}
\]

由 (2)：

\[
\boxed{B_U<0.}
\tag{4}
\]

同时

\[
U_0^2=V_0^2+4000C_0c^4r^2
>4000C_0c^4r^2,
\]

故 `U>U_0` 还给出

\[
\boxed{A_U>V_0^2>0.}
\tag{5}
\]

所以 central Pell family 永远处于“正主系数 + 负固定 norm”的情形。

---

## 3. `A_U` 为平方的全部退化族统一无解

假设

\[
A_U=S^2,
\qquad S\in\mathbf Z_{>0}.
\]

则 Pell 方程成为

\[
Y^2=S^2L^2+B_U
=(SL)^2-|B_U|.
\tag{6}
\]

由 (5)，

\[
S>V_0=10c\Gamma.
\]

因此

\[
SL>10c\Gamma\frac{10^k}{c}
=10\Gamma\,10^k.
\]

当前 `Gamma>=16`、`k>=26`，故

\[
\boxed{SL>1.6\times10^{28}.}
\tag{7}
\]

另一方面 30 个 central 组合统一满足

\[
\boxed{|B_U|<4\times10^{11}.}
\tag{8}
\]

该数值界只使用 `w<=4`、`Gamma<=39`、`c<=32` 和已有 `U` 上窗；附带脚本用精确整数再次审计全部 30 个组合。

于是

\[
0<|B_U|<2SL-1.
\]

因此

\[
(SL-1)^2
=(SL)^2-2SL+1
<(SL)^2-|B_U|
<(SL)^2.
\]

也就是 `Y^2` 被严格夹在两个相邻整数平方之间，矛盾。

故

\[
\boxed{
A_U\text{ 为整数平方}
\Longrightarrow
\text{该 central family 在 }k\ge26\text{ 无解}.}
\tag{9}
\]

从此 central core 只需研究

\[
\boxed{A_U>0\text{ 且 nonsquare}.}
\]

---

## 4. `B_U` 必须同时是 2-adic 与 5-adic 平方

记

\[
e_2=v_2(L)=k-v_2(c),
\qquad
e_5=v_5(L)=k-v_5(c).
\]

central 范围中 `v_2(c)<=5`、`v_5(c)<=1`，所以 `k>=26` 给出

\[
\boxed{e_2\ge21,\qquad e_5\ge25.}
\tag{10}
\]

由 Pell 方程

\[
Y^2=A_UL^2+B_U
\]

可得

\[
Y^2\equiv B_U\pmod{2^{2e_2}},
\qquad
Y^2\equiv B_U\pmod{5^{2e_5}}.
\tag{11}
\]

而 (8) 保证非零 `B_U` 的 2/5 赋值远小于 `2e_2,2e_5`。因此 `B_U` 必须本身属于

\[
\boxed{\mathbf Q_2^{\times2}\cap\mathbf Q_5^{\times2}.}
\tag{12}
\]

这不是只检查一个低模平方剩余；它是完整的局部平方类条件。

---

## 5. 把局部平方类写成 `t=U-U_0` 的显式条件

令

\[
\boxed{t:=U-U_0>0.}
\]

由 (2)：

\[
B_U=-4C_0rt.
\tag{13}
\]

写

\[
\alpha=v_2(C_0r),
\qquad
\beta=v_5(C_0r),
\]

\[
a=v_2(t),
\qquad
b=v_5(t),
\]

并令

\[
t=2^a5^b m,
\qquad\gcd(m,10)=1.
\]

### 5.1 二进条件

因为前面的 `4` 已贡献偶赋值，`B_U` 为 `Q_2` 平方首先要求

\[
\boxed{a\equiv\alpha\pmod2.}
\tag{14}
\]

去掉全部 2 次幂后，奇单位必须为 `1 mod 8`：

\[
\boxed{
-\frac{C_0r}{2^\alpha}\,5^b m
\equiv1\pmod8.
}
\tag{15}
\]

### 5.2 五进条件

同理必须有

\[
\boxed{b\equiv\beta\pmod2.}
\tag{16}
\]

并且去掉全部 5 次幂后的单位必须是模 5 二次剩余：

\[
\boxed{
\left(
\frac{
-(C_0r/5^\beta)\,2^a m
}{5}
\right)=1.
}
\tag{17}
\]

其中括号是 Legendre symbol。

因此，对每一对 valuation `(a,b)`：

- `a,b` 的奇偶性已固定；
- `m mod 8` 被唯一锁定；
- `m mod 5` 只剩两个二次特征允许类。

由 CRT，`m` 只落在两个显式 `mod 40` residue classes 中。

所以 central 的有限 `U` 窗并非无结构大区间，而是进一步分裂成

\[
\boxed{
\text{有限 valuation pairs }(a,b)
\times
\text{每对至多两个 }m\pmod{40}
}
\tag{18}
\]

的局部平方类射线。

---

## 6. 当前 central Pell 核心

结合 `central-supply-pell-normal-form.md` 与本文：

1. type-gap 只剩 30 个；
2. 每个组合 `U` 落在绝对有限、`k`-independent 的整数窗；
3. 所有 `A_U` square 的退化族已经统一排空；
4. 剩余 `U` 必须满足 (14)-(17) 的完整 2/5-adic squareclass；
5. 对每个尚存 `U`，只剩真正 nonsquare generalized Pell
   \[
   Y^2-A_UL^2=B_U,
   \qquad L=10^k/c.
   \]

下一步应只研究这些 nonsquare、local-compatible families；无需再把 square-`A_U` 或局部不可能的 `U` 带入 Pell/primitive-divisor 阶段。