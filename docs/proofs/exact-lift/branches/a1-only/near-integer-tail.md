# A1 minimal diagonal second-order near-integer tail lock

> 日期：2026-08-19。本文只研究已经由 `diagonal.md` 缩到的无界 minimal diagonal
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge3.
> \]
> 目标是保留上一轮 sharp significand lock 中被统一替换掉的 `10^{-k}`，把误差从固定 `1.2\times10^{-3}` 改写成随 `k` 衰减的 `O(10^{-k})`，并在原始 `\rho` 尺度上得到固定常数窗口。

状态：**本文中的不等式与推论均已严格完成。**

---

## 1. 输入与记号

沿用 `diagonal.md` 的 minimal diagonal 记号。令

\[
\delta=10^{-k},
\qquad
\varepsilon=10^{-2k}=\delta^2,
\]

因此

\[
0<\delta\le10^{-3},
\qquad
0<\varepsilon\le10^{-6}.
\]

第三分母正规化为

\[
\rho=\frac{b_3}{10^\ell},
\qquad
\sigma=\frac{b_3}{10^{m_3}}
=\frac\rho{10^k}
=\delta\rho,
\]

且

\[
0.1\le\sigma<1.
\]

prefix remainder 写成

\[
u=\frac{j}{10^{k+1}}.
\]

六个 minimal-surplus 类型仍满足

\[
(z,w)\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\},
\]

并令

\[
c=5-z\in\{4,2\}.
\]

已有 half-gap kernel 给出

\[
0<\phi_1<0.434,
\qquad
\phi_2=\frac z{10}\le0.3.
\]

已有 sharp significand 推导中的精确关系为

\[
\boxed{
 u
=5E
-\frac{w\varepsilon}{2}E
-\frac{cw\varepsilon}{10},
}
\tag{1}
\]

其中

\[
E=2(\phi_1+\phi_2)-1.
\]

positive excess decomposition 为

\[
\begin{aligned}
E
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon\phi_1+\frac RM\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}
+\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2,
\end{aligned}
\tag{2}
\]

并且

\[
\frac{\mathfrak h}{M\varepsilon}
=
\frac\lambda\varepsilon(A+\sigma B),
\tag{3}
\]

其中

\[
A=(1+\varepsilon\phi_1)-\delta(1-\varepsilon\phi_2),
\]

\[
B=\frac RM-\frac{r_3}{M},
\]

\[
\frac\lambda\varepsilon
=
\frac1{100-(10w-1)\varepsilon}.
\]

本文只在这些已经证明的恒等式上做一轮保留 `\delta` 的误差 bookkeeping。

---

## 2. 不再把 `delta` 粗化成 `10^-3`

定义主中心

\[
\boxed{
X=1+\sigma-\delta.
}
\tag{4}
\]

注意

\[
1.099<X<2.
\]

### 2.1 `A` 的二阶误差

由定义

\[
A
=1-\delta
+\varepsilon\phi_1
+\delta\varepsilon\phi_2.
\]

利用

\[
\phi_1<0.434,
\qquad
\delta\phi_2\le0.001\cdot0.3=0.0003,
\]

得到

\[
\boxed{
1-\delta<A<1-\delta+0.435\varepsilon.
}
\tag{5}
\]

### 2.2 `B` 的二阶误差

已有 carrier bounds 给出

\[
1-\varepsilon\phi_2
<\frac RM
<1+\varepsilon\phi_1.
\]

最高层还有

\[
0<\frac{r_3}{M}<10^{-3k}=\delta^3
\le0.001\varepsilon.
\]

因此

\[
\boxed{
1-0.301\varepsilon
<B
<1+0.434\varepsilon.
}
\tag{6}
\]

### 2.3 外层 factor 的二阶误差

令

\[
F=1+\varepsilon\phi_1+\frac RM.
\]

由同一组 bounds：

\[
\boxed{
2-0.3\varepsilon
<F
<2+0.868\varepsilon.
}
\tag{7}
\]

另一方面 `w\le4`，故

\[
\frac\lambda\varepsilon
\le
\frac1{100-39\varepsilon}
=
0.01\frac1{1-0.39\varepsilon}.
\]

当 `\varepsilon\le10^{-6}` 时

\[
(1+0.391\varepsilon)(1-0.39\varepsilon)
=1+0.001\varepsilon-0.15249\varepsilon^2>1,
\]

所以

\[
\boxed{
0.01
<\frac\lambda\varepsilon
<0.01(1+0.391\varepsilon).
}
\tag{8}
\]

---

## 3. 第一 positive source 的 `delta`-精确中心

记 (2) 的第一项为

\[
S_1
:=
\frac\lambda\varepsilon(A+\sigma B)F.
\]

### 3.1 下界

由 (5)–(8)：

\[
A+\sigma B
>
(1-\delta)+\sigma(1-0.301\varepsilon)
=X-0.301\sigma\varepsilon.
\]

因此

\[
S_1
>
0.01
(X-0.301\sigma\varepsilon)
(2-0.3\varepsilon).
\]

展开：

\[
\begin{aligned}
S_1
>{}&0.02X
-0.003X\varepsilon
-0.00602\sigma\varepsilon
+0.000903\sigma\varepsilon^2.
\end{aligned}
\]

因为 `X<2`、`sigma<1`，得到安全粗化

\[
\boxed{
S_1>0.02X-0.0121\varepsilon.
}
\tag{9}
\]

### 3.2 上界

由 (5)–(8)：

\[
A+\sigma B
<X+0.869\varepsilon.
\]

所以

\[
S_1
<
0.01(1+0.391\varepsilon)
(X+0.869\varepsilon)
(2+0.868\varepsilon).
\]

对右侧直接展开。一次项系数在 `X<2` 时严格小于

\[
0.01\bigl(0.868\cdot2+2\cdot0.869+2\cdot0.391\cdot2\bigr)
=0.05038.
\]

二次与三次项在 `\varepsilon\le10^{-6}` 下总计小于
`2\times10^{-8}\varepsilon`。因此可安全写成

\[
\boxed{
S_1<0.02X+0.0504\varepsilon.
}
\tag{10}
\]

于是第一 source 的真正中心是

\[
\boxed{0.02(1+\sigma-\delta),}
\]

而不是上一轮统一粗化后使用的 `0.02(1+sigma)`。

---

## 4. 全 excess 的二阶夹逼

其余三个 source 都是非负项。

第三半径项满足

\[
0<\frac{(r_3/M)^2}{\varepsilon}
<10^{-4k}=\varepsilon^2.
\tag{11}
\]

曲率项满足

\[
0<2\phi_1+\phi_2^2-\phi_1^2<0.958,
\]

故

\[
0<
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
<0.958\varepsilon.
\tag{12}
\]

最后

\[
0<\varepsilon^2\phi_1^2
<0.189\varepsilon^2.
\tag{13}
\]

由 (9)–(13)：

\[
\boxed{
0.02X-0.0121\varepsilon
<E
<0.02X+1.009\varepsilon.
}
\tag{14}
\]

特别地，因为 `X<2`、`varepsilon<=10^-6`，有

\[
\boxed{E<0.041.}
\tag{15}
\]

---

## 5. 从 `u` 恢复到原始 `rho` 尺度

把 (14) 代回精确式 (1)。

### 5.1 `u` 的下界

利用 `w\le4`、`c\le4` 和 (15)：

\[
\frac{w\varepsilon}{2}E
<2\varepsilon\cdot0.041
=0.082\varepsilon,
\]

\[
\frac{cw\varepsilon}{10}
\le1.6\varepsilon.
\]

所以

\[
\begin{aligned}
u
&>5(0.02X-0.0121\varepsilon)
-0.082\varepsilon
-1.6\varepsilon\\
&=0.1X-1.7425\varepsilon.
\end{aligned}
\]

即

\[
\boxed{
u>0.1X-1.7425\varepsilon.}
\tag{16}
\]

### 5.2 `u` 的上界

(1) 的后两项非负，因此

\[
u<5E.
\]

由 (14)：

\[
\boxed{
u<0.1X+5.045\varepsilon.}
\tag{17}
\]

合并：

\[
\boxed{
-1.7425\varepsilon
<
 u-\frac{1+\sigma-\delta}{10}
<5.045\varepsilon.
}
\tag{18}
\]

这就是上一版 sharp significand lock 的二阶版本。

---

## 6. near-integer tail theorem

因为

\[
10u=\frac j{10^k}=\delta j,
\qquad
\sigma=\delta\rho,
\]

把 (18) 乘以 `10/delta` 得

\[
-17.425\delta
<
j-10^k-\rho+1
<50.45\delta.
\tag{19}
\]

而 `k>=3` 给出 `delta<=10^-3`。所以全体无界 minimal diagonal 上统一有

\[
\boxed{
-0.0175
<
j-10^k-\rho+1
<0.0505.
}
\tag{20}
\]

令

\[
\boxed{N=j-10^k+1\in\mathbb Z.}
\tag{21}
\]

则 (20) 等价于

\[
\boxed{
N-0.0505
<\rho
<N+0.0175.
}
\tag{22}
\]

也就是说，虽然 `rho` 本身处在随 `k` 增长的 decade

\[
10^{k-1}\le\rho<10^k,
\]

但它到一个明确整数 `N` 的距离始终小于 `0.0505`，且上、下两侧还具有明显不对称性。

这是一个 **与 `k` 无关的常数窗口**。

---

## 7. 十进制尾位直接坍缩

若 `rho` 不是整数，记其小数部分为 `{rho}`。

由 (22) 只有两种可能：

\[
\rho\ge N
\Longrightarrow
0<\{\rho\}<0.0175,
\]

或

\[
\rho<N
\Longrightarrow
0.9495<\{\rho\}<1.
\]

连同整数情形可统一写成

\[
\boxed{
\{\rho\}
\in
[0,0.0175)
\cup
(0.9495,1).
}
\tag{23}
\]

由于

\[
\rho=\frac{b_3}{10^\ell},
\]

小数点恰好位于 `b_3` 的前 `k` 位之后。因此：

\[
\boxed{
\text{`b_3` 的前 `k` 位之后紧接的下一位十进制数字只能是 `0` 或 `9`.}
}
\tag{24}
\]

这比上一轮只同步 leading significand 的结论更强：现在第三分母在 prefix/tail 分界处已经出现一个真实的十进制 digit collapse。

---

## 8. 整数尾与小分母排除

### 8.1 整数尾精确化

若

\[
\rho\in\mathbb Z,
\]

则

\[
j-10^k-\rho+1
\]

也是整数。区间 (20) 中唯一的整数是 `0`，所以

\[
\boxed{
\rho=j-10^k+1.
}
\tag{25}
\]

特别地，若 normalized tail

\[
\rho=h2^x5^y
\]

满足

\[
x\ge0,
\qquad y\ge0,
\]

则 `rho` 自动为整数，因此

\[
\boxed{
 j=10^k-1+h2^x5^y.
}
\tag{26}
\]

这把 nonnegative `2/5` sector 中的 prefix remainder 与 odd-prime supply 变成了**精确等式**，不再只是 significand 近似。

### 8.2 非整数尾必须有较大约分母

若

\[
\rho=\frac ad
\]

为既约非整数有理数，则它到任一整数的距离至少为 `1/d`。

由 (22)：

\[
\operatorname{dist}(\rho,\mathbb Z)<0.0505.
\]

因此

\[
\boxed{d\ge20.}
\tag{27}
\]

对

\[
\rho=h2^x5^y,
\qquad \gcd(h,10)=1,
\]

其既约分母精确为

\[
\boxed{
d=2^{\max(-x,0)}5^{\max(-y,0)}.
}
\tag{28}
\]

所以任何非整数 tail state 都必须满足

\[
\boxed{
2^{\max(-x,0)}5^{\max(-y,0)}\ge20.
}
\tag{29}
\]

这在 `(x,y)` 平面上挖掉了 nonnegative quadrant 周围的一整圈小负指数状态。例如：

- 只有 `x<0` 时必须 `x\le-5`；
- 只有 `y<0` 时必须 `y\le-2`；
- `x=-1,y=-1` 的分母 `10` 不可能；
- `x=-2,y=-1` 的分母 `20` 是第一个未被该粗界自动排除的双负例子。

---

## 9. 对当前 A1 前沿的意义

此前 `k=g>=3` 的 diagonal 已有：

- `X_0=Y_0=k` 的统一 `2/5` cross-corridor cap；
- odd-prime supply
  \[
  h=qs,
  \qquad q\mid Q,
  \]
  且 `b_1` 侧只允许完整选择 `1 mod 4` prime-power blocks；
- sharp significand lock
  \[
  \left|\frac j{10^k}-(1+\sigma)\right|<0.0012.
  \]

本文把第三条升级成原始 `rho` 尺度上的常数刚性：

\[
\boxed{
\rho
=j-10^k+1+\eta,
\qquad
-0.0505<\eta<0.0175.
}
\tag{30}
\]

因此下一步不应再把 `rho` 当作整个 decade 中连续漂移的尾参数。真正剩余的 tail geometry 已分成两类：

1. **整数尾 sector**：直接使用精确式
   \[
   j=10^k-1+h2^x5^y;
   \]
2. **非整数尾 sector**：约分母至少为 `20`，并且 `b_3` 在 prefix/tail 分界后的第一位只能为 `0` 或 `9`。

这给 denominator prime graph、`2/5` resonance 和 decimal digit geometry 提供了一个新的共同接口。
