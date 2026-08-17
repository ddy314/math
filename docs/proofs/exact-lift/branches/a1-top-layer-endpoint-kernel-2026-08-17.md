# A1 top layer endpoint kernel — 2026-08-17

本文研究全局四层定理中的最高层

\[
\boxed{d:=s_1-g=2.}
\]

这一层的十进制尺度恰好位于一个边界接触状态：`10^k r_1` 从上侧逼近同一十进制边界，而 `r_2` 从下侧逼近它。利用 rational contact 可以把这种直觉严格化为一个 endpoint-offset normal form。

核心结论：

1. 最高层全局满足
   \[
   \boxed{m_1\ge2k};
   \]
2. 令
   \[
   r=m_1-2k,
   \qquad
   s=m_2+g-k,
   \]
   则必有 `r,s\ge0`，并且四个前缀整数都被压在各自十进制端点附近；
3. 整个最高层可以写成一个紧致的四-offset kernel；
4. 若 `g\ge1`，进一步严格有
   \[
   \boxed{r\ge1,\qquad s\ge1};
   \]
5. 若 `g=0`，至少不能同时 `r=s=0`。

本文结论均为 **已严格完成**。

---

## 1. 最高层中的第三坐标极小

沿用

\[
A_0=10^k r_1,
\qquad
t=\frac{r_2}{A_0},
\qquad
q_0=\frac{r_3}{A_0},
\qquad
R_0=\frac{\mathcal R}{A_0}.
\]

由 `a1-global-four-layer-collapse-2026-08-17.md`：

\[
\boxed{R_0>\frac12.}
\tag{1}
\]

现在假设

\[
s_1=g+2.
\]

位数窗给出

\[
r_1>10^{g+1},
\qquad
r_3<10^{1-g}.
\]

于是

\[
A_0>10^{k+g+1},
\]

从而

\[
\boxed{q_0<10^{-k-2g}.}
\tag{2}
\]

球面式

\[
R_0^2=t^2+10^{-2k}+q_0^2
\]

与 (1)–(2) 联立得到

\[
t^2>
\frac14-10^{-2k}-10^{-2k-4g}.
\]

右侧在 `k\ge1,g\ge0` 时最小为

\[
\frac14-rac1{100}-\frac1{100}=rac{23}{100}.
\]

故

\[
\boxed{t>\frac{\sqrt{23}}{10}>\frac{47}{100}.}
\tag{3}
\]

---

## 2. 最高层的精确四因子分解

因为

\[
s_1=g+2,
\qquad
s_2=k+g,
\]

有

\[
n_1=m_1+g+2,
\qquad
n_2=m_2+k+g.
\]

直接检查十进制指数可得

\[
\boxed{
 t
=
\left(\frac{a_2}{10^{n_2}}\right)
\left(\frac{b_1}{10^{m_1}}\right)
\left(\frac{10^{n_1-1}}{a_1}\right)
\left(\frac{10^{m_2-1}}{b_2}\right).
}
\tag{4}
\]

四个因子都属于 `(0,1]`，而它们的乘积由 (3) 大于 `47/100`。因此每一个因子都严格大于 `47/100`：

\[
\boxed{a_2>\frac{47}{100}10^{n_2},}
\tag{5}
\]

\[
\boxed{b_1>\frac{47}{100}10^{m_1},}
\tag{6}
\]

\[
\boxed{a_1<\frac{100}{47}10^{n_1-1},}
\tag{7}
\]

\[
\boxed{b_2<\frac{100}{47}10^{m_2-1}.}
\tag{8}
\]

所以最高层从一开始就位于四个十进制端点组成的角落，而不是一个普通内部矩形。

---

## 3. contact 把 `1-t` 锁到 `10^{-2k}` 尺度

记

\[
Q=b_1 10^{m_2}+b_2,
\qquad
\lambda=\frac{b_2}{Q}.
\]

由 (6)、(8)：

\[
\lambda
<
\frac{b_2}{b_1 10^{m_2}}
<
\frac{1000}{2209}10^{-m_1}.
\tag{9}
\]

同样

\[
\frac1Q
<
\frac1{b_1 10^{m_2}}
<
\frac{100}{47}10^{-m_1-m_2}
\le
\frac{10}{47}10^{-m_1}.
\tag{10}
\]

rational contact 在无量纲坐标中为

\[
1-R_0
=
\lambda(1-10^{-g}t)
+
\theta(R_0-q_0),
\qquad
0<\theta<\frac1Q.
\]

因为 `R_0<1`，所以由 (9)–(10)

\[
\boxed{
1-R_0
<
\frac{1470}{2209}10^{-m_1}.
}
\tag{11}
\]

另一方面，(4) 中第二因子给出

\[
t<\frac{b_1}{10^{m_1}},
\]

所以

\[
1-t
>
1-\frac{b_1}{10^{m_1}}
\ge10^{-m_1}.
\tag{12}
\]

因此

\[
R_0-t
=(1-t)-(1-R_0)
>
\boxed{
\frac{739}{2209}10^{-m_1}.
}
\tag{13}
\]

另一方面由球面式

\[
R_0-t
=
\frac{10^{-2k}+q_0^2}{R_0+t}.
\]

由 (2)、(3)，

\[
R_0+t>2t>\frac{94}{100},
\]

故

\[
R_0-t
<
\frac{100}{94}
10^{-2k}(1+10^{-4g})
\le
\boxed{\frac{100}{47}10^{-2k}.}
\tag{14}
\]

若 `m_1\le2k-1`，则 (13) 给出

\[
R_0-t
>
\frac{7390}{2209}10^{-2k},
\]

但

\[
\frac{7390}{2209}>rac{4700}{2209}=rac{100}{47},
\]

与 (14) 矛盾。

所以最高层全局满足

\[
\boxed{m_1\ge2k.}
\tag{15}
\]

这已经把 `k` 压入第一分母位数的一半尺度：

\[
k\le\frac{m_1}{2}.
\]

---

## 4. 更强的贴边：`1-t<3\cdot10^{-2k}`

由 (15)：

\[
10^{-m_1}\le10^{-2k}.
\]

把它代入 (11)：

\[
1-R_0
<
\frac{1470}{2209}10^{-2k}.
\]

再与 (14) 相加：

\[
1-t
=(1-R_0)+(R_0-t)
<
\left(
\frac{1470}{2209}
+
\frac{4700}{2209}
\right)10^{-2k}.
\]

因此

\[
\boxed{
1-t
<
\frac{6170}{2209}10^{-2k}
<3\cdot10^{-2k}.
}
\tag{16}
\]

所以最高层的四因子乘积并非仅仅大于一个固定常数；它实际上以 `10^{-2k}` 的速度逼近 1。

---

## 5. 两个 surplus 与四个端点偏移

定义

\[
\boxed{r=m_1-2k\ge0.}
\tag{17}
\]

再定义

\[
\boxed{s=m_2+g-k.}
\tag{18}
\]

从 (4)、(16)，每个因子都大于

\[
1-3\cdot10^{-2k}.
\]

令端点偏移

\[
\boxed{w=10^{m_1}-b_1\ge1,}
\]

\[
\boxed{x=a_1-10^{n_1-1}\ge0,}
\]

\[
\boxed{z=10^{n_2}-a_2\ge1,}
\]

\[
\boxed{y=b_2-10^{m_2-1}\ge0.}
\]

则由四因子逐项得到

\[
\boxed{1\le w<3\cdot10^r,}
\tag{19}
\]

\[
\boxed{0\le x<4\cdot10^{r+g+1},}
\tag{20}
\]

\[
\boxed{1\le z<3\cdot10^s,}
\tag{21}
\]

\[
\boxed{0\le y<4\cdot10^{s-k-g-1}.}
\tag{22}
\]

其中 (20)、(22) 使用了

\[
\frac{3\cdot10^{-2k}}{1-3\cdot10^{-2k}}
<4\cdot10^{-2k}.
\]

由于 `z\ge1`，(21) 立即强迫

\[
\boxed{s\ge0,}
\tag{23}
\]

即

\[
\boxed{m_2+g\ge k.}
\]

特别地，若

\[
s=0,
\]

则

\[
\boxed{z\in\{1,2\}.}
\tag{24}
\]

若

\[
r=0,
\]

则同理

\[
\boxed{w\in\{1,2\}.}
\tag{25}
\]

此外若

\[
s\le k+g,
\]

则 (22) 的右侧小于 1，故整数 `y` 必须为零：

\[
\boxed{s\le k+g\Longrightarrow b_2=10^{m_2-1}.}
\tag{26}
\]

这时 `gcd(a_2,b_2)=1` 还等价强迫

\[
\boxed{\gcd(z,10)=1.}
\tag{27}
\]

因为

\[
a_2=10^{n_2}-z.
\]

---

## 6. endpoint normal form

利用

\[
m_1=2k+r,
\qquad
m_2=k-g+s,
\]

最高层的四个前缀整数可以统一写成

\[
\boxed{
b_1=10^{2k+r}-w,}
\tag{28}
\]

\[
\boxed{
a_1=10^{2k+r+g+1}+x,}
\tag{29}
\]

\[
\boxed{
b_2=10^{k-g+s-1}+y,}
\tag{30}
\]

\[
\boxed{
a_2=10^{2k+s}-z.}
\tag{31}
\]

所有增长已经从原来的四个大整数转移到 `k,g,r,s`，而 `w,x,y,z` 只允许在 (19)–(22) 的端点薄层中移动。

---

## 7. 精确 determinant 展开

定义第一、第二坐标十进制移位差

\[
\boxed{
\Delta
=10^k a_1b_2-a_2b_1
>0.
}
\tag{32}
\]

这里正性等价于 `t<1`。

把 (28)–(31) 代入并消去主导的相同十进制幂，可以得到完全正的展开：

\[
\boxed{
\begin{aligned}
\Delta={}&
10^{m_1+k+g+1}y
+10^{k+m_2-1}x
+10^kxy\\
&+10^{k+g+m_2}w
+b_1z.
\end{aligned}
}
\tag{33}
\]

右端五项全部非负，且最后两项严格为正。

定义统一尺度

\[
\boxed{
L_0=10^{m_1+m_2+g-k}=10^{2k+r+s}.
}
\tag{34}
\]

再定义紧致 offset 坐标

\[
\boxed{X=\frac{x}{10^{r+g+1}},}
\qquad
\boxed{W=\frac{w}{10^r},}
\]

\[
\boxed{Z=\frac{z}{10^s},}
\qquad
\boxed{Y=10^{k+g+1-s}y.}
\tag{35}
\]

并记

\[
\varepsilon=10^{-2k}.
\]

则 (33) 精确化成

\[
\boxed{
\frac{\Delta}{L_0}
=
X+W+Y+Z
+
\varepsilon(XY-WZ).
}
\tag{36}
\]

这就是最高层的紧致四-offset kernel。

还可以从

\[
1-t=\frac{\Delta}{10^k a_1b_2}
\]

得到另一条精确表达：

\[
\boxed{
\frac{\Delta}{L_0}
=
\frac{1-t}{\varepsilon}
(1+\varepsilon X)(1+\varepsilon Y).
}
\tag{37}
\]

由球面式

\[
R_0-t
>
\frac{\varepsilon}{2}
\]

可得

\[
1-t>\frac\varepsilon2,
\]

再结合 (16)、(37)：

\[
\boxed{
\frac12
<
\frac{\Delta}{L_0}
<
\frac72.
}
\tag{38}
\]

因此原本无界的最高层已经被压成一个固定宽度的 compact determinant window。

---

## 8. `g\ge1` 时两个 surplus 都必须严格为正

现在额外假设

\[
g\ge1.
\]

由 (16) 与四因子贴边：

\[
b_1>(1-3\varepsilon)10^{m_1},
\qquad
b_2<\frac{10^{m_2-1}}{1-3\varepsilon}.
\]

因为 `m_1\ge2k`、`m_2\ge1`、`\varepsilon\le1/100`，有

\[
\lambda<\frac\varepsilon9,
\qquad
\frac1Q<\frac\varepsilon9.
\]

所以

\[
\boxed{1-R_0<\frac{2}{9}\varepsilon.}
\tag{39}
\]

又由 `g\ge1` 和 (2)：

\[
q_0^2<\frac{\varepsilon}{10000}.
\]

设

\[
\delta=1-t.
\]

由

\[
1-R_0^2
=2\delta-\delta^2-\varepsilon-q_0^2
\]

以及

\[
1-R_0^2<2(1-R_0)<\frac49\varepsilon,
\]

再用 `\delta<3\varepsilon`，得到

\[
2\delta
<
\left(
\frac9{100}+1+\frac1{10000}+\frac49
\right)\varepsilon
<
\frac85\varepsilon.
\]

因此

\[
\boxed{\delta<\frac45\varepsilon.}
\tag{40}
\]

代回 (37)。由于

\[
\delta<\frac45\varepsilon\le\frac1{125},
\]

且

\[
1+\varepsilon X<\frac1{1-\delta},
\qquad
1+\varepsilon Y<\frac1{1-\delta},
\]

有

\[
\boxed{
\frac{\Delta}{L_0}<\frac56.
}
\tag{41}
\]

若 `r=0`，则 `W=w\ge1`，而 (33) 的归一化各项全为非负，故

\[
\frac{\Delta}{L_0}\ge W\ge1,
\]

与 (41) 矛盾。因此

\[
\boxed{g\ge1\Longrightarrow r\ge1.}
\tag{42}
\]

若 `s=0`，则 `Z=z\ge1`。在 (36) 中真正对应最后一项的是

\[
\frac{b_1}{10^{m_1}}Z.
\]

而

\[
\frac{b_1}{10^{m_1}}>t=1-\delta>\frac{124}{125}>\frac56.
\]

故单独这一项已经大于 `5/6`，再次与 (41) 矛盾。所以

\[
\boxed{g\ge1\Longrightarrow s\ge1.}
\tag{43}
\]

综合：

\[
\boxed{
 d=2,\ g\ge1
\Longrightarrow
m_1\ge2k+1,
\qquad
m_2+g\ge k+1.
}
\tag{44}
\]

---

## 9. `g=0` 时两个 equality surplus 不能同时出现

若 `g=0`，仍有 (39)。此时由 (2)

\[
q_0^2<\varepsilon.
\]

同样计算得到

\[
\delta<\frac{13}{10}\varepsilon.
\]

因此由 (37) 可取安全粗界

\[
\boxed{
\frac{\Delta}{L_0}<\frac75.
}
\tag{45}
\]

若同时

\[
r=s=0,
\]

则 `W=w\ge1`、`Z=z\ge1`，并且

\[
\frac{b_1}{10^{m_1}}>1-\delta>0.98.
\]

所以 (33) 归一化后的 `w` 项与 `z` 项之和已经严格大于

\[
1+0.98>\frac75,
\]

与 (45) 矛盾。

故

\[
\boxed{
 d=2,\ g=0
\Longrightarrow
(r,s)\ne(0,0).
}
\tag{46}
\]

---

## 10. 当前最高层剩余核心

最高层已经从原来的任意四整数前缀压缩成：

\[
\boxed{
 r=m_1-2k\ge0,
\qquad
s=m_2+g-k\ge0,
}
\]

加上紧致 offset

\[
(X,W,Y,Z)
\]

满足精确 determinant 核

\[
\boxed{
\frac{\Delta}{10^{2k+r+s}}
=X+W+Y+Z+10^{-2k}(XY-WZ),
}
\]

以及固定窗口

\[
\boxed{
\frac12<\frac{\Delta}{10^{2k+r+s}}<\frac72.
}
\]

在 `g\ge1` 时窗口进一步缩到

\[
\boxed{
\frac12<\frac{\Delta}{10^{2k+r+s}}<\frac56,
\qquad r,s\ge1.
}
\]

并且当 `s\le k+g` 时还有

\[
\boxed{b_2=10^{m_2-1},\qquad\gcd(z,10)=1.}
\]

因此 `d=2` 后续不应再以原始 `(a_1,b_1,a_2,b_2)` 为变量，而应直接攻击上述 `(k,g,r,s;X,W,Y,Z)` compact endpoint kernel，并把 normalized-square / 2,5-adic 条件转写到该坐标中。
