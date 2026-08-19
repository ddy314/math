# A2 additive CRT quotient 的 exact source-scale normalization

> **依赖：** `endpoint-lattice.md` §§16.33–16.38、`source-discriminant.md`。
>
> **严格状态：**`endpoint-lattice.md` 已把三个 rational-root cofactor 的右 gap `Delta_+` 固定在模 `D^2-C^2` 的唯一 CRT 余类，但缺少商 `Q_Delta=floor(Delta_+/(D^2-C^2))` 的无界高度控制。本文首先把 §16.35 的 prefactor精确约成 `c_u^2 D`，再利用 source identities把 `S_+` 中唯一的 rational term完全整数化。最终 `D Delta_+` 成为显式 `(C,D,z,c_u,K,T,a_3)` 整数多项式；归一化后证明 `Q_Delta` 的尺度只剩 `c_u^2/g` 这一项 source allocation ratio。CRT、third-coordinate 与顶部 defect不再引入独立无界尺度。本文没有控制 `c_u^2/g`，所以不关闭 A2。

---

## 1. notation from the additive CRT core

沿用 dangerous reflection core：

\[
L:=2^m5^d,
\qquad
D=gL,
\qquad
T=10^m=L5^\lambda,
\]

\[
N_s:=3D-C,
\qquad
r:=\frac{N_s}{D}=3-\frac CD,
\]

以及

\[
0<\frac CD<\frac3{250}.
\tag{1.1}
\]

第三块写成

\[
\zeta:=\frac{a_3}{T},
\qquad
1<\zeta<\frac{251}{250}.
\tag{1.2}
\]

§16.35 定义

\[
\Delta_+
=\frac{A\mathscr S_+}
{2^{2M+2}5^{\nu_5}DL},
\qquad
A=b_2^2T,
\tag{1.3}
\]

其中

\[
\nu_5=\lambda-2d,
\]

以及

\[
\begin{aligned}
\mathscr S_+={}&
TK^2-4a_3K
-T^2\frac{f(r)}{h(r)}\\
&+(r+7)(2a_3-2KT)
+(r^2+7r+37)T,
\end{aligned}
\tag{1.4}
\]

\[
f(r)=r(Tr+2a_3)(K-r)^2,
\qquad
h(r)=(Tr+a_3)^2.
\tag{1.5}
\]

---

## 2. the huge prefactor collapses exactly to `c_u^2 D`

当前 denominator normal form为

\[
b_2=2^{M+m+1}c_ug.
\tag{2.1}
\]

因此 (1.3) 的 prefactor为

\[
\frac{b_2^2T}
{2^{2M+2}5^{\nu_5}DL}.
\]

使用 `D=gL`：

\[
\begin{aligned}
\frac{b_2^2T}
{2^{2M+2}5^{\nu_5}DL}
&=
\frac{2^{2M+2m+2}c_u^2g^2T}
{2^{2M+2}5^{\nu_5}gL^2}\\
&=
\frac{2^{2m}c_u^2gT}
{5^{\nu_5}L^2}.
\end{aligned}
\]

由于

\[
L=2^m5^d,
\qquad
\nu_5+2d=\lambda,
\qquad
T=L5^\lambda,
\]
得到

\[
\boxed{
\frac{b_2^2T}
{2^{2M+2}5^{\nu_5}DL}
=c_u^2D.}
\tag{2.2}
\]

所以右 gap具有极简 exact form：

\[
\boxed{\Delta_+=c_u^2D\mathscr S_+.}
\tag{2.3}
\]

这一步已经把原 cofactor / rational-root normalization 的所有巨大公共 scale约掉。

---

## 3. naturalize the only rational term

source identities给

\[
Tr+a_3=\frac{H_0}{g}
=\frac{c_uW_q}{g},
\tag{3.1}
\]

以及

\[
K-r
=K-\frac{N_s}{D}
=\frac{DK-N_s}{D}
=\frac{qW_q}{D}.
\tag{3.2}
\]

另有

\[
z=q5^\lambda,
\qquad
\frac{qgT}{D}=q5^\lambda=z.
\tag{3.3}
\]

把 (3.1)–(3.3) 代入 (1.5)：

\[
\boxed{
T^2\frac{f(r)}{h(r)}
=
\frac{
 z^2N_s(TN_s+2a_3D)
}{c_u^2D^2}.}
\tag{3.4}
\]

因此 (2.3) 中唯一的 rational source term也完全可乘回整数平面。

---

## 4. fully integral formula for `D Delta_+`

把 (3.4) 代入 (1.4)，并用 `r=N_s/D`，得到

\[
\boxed{
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
D^2(TK^2-14KT-4Ka_3+37T+14a_3)\\
&\qquad
+DN_s(-2KT+7T+2a_3)
+TN_s^2
\Bigr]\\
&-z^2N_s(TN_s+2a_3D).
\end{aligned}}
\tag{4.1}
\]

所有量均为原 endpoint/source integers；`f(r)/h(r)` 已消失。

再用 `N_s=3D-C`，(4.1) 等价于

\[
\boxed{
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
C^2T+2CDKT-13CDT-2CDa_3\\
&\qquad+D^2K^2T-20D^2KT-4D^2Ka_3
+67D^2T+20D^2a_3
\Bigr]\\
&+z^2\Bigl[
-C^2T+6CDT+2CDa_3
-9D^2T-6D^2a_3
\Bigr].
\end{aligned}}
\tag{4.2}
\]

所以 additive CRT quotient现在已有一个完全显式的 integer numerator。

---

## 5. normalized `S_+` is a quadratic in `K`

将

\[
r=3-C/D,
\qquad
\zeta=a_3/T
\]
代入 (1.4)，除以 `T`。精确得到

\[
\boxed{
\frac{\mathscr S_+}{T}
=
\frac{
\zeta^2K^2-2\mathcal L(r,\zeta)K+\mathcal C(r,\zeta)
}{(r+\zeta)^2},}
\tag{5.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal L(r,\zeta)={}&
2r^2\zeta+7r^2+5r\zeta^2+14r\zeta\\
&+2\zeta^3+7\zeta^2,
\end{aligned}}
\tag{5.2}
\]

\[
\boxed{
\begin{aligned}
\mathcal C(r,\zeta)={}&
2r^3\zeta+7r^3+5r^2\zeta^2+28r^2\zeta+37r^2\\
&+2r\zeta^3+35r\zeta^2+74r\zeta
+14\zeta^3+37\zeta^2.
\end{aligned}}
\tag{5.3}
\]

在 current box中 `L,C>0`。

首项 coefficient满足

\[
\boxed{
\frac1{16}
<\frac{\zeta^2}{(r+\zeta)^2}
<\frac4{63}.}
\tag{5.4}
\]

左端由 `r<3, zeta>1` 严格得到；右端可在 box端点直接验证。

---

## 6. fixed quadratic window for `S_+`

§16.35 已证明

\[
\frac{\mathscr S_+}{T}
>\frac{K^2}{16}-28K.
\]

由于

\[
K>9\cdot10^{11}>7616,
\]
有

\[
\boxed{
\frac{\mathscr S_+}{T}>rac{K^2}{17}.}
\tag{6.1}
\]

对上界，(5.1) 中 linear term严格为负；在

\[
2.988<r<3,
\qquad
1<\zeta<1.004
\]
内粗略有

\[
\frac{\mathcal C(r,\zeta)}{(r+\zeta)^2}<2500.
\]

结合 (5.4)：

\[
\frac{\mathscr S_+}{T}
<\frac4{63}K^2+2500.
\]

而 `K>9*10^11` 远强于 `K^2/315>2500`，故

\[
\boxed{
\frac{\mathscr S_+}{T}<\frac{K^2}{15}.}
\tag{6.2}
\]

综上：

\[
\boxed{
\frac{TK^2}{17}
<\mathscr S_+
<\frac{TK^2}{15}.}
\tag{6.3}
\]

---

## 7. `Q_Delta` has only one unbounded source scale

additive CRT modulus为

\[
M_\Delta:=D^2-C^2
=D^2\left(1-(C/D)^2\right).
\]

由 (2.3)：

\[
\boxed{
\frac{\Delta_+}{D^2-C^2}
=
\frac{c_u^2\mathscr S_+}
{D\left(1-(C/D)^2\right)}.}
\tag{7.1}
\]

定义唯一剩余的 source allocation scale

\[
\boxed{
\mathfrak a_\Delta
:=\frac{c_u^2TK^2}{D}
=\frac{c_u^25^\lambda}{g}K^2.}
\tag{7.2}
\]

因为 `0<C/D<3/250`，

\[
1<\frac1{1-(C/D)^2}<\frac{1001}{1000}.
\]

结合 (6.3)：

\[
\boxed{
\frac{\mathfrak a_\Delta}{17}
<
\frac{\Delta_+}{D^2-C^2}
<
\frac{\mathfrak a_\Delta}{14}.}
\tag{7.3}
\]

因此

\[
\boxed{
\frac{\mathfrak a_\Delta}{17}-1
< Q_\Delta
<\frac{\mathfrak a_\Delta}{14}.}
\tag{7.4}
\]

所以 `Q_Delta` 的无界性已被严格隔离到单一 scalar

\[
\boxed{c_u^2/g.}
\]

`C/D`、`a_3/T`、三 cofactor 与 CRT residue本身都只在固定窄区间内改变常数因子。

---

## 8. revised CRT frontier

此前 README 把下一缺口写成“控制无界 CRT 商 `Q_Delta`”。本文将其收紧为：

\[
\boxed{
\text{控制 source allocation ratio }c_u^2/g.}
\tag{8.1}
\]

一旦 `c_u^2/g` 在某个 allocation branch获得上下界，(7.3) 会立刻把 `Q_Delta` 压成对应的 finite / short interval；无需重新分析 cubic cofactor 或 CRT residue。

因此最值得与本文联立的是已经包含 `c_u,g` 的 Gaussian/source allocation equations，而不是继续对 `Delta_+` 做独立粗估计。

A2 仍为 `待证`。
