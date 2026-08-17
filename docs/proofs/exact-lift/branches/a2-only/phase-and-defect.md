# A2 ellipse, defect window and low-defect angle squeeze

> 本文件是按数学依赖整合的规范编辑入口。每个来源笔记只在本文件中保留一次；来源边界、原状态和公式正文均保留，避免日期文件之间形成平行副本。

## 整合顺序

`a2-decimal-ellipse-phase.md` → `a2-ellipse-to-defect-window.md` → `a2-low-defect-angle-squeeze.md`

---

## 1. `A_2` decimal ellipse phase compression

> 整合来源：`a2-decimal-ellipse-phase.md`。以下正文保留该来源的原始证明状态和审计边界。

> 分支：`agent/a2-hensel-resultant-progress`
> 状态：**严格结构推进；得到 core-dependent Gaussian divisor window，尚未单独关闭整个 `A_2`。**
> 依赖：`core.md` 的 terminal deep-even/source split、旧 A2 工作稿中的 canonical discriminant 与 Gaussian companion：
> \[
> T^2=A^2-\Sigma\mathcal N,\qquad T^2+J^2=n\mathcal N.
> \]

本文把 source-side 尺度全部消去，将 \(n/\Sigma\)、canonical discriminant angle \(T/A\) 和真实十进制窗口直接联结起来。它的目标是把此前“二维 ellipse + decimal phase”变成可直接作用于 Gaussian divisor allocation 的定量不等式。

---

### 1. 记号

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

### 2. `已严格完成`：第三块实尺度给出精确的 source normalized `z`

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

### 3. `已严格完成`：`n/Sigma` 的完全尺度消去

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

### 4. `已严格完成`：Gaussian angle 完全进入 `(x,y)` 窗口

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

### 5. `已严格完成`：五个 core 的显式 angle cap

在 `core.md` 的严格实窗口上，(4.4)–(4.5) 给出：

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

### 6. `已严格完成`：Gaussian divisor 必须处于窄乘法窗

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

### 7. 证明边界

本节严格完成的是：

1. \(z\) 与真实 decimal phase 的精确恢复；
2. \(n/\Sigma\) 的完全 scale-free 化；
3. \(J/A\) 的完全 scale-free 化；
4. 五个 core 的显式 \(T/A\) 上界；
5. 因而得到 Gaussian mixed-sign factors 的 core-dependent 窄乘法窗。

这些结论排除了“Gaussian divisor 可以任意失衡”的剩余自由度，但尚未单独证明所有离散 allocation 均不落入 (6.2)。下一步必须把 (6.2) 与已有的平方单边 allocation、finite defect / CRT 唯一代表直接联立；继续单独追 source prime 不会增加约束。

---

## 2. `A_2` ellipse-to-defect remainder window

> 整合来源：`a2-ellipse-to-defect-window.md`。以下正文保留该来源的原始证明状态和审计边界。

> 分支：`agent/a2-hensel-resultant-progress`
> 状态：**严格结构推进；连续 canonical ellipse 已直接限制 finite-defect 余量。**
> 依赖：[`phase-and-defect.md`](phase-and-defect.md) 与旧 terminal factor / finite-defect 正规形。

本文把 canonical signed-square angle 的新实数窄窗与旧 finite-defect

\[
c_-^2X=kD+R,\qquad 0<R<D
\]

直接联立。所得结论第一次把连续 ellipse 约束变成 \(R/D\) 的显式下界。

---

### 1. 两套第三坐标因子的精确对应

terminal factor system 有

\[
H_0-Y_3=5^E c_-^2X,
\qquad
H_0+Y_3=c_+^2Y.
\tag{1.1}
\]

finite-defect 记号满足

\[
5^ED=g10^m,
\qquad
J_{\rm def}:=\frac{c_-^2X}{D}=k+\frac RD.
\tag{1.2}
\]

于是

\[
H_0-Y_3=g10^mJ_{\rm def}.
\]

旧 k-free 恒等式又给出

\[
H_0=g(a_3+10^mJ_{\rm def}),
\]

故

\[
\boxed{
\frac{H_0-Y_3}{H_0+Y_3}
=
\frac{J_{\rm def}}{J_{\rm def}+2\zeta},
\qquad
\zeta:=\frac{a_3}{10^m}.
}
\tag{1.3}
\]

真实第三分子窗口给出

\[
1<\zeta<
\begin{cases}
21/20,&a=5,\\
8/7,&a=7,\\
6/5,&a=9,11,\\
11/10,&a=13.
\end{cases}
\tag{1.4}
\]

其中左端严格：若 \(a_3=10^m\)，则 \(a_3\) 为偶数，而 terminal deep-even 的 \(b_3\) 也是偶数，违背 \(\gcd(a_3,b_3)=1\)。

---

### 2. Canonical mixed-sign ratio 与 sphere ratio 的校正因子

canonical discriminant factorization 写成

\[
fZ=A-T,
\qquad
qW=A+T,
\]

且

\[
Z=c_-^2X,
\qquad
W=c_+^2Y.
\]

所以

\[
\frac{fZ}{qW}
=
\frac{f}{5^Eq}
\frac{H_0-Y_3}{H_0+Y_3}.
\tag{2.1}
\]

这里不能把两种 ratio 直接认成同一个量；差别正是 \(f/(5^Eq)\)。

由 source normalization

\[
q=\frac{U(x+2)}{2c_Q},
\]

\[
f=\frac{U}{2D_0}\bigl(z(x+2)+2x\bigr),
\]

以及

\[
z=\frac{10^Mx}{w},
\]

得到

\[
\boxed{
\vartheta:=\frac{5^Eq}{f}
=
\frac{z(x+2)}{z(x+2)+2x}
=
\frac{10^M(x+2)}{10^M(x+2)+2w}.
}
\tag{2.2}
\]

因为 \(x>0\) 且 \(0<w<1\)，

\[
\boxed{
\vartheta>
rac{10^M}{10^M+1}.
}
\tag{2.3}
\]

在当前开放范围 \(M\ge11\) 中统一有

\[
\boxed{
\vartheta>
artheta_{11}:=
rac{10^{11}}{10^{11}+1}.
}
\tag{2.4}
\]

这说明 canonical ratio 到 sphere ratio 的校正只有十进制指数级小量。

---

### 3. `已严格完成`：finite-defect 商的 core-dependent 下界

前一文件得到

\[
\frac{fZ}{qW}>\eta_a,
\]

其中

\[
\eta_5=\frac5{11},\qquad
\eta_7=\frac{69}{131},\qquad
\eta_9=\frac{37}{63},\qquad
\eta_{11}=\frac{79}{121},\qquad
\eta_{13}=\frac57.
\tag{3.1}
\]

由 (2.1)–(2.4)，

\[
\frac{H_0-Y_3}{H_0+Y_3}
>\eta_a\vartheta_{11}.
\]

再代入 (1.3)，得到

\[
\boxed{
J_{\rm def}
>
\frac{2\eta_a\vartheta_{11}}
{1-\eta_a\vartheta_{11}}\,\zeta.
}
\tag{3.2}
\]

因为 \(\zeta>1\)，可去掉第三分子的连续参数：

\[
\boxed{
J_{\rm def}>C_a,
}
\tag{3.3}
\]

其中精确常数为

\[
\begin{array}{c|c|c}
a&C_a&\text{数值}\ \hline
5&\dfrac{10^{12}}{600000000011}&1.666666666636\ldots\\[2mm]
7&\dfrac{600000000000}{269565217397}&2.225806451565\ldots\\[2mm]
9&\dfrac{7400000000000}{2600000000063}&2.846153846084\ldots\\[2mm]
11&\dfrac{15800000000000}{4200000000121}&3.761904761796\ldots\\[2mm]
13&\dfrac{10^{12}}{200000000007}&4.999999999825\ldots
\end{array}
\tag{3.4}
\]

---

### 4. `已严格完成`：七个 defect 状态中的四个获得真余量下界

由于

\[
J_{\rm def}=k+\frac RD,
\qquad 0<\frac RD<1,
\]

旧 defect 状态为

\[
k\in
\begin{cases}
\{1\},&a=5,\\
\{2\},&a=7,\\
\{2,3\},&a=9,\\
\{3,4\},&a=11,\\
\{5\},&a=13.
\end{cases}
\]

(3.3) 对低商状态给出：

\[
\boxed{
\begin{array}{c|c|c}
a&k& R/D\ \hline
5&1&>33/50\\
7&2&>11/50\\
9&2&>21/25\\
11&3&>19/25
\end{array}}
\tag{4.1}
\]

这些是故意取弱后的干净有理界；均严格弱于 (3.4) 的精确值，因此无需浮点判断。

特别是两个此前仍有整段 \((0,D)\) 自由度的状态被压到顶端薄层：

\[
\boxed{
a=9,\ k=2\Longrightarrow \frac RD>\frac{21}{25},}
\]

\[
\boxed{
a=11,\ k=3\Longrightarrow \frac RD>\frac{19}{25}.}
\]

也就是说相应 CRT 唯一代表若存在，只能落在区间最后的 \(16\%\) 或 \(24\%\)。

对 \((a,k)=(9,3),(11,4),(13,5)\)，当前 lower angle cap 尚不足以超过商的整数基线，因此本节不宣称新余量下界。

---

### 5. 与统一平方深度 CRT 的直接组合

固定 core、\(k\)、二进相位以及 \(c_Q,\rho\) 的平方单边分配后，已有统一模数

\[
\mathfrak L
=2^{2t-1}c_u\rho^2\operatorname{lcm}(q,c_Q^2),
\]

使 \(R\) 落在模 \(\mathfrak L\) 的至多一个兼容类。

在平衡支已有 \(\mathfrak L>D\)，所以 \(0<R<D\) 中至多一个代表。现在 (4.1) 进一步要求这个唯一代表还必须落在

\[
\left(\frac{33}{50}D,D\right),
\quad
\left(\frac{11}{50}D,D\right),
\quad
\left(\frac{21}{25}D,D\right),
\quad
\left(\frac{19}{25}D,D\right)
\]

之一（依 core / defect 而定）。

因此下一步已不再是“枚举 \(R\)”：只需证明统一 CRT 的唯一代表与相应顶端 interval 不相容。特别应优先攻击 \((a,k)=(9,2)\) 与 \((11,3)\)，因为它们只剩最薄的顶部窗口。

---

### 6. 当前证明边界

本文新增的是严格的 bridge

\[
\boxed{
\text{decimal ellipse angle}
\Longrightarrow
\text{sphere distance ratio}
\Longrightarrow
J_{\rm def}=k+R/D
\Longrightarrow
\text{CRT remainder interval}.
}
\]

它没有单独关闭全部 A2，但已把连续几何约束真正送入最后的离散 CRT representative，而不是停留在独立的实数估计。

---

## 3. `A_2` low-defect angle squeeze

> 整合来源：`a2-low-defect-angle-squeeze.md`。以下正文保留该来源的原始证明状态和审计边界。

> 分支：`agent/a2-hensel-resultant-progress`
> 状态：**已严格完成两个低商状态的额外十进制窗口收缩。**
> 依赖：[`phase-and-defect.md`](phase-and-defect.md) 与 [`phase-and-defect.md`](phase-and-defect.md)。

本文利用 finite-defect 商的上界

\[
J_{\rm def}=k+\frac RD<k+1
\]

反向给 canonical angle \(T/A\) 一个下界，再与前一文件的 ellipse 上界夹逼。其作用集中在 \((a,k)=(9,2)\) 与 \((11,3)\)。

---

### 1. 从 `J_def < k+1` 得到 angle 下界

记

\[
s:=\frac{H_0-Y_3}{H_0+Y_3}
=
\frac{J_{\rm def}}{J_{\rm def}+2\zeta},
\qquad
\zeta=\frac{a_3}{10^m}>1.
\]

因为 \(J_{\rm def}<k+1\)，函数 \(J/(J+2\zeta)\) 关于 \(J\) 递增、关于 \(\zeta\) 递减，所以

\[
\boxed{
s<\frac{k+1}{k+3}=:s_k.}
\tag{1.1}
\]

canonical mixed-sign ratio 为

\[
r_{\rm can}:=\frac{A-T}{A+T}
=\frac{fZ}{qW}
=\frac{s}{\vartheta},
\]

其中前一文件已证

\[
\vartheta=
rac{5^Eq}{f}
>
artheta_{11}:=\frac{10^{11}}{10^{11}+1}
\]

对全部当前开放范围 \(M\ge11\) 成立。因此

\[
r_{\rm can}<\frac{s_k}{\vartheta_{11}}.
\]

而

\[
\frac TA=\frac{1-r_{\rm can}}{1+r_{\rm can}},
\]

故

\[
\boxed{
\frac TA>\lambda_k
:=
\frac{\vartheta_{11}-s_k}{\vartheta_{11}+s_k}.
}
\tag{1.2}
\]

对两个关键低商状态：

\[
\boxed{
\lambda_2
=\frac{199999999997}{800000000003}
=0.2499999999953125\ldots,
}
\tag{1.3}
\]

\[
\boxed{
\lambda_3
=\frac{49999999999}{250000000001}
=0.1999999999952\ldots.
}
\tag{1.4}
\]

所以 \(k=2\) 几乎强制 \(T/A>1/4\)，\(k=3\) 几乎强制 \(T/A>1/5\)。

---

### 2. 与 scale-free ellipse 上界夹逼

前一文件已证

\[
\left(\frac TA\right)^2<H_a(x,y)<H_a(x,1),
\]

其中

\[
H_a(x,1)
=-\frac{
25a^2x^4+100a^2x^3-(200a+99)x^2+4x+4
}{100x^2(a+1)^2},
\]

且

\[
\frac d{dx}H_a(x,1)
=-\frac{(x+2)(25a^2x^3-2)}{50x^3(a+1)^2}.
\]

对于 \(a=9,11\)，唯一正临界点

\[
x_*=(2/(25a^2))^{1/3}
\]

都严格小于 \(1/10\)。因此 \(H_a(x,1)\) 在整个合法窗口 \(x\ge1/10\) 上严格递减。

---

### 3. `已严格完成`：`a=9,k=2` 只剩最左 `6%` 薄层

若 \(a=9,k=2\)，由 (1.2)–(1.3)

\[
\left(\frac TA\right)^2>\lambda_2^2.
\]

另一方面精确有理计算给出

\[
H_9\!\left(\frac{53}{500},1\right)
<\lambda_2^2.
\tag{3.1}
\]

两边之差精确为正：

\[
\lambda_2^2-H_9(53/500,1)
=
\frac{19547494618796606215170368636649}
{179776000001348320000002528100000000}>0.
\]

由于 \(H_9(x,1)\) 在 \([1/10,3/20)\) 上递减，若 \(x\ge53/500\)，则

\[
(T/A)^2<H_9(x,1)\le H_9(53/500,1)<\lambda_2^2,
\]

与 angle 下界矛盾。

故

\[
\boxed{
(a,k)=(9,2)
\Longrightarrow
\frac1{10}\le x<\frac{53}{500}.
}
\tag{3.2}
\]

原窗口为 \(1/10\le x<3/20\)，现在只剩左端宽度 \(0.006\)。

---

### 4. `已严格完成`：`a=11,k=3` 只剩最左 `9%` 薄层

若 \(a=11,k=3\)，同理由 (1.4)

\[
(T/A)^2>\lambda_3^2.
\]

精确有理计算：

\[
H_{11}\!\left(\frac{109}{1000},1\right)
<\lambda_3^2,
\tag{4.1}
\]

且

\[
\lambda_3^2-H_{11}(109/1000,1)
=
\frac{17192037971391456305230243712609}
{47524000000380192000000760384000000}>0.
\]

由于 \(H_{11}(x,1)\) 在合法窗口递减，得到

\[
\boxed{
(a,k)=(11,3)
\Longrightarrow
\frac1{10}\le x<\frac{109}{1000}.
}
\tag{4.2}
\]

原窗口为 \(1/10\le x<1/8\)，现只剩 \([0.1,0.109)\)。

---

### 5. 当前意义

结合上一文件：

\[
(a,k)=(9,2):
\qquad
\frac RD>\frac{21}{25},
\qquad
\frac1{10}\le x<\frac{53}{500},
\]

\[
(a,k)=(11,3):
\qquad
\frac RD>\frac{19}{25},
\qquad
\frac1{10}\le x<\frac{109}{1000}.
\]

因此这两个状态同时受到：

1. CRT 余量必须位于 \((0,D)\) 的最顶部；
2. 第二分母归一化量必须位于其 core window 的最左端；
3. canonical angle 必须位于极窄区间
   \[
   \lambda_k<T/A<\text{core cap}.
   \]

下一步应把 \(x=2^{m+t}u/5^M\) 的 source 格点和统一 square-depth CRT 代表一起代入这两个薄层，而不再对完整原参数空间做无差别搜索。
