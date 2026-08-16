# A1 square-denominator recovery — 2026-08-16

本文从 A1 的 normalized discriminant square 出发，对

\[
\rho=\frac{b_3}{10^\ell}
\]

本身做既约分母分析。结果把 saturated 支中的 denominator-only 证书推广到整个 A1，并给出一条完全避开旧 `a_3/\delta_3` 问题的全 A1 尾长锥。

本文结论均为 **已严格完成**。

---

## 1. `rho` 的既约表示

令

\[
T=10^\ell,
\qquad
\delta=\gcd(T,b_3),
\]

\[
\boxed{L=\frac T\delta,
\qquad
\tau=\frac{b_3}{\delta}.}
\]

则

\[
\gcd(L,\tau)=1,
\qquad
\boxed{\rho=\frac{b_3}{T}=\frac\tau L.}
\tag{1}
\]

A1 的 decade window 为

\[
\boxed{10^{g-1}\le\frac\tau L<10^g.}
\tag{2}
\]

---

## 2. 判别平方的既约分母必须是平方

沿用

\[
K=G^2C^2-D^2N.
\]

normalized discriminant square 写成

\[
\boxed{
V^2=K-2\rho DN
=K-\frac{2DN\tau}{L}.
}
\tag{3}
\]

因此

\[
V^2=rac{LK-2DN\tau}{L}.
\]

定义

\[
\boxed{c_0:=\gcd(L,2DN).}
\tag{4}
\]

由于 `gcd(L,tau)=1`，

\[
\begin{aligned}
\gcd(L,LK-2DN\tau)
&=\gcd(L,2DN\tau)\\
&=\gcd(L,2DN)\\
&=c_0.
\end{aligned}
\tag{5}
\]

所以 (3) 约成既约分数后，分母恰为

\[
\frac L{c_0}.
\]

一个既约有理数平方的分子、分母都必须是完全平方。因此存在非负整数 `w` 和正整数 `s`，满足

\[
\boxed{
L=c_0s^2,
}
\tag{6}
\]

\[
\boxed{
LK-2DN\tau=c_0w^2.
}
\tag{7}
\]

并且

\[
\boxed{V=\frac ws}
}
\tag{8}
\]

（符号可由根支吸收）。

因此：

\[
\boxed{
\frac{L}{\gcd(L,2DN)}
\text{ 必须是完全平方。}
}
\tag{9}
\]

因为 `L` 只有素因子 `2,5`，(9) 等价于：超过前缀 `2DN` 所能吸收的 `2/5` 指数，只能以偶数深度继续增长。

---

## 3. 通用 denominator-only 根公式

A1 的 normalized root formula 为

\[
r_3
=
\frac{
G\rho C\pm(D+\rho)V
}{DG(D+2\rho)}.
\tag{10}
\]

代入

\[
\rho=\frac\tau L,
\qquad
V=\frac ws,
\]

并清去 `L,s`：

\[
\boxed{
 r_3
=
\frac{
G\tau Cs\pm(DL+\tau)w
}{
sDG(DL+2\tau)
}.
}
\tag{11}
\]

原问题中

\[
r_3=\frac{a_3}{b_3}
\]

已经是既约分数，因此其既约分母必须整除 (11) 的整数分母：

\[
\boxed{
 b_3\mid sDG(DL+2\tau).
}
\tag{12}
\]

这就是覆盖整个 A1 的 denominator-only certificate。

当 `L=1` 时，`c_0=s=1`，(12) 自动退化为 saturated 已有的

\[
b_3\mid DG(D+2\tau).
\]

---

## 4. Reduced slope numerator `tau` 只来自 prefix × square-root tail

由

\[
b_3=\delta\tau
\]

和 (12)，首先有

\[
\tau\mid sDG(DL+2\tau).
\]

模 `tau` 化简：

\[
DL+2\tau\equiv DL\pmod\tau,
\]

故

\[
\tau\mid sD^2GL.
\]

又 `gcd(tau,L)=1`，于是

\[
\boxed{
\tau\mid sD^2G.
}
\tag{13}
\]

因此 `tau` 的全部素数供给被压入

\[
sD^2G,
\]

其中 `s^2=L/c_0` 只承担尾部必需的平方根尺度。

---

## 5. `L` 的纯前缀高度上界

由 decade window (2)：

\[
\tau\ge10^{g-1}L.
\tag{14}
\]

另一方面由 (13)：

\[
\tau\le sD^2G.
\tag{15}
\]

再由 `L=c_0s^2`，有

\[
s=\sqrt{\frac L{c_0}}\le\sqrt L.
\]

所以

\[
10^{g-1}L
\le\sqrt L\,D^2G.
\]

除以 `sqrt(L)`：

\[
\sqrt L
\le10^{1-g}D^2G.
\]

使用

\[
D=10^gQ
\]

得到

\[
\boxed{
L\le10^{2+2g}Q^4G^2.
}
\tag{16}
\]

更精确地，保留 `c_0` 可写成

\[
\boxed{
Lc_0\le10^{2+2g}Q^4G^2.
}
\tag{17}
\]

因为 (14)–(15) 实际给出

\[
10^{g-1}\sqrt{Lc_0}\le D^2G.
\]

---

## 6. 全 A1 的安全尾长锥

由 (12) 取绝对值：

\[
b_3
\le sDG(DL+2\tau).
\]

又

\[
b_3=\delta\tau,
\qquad
T=\delta L,
\]

所以

\[
T=\frac{Lb_3}{\tau}
\le
sLDG\left(\frac{DL}{\tau}+2\right).
\]

由 decade window

\[
\frac\tau L\ge10^{g-1},
\]

故

\[
\frac{DL}{\tau}
\le
\frac D{10^{g-1}}
=10Q.
\]

于是

\[
\boxed{
T\le sLDG(10Q+2)
\le L^{3/2}DG(10Q+2).
}
\tag{18}
\]

代入 (16)：

\[
L^{3/2}
\le
10^{3+3g}Q^6G^3.
\]

再用

\[
D=10^gQ,
\qquad
10Q+2<11Q,
\]

得到

\[
\boxed{
10^\ell=T
<11\cdot10^{3+4g}Q^8G^4.
}
\tag{19}
\]

令

\[
M=m_1+m_2.
\]

`Q` 恰有 `M` 位，并且

\[
G=b_1b_2<Q<10^M.
\]

所以

\[
T
<11\cdot10^{3+4g}\cdot10^{12M}
<10^{4g+12M+5}.
\]

由于 `ell` 是整数：

\[
\boxed{
\ell\le4g+12(m_1+m_2)+4.
}
\tag{20}
\]

这是一条覆盖 saturated 与 non-saturated 的、完全由安全 rational-contact / denominator recovery 推出的 A1 尾长锥。

---

## 7. 与旧尾长结论的证明边界

旧公共框架曾通过 `a_3/delta_3` primitive tail quadratic 给出更漂亮的统一线性尾界，但该整数化步骤在 `delta_3>1` 时存在审计问题。

本文 (20) 的常数较粗，但它具有两个优点：

1. 不要求 `delta|a_3`；
2. 根公式 (11) 与 denominator certificate (12) 可逐步审计，并在 `L=1` 时与 saturated 的独立证明完全一致。

因此在 A1 新主线中，(20) 可以作为当前**安全的全分支尾长锥**使用；以后若能独立修复旧更强尾界，再做替换。
