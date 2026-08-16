# `A_2` decimal ellipse phase compression

> 分支：`agent/a2-hensel-resultant-progress`  
> 状态：**严格结构推进；得到 core-dependent Gaussian divisor window，尚未单独关闭整个 `A_2`。**  
> 依赖：`a2-only.md` 的 terminal deep-even/source split、旧 A2 工作稿中的 canonical discriminant 与 Gaussian companion：
> \[
> T^2=A^2-\Sigma\mathcal N,\qquad T^2+J^2=n\mathcal N.
> \]

本文把 source-side 尺度全部消去，将 \(n/\Sigma\)、canonical discriminant angle \(T/A\) 和真实十进制窗口直接联结起来。它的目标是把此前“二维 ellipse + decimal phase”变成可直接作用于 Gaussian divisor allocation 的定量不等式。

---

## 1. 记号

沿用 terminal A2：

\[
M=m_2,\qquad m=m_3,\qquad a=a_1\in\{5,7,9,11,13\},
\]

\[
x=\frac{b_2}{10^M},\qquad y=\frac{a_2}{10^{M-1}},\qquad w=\frac{b_3}{10^m}.
\]

source split：

\[
U=5^{M-\sigma_5},\quad D_0=2^{m+t-1}\rho,\quad H_s=D_0c_u,
\]

\[
c_Qq=U+H_s,\qquad Ux=2H_s.
\]

定义

\[
E=E_5,\qquad z=\frac{5^ED_0}{c_Q},
\]

\[
\Phi(x,z)=(99x-4)z-2x-4,
\]

\[
f=5^Eq+2c_u,\qquad \Sigma=c_Q^2qf,
\]

以及 source norm scale

\[
n=2c_u\sigma.
\]

canonical discriminant / Gaussian companion 使用

\[
A=10H_s5^dP,
\]

\[
A^2-T^2=\Sigma\mathcal N,
\qquad
T^2+J^2=n\mathcal N.
\]

同时

\[
J=-5^dL_0>0,
\qquad
L_0=-U10^{M-1}(25ax^2-y).
\]

---

## 2. `已严格完成`：第三块实尺度给出精确的 source normalized `z`

由 deep-even 第三分母正规形

\[
b_3=2^{m+M+1}5^{m-\lambda}c,
\qquad c=c_Qc_u,
\]

有

\[
w=\frac{b_3}{10^m}
=\frac{2^{M+1}c_Qc_u}{5^\lambda}.
\]

另一方面

\[
D_0=\frac{Ux}{2c_u}=\frac{5^{M-\sigma_5}x}{2c_u}.
\]

因此

\[
\begin{aligned}
z
&=\frac{5^{\lambda+\sigma_5}D_0}{c_Q}\\
&=\frac{5^{M+\lambda}x}{2c_uc_Q}\\
&=\frac{10^M x}{w}.
\end{aligned}
\]

即

\[
\boxed{z=\frac{10^Mx}{w}=\frac{b_2}{w}.}
\]

所以 \(z\) 不是新的无界自由尺度；一旦 \((M,b_2,b_3)\) 固定，它由真实十进制 phase 精确确定。

---

## 3. `已严格完成`：`n/Sigma` 的完全尺度消去

由前一研究文件的精确恒等式

\[
4\sigma=Uc_Q\Phi(x,z)
\]

以及

\[
c_u=\frac{Ux}{2D_0}
\]

得到

\[
n=2c_u\sigma
=\frac{U^2xc_Q}{4D_0}\Phi(x,z).
\]

另一方面

\[
q=\frac{U(x+2)}{2c_Q}.
\]

又

\[
\begin{aligned}
f
&=5^Eq+2c_u\\
&=\frac{U}{2D_0}\left(z(x+2)+2x\right).
\end{aligned}
\]

因此

\[
\Sigma=c_Q^2qf
=\frac{c_QU^2}{4D_0}(x+2)\left(z(x+2)+2x\right).
\]

两式相除：

\[
\boxed{
\frac n\Sigma
=
\frac{x\Phi(x,z)}{(x+2)(z(x+2)+2x)}.
}
\tag{3.1}
\]

所有 \(U,D_0,c_Q,c_u,q,f\) 尺度全部消失。

再用恒等式

\[
x\Phi(x,z)+(x+2)(z(x+2)+2x)
=4z(25x^2+1),
\]

可把 (3.1) 写成

\[
\boxed{
\frac n\Sigma
=
\frac{x(99x-4)}{(x+2)^2}
-
\frac{8x(25x^2+1)}{(x+2)^2\bigl(z(x+2)+2x\bigr)}.
}
\tag{3.2}
\]

因 terminal window 中 \(x>0,z>0\)，第二项严格为正。故

\[
\boxed{
0<\frac n\Sigma
<r_0(x):=\frac{x(99x-4)}{(x+2)^2}.
}
\tag{3.3}
\]

这里正性来自 \(n,\Sigma>0\)。特别地，它还重新推出

\[
\Phi(x,z)>0.
\]

由于 \(z=10^Mx/w\)，(3.2) 的误差是显式 \(O(10^{-M})\)；也就是说 source/denominator 比例被真实第二块十进制 phase 指数级贴近于单变量曲线 \(r_0(x)\)。

---

## 4. `已严格完成`：Gaussian angle 完全进入 `(x,y)` 窗口

由

\[
J=-5^dL_0
=5^dU10^{M-1}(25ax^2-y)
\]

和

\[
A=10H_s5^dP,
\qquad H_s=\frac{Ux}{2},
\qquad P=10^{M-1}(a+y),
\]

得到精确无尺度比值

\[
\boxed{
\frac JA
=\frac{25ax^2-y}{5x(a+y)}.
}
\tag{4.1}
\]

记

\[
r=\frac n\Sigma,\qquad
\tau=\frac TA,\qquad
\jmath=\frac JA.
\]

由

\[
T^2+J^2=n\mathcal N,
\qquad
A^2-T^2=\Sigma\mathcal N
\]

相除得到

\[
r=\frac{\tau^2+\jmath^2}{1-\tau^2},
\]

从而

\[
\boxed{
\tau^2=\frac{r-\jmath^2}{1+r}.
}
\tag{4.2}
\]

结合 \(r<r_0(x)\)，并注意右端关于 \(r\) 严格递增，得到

\[
\boxed{
\left(\frac TA\right)^2
<
H_a(x,y)
:=
\frac{r_0(x)-\left(\frac{25ax^2-y}{5x(a+y)}\right)^2}
{1+r_0(x)}.
}
\tag{4.3}
\]

在全部合法 core window 中已有 \(25ax^2-y>0\)。直接求导可见

\[
\frac{\partial}{\partial y}
\frac{25ax^2-y}{5x(a+y)}
<0,
\]

故 \(H_a(x,y)\) 关于 \(y\) 递增。由于 \(y<1\)，

\[
H_a(x,y)<H_a(x,1).
\]

而后者惊人地化成

\[
\boxed{
H_a(x,1)
=-\frac{
25a^2x^4+100a^2x^3-(200a+99)x^2+4x+4
}{100x^2(a+1)^2}.
}
\tag{4.4}
\]

并有

\[
\boxed{
\frac{d}{dx}H_a(x,1)
=-\frac{(x+2)(25a^2x^3-2)}{50x^3(a+1)^2}.
}
\tag{4.5}
\]

因此每个 core 的最大值只有一个可能内临界点；不存在复杂的二维连续优化。

---

## 5. `已严格完成`：五个 core 的显式 angle cap

在 `a2-only.md` 的严格实窗口上，(4.4)–(4.5) 给出：

\[
\boxed{
\begin{array}{c|c}
a&T/A\\ \hline
5&<3/8\\
7&<31/100\\
9&<13/50\\
11&<21/100\\
13&<1/6
\end{array}}
\tag{5.1}
\]

说明：对 \(a=5,7\)，唯一临界点由 \(25a^2x^3=2\) 给出；对 \(a=9,11,13\)，该临界点已经落在合法 \(x\)-窗口左侧，所以最大值在 \(x=1/10\) 端点。附带 checker 使用精确有理 Sturm root count 验证对应阈值多项式在整个闭区间无零点且为正，因此 (5.1) 不依赖浮点数。

---

## 6. `已严格完成`：Gaussian divisor 必须处于窄乘法窗

canonical mixed signs 给出

\[
fZ=A-T,
\qquad
qW=A+T.
\]

因此

\[
\frac{fZ}{qW}=\frac{1-T/A}{1+T/A}.
\]

由 (5.1) 得到严格下界：

\[
\boxed{
\begin{array}{c|c}
a&\displaystyle \frac{fZ}{qW}\\ \hline
5&>5/11\\
7&>69/131\\
9&>37/63\\
11&>79/121\\
13&>5/7
\end{array}}
\tag{6.1}
\]

同时 \(T>0\) 给出

\[
\frac{fZ}{qW}<1.
\]

也就是说合法 Gaussian allocation 不允许两个 mixed-sign 因子发生任意大的乘法失衡。特别是高 core 越大，窗口越窄：\(a=13\) 时

\[
\boxed{
\frac57<\frac{fZ}{qW}<1.
}
\]

若再代入

\[
Z=c_-^2X,\qquad W=c_+^2Y,\qquad XY=\mathcal N,
\]

则每一种 \(c_Q=c_-c_+\) 的平方单边 allocation 都必须满足

\[
\boxed{
\eta_a
<
\frac{f c_-^2X}{q c_+^2Y}
<1,
}
\tag{6.2}
\]

其中 \(\eta_a\) 为 (6.1) 左栏对应常数。

这正是后续把连续 ellipse 与离散 \(c_Q\)-allocation、\(q/f\) singular lift、2/5-adic phase 联立所需的 multiplicative window。

---

## 7. 证明边界

本节严格完成的是：

1. \(z\) 与真实 decimal phase 的精确恢复；
2. \(n/\Sigma\) 的完全 scale-free 化；
3. \(J/A\) 的完全 scale-free 化；
4. 五个 core 的显式 \(T/A\) 上界；
5. 因而得到 Gaussian mixed-sign factors 的 core-dependent 窄乘法窗。

这些结论排除了“Gaussian divisor 可以任意失衡”的剩余自由度，但尚未单独证明所有离散 allocation 均不落入 (6.2)。下一步必须把 (6.2) 与已有的平方单边 allocation、finite defect / CRT 唯一代表直接联立；继续单独追 source prime 不会增加约束。
