# A2 moving endpoint-height common channel 的 singular no-go

> **依赖：** `spontaneous-height-parity-ledger.md`、`primitive-reduction.md`。
>
> **严格状态：**`spontaneous-height-parity-ledger.md` 已把 genuine endpoint-external height prime 同时进入 angle/additive common gcd 的 first-layer geometry降成纯 decimal system
> \[
> H_1H_2=0,\qquad J_H=0.
> \]
> 本文对两个 sphere orientations逐一完成 singular bad-reduction audit。结论是：对任意 genuine non-`3` inert external prime，full three-variable system没有 surviving singular Hensel tree。`H_1` 本身在 genuine locus光滑；`H_2` 的 intrinsic singularity只出现在 `x=-2` denominator boundary。若 `J_H` 对 decimal phase出现 repeated root，第一 orientation只有三个 genuine singular primes `102251,630451,136776907`，第二 orientation只有 `8971`；四个有限状态全部在 `p^2` carry compatibility上失败。`p=11` 单独审计后也只有 `x=y=0` boundary。本文不排除 simple moving roots，因此不关闭 height pool或 A2；它删除的是 moving height common channel 的最后一类 singular branching 解释。

---

## 1. normalized moving system

沿用

\[
x:=\frac BN,
\qquad
y:=\frac{10A}{N},
\qquad
\tau:=N^{-1}=10^{-M}.
\]

`spontaneous-height-parity-ledger.md` 的两个 orientation polynomials 为

\[
\boxed{
H_1
=202500x^4+(101x^2+4x+4)y^2,}
\tag{1.1}

\[
\boxed{
\begin{aligned}
H_2={}&
410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{1.2}

additive-height carrier `J_H` 除去 decimal unit后为

\[
\boxed{
\begin{aligned}
G_H(x,y,\tau)
={}&100x^2\left[5(y+9)^2-36(y+9)\tau+55\tau^2\right]\\
&-(x+2)^2(2025x^2+y^2).
\end{aligned}}
\tag{1.3}

所以 genuine external common prime必须在某个 orientation上满足

\[
\boxed{H_i=G_H=0\pmod p.}
\tag{1.4}

本文固定

\[
p\equiv3\pmod4,
\qquad p\ne3,5,
\]
并使用 external separation：

\[
\boxed{x\ne0,\quad y\ne0,\quad x+2\ne0\pmod p.}
\tag{1.5}

最后一项就是 `p\nmid Q`；fixed denominator `23` 等非-external channel不属于本文。

---

## 2. full-system singularity 的两种来源

因为

\[
\partial_\tau H_i=0,
\]
若

\[
\partial_\tau G_H\ne0,
\]
则只要 `grad H_i` 非零，两行 Jacobian自动线性独立。

因此 rank drop只能来自：

1. `H_i` 自身 intrinsic singular：
   \[
   H_i=H_{i,x}=H_{i,y}=0;
   \]
2. phase repeated root：
   \[
   G_{H,\tau}=0,
   \]
   且两个 `(x,y)` gradients线性相关。

下面分别审计。

---

# I. intrinsic sphere-orientation singularity

## 3. `H_1` 在 genuine locus 自动光滑

写

\[
C_1(x):=101x^2+4x+4.
\]
则

\[
H_1=202500x^4+C_1y^2,
\]

\[
H_{1,y}=2C_1y.
\]

在 genuine locus中 `p` 为奇数且 `y` 是 unit。若 `H_{1,y}=0`，则

\[
C_1=0.
\]
代回 `H_1=0`：

\[
202500x^4=0.
\]
由于 `p\ne2,3,5` 且 `x` 为 unit，矛盾。因此

\[
\boxed{\nabla H_1\ne0}
\tag{3.1}

对所有 genuine target primes成立。

---

## 4. `H_2` intrinsic singularity 只剩 denominator boundary

消去 `y` 得

\[
\boxed{
\begin{aligned}
\operatorname{Res}_y(H_2,H_{2,y})
={}&c_y\,x^{14}(x+2)^4 C_2(x)A_6(x),
\end{aligned}}
\tag{4.1}

其中 `c_y` 只含 `2,3,5`，

\[
C_2=101x^2+4x+4,
\]

\[
\boxed{
A_6=
64478501x^6+1908012x^5+9602508x^4+106144x^3
+438960x^2+4800x+8000.}
\tag{4.2}

另一方面

\[
\boxed{
\operatorname{Res}_y(H_2,H_{2,x})
=c_x\,x^{16}(x+2)^4A_8(x),}
\tag{4.3}

`c_x` 同样只含 `2,3,5`，且

\[
\boxed{
\begin{aligned}
A_8={}&6512328601x^8+708537220x^7+1501885036x^6
+121752064x^5\\
&+219524016x^4+3371072x^3+8584000x^2+89600x+128000.
\end{aligned}}
\tag{4.4}

非边界 common x-root只能来自 `C_2A_6` 与 `A_8`。两个整数 resultant 分别为

\[
\boxed{
\operatorname{Res}(C_2,A_8)
=2^{24}13^2 101^2\cdot59729\cdot22177889,}
\tag{4.5}

\[
\boxed{
\begin{aligned}
\operatorname{Res}(A_6,A_8)
={}&2^{72}5^9 17^6\cdot31\cdot47^6\cdot101^6\cdot181^2\cdot251\\
&\cdot371069497788281179471251313.
\end{aligned}}
\tag{4.6}

限制到 non-`3` inert prime，只剩

\[
\boxed{31,47,251.}
\tag{4.7}

checker 在这三个有限域上直接计算 polynomial gcd：

- `p=31` 的非边界 resultant gcd只有 `x=8`，但 `H_2,H_{2,x},H_{2,y}` 在该 `x` 下没有共同 `y`；
- `p=47` 的非边界 x-gcd为 `1`；
- `p=251` 的非边界 resultant gcd只有 `x=51`，同样没有共同 `y`。

完整 singular states 中出现的其余点都来自共享显式因子

\[
x+2=0,
\]
即 denominator boundary，违反 (1.5)。因此

\[
\boxed{H_2\text{ 在 genuine external locus也无 intrinsic singular point}.}
\tag{4.8}

---

# II. repeated decimal-phase branch

## 5. `p != 11` 时 repeated `tau` 精确降成同一个 `D_H`

由 (1.3)：

\[
G_{H,\tau}
=100x^2\left[-36(y+9)+110\tau\right].
\]
对 `p\ne11` 且 `x` 为 unit：

\[
\boxed{
G_{H,\tau}=0
\iff
55\tau=18(y+9).}
\tag{5.1}

代入

\[
\tau=\frac{18}{55}(y+9)
\]
后有精确恒等式

\[
\boxed{
G_H=-\frac1{11}D_H(x,y),}
\tag{5.2}

其中

\[
\boxed{
\begin{aligned}
D_H={}&22275x^4+89100x^3+991x^2y^2+17640x^2y\\
&+168480x^2+44xy^2+44y^2.
\end{aligned}}
\tag{5.3}

因为在 repeated root上 `G_{H,\tau}=0`，chain rule给

\[
(G_{H,x},G_{H,y})
=-\frac1{11}(D_{H,x},D_{H,y}).
\]
所以 full rank drop等价于 plane intersection

\[
H_i=D_H=0
\]
本身为 singular intersection。

---

## 6. orientation `H_1`: fixed bad primes

直接消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_1,D_H)
=164025x^4P_1(x),}
\tag{6.1}

其中

\[
\boxed{
\begin{aligned}
P_1={}&240046103025x^8-431151600x^7+18108996360x^6
-937618080x^5\\
&+354227216x^4+108902528x^3+76745984x^2
+8466432x+2768896.
\end{aligned}}
\tag{6.2}

其判别式为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(P_1)
={}&2^{120}3^75^{34}7^{28}11^4 13^4 89^2 101^4 367^2\\
&\cdot102251\cdot630451\cdot136776907.
\end{aligned}}
\tag{6.3}

因此 non-`3` inert bad-reduction候选为

\[
\boxed{7,11,367,102251,630451,136776907.}
\tag{6.4}

`7` 没有 full singular state，`367` 没有 `F_p` repeated x-root；`11` 稍后单列。剩下三个 prime各有唯一 genuine finite state：

\[
\boxed{
\begin{array}{c|c|c|c}
p&x_0&y_0&\tau_0\\ \hline
102251&61220&95782&35068\\
630451&340435&610253&474828\\
136776907&4766067&102799536&58512016
\end{array}}
\tag{6.5}

其中 `tau_0=18(y_0+9)/55 mod p`。

---

## 7. `H_1` 三个 singular states 全部没有 `p^2` lift

在标准 representatives上写

\[
x=x_0+pX,\quad y=y_0+pY,\quad\tau=\tau_0+pT_1.
\]

两行 Jacobian模 `p` 线性相关：

\[
\nabla G_H=c_p\nabla H_1.
\]

对应 carry compatibility residual

\[
\boxed{
r_p
:=\frac{G_H(x_0,y_0,\tau_0)}p
-c_p\frac{H_1(x_0,y_0)}p
\pmod p}
\tag{7.1}

必须为 `0` 才能 lift。exact certificate给

\[
\boxed{
\begin{array}{c|c|c}
p&c_p&r_p\\ \hline
102251&51620&99510\\
630451&365778&401091\\
136776907&46110684&133381104
\end{array}}
\tag{7.2}

三者都非零。因此

\[
\boxed{
\text{orientation }H_1\text{ 没有 surviving repeated-phase singular lift}.}
\tag{7.3}

---

## 8. orientation `H_2`: fixed bad primes

消去 `y` 得

\[
\boxed{
\operatorname{Res}_y(H_2,D_H)
=430467210000\,x^8(25x^2+1)^2P_2(x),}
\tag{8.1}

其中

\[
\boxed{
\begin{aligned}
P_2={}&629879737734025x^8+220216678224400x^7
+297840014098760x^6\\
&+74145474010720x^5+52673580295056x^4
+7788392965248x^3\\
&+3650462246144x^2+247566938112x+80965287936.
\end{aligned}}
\tag{8.2}

对 inert `p`，`25x^2+1=0` 没有 `F_p` root，因为这等价于 `-1` 为平方。因此只需看 `P_2`。

其判别式为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(P_2)
={}&2^{116}3^55^{26}7^{64}11^4 13^4 19^2 101^4
\cdot5827^2\cdot9323^2\\
&\cdot8971\cdot5019481^2\cdot833453052690874208617.
\end{aligned}}
\tag{8.3}

non-`3` inert candidates为

\[
\boxed{7,11,19,5827,8971,9323.}
\tag{8.4}

其中：

- `7,5827,9323` 没有 genuine full singular state；
- `19` 只给 `x=y=0` boundary；
- `11` 单列；
- `8971` 唯一给
  \[
  \boxed{(x_0,y_0,\tau_0)=(2914,6787,4997).}
  \tag{8.5}
  
该点 Jacobian比例与 carry residual为

\[
\boxed{c_{8971}=8281,\qquad r_{8971}=3710\ne0.}
\tag{8.6}

所以它也没有 `8971^2` lift。

因此

\[
\boxed{
\text{orientation }H_2\text{ 没有 surviving repeated-phase singular lift}.}
\tag{8.7}

---

## 9. exceptional `p=11` 的直接 full-system audit

`p=11` 时不能从 `G_{H,\tau}=0` 除以 `55`。因此 checker直接遍历

\[
(x,y,\tau)\in\mathbf F_{11}^3
\]
并同时检查

\[
H_i=G_H=0
\]
及两行 Jacobian rank `<2`。

两个 orientations 的全部 singular states都是

\[
\boxed{x=y=0,\qquad\tau\text{ arbitrary}.}
\tag{9.1}

它们违反 genuine conditions (1.5)。所以 `11` 不产生 external singular state。

---

## 10. final local classification

综合 intrinsic 与 repeated-phase 两部分：

\[
\boxed{
\text{genuine non-`3` inert moving height common channel
没有 surviving singular Hensel tree}.}
\tag{10.1}

所有能够继续到高 prime-power depth的 moving external common state都必须位于

\[
\boxed{H_i=G_H=0}
\]
的 simple branches。

这与 source、pure-`c_Q`、omega-content 等此前审计的模式一致：local singular mechanism 已经不是 A2 剩余 parity 的来源。

---

## 11. proof boundary

本文没有证明 moving height common prime不存在，也没有证明它对

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2)
\]
的 valuation 必为偶数。simple roots仍可沿真实 decimal orbit逐层 Hensel lift。

所以后续不得把本文解释成 height pool closure。真正剩余的是

\[
\boxed{
\text{simple moving decimal orbit}
+\text{natural representative / global parity allocation}.}
\]

若继续 height pool，最有价值的输入应来自 `W_q` 作为 reduced numerator 的真实 decimal representative，或 same-prime Gaussian orientation；再做 singular discriminant/resultant只会重复本文已经完成的局部审计。