# `A_2` ellipse-to-defect remainder window

> 分支：`agent/a2-hensel-resultant-progress`  
> 状态：**严格结构推进；连续 canonical ellipse 已直接限制 finite-defect 余量。**  
> 依赖：[`a2-decimal-ellipse-phase.md`](a2-decimal-ellipse-phase.md) 与旧 terminal factor / finite-defect 正规形。

本文把 canonical signed-square angle 的新实数窄窗与旧 finite-defect

\[
c_-^2X=kD+R,\qquad 0<R<D
\]

直接联立。所得结论第一次把连续 ellipse 约束变成 \(R/D\) 的显式下界。

---

## 1. 两套第三坐标因子的精确对应

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

## 2. Canonical mixed-sign ratio 与 sphere ratio 的校正因子

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
\vartheta>rac{10^M}{10^M+1}.
}
\tag{2.3}
\]

在当前开放范围 \(M\ge11\) 中统一有

\[
\boxed{
\vartheta>artheta_{11}:=rac{10^{11}}{10^{11}+1}.
}
\tag{2.4}
\]

这说明 canonical ratio 到 sphere ratio 的校正只有十进制指数级小量。

---

## 3. `已严格完成`：finite-defect 商的 core-dependent 下界

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

## 4. `已严格完成`：七个 defect 状态中的四个获得真余量下界

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

## 5. 与统一平方深度 CRT 的直接组合

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

## 6. 当前证明边界

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
