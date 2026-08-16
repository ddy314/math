# A1 top-layer second-repunit escape cone — 2026-08-16

本文继续第二 repunit 边缘，并把此前逐个边界推进的结果统一成一个真正的无界斜率定理。

当前边缘固定为

\[
 g=0,
\quad n_2=2k,
\quad a_2=10^{2k}-1,
\quad b_2=10^{k-1},
\]

且前文已经证明

\[
 m_1\ge4k+1,
\qquad
\ell\ge2k+1.
\]

本文证明更强的整体逃逸锥：

\[
\boxed{
\max(m_1-4k,\ \ell-2k)\ge k-3.
}
\]

因此

\[
\boxed{
 m_1\ge5k-3
\quad\text{或}\quad
\ell\ge3k-3.
}
\]

这里没有固定 `r,s` 后枚举 `k`；结论直接覆盖全部无界 excess。

---

## 1. Excess 参数与端点 envelope

写

\[
\boxed{r=m_1-4k\ge1,}
\qquad
\boxed{s=\ell-2k\ge1,}
\]

并令

\[
R=10^r,
\qquad
S=10^s,
\qquad
x=10^k.
\]

于是

\[
 b_1=Rx^4-d,
\qquad
 a_1=10Rx^4+e,
\]

\[
 b_2=\frac{x}{10},
\qquad
 a_2=x^2-1,
\]

\[
 b_3=\frac{Sx^2}{10}+f,
\qquad
 a_3=Sx^2-h.
\]

其中 `d,h` 为正整数，`e,f` 为非负整数。

第一块 slope-4 分析给出 normalized endpoint distance

\[
\xi<\frac{61}{100}10^{-4k}.
\]

把它写回 `d,e` 后可粗化为

\[
\boxed{10d+e<7R.}
\tag{1}
\]

所以可安全使用

\[
|d|\le R,
\qquad
|e|\le7R.
\tag{2}
\]

第三块 endpoint cone 给出

\[
1\le h<\frac65S,
\qquad
0\le f<\frac18S.
\]

因此可粗化为

\[
\boxed{|h|\le2S,
\qquad
|f|\le S.}
\tag{3}
\]

---

## 2. exact lift 的通用多项式

由于

\[
C=a_1x^2+a_2,
\qquad
Q=b_1x+b_2,
\qquad
T=Sx^2,
\]

有

\[
\alpha=TC+a_3,
\qquad
\beta=TQ+b_3.
\]

exact lift 平方后为

\[
\alpha^2b_1^2b_2^2b_3^2
=
\beta^2
\left(
(a_1b_2b_3)^2
+(a_2b_1b_3)^2
+(a_3b_1b_2)^2
\right).
\]

清掉 `b_2=x/10` 的固定分母，得到

\[
\boxed{\Phi_{R,S,d,e,h,f}(x)=0,}
\tag{4}
\]

其中 `\Phi` 为次数至多 `26` 的整数多项式。

符号展开给出统一的最高两项：

\[
\boxed{
[x^{26}]\Phi
=2000R^3S^3L,
}
\tag{5}
\]

其中

\[
\boxed{
L=-5RS+100Rf+10Rh+10Sd+Se,
}
\tag{6}
\]

以及恒等地

\[
\boxed{
[x^{25}]\Phi=-2000R^3S^4.
}
\tag{7}
\]

所以 `\Phi` 永远不是零多项式：即使 `L=0`，`x^{25}` 项仍严格非零。

---

## 3. 所有低次系数的统一大小

脚本 `scripts/check_a1_repunit_escape_cone.py` 对符号系数逐 monomial 计算 L1 envelope。

在 (2)–(3) 下，每个系数均满足

\[
\boxed{
|[x^j]\Phi|
\le
19{,}849{,}340\,R^4S^4.
}
\tag{8}
\]

并且

\[
19{,}849{,}340<2000\cdot9925.
\tag{9}
\]

这个 bound 来自有限个符号 monomial 的精确整数系数求和，不涉及任何 `k,r,s` 枚举。

---

## 4. 首项不消失时的 Cauchy 根界

先设

\[
L\ne0.
\]

因为 `R,S` 都是 10 的正整数幂，(6) 中每一项都被

\[
\gcd(R,S)
\]

整除。因此若 `L\ne0`：

\[
\boxed{|L|\ge\gcd(R,S)=10^{\min(r,s)}.}
\tag{10}
\]

令

\[
M=\max(R,S)=10^{\max(r,s)}.
\]

由 (5)、(8)、(10)，任一低次系数相对于首项满足

\[
\left|
\frac{c_j}{c_{26}}
\right|
<9925\,
\frac{RS}{\gcd(R,S)}
=9925M.
\]

Cauchy 根界因此给出任意复根 `x`：

\[
|x|<1+9925M.
\]

而 `M\ge10`，故

\[
1+9925M<10000M.
\]

所以对 exact lift 所需的正根 `x=10^k`：

\[
10^k<10^4\,10^{\max(r,s)}.
\]

于是

\[
\boxed{\max(r,s)\ge k-3.}
\tag{11}
\]

---

## 5. 首项消失时仍得到同一结论

若

\[
L=0,
\]

则由 (7) 多项式次数恰为 `25`，首项绝对值为

\[
2000R^3S^4.
\]

由 (8)：

\[
\left|
\frac{c_j}{c_{25}}
\right|
<9925R.
\]

Cauchy 根界给出

\[
10^k<1+9925R<10000R=10^{r+4}.
\]

因此

\[
\boxed{r\ge k-3,}
\]

从而仍然有

\[
\boxed{\max(r,s)\ge k-3.}
\tag{12}
\]

---

## 6. 整体逃逸锥

由 (11)–(12)：

\[
\boxed{
\max(m_1-4k,\ \ell-2k)\ge k-3.
}
\tag{13}
\]

等价地，任意剩余 second-repunit-edge 候选都必须满足

\[
\boxed{
 m_1\ge5k-3
\quad\text{或}\quad
\ell\ge3k-3.
}
\tag{14}
\]

这严格强化了此前仅有的

\[
m_1\ge4k+1,
\qquad
\ell\ge2k+1.
\]

特别地，对任意固定常数 `B`，同时满足

\[
m_1\le4k+B,
\qquad
\ell\le2k+B
\]

的候选只能出现在

\[
k\le B+3
\]

的有限 `k` 切片中。

所以第二 repunit 边缘已经没有任何 bounded-width 无界通道；若存在无界族，它必须沿第一块或第三尾至少一个方向以额外线性速度逃离端点。