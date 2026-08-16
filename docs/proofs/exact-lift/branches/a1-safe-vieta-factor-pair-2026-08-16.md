# A1 safe Vieta factor pair — 2026-08-16

本文从新的 universal integer-square certificate 构造一套覆盖整个 A1 的安全 Vieta 因子对，用来替代旧 primitive tail quadratic 中依赖 `a_3/\delta_3` 的部分。

核心恒等式：

\[
\boxed{
(TGC-W)(TGC+W)
=TDN(TD+2b_3).
}
\]

本文结论均为 **已严格完成**。

---

## 1. 起点：安全整数平方证书

沿用

\[
T=10^\ell,
\qquad
D=10^gQ,
\]

\[
G=b_1b_2,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2,
\]

\[
C=a_1 10^{n_2}+a_2,
\]

以及

\[
K=G^2C^2-D^2N.
\]

整个 A1 已严格证明存在整数 `W\ge0` 满足

\[
\boxed{
W^2=T^2K-2Tb_3DN.
}
\tag{1}
\]

代入 `K`：

\[
W^2
=T^2G^2C^2-T^2D^2N-2Tb_3DN.
\]

整理：

\[
(TGC)^2-W^2
=TDN(TD+2b_3).
\]

所以

\[
\boxed{
(TGC-W)(TGC+W)
=TDN(TD+2b_3).
}
\tag{2}
\]

---

## 2. 定义安全 Vieta 对

定义

\[
\boxed{F_-=TGC-W,}
\qquad
\boxed{F_+=TGC+W.}
\tag{3}
\]

由判别平方非退化性和 `W<TGC`（因为右侧 (2) 为正），二者均为正整数。

并且精确满足

\[
\boxed{F_-F_+=TDN(TD+2b_3),}
\tag{4}
\]

\[
\boxed{F_-+F_+=2TGC,}
\tag{5}
\]

\[
\boxed{F_+-F_-=2W.}
\tag{6}
\]

这是一套完全由安全 discriminant square 得到的整数因子对。

---

## 3. gcd 只来自固定交叉容量

由 (5)、(6)：

\[
\gcd(F_-,F_+)
\mid2TGC
\]

以及

\[
\gcd(F_-,F_+)
\mid2W.
\]

因此

\[
\boxed{
\gcd(F_-,F_+)\mid2\gcd(TGC,W).
}
\tag{7}
\]

特别地，若素数 `p` 满足

\[
\boxed{p\nmid2TGC,}
\]

则

\[
\boxed{
 p\nmid\gcd(F_-,F_+).
}
\tag{8}
\]

所以这样的 `p` 若进入右侧

\[
TDN(TD+2b_3),
\]

其完整 `p`-进指数不能在 `F_-`,`F_+` 两侧同时出现；它必须整块进入其中一侧。

---

## 4. 一个安全的 prime-power side routing

设

\[
p\nmid2TGC.
\]

若

\[
p^e\mid TDN(TD+2b_3),
\]

且 `e` 是该右侧的完整 `p`-进赋值，则由 (4)、(8)：

\[
\boxed{
\{v_p(F_-),v_p(F_+)\}=
\{e,0\}.
}
\tag{9}
\]

这给出一个新的“因子侧选择”变量，但它只有二元选择，且不存在局部容量共享。

与旧 Gaussian/Vieta 路线相比，这里没有引入任何错误的第三分子 primitive normalization。

---

## 5. 与 rational-contact root 的关系

判别平方中的有理平方根为

\[
z=\frac{W}{TDG}.
\]

因此

\[
F_-
=TG(C-Dz),
\qquad
F_+
=TG(C+Dz).
\tag{10}
\]

所以 `F_-` 是前缀接触中较小的 algebraic factor，`F_+` 是其共轭大因子。

又因为

\[
z^2=P^2-(1+2\theta)S,
\qquad
P=\frac CD,
\]

有

\[
C^2-D^2z^2
=D^2(1+2\theta)S.
\]

乘以 `T^2G^2` 正好恢复 (2)。

因此 safe Vieta pair 与 rational-contact discriminant 完全等价，只是把它整数化为 factor-pair 语言。

---

## 6. 当前用途

A1 现在有三套互相兼容的安全算术接口：

1. denominator funnel
   \[
   b_3\mid T^2D^2G;
   \]
2. integer gap
   \[
   TE=b_3U,
   \qquad U=LA,\ E=\tau A;
   \]
3. safe Vieta pair
   \[
   F_-F_+=TDN(TD+2b_3),
   \qquad F_-+F_+=2TGC.
   \]

后续处理 odd split pair-max、`2/5` 局部位置或 moving-prefix 常数核时，可以从 (4)–(9) 直接追踪 prime-power 落在哪个 factor side，而无需再调用旧 `z_3=a_3/\delta_3` quadratic。