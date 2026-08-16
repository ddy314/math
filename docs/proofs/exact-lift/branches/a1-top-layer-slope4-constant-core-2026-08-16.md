# A1 top-layer slope-4 constant core — 2026-08-16

本文继续 `a1-top-layer-edge-closure-and-slope4-2026-08-16.md`，专门处理第二 repunit 边缘的新取等层

\[
\boxed{m_1=4k+1.}
\]

前文已经知道这里 `b_1` 与 `a_1` 只有常数级十进制偏移。本文进一步证明连续几何只允许

\[
\boxed{10d+e\le52,}
\]

从而把该无界 `k` 家族压成有限个 constant-offset 类型。

本文结论均为 **已严格完成**。

---

## 1. 边界参数

当前边缘固定为

\[
g=0,
\qquad
n_2=2k,
\qquad
 a_2=10^{2k}-1,
\qquad
 b_2=10^{k-1},
\]

以及

\[
m_1=4k+1.
\]

最高层 `s_1=2` 给出

\[
n_1-1=m_1+1=4k+2.
\]

写

\[
\boxed{b_1=10^{4k+1}-d,}
\qquad d\ge1,
\]

\[
\boxed{a_1=10^{4k+2}+e,}
\qquad e\ge0.
\]

前文已经粗略得到

\[
d\le6,
\qquad e<61.
\tag{1}
\]

记

\[
a=10^{-2k},
\]

则

\[
D:=\frac{d}{10^{m_1}}
=\frac d{10}a^2,
\]

\[
E:=\frac{e}{10^{n_1-1}}
=\frac e{100}a^2.
\]

沿用

\[
w=\frac{1-D}{1+E},
\qquad
x=1-w.
\]

所以

\[
\boxed{
 x
=\frac{D+E}{1+E}
=a^2\frac{10d+e}{100+e a^2}.
}
\tag{2}
\]

特别地，连续几何在这个边界上只看组合

\[
\boxed{c:=10d+e.}
\]

并且原分数还有精确关系

\[
\boxed{a_1=10b_1+c.}
\tag{3}
\]

---

## 2. 边界上的 `\lambda` 已是 `O(a^2)`

本边缘

\[
\lambda=\frac1{10b_1+1}.
\]

由 `d\le6`、`k\ge1`：

\[
b_1
=10^{4k+1}-d
>\frac{99}{100}10^{4k+1}.
\]

因此

\[
\boxed{\lambda<\frac{a^2}{99}.}
\tag{4}
\]

又

\[
b_2=10^{k-1},
\qquad
\frac1Q=\frac\lambda{b_2}\le\lambda,
\]

故

\[
\boxed{c_Q<\frac{a^2}{49}.}
\tag{5}
\]

最高层仍有

\[
1-t<5a,
\]

所以

\[
\boxed{
2\lambda(1-t)<\frac{a^2}{990}.}
\tag{6}
\]

---

## 3. Contact 把 `x` 收紧到 `0.52a^2`

沿用前文精确式

\[
t=(1-a)(1-x),
\]

以及

\[
z^2<a(1-x)^2.
\]

令

\[
B=1-a+a^2.
\]

由

\[
u=1-\lambda(1-t)
\]

和 prefix defect，可得

\[
F-a(1-x)^2
>
-a^2+B(2x-x^2)-2\lambda(1-t).
\tag{7}
\]

另一方面 contact 给出

\[
F-a(1-x)^2
<c_Q(a+t^2+z^2).
\tag{8}
\]

前文已有

\[
x<\frac{61}{100}a^2.
\]

所以

\[
x<10^{-4},
\qquad
B>\frac{99}{100},
\]

从而

\[
\boxed{
B(2x-x^2)>\frac{99}{50}x.
}
\tag{9}
\]

又

\[
a+t^2+z^2<1+2a<\frac{51}{50}.
\]

由 (5)：

\[
\boxed{
 c_Q(a+t^2+z^2)
<\frac{51}{2450}a^2.
}
\tag{10}
\]

将 (6)、(9)、(10) 代入 (7)–(8)：

\[
\frac{99}{50}x
<
a^2+rac{a^2}{990}+rac{51}{2450}a^2.
\]

右侧系数小于 `1.022`，故

\[
\boxed{x<\frac{13}{25}a^2.}
\tag{11}
\]

即

\[
\boxed{x<0.52\,10^{-4k}.}
\]

---

## 4. 常数核 `10d+e\le52`

由 (2)、(11)：

\[
\frac{10d+e}{100+ea^2}<\frac{13}{25}.
\]

因此

\[
10d+e
<52+\frac{13}{25}ea^2.
\]

由 (1)、`a^2\le10^{-4}`：

\[
\frac{13}{25}ea^2<0.004.
\]

左侧为整数，所以

\[
\boxed{10d+e\le52.}
\tag{12}
\]

立刻得到

\[
\boxed{d\in\{1,2,3,4,5\},}
\tag{13}
\]

以及逐个上界

\[
\boxed{
\begin{array}{c|c}
d&0\le e\le52-10d\\ \hline
1&42\\
2&32\\
3&22\\
4&12\\
5&2
\end{array}}
\tag{14}
\]

所以候选 constant-offset 类型总数至多

\[
43+33+23+13+3=115.
\]

---

## 5. 既约性进一步变成固定模数条件

由 (3)：

\[
a_1=10b_1+c,
\qquad c=10d+e.
\]

因此

\[
\gcd(a_1,b_1)
=
\gcd(c,b_1).
\]

原问题要求 `\gcd(a_1,b_1)=1`，所以每个常数类型还必须满足

\[
\boxed{
\gcd(10d+e,\ 10^{4k+1}-d)=1.
}
\tag{15}
\]

这里第一参数 `10d+e` 已经不超过 `52`。因此对固定 `(d,e)`，条件 (15) 只依赖 `10^{4k+1}` 在一个不超过 `52` 的固定模数中的周期。

这意味着 slope-4 取等边界已经从连续无界族降为：

\[
\boxed{
\text{至多 115 个固定常数类型}
+
\text{每个类型一个有限周期的 }k\text{ 同余条件}.}
\]

下一步可以把这些类型与 safe Vieta square / odd-prime routing 联立，而无需再允许任意十进制 mantissa。