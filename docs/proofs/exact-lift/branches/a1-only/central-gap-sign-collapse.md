# A1 minimal diagonal: central-gap sign collapse

> 日期：2026-08-19。依赖 `central-gap-2adic.md`。
> 本文研究 central denominator sector 的整数平方核
> \[
> R=K-2(10^k\rho)Q\mathcal N.
> \]

令

\[
T=10^k,
\qquad
s=\frac{N_0}{T}\in[0.1,1].
\]

把 central relation

\[
10^k\rho=N_0T-\Gamma
\]

代入后，`R` 是 `T,N_0` 的显式整数多项式。本文证明其最高阶项已经能统一排除 18 个 central type-gap 组合。

结合 `central-gap-2adic.md`，central core 从 `48` 个进一步降到

\[
\boxed{30}
\]

个 type-gap 组合。

状态：**已严格完成。**

---

## 1. 全部 prefix 写成 `T,N_0`

minimal diagonal 中

\[
b_1=10T^2-w,
\qquad
a_2=10T^2-z,
\]

\[
Q=100T^2-10w+1,
\qquad D=TQ.
\]

又 `j=N_0+T-1`，故

\[
a_1
=100T^3+igl(10(5-z-w)+1\bigr)T+N_0-1.
\tag{1}
\]

其余量为

\[
C=10T^2a_1+a_2,
\]

\[
\mathcal N=a_1^2+(a_2b_1)^2,
\]

\[
K=b_1^2C^2-D^2\mathcal N.
\]

central sector 中

\[
B:=10^k\rho=N_0T-\Gamma,
\]

所以整数平方必要条件为

\[
\boxed{
R=K-2BQ\mathcal N\ge0,
\qquad R\text{ 为整数平方}.}
\tag{2}
\]

---

## 2. 最高阶系数

把

\[
N_0=sT
\]

形式代入多项式并按 `T` 收集。精确得到

\[
\boxed{
R=10000F_{z,w,\Gamma}(s)T^{10}
+\sum_{j=0}^{9}c_j(s)T^j.}
\tag{3}
\]

六类型的 `F` 为：

\[
F_{1,1,\Gamma}(s)
=s^2-280s+200\Gamma-5980,
\]

\[
F_{1,2,\Gamma}(s)
=s^2-280s+200\Gamma-5180,
\]

\[
F_{1,3,\Gamma}(s)
=s^2-280s+200\Gamma-4380,
\]

\[
F_{1,4,\Gamma}(s)
=s^2-280s+200\Gamma-3580,
\]

\[
F_{3,1,\Gamma}(s)
=s^2-240s+200\Gamma-4340,
\]

\[
F_{3,2,\Gamma}(s)
=s^2-240s+200\Gamma-3940.
\tag{4}
\]

这些二次式在 `s in [0.1,1]` 上都严格递减，因为导数分别小于 `2-240<0`。

---

## 3. 低阶余项有绝对统一界

对六类型与整个粗区间

\[
16\le\Gamma\le39,
\]

把每个 `c_j(s)` 视为 `s` 的整数多项式。对 `|s|<=1` 用系数绝对值和估计，可精确审计得到

\[
\boxed{
\sum_{j=0}^{9}\|c_j\|_1
\le101834561.}
\tag{5}
\]

因此对 `T>=1`：

\[
\left|\sum_{j=0}^{9}c_j(s)T^j\right|
\le101834561\,T^9.
\tag{6}
\]

而当前 fixed-layer 统一范围从 `k>=6` 开始，所以

\[
T\ge10^6.
\]

于是归一化余项满足

\[
\boxed{
\frac{|\text{remainder}|}{T^{10}}
<102.}
\tag{7}
\]

---

## 4. 若 `F<=-0.799`，平方核必严格为负

由 (3) 与 (7)，只要

\[
F_{z,w,\Gamma}(s)\le-0.799,
\]

就有最高阶项至多

\[
-7990T^{10},
\]

远大于低阶余项的绝对值，所以

\[
R<0.
\]

实际下面使用的最弱负 margin 更强：`(z,w,Gamma)=(1,1,30)` 在 `s=0.1` 时已有

\[
F=-7.99.
\]

因此不存在边界问题。

---

## 5. 被统一杀掉的 18 个组合

结合 `central-gap-2adic.md` 已允许的 gap 集合，逐类型利用 `F` 在 `[0.1,1]` 上递减，只需检查 `s=0.1` 的最大值。

### `(1,1)`

\[
\boxed{
\Gamma=16,18,20,22,24,26,28,30
\Longrightarrow R<0.}
\]

剩余 `32,34,36,38`。

### `(1,3)`

\[
\boxed{
\Gamma=16,18,20,22
\Longrightarrow R<0.}
\]

剩余 `24,26,28,30,32,34,36,38`。

### `(3,1)`

\[
\boxed{
\Gamma=16,18,20
\Longrightarrow R<0.}
\]

`Gamma=22` 的 leading sign 在当前 decade 内发生一次转换；`24,...,38` 保留。

### `(1,2)`

\[
\boxed{
\Gamma=16,22
\Longrightarrow R<0.}
\]

剩余 `30,32,38`。

### `(3,2)`

\[
\boxed{
\Gamma=16\Longrightarrow R<0.}
\]

剩余 `22,30,32,38`。

### `(1,4)`

2-adic 层只剩 `24,26`，二者 leading sign 均为正，所以本层不再删除。

总删除数：

\[
8+4+3+2+1=\boxed{18}.
\]

因此 central core 从 48 个降为

\[
\boxed{30}.
\tag{8}
\]

---

## 6. 唯一 crossing case `(3,1,Gamma=22)`

这里

\[
F(s)=s^2-240s+60.
\]

在 `s=0.251`：

\[
F(0.251)=-0.176999\ldots
\]

最高阶贡献小于 `-1769 T^10`，仍压过 (7) 的低阶余项。因此

\[
\boxed{
(z,w,\Gamma)=(3,1,22)
\Longrightarrow
\frac{N_0}{10^k}<0.251.}
\tag{9}
\]

所以 crossing case 虽未完全关闭，也被压入 decade 的最左约 15.1% 区间 `[0.1,0.251)`。

---

## 7. central sector 当前剩余表

| `(z,w)` | remaining `Gamma` |
|---|---|
| `(1,1)` | `32,34,36,38` |
| `(1,3)` | `24,26,28,30,32,34,36,38` |
| `(3,1)` | `22,24,26,28,30,32,34,36,38` (`22` 还要求 `N_0<0.251*10^k`) |
| `(1,2)` | `30,32,38` |
| `(3,2)` | `22,30,32,38` |
| `(1,4)` | `24,26` |

总数

\[
4+8+9+3+4+2=\boxed{30}.
\]

下一步可以在这 30 个正号组合上继续研究“是否为平方”，而不再浪费精力在已经由符号排除的 central gaps 上。