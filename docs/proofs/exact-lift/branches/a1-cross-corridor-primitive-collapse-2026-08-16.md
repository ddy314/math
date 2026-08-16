# A1 cross-corridor primitive collapse — 2026-08-16

本文继续 `a1-cross-corridor-reduction-2026-08-16.md`，证明其中最后两条可能无界的 cross corridors 实际也不能承载固定前缀下的无界尾族。

关键新输入只有一个：原问题中的第三分数

\[
r_3=\frac{a_3}{b_3}
\]

始终是既约分数。

本文结论均为 **已严格完成**。

---

## 1. 归一化第三块

记

\[
T=10^\ell,
\qquad
\rho=\frac{b_3}{T},
\qquad
\eta=\frac{a_3}{T}.
\]

于是

\[
r_3=\frac{\eta}{\rho}.
\]

由

\[
b_3=h2^{\ell+x}5^{\ell+y}
\]

有

\[
\boxed{\rho=h2^x5^y}.
\]

A1 rational-contact 判别式给出

\[
V^2=K-2\rho DN
\tag{1}
\]

对某个 `V\in\mathbf Q`。这里可以直接取

\[
V=\frac WT,
\]

因为 denominator-funnel 中

\[
W^2=T^2K-2Tb_3DN
=T^2(K-2\rho DN).
\]

由 rational-contact 根公式，归一化分子满足

\[
\boxed{
\eta
=
\rho\,
\frac{
G\rho C\pm(D+\rho)V
}{DG(D+2\rho)}.
}
\tag{2}
\]

所有 `C,D,G,N,K` 都只由固定前两块与 `g` 决定。

---

## 2. 第一交叉走廊 `\mathcal C_{2+5-}` 的二进结构

该走廊定义为

\[
x>x_*,
\qquad y<y_*.
\]

由 `x>x_*`，在 (1) 中二进赋值由 `K` 项严格主导：

\[
v_2(K)<v_2(2\rho DN).
\]

平方存在首先要求

\[
\boxed{k_2:=v_2(K)\text{ 为偶数}.}
\]

并且

\[
\boxed{v_2(V)=\frac{k_2}{2}.}
\tag{3}
\]

记

\[
d_2=v_2(D),
\qquad
g_2=v_2(G),
\qquad c_2=v_2(C).
\]

若

\[
x>d_2,
\]

则

\[
v_2(D+\rho)=d_2,
\qquad
v_2(D+2\rho)=d_2,
\]

因为

\[
v_2(\rho)=x>d_2,
\qquad
v_2(2\rho)=x+1>d_2.
\]

由 (2)，方括号中两项的二进赋值分别为

\[
g_2+c_2+x
\]

与

\[
d_2+\frac{k_2}{2}.
\]

因此无论是否发生额外抵消，都有

\[
v_2\!\left(
G\rho C\pm(D+\rho)V
\right)
\ge
\min\left(
g_2+c_2+x,\ d_2+\frac{k_2}{2}\right).
\]

代回 (2)：

\[
\boxed{
 v_2(\eta)
\ge
x+
\min\left(
g_2+c_2+x,\ d_2+\frac{k_2}{2}\right)
-(2d_2+g_2).
}
\tag{4}
\]

当

\[
x>d_2+\frac{k_2}{2}-g_2-c_2,
\]

最小值已经固定为第二项，故

\[
\boxed{
 v_2(\eta)
\ge
x-d_2-g_2+\frac{k_2}{2}.
}
\tag{5}
\]

特别地，若再有

\[
x>d_2+g_2-\frac{k_2}{2},
\]

则

\[
\boxed{v_2(\eta)>0.}
\tag{6}
\]

---

## 3. 既约性与 (6) 直接矛盾

在第一交叉走廊中

\[
u=\ell+x.
\]

只要

\[
u>0,
\]

就有

\[
2\mid b_3.
\]

由于

\[
\gcd(a_3,b_3)=1,
\]

必有

\[
v_2(a_3)=0.
\]

所以

\[
\boxed{
 v_2(\eta)
=v_2(a_3)-v_2(T)
=-\ell
\le0.
}
\tag{7}
\]

这与 (6) 矛盾。

因此定义显式阈值

\[
\boxed{
X_{\max}
=
\max\left(
 d_2,
 d_2+\frac{k_2}{2}-g_2-c_2,
 d_2+g_2-\frac{k_2}{2},
 -\ell
\right)
}
\]

时最后一项不适合做前缀常数；更干净地分两步写：

- 若 `x\ge0`，则自动 `u=\ell+x>0`；
- 对 `x<0`，只有有限多个 `x` 落在 `x_*<x<0`。

故真正可能向 `+\infty` 延伸的部分满足 `x\ge0`，并且一旦

\[
\boxed{
 x>
X_0:=
\max\left(
0,
 d_2,
 d_2+\frac{k_2}{2}-g_2-c_2,
 d_2+g_2-\frac{k_2}{2}
\right),
}
\tag{8}
\]

便产生 (6) 与 (7) 的矛盾。

所以：

\[
\boxed{
\mathcal C_{2+5-}
\text{ 中所有可行整数 }x\text{ 都有固定前缀上界。}
}
\tag{9}
\]

结合 decade window，固定 `x` 后 `y` 落在长度小于 `2` 的区间，因此 `y` 也只有有限多个值。

于是第一交叉走廊固定前缀下严格有限。

---

## 4. 第二交叉走廊 `\mathcal C_{2-5+}` 的五进结构

现在考虑

\[
x<x_*,
\qquad y>y_*.
\]

由 `y>y_*`，(1) 中五进赋值由 `K` 项严格主导：

\[
v_5(K)<v_5(2\rho DN).
\]

平方存在要求

\[
\boxed{k_5:=v_5(K)\text{ 为偶数},}
\]

并且

\[
\boxed{v_5(V)=\frac{k_5}{2}.}
\tag{10}
\]

记

\[
d_5=v_5(D),
\qquad g_5=v_5(G),
\qquad c_5=v_5(C).
\]

若

\[
y>d_5,
\]

由于 `2` 是五进单位，

\[
v_5(D+\rho)=d_5,
\qquad
v_5(D+2\rho)=d_5.
\]

由 (2) 得

\[
\boxed{
 v_5(\eta)
\ge
 y+
\min\left(g_5+c_5+y,\ d_5+\frac{k_5}{2}\right)
-(2d_5+g_5).
}
\tag{11}
\]

一旦

\[
y>d_5+\frac{k_5}{2}-g_5-c_5,
\]

有

\[
 v_5(\eta)
\ge
 y-d_5-g_5+\frac{k_5}{2}.
\]

若再有

\[
y>d_5+g_5-\frac{k_5}{2},
\]

便得到

\[
\boxed{v_5(\eta)>0.}
\tag{12}
\]

另一方面，只要

\[
v=\ell+y>0,
\]

就有 `5\mid b_3`，既约性强迫

\[
v_5(a_3)=0,
\]

所以

\[
\boxed{v_5(\eta)=-\ell\le0,}
\tag{13}
\]

与 (12) 矛盾。

如第一走廊一样，所有 `y<0` 且 `y_*<y<0` 的状态本来就是有限的；真正可能向 `+\infty` 延伸的部分有 `y\ge0`。因此定义

\[
\boxed{
Y_0=
\max\left(
0,
 d_5,
 d_5+\frac{k_5}{2}-g_5-c_5,
 d_5+g_5-\frac{k_5}{2}
\right),
}
\tag{14}
\]

则任何可行解必须满足

\[
\boxed{y\le Y_0.}
\tag{15}
\]

固定 `y` 后 decade window 把 `x` 限制在长度小于 `4` 的整数区间。

所以第二交叉走廊固定前缀下也严格有限。

---

## 5. 两条 cross corridors 均不能承载无界尾族

结合 §§2–4：

\[
\boxed{
\mathcal C_{2+5-}
\text{ 的 }x\text{ 有显式前缀上界};
}
\]

\[
\boxed{
\mathcal C_{2-5+}
\text{ 的 }y\text{ 有显式前缀上界}.
}
\]

再结合 decade window，两个走廊的另一坐标也随之只剩有限整数集合。

固定 `(h,x,y)` 后

\[
\rho=h2^x5^y
\]

固定，进而 `\theta=\rho/D` 固定，rational-contact quadratic 给出的 `r_3` 至多两个固定有理根。原问题要求 `b_3` 正好等于该固定有理数的既约分母，而

\[
b_3=10^\ell\rho,
\]

故每个根至多对应一个 `\ell`。

因此：

\[
\boxed{
\text{A1 的两个 cross corridors 均为 fixed-prefix finite。}
}
\tag{16}
\]

---

## 6. A1 fixed-prefix finite theorem

此前已经证明：

- resonance sectors：fixed-prefix finite；
- double-nonresonant 的 `++`、`--` 象限：fixed-prefix finite；
- 本文：两个 cross corridors：fixed-prefix finite。

而 `h\mid Q^2G` 本身只有有限多个可能值，`g` 又满足

\[
0\le g\le\min(s_2-1,s_1+1)
\]

并受到 rational-contact prefix gap 的进一步限制。

所以得到完整结论：

\[
\boxed{
\text{对任意固定的前两块 }(a_1,b_1,a_2,b_2),
\text{ A1 第三块候选集合是有限的。}
}
\tag{17}
\]

而且这个有限性不是抽象存在：上述文件给出了 `g`、`h`、resonance 状态、cross-corridor offset 与每个 offset 的 `\ell` 恢复规则，可转化为显式有限证书。

必须保留证明边界：

\[
\boxed{
\text{(17) 仍不等于全局 A1 空性。}
}
\]

前两块本身尚未得到 prefix-uniform 的绝对高度上界，因此不能把所有 fixed-prefix finite 集合的并集称为有限。

下一阶段的唯一任务已经从“控制第三尾”转为：利用本框架对前缀对象 `C,D,G,N,K` 的必要条件，证明所有可能前缀本身为空，或把前缀压入一个全局有限盒。
