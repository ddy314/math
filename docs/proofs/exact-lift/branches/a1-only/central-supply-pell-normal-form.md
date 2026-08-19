# A1 minimal diagonal: central supply Pell normal form

> 日期：2026-08-19。依赖 `gap-denominator-normal-form.md`、`central-gap-2adic.md`、`central-gap-sign-collapse.md`。
> 当前统一前沿为 `k=g>=26`，central core 已只剩 30 个 `(z,w,Gamma)` 组合。

本文把 odd-prime supply 的粗必要条件

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1
\]

进一步转成一个与 `k` 无关的有限参数 `U`，并把所有剩余十进制尺度装进

\[
L=\frac{10^k}{c_\Gamma}.
\]

最终每个 central type-gap 组合都被严格归约为有限多个广义 Pell / Thue-Mahler 方程

\[
\boxed{Y^2=A_U L^2+B_U,\qquad L=10^k/c_\Gamma.}
\]

这一步尚未宣称这些方程全部无解，但它第一次把 central sector 中的 `k`-uniform odd-supply 问题降成**绝对有限个固定系数二次方程族**。

状态：**归约严格完成；方程族的统一无解性待证。**

---

## 1. central decimal equation

固定 central gap

\[
\Gamma\in\{16,\ldots,39\}.
\]

令

\[
\boxed{
c:=c_\Gamma
=2^{v_2(\Gamma)}5^{v_5(\Gamma)},}
\]

\[
\boxed{r:=\Gamma/c.}
\]

于是

\[
\gcd(r,10)=1.
\]

再令

\[
\boxed{L:=10^k/c.}
\]

因为当前 `k>=26` 而 `c<=32`，`L` 是一个巨大整数，并且

\[
\gcd(r,L)=1.
\]

central normal form

\[
c h=N_0 10^k-\Gamma
\]

精确化为

\[
\boxed{h=N_0L-r.}
\tag{1}
\]

---

## 2. odd supply 首先给出 `h | Q b1`

minimal-diagonal odd-prime theorem 给

\[
h=qs,
\qquad q\mid Q,
\]

而 `s` 是 `b_1` 的 whole-block selector，因此特别有

\[
s\mid b_1.
\]

又

\[
\gcd(Q,b_1)=1,
\]

所以

\[
\boxed{h\mid Qb_1.}
\tag{2}
\]

本文只使用 (2)，因此所得结论甚至比完整 whole-block supply 更弱、更安全；任何 exact candidate 必须通过它。

---

## 3. `Qb1` 在 `L` 坐标下只有三层

因为

\[
10^k=cL,
\]

有

\[
b_1=10c^2L^2-w,
\]

\[
Q=100c^2L^2-10w+1.
\]

记

\[
\boxed{C_0:=w(10w-1).}
\tag{3}
\]

直接相乘：

\[
\boxed{
Qb_1
=1000c^4L^4
+10c^2(1-20w)L^2
+C_0.}
\tag{4}
\]

没有 `L^3` 或 `L` 项。正是这个稀疏性允许做下面的十进制 Euclidean descent。

---

## 4. 第一次商余：固定小 residual `tau`

由 (2)，定义正整数

\[
\boxed{M:=\frac{Qb_1}{h}.}
\]

对 `L` 作 Euclidean division：

\[
\boxed{M=B L+m,\qquad0\le m<L.}
\tag{5}
\]

由 (1)：

\[
h\equiv-r\pmod L,
\]

由 (4)：

\[
Qb_1\equiv C_0\pmod L.
\]

所以

\[
-rm\equiv C_0\pmod L.
\]

即存在整数 `tau` 使

\[
\boxed{rm+C_0=\tau L.}
\tag{6}
\]

因为 `0<=m<L`、`L>C_0` 且 `r>=1`，有

\[
\boxed{1\le\tau\le r.}
\tag{7}
\]

因此第一次余数虽然 `m` 随 `L` 增长，但它由一个绝对小的 `tau` 唯一控制。

---

## 5. 第二次下降产生 bounded integer `U`

把

\[
Qb_1=(N_0L-r)(BL+m)
\]

展开，并使用 (4)、(6)。比较除去常数项后的 `L`-倍数，模 `L` 得

\[
N_0m-rB-\tau\equiv0\pmod L.
\]

乘以 `r` 并用

\[
rm=\tau L-C_0
\]

得到

\[
\boxed{
r^2B+N_0C_0+r\tau=UL}
\tag{8}
\]

对某个正整数 `U`。

将 (6)、(8) 全部代回精确乘积恒等式，所有 `B,m,tau` 消失，最终得到

\[
\boxed{
C_0N_0^2
-U L N_0
+1000c^4r^2L^2
+rU
-10c^2r^2(20w-1)
=0.}
\tag{9}
\]

这是 central odd-supply 的核心二次正规形。

---

## 6. `U` 的区间与 `k` 无关

由 (9) 也可直接解出

\[
\boxed{
U=
\frac{
C_0N_0^2
+1000c^4r^2L^2
-10c^2r^2(20w-1)
}{N_0L-r}.}
\tag{10}
\]

写

\[
s=N_0/L.
\]

由于

\[
10^{k-1}\le N_0<10^k=cL,
\]

有

\[
\boxed{c/10\le s<c.}
\tag{11}
\]

忽略 `O(L^-2)` 的精确主函数为

\[
f(s)=C_0s+\frac{1000c^4r^2}{s}.
\tag{12}
\]

在 (11) 上

\[
f'(s)=C_0-\frac{1000c^4r^2}{s^2}
< C_0-1000c^2r^2
=C_0-1000\Gamma^2<0.
\]

所以 `f` 严格递减。

从 (10) 直接比较可见 `U>f(s)`；而当前 `k>=26` 给出的 `L` 极大，使正误差严格小于 `1`。因此可取安全整数窗

\[
\boxed{
 c(C_0+1000\Gamma^2)
<U
<c\left(\frac{C_0}{10}+10000\Gamma^2\right)+1.}
\tag{13}
\]

关键点是：这个区间**完全不含 `k`**。

所以对每个固定 `(w,Gamma)`，`U` 只属于一个绝对有限整数集合。

---

## 7. 判别式给出 generalized Pell equation

把 (9) 看成关于整数 `N_0` 的二次方程。其判别式必须是整数平方：

\[
\boxed{Y^2=\Delta_U(L).}
\]

直接展开得到

\[
\boxed{
Y^2
=
\left(
U^2-4000C_0c^4r^2
\right)L^2
-4C_0rU
+40C_0c^2r^2(20w-1).}
\tag{14}
\]

定义固定整数

\[
\boxed{
A_U:=U^2-4000C_0c^4r^2,}
\]

\[
\boxed{
B_U:=-4C_0rU
+40C_0c^2r^2(20w-1).}
\]

则

\[
\boxed{Y^2=A_UL^2+B_U.}
\tag{15}
\]

而

\[
\boxed{
L=10^k/c
=2^{k-v_2(c)}5^{k-v_5(c)}.}
\tag{16}
\]

因此每个固定 `U` 对应一个固定系数的 generalized Pell / binary quadratic `S`-unit 方程，其中第二变量 `L` 只能沿一条纯 `2/5` 指数射线增长。

---

## 8. Q-side / b1-side resultants

完整 supply 还能保留更多信息。写

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1.
\]

由 central congruence

\[
N_0 10^k\equiv\Gamma\pmod q,
\]

以及

\[
Q=100(10^k)^2-(10w-1),
\]

得到

\[
\boxed{
q\mid
(10w-1)N_0^2-100\Gamma^2.}
\tag{17}
\]

同理，从 `s|b1` 得

\[
\boxed{
s\mid wN_0^2-10\Gamma^2.}
\tag{18}
\]

两个 resultant 还满足精确差式

\[
\boxed{
10(wN_0^2-10\Gamma^2)
-igl((10w-1)N_0^2-100\Gamma^2\bigr)
=N_0^2.}
\tag{19}
\]

这些关系将在继续筛选有限 `U` families 时保留 Q-side / whole-block side 的来源信息。

---

## 9. 当前 central core 的新形状

此前 central sector 经 2-adic + sign collapse 只剩 30 个 `(z,w,Gamma)`。

本文进一步证明：对每个这样的固定组合，任意 candidate 都必须给出一个整数 `U`，满足绝对有限窗 (13)，并使

\[
Y^2=A_UL^2+B_U,
\qquad L=10^k/c,\quad k>=26.
\]

所以 central sector 的无界问题已经从

- `k` 任意增长；
- `N_0` 有约 `9*10^(k-1)` 个值；
- odd-prime supply 随 `b_1,Q` factorization 改变；

归约为：

\[
\boxed{
30\text{ 个 type-gap}
\times
\text{每个一个固定有限 }U\text{ 区间}
\times
\text{固定系数 }S\text{-unit Pell families}.}
\]

下一步应优先利用：

1. `B_U` 必须同时是足够深的 `2`-adic、`5`-adic square residue；
2. 若 `A_U` 是整数平方，则 (15) 立即退化成固定因子差平方，`k` 大时极易排除；
3. 若 `A_U` 非平方，则 (15) 是一族固定 generalized Pell 方程，而 `L` 被限制为纯 `2/5`-unit，可继续用局部模筛、Lucas/Pell primitive divisor 或显式 Thue-Mahler 方法；
4. (17)-(19) 继续保留 full odd-prime source split，可进一步过滤 `U,N_0`。

本文只完成归约，不把这些后续算术任务误写成已经关闭。