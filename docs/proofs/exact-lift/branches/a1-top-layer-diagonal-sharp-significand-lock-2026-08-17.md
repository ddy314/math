# A1 top-layer diagonal sharp significand lock for `k>=3` — 2026-08-17

本文结合 `k=g=1,2` 两个有限证书，从此只研究 minimal diagonal 的无界部分

\[
\boxed{k=g\ge3.}
\]

上一版 significand lock 为

\[
\left|
\frac j{10^k}
-
1
-
\frac{b_3}{10^{m_3}}
\right|<0.03.
\]

利用 `k>=3` 后

\[
10^{-k}\le10^{-3},
\qquad
\varepsilon=10^{-2k}\le10^{-6},
\]

positive excess decomposition 中的误差可以再压两个数量级。

令

\[
\boxed{
\sigma=\frac{b_3}{10^{m_3}}\in[0.1,1),
}
\]

\[
\boxed{
 u=\frac{j}{10^{k+1}}.
}
\]

本文证明

\[
\boxed{
0.09989+0.09999\sigma
<u
<0.100005+0.100001\sigma.
}
\tag{1}
\]

因此

\[
\boxed{
\left|
\frac j{10^k}-(1+\sigma)
\right|<0.0012.
}
\tag{2}
\]

本文结论均为 **已严格完成**。

---

## 1. 输入

仍沿用 minimal diagonal 的

\[
\phi_1,
\qquad
\phi_2=\frac z{10}\le0.3,
\qquad
\varepsilon=10^{-2k},
\]

以及正项 excess

\[
E:=2(\phi_1+\phi_2)-1.
\]

`a1-top-layer-excess-decomposition-2026-08-17.md` 给出

\[
\begin{aligned}
E
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon\phi_1+\frac RM\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}
+\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2.
\end{aligned}
\tag{3}
\]

其中

\[
\frac{\mathfrak h}{M}
=\lambda A+\theta B,
\]

\[
A=(1+\varepsilon\phi_1)-10^{-k}(1-\varepsilon\phi_2),
\]

\[
B=\frac RM-\frac{r_3}{M}.
\]

在 diagonal 中

\[
\boxed{\theta=\sigma\lambda.}
\tag{4}
\]

而六类型始终有

\[
0<\phi_1<0.434.
\]

---

## 2. `lambda/epsilon` 的六位精度

minimal diagonal 有

\[
\frac\lambda\varepsilon
=
\frac1{100-(10w-1)\varepsilon},
\qquad w\le4.
\]

当 `k>=3` 时

\[
\varepsilon\le10^{-6},
\]

故

\[
100-(10w-1)\varepsilon
\ge100-39\cdot10^{-6}.
\]

于是

\[
\boxed{
0.01
<\frac\lambda\varepsilon
<0.010000004.
}
\tag{5}
\]

---

## 3. `A,B` 的统一上下界

因为

\[
10^{-k}\le0.001,
\]

有

\[
\boxed{A>1-10^{-k}\ge0.999.}
\tag{6}
\]

又

\[
A<1+\varepsilon\phi_1<1.000000434.
\tag{7}
\]

对 `B`，由

\[
R>r_2=M(1-\varepsilon\phi_2)
\]

和最高层

\[
\frac{r_3}{M}<10^{-3k}\le10^{-9}
\]

得到

\[
B
>1-0.3\varepsilon-10^{-3k}
>0.9999996.
\tag{8}
\]

另一方面

\[
B<\frac RM<\frac{10^kr_1}{M}
=1+\varepsilon\phi_1
<1.000000434.
\tag{9}
\]

---

## 4. 第一 positive source 的精确夹逼

由 (4)–(9)：

\[
\frac{\mathfrak h}{M\varepsilon}
=
\frac\lambda\varepsilon(A+\sigma B).
\]

下侧：

\[
\boxed{
\frac{\mathfrak h}{M\varepsilon}
>0.01(0.999+0.9999996\sigma).
}
\tag{10}
\]

上侧：

\[
\boxed{
\frac{\mathfrak h}{M\varepsilon}
<0.010000004\cdot1.000000434(1+\sigma).
}
\tag{11}
\]

同时

\[
1+\varepsilon\phi_1+R/M
>2-\varepsilon\phi_2
>1.9999997,
\tag{12}
\]

以及

\[
1+\varepsilon\phi_1+R/M
<2(1+\varepsilon\phi_1)
<2.000000868.
\tag{13}
\]

因此 (3) 第一 source 满足一个几乎精确的

\[
0.02(1+\sigma)
\]

比例。

---

## 5. 其余 source 总量小于 `10^{-6}` 量级

第三半径：

\[
\frac{(r_3/M)^2}{\varepsilon}
<10^{-4k}
\le10^{-12}.
\tag{14}
\]

曲率：

\[
2\phi_1+\phi_2^2-\phi_1^2
<2(0.434)+0.3^2
=0.958.
\]

所以

\[
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
<0.958\cdot10^{-6},
\tag{15}
\]

并且

\[
\varepsilon^2\phi_1^2<2\cdot10^{-13}.
\tag{16}
\]

---

## 6. 从 excess 转回 `u`

minimal diagonal 的精确关系为

\[
\boxed{
 u
=5E
-\frac{w\varepsilon}{2}E
-\frac{(5-z)w\varepsilon}{10}.
}
\tag{17}
\]

由 half-gap 上界 `E<0.068`、`w<=4`、`5-z<=4`，当 `epsilon<=10^-6` 时两个减项总和小于

\[
1.74\cdot10^{-6}.
\tag{18}
\]

把 (10)–(16) 代入 (3)，再代入 (17)，采用安全十进制粗化即可得到

\[
\boxed{
 u>0.09989+0.09999\sigma,
}
\tag{19}
\]

以及

\[
\boxed{
 u<0.100005+0.100001\sigma.
}
\tag{20}
\]

这就是 (1)。

---

## 7. sharpened significand lock

目标中心为

\[
\frac{1+\sigma}{10}
=0.1+0.1\sigma.
\]

由 (19)：

\[
\frac{1+\sigma}{10}-u
<0.00011+0.00001\sigma
<0.00012.
\]

由 (20)：

\[
u-\frac{1+\sigma}{10}
<0.000005+0.000001\sigma
<0.000006.
\]

因此统一有

\[
\boxed{
\left|
 u-\frac{1+\sigma}{10}
\right|<0.00012.
}
\tag{21}
\]

乘以 `10`：

\[
\boxed{
\left|
\frac j{10^k}-(1+\sigma)
\right|<0.0012.
}
\tag{22}
\]

即

\[
\boxed{
\left|
\frac j{10^k}
-1
-\frac{b_3}{10^{m_3}}
\right|<0.0012.
}
\tag{23}
\]

---

## 8. 全局 `j` 窗进一步缩窄

由

\[
0.1\le\sigma<1
\]

和 (19)–(20)：

\[
u>0.09989+0.009999=0.109889,
\]

\[
u<0.100005+0.100001=0.200006.
\]

因此

\[
\boxed{
1.09889
<\frac j{10^k}
<2.00006.
}
\tag{24}
\]

与早先的

\[
1.079<j/10^k<2.02
\]

相比，两侧都明显收紧。

特别地 `j` 若达到或超过

\[
2\cdot10^k,
\]

则 (22) 强迫

\[
\sigma>0.9988.
\]

所以 `j` 以十进制数字 `2` 开头的尾部已被压到第三分母 significand 的最顶部 `0.12%`。

---

## 9. 当前意义

在 minimal diagonal 的全部无界范围 `k=g>=3` 中，moving prefix remainder `j` 与第三分母 significand `sigma` 已经在 `1.2×10^-3` 的绝对误差内同步。

配合 valuation normal form

\[
X_0=Y_0=k,
\]

下一步可以把 `(j,sigma)` 的数字锁直接叠加到 `rho=h2^x5^y` 的 resonance / cross-corridor 几何中，尝试获得对 `k` 本身的统一矛盾。
