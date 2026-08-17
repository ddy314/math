# A1 top layer coprime-residue kernel — 2026-08-17

本文继续 `a1-top-layer-endpoint-kernel-2026-08-17.md`。最高层

\[
d=s_1-g=2
\]

已经被压入端点变量 `(w,x,y,z)`；本文进一步把四个端点变量合并成两个与既约性直接兼容的正整数余量。

核心结果为

\[
\boxed{a_1=10^{g+1}b_1+U_1,}
\qquad
\boxed{a_2=10^{k+g+1}b_2-U_2,}
\]

\[
\boxed{\gcd(U_1,b_1)=\gcd(U_2,b_2)=1,}
\]

以及 determinant 的二项正分解

\[
\boxed{
\Delta=10^k b_2U_1+b_1U_2.
}
\]

这把最高层改写成“同一十进制中心两侧的两个既约 rational defects”。本文结论均为 **已严格完成**。

---

## 1. 端点基线

沿用前文

\[
m_1=2k+r,
\qquad
m_2=k-g+s,
\]

以及

\[
b_1=10^{2k+r}-w,
\qquad
 a_1=10^{2k+r+g+1}+x,
\]

\[
b_2=10^{k-g+s-1}+y,
\qquad
 a_2=10^{2k+s}-z.
\]

其中

\[
w,z\ge1,
\qquad x,y\ge0.
\]

定义

\[
\boxed{
U_1=x+10^{g+1}w,
}
\tag{1}
\]

\[
\boxed{
U_2=z+10^{k+g+1}y.
}
\tag{2}
\]

二者均为正整数。

---

## 2. 两个原分数变成十进制中心加减既约余量

由

\[
10^{g+1}b_1
=10^{2k+r+g+1}-10^{g+1}w,
\]

结合 (1)：

\[
\boxed{
 a_1=10^{g+1}b_1+U_1.
}
\tag{3}
\]

同理

\[
10^{k+g+1}b_2
=10^{2k+s}+10^{k+g+1}y,
\]

结合 (2)：

\[
\boxed{
 a_2=10^{k+g+1}b_2-U_2.
}
\tag{4}
\]

因此

\[
\boxed{
 r_1=10^{g+1}+\frac{U_1}{b_1},
}
\tag{5}
\]

\[
\boxed{
 r_2=10^{k+g+1}-\frac{U_2}{b_2}.
}
\tag{6}
\]

令共同十进制中心

\[
\boxed{M=10^{k+g+1}.}
\]

则

\[
10^k r_1
=M+10^k\frac{U_1}{b_1},
\qquad
r_2
=M-\frac{U_2}{b_2}.
\]

所以最高层精确描述成第一 carrier 坐标从 `M` 的上侧逼近、第二坐标从 `M` 的下侧逼近。

---

## 3. 原始既约性直接传给两个余量

由 (3)：

\[
\gcd(a_1,b_1)
=
\gcd(U_1,b_1).
\]

原问题要求 `gcd(a_1,b_1)=1`，故

\[
\boxed{
\gcd(U_1,b_1)=1.
}
\tag{7}
\]

同理由 (4)：

\[
\boxed{
\gcd(U_2,b_2)=1.
}
\tag{8}
\]

因此两个 rational defects

\[
\frac{U_1}{b_1},
\qquad
\frac{U_2}{b_2}
\]

本身已经是既约分数。

---

## 4. carrier gap 的二项分解

定义

\[
\Delta=10^k a_1b_2-a_2b_1>0.
\]

把 (3)–(4) 代入：

\[
\begin{aligned}
\Delta
&=10^k(10^{g+1}b_1+U_1)b_2
 -(10^{k+g+1}b_2-U_2)b_1\\
&=10^k b_2U_1+b_1U_2.
\end{aligned}
\]

所以

\[
\boxed{
\Delta=10^k b_2U_1+b_1U_2.
}
\tag{9}
\]

除以 `G=b_1b_2`：

\[
\boxed{
10^k r_1-r_2
=
10^k\frac{U_1}{b_1}
+
\frac{U_2}{b_2}.
}
\tag{10}
\]

这就是最高层真正的 rational gap。

---

## 5. 与四-offset compact kernel 的精确对应

沿用

\[
\varepsilon=10^{-2k},
\]

\[
X=\frac{x}{10^{r+g+1}},
\quad
W=\frac{w}{10^r},
\quad
Y=10^{k+g+1-s}y,
\quad
Z=\frac{z}{10^s}.
\]

则

\[
\boxed{
\frac{U_1}{10^{r+g+1}}=X+W,
}
\tag{11}
\]

\[
\boxed{
\frac{U_2}{10^s}=Y+Z.
}
\tag{12}
\]

又

\[
\frac{b_1}{10^{m_1}}=1-\varepsilon W,
\qquad
\frac{b_2}{10^{m_2-1}}=1+\varepsilon Y.
\]

令

\[
L_0=10^{2k+r+s}.
\]

把 (9) 除以 `L_0`：

\[
\boxed{
\frac{\Delta}{L_0}
=(1+\varepsilon Y)(X+W)
 +(1-\varepsilon W)(Y+Z).
}
\tag{13}
\]

展开恰为前文

\[
X+W+Y+Z+\varepsilon(XY-WZ).
\]

所以 residue kernel 与 compact offset kernel 完全等价，但 (13) 保留了两个正的既约余量块，后续做素数与整除分析更自然。

---

## 6. `g\ge1` 时两个余量都有固定十进制上界

前文已经证明在 `g\ge1` 的最高层：

\[
\boxed{
\frac12<\frac{\Delta}{L_0}<\frac56,
}
\tag{14}
\]

并且

\[
\delta:=1-t<\frac45\varepsilon.
\]

因此

\[
\frac{b_1}{10^{m_1}}>t>1-\frac45\varepsilon
\ge\frac{124}{125},
\]

即

\[
1-\varepsilon W>\frac{124}{125}.
\tag{15}
\]

从 (13) 的第一正项：

\[
(1+\varepsilon Y)(X+W)<\frac56,
\]

故

\[
\boxed{
0<X+W<\frac56.
}
\tag{16}
\]

也就是

\[
\boxed{
0<U_1<\frac56\,10^{r+g+1}.
}
\tag{17}
\]

从第二正项及 (15)：

\[
\frac{124}{125}(Y+Z)<\frac56,
\]

所以

\[
\boxed{
0<Y+Z<\frac{625}{744}.
}
\tag{18}
\]

即

\[
\boxed{
0<U_2<\frac{625}{744}\,10^s.
}
\tag{19}
\]

另一方面，由 (13) 下界 `>1/2`。又由 `\delta<4\varepsilon/5` 可得

\[
1+\varepsilon Y<\frac1{1-\delta}<\frac{125}{124}.
\]

若同时

\[
X+W\le\frac{62}{249},
\qquad
Y+Z\le\frac{62}{249},
\]

则

\[
\frac{\Delta}{L_0}
<
\left(\frac{125}{124}+1\right)\frac{62}{249}
=\frac12,
\]

矛盾。因此

\[
\boxed{
\max\left(
\frac{U_1}{10^{r+g+1}},
\frac{U_2}{10^s}
\right)
>\frac{62}{249}.
}
\tag{20}
\]

也就是说，两个余量至少有一个必须占据其自然十进制尺度的约四分之一以上；不能同时退化成极小余量。

---

## 7. rational gap 的固定半尺度窗口

由 (10) 与

\[
\frac{\Delta}{G}
=
\frac{L_0}{G}\frac{\Delta}{L_0},
\]

而

\[
G=b_1b_2
=10^{3k+r+s-g-1}
(1-\varepsilon W)(1+\varepsilon Y),
\]

有

\[
\boxed{
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
=
10^{g+1-k}
\frac{\Delta/L_0}
{(1-\varepsilon W)(1+\varepsilon Y)}.
}
\tag{21}
\]

在 `g\ge1` 时，利用

\[
\frac12<\frac{\Delta}{L_0}<\frac56,
\]

以及

\[
1-\varepsilon W>\frac{124}{125},
\qquad
1+\varepsilon Y<\frac{125}{124},
\]

得到安全窗口

\[
\boxed{
\frac{62}{125}\,10^{g+1-k}
<
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
<
\frac{625}{744}\,10^{g+1-k}.
}
\tag{22}
\]

因此最高层的 carrier gap 已被固定在大约 `1/2` 个自然十进制单位上。

---

## 8. 后续接口

最高层 `d=2,g\ge1` 现在可以完全改写成：

\[
\boxed{
 r,s\ge1,
}
\]

两个既约 rational defects

\[
\boxed{
\frac{U_1}{b_1},\qquad\frac{U_2}{b_2},
\quad
(U_1,b_1)=(U_2,b_2)=1,
}
\]

满足

\[
\boxed{
\frac{62}{125}\,10^{g+1-k}
<
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
<
\frac{625}{744}\,10^{g+1-k},
}
\]

以及 residue-size 条件 (17)、(19)、(20)。

这一坐标下一步应优先把 denominator prime graph、safe integer-gap identity

\[
10^\ell E=b_3U
\]

和第三分母 funnel 转写成关于 `(b_1,U_1;b_2,U_2)` 的素数流条件。这样可以直接攻击 moving prefix，而无需重新展开四个大整数。
