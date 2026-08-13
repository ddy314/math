# Double-deficit（DD）分支

本文件对应原总稿 §§17–27。它包含公共商正规化、判别平方、surplus simplex、near-square、squarefree gap、`2`/`5`-进 resonance、near-`S`-unit、denominator 不对称、双 resonance 尖角和截至后续研究分叉点的 `n_3 <= 8 S_12 - 1` 相对界。

> **2026-08-13 接续说明。** 本文件的 §27.33 起整合两个后续研究分支。新进展关闭了
> `n_3=8S_12-1` 整层，得到 `n_3<31S_12/4+6581/960`，并在明确调用经典
> Schmidt Subspace Theorem 的前提下得到非有效渐近界
> `limsup m_3/S_12<=5` 与 `limsup n_3/S_12<=6.308883577618...`。
> DD 全局空性与绝对有效的 `S_12` 上界仍未得到。

> 迁移说明：以下正文由原始总稿机械拆分，公式和证明状态不作数学改写。
# 17. Double-deficit 分支：公共商正规化

DD 统一记

\[
\boxed{
d_3=s_3>0,
\qquad
k_{12}=s_2+s_3>0.
}
\]

令

\[
T=10^{m_3},
\]

\[
A=10^{m_2}b_1,
\qquad
B=b_2,
\]

以及球面 gap

\[
\boxed{
e=H-y_3>0.
}
\]

定义前两 ghost 平方和

\[
\boxed{
\mathcal S_{12}=y_1^2+y_2^2.
}
\]

定义 DD 线性组合

\[
\mathcal M
=
10^{k_{12}}Ay_1
+
10^{d_3}By_2,
\]

以及

\[
\mathcal G
=
\mathcal M-(A+B)H.
\]

exact balance 可化为

\[
\boxed{
T\mathcal G=b_3e.
}
\]

令

\[
\omega=\gcd(T,b_3),
\qquad
L=T/\omega,
\qquad
\tau=b_3/\omega.
\]

则存在唯一正整数 \(a\) 使

\[
\boxed{
e=La,
\qquad
\mathcal G=\tau a.
}
\]

由于球面恒等式

\[
(H-y_3)(H+y_3)
=
\mathcal S_{12},
\]

有

\[
\boxed{
La\mid\mathcal S_{12},
}
\]

并且

\[
\boxed{
H
=
\frac12
\left(
La+\frac{\mathcal S_{12}}{La}
\right),
}
\]

\[
\boxed{
y_3
=
\frac12
\left(
\frac{\mathcal S_{12}}{La}
-La
\right).
}
\]

因此固定 ghost \((y_1,y_2)\) 与正规化参数后，第三坐标只可能来自 \(\mathcal S_{12}\) 的有限除数。

这解决了“第三块是否还存在独立连续缩放自由度”的问题：没有。

真正的无界性来自前两 ghost 本身。

---

# 18. DD 的判别平方与斜率锁

DD 的恢复方程可整理出平方判别条件

\[
\boxed{
LJ=W^2.
}
\]

实际根甚至进一步满足

\[
\boxed{
W=L\Xi,
\qquad
J=L\Xi^2,
}
\]

其中

\[
\Xi=
|\mathcal M-C_0a|
\]

为显式整数。

另一方面由

\[
\frac{\mathcal G}{e}
=
\frac{\tau}{L}
\]

得到斜率锁

\[
\boxed{
\frac1{10}
\le
\frac{\tau}{L}
<1.
}
\]

这说明 DD 的尾 gap 与尾分母始终处在一个固定十倍窗口。

---

# 19. DD 的 surplus simplex

定义总前两分母位数尺度

\[
\boxed{
S_{12}=m_1+m_2.
}
\]

利用第一 denominator weight 在总权重中的固定占比，对 exact weighted average 做尺度比较，可以得到

\[
\boxed{
s_1+s_2+d_3
-
\max(s_1,s_2,d_3)
\le2.
}
\]

因此 DD 被切成三个很薄的扇区：

\[
\boxed{
\begin{array}{c|c}
s_1=\max&s_2+d_3\le2\\
s_2=\max&s_1+d_3\le2\\
d_3=\max&s_1+s_2\le2
\end{array}
}
\]

两个非 \(d_3\)-dominant 扇区都满足

\[
\boxed{
n_3\le7S_{12}+4.
}
\]

所以一旦

\[
n_3>7S_{12}+4,
\]

就必须进入

\[
\boxed{
d_3=\max(s_1,s_2,d_3).
}
\]

这把真正可能无界的 DD 候选集中到第三分子 surplus 主导的一个扇区。

---

# 20. DD 的 near-square 结构

定义普通前两分子拼接

\[
\boxed{
A_{12}
=
a_1 10^{n_2}+a_2.
}
\]

从 exact lift 关于 \(a_3\) 的二次方程出发，其判别平方可写成

\[
\boxed{
Y^2
=
X^2
-
\mathcal N_{12}
10^{m_3}Q
\left(
10^{m_3}Q+2b_3
\right),
}
\]

其中

\[
\boxed{
X=GA_{12}10^{n_3}.
}
\]

所以

\[
\boxed{
(X-Y)(X+Y)
=
\mathcal N_{12}
10^{m_3}Q
(10^{m_3}Q+2b_3).
}
\]

由于 \(X,Y\) 为正整数，两个不同平方之间至少相差

\[
2X-1.
\]

因此得到

\[
\boxed{
2GA_{12}10^{n_3}-1
\le
\mathcal N_{12}
10^{m_3}Q
(10^{m_3}Q+2b_3).
}
\]

粗化后得到

\[
\boxed{
n_3
\le
2m_3
+
3S_{12}
+
|s_1-s_2|
+1.
}
\]

从而

\[
\boxed{
d_3
\le
m_3
+
3S_{12}
+
|s_1-s_2|
+1.
}
\]

---

# 21. DD 的 squarefree gap 加强

写

\[
\kappa=s_\kappa q_\square^2,
\]

其中 \(s_\kappa\) 为平方自由部分。

统一判别平方要求 \(W\) 被 \(q_\square\) 整除。因此小平方差因子不能只用“至少为 1”，而至少包含平方部分带来的额外离散尺度。

由此可加强为

\[
\boxed{
10^{d_3}A_{12}
<
40Q^2\mathcal N_{12}.
}
\]

按位数估计：

\[
\boxed{
d_3
\le
3S_{12}
+
|s_1-s_2|
+2.
}
\]

在 \(d_3\)-dominant 扇区中

\[
|s_1-s_2|
\le
2(S_{12}-1),
\]

所以

\[
\boxed{
d_3\le5S_{12}.
}
\]

结合统一 denominator-tail cone，

\[
m_3\le6S_{12}+3,
\]

得到

\[
\boxed{
n_3=m_3+d_3
\le11S_{12}+3.
}
\]

这已经把 DD 的所有第三块位数压入一个显式线性锥。

---

# 22. DD 的 \(2\)-进与 \(5\)-进双 resonance

near-square 的两个正因子可以写成

\[
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0},
\]

\[
F_+=
\frac{2\kappa\mathcal N_{12}\nu^2}{G_0},
\]

并且

\[
\boxed{
F_-+F_+
=
2GA_{12}10^{n_3}.
}
\]

对 \(p=2,5\)，若记

\[
r_p=v_p(\mu),
\qquad
s_p=v_p(\nu),
\]

\[
k_p=v_p(\kappa),
\qquad
f_p=v_p(\kappa+2G),
\]

\[
n_p=v_p(\mathcal N_{12}),
\qquad
c_p=v_p(G_0),
\]

则

\[
v_p(F_-)
=
v_p(2)+f_p+2r_p-c_p,
\]

\[
v_p(F_+)
=
v_p(2)+k_p+n_p+2s_p-c_p.
\]

如果两边赋值不同，那么和的 \(p\)-进深度只能等于较小者，无法支持极长的十进制尾零。

因此足够大的 \(n_3\) 必须发生精确 resonance：

\[
\boxed{
f_p+2r_p
=
k_p+n_p+2s_p.
}
\]

具体已经得到：

\[
\boxed{
d_3=\max,\ n_3\ge9S_{12}+2
\Longrightarrow
5\text{-adic resonance},
}
\]

以及

\[
\boxed{
d_3=\max,\ n_3\ge10S_{12}+11
\Longrightarrow
2\text{-adic resonance}.
}
\]

所以在最顶部区域

\[
\boxed{
n_3\ge10S_{12}+11
}
\]

时，\(2\) 与 \(5\) 两处必须同时 resonance。

约掉共同赋值以后，还会留下深 Hensel 相位

\[
\boxed{
\mu_p
\equiv
\pm\rho_p\nu_p
\pmod{p^{R_p}}.
}
\]

特别是 \(5\)-进剩余深度满足近似下界

\[
R_5>1.415S_{12}+9.
\]

这意味着模数

\[
5^{R_5}
\]

已经接近十进制尺度 \(10^{S_{12}}\)。

---

# 23. DD 的 near-\(S\)-unit 化

若

\[
n_3\ge10S_{12}+11,
\]

由

\[
d_3\le5S_{12}
\]

可得

\[
m_3\ge5S_{12}+11.
\]

定义

\[
\boxed{
\mathscr T
=
\frac{
\kappa^2(\kappa+2G)
}{
10^{m_3}
}
\in\mathbf Z_{>0}.
}
\]

统一尾权区间给出

\[
\boxed{
1\le\mathscr T<10^{S_{12}-7}.
}
\]

写

\[
\kappa=2^a5^bu,
\qquad
\gcd(u,10)=1,
\]

\[
\kappa+2G=2^c5^ev,
\qquad
\gcd(v,10)=1.
\]

则

\[
u^2\mid\mathscr T,
\qquad
v\mid\mathscr T.
\]

所以

\[
\boxed{
u<10^{(S_{12}-7)/2},
}
\]

\[
\boxed{
v<10^{S_{12}-7}.
}
\]

相对于

\[
\kappa,\kappa+2G
\asymp QG
\]

的整体尺度，其去掉 \(2,5\) 后的奇部分已经非常小。

因此最顶部 DD 候选必然满足：

\[
\boxed{
\kappa
\text{ 与 }
\kappa+2G
\text{ 同时接近 }2,5\text{-smooth}.
}
\]

---

# 24. DD 的 square-part 上下界夹逼与极端不对称

由统一终端式可以构造 \(\kappa\) 平方部分 \(q_\square\) 的上界。

一方面得到

\[
q_\square
<
1.92\times10^6
\,
10^{
9S_{12}
+
|s_1-s_2|
-
n_3
}.
\]

另一方面 \(5\)-进深尾给出

\[
\log_{10}q_\square
>
0.1747425\,m_3
-\frac{S_{12}}2
-0.619281.
\]

消元可得

\[
\boxed{
n_3
<
8.533128S_{12}
+
|s_1-s_2|
+
6.173325.
}
\]

如果仍在顶部

\[
n_3\ge10S_{12}+11,
\]

则必须有

\[
\boxed{
|s_1-s_2|
>
1.466872S_{12}
+
4.826675.
}
\]

利用 digit window 再转化为分母位数不对称：

\[
\boxed{
|m_1-m_2|
>
0.466872S_{12}
+
4.826675.
}
\]

所以一个前两分母块必须占据总位数的约 \(73.3\%\) 以上，另一个则低于约 \(26.7\%\)。

若长的一侧对应 \(s_1>s_2\)，还可得到短 numerator block 的估计

\[
\boxed{
n_2
<
0.266564S_{12}
-2.413.
}
\]

交换 \(1,2\) 可得对称结论。

因此 DD 的顶部空间已经从多参数无界族压成：

\[
\boxed{
\text{极端 denominator 不对称}
+
\text{一个极短 numerator block}
+
2/5\text{-adic 双 resonance}
+
\text{near-}S\text{-unit}.
}
\]

---

# 25. DD 最大 denominator-tail 层已排除

若

\[
m_3=6S_{12}+3,
\]

则

\[
\mathscr T=1,
\]

即

\[
\kappa^2(\kappa+2G)=10^{6S_{12}+3}.
\]

于是

\[
\kappa,\kappa+2G
\]

只能含素数 \(2,5\)。

利用有理 \(2,5\)-单位之间距离 \(1\) 的最小间距，可以得到

\[
\frac{2G}{\kappa}
\ge5^{-S_{12}}.
\]

但尾权区间给出

\[
\frac{2G}{\kappa}
<
\frac2Q
\le
20\cdot10^{-S_{12}}.
\]

当

\[
S_{12}\ge5
\]

时两者矛盾。

因此

\[
\boxed{
S_{12}\ge5
\Longrightarrow
m_3\ne6S_{12}+3,
}
\]

从而加强为

\[
\boxed{
m_3\le6S_{12}+2.
}
\]

---

# 26. DD 的双 resonance 终端尖角

把目前的上界和 resonance 阈值合并，DD 的最顶层为

\[
\boxed{
10S_{12}+11
\le
n_3
\le
11S_{12}+3.
}
\]

并同时满足

\[
\boxed{
d_3=\max(s_1,s_2,d_3),
}
\]

\[
\boxed{
d_3\le5S_{12},
}
\]

\[
\boxed{
m_3\le6S_{12}+2,
}
\]

\[
\boxed{
2\text{-adic 与 }5\text{-adic 同时 resonance},
}
\]

\[
\boxed{
|s_1-s_2|
>
1.466872S_{12}
+
4.826675,
}
\]

\[
\boxed{
|m_1-m_2|
>
0.466872S_{12}
+
4.826675.
}
\]

这是同时发生 \(2\)-进与 \(5\)-进 resonance 的终端尖角。需要注意，上述性质在本节之前只描述“如果候选进入该顶层，它必须长成什么样”；它们本身并没有排除随 \(S_{12}\) 一起增长的中低层线性锥。

---

# 27. DD 双 resonance 尖角的严格排除

这一节给出一个新的 prefix-uniform 矛盾。它不再需要猜测判别式最接近哪个平方，而是把十进制拼接 gap 的赋值与一个显式高度直接比较。

## 27.1 拼接行列式 gap

定义

\[
\boxed{
E
=
b_3A_{12}10^{d_3}-a_3Q.
}
\]

由 \(\mathcal R>r_3\) 以及拼接差的直接展开，

\[
\mathcal R-r_3
=
\frac{
10^{m_3}E
}{
b_3(10^{m_3}Q+b_3)
},
\]

因此

\[
\boxed{E\in\mathbf Z_{>0}.}
\]

利用

\[
b_3=\frac{10^{m_3}QG}{\kappa},
\]

可将统一球面 gap 精确写为

\[
\boxed{
\frac{\mu}{\nu}
=
G(\mathcal R-r_3)
=
\frac{
E\kappa^2
}{
10^{m_3}Q^2(\kappa+G)
},
}
\]

右端再约分成互素的 \(\mu,\nu\)。

## 27.2 resonance 的赋值转移

对 \(p\in\{2,5\}\) 记

\[
e_p=v_p(E),
\quad
q_p=v_p(Q),
\quad
k_p=v_p(\kappa),
\]

\[
h_p=v_p(\kappa+G),
\quad
f_p=v_p(\kappa+2G),
\quad
n_p=v_p(\mathcal N_{12}).
\]

由上式约分前后的赋值差，

\[
\boxed{
r_p-s_p
=
e_p+2k_p-m_3-2q_p-h_p.
}
\]

而 \(p\)-进 resonance 正是

\[
f_p+2r_p
=
k_p+n_p+2s_p.
\]

消去 \(r_p,s_p\) 得到精确恒等式

\[
\boxed{
3k_p+f_p
=
2m_3+4q_p+2h_p+n_p-2e_p.
}
\]

如果

\[
p\mid b_3,
\qquad
d_3+v_p(b_3)+v_p(A_{12})>q_p,
\]

则由 \(\gcd(a_3,b_3)=1\)，

\[
v_p(a_3Q)=q_p
<
v_p(b_3A_{12}10^{d_3}),
\]

所以

\[
\boxed{e_p=q_p.}
\]

代回 resonance 恒等式即得

\[
\boxed{
v_p\!\left(\kappa^3(\kappa+2G)\right)
=
3k_p+f_p
=
2m_3+2q_p+2h_p+n_p
\ge2m_3.
}
\]

这是尖角排除的核心赋值放大。

### 非 resonance 的两条精确支

同一个 gap 恒等式也能把非 resonance 情形从“赋值不相等”加强为两条显式线性恒等式。再记

\[
\lambda_p=v_p(2),
\qquad
g_p=v_p(G),
\qquad
a_p=v_p(A_{12}),
\]

并定义两个 near-square 因子的赋值差

\[
\Delta_p
=
v_p(F_-)-v_p(F_+)
=
f_p+2r_p-k_p-n_p-2s_p.
\]

由

\[
F_-+F_+=2GA_{12}10^{n_3}
\]

及

\[
v_p(F_-F_+)
=
2m_3+2q_p+f_p-k_p+n_p,
\]

当 \(\Delta_p\ne0\) 时，和的赋值等于两项中的较小者。把上述各式消元得到

\[
\boxed{
n_3
=
\begin{cases}
2m_3+3q_p+h_p+n_p-e_p-2k_p-\lambda_p-g_p-a_p,
&\Delta_p>0,\\[0.4em]
e_p+f_p+k_p-q_p-h_p-\lambda_p-g_p-a_p,
&\Delta_p<0.
\end{cases}
}
\]

这两式尚未单独给出绝对高度界，但它们已经把 DD 的剩余中低层精确分成 resonance、\(\Delta_p>0\) 与 \(\Delta_p<0\) 三种可逐支估计的状态，不再只有一个粗阈值。

## 27.3 统一阿基米德上界

令

\[
S=S_{12},
\qquad
N=10^S.
\]

\(Q\) 是恰有 \(S\) 位的前两分母拼接，并且 \(G=b_1b_2\)，因此

\[
Q<N,
\qquad
G<N.
\]

再由 \(\kappa\le10QG\)，

\[
\begin{aligned}
\kappa^3(\kappa+2G)
&\le
(10QG)^3G(10Q+2)\\
&=
10^4Q^3G^4\left(Q+\frac15\right)\\
&<
10^4N^8.
\end{aligned}
\]

于是得到严格高度上界

\[
\boxed{
\kappa^3(\kappa+2G)
<
10^{8S_{12}+4}.
}
\]

## 27.4 排除整个双 resonance 顶部

反设存在第 26 节的候选。由

\[
n_3\ge10S+11,
\qquad
d_3\le5S,
\]

有

\[
\boxed{m_3\ge5S+11.}
\]

又由统一尾长锥 \(m_3\le6S+3\)，

\[
d_3=n_3-m_3\ge4S+8.
\]

因此对 \(p=2,5\) 都有

\[
d_3>v_p(Q),
\]

因为 \(Q<10^S\)。

首先必有

\[
\boxed{5\mid b_3.}
\]

否则由 \(\kappa=10^{m_3}QG/b_3\)，

\[
v_5(\kappa)
=
m_3+v_5(Q)+v_5(G)
\ge m_3,
\]

从而

\[
\kappa\ge5^{m_3}
\ge5^{5S+11}
>10^{2S+1}
>\kappa,
\]

矛盾。这里最后一个上界来自

\[
\kappa\le10QG<10^{2S+1}.
\]

现在分两种奇偶性。

### 情形 I：\(2\mid b_3\)

对 \(p=2,5\)，上述深度不等式都成立，所以双 resonance 给出

\[
2^{2m_3}5^{2m_3}
=
10^{2m_3}
\mid
\kappa^3(\kappa+2G).
\]

因而

\[
\kappa^3(\kappa+2G)
\ge10^{2m_3}
\ge10^{10S+22},
\]

与 \(10^{8S+4}\) 的上界矛盾。

### 情形 II：\(2\nmid b_3\)

此时

\[
v_2(\kappa)
=
m_3+v_2(Q)+v_2(G)
\ge m_3.
\]

另一方面，\(5\mid b_3\) 且顶部的 \(5\)-进 resonance 已经给出

\[
v_5\!\left(\kappa^3(\kappa+2G)\right)
\ge2m_3.
\]

所以

\[
200^{m_3}
=
2^{3m_3}5^{2m_3}
\mid
\kappa^3(\kappa+2G).
\]

特别地

\[
\kappa^3(\kappa+2G)
\ge200^{m_3}
>10^{2m_3}
\ge10^{10S+22},
\]

同样矛盾。

因此得到：

\[
\boxed{
\text{DD 中不存在 }
10S_{12}+11
\le n_3\le
11S_{12}+3
\text{ 的候选}.
}
\]

同一论证还给出一个对剩余中高层有用的奇偶锁。若

\[
d_3=\max(s_1,s_2,d_3),
\qquad
n_3\ge9S+2,
\]

则 \(5\)-进 resonance 已被强制，且由 \(d_3\le5S\) 有

\[
m_3\ge4S+2.
\]

此时还有 \(d_3\ge3S-1>v_5(Q)\)，并且 \(5^{4S+2}>10^{2S+1}\)。因此与上面完全相同地，先得到 \(5\mid b_3\) 与

\[
5^{2m_3}\mid\kappa^3(\kappa+2G).
\]

如果 \(b_3\) 为奇数，则还有 \(v_2(\kappa)\ge m_3\)，从而

\[
200^{m_3}\mid\kappa^3(\kappa+2G).
\]

但

\[
200^{m_3}
>10^{2m_3}
\ge10^{8S+4},
\]

与高度上界矛盾。所以

\[
\boxed{
d_3=\max(s_1,s_2,d_3),\ n_3\ge9S_{12}+2
\Longrightarrow
10\mid b_3.
}
\]

在这个剩余中高层带中，五进相对位置还能被完全固定。记

\[
B_5=v_5(b_3),
\qquad
k_5=v_5(\kappa),
\qquad
g_5=v_5(G).
\]

已知 \(e_5=q_5\)。若 \(k_5<g_5\)，则超距性给出

\[
h_5=f_5=k_5.
\]

五进 resonance 恒等式因而化为

\[
2k_5=2m_3+2q_5+n_5,
\]

所以 \(k_5\ge m_3\)。但 \(k_5<g_5\) 意味着

\[
5^{m_3}
\le5^{k_5}
<5^{g_5}
\le G
<10^S,
\]

这与 \(m_3\ge4S+2\) 矛盾。

若 \(k_5=g_5\)，则 resonance 给出

\[
3g_5+f_5\ge2m_3.
\]

因此

\[
5^{2m_3}
\le
5^{3g_5+f_5}
\le
G^3(\kappa+2G)
<
11\cdot10^{5S}.
\]

可是

\[
5^{2m_3}
\ge
5^{8S+4}
>
11\cdot10^{5S},
\]

再次矛盾。因而只剩

\[
\boxed{k_5>g_5.}
\]

此时超距性给出

\[
h_5=f_5=g_5.
\]

五进 resonance 与 \(\kappa=10^{m_3}QG/b_3\) 分别化为

\[
\boxed{
3k_5
=
2m_3+2q_5+g_5+n_5,
}
\]

以及

\[
\boxed{
3B_5
=
m_3+q_5+2g_5-n_5.
}
\]

所以只发生五进 resonance 的中高层，已被压成一条唯一的五进线性正规形，并自动带有两条模 \(3\) 整除条件。

这条正规形还能恢复 \(\mu,\nu,G_0,F_\pm\) 的全部五进深度。为避免与全局位数混淆，本段仍以 \(r_5=v_5(\mu)\)、\(s_5=v_5(\nu)\)、\(n_5=v_5(\mathcal N_{12})\) 表示赋值。由 gap 赋值差与五进正规形，

\[
r_5-s_5
=
\frac{m_3+q_5-g_5+2n_5}{3}
>0.
\]

因为 \(\gcd(\mu,\nu)=1\)，必有

\[
\boxed{
s_5=0,
\qquad
r_5=\frac{m_3+q_5-g_5+2n_5}{3}.
}
\]

还有两个精确差值

\[
2r_5-n_5=k_5-g_5>0,
\]

\[
g_5+r_5-n_5=B_5>0.
\]

因此在

\[
G_0
=
\gcd(
\mathcal N_{12}\nu^2-\mu^2,
2G\mu\nu
)
\]

中，第一个参数的五进赋值恰为 \(n_5\)，第二个则为 \(n_5+B_5\)。所以

\[
\boxed{v_5(G_0)=n_5.}
\]

代回 \(F_-,F_+\) 的定义，两个因子的五进赋值不仅相等，而且都恰为

\[
\boxed{
v_5(F_-)=v_5(F_+)=k_5.
}
\]

记 \(a_5=v_5(A_{12})\)，则约去 \(5^{k_5}\) 后的两个五进单位在和中发生深度

\[
\boxed{
\mathscr R_5
=
n_3+g_5+a_5-k_5
}
\]

的精确抵消。由 \(n_3\ge9S+2\) 与 \(\kappa<10^{2S+1}\)，

\[
\boxed{
\mathscr R_5
>
\left(9-2\log_5 10\right)S
+2-\log_5 10
>
6.1386S+0.569.
}
\]

所以剩余中高层必须同时承担一个随 \(S\) 线性增长的超深五进单位抵消；这是后续做 rational reconstruction 或线性形下界时应直接攻击的目标。

五进正规形与阿基米德大小还会立即产生一次新的线性锥收缩。记

\[
L_5=\log_5 10.
\]

由 \(\kappa<10^{2S+1}\)，

\[
k_5<(2S+1)L_5.
\]

代入

\[
3k_5=2m_3+2q_5+g_5+n_5
\]

先得到

\[
\boxed{
m_3
<
3L_5S+\frac32L_5.
}
\]

再结合 \(d_3\le5S\)，对该中高层有

\[
\boxed{
n_3
<
\left(5+3L_5\right)S
+\frac32L_5.
}
\]

在未达到五进 resonance 阈值时本来就有 \(n_3\le9S+1\)，而非 \(d_3\)-dominant 扇区有 \(n_3\le7S+4\)。因此这一上界对全部 DD 候选都成立：

\[
\boxed{
n_3
<
\left(5+3\log_5 10\right)S_{12}
+\frac32\log_5 10
<
9.29203S_{12}+2.14602.
}
\]

这比先前的 \(n_3\le10S_{12}+10\) 真正降低了线性主系数。

还可以把这个新上界反代回 squarefree gap。在剩余中高层中，

\[
n_3\ge9S+2
\]

与 \(m_3<3L_5S+\frac32L_5\) 给出

\[
d_3
>
\left(9-3L_5\right)S
+2-\frac32L_5.
\]

第 21 节的界

\[
d_3
\le
3S+|s_1-s_2|+2
\]

因而加强为

\[
\boxed{
|s_1-s_2|
>
\left(6-3L_5\right)S
-\frac32L_5
>
1.70797S-2.14602.
}
\]

由 \(s_1+s_2\le2\) 且

\[
|n_1-n_2|
\le
n_1+n_2-2
\le S,
\]

得到分母位数不对称

\[
\boxed{
|m_1-m_2|
>
\left(5-3L_5\right)S
-\frac32L_5
>
0.70797S-2.14602.
}
\]

例如若 \(s_1>s_2\)，则第二分母块是长块，并且

\[
\boxed{
m_2
>
\left(3-\frac32L_5\right)S
-\frac34L_5
>
0.85398S-1.07301,
}
\]

\[
\boxed{
n_2
<
\left(\frac32L_5-2\right)S
+\frac34L_5
<
0.14602S+1.07301.
}
\]

交换 \(1,2\) 得到对称结论。这使

\[
\mathcal N_{12}=X_0^2+\varepsilon^2
\]

的 near-square 误差得到新的指数级界。确实，选取 \(X_0\) 为较大的 \(a_1b_2,a_2b_1\) 之一，则十进制位数窗口给出

\[
\frac{|\varepsilon|}{X_0}
<
10^{2-|s_1-s_2|}.
\]

因而：

\[
\boxed{
0<\frac{|\varepsilon|}{X_0}
<
10^{
-\left(6-3L_5\right)S
+2+\frac32L_5
}
<
10^{-1.70797S+4.14602}.
}
\]

而且这里不只有相对误差小。在 \(s_1>s_2\) 时，短块正是 \(a_2\) 与 \(b_1\)，因而

\[
|\varepsilon|=a_2b_1.
\]

由上述 \(n_2,m_1\) 界，

\[
\boxed{
0<|\varepsilon|
<
10^{
\left(3L_5-4\right)S
+\frac32L_5
}
<
10^{0.29203S+2.14602},
}
\]

\[
\boxed{
\varepsilon^2
<
10^{
\left(6L_5-8\right)S
+3L_5
}
<
10^{0.58406S+4.29203}.
}
\]

对称方向完全相同。

因而原先只在更高顶部出现的“极短 numerator block + near-square”现在已经下降到整个剩余单 resonance 薄带。

同时，由 \(m_3\ge4S+2\)，

\[
\boxed{
2q_5+g_5+n_5
<
\left(6L_5-8\right)S
+3L_5-4
<
0.58406S+0.29203.
}
\]

再代入

\[
3B_5=m_3+q_5+2g_5-n_5
\]

得到第三个统一挤压：

\[
\boxed{
B_5
>
\left(2-L_5\right)(2S+1)
>
1.13864S+0.569.
}
\]

因而剩余中高层同时具有：极小的前缀五进赋值预算、线性深度的 \(5\mid b_3\)，以及超深五进单位抵消。

还可以把 \(\kappa\) 本身的非五进核直接压小。写

\[
\kappa=5^{k_5}u_5,
\qquad
5\nmid u_5.
\]

由五进正规形与 \(m_3\ge4S+2\)，

\[
k_5
\ge
\frac{2m_3}{3}
\ge
\frac{8S+4}{3}.
\]

再用 \(\kappa<10^{2S+1}\)，

\[
\boxed{
u_5
<
10^{
\left(2-\frac83\log_{10}5\right)S
+1-\frac43\log_{10}5
}
<
10^{0.13609S+0.06805}.
}
\]

特别地，\(\mathfrak k=v_2(\kappa)=v_2(u_5)\)，所以

\[
\boxed{
\mathfrak k
<
0.45205S+0.22603.
}
\]

由

\[
\mathfrak b
=
m_3+\mathfrak q+\mathfrak g-\mathfrak k
\]

又得

\[
\boxed{
\mathfrak b
>
3.54795S+1.77397.
}
\]

也就是说，剩余中高层不仅有深五进尾，还必须有更深的二进尾；与此同时，\(\kappa\) 除去五次幂后的整个核只能占前缀高度约 \(13.61\%\) 的十进制位数。

二进侧也可以做出精确分支。为避免与全局位数 \(n_2\) 混淆，局部记

\[
\mathfrak b=v_2(b_3),
\quad
\mathfrak q=v_2(Q),
\quad
\mathfrak g=v_2(G),
\quad
\mathfrak n=v_2(\mathcal N_{12}),
\]

\[
\mathfrak a=v_2(A_{12}),
\quad
\mathfrak k=v_2(\kappa),
\quad
\mathfrak h=v_2(\kappa+G),
\quad
\mathfrak f=v_2(\kappa+2G).
\]

先证明在该中高层中必有

\[
\boxed{v_2(E)=\mathfrak q.}
\]

否则必须有

\[
\mathfrak b+d_3+\mathfrak a\le\mathfrak q.
\]

但由

\[
\mathfrak k
=
m_3+\mathfrak q+\mathfrak g-\mathfrak b
\]

就会得到

\[
\mathfrak k
\ge
m_3+d_3+\mathfrak a+\mathfrak g
\ge n_3.
\]

于是

\[
\kappa
\ge2^{n_3}
\ge2^{9S+2}
>10^{2S+1},
\]

与 \(\kappa<10^{2S+1}\) 矛盾。因此二进拼接 gap 中不可能发生比 \(Q\) 更深的额外抵消。

其次，二进侧不可能 resonance。否则 \(v_2(E)=\mathfrak q\) 给出

\[
2^{2m_3}\mid\kappa^3(\kappa+2G),
\]

而五进 resonance 已给出

\[
5^{2m_3}\mid\kappa^3(\kappa+2G).
\]

这会导致

\[
10^{2m_3}
\mid
\kappa^3(\kappa+2G),
\qquad
m_3\ge4S+2,
\]

再次与严格上界 \(10^{8S+4}\) 矛盾。

最后，在二进非 resonance 中还必有

\[
\boxed{\Delta_2>0.}
\]

确实，若 \(\Delta_2<0\)，则第 27.2 节的第二条恒等式化为

\[
n_3
=
\mathfrak f+\mathfrak k-\mathfrak h-1-\mathfrak g-\mathfrak a.
\]

对 \(\mathfrak k<\mathfrak g\)、\(\mathfrak k=\mathfrak g\)、\(\mathfrak k>\mathfrak g\) 分别使用超距性：

- \(\mathfrak k<\mathfrak g\) 时 \(\mathfrak f=\mathfrak h=\mathfrak k\)，右端为负；
- \(\mathfrak k=\mathfrak g\) 时 \(\mathfrak f=\mathfrak g\) 且 \(\mathfrak h\ge\mathfrak g+1\)，右端仍为负；
- \(\mathfrak k\ge\mathfrak g+2\) 时 \(\mathfrak h=\mathfrak g\)、\(\mathfrak f=\mathfrak g+1\)，从而 \(n_3\le\mathfrak k<\log_2(10^{2S+1})<9S+2\)；
- \(\mathfrak k=\mathfrak g+1\) 时 \(\mathfrak h=\mathfrak g\)，并且 \(n_3\le\mathfrak f\le\log_2(\kappa+2G)<\log_2(11\cdot10^{2S})<9S+2\).

四种情形均矛盾。所以中高层的二进侧只能落在 \(\Delta_2>0\) 支。把第 27.2 节的第一条恒等式与

\[
\mathfrak k=m_3+\mathfrak q+\mathfrak g-\mathfrak b
\]

合并，最终得到三条显式正规形：

\[
\boxed{
n_3
=
\begin{cases}
m_3+\mathfrak q+\mathfrak b+\mathfrak n-2\mathfrak g-1-\mathfrak a,
&\mathfrak k<\mathfrak g,\\[0.4em]
2\mathfrak b+\mathfrak h+\mathfrak n-3\mathfrak g-1-\mathfrak a,
&\mathfrak k=\mathfrak g,\\[0.4em]
2\mathfrak b-2\mathfrak g+\mathfrak n-1-\mathfrak a,
&\mathfrak k>\mathfrak g.
\end{cases}
}
\]

至此，原来的“单五进 resonance 中高层”已被改写为：一条唯一五进正规形，加上三条互斥的二进正规形。

特别地，五进正规形本身先给出统一相对上界

\[
\boxed{
n_3
<
\left(5+3\log_5 10\right)S_{12}
+\frac32\log_5 10.
}
\]

## 27.5 二进主导项关闭整个单五进 resonance 带

上面的三条二进正规形实际上还能继续闭合。关键不是再估计其中每一项，而是回到有理球面恒等式

\[
(\mathcal R-r_3)(\mathcal R+r_3)
=
r_1^2+r_2^2
=
\frac{\mathcal N_{12}}{G^2}.
\]

仍处在

\[
d_3=\max(s_1,s_2,d_3),
\qquad
n_3\ge9S+2
\]

的剩余中高层。沿用二进记号

\[
\mathfrak b=v_2(b_3),
\quad
\mathfrak q=v_2(Q),
\quad
\mathfrak g=v_2(G),
\quad
\mathfrak k=v_2(\kappa).
\]

第 27.4 节已经给出

\[
\mathfrak b>3.54795S+1.77397.
\]

另一方面，对 \(i=1,2\)，

\[
v_2(b_i)
<
m_i\log_2 10
\le
(S-1)\log_2 10
<
\mathfrak b.
\]

所以 \(b_3\) 的二进分母指数严格独占最大值。又因 \(2\mid b_3\) 与 \(\gcd(a_3,b_3)=1\)，\(a_3\) 为奇数，从而 \(r_3^2\) 是

\[
r_1^2+r_2^2+r_3^2=\mathcal R^2
\]

中唯一具有最小二进赋值的一项。因此

\[
v_2(\mathcal R)=-\mathfrak b.
\]

拼接分子

\[
\alpha=10^{n_3}A_{12}+a_3
\]

也是奇数，于是 exact lift 强迫

\[
v_2(\beta)=\mathfrak b.
\]

由

\[
\beta
=
10^{m_3}Q+b_3
=
10^{m_3}Q\frac{\kappa+G}{\kappa}
\]

以及

\[
\mathfrak b
=
m_3+\mathfrak q+\mathfrak g-\mathfrak k,
\]

得到

\[
\mathfrak h=v_2(\kappa+G)=\mathfrak g.
\]

若 \(\mathfrak k<\mathfrak g\)，则超距性给出 \(\mathfrak h=\mathfrak k\)；若 \(\mathfrak k=\mathfrak g\)，则 \(\mathfrak h\ge\mathfrak g+1\)。两者都不可能。因此三条二进正规形中前两条自动消失，并且

\[
\boxed{
\mathfrak k>\mathfrak g,
\qquad
\mathfrak h=\mathfrak g.
}
\]

现在记

\[
\delta=\mathcal R-r_3>0.
\]

由拼接 gap 赋值式 \(v_2(E)=\mathfrak q\)，

\[
v_2(\delta)
=
2\mathfrak k-m_3-\mathfrak q-2\mathfrak g.
\]

而

\[
v_2(2r_3)
=
1-\mathfrak b
=
1-m_3-\mathfrak q-\mathfrak g+\mathfrak k.
\]

两者之差恰为

\[
v_2(\delta)-v_2(2r_3)
=
\mathfrak k-\mathfrak g-1.
\]

若 \(\mathfrak k\ge\mathfrak g+2\)，则 \(2r_3\) 在

\[
\mathcal R+r_3=2r_3+\delta
\]

中严格主导。对球面差分取二进赋值便得到

\[
\mathfrak n-2\mathfrak g
=
v_2(\delta)+v_2(2r_3),
\]

即

\[
\mathfrak n
=
3\mathfrak k
-2m_3
-2\mathfrak q
-\mathfrak g
+1.
\]

但第 27.4 节的非五进核估计可以精确写成

\[
\mathfrak k
<
\eta S+\eta_0,
\qquad
\eta=\frac{8-2\log_2 10}{3}<0.452048,
\qquad
\eta_0=\frac{4-\log_2 10}{3}<0.226024.
\]

结合 \(m_3\ge4S+2\) 与 \(\mathfrak q,\mathfrak g\ge0\)，上式右端满足

\[
\mathfrak n
<
(3\eta-8)S+3\eta_0-3
<0,
\]

与 \(\mathfrak n\ge0\) 矛盾。故只能有

\[
\boxed{\mathfrak k=\mathfrak g+1.}
\]

为避免与全局的第二个有理数 \(r_2\) 及位数差 \(s_2\) 混淆，改记

\[
\rho_2=v_2(\mu),
\qquad
\sigma_2=v_2(\nu).
\]

由 gap 赋值差

\[
\rho_2-\sigma_2
=
\mathfrak g+2-m_3-\mathfrak q
<
(\eta-4)S+\eta_0-1
<0
\]

且右端严格为负，所以互素性给出

\[
\rho_2=0,
\qquad
\sigma_2=m_3+\mathfrak q-\mathfrak g-2.
\]

于是已证的 \(\Delta_2>0\) 化为

\[
0<\Delta_2
=
\mathfrak f+\mathfrak g+3
-\mathfrak n-2m_3-2\mathfrak q.
\]

因此

\[
\mathfrak f
\ge
2m_3+2\mathfrak q+\mathfrak n-\mathfrak g-2
\ge
8S+2-\mathfrak g.
\]

另一方面，\(\mathfrak g=\mathfrak k-1<\eta S+\eta_0-1\)，所以

\[
\mathfrak f
>
(8-\eta)S+3-\eta_0.
\]

可是统一高度窗口给出

\[
2^{\mathfrak f}
\le
\kappa+2G
<
11\cdot10^{2S},
\]

即

\[
\mathfrak f
<
2S\log_2 10+\log_2 11.
\]

两条界的差至少为

\[
\left(8-\eta-2\log_2 10\right)S
+3-\eta_0-\log_2 11
>
0.90409S-0.68546
>0,
\]

这里 \(S=m_1+m_2\ge2\)。矛盾。

所以单五进 resonance 的整个中高层带也是空的：

\[
\boxed{
d_3=\max(s_1,s_2,d_3),\quad
n_3\ge9S_{12}+2
\Longrightarrow
\text{无候选}.
}
\]

与两个非 \(d_3\)-dominant 扇区的 \(n_3\le7S_{12}+4\) 合并，得到这一阶段的 DD 统一相对界

\[
\boxed{
n_3\le9S_{12}+1.
}
\]

## 27.6 阈值以下上层的五进入口

虽然强制五进 resonance 的整带已经排除，但同一个方法还能把剩余区域的上层先压成两个精确状态。仍令

\[
L_5=\log_5 10.
\]

首先，若 \(d_3\)-dominant 候选满足 \(5\nmid b_3\)，则

\[
k_5
=
m_3+q_5+g_5
\ge
m_3.
\]

由 \(\kappa<10^{2S+1}\) 与 \(d_3\le5S\)，

\[
\boxed{
5\nmid b_3
\Longrightarrow
n_3
<
(5+2L_5)S+L_5
<
7.86136S+1.43068.
}
\]

所以

\[
n_3\ge(5+2L_5)S+L_5
\]

时必有 \(5\mid b_3\)。

其次，若

\[
n_3>(6+L_5)S+3,
\]

则由 \(m_3\le6S+3\) 得

\[
d_3>L_5S>q_5.
\]

在 \(5\mid b_3\) 时，\(\gcd(a_3,b_3)=1\) 给出 \(5\nmid a_3\)，故拼接行列式的第一项具有更深五进赋值，并且

\[
\boxed{e_5=q_5.}
\]

当 \(S\ge4\) 时，

\[
(5+2L_5)S+L_5
>
(6+L_5)S+3.
\]

对剩余的 \(S=2,3\)，整数性分别给出

\[
\begin{array}{c|c|c}
S&d_3\text{ 的下界}&q_5\text{ 的上界}\\
\hline
2&3&2\\
3&5&4
\end{array}
\]

所以仍有 \(d_3>q_5\)。因此对所有 \(S=m_1+m_2\ge2\)，只要进入

\[
\boxed{
n_3\ge(5+2L_5)S+L_5,
}
\]

就同时有

\[
\boxed{
5\mid b_3,
\qquad
e_5=q_5.
}
\]

在这个上层，五进的 \(\Delta_5<0\) 支不可能发生。事实上，第 27.2 节的第二条恒等式化为

\[
n_3=f_5+k_5-h_5-g_5-a_5.
\]

按 \(k_5\) 与 \(g_5\) 的相对大小分类：

- 若 \(k_5<g_5\)，则 \(h_5=f_5=k_5\)，右端为 \(k_5-g_5-a_5<0\)；
- 若 \(k_5>g_5\)，则 \(h_5=f_5=g_5\)，从而
  \[
  n_3=k_5-g_5-a_5<k_5<(2S+1)L_5;
  \]
- 若 \(k_5=g_5\)，则
  \[
  n_3=f_5-h_5-a_5
  \le f_5
  <
  2L_5S+\log_5 11.
  \]

三种情形都到不了 \((5+2L_5)S+L_5\)。所以

\[
\boxed{\Delta_5<0\text{ 在该上层为空}.}
\]

若该上层发生五进 resonance，则同样只能有 \(k_5>g_5\)。确实：

- \(k_5<g_5\) 时 resonance 化为
  \[
  2k_5=2m_3+2q_5+n_5,
  \]
  因而 \(k_5\ge m_3\)，但上层给出
  \[
  m_3\ge n_3-d_3\ge2L_5S+L_5>g_5>k_5,
  \]
  矛盾；
- \(k_5=g_5\) 时 resonance 给出
  \[
  g_5+f_5\ge2m_3.
  \]
  于是
  \[
  5^{2m_3}
  \le
  G(\kappa+2G)
  <
  11\cdot10^{3S},
  \]
  但 \(m_3\ge2L_5S+L_5\) 又使左端至少为 \(10^{4S+2}\)，仍然矛盾。

故 resonance 情形重新落入唯一五进正规形

\[
\boxed{
k_5>g_5,
\qquad
3k_5=2m_3+2q_5+g_5+n_5.
}
\]

\(\Delta_5>0\) 支也能化成唯一正规形。先排除 \(k_5<g_5\)。此时

\[
B_5
=
m_3+q_5+g_5-k_5
>
m_3
\ge
2L_5S+L_5.
\]

而对 \(i=1,2\)，

\[
v_5(b_i)
<
m_iL_5
\le
(S-1)L_5
<
B_5.
\]

所以 \(b_3\) 独占最大五进分母指数。与第 27.5 节的二进论证相同，\(r_3^2\) 是球面和中唯一具有最小五进赋值的一项；又因拼接分子是五进单位，exact lift 强迫

\[
v_5(\beta)=B_5.
\]

由

\[
v_5(\beta)
=
m_3+q_5+h_5-k_5
\]

与 \(B_5=m_3+q_5+g_5-k_5\)，得到 \(h_5=g_5\)。但 \(k_5<g_5\) 时超距性给出 \(h_5=k_5\)，矛盾。因此

\[
k_5\ge g_5.
\]

若 \(k_5>g_5\)，超距性直接给出 \(h_5=g_5\)；若 \(k_5=g_5\)，上面的 unique-max 论证仍给出同一结论。于是 \(\Delta_5>0\) 的第一条精确恒等式统一化为

\[
\boxed{
k_5\ge g_5,
\qquad
h_5=g_5,
\qquad
n_3
=
2m_3+2q_5+n_5-2k_5-a_5.
}
\]

因此阈值以下的剩余上层已经从三种五进状态压成两条显式正规形：

\[
\boxed{
\begin{array}{ll}
\text{resonance:}
&
k_5>g_5,\quad
3k_5=2m_3+2q_5+g_5+n_5,
\\[0.4em]
\Delta_5>0:
&
k_5\ge g_5,\quad
n_3=2m_3+2q_5+n_5-2k_5-a_5.
\end{array}
}
\]

这一区域仍未排除，但新的精确攻关带已从 \(9S+2\) 下移到约 \(7.86136S+1.43068\)。

## 27.7 二进分母主导位置与全奇分母锥

剩余 DD 还可以按三个分母的二进最高指数来自何处做全局切分。记

\[
e_i^{(2)}=v_2(b_i),
\qquad
E_2=\max_i e_i^{(2)}.
\]

若 \(E_2>0\)，整数球面模 \(4\) 与 primitive recovery 表明 \(E_2\) 必须唯一取得。exact lift 又进一步限制了这个唯一最大值的位置。

若 \(b_3\) 为奇数而 \(E_2>0\)，则拼接分母 \(\beta\) 为奇数，所以

\[
v_2(\alpha/\beta)\ge0.
\]

但球面和中唯一拥有最大二进分母指数的坐标会给出

\[
v_2(\mathcal R)=-E_2<0,
\]

矛盾。因此只要某个分母为偶数，就必有 \(2\mid b_3\)，从而 \(a_3\) 与拼接分子 \(\alpha\) 都是奇数。

沿用

\[
\mathfrak b=v_2(b_3),
\quad
\mathfrak g=v_2(G),
\quad
\mathfrak k=v_2(\kappa),
\quad
\mathfrak h=v_2(\kappa+G),
\]

由 \(v_2(\mathcal R)=-E_2\) 及 exact lift，

\[
v_2(\beta)=E_2.
\]

又

\[
v_2(\beta)-\mathfrak b
=
\mathfrak h-\mathfrak g.
\]

因此出现严格二分：

\[
\boxed{
\begin{array}{c|c}
\mathfrak b>\max(e_1^{(2)},e_2^{(2)})
&
\mathfrak k>\mathfrak g,\quad
\mathfrak h=\mathfrak g
\\[0.4em]
\max(e_1^{(2)},e_2^{(2)})>\mathfrak b
&
\mathfrak k=\mathfrak g,\quad
\mathfrak h>\mathfrak g.
\end{array}
}
\]

第二行还能给出第三尾长的显式前缀界。若唯一最大值来自 \(b_1\)，则

\[
\mathfrak q=e_2^{(2)},
\qquad
\mathfrak b=m_3+e_2^{(2)},
\qquad
e_1^{(2)}>m_3+e_2^{(2)},
\]

所以

\[
\boxed{m_3<e_1^{(2)}-e_2^{(2)}<m_1\log_2 10.}
\]

若唯一最大值来自 \(b_2\)，则必须先有

\[
e_2^{(2)}>e_1^{(2)}+m_2,
\qquad
\mathfrak q=e_1^{(2)}+m_2,
\]

并进一步有

\[
e_2^{(2)}>m_3+e_1^{(2)}+m_2.
\]

所以

\[
\boxed{
m_3
<
e_2^{(2)}-e_1^{(2)}-m_2
<
(\log_2 10-1)m_2.
}
\]

特别地，二进最高分母指数来自前缀时，总有

\[
\boxed{
n_3
<
(5+\log_2 10)S_{12}-\log_2 10.
}
\]

某些方向还能更强。若 \(s_1>s_2\)，则 \(b_1\) 是短 denominator block；如果此时二进唯一最大值恰来自 \(b_1\)，squarefree gap 给出

\[
\boxed{
n_3
<
(3+\log_2 10)S_{12}
+4-\log_2 10
<
6.32193S_{12}+0.67808.
}
\]

最后处理

\[
e_1^{(2)}=e_2^{(2)}=\mathfrak b=0,
\]

即三个分母全部为奇数的锥。此时

\[
\mathfrak q=\mathfrak g=0,
\qquad
\mathfrak k=m_3,
\qquad
\mathfrak h=0.
\]

记 \(e=v_2(E)\)。拼接 gap 赋值差给出

\[
v_2(\mu)-v_2(\nu)=m_3+e>0.
\]

由 \(\gcd(\mu,\nu)=1\)，

\[
v_2(\mu)=m_3+e,
\qquad
v_2(\nu)=0.
\]

再对 primitive recovery

\[
10^{m_3}QG_0=2\kappa\mu\nu
\]

取二进赋值，得到

\[
v_2(G_0)=m_3+e+1.
\]

由于

\[
G_0
=
\gcd(
\mathcal N_{12}\nu^2-\mu^2,\,
2G\mu\nu
),
\]

且 \(\mu^2\) 已被 \(2^{2(m_3+e)}\) 整除，必有

\[
\boxed{
v_2(\mathcal N_{12})\ge m_3+e+1.
}
\]

写 \(u_i=v_2(a_i)\)。因 \(b_1,b_2\) 为奇数，二平方和的二进赋值律给出

\[
\min(u_1,u_2)
\ge
\frac{m_3+e}{2}.
\]

所以两个前缀分子都必须含有至少约 \(2^{m_3/2}\) 的公共二进尺度。结合

\[
n_1+n_2=S+s_1+s_2\le S+2
\]

先得到

\[
m_3<(S+2)\log_2 10.
\]

再令 \(D_s=|s_1-s_2|\)。较短的 numerator block 满足

\[
n_{\rm short}\le S-\frac{D_s}{2},
\]

而 squarefree gap 给出

\[
D_s\ge d_3-3S-2.
\]

把 \(m_3/2<(\log_2 10)n_{\rm short}\) 代入并消去 \(D_s\)，得到

\[
d_3
<
5S+2-\frac{m_3}{\log_2 10}.
\]

最终：

\[
\boxed{
\text{三个分母全奇}
\Longrightarrow
n_3
<
(4+\log_2 10)S_{12}
+2\log_2 10
<
7.32193S_{12}+6.64386.
}
\]

这些界尚未排除整个低层，但已证明 DD 的真正最危险锥必须让 \(b_3\) 承担二进唯一最大值，或落入“\(b_1\) 为长 denominator block 且独占二进最大”的定向前缀锥。

## 27.8 两条五进正规形与二进主导位置的交叉

第 27.6 节上层中的两条五进正规形还可以与第 27.7 节的二进分母位置逐一相交，从而再次降低 DD 的全局线性主系数。

### 小因子 \(F_-\) 的统一阿基米德高度

先记

\[
P=\frac{10^{d_3}A_{12}}{Q}.
\]

由两级正权平均，

\[
\mathcal R
=
\frac{\kappa P+Gr_3}{\kappa+G},
\qquad
P>\mathcal R>r_3.
\]

利用 primitive recovery，可以把 near-square 两因子在总和中的比例精确写成

\[
\frac{F_+}{F_-+F_+}
=
\frac{\mathcal R+r_3}{2P},
\]

\[
\frac{F_-}{F_-+F_+}
=
\frac{2P-\mathcal R-r_3}{2P}.
\]

令 \(\delta=\mathcal R-r_3\)。由于

\[
2P-\mathcal R-r_3
=
\frac{\kappa+2G}{\kappa}\delta
\]

且 \(\kappa>QG\)，有

\[
\frac{F_-}{F_-+F_+}
<
\frac{\delta}{P}.
\]

再由

\[
\delta(\mathcal R+r_3)
=
\frac{\mathcal N_{12}}{G^2}
=
r_1^2+r_2^2,
\]

以及十进制位数窗口，若

\[
D_s=|s_1-s_2|,
\]

则

\[
\frac{\delta}{P}
<
10^{D_s-2d_3+4}.
\]

结合

\[
F_-+F_+=2GA_{12}10^{n_3},
\qquad
s_1+s_2\le2,
\qquad
D_s\le2(S-1),
\]

得到统一阿基米德上界

\[
\boxed{
F_-
<
10^{4S+2m_3-n_3+5}.
}
\]

这个上界本身与五进处于 resonance 还是 non-resonance 无关；下面两支都可使用。

### 四种二进位置给出的公共因子

记

\[
\mathfrak r=v_2(\mu),\qquad
\mathfrak s=v_2(\nu),\qquad
\mathfrak c=v_2(G_0).
\]

先设 \(b_3\) 独占二进最大，并仍写

\[
t_2=\mathfrak k-\mathfrak g\ge1.
\]

若 \(t_2\ge2\) 且发生二进 resonance（下一个小节将证明当前上层必然如此），则

\[
\mathfrak n
=
3\mathfrak k-2m_3-2\mathfrak q-\mathfrak g+1.
\]

此时

\[
2(\mathfrak r-\mathfrak s)=\mathfrak n+t_2-1>0,
\]

故 \(\mathfrak s=0\)。把 primitive recovery

\[
10^{m_3}QG_0=2\kappa\mu\nu
\]

代入 \(F_-\) 的赋值式，逐项消去后得到

\[
\boxed{v_2(F_-)=\mathfrak k+1.}
\]

若 \(t_2=1\) 且发生二进 resonance，则不必判断
\(\mathfrak r-\mathfrak s\) 的符号。由 gap 赋值差

\[
\mathfrak r-\mathfrak s
=
\mathfrak k+1-m_3-\mathfrak q
\]

与 primitive recovery 直接得到

\[
\boxed{v_2(F_-)=\mathfrak f+1.}
\]

再看二进最高分母指数来自前缀的两种情形。沿用第 27.7 节的记号
\(e_i^{(2)}=v_2(b_i)\)。若最大值来自 \(b_1\)，令
\(E_{\max}=e_1^{(2)}\)、\(l=e_2^{(2)}\)。则

\[
\mathfrak q=l,\quad
\mathfrak b=m_3+l,\quad
\mathfrak k=\mathfrak g=E_{\max}+l,\quad
\mathfrak h>\mathfrak g.
\]

拼接 gap 的二进深度为 \(l\)，故

\[
\mathfrak r=l,\quad \mathfrak s=0,\quad
\mathfrak c=1+\mathfrak g-m_3.
\]

又因 \(\mathfrak k=\mathfrak g<\mathfrak h\)，有
\(\mathfrak f=\mathfrak g\)，从而

\[
\boxed{v_2(F_-)=m_3+2l.}
\]

若最大值来自 \(b_2\)，令
\(E_{\max}=e_2^{(2)}\)、\(l=e_1^{(2)}\)。同样的逐项计算给出

\[
\mathfrak q=l+m_2,\quad
\mathfrak k=\mathfrak g=E_{\max}+l,\quad
\mathfrak r=l,\quad
\mathfrak s=0,
\]

以及

\[
\boxed{v_2(F_-)=m_3+m_2+2l.}
\]

所以前缀独占二进最大时总有

\[
\boxed{v_2(F_-)\ge m_3.}
\]

最后，若三个分母全奇，第 27.7 节已有

\[
\mathfrak k=m_3,\quad
\mathfrak g=0,\quad
\mathfrak r=m_3+e,\quad
\mathfrak s=0,\quad
\mathfrak c=m_3+e+1.
\]

这里 \(e=v_2(E)\)。由于 \(m_3\ge1\)，总有
\(v_2(\kappa+2G)\ge1\)，因此

\[
\boxed{v_2(F_-)\ge m_3+1.}
\]

这就给出了后面所需的完整二进因子表：

\[
\boxed{
\begin{array}{c|c}
\text{二进位置}&v_2(F_-)\\
\hline
b_3\text{ 独占最大},\ t_2\ge2&\mathfrak k+1\\
b_3\text{ 独占最大},\ t_2=1&\mathfrak f+1\\
\text{前缀独占最大}&\ge m_3\\
\text{三个分母全奇}&\ge m_3+1
\end{array}}
\]

### \(\Delta_5>0\) 的五进因子

另一方面，在 \(\Delta_5>0\) 支中，

\[
v_5(F_-)>v_5(F_+)
=
v_5(F_-+F_+)
=
n_3+g_5+a_5.
\]

所以

\[
F_-\ge5^{n_3+g_5+a_5+1}\ge5^{n_3+1}.
\]

记

\[
c_5=\log_{10}5.
\]

上下界合并为

\[
\boxed{
(1+c_5)n_3
<
4S+2m_3+5-c_5.
}
\tag{DD-\Delta_5\text{-size}}
\]

### 上层中第三分母承担二进唯一最大时必二进 resonance

现在仍处于第 27.6 节的上层

\[
n_3\ge(5+2\log_5 10)S+\log_5 10.
\]

若 \(b_3\) 承担二进唯一最大值，则

\[
\mathfrak h=\mathfrak g,
\qquad
\mathfrak k>\mathfrak g.
\]

由于该上层满足

\[
n_3
>
2S\log_2 10+\log_2 10,
\]

第 27.4 节证明 \(v_2(E)=\mathfrak q\) 的同一论证仍然适用。令

\[
t_2=\mathfrak k-\mathfrak g\ge1.
\]

若 \(t_2\ge2\)，则 \(\mathfrak f=\mathfrak g+1\)，并且 \(\delta\) 与 \(2r_3\) 的二进赋值不同。球面差分给出

\[
\mathfrak n
=
3\mathfrak k
-2m_3
-2\mathfrak q
-\mathfrak g
+1.
\]

此时

\[
2\bigl(v_2(\mu)-v_2(\nu)\bigr)
=
\mathfrak n+t_2-1>0,
\]

直接代回 \(\Delta_2\) 可得

\[
\boxed{\Delta_2=0.}
\]

也就是说 \(t_2\ge2\) 自动强制二进 resonance，并且

\[
\boxed{
\mathfrak k\ge\frac{2m_3-1}{3}.
}
\]

若 \(t_2=1\)，则二进非 resonance 的两条正规形分别给出

\[
\Delta_2<0
\Longrightarrow
n_3=\mathfrak f-\mathfrak g-\mathfrak a<\mathfrak f,
\]

\[
\Delta_2>0
\Longrightarrow
\Delta_2
=
\mathfrak f-(n_3+\mathfrak g+\mathfrak a)>0.
\]

但

\[
\mathfrak f
<
2S\log_2 10+\log_2 11
<
(5+2\log_5 10)S+\log_5 10
\]

对 \(S\ge2\) 成立，所以两条非 resonance 支都不能进入当前上层。因此：

\[
\boxed{
\text{当前上层中，只要 \(b_3\) 独占二进最大，就必发生二进 resonance.}
}
\]

### 五进 resonance 支的新上界

若同时发生五进 resonance，则

\[
k_5\ge\frac{2m_3}{3}.
\]

而且第 27.4 节中由唯一五进正规形得到的 recovery 计算原样适用：

\[
\boxed{v_5(F_-)=v_5(F_+)=k_5.}
\]

当 \(t_2\ge2\) 时，

\[
\kappa
\ge
2^{(2m_3-1)/3}5^{2m_3/3}.
\]

与 \(\kappa<10^{2S+1}\) 比较，

\[
\boxed{
m_3
<
3S+\frac32+\frac12\log_{10}2.
}
\]

令

\[
a=\log_{10}2,
\qquad
b=\log_{10}5=1-a.
\]

由刚才的二进因子表，

\[
F_-
\ge
2^{\mathfrak k+1}5^{k_5}
\ge
2^{(2m_3-1)/3+1}5^{2m_3/3}.
\]

与统一阿基米德上界比较，

\[
n_3
<
4S+\frac43m_3+5-\frac23a.
\]

代入上面的 \(m_3\) 界，常数项恰好化简为 \(7\)，所以

\[
\boxed{t_2\ge2\Longrightarrow n_3<8S+7.}
\]

当 \(t_2=1\) 时，二进 resonance 化为

\[
\mathfrak f+\mathfrak g+3
=
2m_3+2\mathfrak q+\mathfrak n.
\]

再用

\[
\mathfrak k
<
2S\log_2 10+\log_2 10
-\frac23m_3\log_2 5
\]

和

\[
\mathfrak f
<
2S\log_2 10+\log_2 11,
\]

得到

\[
\boxed{
m_3
<
3.74518S+2.47506.
}
\]

此时二进因子表给出

\[
v_2(F_-)=\mathfrak f+1,
\qquad
\mathfrak f+\mathfrak g+3\ge2m_3.
\]

另一方面，\(\mathfrak k=\mathfrak g+1\) 与
\(k_5\ge2m_3/3\) 给出

\[
a(\mathfrak g+1)+bk_5<2S+1.
\]

消去 \(\mathfrak g\)，得到乘法高度下界

\[
\log_{10}F_-
>
\left(2a+\frac43b\right)m_3
-2S-1-a.
\]

再与统一上界比较并代入 \(m_3\) 界，

\[
\boxed{
t_2=1
\Longrightarrow
n_3<7.74518S+7.45436.
}
\]

对“全奇分母”和“前缀独占二进最大”，有

\[
v_2(\kappa)\ge m_3,
\qquad
k_5\ge\frac23m_3.
\]

所以

\[
\left(a+\frac23b\right)m_3<2S+1,
\]

再结合其 \(F_-\) 二进因子，直接得到

\[
n_3<7.21506S+6.60753<8S+7.
\]

故对所有 \(S\ge2\)，当前上层的五进 resonance 支统一满足

\[
\boxed{n_3<8S+7.}
\]

### \(\Delta_5>0\) 支的新上界

仍只需考虑 \(b_3\) 独占二进最大；其余二进位置已由第 27.7 节给出更强上界。

若 \(t_2=1\)，二进 resonance 及

\[
2^{\mathfrak f+\mathfrak g}
\le
G(\kappa+2G)
<
11\cdot10^{3S}
\]

给出

\[
m_3
<
\frac{
3S\log_2 10+\log_2 11+3
}{2}.
\]

这里还能保留 \(F_-\) 的二进公因子。由

\[
v_2(F_-)=\mathfrak f+1,
\qquad
\mathfrak f+\mathfrak g+3\ge2m_3,
\qquad
G<10^S,
\]

得到

\[
\log_{10}F_-
>
2am_3-S-2a+b(n_3+1).
\]

因而

\[
(1+b)n_3
<
5S+(2-2a)m_3+5+2a-b.
\]

同时上面的 \(m_3\) 界用十进制写成

\[
m_3
<
\frac{3S+\log_{10}11+3a}{2a}
<
4.982893S+3.229716.
\]

故

\[
\boxed{
t_2=1
\Longrightarrow
n_3<7.042964S+5.543382.
}
\]

若 \(t_2\ge2\)，则

\[
\mathfrak k\ge\frac{2m_3-1}{3}.
\]

在五进侧，若 \(k_5>g_5\)，尾整除立即给出 \(k_5\ge(m_3+1)/3\)，所得界比下面更强。最坏情形是

\[
k_5=g_5.
\]

这时由 \(\kappa\) 的大小与

\[
2k_5+f_5\ge m_3
\]

分别得到

\[
\frac{2\log_{10}2}{3}m_3
+(\log_{10}5)g_5
<
2S+1+\frac13\log_{10}2,
\]

\[
(\log_{10}5)(m_3-2g_5)
<
2S+\log_{10}11.
\]

消去 \(g_5\)，

\[
\boxed{
m_3
<
5.45285S+2.94643.
}
\]

再代入小因子高度式，

\[
\boxed{
n_3
<
8.12927S+5.53388.
}
\]

这是 \(\Delta_5>0\) 支中的最坏线性界。

最后核对另外两种二进位置。由二进因子表与
\(v_5(F_-)\ge n_3+1\)，

\[
(1+b)n_3
<
4S+(2-a)m_3+5-b.
\]

全奇分母满足 \(m_3<(S+2)/a\)，前缀独占最大满足更强的
\(m_3<(S-1)/a\)。取较弱者也只有

\[
n_3<5.67630S+9.17541,
\]

它对 \(S\ge2\) 严格小于上述最坏界。因此没有遗漏二进位置。

### 新的 DD 全局相对界

以下 \(8.12927\) 界是第 27.8 节得到的中间结果；第 27.10 节会在排除整个上层 \(\Delta_5>0\) 支后把它继续加强。

低于第 27.6 节入口的候选本来就满足

\[
n_3<(5+2\log_5 10)S+\log_5 10.
\]

入口以上的 resonance 与 \(\Delta_5>0\) 两支则分别由刚才的两个界控制；非 \(d_3\)-dominant 扇区还有 \(n_3\le7S+4\)。因此对全部 DD 候选，

\[
\boxed{
n_3
<
8.12927S_{12}+7.
}
\]

这里把常数统一放宽为 \(7\)，以同时覆盖 resonance 支的
\(8S+7\)。这个结果把线性主系数从 \(9\) 再降到约
\(8.12927\)，但仍然不是绝对高度界。

## 27.9 这一中间结论的逻辑边界

上述证明把五进入口以上的两条精确支继续压缩到了新的线性带内，但它不能被表述为“DD 分支已全局关闭”。原因是

\[
n_3<8.12927S_{12}+7
\]

仍然只是相对线性界；当 \(S_{12}\to\infty\) 时，它仍允许无界序列。现在 DD 的主要剩余区域可分为：

1. \(d_3\) 不是最大 surplus 的扇区，其中
   \[
   n_3\le7S_{12}+4;
   \]
2. \(d_3\)-dominant 且低于 \(5\)-进入口的区域，其中
   \[
   n_3<(5+2\log_5 10)S_{12}+\log_5 10;
   \]
3. \(d_3\)-dominant 且达到该入口的窄带，其中只剩第 27.6 节的
   resonance 与 \(\Delta_5>0\) 两条正规形，并满足
   \[
   (5+2\log_5 10)S_{12}+\log_5 10
   \le n_3
   <8.12927S_{12}+7.
   \]

新证明的核心方法——把 \(F_-\) 的二进与五进公因子同时送入阿基米德小因子上界——已经把主系数继续降低，但尚未产生与 \(S_{12}\) 无关的高度界。DD 的下一步必须在上述三类剩余锥中寻找新的 prefix-uniform 约束；特别是要继续利用 \(F_-/F_+\) 的约化后互补因子，而不能把本节的相对界当成闭环。

## 27.10 排除五进入口以上的整个 \(\Delta_5>0\) 支

**状态：`已严格完成`。** 本节只加强 DD 的全局相对界，不关闭 DD 分支。依赖第 27.2、27.6–27.8 节。

第 27.6 节把五进入口以上的 non-resonance 候选压到了
\(\Delta_5>0\)，并得到二分

\[
\boxed{
k_5=g_5
\quad\text{或}\quad
k_5>g_5.
}
\]

下面用 primitive recovery 同时排除这两种可能。仍处在第 27.6 节的五进入口以上，故

\[
n_3\ge(5+2L_5)S+L_5,
\qquad
L_5=\log_5 10,
\]

并且已有

\[
5\mid b_3,
\qquad
e_5=q_5,
\qquad
k_5\ge g_5,
\qquad
h_5=g_5.
\]

反设 \(k_5=g_5\)。由

\[
k_5=m_3+q_5+g_5-B_5
\]

得到

\[
\boxed{B_5=m_3+q_5.}
\]

此时 gap 赋值差为

\[
r_5-s_5
=
e_5+2k_5-m_3-2q_5-h_5
=
g_5-B_5<0.
\]

这里 \(B_5>g_5\) 可直接由

\[
m_3\ge n_3-d_3
\ge2L_5S+L_5
>g_5
\]

得到。于是 \(\gcd(\mu,\nu)=1\) 给出

\[
r_5=0,
\qquad
s_5=B_5-g_5.
\]

把 primitive recovery 约去公共的 \(10^{m_3}Q\)，可得

\[
\boxed{b_3G_0=2G\mu\nu.}
\]

对它取五进赋值，若 \(c_5'=v_5(G_0)\)，则

\[
B_5+c_5'
=g_5+r_5+s_5
=B_5,
\]

所以

\[
\boxed{c_5'=0.}
\]

因此

\[
v_5(F_-)
=f_5+2r_5-c_5'
=f_5.
\]

但 \(\Delta_5>0\) 意味着 \(F_+\) 是五进赋值较小的因子。由

\[
F_-+F_+=2GA_{12}10^{n_3}
\]

便有

\[
v_5(F_+)=n_3+g_5+a_5,
\qquad
f_5=v_5(F_-)>n_3+g_5+a_5\ge n_3.
\]

另一方面，统一高度窗口给出

\[
5^{f_5}
\le\kappa+2G
<11\cdot10^{2S},
\]

从而

\[
f_5<2L_5S+\log_5 11.
\]

这与入口下界矛盾，因为对 \(S\ge2\)，

\[
n_3
\ge(5+2L_5)S+L_5
>2L_5S+\log_5 11.
\]

所以

\[
\boxed{
k_5=g_5
\Longrightarrow
\text{矛盾}.
}
\tag{DD-\Delta_5\text{-equal-empty}}
\]

现在设

\[
k_5>g_5.
\]

令

\[
M_5=m_3+q_5,
\qquad
u_5=r_5-s_5.
\]

由尾权定义和 gap 赋值差，

\[
B_5=M_5+g_5-k_5,
\qquad
u_5=2k_5-M_5-g_5.
\]

若 \(u_5\le0\)，则 \(\gcd(\mu,\nu)=1\) 给出

\[
r_5=0,
\qquad
s_5=-u_5.
\]

再对

\[
b_3G_0=2G\mu\nu
\]

取五进赋值，会得到

\[
c_5'
=g_5+s_5-B_5
=g_5-k_5<0,
\]

不可能。因此

\[
u_5>0,
\qquad
r_5=u_5,
\qquad
s_5=0.
\]

同一 recovery 恒等式于是给出

\[
c_5'
=g_5+r_5-B_5
=3k_5-2M_5-g_5.
\]

由于 \(k_5>g_5\)，超距性还有

\[
f_5=g_5.
\]

代回 \(F_-\) 的赋值式，所有 \(M_5,g_5\) 项恰好消去：

\[
\boxed{
v_5(F_-)
=f_5+2r_5-c_5'
=k_5.
}
\]

但在 \(\Delta_5>0\) 中，

\[
v_5(F_-)
>
v_5(F_+)
=
v_5(F_-+F_+)
=n_3+g_5+a_5.
\]

因而

\[
k_5>n_3.
\]

这与尾权高度立即矛盾：

\[
k_5
<
\log_5(10^{2S+1})
=(2S+1)L_5
<n_3,
\]

其中最后一步正是五进入口

\[
n_3\ge(5+2L_5)S+L_5.
\]

所以

\[
\boxed{
n_3\ge(5+2L_5)S+L_5
\Longrightarrow
\Delta_5>0\text{ 为空}.
}
\tag{DD-\Delta_5\text{-upper-empty}}
\]

第 27.6 节已经在同一区域排除了 \(\Delta_5<0\)。因此五进入口以上只剩 resonance；第 27.8 节对此已有

\[
\boxed{
n_3<8S_{12}+7.
}
\]

低于五进入口的 dominant 候选满足

\[
n_3<(5+2L_5)S+L_5<8S+7,
\]

非 \(d_3\)-dominant 扇区则满足 \(n_3\le7S+4<8S+7\)。综上，所有 DD 候选都服从上述严格界。

由于 \(n_3,S_{12}\) 均为整数，这等价于这一阶段的 DD 全局相对界

\[
\boxed{
n_3\le8S_{12}+6.
}
\tag{DD-global-relative-8}
\]

这仍允许 \(S_{12}\to\infty\)，所以它是 `已严格完成` 的相对锥收缩，不是 DD 空性或主不存在性定理。

### 机械核验（非证明器）

第 27.10 节中的 recovery 消元与高度余量可由

```bash
uv run python scripts/check_dd_2710.py
```

复核。脚本输出三条符号恒等式、入口余量，并以
`DD 27.10 symbolic checks: OK` 结束。它没有枚举参数；这里的无界
\(S\ge2\) 覆盖来自正文中的符号恒等式和正斜率论证，而不是脚本循环。

## 27.11 resonance 的加权赋值惩罚

**状态：`已严格完成`。** 本节加强入口以上唯一剩余的 resonance
支，并把 DD 全局相对界再降低一个整数层；它仍不关闭 DD。依赖第
27.7–27.10 节。

### 恢复 \(F_-\) 上界中被粗化的常数

第 27.8 节已经证明

\[
\frac{F_-}{F_-+F_+}
<10^{D_s-2d_3+4},
\qquad
D_s=|s_1-s_2|.
\]

在 \(d_3\)-dominant 扇区，

\[
G<10^S,
\qquad
A_{12}<10^{S+s_1+s_2}\le10^{S+2},
\qquad
D_s\le2S-2.
\]

因此不必把前面的系数 \(2\) 粗化成一个完整十进制位。由

\[
F_-+F_+=2GA_{12}10^{n_3}
\]

直接得到

\[
\boxed{
F_-
<
2\cdot10^{4S+2m_3-n_3+4}
=
10^{4S+2m_3-n_3+4+a},
\qquad
a=\log_{10}2.
}
\tag{DD-Fminus-sharp}
\]

这比第 27.8 节使用的 \(10^{4S+2m_3-n_3+5}\) 严格节省
\(1-a=\log_{10}5\) 个十进制指数。

### \(b_3\) 独占二进最大且 \(t_2\ge2\)

仍令

\[
b=\log_{10}5=1-a.
\]

对二进侧沿用

\[
\mathfrak q=v_2(Q),
\quad
\mathfrak g=v_2(G),
\quad
\mathfrak n=v_2(\mathcal N_{12}),
\quad
\mathfrak k=v_2(\kappa),
\]

并定义三个加权前缀赋值

\[
V_Q=a\mathfrak q+bq_5,
\qquad
V_G=a\mathfrak g+bg_5,
\qquad
V_N=a\mathfrak n+bn_5.
\]

二进、五进 resonance 正规形分别为

\[
3\mathfrak k
=2m_3+2\mathfrak q+\mathfrak g+\mathfrak n-1,
\]

\[
3k_5
=2m_3+2q_5+g_5+n_5.
\]

所以

\[
a\mathfrak k+bk_5
=
\frac{2m_3}{3}
+\frac{2V_Q}{3}
+\frac{V_G}{3}
+\frac{V_N}{3}
-\frac a3.
\]

由 \(2^{\mathfrak k}5^{k_5}\le\kappa<10^{2S+1}\)，

\[
m_3
<
3S+\frac32+\frac a2
-V_Q-\frac{V_G}{2}-\frac{V_N}{2}.
\tag{DD-resonance-m-weighted}
\]

另一方面，第 27.8 节的因子表与五进 recovery 给出

\[
v_2(F_-)=\mathfrak k+1,
\qquad
v_5(F_-)=k_5.
\]

把这个下界与 \((\mathrm{DD\text{-}Fminus\text{-}sharp})\) 比较，再代入
\((\mathrm{DD\text{-}resonance\text{-}m\text{-}weighted})\)，逐项化简得到

\[
\boxed{
n_3
<
8S+6+a
-2V_Q-V_G-V_N.
}
\tag{DD-resonance-weighted}
\]

现在定义整数

\[
\mathscr A_2
=2\mathfrak q+\mathfrak g+\mathfrak n,
\qquad
\mathscr A_5
=2q_5+g_5+n_5,
\]

\[
\Xi
=2^{\mathscr A_2}5^{\mathscr A_5}.
\]

则惩罚项正是

\[
2V_Q+V_G+V_N=\log_{10}\Xi.
\]

两条 resonance 正规形的模 \(3\) 条件给出

\[
2m_3+\mathscr A_2-1\equiv0\pmod3,
\qquad
2m_3+\mathscr A_5\equiv0\pmod3,
\]

故

\[
\boxed{
\mathscr A_2-\mathscr A_5\equiv1\pmod3.
}
\tag{DD-resonance-mod3}
\]

特别地 \((\mathscr A_2,\mathscr A_5)\ne(0,0)\)，所以

\[
\Xi\ge2,
\qquad
\log_{10}\Xi\ge a.
\]

代回加权界便有

\[
\boxed{
t_2\ge2
\Longrightarrow
n_3<8S+6.
}
\tag{DD-resonance-t2-ge2-new}
\]

### 其余二进位置

当 \(b_3\) 独占二进最大但 \(t_2=1\) 时，保留第 27.8 节推导中的精确常数。令

\[
c=\log_{10}11.
\]

该节的 \(m_3\) 上界与新的小因子上界分别给出

\[
m_3
<
\frac{6}{1+2a}S
+
\frac{3(1+c+2a)}{2(1+2a)},
\]

\[
n_3
<
\frac{10+8a}{1+2a}S
+5+2a
+\frac{(1-a)(1+c+2a)}{1+2a}.
\tag{DD-resonance-t2-one-exact}
\]

只需非常粗的严格对数夹逼

\[
\frac3{10}<a<\frac13,
\qquad
c<\frac{21}{20}
\]

即可完成比较；它们分别来自
\(10^3<2^{10}\)、\(2^3<10\) 与
\(11^{20}<10^{21}\)。于是

\[
\frac{10+8a}{1+2a}<\frac{31}{4},
\]

且上式常数项严格小于

\[
\frac{6581}{960}.
\]

因此 \(S\ge4\) 时

\[
n_3
<
\frac{31}{4}S+\frac{6581}{960}
<8S+6.
\]

对剩余的 \(S=2,3\)，同一组夹逼先给出

\[
m_3
<
\frac{15}{4}S+\frac{163}{64}.
\]

再用 \(d_3\le5S\) 与 \(n_3=m_3+d_3\)，

\[
n_3
<
\frac{35}{4}S+\frac{163}{64}
<8S+6.
\]

所以 \(t_2=1\) 也满足同一个严格界。

若二进唯一最大来自前缀，或三个分母全奇，第 27.8 节的计算保留精确常数后为

\[
n_3
<
\frac{2(8+a)}{2+a}S
+
\frac{2(7+2a)}{2+a}.
\]

由 \(a>3/10\) 可粗化为

\[
n_3
<
\frac{29}{4}S+\frac{20}{3}
<8S+6
\]

（事实上这里只需 \(a>2/7\) 与 \(a>1/4\)）。因此入口以上的 resonance 已在所有二进位置统一满足 \(n_3<8S+6\)。

### 新的 DD 全局相对界与顶层核

低于五进入口的 dominant 候选满足

\[
n_3<(5+2\log_5 10)S+\log_5 10<8S+6,
\]

这里用了 \(\log_5 10<3/2\)，等价于 \(10^2<5^3\)。非
\(d_3\)-dominant 扇区仍有 \(n_3\le7S+4<8S+6\)。综上，所有 DD 候选满足

\[
\boxed{
n_3<8S_{12}+6.
}
\]

由于 \(n_3,S_{12}\) 为整数，这一阶段的 DD 全局相对界是

\[
\boxed{
n_3\le8S_{12}+5.
}
\tag{DD-global-relative-8-plus-5}
\]

加权形式还留下一个比总界更细的终端信息。在唯一仍可随 \(S\)
无界的 \(b_3\)-二进主导、\(t_2\ge2\) 子锥中，如果达到最高整数层

\[
n_3=8S+5,
\]

则 \((\mathrm{DD\text{-}resonance\text{-}weighted})\) 强迫

\[
\Xi<10^{1+a}=20.
\]

结合 \(\mathscr A_2-\mathscr A_5\equiv1\pmod3\)，只有

\[
\boxed{
\Xi\in\{2,16\}.
}
\]

确实，若 \(\mathscr A_5=0\)，则
\(2^{\mathscr A_2}<20\) 与模 \(3\) 条件只允许
\(\mathscr A_2=1,4\)；若 \(\mathscr A_5=1\)，则
\(5\cdot2^{\mathscr A_2}<20\) 只允许
\(\mathscr A_2=0,1\)，均不满足模 \(3\) 条件；而
\(\mathscr A_5\ge2\) 时 \(\Xi\ge25\)。

特别地，最高整数层必有

\[
q_5=g_5=n_5=0,
\qquad
3\mid m_3.
\]

若写 \(m_3=3h\)，则五进正规形进一步固定为

\[
\boxed{
k_5=2h,
\qquad
B_5=h,
\qquad
\mathscr A_2\in\{1,4\}.
}
\tag{DD-top-resonance-kernel}
\]

这只是最高整数层的严格正规形，不排除更低层，也不构成 DD 闭环。

### 机械核验（非证明器）

本节的符号消元、粗有理常数和 \(\Xi<20\) 的有限 residue 列表可由

```bash
uv run python scripts/check_dd_2711.py
```

复核。脚本不验证正文假设，也不枚举 DD 候选。

## 27.12 排除最高整数层 \(n_3=8S+5\)

**状态：`已严格完成`。** 本节排除第 27.11 节相对界的最高整数层，
但所得新界仍随 \(S\) 线性增长，因此不关闭 DD。依赖第 21、27.7、
27.8、27.11 节。

反设存在

\[
n_3=8S+5.
\tag{DD-top-layer-assumption}
\]

由 \(d_3\le5S\) 与 \(n_3=m_3+d_3\)，首先有统一下界

\[
\boxed{
m_3\ge3S+5.
}
\tag{DD-top-layer-m-lower}
\]

下面按第 27.8 节的二进位置逐一排除。

### \(b_3\) 独占二进最大且 \(t_2\ge2\)

第 27.11 节已经证明，在该子锥的最高整数层中

\[
\Xi\in\{2,16\},
\qquad
3\mid m_3.
\]

而 \((\mathrm{DD\text{-}resonance\text{-}m\text{-}weighted})\) 可写成

\[
m_3
<
3S+\frac32+\frac a2-\frac12\log_{10}\Xi.
\]

由于 \(\Xi\ge2=10^a\)，

\[
m_3<3S+\frac32.
\]

结合 \(3\mid m_3\) 与 \(S\in\mathbf Z\)，得到

\[
m_3\le3S,
\]

这与 \((\mathrm{DD\text{-}top\text{-}layer\text{-}m\text{-}lower})\) 矛盾。

### 前缀独占二进最大或三个分母全奇

第 27.11 节保留的精确上界为

\[
n_3
<
\frac{2(8+a)}{2+a}S
+
\frac{2(7+2a)}{2+a}
<
\frac{29}{4}S+\frac{20}{3}.
\]

当 \(S\ge3\) 时，右端严格小于 \(8S+5\)。若 \(S=2\)，相应的
\(m_3\) 界为

\[
m_3
<
\frac{6S+3}{2+a}
<
\frac{150}{23}
<7,
\]

这里用了 \(a>3/10\)。但最高层下界给出 \(m_3\ge11\)，仍然矛盾。

### \(b_3\) 独占二进最大且 \(t_2=1\)

这一支需要保留第 27.8 节的小因子比例，而不能只看已经粗化后的
线性界。令

\[
s=s_1+s_2,
\qquad
D_s=|s_1-s_2|.
\]

在粗化 \(s\le2\)、\(D_s\le2S-2\) 之前，第 27.8 节的同一计算实际给出

\[
F_-
<
2\cdot10^{2S+s+D_s+2m_3-n_3+4}.
\]

另一方面，\(t_2=1\) 的乘法高度下界为

\[
\log_{10}F_-
>
\left(2a+\frac43b\right)m_3
-2S-1-a.
\]

代入 \(n_3=8S+5\) 并比较上下界，得到必要条件

\[
\boxed{
s+D_s
>
4S-2a-\frac{2b}{3}m_3.
}
\tag{DD-top-layer-surplus}
\]

又因为

\[
s+D_s=2\max(s_1,s_2)\le2S,
\]

所以

\[
m_3>\frac{3(S-a)}{b}.
\]

与第 27.11 节的 \(m_3\) 上界比较，并使用

\[
\frac3{10}<a<\frac13,
\qquad
c<\frac{21}{20},
\]

先得到

\[
\frac{30}{7}\left(S-\frac13\right)
<m_3
<
\frac{15}{4}S+\frac{163}{64}.
\]

两端相容要求

\[
S<\frac{1781}{240}<8.
\]

而 \(S=7\) 时左端给出 \(m_3>200/7\)，右端给出
\(m_3<1843/64<29\)，也不可能。因此

\[
\boxed{S\le6.}
\]

为了精确列出剩余 \(m_3\)，使用稍紧但仍由整数幂直接验证的夹逼

\[
\frac{301}{1000}<a<\frac{302}{1000},
\qquad
c<\frac{521}{500}.
\]

它们来自

\[
10^{301}<2^{1000}<10^{302},
\qquad
11^{500}<10^{521}.
\]

于是

\[
m_3
<
\frac{1000}{267}S+\frac{441}{178}.
\]

与 \(m_3\ge3S+5\) 合并后，\(S=4,5,6\) 只可能有

\[
\begin{array}{c|c}
S&m_3\\
\hline
4&17\\
5&20,21\\
6&23,24
\end{array}
\]

（\(S=2,3\) 的上下界已经直接冲突）。对

\[
(S,m_3)=(5,20),(6,23),(6,24),
\]

由 \(a>3/10\) 可逐一验证

\[
3S
>
m_3+a(3-m_3),
\]

这等价于 \((\mathrm{DD\text{-}top\text{-}layer\text{-}surplus})\) 的右端严格大于 \(2S\)，矛盾。故只剩

\[
\boxed{
(S,m_3)=(4,17)\quad\text{或}\quad(5,21).
}
\tag{DD-top-layer-two-sizes}
\]

在这两个情形中，\((\mathrm{DD\text{-}top\text{-}layer\text{-}surplus})\)
分别强迫

\[
s+D_s
>
\frac{14}{3}+\frac{28a}{3}
>
\frac{112}{15}
>7
\qquad(S,m_3)=(4,17),
\]

以及

\[
s+D_s
>
6+12a
>
\frac{48}{5}
>9
\qquad(S,m_3)=(5,21).
\]

因为 \(s+D_s=2\max(s_1,s_2)\) 是偶整数且不超过 \(2S\)，分别只能有

\[
s+D_s=8
\quad\text{或}\quad
s+D_s=10.
\]

也就是说总有 \(\max(s_1,s_2)=S\)。再结合
\(s_1+s_2\le2\)、\(m_1+m_2=S\) 与两个 numerator block 都非空，
除交换 \(1,2\) 外只能是

\[
\boxed{
(m_{\rm long\ surplus},n_{\rm long\ surplus})=(1,S+1),
\qquad
(m_{\rm other},n_{\rm other})=(S-1,1).
}
\tag{DD-top-layer-digit-shape}
\]

最后把两处 resonance 的高度预算代入这个极端位数形状。记

\[
\mathscr A_5=2q_5+g_5+n_5.
\]

由 \(t_2=1\)、二进 resonance、五进 resonance 以及
\(\kappa<10^{2S+1}\)、\(\kappa+2G<11\cdot10^{2S}\)，消去
\(v_2(G)\) 得到

\[
\frac{2(1+2a)}{3}m_3
+2a\mathfrak q+a\mathfrak n
+\frac b3\mathscr A_5
<
4S+1+c+2a.
\tag{DD-top-layer-combined-height}
\]

若 \((S,m_3)=(4,17)\)，模 \(3\) 条件给出
\(\mathscr A_5\equiv2\pmod3\)。在扣除最小项 \(2b/3\) 后，
剩余预算为

\[
5+c-20a<a,
\]

其中最后一步可由刚才的千分位夹逼严格验证。因此

\[
\mathfrak q=\mathfrak n=0,
\qquad
\mathscr A_5=2.
\]

五进 resonance 给出 \(k_5=12\)。再令
\(\mathfrak g=v_2(G)\)。由

\[
2^{\mathfrak g+1}5^{12}<10^9,
\qquad
2^{31-\mathfrak g}<11\cdot10^8,
\]

只能有 \(\mathfrak g=1\)。于是

\[
\kappa
\ge2^2 5^{12}
=976562500.
\]

但位数形状给出

\[
G\le9\cdot999=8991,
\qquad
Q<10^4,
\]

所以

\[
\kappa\le10QG<899100000,
\]

矛盾。

若 \((S,m_3)=(5,21)\)，模 \(3\) 条件给出
\(\mathscr A_5\equiv0\pmod3\)，而剩余预算

\[
7+c-26a<a
\]

强迫

\[
\mathfrak q=\mathfrak n=\mathscr A_5=0.
\]

于是 \(k_5=14\)。同样由

\[
2^{\mathfrak g+1}5^{14}<10^{11},
\qquad
2^{39-\mathfrak g}<11\cdot10^{10}
\]

只能有 \(\mathfrak g=3\)。所以

\[
\kappa
\ge2^4 5^{14}
=97656250000.
\]

然而此时

\[
G\le9\cdot9999=89991,
\qquad
Q<10^5,
\]

从而

\[
\kappa\le10QG<89991000000,
\]

再次矛盾。至此 \(t_2=1\) 的最高整数层也被排除。

三个二进位置已经穷尽，因此

\[
\boxed{
n_3=8S_{12}+5
\quad\text{在 DD 中为空}.
}
\tag{DD-top-layer-empty}
\]

结合第 27.11 节，当前最强的 DD 全局相对界为

\[
\boxed{
n_3\le8S_{12}+4.
}
\tag{DD-global-relative-8-plus-4}
\]

该结论仍不是绝对高度界。

### 机械核验（非证明器）

本节的对数夹逼、候选 \((S,m_3)\)、剩余赋值预算和两个最终整数高度比较可由

```bash
uv run python scripts/check_dd_2712.py
```

复核。脚本不枚举原问题候选，也不替代上述无界参数推导。

## 27.13 无界 \(t_2\ge2\) 子锥降层与 \(8S+4\) 层排除

**状态：`已严格完成`；最后十个尺寸由 `有限证书` 排除。** 本节继续处理第
27.12 节留下的新最高层。入口以上的 \(t_2\ge2\) resonance 子锥先
整体降到 \(n_3\le8S\)；其余位置把 \(n_3=8S+4\) 压成十个
\(t_2=1\) 尺寸，最后由精确余因子区间证书全部排除。依赖第
21、27.7、27.8、27.10–27.12 节。所得界仍随 \(S\) 线性增长，不
关闭 DD。

### \(t_2\ge2\) resonance 子锥的统一降层

仍处在五进入口以上、\(b_3\) 独占二进最大且 \(t_2\ge2\) 的
resonance 子锥。第 27.11 节的加权 \(m_3\) 界为

\[
m_3
<
3S+\frac32+\frac a2-\frac12\log_{10}\Xi,
\qquad
\Xi\ge2=10^a.
\]

因此

\[
m_3<3S+\frac32,
\]

而 \(m_3\) 为整数，所以 \(m_3\le3S+1\)。再用第 21 节的
\(d_3\le5S\)，先得到

\[
n_3=m_3+d_3\le8S+1.
\]

若等号成立，则必有

\[
m_3=3S+1,
\qquad
d_3=5S.
\]

把 \(m_3=3S+1\) 代回未粗化的加权 \(m_3\) 界，得到

\[
\log_{10}\Xi<1+a,
\qquad
\Xi<20.
\]

另一方面，

\[
\mathscr A_2-\mathscr A_5\equiv1\pmod3,
\qquad
\Xi=2^{\mathscr A_2}5^{\mathscr A_5}.
\]

若 \(\mathscr A_5\ge2\)，则 \(\Xi\ge25\)；若
\(\mathscr A_5=1\)，模 \(3\) 条件强迫
\(\mathscr A_2\equiv2\pmod3\)，故 \(\Xi\ge20\)。所以严格小于
\(20\) 时只能有

\[
\Xi\in\{2,16\},
\qquad
\mathscr A_5=0.
\]

五进 resonance 正规形随即化为

\[
3k_5=2m_3,
\]

从而 \(3\mid m_3\)。这与 \(m_3=3S+1\) 矛盾。故整个无界子锥满足

\[
\boxed{
t_2\ge2, \text{入口以上 resonance}
\Longrightarrow
n_3\le8S.
}
\tag{DD-t2-ge2-eight-S}
\]

这比全局相对界强四个整数层，但只适用于这里写明的二进位置。

### 新最高层只可能来自 \(t_2=1\)

现在反设

\[
n_3=8S+4.
\tag{DD-eight-S-plus-four-assumption}
\]

非 \(d_3\)-dominant 扇区满足 \(n_3\le7S+4\)，故不可能达到该层。
在 dominant 扇区中，由

\[
\log_5 10<\frac32
\]

可知五进入口严格小于 \(8S+\frac32\)，所以该层必在入口以上；第
27.10 节于是把五进位置强制为 resonance。

刚才的 \((\mathrm{DD\text{-}t2\text{-}ge2\text{-}eight\text{-}S})\)
已经排除 \(t_2\ge2\)。若二进唯一最大来自前缀，或三个分母全奇，
第 27.11 节给出

\[
n_3
<
\frac{29}{4}S+\frac{20}{3}.
\]

当 \(S\ge4\) 时右端小于 \(8S+4\)。对 \(S=2,3\)，相应的
\(m_3\) 上界和 \(a>3/10\) 给出

\[
m_3
<
\frac{6S+3}{2+a}
<
\begin{cases}
150/23,&S=2,\\
210/23,&S=3,
\end{cases}
\]

而 \(d_3\le5S\) 要求 \(m_3\ge3S+4\)，仍然矛盾。因此最高层只可能
来自

\[
\boxed{
b_3\text{ 独占二进最大},
\qquad
t_2=1.
}
\tag{DD-eight-S-plus-four-t2-one}
\]

### \(t_2=1\) 的有理尺寸压缩

沿用

\[
s=s_1+s_2,
\qquad
D_s=|s_1-s_2|.
\]

把 \(n_3=8S+4\) 代入第 27.12 节使用的未粗化小因子上界，并与同一
乘法高度下界比较，得到必要条件

\[
\boxed{
s+D_s
>
4S-1-2a-\frac{2(1-a)}{3}m_3.
}
\tag{DD-eight-S-plus-four-surplus}
\]

因为 \(s+D_s\le2S\)，上式推出

\[
m_3
>
\frac{3(2S-1-2a)}{2(1-a)}.
\]

使用已经验证的整数幂夹逼

\[
\frac{301}{1000}<a<\frac{302}{1000},
\qquad
c=\log_{10}11<\frac{521}{500},
\]

并保留第 27.11 节的精确 \(m_3\) 上界，可严格粗化为

\[
\boxed{
\frac{1000S-801}{233}
<m_3<
\frac{1000S+661}{267}.
}
\tag{DD-eight-S-plus-four-m-window}
\]

两端相容要求

\[
S<\frac{541}{50}<11.
\]

再与 \(m_3\ge3S+4\) 合并，逐个检查整数 \(2\le S\le10\)，得到十三个
必要尺寸

\[
\begin{aligned}
\mathcal K_0=\{&
(3,13),
(4,16),(4,17),
(5,19),(5,20),(5,21),\\
&(6,23),(6,24),
(7,27),(7,28),
(8,31),(8,32),
(9,36)
\}.
\end{aligned}
\tag{DD-eight-S-plus-four-initial-kernel}
\]

这一步是有限的整数区间核对，不是对原始有理数候选的枚举。

### 所有必要尺寸都强迫同一个位数形状

对 \(\mathcal K_0\) 中每一对都有

\[
30S+6>7m_3.
\]

由于 \(a>3/10\)，这正好给出

\[
4S-1-2a-\frac{2(1-a)}3m_3>2S-2.
\]

而 \(s+D_s=2\max(s_1,s_2)\) 是不超过 \(2S\) 的偶整数，故

\[
s+D_s=2S,
\qquad
\max(s_1,s_2)=S.
\]

再由 \(s_1+s_2\le2\)、\(m_1+m_2=S\) 和所有块非空，除交换
\(1,2\) 外只能有

\[
\boxed{
(m_{\rm long\ surplus},n_{\rm long\ surplus})=(1,S+1),
\qquad
(m_{\rm other},n_{\rm other})=(S-1,1).
}
\tag{DD-eight-S-plus-four-digit-shape}
\]

第 27.12 节对 \((S,m_3)=(4,17),(5,21)\) 的最终整数高度矛盾只使用
\(t_2=1\)、两处 resonance、该位数形状和对应的 \((S,m_3)\)，不使用
\(n_3=8S+5\) 本身。因此这两个尺寸在当前层同样被排除。

还可直接排除 \((S,m_3)=(8,32)\)。五进模 \(3\) 条件给出
\(\mathscr A_5\equiv2\pmod3\)。把最小值 \(\mathscr A_5=2\) 从第
27.12 节的 combined-height 界扣除，剩余预算为

\[
11+c-40a<a,
\]

其中

\[
11+c-40a
<11+\frac{521}{500}-40\frac{301}{1000}
=\frac1{500}<a.
\]

故若该尺寸尚未立即矛盾，就必须有

\[
\mathfrak q=\mathfrak n=0,
\qquad
\mathscr A_5=2,
\qquad
k_5=22.
\]

这里额外的 \(\mathfrak n\) 至少耗费 \(a\)，额外的
\(\mathfrak q\) 至少耗费 \(2a\)，而
\(\mathscr A_5\) 在同一模 \(3\) 类中的下一值至少增加 \(3\)，耗费
\(b=1-a>a\)；最后一个严格不等式来自 \(a<1/3\)。

令 \(\mathfrak g=v_2(G)\)。二进 resonance 给出

\[
\mathfrak f=61-\mathfrak g.
\]

由 \(\kappa<10^{17}\) 及

\[
2^6 5^{22}>10^{17}
\]

可知 \(\mathfrak g\le4\)。于是 \(\mathfrak f\ge57\)，但

\[
2^{57}>11\cdot10^{16}>\kappa+2G
\]

又与 \(\mathfrak f=v_2(\kappa+2G)\) 矛盾。

所以当前最高层若存在，只能具有

\[
\boxed{
\begin{aligned}
(S,m_3)\in\mathcal K=\{&
(3,13),(4,16),(5,19),(5,20),\\
&(6,23),(6,24),(7,27),(7,28),\\
&(8,31),(9,36)
\},
\end{aligned}
}
\tag{DD-eight-S-plus-four-residual-kernel}
\]

并同时满足
\((\mathrm{DD\text{-}eight\text{-}S\text{-}plus\text{-}four\text{-}digit\text{-}shape})\)。

### 十尺寸核的余因子区间证书

下面只枚举由正文严格推出的有界赋值数据，不枚举原始分子、分母。
在统一极端位数形状中，无论长 surplus 位于第一个还是第二个块，都有

\[
G\le G_{\max}:=9(10^{S-1}-1),
\qquad
\mathcal N_{12}<2\cdot10^{4S}.
\]

又由 \(Q,G<10^S\)、\(S\ge2\)、\(10^2<5^3\)、五进 resonance
及 \(m_3\ge3S+4\)，所有待查赋值都落在显式有限盒

\[
0\le\mathfrak q,\mathfrak g<4S,
\qquad
0\le\mathfrak n<14S,
\qquad
0\le\mathscr A_5\le3S-5.
\tag{DD-eight-S-plus-four-valuation-box}
\]

这里 \(2^{14S}>2\cdot10^{4S}\) 对 \(S\ge2\) 成立：先用
\(2^{28}>2\cdot10^8\)，再逐次乘以 \(2^{14}>10^4\)。最后一个界
来自

\[
5^{k_5}\le\kappa<10^{2S+1}
\Longrightarrow
k_5\le3S+1,
\qquad
\mathscr A_5=3k_5-2m_3.
\]

对盒内每一点，必须同时满足两条 resonance 整式

\[
3k_5=2m_3+\mathscr A_5,
\qquad
\mathfrak f
=2m_3+2\mathfrak q+\mathfrak n-\mathfrak g-3,
\]

以及两个单因子高度界

\[
2^{\mathfrak g+1}5^{k_5}<10^{2S+1},
\qquad
2^{\mathfrak f}<11\cdot10^{2S}.
\]

第 27.12 节的 combined-height 不等式乘以 \(3\) 后取十的幂，恰好
等价于纯整数条件

\[
\boxed{
10^{2m_3}
2^{4m_3+6\mathfrak q+3\mathfrak n}
5^{\mathscr A_5}
<
2^6 11^3 10^{12S+3}.
}
\tag{DD-eight-S-plus-four-combined-integer}
\]

对 \(\mathcal K\) 中依次列出的十个尺寸，这些必要条件分别留下

\[
\boxed{
3,\ 27,\ 72,\ 7,\ 42,\ 14,\ 42,\ 1,\ 16,\ 1
}
\tag{DD-eight-S-plus-four-valuation-counts}
\]

个
\((\mathfrak q,\mathfrak n,\mathscr A_5,\mathfrak g,\mathfrak f,k_5)\)
元组。

现在利用此前高度估计尚未使用的精确余因子。因为

\[
v_2(\kappa)=\mathfrak g+1,
\qquad
v_5(\kappa)=k_5,
\]

可唯一写成

\[
\kappa
=
2^{\mathfrak g+1}5^{k_5}u,
\qquad
\gcd(u,10)=1.
\]

由 \(\kappa\le10QG\)、\(Q\le10^S-1\) 与 \(G\le G_{\max}\)，

\[
1\le u\le
\left\lfloor
\frac{10(10^S-1)G_{\max}}
{2^{\mathfrak g+1}5^{k_5}}
\right\rfloor.
\tag{DD-eight-S-plus-four-u-range}
\]

再写

\[
G=2^{\mathfrak g}G_*,
\qquad
G_*\ \text{为奇数},
\qquad
1\le G_*\le
\left\lfloor\frac{G_{\max}}{2^{\mathfrak g}}\right\rfloor.
\]

于是

\[
\kappa+2G
=
2^{\mathfrak g+1}
\left(5^{k_5}u+G_*\right).
\]

令

\[
h=\mathfrak f-\mathfrak g-1.
\]

精确条件 \(v_2(\kappa+2G)=\mathfrak f\) 要求区间

\[
\boxed{
\left[
5^{k_5}u+1,\
5^{k_5}u+
\left\lfloor\frac{G_{\max}}{2^{\mathfrak g}}\right\rfloor
\right]
}
\tag{DD-eight-S-plus-four-cofactor-interval}
\]

包含一个 \(2^h z\)，其中 \(z\) 为正奇数。对上述全部赋值元组及
\((\mathrm{DD\text{-}eight\text{-}S\text{-}plus\text{-}four\text{-}u\text{-}range})\)
中的每个 \(u\)，逐项计算

\[
z_0
=
\min\left\{
z\ge
\left\lceil\frac{5^{k_5}u+1}{2^h}\right\rceil:
z\text{ 为奇数}
\right\}
\]

后，均有

\[
2^h z_0
>
5^{k_5}u+
\left\lfloor\frac{G_{\max}}{2^{\mathfrak g}}\right\rfloor.
\]

因此区间证书无幸存者，十个尺寸全部矛盾。结合前面的二进位置穷尽，

\[
\boxed{
n_3=8S_{12}+4
\quad\text{在 DD 中为空}.
}
\tag{DD-eight-S-plus-four-empty}
\]

由第 27.12 节的旧全局界和整数性，当前最强的 DD 全局相对界更新为

\[
\boxed{
n_3\le8S_{12}+3.
}
\tag{DD-global-relative-8-plus-3}
\]

这仍不是 prefix-uniform 绝对高度界，也不排除更低层。

### 机械核验（非证明器）

本节的对数夹逼、\(\Xi<20\) residue、十三个初始尺寸、统一极端位数
形状、\((8,32)\) 的直接赋值矛盾，以及十个残余尺寸的精确赋值与
余因子区间证书可由

```bash
uv run python scripts/check_dd_2713.py
```

复核。脚本中的最终循环是一个只覆盖上述显式有限盒和余因子区间的
有限证书；它不枚举原始分子、分母，也不覆盖 \(n_3\le8S+3\) 的更低
无界区域。

## 27.14 排除 \(8S+3\) 与 \(8S+2\) 两层

**状态：`已严格完成`；两个有界赋值核由 `有限证书` 排除。**
本节把第 27.13 节的余因子区间方法从极端位数形状推广到一般
\(G<10^S\)，连续排除当前最高的两个整数层。依赖第 21、27.7、
27.8、27.10–27.13 节。结论仍是随 \(S\) 增长的相对界，不关闭 DD。

### 两层都只能进入 \(t_2=1\)

统一令

\[
n_3=8S+C,
\qquad
C\in\{3,2\}.
\tag{DD-next-two-layer-assumption}
\]

非 \(d_3\)-dominant 扇区满足 \(n_3\le7S+4\)。对 \(C=3,S\ge2\)
及 \(C=2,S\ge3\)，都有 \(8S+C>7S+4\)，故这些情形自动进入
\(d_3\)-dominant 扇区。唯一的等号边界是 \(C=2,S=2\)。此时
\(m_1=m_2=1\)，所以 \(s_1,s_2\ge0\)；另一方面统一
denominator-tail cone 给出 \(m_3\le15\)，从而
\(d_3=18-m_3\ge3\)。若 \(s_1\) 或 \(s_2\) 最大，surplus simplex
分别要求 \(s_2+d_3\le2\) 或 \(s_1+d_3\le2\)，均矛盾。因此这个
等号边界也必须是 \(d_3\)-dominant。

又由 \(\log_5 10<3/2\)，五进入口严格小于
\(8S+3/2\)，故这两个层都在入口以上；第 27.10 节将其五进位置强制
为 resonance。第 27.13 节的
\((\mathrm{DD\text{-}t2\text{-}ge2\text{-}eight\text{-}S})\)
立即排除 \(t_2\ge2\)。

若二进唯一最大来自前缀，或三个分母全奇，第 27.11 节给出

\[
n_3<\frac{29}{4}S+\frac{20}{3}.
\]

对 \(C=3\)，当 \(S\ge5\) 时右端小于 \(8S+3\)；对
\(S=2,3,4\)，由

\[
m_3<\frac{6S+3}{2+a}
<\frac{10(6S+3)}{23}
<3S+3
\]

和 \(m_3\ge n_3-5S=3S+3\) 矛盾。对 \(C=2\)，同样的比较分别
在 \(S\ge7\) 及 \(2\le S\le6\) 生效，并与 \(m_3\ge3S+2\)
矛盾。所以两个层若存在，都只能满足

\[
\boxed{
b_3\text{ 独占二进最大},
\qquad
t_2=1.
}
\tag{DD-next-two-t2-one}
\]

### 两个显式尺寸核

把 \(n_3=8S+C\) 代入未粗化 small-factor 上界，与第 27.8 节的
\(t_2=1\) 乘法高度下界比较，得到

\[
\boxed{
s+D_s
>
4S+C-5-2a-\frac{2(1-a)}3m_3.
}
\tag{DD-next-two-surplus}
\]

利用 \(s+D_s\le2S\)，

\[
m_3>
\frac{3(2S+C-5-2a)}{2(1-a)}.
\tag{DD-next-two-m-lower}
\]

函数

\[
a\longmapsto
\frac{3(2S+C-5-2a)}{2(1-a)}
\]

的导数符号由 \(2S+C-7\) 决定。因此对 \(C=3,S\ge2\) 以及
\(C=2,S\ge3\)，使用 \(a>301/1000\)，并与第 27.11 节的
精确 \(m_3\) 上界合并，分别得到

\[
\frac{1000S-1301}{233}
<m_3<
\frac{1000S+661}{267}
\qquad(C=3),
\tag{DD-eight-S-plus-three-m-window}
\]

\[
\frac{1000S-1801}{233}
<m_3<
\frac{1000S+661}{267}
\qquad(C=2,\ S\ge3).
\tag{DD-eight-S-plus-two-m-window}
\]

两端相容分别要求

\[
S<\frac{25069}{1700}<15,
\qquad
S<\frac{7936}{425}<19.
\]

在 \(C=2,S=2\) 时无需使用下界：\(m_3\ge8\) 与同一上界只留下
\(m_3=8,9\)。逐个取整数后，两个尺寸核为

\[
\begin{array}{c|l}
C=3&S:m_3\\
\hline
&2:9\\
&3:12,13\\
&4:15,16,17\\
&5:18,19,20,21\\
&6:21,22,23,24\\
&7:25,26,27,28\\
&8:29,30,31,32\\
&9:34,35,36\\
&10:38,39\\
&11:42,43\\
&12:46,47\\
&13:51
\end{array}
\tag{DD-eight-S-plus-three-size-kernel}
\]

和

\[
\begin{array}{c|l}
C=2&S:m_3\\
\hline
&2:8,9\\
&3:11,12,13\\
&4:14,15,16,17\\
&5:17,18,19,20,21\\
&6:20,21,22,23,24\\
&7:23,24,25,26,27,28\\
&8:27,28,29,30,31,32\\
&9:31,32,33,34,35,36\\
&10:36,37,38,39\\
&11:40,41,42,43\\
&12:44,45,46,47\\
&13:49,50,51\\
&14:53,54\\
&15:57,58\\
&16:61,62\\
&17:66
\end{array}.
\tag{DD-eight-S-plus-two-size-kernel}
\]

前者有 \(32\) 个尺寸，后者有 \(59\) 个尺寸。这里已经由符号不等式
给出 \(S\) 的上界，所以接下来的有限检查只证明这两个明确层，不是
对无界前缀的替代。

### 不依赖极端位数形状的一般余因子证书

第 27.13 节使用了 \(G\) 的极端位数形状上界。当前不再需要该形状；
只使用

\[
G\le G_{\max}:=10^S-1.
\]

在 \(d_3\)-dominant 扇区，
\(s_1+s_2\le2\) 且 \(D_s\le2S-2\)，所以
\(\max(s_1,s_2)\le S\)。因而

\[
a_1b_2<10^{S+s_1}\le10^{2S},
\qquad
a_2b_1<10^{S+s_2}\le10^{2S},
\]

并仍有

\[
\mathcal N_{12}<2\cdot10^{4S}.
\]

于是第 27.13 节的有限赋值盒及全部纯整数条件原样适用，只需把
\(\mathscr A_5\) 的统一上界放宽为

\[
0\le\mathscr A_5\le3S-1;
\]

这是由 \(m_3\ge3S+2\)、\(k_5\le3S+1\) 和
\(\mathscr A_5=3k_5-2m_3\) 得到的。具体说，仍检查

\[
0\le\mathfrak q,\mathfrak g<4S,
\qquad
0\le\mathfrak n<14S,
\]

两条 resonance 整式、两个单因子高度界，以及
\((\mathrm{DD\text{-}eight\text{-}S\text{-}plus\text{-}four\text{-}combined\text{-}integer})\)。
在 \(C=3\) 的 \(32\) 个尺寸中共留下 \(2677\) 个赋值元组；在
\(C=2\) 的 \(59\) 个尺寸中共留下 \(14095\) 个赋值元组。

对每个元组仍写

\[
\kappa=2^{\mathfrak g+1}5^{k_5}u,
\qquad
\gcd(u,10)=1.
\]

现在使用更宽但对两种前缀排列都成立的范围

\[
1\le u\le
\left\lfloor
\frac{10(10^S-1)^2}
{2^{\mathfrak g+1}5^{k_5}}
\right\rfloor,
\]

并检查一般区间

\[
\left[
5^{k_5}u+1,\
5^{k_5}u+
\left\lfloor\frac{10^S-1}{2^{\mathfrak g}}\right\rfloor
\right].
\tag{DD-next-two-general-cofactor-interval}
\]

精确等式 \(v_2(\kappa+2G)=\mathfrak f\) 要求该区间包含
\(2^h\) 的一个奇数倍，其中 \(h=\mathfrak f-\mathfrak g-1\)。
对总计

\[
2677+14095=16772
\]

个赋值元组及其范围内所有 \(\gcd(u,10)=1\) 的余因子，逐项计算最小
候选奇数倍后，两个层都没有幸存者。因此

\[
\boxed{
n_3=8S_{12}+3
\quad\text{与}\quad
n_3=8S_{12}+2
\quad\text{在 DD 中均为空}.
}
\tag{DD-next-two-layers-empty}
\]

结合第 27.13 节，当前最强的 DD 全局相对界为

\[
\boxed{
n_3\le8S_{12}+1.
}
\tag{DD-global-relative-8-plus-1}
\]

这仍不是绝对高度界。

### 机械核验（非证明器）

上述两个有理尺寸核、16772 个精确赋值元组和一般余因子区间证书可由

```bash
uv run python scripts/check_dd_2714.py
```

复核。脚本只使用整数算术验证正文给出的有限盒；它不枚举原始 DD
分子、分母，也不覆盖 \(n_3\le8S+1\) 的更低无界区域。

## 27.15 \(8S+1\) 层的 \(S\ge4\) 全排除

**状态：\(S\ge4\) 为 `已严格完成`；\(S=2,3\) 为
`待证`。** 本节继续处理第 27.14 节留下的最高层，但不把
入口边界下方的两个小 \(S\) 静默并入 resonance 证明。结论是

\[
n_3=8S+1
\Longrightarrow
S\in\{2,3\}.
\tag{DD-eight-S-plus-one-small-S-only}
\]

这还不能把全局相对界降到 \(8S\)。依赖第 19、21、27.7、
27.10–27.14 节。

### \(S\ge4\) 时仍被强制到 \(t_2=1\)

反设

\[
n_3=8S+1,
\qquad
S\ge4.
\]

此时 \(8S+1>7S+4\)，故候选必在 \(d_3\)-dominant 扇区。令
\(L_5=\log_5 10\)。在 \(S=4\) 时，层高超过五进入口等价于

\[
13>9L_5,
\]

而这来自 \(10^9<5^{13}\)。又因 \(L_5<3/2\)，差值

\[
(3-2L_5)S+1-L_5
\]

随 \(S\) 严格增加，所以全部 \(S\ge4\) 都在五进入口以上，只剩五进
resonance。

\(t_2\ge2\) 已由
\((\mathrm{DD\text{-}t2\text{-}ge2\text{-}eight\text{-}S})\)
排除。对前缀二进主导或三个分母全奇的位置，当 \(S\ge8\) 时

\[
\frac{29}{4}S+\frac{20}{3}<8S+1;
\]

当 \(4\le S\le7\) 时

\[
m_3
<
\frac{6S+3}{2+a}
<
\frac{10(6S+3)}{23}
<
3S+1
\]

又与 \(m_3\ge n_3-5S=3S+1\) 矛盾。因此仍只需考虑

\[
b_3\text{ 独占二进最大},
\qquad
t_2=1.
\]

### 86 个尺寸与 48808 个赋值元组

第 27.14 节的一般 surplus 公式在 \(C=1\) 时给出

\[
s+D_s
>
4S-4-2a-\frac{2(1-a)}3m_3.
\]

对 \(S\ge4\)，相应下界关于 \(a\) 递增。使用
\(a>301/1000\) 和同一个 \(m_3\) 上界，

\[
\boxed{
\frac{1000S-2301}{233}
<m_3<
\frac{1000S+661}{267}.
}
\tag{DD-eight-S-plus-one-m-window}
\]

两端相容要求

\[
S<\frac{38419}{1700}<23.
\]

再与 \(m_3\ge3S+1\) 合并，得到

\[
\begin{array}{c|l}
S&m_3\\
\hline
4&13,14,15,16,17\\
5&16,17,18,19,20,21\\
6&19,20,21,22,23,24\\
7&22,23,24,25,26,27,28\\
8&25,26,27,28,29,30,31,32\\
9&29,30,31,32,33,34,35,36\\
10&34,35,36,37,38,39\\
11&38,39,40,41,42,43\\
12&42,43,44,45,46,47\\
13&46,47,48,49,50,51\\
14&51,52,53,54\\
15&55,56,57,58\\
16&59,60,61,62\\
17&64,65,66\\
18&68,69\\
19&72,73\\
20&76,77\\
21&81
\end{array}.
\tag{DD-eight-S-plus-one-size-kernel}
\]

这是 \(86\) 个尺寸。此层由 \(m_3\ge3S+1\) 得到的统一五进范围是
\(0\le\mathscr A_5\le3S+1\)；其余仍使用第 27.14 节的一般赋值盒、
combined-height 整数式和 \(G_{\max}=10^S-1\) 余因子区间。逐项代入
共得到 \(48808\) 个允许赋值元组；其中只有一个元组—余因子对幸存：

\[
\boxed{
\begin{gathered}
(S,m_3)=(5,16),\\
(\mathfrak q,\mathfrak n,\mathscr A_5,
\mathfrak g,\mathfrak f,k_5)
=(0,0,1,8,21,11),\\
u=1.
\end{gathered}
}
\tag{DD-eight-S-plus-one-sole-cofactor}
\]

### 唯一余因子强制前缀，再由模 \(3\) 排除

此时

\[
h=\mathfrak f-\mathfrak g-1=12.
\]

一般余因子区间化为

\[
\left[
5^{11}+1,\
5^{11}+\left\lfloor\frac{99999}{2^8}\right\rfloor
\right].
\]

区间长度小于 \(2^{12}\)，其中唯一的 \(2^{12}\) 奇数倍是

\[
5^{11}+291=11921\cdot2^{12}.
\]

因此

\[
G_*=291,
\qquad
G=2^8G_*=74496.
\]

又因 \(\mathfrak q=0\)，\(Q\) 为奇数，故第二 denominator block
\(b_2\) 为奇数。对 \(m_1+m_2=5\) 的所有有序位数分解检查
\(b_1b_2=74496\)，唯一可能为

\[
\boxed{
(m_1,m_2)=(3,2),
\qquad
(b_1,b_2)=(768,97),
\qquad
Q=76897.
}
\tag{DD-eight-S-plus-one-denominators}
\]

在 \((S,m_3)=(5,16)\) 中，surplus 下界为

\[
\frac{16}{3}+\frac{26}{3}a
>
\frac{119}{15}
>7.
\]

所以 \(s+D_s=2\max(s_1,s_2)\ge8\)。结合
\(s_1+s_2\le2\)、\(D_s\le8\)、\(n_i=m_i+s_i\ge1\)，唯一有序
surplus 为

\[
\boxed{
(s_1,s_2)=(-2,4),
\qquad
(n_1,n_2)=(1,6).
}
\tag{DD-eight-S-plus-one-surpluses}
\]

最后

\[
\kappa=2^9 5^{11}=25000000000,
\]

且 \(\kappa=10^{m_3}QG/b_3\) 固定

\[
b_3=2291407564800000.
\]

回到第 20 节的 near-square 判别式

\[
Y^2
=
X^2
-\mathcal N_{12}10^{m_3}Q
\left(10^{m_3}Q+2b_3\right).
\]

模 \(3\) 考察。由于 \(3\mid G\)，有 \(X\equiv0\pmod3\)；
\(Q\equiv1\pmod3\)、\(3\mid b_3\) 且 \(10^{m_3}\equiv1\pmod3\)，
故尾部两因子的乘积模 \(3\) 为 \(1\)。另一方面

\[
\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2
\equiv a_1^2\pmod3.
\]

因 \(\gcd(a_1,b_1)=1\) 且 \(3\mid b_1\)，必有
\(a_1^2\equiv1\pmod3\)。所以

\[
Y^2\equiv-1\equiv2\pmod3,
\]

与模 \(3\) 平方剩余只有 \(0,1\) 矛盾。故

\[
\boxed{
n_3=8S_{12}+1,\ S\ge4
\quad\text{在 DD 中为空}.
}
\tag{DD-eight-S-plus-one-large-S-empty}
\]

本节把当前层缩到 \(S=2,3\)。这两个尺寸位于或跨过五进入口的另一侧，
不能引用本节的强制 resonance；本节本身因此只得到
\(n_3\le8S_{12}+1\)。第 27.16 节另行处理并关闭这两个边界。

### 机械核验（非证明器）

86 个尺寸、48808 个赋值元组、唯一余因子、\(G\) 的有序因子分解、
surplus 形状与最终模 \(3\) 矛盾可由

```bash
uv run python scripts/check_dd_2715.py
```

复核。脚本明确不覆盖 \(S=2,3\)，因而不是整个 \(8S+1\) 层的空性
证书。

## 27.16 关闭 \(8S+1\) 层的两个入口边界

**状态：分扇区与赋值归约为“已严格完成”；\(S=2,3\) 的最终空性为
“有限证书”。** 本节只关闭第 27.15 节明确留下的两个小尺寸，不把有限
枚举外推到更低的无界区域。结论是

\[
\boxed{
n_3=8S_{12}+1
\quad\text{在 DD 中为空},
}
\tag{DD-eight-S-plus-one-empty}
\]

从而把 DD 的全局相对界推进为

\[
\boxed{n_3\le8S_{12}.}
\tag{DD-global-relative-8-final}
\]

这仍不是 DD 空性。依赖第 19–21、27.2、27.7–27.8 与 27.15 节。

### 非 \(d_3\)-dominant 扇区实际满足 \(n_3\le7S+3\)

第 19 节的 \(7S+4\) 界还可利用“每个 numerator block 至少一位”
节省一层。若 \(s_1=\max(s_1,s_2,d_3)\)，surplus simplex 给出

\[
s_2+d_3\le2.
\]

而 \(n_2=m_2+s_2\ge1\)，故

\[
s_2\ge1-m_2,
\qquad
d_3\le1+m_2.
\]

结合 \(m_3\le6S+3\) 与 \(m_2\le S-1\)，得到

\[
n_3=m_3+d_3
\le6S+4+m_2
\le7S+3.
\]

\(s_2\) 最大时完全对称。因此

\[
\boxed{
d_3\ne\max(s_1,s_2,d_3)
\Longrightarrow
n_3\le7S+3.
}
\tag{DD-nondominant-seven-S-plus-three}
\]

当 \(S=3,n_3=25\) 时，\(25>24\)，所以必在
\(d_3\)-dominant 扇区。当 \(S=2,n_3=17\) 时若不 dominant，则上述
不等式链必须处处取等，特别地

\[
m_1=m_2=1,
\qquad
m_3=15,
\qquad
d_3=2.
\]

对 \(1\le b_1,b_2\le9\) 的 81 个有序 denominator 前缀，统一尾权
必须满足

\[
QG<\kappa\le10QG,
\qquad
\kappa\mid10^{15}QG,
\qquad
10^{15}\mid\kappa^2(\kappa+2G).
\]

逐个枚举该显式除数区间没有任何 \(\kappa\)。故 \(S=2\) 的取等锥
也为空，余下两个尺寸都可进入 \(d_3\)-dominant 分析。

### 两个 dominant 尺寸的 denominator-tail 核

在 \(d_3\)-dominant 扇区，第 21 节给出 \(d_3\le5S\)，故

\[
\begin{array}{c|c|c|c}
S&n_3&m_3\text{ 的初始范围}&(m_1,m_2)\\
\hline
2&17&7\le m_3\le15&(1,1)\\
3&25&10\le m_3\le21&(1,2),(2,1).
\end{array}
\]

固定 \((b_1,b_2,m_3)\) 后，

\[
\kappa=\frac{10^{m_3}QG}{b_3}
\]

在 \(m_3\)-位正整数 \(b_3\) 与满足

\[
QG<\kappa\le10QG,
\qquad
\kappa\mid10^{m_3}QG
\]

的除数之间给出双射。再加入统一 primitive-tail 必要条件

\[
10^{m_3}\mid\kappa^2(\kappa+2G),
\tag{DD-small-top-tail-divisibility}
\]

得到

\[
\begin{array}{c|c|c}
S&m_3&\text{尾权数}\\
\hline
2&7,8,9,10&364,203,44,7\\
3&10,11,12,13,14,15,16,17&
22246,9848,5593,1490,481,45,5,2.
\end{array}
\tag{DD-small-top-tail-kernel}
\]

其余初始 \(m_3\) 全部为空。两个尺寸分别只有 618 与 39710 个
denominator-tail 元组；同一张表也已经排除了上面的
\(S=2,m_3=15\) 非 dominant 取等锥。

### 二进位置与强制 resonance

第 27.7 节表明：若三个分母不全奇，则最大二进分母赋值必须唯一。
若它来自前缀，必要高度为

\[
n_3<(5+\log_2 10)S-\log_2 10.
\]

但在两个待查尺寸中分别有

\[
2^{17-5\cdot2}=2^7>10,
\qquad
2^{25-5\cdot3}=2^{10}>10^2,
\]

所以前缀主导位置均不可能。若 \(b_3\) 独占二进最大，第 27.7 节还
强制

\[
\mathfrak k>\mathfrak g,
\qquad
\mathfrak h=\mathfrak g.
\]

此外

\[
\begin{array}{c|c|c}
S&2^{n_3}>10^{2S+1}&2^{n_3}>11\cdot10^{2S}\\
\hline
2&2^{17}>10^5&2^{17}>11\cdot10^4\\
3&2^{25}>10^7&2^{25}>11\cdot10^6
\end{array}
\]

使第 27.8 节证明 \(v_2(E)=\mathfrak q\) 与排除二进
non-resonance 的同一论证在这两个入口边界仍然成立。于是
\(b_3\) 二进主导时必须 resonance，并精确要求

\[
\boxed{
v_2(\mathcal N_{12})
=
3\mathfrak k+\mathfrak f
-2m_3-2\mathfrak q-2\mathfrak g.
}
\tag{DD-small-top-two-requirement}
\]

若三个分母全奇，则第 27.7 节给出另一必要条件

\[
\boxed{v_2(\mathcal N_{12})\ge m_3+1.}
\tag{DD-small-top-all-odd-requirement}
\]

对 618 个 \(S=2\) 尾权，6 个属于全奇分母，3 个落在已排除的
前缀主导或并列位置；其余 609 个中，118 个违反
\(\mathfrak k>\mathfrak g\)，422 个使右端为负，最终留下 75 个。
对 39710 个 \(S=3\) 尾权，相应计数为

\[
139,\quad165,\quad39406,\quad3442,\quad30987,
\]

最终留下 5116 个。

### 五进三分支只剩 \(\Delta_5>0\)

上述 tail 核中的 \(b_3\) 全部被 \(5\) 整除，并逐项满足

\[
d_3+v_5(b_3)>q_5.
\]

所以第 27.2 节的拼接 gap 锁给出 \(e_5=q_5\)。记

\[
k_5=v_5(\kappa),\quad
f_5=v_5(\kappa+2G),\quad
h_5=v_5(\kappa+G),
\]

\[
n_5=v_5(\mathcal N_{12}),\quad
a_5=v_5(A_{12}).
\]

resonance、\(\Delta_5>0\)、\(\Delta_5<0\) 三个必要等式依次化为

\[
3k_5+f_5=2m_3+2q_5+2h_5+n_5,
\]

\[
n_3
=2m_3+2q_5+h_5+n_5-2k_5-g_5-a_5,
\]

\[
n_3=f_5+k_5-h_5-g_5-a_5.
\]

这里

\[
A_{12}<10^{S+2},
\qquad
\mathcal N_{12}<2\cdot10^{4S}
\]

给出 \(a_5,n_5\) 的显式有限范围。逐个代入 75 与 5116 个尾权后，
resonance 和 \(\Delta_5<0\) 均与该范围冲突，只剩
\(\Delta_5>0\)，并固定

\[
\boxed{
n_5-a_5
=
n_3-2m_3-2q_5-h_5+2k_5+g_5.
}
\tag{DD-small-top-five-gap}
\]

现在 \(n_1,n_2\ge1\) 且

\[
n_1+n_2
=S+s_1+s_2
\le S+2.
\]

穷尽这些前缀位数、既约条件、上面的二进条件与五进差后，
\(S=2,3\) 分别只剩 114、27 个 tail-prefix 组合。

### squarefree gap 与最后十个判别式

再使用第 21 节未粗化的必要条件

\[
10^{d_3}A_{12}<40Q^2\mathcal N_{12},
\tag{DD-small-top-squarefree-gap}
\]

上述 114、27 个组合分别只剩 2、8 个：

\[
\begin{array}{c|c|c|c|c|c|r}
S&(m_1,m_2)&(b_1,b_2)&(n_1,n_2)&(a_1,a_2)&m_3&\kappa\\
\hline
2&(1,1)&(5,5)&(1,3)&(1,818)&8&4000\\
2&(1,1)&(5,5)&(1,3)&(1,932)&8&4000\\
3&(1,2)&(5,65)&(4,1)&(9944,4)&12&1600000\\
3&(1,2)&(5,95)&(3,1)&(991,3)&12&800000\\
3&(1,2)&(5,95)&(4,1)&(2973,9)&12&800000\\
3&(2,1)&(65,5)&(1,4)&(4,9944)&12&1600000\\
3&(2,1)&(90,5)&(1,4)&(7,4793)&12&800000\\
3&(2,1)&(90,5)&(1,4)&(7,4793)&12&2400000\\
3&(2,1)&(95,5)&(1,3)&(3,991)&12&800000\\
3&(2,1)&(95,5)&(1,4)&(9,2973)&12&800000.
\end{array}
\tag{DD-small-top-final-ten}
\]

在 DD 中统一 coefficient 满足

\[
C=10^{d_3}A_{12},
\qquad
D=Q.
\]

所以第 7 节的统一判别平方在这里恰为

\[
\boxed{
\mathscr D
=
\left(\kappa GA_{12}10^{d_3}\right)^2
-\kappa(\kappa+2G)Q^2\mathcal N_{12}
=W^2.
}
\tag{DD-small-top-discriminant}
\]

对表中十行作精确整数平方根检查，每个正整数 \(\mathscr D\) 都严格
落在相邻两个整数平方之间。故十行全部排除，两个入口边界为空。
结合第 27.15 节的 \(S\ge4\) 结论，得到
\((\mathrm{DD\text{-}eight\text{-}S\text{-}plus\text{-}one\text{-}empty})\)
与新的全局相对界
\((\mathrm{DD\text{-}global\text{-}relative\text{-}8\text{-}final})\)。

### 机械核验（明确有界的有限证书）

分母尾权表、二进位置计数、五进三分支、所有允许前缀、squarefree
gap 和最后十个判别式可由

~~~bash
uv run python scripts/check_dd_2716.py
~~~

复核。脚本使用整数除数、整数赋值与 math.isqrt；numpy 只用于
对明确有界的前缀整数数组做精确 int64 运算。它只覆盖
\(S=2,3,n_3=8S+1\)，不覆盖新的 \(n_3\le8S\) 无界区域，也不是
DD 空性或主不存在性定理的证书。

## 27.17 新边界 \(n_3=8S\) 的入口上分解

**状态：入口、位置与 \(t_2\ge2\) 正规形为“已严格完成”；
\(t_2=1,S\ge11\) 的空性为“有限证书”；整个 \(8S\) 层仍为
“待证”。** 本节不降低第 27.16 节的全局相对界，而是第一次把等号层
在五进入口以上分成一个已经为空的有限核和八个仍随前缀增长的常数核。
依赖第 19、21、27.7–27.8、27.10–27.14 与 27.16 节。

### \(S\ge11\) 时的位置强制

反设

\[
n_3=8S.
\tag{DD-eight-S-boundary-assumption}
\]

第 27.16 节已经把非 \(d_3\)-dominant 界加强为
\(n_3\le7S+3\)，所以 \(S\ge4\) 时等号层必在 dominant 扇区。
令 \(L_5=\log_5 10\)。该层达到五进入口等价于

\[
5^{3S}\ge10^{2S+1}.
\]

在 \(S=11\) 时这是 \(5^{33}>10^{23}\)，而 \(S\) 每增加一，
左右比值再乘 \(125/100>1\)。因此全部 \(S\ge11\) 都在入口以上，
五进位置只能是 resonance。相反，\(5^{30}<10^{21}\) 表明这里没有
把 \(S=10\) 静默并入入口上证明。

若二进唯一最大来自前缀，或三个分母全奇，第 27.11 节给出

\[
n_3<\frac{29}{4}S+\frac{20}{3}.
\]

右端在 \(S=9\) 已严格小于 \(8S\)，且之后差值继续增加。因此当
\(S\ge11\) 时只剩

\[
\boxed{
b_3\text{ 独占二进最大},
\qquad t_2\ge1.
}
\tag{DD-eight-S-boundary-b3-position}
\]

### \(t_2=1\) 被压成 70 个尺寸

第 27.14 节的一般 surplus 公式在 \(C=0\) 时为

\[
s+D_s
>
4S-5-2a-\frac{2(1-a)}3m_3,
\qquad a=\log_{10}2.
\]

由 \(s+D_s\le2S\)、\(a>301/1000\) 以及第 27.11 节的精确
\(m_3\) 上界得到

\[
\boxed{
\frac{1000S-2801}{233}
<m_3<
\frac{1000S+661}{267}.
}
\tag{DD-eight-S-t2-one-m-window}
\]

两端相容要求

\[
S<\frac{22547}{850}<27.
\]

把 \(11\le S\le26\) 逐个取整数后，\(S=26\) 没有候选，其余得到
下列 70 个尺寸：

\[
\begin{array}{c|l@{\qquad}c|l}
S&m_3&S&m_3\\
\hline
11&36,37,38,39,40,41,42,43&19&70,71,72,73\\
12&40,41,42,43,44,45,46,47&20&74,75,76,77\\
13&44,45,46,47,48,49,50,51&21&79,80,81\\
14&49,50,51,52,53,54&22&83,84\\
15&53,54,55,56,57,58&23&87,88\\
16&57,58,59,60,61,62&24&91,92\\
17&61,62,63,64,65,66&25&96\\
18&66,67,68,69&&
\end{array}
\tag{DD-eight-S-t2-one-size-kernel}
\]

这一步先给出了 \(S\) 的绝对上界，所以下面的计算只覆盖一个严格
有界切片。

### 精确模计数消去全部余因子

沿用第 27.14 节的赋值记号

\[
(\mathfrak q,\mathfrak n,\mathscr A_5,
  \mathfrak g,\mathfrak f,k_5).
\]

由 \(Q,G<10^S\)、\(\mathcal N_{12}<2\cdot10^{4S}\) 和
\(\kappa<10^{2S+1}\)，只需检查

\[
0\le\mathfrak q,\mathfrak g<4S,
\qquad
0\le\mathfrak n\le14S,
\qquad
0\le\mathscr A_5\le3S+3.
\]

最后一个范围来自 \(k_5\le3S+1\)、\(m_3\ge3S\) 与
\(\mathscr A_5=3k_5-2m_3\)。在这个盒中继续要求

\[
k_5=\frac{2m_3+\mathscr A_5}{3}\in\mathbf Z,
\qquad
\mathfrak f=2m_3+2\mathfrak q+\mathfrak n-\mathfrak g-3,
\]

两个单因子高度界，以及第 27.13 节的 combined-height 整数不等式

\[
10^{2m_3}2^{4m_3+6\mathfrak q+3\mathfrak n}5^{\mathscr A_5}
<2^6 11^3 10^{12S+3}.
\tag{DD-eight-S-t2-one-combined-integer}
\]

70 个尺寸共留下 51828 个赋值行，其中 63 个尺寸非空。

对每一行写

\[
\kappa=2^{\mathfrak g+1}5^{k_5}u,
\qquad \gcd(u,10)=1,
\]

并令

\[
U=\left\lfloor
\frac{10(10^S-1)^2}{2^{\mathfrak g+1}5^{k_5}}
\right\rfloor,
\quad
M=\left\lfloor\frac{10^S-1}{2^{\mathfrak g}}\right\rfloor,
\quad
h=\mathfrak f-\mathfrak g-1.
\]

精确等式 \(v_2(\kappa+2G)=\mathfrak f\) 要求某个
\(1\le u\le U\) 使

\[
\left[5^{k_5}u+1,\ 5^{k_5}u+M\right]
\]

包含 \(2^h\) 的一个奇数倍。模 \(2^{h+1}\) 看，这等价于
\(5^{k_5}u\) 落在从 \(2^h-M\) 到 \(2^h-1\) 的循环剩余类区间。
脚本用精确 floor-sum 计算该区间中的 \(u\) 数量，再对 \(2,5\)
作容斥；因此不需要逐个走过可能极长的十进制余因子区间。该计数器
先与 1000 个随机小盒的直接枚举逐项对照，随后检查全部 51828 行，
得到

\[
\boxed{
t_2=1,\ S\ge11,\ n_3=8S
\Longrightarrow\text{无候选}.
}
\tag{DD-eight-S-t2-one-empty}
\]

### \(t_2\ge2\) 等号层的八个常数核

这一支不能用上面的有限证书代替无界推导。第 27.13 节的加权界与
\(\Xi\ge2\) 给出 \(m_3\le3S+1\)，而 \(d_3\le5S\) 给出
\(m_3\ge3S\)。若 \(m_3=3S+1\)，代回未粗化的加权界便有
\(\Xi<20\)。模 \(3\) 锁只允许

\[
\Xi\in\{2,16\},
\qquad \mathscr A_5=0.
\]

但五进 resonance 随即要求

\[
3k_5=2m_3=6S+2,
\]

不可能。因此必有

\[
\boxed{m_3=3S,\qquad d_3=5S.}
\tag{DD-eight-S-t2-ge2-md-shape}
\]

squarefree gap 界

\[
d_3\le3S+D_s+2
\]

继而强迫 \(D_s=2S-2\)。结合 surplus simplex、
\(m_1+m_2=S\) 与两个 numerator block 均非空，除交换前两块外
只有

\[
\boxed{
(m_{\rm long\ surplus},n_{\rm long\ surplus})=(1,S+1),
\quad
(m_{\rm other},n_{\rm other})=(S-1,1).
}
\tag{DD-eight-S-t2-ge2-digit-shape}
\]

两处 resonance 的模 \(3\) 条件可写成

\[
\mathscr A_2=1+3u,
\qquad
\mathscr A_5=3v,
\qquad u,v\ge0.
\]

于是

\[
k_2=2S+u,
\qquad k_5=2S+v,
\]

并存在与 10 互素的正整数 \(w\) 使

\[
\kappa
=10^{2S}c,
\qquad
c=2^u5^v w.
\]

上述极端位数形状给出

\[
G<9\cdot10^{S-1},
\qquad Q<10^S.
\]

再用 \(\kappa\le10QG\)，得到 \(c<9\)。所以等号层被严格压成

\[
\boxed{c\in\{1,2,3,4,5,6,7,8\}.}
\tag{DD-eight-S-eight-constant-cores}
\]

对应的加权赋值只有

\[
\begin{array}{c|cccccccc}
c&1&2&3&4&5&6&7&8\\
\hline
\mathscr A_2&1&4&1&7&1&4&1&10\\
\mathscr A_5&0&0&0&0&3&0&0&0
\end{array}
\tag{DD-eight-S-core-valuations}
\]

特别地，\(c\ne5\) 时
\(q_5=g_5=n_5=0\)。由

\[
b_3=\frac{10^S QG}{c}
\]

和 \(\gcd(w,10)=1\) 还可严格推出 \(w\mid QG\)，从而

\[
b_3=2^{S-u}5^{S-v}\frac{QG}{w},
\qquad
\boxed{10^{S-3}\mid b_3.}
\tag{DD-eight-S-forced-tail-zeros}
\]

这里的八个 \(c\) 是八个**无界前缀族**，不是八个原问题候选；统一
判别平方、既约性和真实块同余仍需继续施加。

### 当前边界与机械核验

综上，\(n_3=8S\) 的入口上部分已经精确分解为：

1. \(S\ge11,t_2=1\)：由有限证书排除；
2. \(S\ge11,t_2\ge2\)：只剩上述八个常数核无界族；
3. \(2\le S\le10\)：仍在入口边界下方的有限 \(S\)-列表；这本身
   不构成完整有限候选盒，尚未核验。

因此本节没有证明 \(n_3=8S\) 为空，也没有把全局界降低到
\(8S-1\)。有理尺寸核、51828 个赋值行、精确模计数器的小盒对照、
零余因子结论和八核赋值表可由

```bash
uv run python scripts/check_dd_2717.py
```

复核。脚本不枚举原始 DD 候选；有限证书只覆盖先由符号不等式固定的
\(11\le S\le25,t_2=1\) 切片，不能关闭八个无界常数核或
\(S\le10\) 的剩余 \(S\)-列表。

## 27.18 用 \(F_-\) 常数商关闭入口上的八个无界核

**状态：`已严格完成`。** 本节关闭第 27.17 节留下的全部
\(S\ge11,t_2\ge2,n_3=8S\) 常数核，但不处理
\(2\le S\le10\) 的入口下切片，也不排除 \(n_3<8S\) 的无界区域。
依赖第 7、27.1、27.8、27.11、27.17 节。

### \(F_-\) 只剩一个小于 20000 的整数商

仍在第 27.17 节的八核正规形中，令

\[
T=10^{2S},
\qquad
\kappa=cT,
\qquad
c=2^u5^v w\in\{1,\ldots,8\},
\qquad
\gcd(w,10)=1.
\]

此时

\[
m_3=3S,
\qquad n_3=8S,
\qquad
k_2=2S+u,
\qquad k_5=2S+v.
\]

第 27.11 节在该 \(t_2\ge2\) 双 resonance 位置给出

\[
v_2(F_-)=k_2+1,
\qquad
v_5(F_-)=k_5.
\]

另一方面，未粗化的阿基米德上界

\[
F_-<2\cdot10^{4S+2m_3-n_3+4}
\]

在当前等号层化为

\[
F_-<2\cdot10^{2S+4}.
\]

所以存在正整数 \(\rho\) 使

\[
\boxed{
F_-=T\rho,
\qquad
0<\rho<20000,
\qquad
v_2(\rho)=u+1,
\qquad
v_5(\rho)=v.
}
\tag{DD-eight-S-Fminus-constant-quotient}
\]

也就是说

\[
\rho=2^{u+1}5^v z,
\qquad \gcd(z,10)=1,
\]

其中 \(z\) 落在与 \(S\) 无关的有限区间。八核合计只有 18300 个
允许的 \((c,\rho)\) 赋值行；下面甚至不需要逐个枚举它们。

### 两个 \(\mu/\nu\) 公式给出大除数

统一因子与 primitive recovery 分别为

\[
F_-=\frac{2(\kappa+2G)\mu^2}{G_0},
\qquad
10^{3S}QG_0=2\kappa\mu\nu,
\qquad
\gcd(\mu,\nu)=1.
\]

把 \(F_-=T\rho\) 与 \(\kappa=cT\) 代入并消去 \(G_0\)，得到

\[
\boxed{
\frac{\mu}{\nu}
=
\frac{\rho c10^S}{Q(cT+2G)}.
}
\tag{DD-eight-S-munu-from-Fminus}
\]

第 27.1 节的拼接 gap 另一方面给出

\[
\frac{\mu}{\nu}
=
\frac{E\kappa^2}{10^{3S}Q^2(\kappa+G)}
=
\frac{Ec^2 10^S}{Q^2(cT+G)},
\qquad E\in\mathbf Z_{>0}.
\tag{DD-eight-S-munu-from-gap}
\]

比较两式并清分母：

\[
\boxed{
\rho Q(cT+G)=Ec(cT+2G).
}
\tag{DD-eight-S-core-divisor-identity}
\]

令

\[
\Gamma=\gcd(cT+2G,cT+G)=\gcd(cT,G).
\]

由上式及互素化立即有

\[
\boxed{
\frac{cT+2G}{\Gamma}\mid\rho Q.
}
\tag{DD-eight-S-core-large-divisor}
\]

这一步是精确整数整除，不是渐近估计。

### gcd 只有常数大小

第 27.17 节已经固定

\[
\mathscr A_2=1+3u,
\qquad
\mathscr A_5=3v.
\]

因为

\[
\mathfrak g=v_2(G)\le\mathscr A_2,
\qquad
g_5=v_5(G)\le\mathscr A_5,
\]

且 \(cT\) 除 \(2,5\) 外的素因子只可能来自 \(w\)，所以

\[
\Gamma
\le2^{\mathscr A_2}5^{\mathscr A_5}w.
\]

八核的逐项常数为

\[
\begin{array}{c|cccccccc}
c&1&2&3&4&5&6&7&8\\
\hline
u&0&1&0&2&0&1&0&3\\
v&0&0&0&0&1&0&0&0\\
w&1&1&3&1&1&3&7&1\\
\Gamma_{\max}&2&16&6&128&250&48&14&1024\\
\Gamma_{\max}/c&2&8&2&32&50&8&2&128
\end{array}
\tag{DD-eight-S-core-gcd-table}
\]

特别地

\[
\frac{\Gamma}{c}\le128.
\]

但大除数的左边严格大于 \(c10^{2S}/\Gamma\)，而
\(\rho Q<20000\cdot10^S\)。因此整除关系强迫

\[
10^S
<20000\frac{\Gamma}{c}
\le2560000
<10^7.
\]

这与 \(S\ge11\) 矛盾。于是

\[
\boxed{
n_3=8S,\ S\ge11,\ t_2\ge2
\Longrightarrow\text{无候选}.
}
\tag{DD-eight-S-t2-ge2-empty}
\]

结合第 27.17 节的 \(t_2=1\) 有限证书与位置穷尽，得到

\[
\boxed{
n_3=8S\Longrightarrow S\le10.
}
\tag{DD-eight-S-small-S-only}
\]

等价地，所有 \(S\ge11\) 的 DD 候选都满足

\[
\boxed{n_3\le8S-1.}
\tag{DD-large-S-relative-eight-minus-one}
\]

这仍不是 DD 空性或 prefix-uniform 绝对高度界；在这一中间阶段，
等号层只剩 \(2\le S\le10\) 的有限 \(S\)-列表，但固定 \(S\) 并不
自动限制 non-dominant prefix surplus，而 \(n_3<8S\) 仍允许
\(S\to\infty\)。

### 机械核验（非证明器）

八核的 \((u,v,w,\mathscr A_2,\mathscr A_5)\) 表、18300 个
\((c,\rho)\) 赋值行的计数、\(\Gamma_{\max}\) 表和最后的统一常数比较可由

```bash
uv run python scripts/check_dd_2718.py
```

复核。脚本不证明
\((\mathrm{DD\text{-}eight\text{-}S\text{-}core\text{-}divisor\text{-}identity})\)
的符号消元，也不枚举原始块；无界 \(S\ge11\) 的覆盖来自正文的精确
整除与指数阶差，而不是有限循环。

## 27.19 小尺寸的 \(t_2=1\) 唯一五进正规形排除

**状态：`有限证书`。** 本节只处理

\[
4\le S\le10,
\qquad n_3=8S,
\]

中同时满足下列假设的子支：\(b_3\) 独占二进最大、\(t_2=1\)，且
五进侧已经落入第 27.6 节的唯一正规形

\[
\boxed{
e_5=q_5,
\qquad
k_5>g_5,
\qquad
h_5=f_5=g_5,
\qquad
3k_5=2m_3+2q_5+g_5+n_5.
}
\tag{DD-small-eight-S-five-normal-form}
\]

入口下的普通 resonance 并不自动满足这组条件；本节不把它、
\(5\nmid b_3\) 或 \(\Delta_5^\pm\) 静默并入证书。依赖第 20–21、
27.1–27.3、27.6–27.8、27.14、27.17 节。

### 56 个尺寸与同步 \(F_-\) 因子界

第 27.17 节的 surplus 推导只需 \(S\ge4\) 使相应函数关于
\(a=\log_{10}2\) 递增。因此同一个有理窗口

\[
\frac{1000S-2801}{233}
<m_3<
\frac{1000S+661}{267}
\]

在当前七个 \(S\) 上给出

\[
\begin{array}{c|l}
S&m_3\\
\hline
4&12,13,14,15,16,17\\
5&15,16,17,18,19,20,21\\
6&18,19,20,21,22,23,24\\
7&21,22,23,24,25,26,27,28\\
8&24,25,26,27,28,29,30,31,32\\
9&27,28,29,30,31,32,33,34,35,36\\
10&31,32,33,34,35,36,37,38,39
\end{array}
\tag{DD-small-eight-S-t2-one-size-kernel}
\]

共 56 个尺寸。第 27.17 节的有限赋值盒先留下 97693 行。这里还可
加入此前余因子扫描没有单独使用的同步因子下界。当前正规形给出

\[
v_2(F_-)=\mathfrak f+1,
\qquad
v_5(F_-)=k_5,
\]

而 \(n_3=8S\) 时

\[
F_-<2\cdot10^{2m_3-4S+4}.
\]

所以每个赋值行还必须满足纯整数不等式

\[
\boxed{
2^{\mathfrak f}5^{k_5}
<10^{2m_3-4S+4}.
}
\tag{DD-small-eight-S-Fminus-integer}
\]

逐项加入后只剩 3121 行。

### 余因子、真实分母块与唯一尾核

对 \(m_3=3S\)，squarefree gap 强迫第 27.17 节的极端位数形状，
所以使用

\[
G\le9(10^{S-1}-1);
\]

其余尺寸使用一般 \(G\le10^S-1\)。精确 floor-sum 余因子区间把
3121 行压成 113 个赋值—余因子对，且只出现在

\[
\begin{array}{c|c|c}
S&m_3&\text{余因子对数}\\
\hline
4&12&56\\
5&15&32\\
5&16&1\\
6&18&14\\
7&21&6\\
8&24&3\\
9&27&1.
\end{array}
\tag{DD-small-eight-S-cofactor-counts}
\]

每个余因子又固定一个或多个奇数 \(G_*\)。对它们精确分解
\(G=b_1b_2\)，要求 \(b_i\) 具有指定十进制位数、
\(Q=b_1 10^{m_2}+b_2\) 具有指定二进赋值、五进预算非负，并重新
施加 \(QG<\kappa\le10QG\)。113 对最终只剩

\[
\boxed{
\begin{gathered}
S=5,\quad m_3=16,\\
(\mathfrak q,\mathfrak n,\mathscr A_5,
  \mathfrak g,\mathfrak f,k_5)
=(0,0,1,8,21,11),\\
u=1,\quad
(m_1,m_2)=(3,2),\quad
(b_1,b_2)=(768,97),\\
Q=76897,\quad G=74496,\quad
\kappa=25000000000,\quad n_5=1.
\end{gathered}
}
\tag{DD-small-eight-S-sole-tail-core}
\]

这里的 \(u\) 是 \(t_2=1\) 余因子，不是第 27.17 节八核中的
二进指数参数。

### 同一个模 \(3\) 判别式矛盾

尾关系固定

\[
b_3=\frac{10^{16}QG}{\kappa}
=2291407564800000.
\]

回到 near-square 判别式

\[
Y^2
=X^2-
\mathcal N_{12}10^{16}Q(10^{16}Q+2b_3).
\]

由于 \(3\mid G\)，有 \(X\equiv0\pmod3\)；又有
\(Q\equiv1\pmod3\)、\(3\mid b_3\) 和 \(10^{16}\equiv1\pmod3\)，
故尾部两个因子的乘积模 \(3\) 为 1。最后

\[
\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2
\equiv a_1^2\equiv1\pmod3,
\]

其中最后一步来自 \(3\mid b_1\) 与 \(\gcd(a_1,b_1)=1\)。因此

\[
Y^2\equiv2\pmod3,
\]

矛盾。于是

\[
\boxed{
4\le S\le10,\ n_3=8S,\ t_2=1,
\ \text{且满足唯一五进正规形}
\Longrightarrow\text{无候选}.
}
\tag{DD-small-eight-S-t2-one-five-normal-empty}
\]

上述 56 个尺寸、97693 个初始赋值行、3121 个同步
\(F_-\) 行、113 个余因子对、真实 denominator factorization 与最终
模 \(3\) 检查可由

```bash
uv run python scripts/check_dd_2719.py
```

复核。它不枚举 numerator block；最后的模 \(3\) 论证统一覆盖所有
与唯一尾核相容的既约 numerators。脚本也不覆盖本节开头明确排除在
证书范围外的其他五进状态。

## 27.20 小尺寸的 \(t_2\ge2\) 唯一五进正规形排除

**状态：\(S\ge7\) 为“已严格完成”；\(S=4,5,6\) 为“有限证书”。**
仍只处理
\((\mathrm{DD\text{-}small\text{-}eight\text{-}S\text{-}five\text{-}normal\text{-}form})\)
所写的五进正规形与 \(b_3\) 二进主导位置，不外推到其他入口下状态。
依赖第 27.17–27.19 节。

在 \(t_2\ge2\) 中，第 27.17 节的符号推导仍原样给出

\[
m_3=3S,
\qquad d_3=5S,
\qquad
\kappa=c10^{2S},\qquad1\le c\le8,
\]

以及一个 1 位 denominator 与一个 \(S-1\) 位 denominator 的极端
形状。第 27.18 节的大除数论证只在最后一步使用 \(S\) 的大小；它
实际给出必要条件

\[
10^S<20000\frac{\Gamma}{c}
\le2560000<10^7.
\]

所以这条正规形对全部 \(S\ge7\) 已经严格为空。

只剩 \(S=4,5,6\)。对每个 \(c\in\{1,\ldots,8\}\)、两种前缀顺序、
1 位分母 \(1\le d\le9\) 和所有 \(S-1\) 位分母 \(B\)，有限证书依次
施加：

1. \(\mathscr A_2=1+3v_2(c)\)、
   \(\mathscr A_5=3v_5(c)\) 的非负剩余预算；
2. \(t_2=2S+v_2(c)-v_2(dB)\ge2\)；
3. 真实拼接 \(Q\) 的尾区间
   \(QG<c10^{2S}\le10QG\)；
4. 大除数
   \[
   H=\frac{c10^{2S}+2G}{\gcd(c10^{2S},G)}
   \]
   在约去 \(\gcd(H,Q)\) 后，必须整除某个
   \(0<\rho<20000\)，且
   \(v_2(\rho)=v_2(c)+1\)、\(v_5(\rho)=v_5(c)\)。

精确计数为

\[
\begin{array}{c|r|r|r|r}
S&\text{真实分母顺序}&\text{局部预算后}&\text{尾区间后}&\text{最终}\\
\hline
4&129600&54219&8373&0\\
5&1296000&542960&83661&0\\
6&12960000&5429698&836574&0.
\end{array}
\tag{DD-small-eight-S-t2-ge2-denominator-counts}
\]

因此

\[
\boxed{
4\le S\le10,\ n_3=8S,\ b_3\text{ 二进主导},
\ \text{且满足唯一五进正规形}
\Longrightarrow\text{无候选}.
}
\tag{DD-small-eight-S-b3-five-normal-empty}
\]

这里合并了第 27.19 节的 \(t_2=1\) 与本节的 \(t_2\ge2\)。仍未
处理的是：\(S=2,3\)；\(4\le S\le8\) 的其他二进位置；以及
\(4\le S\le10\) 中不满足唯一五进正规形的普通 resonance、
\(5\nmid b_3\) 与 \(\Delta_5^\pm\) 状态。对 \(S=9,10\)，其他二进
位置已由第 27.11 节排除，所以等号层若存在，必在 \(b_3\) 二进主导
位置且位于这些尚未处理的五进状态中。

小尺寸分母枚举可由

```bash
uv run python scripts/check_dd_2720.py
```

复核。脚本不枚举 numerator block；它只检查正文严格固定的
denominator/core 必要条件。有限枚举的最大 \(S\) 明确为 6，不能被
外推为更低层或其他五进状态的全局证书。

## 27.21 排除全部 \(S\ge4\) 的 \(8S\) 等号层

**状态：`已严格完成`。** 本节把第 27.20 节尚未覆盖的五进状态逐一
排除，并同时补上唯一五进正规形中的其他二进位置。结论是

\[
\boxed{
n_3=8S\Longrightarrow S\le3,
}
\tag{DD-eight-S-only-S-two-three}
\]

或等价地

\[
\boxed{
S\ge4\Longrightarrow n_3\le8S-1.
}
\tag{DD-S-ge-four-eight-minus-one}
\]

这还没有关闭 \(S=2,3\) 的等号层，也没有处理 \(n_3<8S\) 的无界
区域。依赖第 20–21、27.1–27.8、27.10–27.11、27.17–27.20 节。

### \(5\mid b_3\) 时自动恢复 gap 锁

反设 \(S\ge4,n_3=8S\)。第 27.16 节的非 dominant 界
\(n_3\le7S+3\) 先强制候选进入 \(d_3\)-dominant 扇区，所以

\[
m_3\ge3S.
\tag{DD-eight-S-m-lower-all-S-ge-four}
\]

若 \(5\mid b_3\)，记 \(B_5=v_5(b_3)\ge1\)。统一尾长界
\(m_3\le6S+3\) 给出

\[
d_3=8S-m_3\ge2S-3.
\]

另一方面，\(Q<10^S\)，而

\[
5^{2S-2}>10^S
\]

在 \(S=4\) 时为 \(5^6>10^4\)，之后左右比值每次乘
\(25/10>1\)。所以

\[
q_5=v_5(Q)<2S-2.
\]

于是对任意 \(a_5=v_5(A_{12})\ge0\)，都有

\[
d_3+B_5+a_5>q_5.
\]

第 27.2 节的拼接 gap 锁因此在整个当前等号层恢复为

\[
\boxed{e_5=q_5.}
\tag{DD-eight-S-small-gap-lock}
\]

### 五进 resonance 已无位置可落

先设发生五进 resonance。若 \(k_5<g_5\)，则
\(h_5=f_5=k_5\)，resonance 恒等式化为

\[
2k_5=2m_3+2q_5+n_5,
\]

故 \(k_5\ge m_3\ge3S\)。这与
\(g_5>k_5\) 及 \(5^{g_5}\le G<10^S\) 矛盾。

若 \(k_5=g_5\)，则 \(h_5\ge g_5\)，从而 resonance 恒等式给出

\[
g_5+f_5\ge2m_3\ge6S.
\]

但

\[
5^{g_5+f_5}
\le G(\kappa+2G)
<11\cdot10^{3S},
\]

而 \(5^{6S}>11\cdot10^{3S}\) 已在 \(S=4\) 成立并随 \(S\) 增强，
再次矛盾。

所以只可能有 \(k_5>g_5\)，此时 \(h_5=f_5=g_5\)，恰好回到
\((\mathrm{DD\text{-}small\text{-}eight\text{-}S\text{-}five\text{-}normal\text{-}form})\)。
若 \(b_3\) 二进主导，第 27.19–27.20 节已经排除；若二进最大来自
前缀或三个分母全奇，第 27.8 节在同一五进正规形下给出

\[
m_3<\frac{6S+3}{2+a},
\qquad a=\log_{10}2.
\]

由 \(a>1/4\) 与 \(S\ge4\)，右端严格小于 \(3S\)，又与
\((\mathrm{DD\text{-}eight\text{-}S\text{-}m\text{-}lower\text{-}all\text{-}S\text{-}ge\text{-}four})\)
矛盾。因此五进 resonance 在所有二进位置均为空。

### \(\Delta_5<0\) 与 \(\Delta_5>0\) 也为空

对 \(\Delta_5<0\)，第 27.2 节的精确式在 \(e_5=q_5\) 后为

\[
n_3=f_5+k_5-h_5-g_5-a_5.
\]

若 \(k_5<g_5\)，右端为 \(k_5-g_5-a_5<0\)；若 \(k_5>g_5\)，
右端为 \(k_5-g_5-a_5<k_5\)，但
\(5^{k_5}\le\kappa<10^{2S+1}\) 不可能支持 \(n_3=8S\)；若
\(k_5=g_5\)，则 \(n_3\le f_5\)，又与
\(5^{f_5}\le\kappa+2G<11\cdot10^{2S}\) 矛盾。故
\(\Delta_5<0\) 为空。

对 \(\Delta_5>0\)，第 27.6 节的 unique-max 论证只需
\(m_3\ge3S>v_5(G)\)，所以仍给出

\[
k_5\ge g_5,
\qquad h_5=g_5.
\]

若 \(k_5=g_5\)，第 27.10 节的 primitive recovery 消元得到
\(v_5(F_-)=f_5>n_3\)，与
\(5^{f_5}<11\cdot10^{2S}\) 矛盾。若 \(k_5>g_5\)，同一消元得到

\[
v_5(F_-)=k_5>n_3,
\]

又与 \(5^{k_5}\le\kappa<10^{2S+1}\) 矛盾。因此
\(\Delta_5>0\) 也为空。

综上，只要 \(5\mid b_3\)，三个五进状态已经全部排除。

### \(5\nmid b_3\) 只会产生一个不可能的二进尾核

现在设 \(5\nmid b_3\)。尾关系给出

\[
k_5=m_3+q_5+g_5.
\]

而 \(5^{3S+1}>10^{2S+1}\) 在 \(S=4\) 已成立并持续增强，所以
\(\kappa<10^{2S+1}\) 强迫 \(k_5\le3S\)。结合 \(m_3\ge3S\)，
得到

\[
\boxed{
m_3=k_5=3S,
\qquad q_5=g_5=0,
\qquad d_3=5S.
}
\tag{DD-eight-S-five-unit-md-core}
\]

squarefree gap 再次强迫一个 1 位 denominator 与一个 \(S-1\) 位
denominator。故

\[
G<9\cdot10^{S-1},
\qquad
\kappa<9\cdot10^{2S}.
\]

写 \(\kappa=5^{3S}c\)。由 \(4\cdot5^{3S}>9\cdot10^{2S}\) 可知
\(c\in\{1,2,3\}\)，所以 \(k_2=v_2(\kappa)\le1\)。另一方面

\[
v_2(b_3)=3S+v_2(Q)+v_2(G)-k_2
\]

严格大于 \(v_2(b_1),v_2(b_2)\)：减去任一前缀赋值后，仍至少有
\(3S-k_2>0\)。所以 \(b_3\) 必独占二进最大；第 27.7 节要求
\(k_2>v_2(G)\)。这排除 \(c=1,3\)，并强制

\[
\boxed{
\kappa=2\cdot5^{3S},
\qquad v_2(G)=0,
\qquad t_2=1.
}
\tag{DD-eight-S-five-unit-two-core}
\]

当 \(S\ge7\) 时，\(2\cdot5^{3S}>9\cdot10^{2S}\)，与尾高度直接
矛盾。只剩 \(S=4,5,6\)。在这三个尺寸中，
\(2^{8S}>11\cdot10^{2S}\)，故第 27.8 节的二进 non-resonance
两式都要求 \(n_3<f_2<8S\)，不可能；二进侧必须 resonance。其
\(t_2=1\) 正规形给出

\[
f_2+v_2(G)+3
=2m_3+2v_2(Q)+v_2(\mathcal N_{12}),
\]

从而 \(f_2\ge6S-3\)。但

\[
\kappa+2G=2(5^{3S}+G),
\]

所以必须有

\[
2^{6S-4}\mid5^{3S}+G.
\]

三个剩余类及真实 \(G\) 上界为

\[
\begin{array}{c|r|r}
S&-5^{3S}\bmod2^{6S-4}&9(10^{S-1}-1)\\
\hline
4&177583&8991\\
5&16954995&89991\\
6&3528660519&899991.
\end{array}
\tag{DD-eight-S-five-unit-residues}
\]

每个最小正剩余都已经大于 \(G\) 上界，而模数本身更大，因此没有
任何正整数 \(G\) 可满足同余。五进单位尾也全部排除。

结合 \(5\mid b_3\) 与 \(5\nmid b_3\) 两部分，即得
\((\mathrm{DD\text{-}eight\text{-}S\text{-}only\text{-}S\text{-}two\text{-}three})\)
与
\((\mathrm{DD\text{-}S\text{-}ge\text{-}four\text{-}eight\text{-}minus\text{-}one})\)。

### 机械核验（非证明器）

gap 锁所需幂比较、五进各状态的高度常数、尾权乘数界，以及最后三个
二进剩余类可由

```bash
uv run python scripts/check_dd_2721.py
```

复核。脚本不验证正文的 gap/resonance/primitive recovery 消元，也不
枚举原始 DD 候选；\(S\ge4\) 的无界覆盖来自正文的单调幂比较。

## 27.22 关闭 \(S=2,3\) 并排除整个 \(8S\) 等号层

**状态：non-dominant 排除与 dominant 有限化为“已严格完成”；最终
判别式空性为“有限证书”。** 本节只处理第 27.21 节严格留下的
\(S\in\{2,3\},n_3=8S\)，不把固定 \(S\) 本身误作无界前缀的上界。
结论是

\[
\boxed{n_3=8S_{12}\quad\text{在 DD 中为空},}
\tag{DD-eight-S-empty}
\]

从而 DD 的统一相对界严格改进为

\[
\boxed{n_3\le8S_{12}-1.}
\tag{DD-global-relative-eight-minus-one}
\]

这里 \(S_{12}=m_1+m_2\ge2\)，所以第 27.21 节的 \(S\ge4\) 无界
排除与本节两个小尺寸已经穷尽全部 \(S\)。依赖第 19–21、27.1–27.2、
27.7、27.16 与 27.21 节。

### non-dominant 无需给 prefix surplus 截断

若 \(s_1\) 是最大 surplus，第 27.16 节的细化给出

\[
s_2+d_3\le2,\qquad s_2\ge1-m_2,
\]

故

\[
d_3\le1+m_2\le S.
\]

\(s_2\) 最大时完全对称。因此在当前等号层，任一 non-dominant
候选都必须满足

\[
\boxed{m_3=n_3-d_3\ge8S-S=7S.}
\tag{DD-small-eight-S-nondominant-m-lower}
\]

特别地，\(S=2,3\) 分别要求 \(m_3\ge14,21\)。另一方面，对所有真实
有序 denominator 前缀、所有 \(1\le m_3\le6S+3\)，穷尽

\[
QG<\kappa\le10QG,\qquad
\kappa\mid10^{m_3}QG,\qquad
10^{m_3}\mid\kappa^2(\kappa+2G)
\tag{DD-small-eight-S-tail-kernel-conditions}
\]

所得 primitive denominator-tail 核只在

\[
\begin{array}{c|c}
S&\text{非空的最大 }m_3\\
\hline
2&10\\
3&17
\end{array}
\]

以前出现。因此两个 non-dominant 扇区都为空。这一步没有枚举
\(a_1,a_2\)，也不需要限制可能无界的 prefix surplus。

### dominant 扇区是真正有限的

在 dominant 扇区，squarefree gap 给出 \(d_3\le5S\)，故
\(m_3\ge3S\)。逐项检查
\((\mathrm{DD\text{-}small\text{-}eight\text{-}S\text{-}tail\text{-}kernel\text{-}conditions})\)
得到

\[
\begin{array}{c|r|r|r|r}
S&\text{tail rows}&b_3\text{ 二进独大}&\text{全奇}&\text{前缀独大或并列}\\
\hline
2&1527&1450&32&45\\
3&72092&70478&616&998
\end{array}
\tag{DD-small-eight-S-dominant-tail-counts}
\]

若二进最大值来自前缀，第 27.7 节要求

\[
n_3<(5+\log_2 10)S-\log_2 10.
\]

右端在 \(S=2,3\) 时分别为 \(10+\log_2 10<16\) 与
\(15+2\log_2 10<24\)，所以前缀独大位置为空；正赋值并列则违反
最大二进分母赋值必须唯一。对 \(b_3\) 独大位置还必须有
\(k_2>g_2\)，只剩 1101、62777 个 tail rows。加上 32、616 个
全奇 rows，真正进入前缀证书的 tail rows 共 1133、63393 个。

此时 surplus simplex 给出

\[
n_1+n_2=S+s_1+s_2\le S+2,
\]

而 dominant 条件还要求 \(d_3\ge s_1,s_2\)。所以这里——与上面的
non-dominant 扇区不同——所有 numerator block 确实落在显式有限盒。

### 两素数三状态与统一判别式

对 \(b_3\) 二进独大 rows，有限核逐项满足

\[
d_3+v_2(b_3)>v_2(Q),
\]

故 \(e_2=q_2\)，并且 resonance、\(\Delta_2>0\)、
\(\Delta_2<0\) 三态分别要求

\[
\begin{aligned}
n_2^{(v)}&=3k_2+f_2-2m_3-2q_2-2h_2,\\
n_2^{(v)}-a_2^{(v)}
&=n_3-2m_3-2q_2-h_2+2k_2+g_2+1,\\
a_2^{(v)}&=f_2+k_2-h_2-g_2-1-n_3.
\end{aligned}
\tag{DD-small-eight-S-two-state-requirements}
\]

这里上标 \((v)\) 只表示赋值：
\(n_p^{(v)}=v_p(\mathcal N_{12})\)、
\(a_p^{(v)}=v_p(A_{12})\)，避免与十进制位数混淆。三个分母全奇时
则保留第 27.7 节较弱但无遗漏的必要条件

\[
v_2(\mathcal N_{12})\ge m_3+1.
\]

若 \(5\mid b_3\)，由于当前最小 \(d_3\) 已大于 \(v_5(Q)\)，同样有
\(e_5=q_5\)，并逐项施加与
\((\mathrm{DD\text{-}small\text{-}eight\text{-}S\text{-}two\text{-}state\text{-}requirements})\)
相同的三态公式（把 \(2\) 换成 \(5\)，并删除二进的 \(+1\) 与
\(-1\)）。若 \(5\nmid b_3\)，证书不施加任何五进 gap-lock 条件，
因此不会误删该支。

最后再施加既约性、未粗化 squarefree gap

\[
10^{d_3}A_{12}<40Q^2\mathcal N_{12},
\]

以及第 20 节的统一判别平方必要条件

\[
\mathscr D
=
\left(\kappa GA_{12}10^{d_3}\right)^2
-\kappa(\kappa+2G)Q^2\mathcal N_{12}
=W^2.
\tag{DD-small-eight-S-discriminant}
\]

证书计数为

\[
\begin{array}{c|r|r|r|r}
S&\text{digit pairs}&\text{coprime pairs}&
\text{valuation-tail discriminants}&\text{square discriminants}\\
\hline
2&1898073&796260&703&0\\
3&550901574&221462636&38633&0
\end{array}
\tag{DD-small-eight-S-prefix-certificate-counts}
\]

最后一列由精确整数 `isqrt` 检查；全部 39336 个非负判别式均严格
不是平方。因此 \(S=2,3\) 的 dominant 扇区也为空，与 non-dominant
排除合并即得
\((\mathrm{DD\text{-}eight\text{-}S\text{-}empty})\) 和
\((\mathrm{DD\text{-}global\text{-}relative\text{-}eight\text{-}minus\text{-}one})\)。

### 机械核验（明确有界的有限证书）

denominator-tail 核、二进位置分解、两素数三状态、全部 dominant
前缀、squarefree gap 与统一判别式可由

```bash
uv run python scripts/check_dd_2722.py
```

复核。NumPy 只用于明确有界数组上的精确 `int64` gcd、低位 limb
乘加、比较与赋值计算；可能超过 `int64` 的 squarefree gap 乘积用
基数 \(10^6\) 的多 limb 比较，且由随机小盒与 Python 大整数逐项对照。
最终判别式转为 Python 整数并用 `math.isqrt` 检查。脚本对
non-dominant 扇区只验证尾核在强制 \(m_3\) 范围为空，不枚举其无界
前缀。它不覆盖 \(n_3\le8S-1\) 的无界区域，因此不是 DD 空性或主
不存在性定理的证书。

## 27.23 全局收紧 non-dominant 锥并有限化 \(8S-1\) 层

**状态：denominator-tail 与 non-dominant 加强为“已严格完成”；
\(S=4\) 的遗漏尾层为“有限证书”；\(8S-1\) 层只完成严格有限化，
最终空性仍为“待证”。** 本节没有排除 \(n_3=8S-1\)，而是证明

\[
\boxed{
d_3\ne\max(s_1,s_2,d_3)
\Longrightarrow
n_3\le7S_{12}+2,
}
\tag{DD-nondominant-seven-S-plus-two}
\]

并把新的最高允许层压成

\[
\boxed{
n_3=8S_{12}-1
\Longrightarrow
d_3=\max(s_1,s_2,d_3),\quad S_{12}\le17.
}
\tag{DD-eight-S-minus-one-finite-layer}
\]

所以该层现在是真正的有限原问题切片；这与仅固定 \(S\) 而仍允许
non-dominant prefix surplus 无界的情形不同。依赖第 19、21、25、
27.1–27.2、27.6–27.11、27.18 与 27.22 节。

### denominator-tail 锥统一节省一层

第 25 节已经证明

\[
S\ge5\Longrightarrow m_3\le6S+2.
\]

其原因是若 \(m_3=6S+3\)，primitive tail quotient 必为 1，且
\(\kappa,\kappa+2G\) 都是 \(2,5\)-单位；两单位最小间距与十进制
窗口在 \(2^S>20\) 时矛盾。尚未被该无界论证覆盖的小尺寸只有
\(S=2,3,4\)。第 27.22 节的完整尾表表明前两者分别在
\(m_3=10,17\) 后已经为空；对 \(S=4\)，直接穷尽所有真实有序
denominator 前缀与

\[
QG<\kappa\le10QG,
\qquad
\kappa\mid10^{27}QG,
\qquad
10^{27}\mid\kappa^2(\kappa+2G)
\]

也没有任何 tail row。因此对全部 \(S\ge2\)，统一有

\[
\boxed{m_3\le6S+2.}
\tag{DD-global-tail-six-S-plus-two}
\]

若 \(s_1\) 为最大 surplus，则

\[
s_2+d_3\le2,
\qquad
s_2\ge1-m_2
\]

给出 \(d_3\le1+m_2\le S\)；\(s_2\) 最大时对称。与新的尾长界
合并便得到

\[
n_3=m_3+d_3\le7S+2,
\]

即
\((\mathrm{DD\text{-}nondominant\text{-}seven\text{-}S\text{-}plus\text{-}two})\)。

### \(8S-1\) 层全部进入 dominant 扇区

当 \(S\ge4\) 时，\(8S-1>7S+2\)，所以新边界自动 dominant。
对 \(S=2,3\)，若仍 non-dominant，则 \(d_3\le S\) 分别强迫

\[
m_3\ge13,20,
\]

但第 27.22 节的尾核最大值只有 10、17，同样矛盾。因此当前层对
所有 \(S\ge2\) 都满足

\[
\boxed{d_3=\max(s_1,s_2,d_3),\qquad n_1+n_2\le S+2.}
\tag{DD-eight-S-minus-one-dominant}
\]

### \(S\ge18\) 只剩五进 resonance

第 27.6 节的五进入口在当前层等价于

\[
5^{3S-1}\ge10^{2S+1}.
\]

它在 \(S=18\) 时由 \(5^{53}>10^{37}\) 成立，之后比值每次乘
\(125/100>1\)。因此 \(S\ge18\) 时已有

\[
5\mid b_3,\qquad e_5=q_5,
\]

而第 27.6、27.10 节排除 \(\Delta_5<0\) 与 \(\Delta_5>0\)，只剩
唯一 resonance 正规形

\[
k_5>g_5,
\qquad
3k_5=2m_3+2q_5+g_5+n_5.
\]

若二进最大来自前缀或三个分母全奇，第 27.11 节给出

\[
n_3<\frac{29}{4}S+\frac{20}{3}<8S-1
\]

（第二个不等式在 \(S=18\) 已成立并随 \(S\) 增强）。所以这里只需
考虑 \(b_3\) 二进独大；第 27.8 节又强制二进 resonance。

### \(t_2\ge2\) 退化成 28 个常数核并全部矛盾

沿用第 27.11 节的

\[
\mathscr A_2=2\mathfrak q+\mathfrak g+\mathfrak n,
\qquad
\mathscr A_5=2q_5+g_5+n_5,
\qquad
\Xi=2^{\mathscr A_2}5^{\mathscr A_5}.
\]

对 \(t_2\ge2\)，squarefree gap 给出 \(m_3\ge3S-1\)，而加权
resonance 界为

\[
m_3
<3S+\frac32+\frac a2-\frac12\log_{10}\Xi,
\qquad a=\log_{10}2.
\]

令

\[
j=m_3-(3S-1)\in\mathbf Z_{\ge0}.
\]

由于 \(\Xi\ge2\)，立即有 \(j<5/2\)，所以

\[
j\in\{0,1,2\},
\qquad
\Xi<2\cdot10^{5-2j}.
\tag{DD-eight-S-minus-one-j-Xi-caps}
\]

两条 resonance 同余允许取

\[
T=2^{2S-1}5^{2S}=\frac{10^{2S}}2,
\qquad
\kappa=cT,
\qquad1\le c<20.
\]

具体地，两个相对指数分别为
\((\mathscr A_2+2j)/3\) 与
\((\mathscr A_5+2j-2)/3\)；resonance 同余及
\(\mathscr A_2,\mathscr A_5\ge0\) 保证它们都是非负整数，所以
\(T\mid\kappa\) 而 \(c\) 确为正整数。

若 \(u=v_2(c),v=v_5(c)\)，则精确有

\[
\mathscr A_2=3u-2j,
\qquad
\mathscr A_5=3v-2j+2.
\tag{DD-eight-S-minus-one-core-valuations}
\]

逐个检查 \(1\le c<20\) 与
\((\mathrm{DD\text{-}eight\text{-}S\text{-}minus\text{-}one\text{-}j\text{-}Xi\text{-}caps})\)
得到

\[
\begin{array}{c|c|c|c}
j&c\text{ 的集合}&\rho\text{ 上界}&
\max \Gamma/c\\
\hline
0&1,2,\ldots,19&4000&6400\\
1&2,4,\ldots,18&400000&64\\
2&\varnothing&-&-
\end{array}
\tag{DD-eight-S-minus-one-core-table}
\]

这里

\[
F_-=T\rho,
\qquad
\Gamma=\gcd(cT,G).
\]

事实上 \(v_2(F_-)=v_2(\kappa)+1\)、
\(v_5(F_-)=v_5(\kappa)\)，所以 \(T\mid F_-\) 且 \(\rho\) 为正整数。

\(\rho\) 的常数上界来自

\[
F_-<2\cdot10^{2S+2j+3},
\]

而若写 \(c=2^u5^vw\)、\(\gcd(w,10)=1\)，则

\[
\Gamma\le2^{\mathscr A_2}5^{\mathscr A_5}w.
\]

第 27.18 节比较 \(F_-\) 与 gap 的两个 \(\mu/\nu\) 公式的消元原样
给出

\[
\frac{cT+2G}{\Gamma}\mid\rho Q.
\]

因 \(Q<10^S\) 且左端严格大于 \(cT/\Gamma\)，两行常数表都强迫

\[
10^S
<2\rho\frac{\Gamma}{c}
\le51200000
<10^8,
\]

与当前 \(S\ge18\) 矛盾。因此

\[
\boxed{S\ge18,\quad t_2\ge2\Longrightarrow\text{无候选}.}
\tag{DD-eight-S-minus-one-t2-ge-two-empty}
\]

### \(t_2=1\) 的 45 个尺寸也全部为空

第 27.14 节的一般 surplus 公式在 \(n_3=8S+C\)、\(C=-1\) 时为

\[
s+D_s
>
4S-6-2a-\frac{2(1-a)}3m_3.
\]

利用 \(s+D_s\le2S\)、\(a>301/1000\)，再与第 27.11 节的精确
\(t_2=1\) 上界合并，得到有理窗口

\[
\boxed{
\frac{1000S-3301}{233}
<m_3<
\frac{1000S+661}{267}.
}
\tag{DD-eight-S-minus-one-t2-one-m-window}
\]

两端相容要求

\[
S<\frac{51769}{1700}<31.
\]

逐个取 \(18\le S\le30\) 的整数后，\(S=30\) 没有尺寸，其余只剩

\[
\begin{array}{c|l@{\qquad}c|l}
S&m_3&S&m_3\\
\hline
18&64,65,66,67,68,69&24&89,90,91,92\\
19&68,69,70,71,72,73&25&94,95,96\\
20&72,73,74,75,76,77&26&98,99\\
21&76,77,78,79,80,81&27&102,103\\
22&81,82,83,84&28&107\\
23&85,86,87,88&29&111
\end{array}
\tag{DD-eight-S-minus-one-t2-one-size-kernel}
\]

共 45 个 \((S,m_3)\) 尺寸。它们全部满足 \(m_3\ge3S\)，所以第
27.17 节的 valuation 盒可原样使用：

\[
0\le\mathfrak q,\mathfrak g<4S,
\qquad
0\le\mathfrak n\le14S,
\qquad
0\le\mathscr A_5\le3S+3,
\]

并施加

\[
k_5=\frac{2m_3+\mathscr A_5}{3},
\qquad
\mathfrak f=2m_3+2\mathfrak q+\mathfrak n-\mathfrak g-3,
\]

两个单因子高度以及同一个 combined-height 整数不等式

\[
10^{2m_3}2^{4m_3+6\mathfrak q+3\mathfrak n}5^{\mathscr A_5}
<2^6 11^3 10^{12S+3}.
\]

45 个尺寸共留下 15525 个 valuation rows。对每行再写

\[
\kappa=2^{\mathfrak g+1}5^{k_5}u,
\qquad\gcd(u,10)=1,
\]

并用第 27.17 节已经与 1000 个随机小盒逐项对照的精确 floor-sum
计数器，检查 \(v_2(\kappa+2G)=\mathfrak f\) 所需的奇数倍
\(2^{\mathfrak f-\mathfrak g-1}\) 余因子区间。全部 15525 行的
幸存数仍为零。因此

\[
\boxed{S\ge18,\quad t_2=1\Longrightarrow\text{无候选}.}
\tag{DD-eight-S-minus-one-t2-one-empty}
\]

与其余二进位置及
\((\mathrm{DD\text{-}eight\text{-}S\text{-}minus\text{-}one\text{-}t2\text{-}ge\text{-}two\text{-}empty})\)
合并，得到
\((\mathrm{DD\text{-}eight\text{-}S\text{-}minus\text{-}one\text{-}finite\text{-}layer})\)。

这里的 \(S\le17\)、dominant 与 \(n_1+n_2\le S+2\) 确实同时给出
所有原始块的有限位数盒，但本节没有穷尽这个盒，也没有证明它为空。

### 机械核验（非证明器）

\(S=4,m_3=27\) 的零尾核、五进入口幂比较、\(t_2\ge2\) 的
19、9、0 个常数核与统一 \(51200000\) 界，以及 \(t_2=1\) 的 45 个
尺寸、15525 个 valuation rows 和零余因子幸存数可由

```bash
uv run python scripts/check_dd_2723.py
```

复核。脚本不证明第 27.18 节的 \(\mu/\nu\) 消元，也不枚举
\(S\le17\) 的原始有限盒；无界覆盖来自正文的单调幂比较与整除式。

## 27.24 关闭 \(8S-1\) 层的 \(S=2,3\)

**状态：`有限证书`。** 本节只处理第 27.23 节有限盒中的两个最小
尺寸，不外推到 \(4\le S\le17\)。结论是

\[
\boxed{
n_3=8S_{12}-1
\Longrightarrow
4\le S_{12}\le17.
}
\tag{DD-eight-S-minus-one-only-four-through-seventeen}
\]

因此当前最高层又去掉了两个完整尺寸，但尚未证明为空。依赖第 20–21、
27.1–27.2、27.7、27.22–27.23 节。

### 分扇区与 denominator-tail 核

第 27.23 节已经指出，若 \(S=2,3\) 的当前层 non-dominant，则
\(d_3\le S\) 分别强迫 \(m_3\ge13,20\)。第 27.22 节穷尽的完整
primitive tail 表在 \(m_3=10,17\) 后已经为空，所以两个
non-dominant 扇区无需 numerator 枚举便被排除。

dominant 扇区满足

\[
m_3\ge n_3-5S=3S-1,
\qquad
n_1+n_2\le S+2.
\]

逐项施加

\[
QG<\kappa\le10QG,
\qquad
\kappa\mid10^{m_3}QG,
\qquad
10^{m_3}\mid\kappa^2(\kappa+2G)
\]

得到

\[
\begin{array}{c|r|r|r|r}
S&\text{tail rows}&b_3\text{ 二进独大}&\text{全奇}&
\text{前缀独大或并列}\\
\hline
2&2665&2422&88&155\\
3&126669&119948&1955&4766
\end{array}
\tag{DD-small-eight-S-minus-one-tail-counts}
\]

前缀独大时第 27.7 节要求

\[
n_3<(5+\log_2 10)S-\log_2 10.
\]

右端在 \(S=2,3\) 时分别为
\(10+\log_2 10<15\) 与 \(15+2\log_2 10<23\)，故这些位置为空；
正赋值并列仍违反二进最大赋值必须唯一。对 \(b_3\) 独大位置再施加
\(k_2>g_2\)，与全部全奇 rows 合并后，进入前缀证书的 tail rows
分别为 1929、108434，涉及 74、1619 个有序 denominator 前缀。

### 两素数三状态与判别式证书

对每个 \(b_3\) 二进独大 row，有限核逐项验证

\[
d_3+v_2(b_3)>v_2(Q),
\]

所以 \(e_2=q_2\)，并完整保留 resonance、\(\Delta_2>0\)、
\(\Delta_2<0\) 三种必要赋值式；全奇 rows 则只用无遗漏的

\[
v_2(\mathcal N_{12})\ge m_3+1.
\]

若 \(5\mid b_3\)，同样逐项有
\(d_3+v_5(b_3)>v_5(Q)\)，故施加五进三状态；若 \(5\nmid b_3\)，
不施加任何依赖 gap lock 的五进过滤。这里使用的三状态公式与第
27.22 节完全相同，只把其中的 \(n_3=8S\) 换成当前
\(n_3=8S-1\)。

随后穷尽 \(n_1+n_2\le S+2\) 的所有正十进制块，并依次施加既约性、
dominant 条件、未粗化 squarefree gap 与统一判别式

\[
\mathscr D
=
\left(\kappa GA_{12}10^{d_3}\right)^2
-\kappa(\kappa+2G)Q^2\mathcal N_{12}.
\]

精确计数为

\[
\begin{array}{c|r|r|r|r}
S&\text{digit pairs}&\text{coprime pairs}&
\text{valuation-tail discriminants}&\text{square discriminants}\\
\hline
2&1924074&817860&24396&0\\
3&566651619&228937308&1582338&0
\end{array}
\tag{DD-small-eight-S-minus-one-prefix-counts}
\]

squarefree gap 的大乘积继续使用基数 \(10^6\) 的精确多 limb 比较；
最后 1606734 个非负判别式全部转为 Python 大整数并用 `math.isqrt`
检查，均严格不是平方。因此两个 dominant 扇区也为空，即得
\((\mathrm{DD\text{-}eight\text{-}S\text{-}minus\text{-}one\text{-}only\text{-}four\text{-}through\text{-}seventeen})\)。

### 机械核验（明确有界的有限证书）

上述 tail 核、二进位置、两素数三状态、所有有界 numerator 前缀、
无溢出 squarefree gap 与统一判别式可由

```bash
uv run python scripts/check_dd_2724.py
```

复核。脚本只覆盖 \(S=2,3,n_3=8S-1\)；它不覆盖
\(4\le S\le17\)，也不处理 \(n_3\le8S-2\) 的无界区域。

## 27.25 一个通用 \(F_-\) 大除数与 \(S=4\) 的最低两个尾层

**状态：通用大除数为 `已严格完成`；\(S=4,m_3=11,12\) 的排除为
`有限证书`；本节留下的同尺寸尾层随后由第 27.26–27.28 节关闭。
其余 \(5\le S\le17\) 以及 \(n_3\le8S-2\) 仍为 `待证`。** 本节不会把
两个尾长的空性外推为整个 \(S=4\) 或整个最高层的空性；相邻的
\(m_3=13,14\) 由第 27.26–27.27 节继续处理。依赖第 7、
19、21–22、27.1–27.2、27.7 与 27.22–27.24 节。

### 不依赖 resonance 的通用 \(F_-\) 大除数

第 22 节与第 7 节的 primitive recovery 给出

\[
F_-=\frac{2(\kappa+2G)\mu^2}{G_0},
\qquad
10^{m_3}QG_0=2\kappa\mu\nu.
\]

消去 \(G_0\) 后，第一式等价于

\[
\frac{\mu}{\nu}
=
\frac{F_-\kappa}{10^{m_3}Q(\kappa+2G)}.
\]

另一方面，第 27.1 节的正整数拼接 gap 给出

\[
\frac{\mu}{\nu}
=
\frac{E\kappa^2}{10^{m_3}Q^2(\kappa+G)},
\qquad E\in\mathbf Z_{>0}.
\]

比较两式并清分母，得到对每个 DD 候选都成立的精确恒等式

\[
\boxed{
F_-Q(\kappa+G)
=E\kappa(\kappa+2G).
}
\tag{DD-Fminus-general-divisor-identity}
\]

因此若定义

\[
\mathfrak L_F
=
\frac{\kappa(\kappa+2G)}
{\gcd(\kappa(\kappa+2G),\kappa+G)},
\qquad
L_F=\frac{\mathfrak L_F}{\gcd(\mathfrak L_F,Q)},
\]

则必有

\[
\boxed{L_F\mid F_-.}
\tag{DD-Fminus-general-large-divisor}
\]

这不要求二进或五进 resonance，也不要求达到五进入口。它把第 27.18
节在常数核上使用的大除数机制推广成了任意 DD 尾状态的必要条件。

这个除数还可完全按 \(\gcd(\kappa,G)\) 展开。令

\[
\gamma=\gcd(\kappa,G),
\qquad
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
\gcd(u,v)=1,
\]

并令 \(\delta=\gcd(\gamma,u+v)\)。因为

\[
\gcd\bigl(u(u+2v),u+v\bigr)=1,
\]

所以精确有

\[
\boxed{
\gcd(\kappa(\kappa+2G),\kappa+G)=\gamma\delta,
\qquad
\mathfrak L_F=\frac\gamma\delta u(u+2v)>u^2.
}
\tag{DD-Fminus-gcd-normal-form}
\]

结合第 27.11 节未粗化的小因子上界，可在任意 dominant 位数形状中
使用

\[
L_F
\le F_-
<2\cdot10^{2S+s+D_s+2m_3-n_3+4}.
\]

本节只建立这一必要过滤；它本身尚未给出 DD 的新全局高度界。

### \(S=4,m_3=11\) 只剩一个有序位数形状

现在固定

\[
S=4,
\qquad n_3=8S-1=31.
\]

第 27.23 节的全局尾界与第 21 节的 squarefree gap 先给出

\[
11=3S-1\le m_3\le6S+2=26.
\]

若 \(m_3=11\)，则 \(d_3=20\)。由

\[
d_3\le3S+D_s+2=14+D_s,
\qquad D_s\le2S-2=6,
\]

必须有 \(D_s=6\)。再结合 \(m_1+m_2=4\)、
\(n_1+n_2\le6\) 与所有块非空，除交换两个前缀块外只有

\[
(m_1,m_2;n_1,n_2)
\in
\{(1,3;5,1),(3,1;1,5)\}.
\]

第一个有序形状甚至不需要有限枚举。此时

\[
\frac{\mathcal N_{12}}{A_{12}}
<\frac{a_1b_2^2}{10}+a_2b_1^2
<10^{10}+10^3,
\qquad Q<10^4,
\]

所以

\[
40Q^2\frac{\mathcal N_{12}}{A_{12}}
<4\cdot10^{19}+4\cdot10^{12}
<10^{20},
\]

与第 21 节必要条件
\(10^{20}A_{12}<40Q^2\mathcal N_{12}\) 矛盾。故只需精确检查

\[
\boxed{(m_1,m_2;n_1,n_2)=(3,1;1,5).}
\]

### \(m_3=12\) 只剩三个有序位数形状

若 \(m_3=12\)，则 \(d_3=19\)，从同一个整数位数盒先得到四种形状

\[
\begin{aligned}
&(1,3;4,1),\quad(1,3;5,1),\\
&(3,1;1,4),\quad(3,1;1,5).
\end{aligned}
\]

对第一种形状，刚才的严格估计改为

\[
\frac{\mathcal N_{12}}{A_{12}}<10^9+10^3,
\qquad
40Q^2\frac{\mathcal N_{12}}{A_{12}}
<4\cdot10^{18}+4\cdot10^{12}<10^{19},
\]

仍与 squarefree gap 矛盾。因此有限核只需覆盖

\[
\boxed{
(1,3;5,1),
\quad(3,1;1,4),
\quad(3,1;1,5).
}
\tag{DD-S4-first-two-tail-digit-kernel}
\]

### 两个完整有限证书

在 \(S=4\) 时，第 27.7 节的前缀二进最大界为

\[
(5+\log_2 10)S-\log_2 10<31,
\]

所以前缀独占最大为空，正赋值并列又违反二进最大赋值必须唯一。
剩余 tail rows 中，若 \(b_3\) 二进独大，就逐项恢复二进 gap lock
并保留 resonance、\(\Delta_2>0\)、\(\Delta_2<0\) 三状态；若三个
分母全奇，则使用 \(v_2(\mathcal N_{12})\ge m_3+1\)。五进侧在
\(5\mid b_3\) 时同样逐项恢复 gap lock 与三状态，在
\(5\nmid b_3\) 时不施加入口上才成立的过滤。

对每个固定 \(a_1\) 或 \(a_2\)，未粗化 squarefree gap 是另一个
变量上的开口向上整系数二次不等式。脚本用两侧单调区间的整数二分
精确生成全部正区间，并先与 2000 个随机小盒直接枚举逐项对照；这
不是抽样筛选。结果为

\[
\begin{array}{c|r|r}
&m_3=11&m_3=12\\
\hline
\text{相关 tail rows}&382086&613218\\
\text{二进位置：}b_3\text{ 独大/全奇/前缀或并列}
&359063/5852/17171&594016/6192/13010\\
\text{进入三状态证书的 tail rows}&345643&562830\\
\text{有序 denominator pairs}&8092&16186\\
\text{digit pairs}&6554520000&13766112000\\
\text{coprime pairs}&2745307606&5765369400\\
\text{squarefree-gap pairs}&20178838&834231374\\
\text{valuation-tail discriminants}&694825&138352740\\
\text{模 }2882880\text{ 为平方的判别式}&-&10987773\\
\text{精确平方判别式}&0&0
\end{array}
\tag{DD-S4-first-two-tail-counts}
\]

\(m_3=11\) 的 694825 个非负判别式直接用 Python 大整数平方根检查。
\(m_3=12\) 先用

\[
2882880=2^6\cdot3^2\cdot5\cdot7\cdot11\cdot13
\]

的完整平方剩余表作必要过滤，再把 10987773 个幸存者全部转为 Python
大整数并用 `math.isqrt` 检查；无一为平方。NumPy 只保存本节
\(S=4\) 明确界内可证明不溢出的 \(A_{12},\mathcal N_{12}\) 与模剩余，
最终判别式不经过 `int64`。

因此

\[
\boxed{
S=4,\quad n_3=31
\Longrightarrow
m_3\ge13
\quad\text{且}\quad d_3\le18.
}
\tag{DD-eight-S-minus-one-S4-m-lower-13}
\]

两个证书分别可由

```bash
uv run python scripts/check_dd_2725.py
uv run python scripts/check_dd_2726.py
```

复核。它们不枚举 \(a_3\)，而使用统一判别平方这一必要条件；也不
覆盖 \(S=4\) 的 \(13\le m_3\le26\)、其他 \(S\) 或更低的无界层。

## 27.26 继续排除 \(S=4\) 的 \(m_3=13\) 尾层

**状态：`有限证书`。** 本节只处理
\(S=4,n_3=31,m_3=13\)，不外推到更高尾长、其他 \(S\) 或更低的
无界层。依赖第 21、27.2、27.7、27.22、27.24–27.25 节。

此时 \(d_3=18\)。把

\[
d_3\le3S+D_s+2,
\qquad
m_1+m_2=4,
\qquad
n_1+n_2\le6
\]

在正整数位数盒中逐项解出，先得到十个有序形状

\[
\begin{aligned}
&(1,3;3,1),(1,3;4,1),(1,3;4,2),(1,3;5,1),\\
&(2,2;1,5),(2,2;5,1),\\
&(3,1;1,3),(3,1;1,4),(3,1;1,5),(3,1;2,4).
\end{aligned}
\]

对任意固定的位数形状，直接由 \(A_{12}>a_1 10^{n_2}\) 与
\(A_{12}>a_2\) 有

\[
\frac{\mathcal N_{12}}{A_{12}}
<10^{n_1+2m_2-n_2}+10^{n_2+2m_1}.
\tag{DD-S4-m13-digit-ratio}
\]

对

\[
(1,3;3,1),\qquad(1,3;4,2),\qquad(2,2;5,1)
\]

三种形状，右端都不超过 \(10^8+10^5\)。因 \(Q<10^4\)，

\[
40Q^2\frac{\mathcal N_{12}}{A_{12}}
<4\cdot10^9(10^8+10^5)
<10^{18},
\]

违反未粗化 squarefree gap。故只剩七种形状

\[
\boxed{
\begin{aligned}
&(1,3;4,1),(1,3;5,1),(2,2;1,5),\\
&(3,1;1,3),(3,1;1,4),(3,1;1,5),(3,1;2,4).
\end{aligned}
}
\tag{DD-S4-m13-digit-kernel}
\]

在这七种形状上复用第 27.25 节已经交叉核验的精确二次区间算法、
二进位置、两素数三状态与模平方表，得到

\[
\begin{array}{c|r}
\text{相关 tail rows}&551649\\
\text{二进位置：}b_3\text{ 独大/全奇/前缀或并列}
&546900/1957/2792\\
\text{进入三状态证书的 tail rows}&528622\\
\text{有序 denominator pairs}&23844\\
\text{digit pairs}&27092645100\\
\text{coprime pairs}&10927072288\\
\text{squarefree-gap pairs}&3065318233\\
\text{valuation-tail discriminants}&5088309\\
\text{模 }2882880\text{ 为平方的判别式}&714489\\
\text{精确平方判别式}&0
\end{array}
\tag{DD-S4-m13-counts}
\]

最后 714489 个判别式全部用 Python 大整数与 `math.isqrt` 检查，
无一为平方。因此第 27.25 节的下界再提高一层：

\[
\boxed{
S=4,\quad n_3=31
\Longrightarrow
m_3\ge14
\quad\text{且}\quad d_3\le17.
}
\tag{DD-eight-S-minus-one-S4-m-lower-14}
\]

完整有限证书可由

```bash
uv run python scripts/check_dd_2727.py
```

复核。脚本不枚举 \(a_3\)，也不覆盖 \(14\le m_3\le26\) 或其他
最高层尺寸。

## 27.27 继续排除 \(S=4\) 的 \(m_3=14\) 尾层

**状态：`有限证书`。** 本节只处理
\(S=4,n_3=31,m_3=14\)，不外推到更高尾长、其他 \(S\) 或更低的
无界层。依赖第 21、27.2、27.7、27.22、27.24–27.26 节。

此时 \(d_3=17\)。把与上一节相同的整数位数盒逐项解出，得到十六种
有序形状；其中

\[
(1,3;2,1),\qquad(1,3;3,2),\qquad(2,2;4,1)
\]

由式 \((\mathrm{DD\text{-}S4\text{-}m13\text{-}digit\text{-}ratio})\)
的严格大小估计直接违反 squarefree gap。余下十三种形状为

\[
\boxed{
\begin{aligned}
&(1,3;3,1),(1,3;4,1),(1,3;4,2),(1,3;5,1),\\
&(2,2;1,4),(2,2;1,5),(2,2;5,1),\\
&(3,1;1,2),(3,1;1,3),(3,1;1,4),(3,1;1,5),\\
&(3,1;2,3),(3,1;2,4).
\end{aligned}
}
\tag{DD-S4-m14-digit-kernel}
\]

在这个完整位数核上复用已经交叉核验的精确二次区间、二进位置、
两素数三状态、既约性、squarefree gap、模平方表与统一判别式，得到

\[
\begin{array}{c|r}
\text{相关 tail rows}&379935\\
\text{二进位置：}b_3\text{ 独大/全奇/前缀或并列}
&379590/174/171\\
\text{进入三状态证书的 tail rows}&361023\\
\text{有序 denominator pairs}&23355\\
\text{位数形状--denominator pairs}&101112\\
\text{digit pairs}&40488912720\\
\text{coprime pairs}&15952005956\\
\text{squarefree-gap pairs}&6322749453\\
\text{valuation-tail discriminants}&1077887\\
\text{模 }2882880\text{ 为平方的判别式}&99342\\
\text{精确平方判别式}&0
\end{array}
\tag{DD-S4-m14-counts}
\]

最后 99342 个判别式全部用 Python 大整数与 `math.isqrt` 检查，
无一为平方。因此在这个明确有界的 \(S=4\) 最高层切片中，严格得到

\[
\boxed{
S=4,\quad n_3=31
\Longrightarrow
m_3\ge15
\quad\text{且}\quad d_3\le16.
}
\tag{DD-eight-S-minus-one-S4-m-lower-15}
\]

完整有限证书可由

```bash
uv run python scripts/check_dd_2728.py
```

复核。脚本不枚举 \(a_3\)，也不覆盖 \(15\le m_3\le26\)、其他
最高层尺寸或 \(n_3\le8S-2\) 的无界区域。

## 27.28 关闭 \(S=4,n_3=31\) 的其余尾层

**状态：`有限证书`。** 本节只关闭已经严格有界的
\(S=4,n_3=31,15\le m_3\le26\)；不外推到 \(5\le S\le17\)，
也不处理 \(n_3\le8S-2\) 的无界区域。依赖第 21、27.2、27.7、
27.22 与 27.25–27.27 节。

### \(15\le m_3\le21\) 的流式精确证书

对每个尾长，先机械生成满足

\[
d_3\le3S+|s_1-s_2|+2,
\qquad m_1+m_2=4,
\qquad n_1+n_2\le6
\]

的全部有序位数形状，再用第 27.26 节的严格大小界删除不可能形状。
随后逐个分母块生成完整 primitive denominator-tail 核。对每个短
numerator block，squarefree gap 仍由已经交叉核验的开口向上二次
区间算法精确求出；两素数三状态则由精确 \(2\)-进、\(5\)-进剩余树
流式生成，而每个剩余类最后都会重新代入原状态等式、既约性、严格
squarefree gap、模平方表与统一判别式。这个剩余树不改变候选集合，
只避免物化整个十进制矩形。

七层的固定回归计数为

\[
\begin{array}{c|r|r|r|r|r|r}
m_3&\text{粗/大小删去/保留形状}&\text{tail rows}&\text{eligible rows}
&\text{valuation-tail}&\text{模平方}&\text{精确平方}\\
\hline
15&28/5/23&171086&159257&14150484&1614629&0\\
16&38/3/35&94053&90486&9828&1122&0\\
17&45/0/45&27472&25791&8792&784&0\\
18&45/0/45&9078&7935&112243&30504&0\\
19&45/0/45&1336&1283&70&0&0\\
20&45/0/45&188&179&1887&34&0\\
21&45/0/45&9&9&0&0&0
\end{array}
\tag{DD-S4-m15-through-m21-counts}
\]

其中 \(m_3=15,20,21\) 的全部未过滤计数与独立 Python 完整枚举
逐项一致；可分别用 `--m3 15 --unfiltered`、
`--m3 20 --unfiltered`、`--m3 21 --unfiltered` 复核。C++ 自检还把二次
区间算法、两素数剩余树与多精度整数平方根分别和直接枚举或精确输入
作了交叉核验。最终判别式使用 `boost::multiprecision::cpp_int`，
不经过机器整数截断。

最短的 \(m_3=21\) 层还可独立作一个五进单位性核验。九个 primitive
tail rows 全部为 \(b_3\) 二进独大；五进三态中的 resonance 与
\(\Delta_5<0\) 要求均为负。具体记

\[
\begin{aligned}
R_5&=3k_5+f_5-2m_3-2q_5-2h_5,\\
P_5&=n_3-2m_3-2q_5-h_5+2k_5+g_5,\\
M_5&=f_5+k_5-h_5-g_5-n_3.
\end{aligned}
\]

必要条件是
\(v_5(\mathcal N_{12})=R_5\)、
\(v_5(\mathcal N_{12})-v_5(A_{12})=P_5\) 或
\(v_5(A_{12})=M_5\) 三者之一。由于表中 \(R_5,M_5<0\)，只可能满足
\(v_5(\mathcal N_{12})-v_5(A_{12})=P_5\)。完整九行是

\[
\begin{array}{c|r|r|r|r}
(m_1,m_2)&b_1&b_2&\kappa&(R_5,P_5,M_5)\\
\hline
(1,3)&8&750&500000000&(-26,-1,-25)\\
(1,3)&8&775&156250000&(-18,5,-23)\\
(1,3)&8&910&312500000&(-15,7,-22)\\
(2,2)&91&80&312500000&(-15,7,-22)\\
(2,2)&96&85&625000000&(-15,7,-22)\\
(2,2)&80&91&312500000&(-13,9,-22)\\
(2,2)&85&96&625000000&(-13,9,-22)\\
(3,1)&775&8&156250000&(-14,9,-23)\\
(3,1)&910&8&312500000&(-13,9,-22)
\end{array}
\tag{DD-S4-m21-five-unit-table}
\]

每行恰有一个 \(b_i\) 被 5 整除。若 \(5\mid b_2\)，既约性使
\(a_2b_1\) 为五进单位，而 \(5\mid a_1b_2\)，故
\(v_5(\mathcal N_{12})=v_5(A_{12})=0\)，与表中的
\(P_5\in\{-1,5,7\}\) 矛盾。若 \(5\mid b_1\)，则同理
\(v_5(\mathcal N_{12})=0\)，所以
\(v_5(\mathcal N_{12})-v_5(A_{12})\le0\)，与其余行的
\(P_5=9\) 矛盾。这独立解释了表中 \(m_3=21\) 的
valuation-tail 计数为何为零。

### \(22\le m_3\le26\) 的 primitive tail 核为空

最后，对全部三个有序分母位数拆分与全部真实 \((b_1,b_2)\)，一次
分解 \(QG\) 并穷尽

\[
QG<\kappa\le10QG,
\qquad
\kappa\mid10^{m_3}QG,
\qquad
10^{m_3}\mid\kappa^2(\kappa+2G)
\]

的精确 divisor tree。对 \(m_3=22,23,24,25,26\)，primitive
denominator-tail rows 逐层全为零。因此第 27.27 节剩余的全部尾长
已经穷尽，得到

\[
\boxed{
S=4,\quad n_3=31
\Longrightarrow
\text{无 DD 候选。}
}
\tag{DD-eight-S-minus-one-S4-empty}
\]

编译、全量复核与高尾空核命令为

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  scripts/check_dd_2729.cpp -o /tmp/check_dd_2729_cpp
/tmp/check_dd_2729_cpp --self-check --m3-min 15 --m3-max 21 \
  --expect-baseline
uv run python scripts/check_dd_2729.py --empty-high-only
```

其中 C++ 程序固定断言七层的形状、位置与全部计数，Python 高尾脚本
固定断言五层都没有 primitive tail row。可选的逐层 Python 实现还会
使用四角凸性、valuation height box 与通用 \(L_F\mid F_-\) 作严格
前置过滤；这些过滤不参与上面 C++ 主证书的完备性。

## 27.29 排除 \(S=5\) 的 \(22\le m_3\le32\) 高尾层

**状态：`有限证书`。** 本节只处理最高层中的
\(S=5,n_3=39,22\le m_3\le32\)。它不外推到该尺寸的
\(14\le m_3\le21\)、其余 \(6\le S\le17\) 或
\(n_3\le8S-2\) 的无界区域。依赖第 21、27.2、27.7、27.22、
27.25 与 27.28 节。

第 27.23 节的全局尾界与 squarefree gap 先给出

\[
14=3S-1\le m_3\le6S+2=32.
\tag{DD-S5-tail-range}
\]

对每个固定尾长，脚本机械生成满足

\[
d_3\le3S+|s_1-s_2|+2,
\qquad m_1+m_2=5,
\qquad n_1+n_2\le7
\]

的全部有序位数形状。对 \(22\le m_3\le26\)，粗位数盒都恰有
84 种形状，严格大小界不再删去整种形状。随后穷尽四个有序分母位数
拆分的全部 324000 个真实 \((b_1,b_2)\)，生成完整 primitive
denominator-tail 核，并复用第 27.28 节的精确二次区间、两素数剩余
树、既约性、严格 squarefree gap、模平方表与统一判别式。

由于这里 \(S=5\)，\(\mathcal N_{12}\) 已可能超过 `uint64_t`。证书从
赋值与 squarefree-gap 阶段起使用 `unsigned __int128`，最终再精确
转换为 `boost::multiprecision::cpp_int`；内置自检把 128 位剩余树和
转换分别与直接枚举、分高低 limb 的多精度整数逐项对照。结果为

\[
\begin{array}{c|r|r|r|r|r|r|r}
m_3&\text{tail}&\text{eligible}&\text{denominator}&
\text{squarefree pairs}&\text{valuation-tail}&\text{模平方}&\text{精确平方}\\
\hline
22&136692&132546&62213&724662728226&14434&3022&0\\
23&23052&21862&12626&149533255023&9653&2354&0\\
24&3742&3349&2594&30667990956&464987&40494&0\\
25&401&397&344&3588054173&0&0&0\\
26&35&35&35&371671617&84&21&0
\end{array}
\tag{DD-S5-m22-through-m26-counts}
\]

五层的 primitive rows 全部处于 \(b_3\) 二进独大位置；程序固定断言
形状数、位置分布及表中全部计数。所有模平方幸存者都用多精度整数
重新计算判别式并作精确整数平方根检查，无一为平方。

对更高的六层，不再需要 numerator 前缀。对相同 324000 个真实
分母对，一次穷尽 \(10^{32}QG\) 在 \(QG<\kappa\le10QG\) 中的
divisor tree，并按

\[
10^{m_3}\mid\kappa^2(\kappa+2G)
\]

的精确二进、五进赋值区间同时回收每一层。得到

\[
\begin{array}{c|rrrrrr}
m_3&27&28&29&30&31&32\\
\hline
\text{primitive tail rows}&0&0&0&0&0&0
\end{array}
\tag{DD-S5-m27-through-m32-empty-tail}
\]

因此这个明确有界尺寸的剩余范围严格缩为

\[
\boxed{
S=5,\quad n_3=39
\Longrightarrow
14\le m_3\le21,
\qquad18\le d_3\le25.
}
\tag{DD-eight-S-minus-one-S5-m14-through-m21-only}
\]

完整复核命令为

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  scripts/check_dd_2730.cpp -o /tmp/check_dd_2730_cpp
/tmp/check_dd_2730_cpp --self-check --expect-baseline --threads 12
```

该命令默认复核 \(m_3=22,\ldots,26\) 的全部前缀证书以及
\(m_3=27,\ldots,32\) 的空 tail 核。它没有排除 \(S=5\) 的最低八个
尾长，因此不是整个 \(S=5\) 尺寸、DD 分支或主命题的证书。

## 27.30 排除 \(S=5\) 的最低尾层 \(m_3=14\)

**状态：`有限证书`。** 本节只处理
\(S=5,n_3=39,m_3=14\)。它不外推到 \(15\le m_3\le21\)、其余
最高层尺寸或 \(n_3\le8S-2\) 的无界区域。依赖第 21、27.2、27.7、
27.22、27.25 与 27.29 节。

此时 \(d_3=25\)。把

\[
d_3\le3S+|s_1-s_2|+2,
\qquad m_1+m_2=5,
\qquad n_1+n_2\le7
\]

在正整数位数盒中逐项解出，粗核只有

\[
(1,4;6,1),qquad(4,1;1,6).
\]

第一种形状由第 27.26 节同型的严格 ratio 上界直接违反 squarefree
gap。因此唯一需要有限核验的有序形状是

\[
\boxed{(m_1,m_2;n_1,n_2)=(4,1;1,6).}
\tag{DD-S5-m14-digit-kernel}
\]

### 四个 numerator-free 必要过滤

完整 primitive denominator-tail 核先有 6207930 行，其中 5828153 行
通过二进位置与两素数 gap-lock 的必要状态。对每个固定分母，记

\[
A_{12}=10^6a_1+a_2,
\qquad
\mathcal N_{12}=(a_1b_2)^2+(a_2b_1)^2.
\]

第一，函数 \(\mathcal N_{12}/A_{12}\) 对 \(a_1,a_2\) 分别严格凸。
例如

\[
\frac{\partial^2}{\partial a_1^2}
\frac{b_2^2a_1^2+b_1^2a_2^2}{10^6a_1+a_2}
=
\frac{2a_2^2(b_2^2+10^{12}b_1^2)}{(10^6a_1+a_2)^3}>0,
\]

另一变量同理。所以 digit rectangle 上的最大值必在四个角；四角
都不满足严格 squarefree gap 时可以删除整个 denominator row。该
必要过滤留下 1378380 行。

第二，把二、五进三状态分别与

\[
0\le v_p(A_{12})\le A_p^{\max},
\qquad
0\le v_p(\mathcal N_{12})\le N_p^{\max}
\]

的精确十进制高度盒求交，留下 1123254 行。

第三，第 27.25 节的通用大除数与当前形状的小因子上界给出

\[
L_F\mid F_-,
\qquad
L_F<2\cdot10^{13}.
\tag{DD-S5-m14-large-divisor-bound}
\]

精确检查这个严格不等式后只剩 8495 行。

第四，还可在不枚举 numerator 的情况下利用既约性。对
\(p\in\{2,5\}\)，令

\[
e_1=v_p(b_1),\qquad e_2=v_p(b_2),
\qquad n=v_p(\mathcal N_{12}),\qquad a=v_p(A_{12}).
\]

若 \(e_1>0\)，则 \(v_p(a_1)=0\)；若 \(e_2>0\)，则
\(v_p(a_2)=0\)。因此三状态只可能与下列可达赋值超集相交：

\[
\begin{array}{c|c|c}
(e_1,e_2)&n&a\\
\hline
e_1>0, e_2=0&0&0\le a\le A_p^{\max}\\
e_1=0, e_2>0&0&0\\
e_1,e_2>0, e_1\ne e_2&2\min(e_1,e_2)&0\\
e_1=e_2>0, p=2&2e_1+1&0\\
e_1=e_2>0, p=5&2e_1\le n\le N_5^{\max}&0
\end{array}
\tag{DD-S5-m14-denominator-unit-box}
\]

这里二进相等情形使用奇平方和除去公共幂后恰为 \(2\bmod8\)；五进
相等情形只取允许继续消去的安全上包络，不把下界误写成等式。把
二进、五进三状态依次与这个超集求交，8495 行先缩到 611 行，再缩到
恰 75 行，分布在 49 个真实 denominator pairs 中。

### 完整 prefix 证书

对这 75 条 primitive tails，程序用第 27.29 节已经自检的 128 位
两素数剩余树生成全部真实前缀，并逐项重新验证既约性、严格
squarefree gap 与原三状态。固定计数为

\[
\begin{array}{c|r}
\text{相关 primitive tail rows}&6207930\\
\text{二进位置：}b_3\text{ 独大/全奇/前缀或并列}
&5904517/72157/231256\\
\text{进入三状态的 tail rows}&5828153\\
\text{四角/valuation box/}L_F\text{ 后}
&1378380/1123254/8495\\
\text{二进/五进单位性盒后}&611/75\\
\text{原始 denominator pairs/最终 denominator pairs}&80991/49\\
\text{digit pairs}&396900000\\
\text{coprime pairs}&222531424\\
\text{squarefree-gap pairs}&7930779\\
\text{valuation-tail pairs}&0
\end{array}
\tag{DD-S5-m14-counts}
\]

最后一行表明：所有 squarefree-gap 前缀都不满足 75 条 tail 的完整
二、五进三状态交集，因而无需进入判别式平方检查。证书的随机小盒
自检还会直接枚举既约前缀，确认 denominator-unit height box 从不
删除一个实际满足对应 \(p\)-进状态的行。

因此第 27.29 节的剩余范围再缩一层：

\[
\boxed{
S=5,\quad n_3=39
\Longrightarrow
15\le m_3\le21,
\qquad18\le d_3\le24.
}
\tag{DD-eight-S-minus-one-S5-m15-through-m21-only}
\]

完整有限证书可由

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  scripts/check_dd_2731.cpp -o /tmp/check_dd_2731_cpp
/tmp/check_dd_2731_cpp --self-check --threads 12 --expect-baseline
```

复核。它固定断言上述所有阶段计数，只覆盖这一明确有界的单层。

## 27.31 排除 \(S=5\) 的下一尾层 \(m_3=15\)

**状态：`有限证书`。** 本节只处理
\(S=5,n_3=39,m_3=15\)，不外推到其余尾长、其余最高层尺寸或
\(n_3\le8S-2\) 的无界区域。依赖第 21、27.2、27.7、27.22、
27.25、27.29 与 27.30 节。

此时 \(d_3=24\)。机械求解同一严格位数盒，粗核有 4 种形状，
严格大小界删除 1 种，恰留下

\[
(m_1,m_2;n_1,n_2)
\in\{(1,4;6,1),(4,1;1,5),(4,1;1,6)\}.
\tag{DD-S5-m15-digit-kernel}
\]

对每个形状，程序重新生成与分母拆分匹配的完整 primitive
denominator-tail 核，并复用第 27.30 节的四类 numerator-free 必要
过滤。角点检验中的 \(10^{24}A_{12}\) 全程用 128 位无符号整数；
valuation height box 使用该形状自己的严格上界

\[
A_{12}<10^{n_1+n_2},\qquad
\mathcal N_{12}<10^{2(n_1+m_2)}+10^{2(n_2+m_1)}.
\]

通用大除数保留严格条件

\[
L_F<2\cdot10^{2S+s_1+s_2+|s_1-s_2|+2m_3-n_3+4},
\]

其三个指数依次为 \(15,13,15\)。最后分别把二进、五进三状态与
第 27.30 节的 denominator-unit reachable box 求交。逐形状固定
计数为

\[
\begin{array}{c|r|r|r|r|r|r|r}
(m_1,m_2;n_1,n_2)&\text{tail}&\text{eligible}&\text{corner}&
\text{height}&L_F&2\text{-unit}&5\text{-unit}\\
\hline
(1,4;6,1)&4143226&3970657&1294195&1284602&145896&15971&1404\\
(4,1;1,5)&4037587&3858105&967130&700622&3977&436&17\\
(4,1;1,6)&4037587&3858105&2808958&2728920&259926&34418&5499
\end{array}
\tag{DD-S5-m15-filter-counts}
\]

因此五类必要过滤后共有 \(1404+17+5499=6920\) 条 primitive
tails。对其全部真实前缀，128 位两素数剩余树先生成候选，随后逐项
重新验证既约性、严格 squarefree gap 和原始二、五进三状态；每个
状态下的每条 tail 都分别进入模平方筛与多精度精确判别式。完整计数
为

\[
\begin{array}{c|r|r|r|r|r|r|r|r}
(m_1,m_2;n_1,n_2)&\text{den}&\text{digit}&\text{coprime}&
\text{gap}&\text{valuation-tail}&\text{mod}&\text{nonnegative}&\text{square}\\
\hline
(1,4;6,1)&224&1814400000&1055554100&332164802&18036040&4270550&4270550&0\\
(4,1;1,5)&12&9720000&4689000&167566&0&0&0&0\\
(4,1;1,6)&1035&8383500000&4589789640&1571805173&16890624&3861540&3861540&0
\end{array}
\tag{DD-S5-m15-prefix-counts}
\]

这里 `den` 是五进单位性过滤后仍非空的真实 denominator pairs 数。
两个非空判别式核的所有模筛幸存者都非负，但精确整数平方根检查仍
无一为平方。故第 27.30 节的范围再缩为

\[
\boxed{
S=5,\quad n_3=39
\Longrightarrow
16\le m_3\le21,
\qquad18\le d_3\le23.
}
\tag{DD-eight-S-minus-one-S5-m16-through-m21-only}
\]

完整有限证书可由

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  -Wall -Wextra -Wconversion -Wshadow \
  scripts/check_dd_2732.cpp -o /tmp/check_dd_2732_cpp
/tmp/check_dd_2732_cpp --self-check --threads 12 --expect-baseline
```

复核。程序固定断言位数核、每个形状的全部过滤阶段、位置分布、前缀
计数和最终零平方；独立完整实现也逐项复现了三行前缀计数。本节仍
没有关闭整个 \(S=5\) 尺寸、DD 分支或主命题。

## 27.32 排除 \(S=5\) 的尾层 \(m_3=16\)

**状态：`有限证书`。** 本节只处理
\(S=5,n_3=39,m_3=16\)，不外推到其余尾长或更低的无界 DD 层。
依赖第 21、27.2、27.7、27.22、27.25 与 27.29–27.31 节。

此时 \(d_3=23\)。严格位数核从 10 个粗形状中删除 3 个，留下

\[
\begin{split}
(m_1,m_2;n_1,n_2)\in\{&
(1,4;5,1),(1,4;6,1),(3,2;1,6),\\
&(4,1;1,4),(4,1;1,5),(4,1;1,6),(4,1;2,5)\}.
\end{split}
\tag{DD-S5-m16-digit-kernel}
\]

程序逐形状重新生成完整 primitive denominator-tail 核，并应用第
27.31 节相同的 128 位四角 gap、shape-specific valuation height、
通用 \(L_F\) 大除数以及二/五进 denominator-unit 必要过滤。这里
四角不等式严格按

\[
10^{23}A_{12}<40Q^2\mathcal N_{12}
\]

检查；\(L_F\) 的严格上界指数按形状依次为
\(15,17,15,13,15,17,15\)。逐形状五进单位性过滤后分别留下

\[
832, 45745, 1262, 3, 3145, 60659, 1356
\]

条 primitive tails，总计 113002 条。全部过滤阶段的汇总计数为

\[
\begin{array}{c|r}
\text{primitive tail / eligible}&22660597/22189846\\
\text{位置：}b_3\text{ 独大/全奇/前缀或并列}&22505510/61686/93401\\
\text{corner / height / }L_F&11941591/10410835/2921591\\
\text{二进单位性 / 五进单位性}&318339/113002\\
\text{最终 shape--denominator jobs}&23656
\end{array}
\tag{DD-S5-m16-filter-counts}
\]

对所有幸存前缀，证书复用已经自检的两素数剩余树，并重新验证原始
既约性、严格 gap 与每个二/五进三状态；随后对每个 prefix--tail 对
分别执行模平方筛和多精度精确平方根。七形状汇总得到

\[
\begin{array}{c|r}
\text{digit / coprime / squarefree-gap pairs}
&185509683000/108389174150/69712689215\\
\text{valuation-tail pairs}&141826212\\
\text{modular / nonnegative discriminants}&22535973/22535973\\
\text{exact square discriminants}&0
\end{array}
\tag{DD-S5-m16-prefix-counts}
\]

源码还固定断言七个形状各自的全部过滤、位置与前缀计数，而不仅是
上述汇总；独立实现逐形状复现了完整结果。于是当前范围缩为

\[
\boxed{
S=5,\quad n_3=39
\Longrightarrow
17\le m_3\le21,
\qquad18\le d_3\le22.
}
\tag{DD-eight-S-minus-one-S5-m17-through-m21-only}
\]

完整复核命令为

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  -Wall -Wextra -Wconversion -Wshadow \
  scripts/check_dd_2733.cpp -o /tmp/check_dd_2733_cpp
/tmp/check_dd_2733_cpp --self-check --threads 12 --expect-baseline
```

该证书已经完成严格编译、两次固定基线全量运行与独立代码审计；七个
形状的精确平方判别式均为零。它仍没有关闭整个 \(S=5\) 尺寸、DD
分支或主命题。

---

# 27.33 2026-08-13 后续合并进展

## 第二部分：最高层的有限闭合

### 4. \(S=5,n_3=39,m_3=17\) 的完整证书

本节对

\[
S=5,\qquad n_3=39,\qquad m_3=17
\]

进行了完整有限证书。

#### 4.1 denominator-tail 先行

严格位数盒先产生有限 digit shapes，再依次施加：

- tail window；
- tail divisibility；
- 二进 denominator-position；
- 四角凸性；
- 二、五进 valuation height box；
- 通用大除数；
- denominator-unit 可达盒。

候选规模被大幅压缩。

#### 4.2 五进单状态化

幸存 tail 中，五进状态被压成 \(P_5\) 或 \(R_5\) 两种，而且不再存在 free-five tail。

#### 4.3 short-block Hensel + CRT

固定 denominator-tail row 和短 numerator block 后，把长 numerator block 写成单变量 \(x\)：

\[
A_{12}=\alpha x+\beta,
\qquad
\mathcal N_{12}=(cx)^2+d^2.
\]

对 \(p=2,5\) 做精确 Hensel 提升，再用 CRT 合并，并对真实整数候选重新检查 valuation。

最终完整判别平方检查得到零解，因此

\[
\boxed{
S=5,\ n_3=39,\ m_3=17
\Longrightarrow
\text{无 DD 候选}.
}
\]

---

### 5. 一次关闭 \(S=5\) 的全部剩余 tail

本节把

\[
17\le m_3\le21
\]

全部统一处理。

使用同一 denominator-tail 核：

\[
QG<\kappa\le10QG,
\]

\[
\kappa\mid10^{m_3}QG,
\]

\[
10^{m_3}\mid\kappa^2(\kappa+2G),
\]

配合 numerator-free 的 valuation / denominator-unit / large-divisor 条件。

随后使用精确 Hensel–CRT 生成 numerator 前缀，并最终检查判别式

\[
\mathscr D
=
\left(\kappa G A_{12}10^{d_3}\right)^2
-\kappa(\kappa+2G)Q^2\mathcal N_{12}.
\]

所有层均得到

\[
\#\{\text{exact-square discriminants}\}=0.
\]

于是

\[
\boxed{
S=5,\qquad n_3=39
\Longrightarrow
\text{无 DD 候选}.
}
\]

到这里，\(8S-1\) 最高层只剩 \(S\ge6\) 的问题。

---

## 第三部分：从斜率 8 到 7.75

### 6. gcd-normal form

本节引入非常关键的正规化：

\[
\gamma=(\kappa,G),
\qquad
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1.
\]

由 tail recovery 得

\[
b_3=vt,
\qquad
ut=10^mQ,
\]

并且

\[
\boxed{
Q<\frac uv\le10Q.
}
\]

通用恒等式

\[
F_-Q(\kappa+G)=E\kappa(\kappa+2G)
\]

约去 \(\gamma\) 后变成

\[
F_-Q(u+v)=E\gamma u(u+2v).
\]

由于

\[
\gcd(u(u+2v),u+v)=1,
\]

得到

\[
\boxed{
u(u+2v)\mid F_-Q.
}
\]

继续令

\[
d_0=(u,Q),
\qquad
u=d_0r,
\qquad
Q=d_0q,
\]

则

\[
r\mid10^m,
\]

所以

\[
\boxed{
r=2^A5^B.
}
\]

这说明 tail quotient 的 reduced numerator 具有强烈的 \(2,5\)-smooth 性质。

---

### 7. 全局解析锥

这一正规化与二、五进 resonance、高度上界结合，得到 prefix-uniform 解析界

\[
\boxed{
n_3<
\frac{31}{4}S+\frac{6581}{960}.
}
\]

其主斜率为

\[
\frac{31}{4}=7.75.
\]

这个结论不依赖有限 numerator 枚举。

#### 7.1 高锥中的五进结构

若候选进入该高锥，则最终被强制到：

\[
5\mid b_3,
\]

\[
k_5>g_5,
\]

\[
\boxed{
3k_5
=
2m+2q_5+g_5+n_5.
}
\]

也就是唯一五进 resonance 正规形。

#### 7.2 二进结构

高锥同时强制第三分母成为二进 unique maximum，并进入二进 resonance。

于是危险候选被压到“双 resonance + \(b_3\) 二进独大”的极小状态族。

---

### 8. 整个 \(n_3=8S-1\) 最高层关闭

同一文件还完成了更强的整数层结论：

\[
\boxed{
n_3=8S-1
\quad\text{在 DD 中整层为空}.
}
\]

主要分成 \(t_2\ge2\) 与 \(t_2=1\)。

#### 8.1 \(t_2\ge2\)

解析条件把问题压到极少数低 \(S\) 端点，随后 denominator-only 有限证书完成排除。

#### 8.2 \(t_2=1\)

得到 exact 2-adic resonance 方程

\[
5^{k_5}u+x=2^h z,
\qquad z\text{ odd}.
\]

对余因子 \(u\) 的所有解数使用精确 `floor_sum` 计算，不逐个遍历巨大区间。

最终：

- \(S\ge11\) 无格点；
- \(6\le S\le10\) 只留下 667 个格点对；
- 恢复真实 denominator-tail 后仅剩 6 个核；
- 这 6 个核由模 \(3\)、模 \(7\)、五进 valuation 与 reducedness 逐个排除。

因此

\[
\boxed{
n_3\le8S-2.
}
\]

这一步完成了原“最高层”方向的任务。后面继续逐层枚举已经不再值得。

---

## 第四部分：\(7\sim7.75\) 锥与唯一 S-unit funnel

### 9. 五进侧只剩一个 resonance

在 \(n>7S+O(1)\) 的无界区域，五进侧被统一为

\[
\boxed{
5\mid b_3,
\qquad
k_5>g_5,
\qquad
3k_5=2m+2q_5+g_5+n_5,
}
\]

并且

\[
\boxed{
v_5(F_-)=k_5.
}
\]

其余五进状态全部降到 slope \(7\) 以下。

---

### 10. 二进位置分层

二进 denominator-position 与五进 resonance 联立后得到：

#### 10.1 三分母全奇

\[
n<6.822584\,S+O(1).
\]

#### 10.2 低位 prefix \(b_2\) 二进独大

\[
n<6.462\,S+O(1).
\]

#### 10.3 高位 prefix \(b_1\) 二进独大

\[
n<
7.215055876\ldots S+O(1).
\]

#### 10.4 第三分母 \(b_3\) 二进独大

只剩两个核心：

\[
t_2=1
\qquad\text{或}\qquad
t_2\ge2.
\]

其中

\[
\boxed{
t_2\ge2
\Longrightarrow
n<7.5S+5.951545\ldots
}
\]

因此真正的顶部 \(7.5\sim7.745\) 锥只可能来自 \(t_2=1\)。

---

### 11. \(t_2=1\) 的 S-unit phase

此时可写

\[
u=2\cdot5^TU,
\qquad
v=V,
\]

其中

\[
(UV,10)=1,
\qquad
(U,V)=1.
\]

令

\[
H=v_2(5^TU+V),
\]

\[
Z=\frac{5^TU+V}{2^H}.
\]

得到核心相位方程

\[
\boxed{
2^HZ-5^TU=V.
}
\]

同时 tail window 化成

\[
\boxed{
\frac1{5Q}
\le
\frac{V}{5^TU}
<
\frac2Q.
}
\]

因此

\[
\Lambda
=
H\log2-T\log5+\log(Z/U)
=
\log\left(1+\frac{V}{5^TU}\right)
\]

满足

\[
10^{-S-1}
<
\Lambda
<
20\cdot10^{-S}.
\]

这是一条极深的 real S-unit 近似。

---

### 12. denominator prime-flow

奇素数的来源被分成两个完全不同的通道。

#### 12.1 \(p\mid V\)

它只能来自前两 denominator 的 valuation imbalance，并且

\[
\boxed{
p\mid V
\Longrightarrow
p\equiv1\pmod4.
}
\]

而且

\[
V
\mid
\frac{b_1b_2}{(b_1,b_2)^2}.
\]

所以 \(V\) 是纯粹的 split-prime imbalance 载体。

#### 12.2 \(p\mid U\)

则前两 denominator 在 \(p\) 处必须 equal valuation，额外素数来源于 \(Q\) 的 cancellation：

\[
\boxed{
p\mid U
\Longrightarrow
v_p(b_1)=v_p(b_2).
}
\]

在危险顶部且 \(H\ge2\) 时，模 \(4\) 进一步给出

\[
\boxed{
U\equiv3\pmod4.
}
\]

所以 \(U\) 至少携带一个 \(3\bmod4\) 的 inert cancellation prime。

---

### 13. stability inequality 与 excess 载体

定义

\[
a=\log_{10}2,
\qquad
b=1-a.
\]

可得

\[
\boxed{
n<c_*S+C_*-\Pi,
}
\]

其中

\[
c_*=
\frac{10+8a}{1+2a}
=
7.745178103490709\ldots,
\]

且缺陷项 \(\Pi\) 的所有系数均严格为正。

更关键的是：

\[
\boxed{
V>10^{\,n-7S-O(1)}.
}
\]

所以每一单位 \(n-7S\) 的 excess 都必须由指数级大的 denominator imbalance \(V\) 支付，而且这些素数全部是 Gaussian split primes。

如果存在序列满足

\[
\frac nS\to c_*,
\]

那么所有缺陷变量都必须趋于最小，整个系统被逼到唯一极限射线。

---

## 第五部分：Schmidt Subspace Theorem 关闭 \(>7\) dominant 锥

### 14. 十进制 pinning：\(\kappa\asymp Q^2\)

一个极其有效但此前未充分利用的恒等式是

\[
\frac QG
=
\frac{10^{m_2}}{b_2}
+
\frac1{b_1}.
\]

因为 \(b_2\) 有 \(m_2\) 位，

\[
1<\frac QG\le11.
\]

结合

\[
QG<\kappa\le10QG
\]

得到

\[
\boxed{
\frac{Q^2}{11}
<
\kappa
<
10Q^2.
}
\]

所以 \(\kappa\) 其实被 decimal concat 锁在 \(Q^2\) 的常数倍窗口。

---

### 15. 通用局部公式

对任意素数 \(p\)，记

\[
e=v_p(E),\quad
q=v_p(Q),\quad
k=v_p(\kappa),
\]

\[
h=v_p(\kappa+G),
\quad
f=v_p(\kappa+2G).
\]

由 primitive recovery 消元得到

\[
\boxed{
v_p(F_-)=e+k+f-h-q.
}
\]

若 gap-lock 给出 \(e=q\)，则

\[
\boxed{
v_p(F_-)=k+f-h.
}
\]

这条公式不需要预先假设 resonance。

---

### 16. 所有 slope \(>7\) 被压入唯一 funnel

进一步分类后，任何渐近 slope \(>7\) 的 DD 候选都必须进入：

\[
\boxed{
5\text{-resonance}
+
b_3\text{ 二进 unique}
+
t_2=1
+
2\text{-resonance}.
}
\]

并具有

\[
Q=Uq,
\]

\[
5^TU+V=2^HZ,
\]

\[
\frac1{5Q}
\le
\frac{V}{5^TU}
<
\frac2Q.
\]

---

### 17. 固定目标 Subspace Theorem

取

\[
X=2^HZ,
\qquad
Y=5^TU,
\qquad
X-Y=V.
\]

考察射影点

\[
[X:Y]\in\mathbf P^1(\mathbf Q)
\]

和 places

\[
\{2,5,\infty\},
\]

使用固定线性型

\[
X,\qquad Y,\qquad X-Y.
\]

固定目标 Schmidt Subspace Theorem 强迫：

\[
\boxed{
\liminf_{S\to\infty}
\frac{\log_{10}U+\log_{10}Z}{S}
\ge1.
}
\]

将其代回 stability inequality，得到最终 funnel：

\[
\boxed{
\limsup
\frac nS
\le
6.308883577618031\ldots
<7.
}
\]

其他 dominant 分支最坏也只有

\[
6.861353116\ldots<7.
\]

因此 dominant 整体满足渐近 slope \(<7\)。

当时 non-dominant 仍有

\[
n\le7S+4.
\]

所以已经可以推出存在非有效 \(S_0\)，使 sufficiently large \(S\) 时

\[
n\le7S+4,
\]

并存在某个绝对有限常数 \(C_{DD}\)：

\[
n\le7S+C_{DD}.
\]

---

## 第六部分：全局 tail slope 从 6 降到 5，frontier 降到 6.3089

### 18. 全局 tail quotient

定义

\[
\boxed{
\mathscr T
=
\frac{\kappa^2(\kappa+2G)}{10^m}
\in\mathbf Z_{>0}.
}
\]

纯大小给出

\[
\log_{10}\mathscr T
<
6S+O(1)-m.
\]

令

\[
D=(\kappa,\kappa+2G),
\]

\[
x=\frac{\kappa+2G}{D},
\qquad
y=\frac{\kappa}{D},
\qquad
z=x-y=\frac{2G}{D}.
\]

则

\[
(x,y)=1
\]

且

\[
\frac1{5Q}
\le
\frac zy
<
\frac2Q.
\]

定义删除全部 \(2,5\) 因子的 rough core

\[
R=
\operatorname{core}_{10}(x)
\operatorname{core}_{10}(y).
\]

对 \([x:y]\) 再次应用固定目标 Schmidt Subspace Theorem，得到

\[
\boxed{
\liminf\frac{\log_{10}R}{S}\ge1.
}
\]

另一方面

\[
R\le\mathscr T.
\]

因此

\[
\boxed{
\limsup\frac{m_3}{S}\le5.
}
\]

更定量地，对任意 \(\eta>0\)，存在 \(C_\eta\)：

\[
m_3\le(5+\eta)S+C_\eta.
\]

这是一个全 DD 结论，不要求 numerator、dominant 或 resonance。

---

### 19. non-dominant 直接下降到 slope 6

已有 non-dominant

\[
d\le S.
\]

因此

\[
n=m+d
\]

立即给出

\[
\boxed{
\limsup_{\text{non-dominant}}
\frac nS
\le6.
}
\]

原来的 slope-7 non-dominant frontier 至此消失。

---

### 20. 全 DD 的统一 asymptotic frontier

继续把 tail collapse 与状态分类结合，最终得到

\[
\boxed{
\limsup_{\rm DD}
\frac{n_3}{S_{12}}
\le
6.308883577618\ldots.
}
\]

这个数字成为新的全局 asymptotic frontier。

如果有序列逼近该数值，则必须满足唯一比例模型。

记

\[
c_{38}=6.308883577618\ldots.
\]

则：

\[
\frac mS
\to
2.808883577618\ldots,
\]

\[
\frac dS\to\frac72,
\]

\[
\frac{\log_{10}U}{S}
\to
0.691116422382\ldots,
\]

\[
\frac{\log_{10}Z}{S}
\to
0.308883577618\ldots,
\]

\[
\frac{\log_{10}q}{S}
\to
0.308883577618\ldots,
\]

\[
\frac TS
\to
1.872589051745\ldots,
\]

\[
\frac HS
\to
5.617767155236\ldots.
\]

而且

\[
5^TU=10^{2S+o(S)},
\]

\[
2^HZ=10^{2S+o(S)},
\]

\[
V=10^{S+o(S)}.
\]

digit shape 也极端刚性：

\[
(m_1,m_2;n_1,n_2)
=
(o(S),S-o(S);S-o(S),o(S))
\]

（可能需要交换前两块，具体取向按该 frontier 的规范化）。

因此 \(6.3089\) 已经对应一个唯一 asymptotic geometry。

---

### 21. frontier exact identity

令

\[
X=2^HZ,
\qquad
Y=5^TU.
\]

则已有

\[
X-Y=V.
\]

通用恒等式在 frontier 正规化后变成

\[
\boxed{
F_-\,q\,(X+Y)
=
4E\gamma\,2^H5^T Z.
}
\]

此时

\[
q,\quad Z
\]

恰好都承担约

\[
0.30888358\,S
\]

的 rough 高度。

这最初把 bottleneck 指向了 \(\gcd(q,Z)\) 以及它们的 factor allocation。

---

## 第七部分：从“继续压斜率”转向绝对有限性

### 22. surplus simplex 收缩为 11 个固定模式

另一条分支放弃继续磨斜率，直接研究“是否可能 \(S\to\infty\)”。

利用 DD plane 中

\[
P>\mathcal R>r_3
\]

以及

\[
\frac1{10Q}
\le
\frac{P-\mathcal R}{\mathcal R-r_3}
<
\frac1Q,
\]

可把原来的 surplus simplex 进一步刚化。

#### 22.1 \(d\)-dominant

\[
s_1+s_2\in\{-1,0,1,2\}.
\]

#### 22.2 \(s_2\)-dominant

\[
s_1+d\in\{-1,0,1,2\}.
\]

#### 22.3 \(s_1\)-dominant

只剩三条整数射线。

合计：

\[
\boxed{
4+4+3=11
}
\]

个固定 surplus modes。

这使“无界 surplus 锥”变成有限模式集。

---

### 23. 所有位数尺度都是 \(O(S)\)

整数球面 gap 还给出，例如 \(s_2\)-dominant 中

\[
s_2\le9S+4.
\]

所以在 11 个模式中，numerator/denominator 的所有位数均为 \(O(S)\)。

任何额外无界自由度都必须真正体现为某个 arithmetic height，占据 \(S\) 的正比例。

---

### 24. 双边 large-divisor / large-gcd 结构

由

\[
F_-Q(\kappa+G)=E\kappa(\kappa+2G)
\]

令

\[
A_*=\kappa(\kappa+2G),
\qquad
B_*=Q(\kappa+G),
\]

\[
D_*=(A_*,B_*).
\]

约去公共因子后可写

\[
F_-=\rho A_0,
\qquad
E=\rho B_0,
\]

所以不仅有大因子进入 \(F_-\)，还有互补大因子进入 \(E\)。

继续使用

\[
\gamma=(\kappa,G),
\qquad
\kappa=\gamma u,
\qquad
G=\gamma v,
\]

以及

\[
\delta=(\gamma,u+v),
\]

可得到显式

\[
L_F\mid F_-,
\qquad
L_E\mid E.
\]

这把无界逃逸重新表述为：

\[
\boxed{
\text{large-gcd degeneration}
}
\]

问题。

如果所有 gcd 只有 \(10^{o(S)}\) 高度，则双边大除数应足以造成绝对矛盾；若 gcd 占正比例高度，则要追踪这种退化为何只能来自某种固定代数结构。

---

## 第八部分：第三尾 moving primes 与 carrier defects

### 25. reduced tail denominator

令

\[
t=(10^mQ,b_3),
\]

\[
u=\frac{10^mQ}{t},
\qquad
v=\frac{b_3}{t}.
\]

则

\[
(u,v)=1,
\]

并存在 \(\gamma>0\)：

\[
\kappa=\gamma u,
\qquad
G=\gamma v.
\]

特别地

\[
\boxed{v\mid G.}
\]

---

### 26. 任意 moving odd prime 都是 Gaussian split prime

若

\[
p\mid v,\qquad p\nmid10,
\]

则 denominator prime graph 与整数球面共同强迫：

\[
\boxed{
p\equiv1\pmod4.
}
\]

同时其 denominator valuation pattern 只有 pair-max 一种可能：

第三分母与一个 prefix 分母并列最高，另一个 prefix 较低。

所以 \(v\) 的 odd rough part 精确编码 denominator imbalance。

---

### 27. moving prime 自动产生高阶 Gaussian contact

将 \(v\) 的非十进制部分写成

\[
v_0=v_1v_2,
\qquad
(v_1,v_2)=1,
\]

按照 pair-max 发生在 \(b_1,b_3\) 还是 \(b_2,b_3\) 分配。

则

\[
\boxed{
v_1^2\mid y_1^2+y_3^2,
}
\]

\[
\boxed{
v_2^2\mid y_2^2+y_3^2.
}
\]

并且

\[
v_1\mid H,y_2,
\qquad
v_2\mid H,y_1.
\]

对每个 \(p^{d_p}\Vert v_0\)，若低 prefix exponent 为 \(r\)，还可得到

\[
v_p(E)=r,
\]

\[
v_p(\mathcal N_{12})=2r,
\]

\[
v_p(\gamma)=2r,
\]

\[
\boxed{
v_p(F_-)=v_p(F_+)=2r,
}
\]

而

\[
v_p(F_-+F_+)>2r.
\]

因此所有 moving split primes 都自动形成 deep resonance，无需再逐个奇素数做更高 Hensel lifting。

这说明奇素数局部障碍已经“饱和”，剩下的是跨 prime、跨 carrier 的全局兼容性。

---

### 28. canonical denominator normal form

对 moving split core 可以唯一写

\[
b_1=h\,v_1B_1,
\]

\[
b_2=h\,v_2B_2,
\]

\[
b_3=h\,v_1v_2B_3,
\]

并且

\[
(B_1B_2B_3,v_0)=1.
\]

相应地

\[
E=hE_0,
\qquad
\mathcal N_{12}=h^2N_0,
\]

\[
F_-=h^2F_{-,0},
\qquad
F_+=h^2F_{+,0},
\]

且 reduced cores 与 \(v_0\) 互素。

于是

\[
\boxed{
F_{+,0}\equiv-F_{-,0}\pmod{v_0}.
}
\]

这是一条全局 CRT moving-prime resonance。

---

### 29. carrier defects

定义

\[
D_1=10^{k_{12}}y_1-H,
\]

\[
D_2=10^{d_3}y_2-H.
\]

则

\[
v_2\mid D_1,
\qquad
v_1\mid D_2.
\]

更重要的是：

\[
D_1\ne0,
\qquad
D_2\ne0.
\]

证明来自二平方和障碍。若例如 \(D_1=0\)，则

\[
H=10^{k_{12}}y_1
\]

导致

\[
y_2^2+y_3^2
=
(10^{2k_{12}}-1)y_1^2.
\]

而

\[
10^{2k_{12}}-1\equiv3\pmod4,
\]

其分解中必有 \(3\bmod4\) 素数以奇次出现，与二平方和定理矛盾。

因此

\[
\boxed{
|D_1|\ge v_2,
\qquad
|D_2|\ge v_1.
}
\]

同时 DD plane 给出

\[
\boxed{
10^{m_3}(AD_1+BD_2)
=
b_3(H-y_3)>0.
}
\]

这把 moving Gaussian modulus 直接连接到十进制 carrier defect。

---

### 30. 长尾强制巨大 \(2,5\)-smooth common factor

把

\[
t=t_{10}t_0,
\]

其中

\[
t_{10}=2^a5^b,
\qquad
(t_0,10)=1.
\]

由于

\[
t_0\mid Q,
\qquad
v\mid G,
\]

有

\[
t_0v<10^{2S}.
\]

但

\[
b_3=t_{10}t_0v\ge10^{m_3-1}.
\]

于是

\[
\boxed{
t_{10}>
10^{m_3-2S-1}.
}
\]

因此当

\[
m_3>2S+1
\]

时，第三尾必然含有指数级大的 decimal \(2,5\)-smooth common factor。

这给出一个结构二分：

\[
\boxed{
\text{moving split Gaussian excess}
+
\text{decimal smooth common scale}.
}
\]

---

## 第九部分：primitive determinant ladder 与 overlap

### 31. denominator overlap \(g_*\)

定义

\[
M_{12}=\operatorname{lcm}(b_1,b_2),
\]

\[
d_{12}=(b_1,b_2),
\]

\[
h_3=(M_{12},b_3).
\]

再定义

\[
\boxed{
g_*
=
d_{12}h_3
=
(b_1,b_2)\,
(\operatorname{lcm}(b_1,b_2),b_3).
}
\]

若

\[
c_3=\frac q{b_3},
\]

则

\[
\boxed{
g_*=\frac G{c_3},
\qquad
q=\frac{Gb_3}{g_*}.
}
\]

\(g_*\) 精确测量 denominator overlap。

---

### 32. sphere common scale

定义

\[
D=(H,q).
\]

逐素数分析 denominator maximum 后得到

\[
\boxed{
D\mid g_*.
}
\]

所以球面半径与 lcm 的公共尺度必须由真实 denominator overlap 支付。

---

### 33. exact lift 的 primitive reduction

写

\[
H=DH_0,
\qquad
q=Dq_0,
\qquad
(H_0,q_0)=1.
\]

由 exact lift

\[
q\alpha=H\beta
\]

得到存在唯一 \(C>0\)：

\[
\alpha=CH_0,
\qquad
\beta=Cq_0,
\]

且

\[
C=(\alpha,\beta).
\]

并有粗常数窗口

\[
Dg_*<C<111Dg_*.
\]

---

### 34. primitive determinant ladder

定义 DD determinant

\[
E=b_3A_{12}10^{d_3}-a_3Q>0.
\]

因为 \(C\mid\alpha,\beta\)，可得

\[
C\mid E.
\]

令

\[
E'=\frac EC.
\]

则有两条精确 primitive determinant：

\[
\boxed{
A_{12}10^{d_3}q_0-QH_0=E',
}
\]

\[
\boxed{
b_3H_0-a_3q_0
=
10^{m_3}E'.
}
\]

如果

\[
\omega=(10^{m_3},b_3),
\qquad
L=10^{m_3}/\omega,
\qquad
\tau=b_3/\omega,
\]

还得到

\[
\boxed{
DE'=\tau a,
}
\]

其中

\[
H-y_3=La.
\]

这组式子构成 primitive determinant ladder。

---

### 35. small factor 的 exact factorization

可进一步导出

\[
\boxed{
F_-
=
a\,g_*
\frac{L(LQ+2\tau)}{\tau}.
}
\]

以及

\[
F_->
(H-y_3)Qg_*.
\]

#### 35.1 一个重要修正

后续审计指出：

虽然上述 exact factorization 和不等式成立，但**不能把 \(g_*\) 直接视为独立的额外高度惩罚**。

因为

\[
(H-y_3)g_*
=
q(\mathcal R-r_3)g_*
=
Gb_3(\mathcal R-r_3),
\]

这里会发生精确抵消。

所以后续不得再使用“\(g_*\) 大 \(\Rightarrow\) \(F_-\) 自动多付一份独立指数高度”这一推断。

有效信息应该来自 overlap 的**精确参数化**和 normalized second factor。

这是合并后必须保留的逻辑修正。

---

## 第十部分：overlap 完全参数化与 scale-free quadratic

### 36. \(C\) 是十进制单位

对 exact lift 的 concat gcd 有

\[
\boxed{
(C,10)=1.
}
\]

这是全局结论。

---

### 37. overlap 参数化

令

\[
\eta=(Q,\tau),
\qquad
Q=\eta Q_1,
\qquad
\tau=\eta v.
\]

则

\[
t=(10^{m_3}Q,b_3)=\omega\eta,
\]

并有

\[
u=LQ_1,
\qquad
v=\tau/\eta,
\qquad
(LQ_1,v)=1.
\]

再令

\[
\varepsilon=(c_3,u+v),
\]

\[
c_3=\varepsilon c,
\qquad
u+v=\varepsilon w.
\]

可逐步推出

\[
D=vc\lambda,
\]

\[
C=\lambda w,
\]

\[
g_*=vc\lambda r,
\]

\[
G=\varepsilon vc^2\lambda r.
\]

以及

\[
q_0=\frac{\omega\eta\varepsilon}{\lambda}.
\]

---

### 38. 关键约化 \(c\mid a\)

primitive determinant 两式联立后得到

\[
c\lambda\mid\eta a,
\]

同时

\[
c\mid La,
\]

而

\[
(L,\eta)=1.
\]

所以

\[
\boxed{
c\mid a.
}
\]

写

\[
a=ca_0.
\]

于是 primitive system 变成：

\[
\boxed{
\omega\varepsilon A_{12}10^{d_3}
-\lambda Q_1H_0
=
a_0,
}
\]

\[
\boxed{
\lambda vH_0-a_3\varepsilon
=
La_0,
}
\]

消去 \(H_0\)：

\[
\boxed{
v\omega A_{12}10^{d_3}
-a_3Q_1
=
wa_0.
}
\]

这是后续 numerator/sphere 的核心线性正规形。

---

### 39. scale-free quadratic

把 sphere

\[
(H-y_3)(H+y_3)=y_1^2+y_2^2
\]

与上面的线性正规形联立，并令

\[
x=\frac{a_0}{\omega},
\]

得到

\[
\boxed{
\begin{aligned}
&
L c^4\lambda^2r^2w(LQ_1+2v)x^2\\
&\quad
-2L c^4\lambda^2r^2v(LQ_1+v)
A_{12}10^{d_3}x\\
&\quad
+\eta^2\mathcal N_{12}Q_1w
=0.
\end{aligned}
}
\]

最重要的结构是：

\[
\boxed{
\omega\text{ 从系数中完全消失}.
}
\]

也就是说，公共 decimal scale 不能再作为隐藏自由度混在 coefficient 中。

---

### 40. scale-free depth allocation

令最简根为

\[
x=\frac{A_0}{\Omega},
\qquad
(A_0,\Omega)=1.
\]

由二次方程得到

\[
\boxed{
L\mid\mathcal N_{12}Q_1\Omega^2.
}
\]

因此对 \(p=2,5\)：

\[
v_p(L)
\le
v_p(\mathcal N_{12})
+
v_p(Q_1)
+
2v_p(\Omega).
\]

同时

\[
\boxed{
\min(v_p(a_0),v_p(\omega))
\le
v_p(Q_1).
}
\]

所以被 \(a_0\) 与 \(\omega\) 共同约掉的 decimal depth 也必须由 \(Q_1\) 支付。

这将 tail decimal depth 变成：

\[
\boxed{
L
\longrightarrow
\mathcal N_{12}
\cup Q_1
\cup \Omega^2.
}
\]

---

### 41. normalized near-square

同一结构还能把原判别式规范为

\[
\boxed{
Z^2
=
(LGA_{12}10^{d_3})^2
-
LQ(LQ+2\tau)\mathcal N_{12}.
}
\]

令

\[
X=LGA_{12}10^{d_3},
\]

则

\[
(X-Z)(X+Z)
=
LQ(LQ+2\tau)\mathcal N_{12}.
\]

并可取次序使

\[
\boxed{
F_-=\omega(X-Z),
\qquad
F_+=\omega(X+Z).
}
\]

所以全 DD 都有

\[
\boxed{
\omega\mid F_-,
\qquad
\omega\mid F_+.
}
\]

---

## 第十一部分：denominator-only 无限骨架及其意义

### 42. denominator-tail 单独无法给绝对 \(S\) 界

一个非常重要的反向结果是：

可以显式构造真正无界的 denominator-only skeleton，满足 DD 的大量 denominator/tail 恒等式，但尚未要求 numerator sphere。

例如 pairwise-coprime 情况中存在：

- 固定 \(C=11\) 的长尾 family；
- 固定 \(m_3=1,C=7\) 的 family。

这些 family 中 \(S\to\infty\)，denominator equation 仍成立。

因此得到方法论结论：

\[
\boxed{
\text{denominator-tail arithmetic alone cannot imply }S\le S_0.
}
\]

后续必须真正使用

\[
\boxed{
\text{numerator sphere}
+
\text{primitive determinant ladder}.
}
\]

这解释了为什么继续给 denominator tail 叠加普通整除条件不会自动结束 DD。

#### 42.1 好消息

一旦加入 scale-free rational-root / sphere 条件，上述两个 sanity families 都被整体杀掉。

所以 numerator sphere 的确提供了 denominator skeleton 缺失的独立约束。

---

## 第十二部分：primitive determinant carry 与 ultrametric tetrahedron

### 43. 三个 carrier determinants

定义

\[
\Delta_{12}
=
a_1b_2 10^k-a_2b_1 10^d,
\]

\[
\Delta_{13}
=
a_1b_3 10^k-a_3b_1,
\]

\[
\Delta_{23}
=
a_2b_3 10^d-a_3b_2.
\]

三块 decimal concat 给出两级 carry：

\[
\boxed{
J_1
=
10^{m_3}\Delta_{12}
+
\Delta_{13},
}
\]

\[
\boxed{
E
=
10^{m_2}\Delta_{13}
+
\Delta_{23}.
}
\]

并满足 Plücker 关系

\[
\boxed{
b_1\Delta_{23}
-b_2\Delta_{13}
+b_3\Delta_{12}
=0.
}
\]

---

### 44. primitive carrier vectors

令

\[
g_1=(10^k,b_1),
\qquad
g_2=(10^d,b_2).
\]

定义 primitive vectors

\[
V_1=
\left(
\frac{a_1 10^k}{g_1},
\frac{b_1}{g_1}
\right),
\]

\[
V_2=
\left(
\frac{a_2 10^d}{g_2},
\frac{b_2}{g_2}
\right),
\]

\[
V_3=(a_3,b_3).
\]

这里有一个后期修正后的强 forced factor：

\[
\boxed{
g_1g_2\mid\Delta_{12}.
}
\]

旧版本只抽出 \(\operatorname{lcm}(g_1,g_2)\)，强度不足；合并后统一使用 \(g_1g_2\)。

定义

\[
\theta_{12}=\frac{\Delta_{12}}{g_1g_2},
\]

\[
\theta_{13}=\frac{\Delta_{13}}{g_1},
\]

\[
\theta_{23}=\frac{\Delta_{23}}{g_2}.
\]

---

### 45. determinant ultrametric theorem

对任意三个 primitive 向量 \(U_1,U_2,U_3\in\mathbf Z^2\)，

\[
\gcd(\det(U_1,U_2),\det(U_1,U_3))
\mid
\det(U_2,U_3),
\]

以及循环对称式。

所以对每个素数 \(p\)：

\[
\boxed{
v_p(\theta_{12}),
\quad
v_p(\theta_{13}),
\quad
v_p(\theta_{23})
}
\]

中的两个最小值必须相等。

即只有三种 order type：

\[
x=y\le z,
\qquad
x=z\le y,
\qquad
y=z\le x.
\]

这把原来大量独立 residual state 压成一个 \(p\)-adic projective tree。

---

### 46. exact ratio 加入：carrier tetrahedron

令 exact ratio primitive point 为

\[
V=(H_0,q_0).
\]

定义 carrier-to-parent defects

\[
K_1=a_1 10^kq_0-b_1H_0,
\]

\[
K_2=a_2 10^dq_0-b_2H_0.
\]

有精确 parent carry

\[
\boxed{
E'
=
10^{m_2}K_1+K_2.
}
\]

而且

\[
K_1\ne0,
\qquad
K_2\ne0.
\]

零值同样由

\[
10^{2k}-1\equiv3\pmod4
\]

型二平方和障碍排除。

四个 primitive points

\[
V_1,V_2,V_3,V
\]

形成 carrier tetrahedron，任意三个点对应的 determinant valuations 都满足 ultrametric consistency。

这说明第三块与 exact ratio 的 \(m_3\)-deep contact 会向 tetrahedron 其他边传播，但传播结构高度受限。

---

### 47. 修正后的 nested carry

primitive 后的两级 carry 为

\[
\boxed{
CC_P\varepsilon_P
=
g_2\theta_{23}
+
10^{m_2}g_1\theta_{13},
}
\]

\[
\boxed{
CC_{23}\varepsilon_1
=
\theta_{13}
+
10^{m_3}g_2\theta_{12}.
}
\]

第二级真正 forced decimal depth 是

\[
\boxed{
m_3+v_p(g_2).
}
\]

#### 47.1 另一处逻辑修正

在 \(\varepsilon_2=0\) 的退化中，旧版本曾把 child gcd \(C_{23}\) 过度约化成一个显式邻因子。

后续已修正为真实 gcd：

\[
C_{23}
=
\gcd\!\left(
a_2(10^{m_3}+u),
b_3(g_2 10^{m_3}+1)
\right).
\]

所以不能再使用旧的过强等式。

---

## 第十三部分：Gaussian bottom phase

### 48. prefix norm 的 Gaussian rotation

令

\[
X=a_1b_2,
\qquad
Y=a_2b_1.
\]

则

\[
\mathcal N_{12}=X^2+Y^2.
\]

取

\[
h=\min(k,d),
\]

\[
u=10^{k-h},
\qquad
v=10^{d-h}.
\]

定义

\[
U_{12}=uX-vY,
\]

\[
V_{12}=vX+uY.
\]

则

\[
\boxed{
\Delta_{12}=10^hU_{12},
}
\]

以及精确 Gaussian rotation：

\[
\boxed{
U_{12}^2+V_{12}^2
=
(u^2+v^2)\mathcal N_{12}.
}
\]

因此 scale-free allocation

\[
L\mid\mathcal N_{12}Q_1\Omega^2
\]

若迫使 \(\mathcal N_{12}\) 吞掉深 \(2/5\)-adic valuation，这些深度有具体几何意义：它们对应 primitive prefix angle 在 \(\mathbf Z_p[i]\) 中的高阶接触。

于是形成桥：

\[
\boxed{
\text{scale-free depth allocation}
\to
\text{Gaussian bottom phase}
\to
\text{primitive determinant tetrahedron}.
}
\]

---

### 49. 真正 excess 的三层分解

后续分析应区分：

#### 49.1 decimal baseline

由

\[
m_2,m_3,g_1,g_2,C_P,\ldots
\]

显式带来的 \(2/5\)-depth。

#### 49.2 projective baseline

由 determinant tetrahedron ultrametric 强制的最低 valuation。

#### 49.3 Gaussian angular depth

由 primitive two-square norm 本身产生的 angle depth。

只有在抽掉前两层后仍留下正线性高度的第三层，才是真正可能产生 Subspace/Ridout/resultant 矛盾的 excess。

---

## 第十四部分：stereographic coefficient circle

### 50. 消去 ghost 振幅

令

\[
u=H-y_3>0,
\qquad
v=H+y_3.
\]

定义

\[
\boxed{
z=
\frac{y_1+i y_2}{H+y_3}
=
\frac{y_1+i y_2}{v}
\in\mathbf Q(i).
}
\]

因为

\[
y_1^2+y_2^2=uv,
\]

有

\[
|z|^2=\frac uv<1.
\]

反解：

\[
y_1=v\Re z,
\]

\[
y_2=v\Im z,
\]

\[
y_3=\frac v2(1-|z|^2),
\]

\[
H=\frac v2(1+|z|^2).
\]

---

### 51. DD plane 变成 denominator-only circle

设

\[
r_0=10^kA,
\qquad
s_0=10^dB,
\]

\[
R_0=LQ+2\tau,
\]

\[
\mathcal C=L(r_0+i s_0).
\]

则 DD coefficient plane 等价于

\[
\boxed{
|R_0z-\mathcal C|^2
=
LE_D.
}
\]

这个圆的中心与半径只依赖 denominator/mode。

ghost 的共同振幅 \(v\) 已经完全消失。

因此 DD 的 projective sphere freedom 只有一个 rational circle parameter。

---

### 52. numerator 恢复只有一个共同 scale

固定 rational circle point \(z\) 后：

\[
a_1=\lambda b_1\Re z,
\]

\[
a_2=\lambda b_2\Im z,
\]

\[
a_3=
\lambda\frac{b_3}{2}(1-|z|^2).
\]

把对应 rational shape primitive 化为

\[
(A_1,A_2,A_3),
\qquad
(A_1,A_2,A_3)=1,
\]

则所有整数 numerator 恰为

\[
\boxed{
(a_1,a_2,a_3)
=
t(A_1,A_2,A_3).
}
\]

合法性要求：

\[
(A_i,b_i)=1,
\]

以及

\[
(t,b_1b_2b_3)=1.
\]

三个 digit windows 对 \(t\) 的约束只是三个乘法宽度为 10 的区间之交。

所以原无界 ghost 问题被重写为：

\[
\boxed{
\text{projective primitive shape}
+
\text{一个不足一 decade 的整数 scale interval}.
}
\]

这给出一个很清晰的目标：

\[
\boxed{
\text{primitive shape height / digit-shell incompatibility}.
}
\]

---

## 第十五部分：carrier-circle eliminant

### 53. 三条 carrier equality 线

在 stereographic 坐标 \(z=X+iY\) 上，三条 carrier equality 可写成三个仿射线性型

\[
\ell_{12},
\qquad
\ell_{13},
\qquad
\ell_{23},
\]

并满足

\[
\ell_{13}-\ell_{23}=R\ell_{12}.
\]

三条线有一个共同交点

\[
\boxed{
z_*
=
\frac1{2\cdot10^k}
+
\frac{i}{2\cdot10^d}.
}
\]

---

### 54. 共点永远不在 DD circle 上

把 \(z_*\) 代入 coefficient circle，得到

\[
\boxed{
\mathscr F(z_*)
=
\frac{(10^{2k}+10^{2d})R^2}
{4\cdot10^{2k+2d}}
>0.
}
\]

所以三个 carrier 不可能同时与 exact sphere ratio 相等。

这里更重要的事实是：

\[
\boxed{
\mathscr F(z_*)\text{ 完全不含 }E_D.
}
\]

---

### 55. 对“圆参数 resultant”的修正

若先用 Gaussian norm 参数化圆，再对两条 carrier residual 做 resultant，会出现因子

\[
LE_D.
\]

后续分析发现，这个 \(LE_D\) 主要来自参数化映射的 ramification / condition number。

它不能被解释为真实 carrier degeneracy budget。

因此后续应使用**不经过该参数化的 circle-line eliminant**。

---

### 56. 无 \(E_D\) eliminant

直接从两条 carrier residual 恢复 \((X,Y)\)，再代回 circle equation，可构造

\[
\boxed{
\Xi
=
(LQ+\tau)^2
(LQ+2\tau)^2
(10^{2k}+10^{2d}),
}
\]

完全不含 \(E_D\)。

如果 projective rational point 写成最低项

\[
z=\frac{X_0+iY_0}{Z_0},
\]

两个独立 carrier residual 同时满足

\[
p^h\mid\mathcal E_{12},
\qquad
p^h\mid\mathcal E_{13},
\]

则

\[
\boxed{
h
\le
2v_p(Z_0)
+
v_p(\Xi).
}
\]

于是 simultaneous carrier contact 的深度只能由：

- projective denominator \(Z_0\)；
- decimal baseline \(10^{2k}+10^{2d}\)；
- \(\eta=(Q,\tau)\)；
- 单侧 moving factor \((LQ+\tau)/\eta\) 或 \((LQ+2\tau)/\eta\)

支付。

由于这两个 moving factors 在奇素数处基本互素，不可能同时深。

---

## 第十六部分：projective denominator 的精确分解

### 57. \(Z_0\) 的 exact valuation formula

写

\[
g=(y_1,y_2),
\]

\[
y_1=gX,
\qquad
y_2=gY,
\qquad
(X,Y)=1.
\]

则

\[
(H-y_3)(H+y_3)
=
g^2(X^2+Y^2).
\]

最低项 projective denominator 满足

\[
\boxed{
Z_0=\frac{H+y_3}{(g,H+y_3)}.
}
\]

等价地

\[
\boxed{
Z_0
=
\frac{g(X^2+Y^2)}
{(La,g(X^2+Y^2))}.
}
\]

记

\[
r_p=v_p(g),
\]

\[
\alpha_p=v_p(La),
\]

\[
\omega_p=v_p(X^2+Y^2).
\]

则

\[
\boxed{
v_p(Z_0)
=
\max(0,r_p+\omega_p-\alpha_p).
}
\]

所以 \(Z_0\) 的深度精确分成：

\[
\boxed{
\text{ghost common scale}
+
\text{primitive Gaussian angular depth}
-
\text{sphere-gap depth}.
}
\]

它已经不再是一个神秘自由变量。

---

### 58. 二进没有无界 angular excess

因为 \((X,Y)=1\)：

- 一奇一偶时
  \[
  v_2(X^2+Y^2)=0;
  \]
- 两者都奇时
  \[
  v_2(X^2+Y^2)=1.
  \]

因此

\[
\boxed{
\omega_2\in\{0,1\}.
}
\]

所以二进 projective denominator 的线性深度只能来自 common ghost scale。

---

### 59. 五进的 genuine Gaussian angle

对 \(p=5\)，由于 \(-1\) 是平方，

\[
\omega_5=v_5(X^2+Y^2)
\]

可以任意深。

若

\[
\omega_5>0,
\]

则 \(X,Y\) 都是五进单位，其比值在 \(\mathbf Q_5\) 中高阶逼近

\[
\pm\sqrt{-1}.
\]

所以五进是唯一可能携带 genuine projective angular excess 的 decimal prime。

---

### 60. 五进 angle 与 bottom edge 严格互斥

把 primitive prefix pair 写成

\[
X'=a_1b_2=cX_1,
\]

\[
Y'=a_2b_1=cY_1,
\]

\[
(X_1,Y_1)=1.
\]

primitive bottom residual 为

\[
U_{12}^{\rm prim}
=
aX_1-bY_1,
\]

其中 \(a,b\) 中一个等于 \(1\)，另一个为 \(10^{|k-d|}\)。

逐 \(k>d,d>k,k=d\) 三种情况可证明：

\[
\boxed{
\omega_5>0
\Longrightarrow
v_5(U_{12}^{\rm prim})=0.
}
\]

也就是

\[
\boxed{
\text{primitive 5-adic Gaussian angle depth}
\quad\perp\quad
\text{primitive bottom-carrier depth}.
}
\]

于是当 \(Z_0\) 的危险 5-depth 来自 \(\omega_5\) 时，bottom determinant \(\theta_{12}\) 不能再次吸收同一份角度深度。

这消除了一个此前可能的重复支付通道。

---

### 61. 当前一般 5-adic allocation 的两大机制

scale-free allocation

\[
L\mid\mathcal N_{12}Q_1\Omega^2
\]

与

\[
\mathcal N_{12}
=
c^2(X_1^2+Y_1^2)
\]

给出

\[
v_5(\mathcal N_{12})
=
2v_5(c)+\omega_5.
\]

因此只需区分：

#### A. common-scale / multiplicative branch

\[
v_5(L)
\]

主要由

\[
2v_5(c),
\qquad
v_5(Q_1),
\qquad
2v_5(\Omega)
\]

支付。

#### B. genuine angular branch

\(v_5(L)\) 的正线性部分进入 \(\omega_5\)。

此时 bottom edge 没有 angular depth。

这两支应该分别与 carrier tetrahedron 的 ultrametric tree 和无 \(E_D\) eliminant 联立。

---

## 第十七部分：假想 \(6.308883\ldots\) frontier 的 terminal 线

> 本部分的许多 \(o(S)\) 结论只针对一个假想的无界 DD 序列，且假设其逼近
>
> \[
> \frac{n_3}{S}\to6.308883577618\ldots.
> \]
>
> 它们不能直接当作对所有 DD 候选的全局恒等式。

### 62. terminal denominator normalization

frontier 刚性可以把 denominator 拆成一组大核心与 subexponential cofactors。主要对象包括：

\[
C_L
\]

——pair-max Gaussian core，满足

\[
\log C_L=S+o(S),
\]

以及 clean source core

\[
q_c,
\]

满足

\[
\log q_c
=
0.308883577618\ldots S+o(S),
\]

且

\[
(q_c,C_L)=1.
\]

---

### 63. sphere bridge

terminal exact lift 可坍缩为

\[
g_0H_{\rm sph}
=
V\lambda A_0,
\]

\[
y_3=a_3\lambda,
\]

以及

\[
VA_0-g_0a_3
=
2\cdot5^TR_0.
\]

因此

\[
\boxed{
H_{\rm sph}-y_3
=
2\cdot5^T\rho_0,
}
\]

其中

\[
\log\rho_0=o(S).
\]

互补因子为

\[
\boxed{
H_{\rm sph}+y_3
=
q_c^2K_+.
}
\]

所以

\[
\boxed{
2\cdot5^T\rho_0\,q_c^2K_+
=
y_1^2+y_2^2.
}
\]

在 terminal frontier 上，\(5^T\) 成为球面小因子的主 smooth 深度，\(q_c^2\) 落到互补大因子。

---

### 64. oriented Gaussian pair-max core

对

\[
p^h\Vert C_L,
\qquad
p\equiv1\pmod4,
\]

在 \(\mathbf Z[i]\) 中取方向

\[
p=\pi_p\bar\pi_p
\]

并将 Hensel depth 定向到其中一侧。

可构造

\[
\Pi=\prod\pi_p^h,
\qquad
N(\Pi)=C_L,
\]

使

\[
\boxed{
\Pi^2\mid y_2+i y_3
}
\]

（必要时整体共轭）。

这保存了 split prime 的 orientation；只看 \(C_L^2\mid y_2^2+y_3^2\) 会丢失关键相位信息。

---

### 65. secondary Gaussian core

由 Gaussian cross-determinant 可得到

\[
\boxed{
\Pi
\mid
A_*2^{m-2}q_c
-iB_*5^{2T-m},
}
\]

其中

\[
\log|A_*|,\log|B_*|=o(S).
\]

定义 quotient

\[
\Delta_1
=
\frac{
A_*2^{m-2}q_c-iB_*5^{2T-m}
}{\Pi}.
\]

则

\[
\boxed{
C_LN(\Delta_1)
=
A_*^22^{2m-4}q_c^2
+
B_*^25^{4T-2m}.
}
\]

而

\[
\frac{\log|\Delta_1|}{S}
\to
0.654441788809\ldots.
\]

也就是原来的 terminal geometry 被 Gaussian renormalization 压成一个约 \(0.65444S\) 的 secondary core。

---

## 第十八部分：double numerator reconstruction

### 66. \(A_0\) 的唯一重构

terminal system 给出两个线性同余：

\[
UA_0\equiv-R_0
\pmod{B10^d},
\]

以及

\[
VA_0
\equiv
5^TR_0
\pmod{q_c^2}.
\]

两个主模量基本互素，联合模量高度约为

\[
5.617767155236\ldots S,
\]

而

\[
\log_{10}A_0
=
5.308883577618\ldots S+o(S).
\]

因此对固定 terminal denominator-tail data：

\[
\boxed{
\#\{A_0\}\le1.
}
\]

---

### 67. \(A_{12}\) 的唯一重构

另一条 terminal cross-resultant 消去

\[
A_0,a_3,L
\]

后，再分别模 \(q_c^2\) 与 \(C_L\)，得到对 \(A_{12}\) 的两个有效线性同余。

联合有效模量高度为

\[
1.617767155\ldots S+o(S),
\]

而 frontier 上

\[
\log_{10}A_{12}
=
S+o(S).
\]

所以

\[
\boxed{
\#\{A_{12}\}\le1.
}
\]

结合 \(A_0\) 唯一性：

\[
\boxed{
\text{固定 terminal denominator-tail data 后，整个 numerator triple
没有指数级自由度。}
}
\]

这是 terminal 线非常重要的 entropy collapse。

---

## 第十九部分：对 terminal “Pell cancellation”的审计与修正

### 68. \(J_1\) 自动为平方

此前 terminal Hensel quotient 写成一个 Pell-like 方程：

\[
4\widetilde r^{\,2}5^TR_0L
-
C_L^2J_1
=
P_0^2.
\]

后续 norm audit 发现：

\[
\boxed{
J_1=P_1^2
}
\]

且

\[
J_C=-(q_cP_1)^2.
\]

所以 \(J_1\) 并非新的独立 terminal variable。

---

### 69. 重要逻辑修正：Pell cancellation 是 prefix norm 的重写

将 \(P_1,P_0\) 展开后，上式精确化成

\[
\boxed{
4J^2\widetilde w^{\,2}\widetilde r^{\,2}
5^TR_0L
=
B^2\theta^2g_0^2\mathcal N_{12}.
}
\]

因此所谓 “两个 \(7S\) 量消去成 \(3S\) square” 不能再作为独立第二个 Diophantine approximation 使用。

它本质上就是原 prefix two-square norm 经 terminal 参数变化后的表达。

合并文档必须删除“把它作为独立 Pell 近似再收费”的思路。

不过该审计同时产生两个新结论：

\[
\boxed{
\log_{10}\operatorname{core}_{10}(L)
=
4S+o(S),
}
\]

以及

\[
\boxed{
\log_{10}(C_L,L)=o(S).
}
\]

所以 \(C_L\) 与 \(L\) 是两个巨大且渐近互素的 rough objects。

---

## 第二十部分：真正新的 denominator quotient \(R_2\)

### 70. denominator-only matrix determinant

decimal prefix equation 与 tail phase 可写成 \(2\times2\) 整数矩阵系统。

消元后得到

\[
\boxed{
R_2
=
\frac{
5^T\widetilde r+s q_c\theta
}{
2^{m_2}
}
\in\mathbf Z_{>0}.
}
\]

并有第二关系

\[
\boxed{
UR_2
=
\widetilde r2^{H-m_2}Z
+
s^2\widetilde w5^{m_2}.
}
\]

还有

\[
\boxed{
q_c\theta\,2^{H-m_2}Z
-
s\widetilde w5^{T+m_2}
=
C_0R_2.
}
\]

这些式子完全来自 denominator/tail matrix，而不来自 sphere norm。

这使 \(R_2\) 成为真正新的 independent denominator invariant。

---

### 71. \(R_2\) 的 rough height

frontier 上

\[
\boxed{
\frac{\log_{10}R_2}{S}
\to
1.007853581954\ldots.
}
\]

并且

\[
v_5(R_2)=0,
\]

\[
v_2(R_2)=o(S).
\]

所以

\[
\boxed{
\log_{10}\operatorname{core}_{10}(R_2)
=
1.007853581954\ldots S+o(S).
}
\]

同时

\[
\log(R_2,q_c)=o(S),
\]

\[
\log(R_2,Z)=o(S).
\]

这说明 \(R_2\) 的大 rough mass 与旧的 \(q_c,Z\) rough core 都基本独立。

---

## 第二十一部分：最后 residue entropy 从 \(0.30888S\) 压到 \(0.00785S\)

### 72. 第一级 congruence

由 \(R_2\) 的 integrality：

\[
\boxed{
s\theta q_c
\equiv
-5^T\widetilde r
\pmod{2^{m_2}}.
}
\]

在 normalized funnel 中 coefficient 为二进单位，所以固定 exponents 和 subexponential cofactors 后，\(q_c\) 在模 \(2^{m_2}\) 下只有一个 residue class。

但

\[
q_c
=
10^{z_*S+o(S)},
\]

\[
2^{m_2}
=
10^{aS+o(S)},
\]

其中

\[
z_*=0.308883577618\ldots,
\qquad
a=\log_{10}2=0.301029995664\ldots.
\]

两者差

\[
\boxed{
\delta_*
=
z_*-a
=
0.007853581954\ldots.
}
\]

所以候选 \(q_c\) 数量至多

\[
\boxed{
10^{\delta_*S+o(S)}.
}
\]

一旦 \(q_c\) 固定，\(R_2\) 固定。

而第二关系中 \(R_2\) 的模长约 \(1.00785S\)，远大于 \(Z\) 的 \(0.30888S\) 窗口，所以每个 \(q_c\) 至多对应一个 \((U,Z)\)。

于是 terminal frontier 候选总 entropy 已降到

\[
\boxed{
N_{\rm frontier}(S)
\le
10^{0.007853581954\ldots S+o(S)}.
}
\]

---

## 第二十二部分：critical simplex 与 Gaussian residue transfer

### 73. 为什么再重复一次 fixed-target Subspace Theorem 没用

构造三坐标

\[
A=2^{m_2}UR_2,
\]

\[
B=5^T\widetilde r\,U,
\]

\[
C=\widetilde r2^HZ.
\]

则

\[
A-B=sq_c\theta U,
\]

\[
A-C=s^2\widetilde w10^{m_2}.
\]

frontier 上

\[
\log A
=
\log B
=
\log C
=
2S+o(S),
\]

而两个差只有

\[
S+o(S).
\]

对

\[
P=[A:B:C]\in\mathbf P^2
\]

在 \(\infty,2,5\) places 计算 proximity，恰好得到

\[
\boxed{
\sum\lambda
=
3h(P)+o(S).
}
\]

它正好处于 \(\mathbf P^2\) fixed-target Subspace Theorem 的临界常数。

所以再重复同类型 fixed-target 高度论证，只能到临界等号，无法获得严格线性矛盾。

---

### 74. Gaussian congruence 转移到 \(R_2\)

原 secondary Gaussian congruence 为

\[
\Pi
\mid
A_*2^{m-2}q_c
-iB_*5^{2T-m}.
\]

用

\[
s\theta q_c
=
2^{m_2}R_2-5^T\widetilde r
\]

替换，得到

\[
\boxed{
\Pi
\mid
g_0a_2 2^{m-2}
(2^{m_2}R_2-5^T\widetilde r)
-
i\widetilde rR_0 5^{2T-m}.
}
\]

这条式子对真正 denominator-only quotient \(R_2\) 是线性的。

在固定 oriented core \((C_L,\Pi)\) 及 subexponential data 后，系数在 Gaussian ideal 中除去 \(10^{o(S)}\) 损失后可逆。

其 rational effective period 为

\[
\boxed{
C_L/10^{o(S)}
=
10^{S+o(S)}.
}
\]

---

### 75. 最后的 \(q_c/R_2\) lift 对固定 \((C_L,\Pi)\) 至多一个

第一级 source congruence 的一般解为

\[
q_c=q_0+k2^{m_2},
\]

且

\[
0\le k<10^{\delta_*S+o(S)}.
\]

对应

\[
R_2=R_{2,0}+s\theta k.
\]

所以所有 source lift 产生的 \(R_2\) 只覆盖一个 logarithmic length

\[
\delta_*S+o(S)
\]

的 arithmetic interval。

而独立 Gaussian congruence 给 \(R_2\) 的 period 高度为

\[
S+o(S).
\]

因为

\[
\delta_*<1,
\]

对 sufficiently large \(S\)：

\[
\boxed{
\text{固定 }(C_L,\Pi)\text{ 和 subexponential terminal data 后，
最多一个 }k.
}
\]

所以最终 \(q_c/R_2\) residue lift 自身也不再拥有 exponential freedom。

---

## 第二十三部分：目前真正剩下的 terminal entropy

### 76. moving pair-max Gaussian core

经过上述步骤，假想 frontier family 若仍无界，其唯一可持续移动的主对象是

\[
\boxed{
(C_L,\Pi),
}
\]

其中

\[
C_L=10^{S+o(S)}
\]

由 pair-max split primes 组成，

\[
N(\Pi)=C_L
\]

并带有逐素数 Gaussian orientation。

当前已知：

\[
(C_L,q_c)=1,
\]

\[
(C_L,L)=10^{o(S)},
\]

\(\Pi\) 必须满足 secondary linear Gaussian condition；

一旦 \((C_L,\Pi)\) 固定，最后的 \(q_c,R_2,U,Z,C_0\) 与 numerator triple 基本都被唯一恢复。

因此 terminal 的最终目标可以写成：

\[
\boxed{
\#\{
(C_L,\Pi)
\text{ 满足 pair-max denominator equations 与 Gaussian residue}
\}
=
10^{o(S)}
}
\]

或者更强：

\[
\boxed{
\text{该集合对充分大 }S\text{ 为空}.
}
\]

fixed-target Subspace Theorem 已经达到临界常数，新的证明必须使用 **moving Gaussian orientation** 或 same-prime resultant。

---

## 第二十四部分：两个后期分支如何汇合

现在可以清晰看出两个分支各自做了什么。

### 77. 分支 I：全局高度 / tail / Subspace

这条线完成了：

1. \(8S-1\) 整层关闭；
2. 全局解析锥 \(<7.75S+O(1)\)；
3. \(7\sim7.75\) 状态分类；
4. 唯一 S-unit funnel；
5. Schmidt Subspace Theorem 将 dominant \(>7\) 全部压掉；
6. 全局 tail slope 从 6 降到 5；
7. 全 DD asymptotic frontier 降到
   \[
   6.308883577618\ldots;
   \]
8. 找到唯一 frontier ratios。

它回答的是：

> **如果 DD 真能无界，它究竟必须长成什么样？**

答案已经极其刚性。

---

### 78. 分支 II：projective / determinant / Gaussian

这条线完成了：

1. surplus 收成 11 fixed modes；
2. moving odd primes 全部变成 split Gaussian pair-max；
3. carrier defects 与 moving-prime modulus 对接；
4. denominator overlap \(g_*\) 与 sphere common scale 参数化；
5. primitive determinant ladder；
6. scale-free quadratic；
7. denominator-only 无限 skeleton，证明必须使用 numerator sphere；
8. determinant carry / ultrametric tetrahedron；
9. stereographic circle 消去 ghost amplitude；
10. circle-line eliminant 去掉伪 \(E_D\) budget；
11. projective denominator \(Z_0\) 精确分解；
12. 五进 angular phase 与 bottom edge 严格互斥。

它回答的是：

> **那个唯一无界形状中的剩余高度到底可以藏在哪里？**

目前答案已经从“很多 valuation 槽”压成了极少数 mutually exclusive channels。

---

### 79. terminal 分支：frontier entropy

这条线专门假设已经逼近 \(6.3089\) frontier，然后：

1. Gaussian orientation 提取 \(C_L,\Pi\)；
2. \(A_0\) 唯一重构；
3. \(A_{12}\) 唯一重构；
4. numerator triple 无 exponential entropy；
5. 审计并删除伪独立 Pell approximation；
6. 发现真正新的 denominator quotient \(R_2\)；
7. source entropy 从 \(0.30888S\) 压到 \(0.00785S\)；
8. 再把 Gaussian congruence 转到 \(R_2\)，固定 \((C_L,\Pi)\) 后最后 residue lift 也唯一；
9. 剩下 moving pair-max Gaussian core。

它回答的是：

> **即使已经落在唯一 frontier 上，一整个候选族还能靠什么产生指数多种可能？**

目前只剩 \((C_L,\Pi)\)。

---

## 第二十五部分：已经失败、饱和或被修正的路线

### 80. 继续逐层枚举 \(n_3=8S-c\)

最高层已经通过解析锥和统一结构消失。

继续逐层做巨大 finite search 的收益很低。

有限证书目前更适合最终 absolute \(S\) bound 出现以后做收尾。

---

### 81. 只靠 denominator-tail 整除

已经存在显式无限 denominator skeleton。

所以 denominator arithmetic 必须和 numerator sphere / reducedness / primitive determinant 合用。

---

### 82. 逐个 moving odd prime 做更深 Hensel

对 \(p\mid v_0\)，局部判别平方已经因

\[
p\equiv1\pmod4
\]

而自动 Hensel lift。

继续加深单 prime 局部条件不会自然产生新 obstruction。

问题已经转成 global compatibility / orientation。

---

### 83. ordinary quadratic character

在 S-unit phase 上做普通 Jacobi / quadratic reciprocity 最终只回到恒等式。

因为 split/inert 的一阶信息已经被结构吸收。

需要保留 Gaussian orientation 或更高阶相位。

---

### 84. 把 \(LE_D\) 当 resultant obstruction

circle parametrization 的 resultant 中出现 \(LE_D\)，但 \(E_D\) 是 parametrization ramification budget。

真实 carrier geometry 应使用无 \(E_D\) eliminant \(\Xi\)。

---

### 85. 把 \(g_*\) 当独立高度惩罚

exact formula 成立，但 \(g_*\) 会和 sphere gap 中的尺度精确抵消。

有效方法是 overlap parameterization / scale-free quadratic / normalized second factor。

---

### 86. 把 terminal Pell-like cancellation 当第二独立逼近

审计后发现

\[
J_1=P_1^2
\]

且 Pell-like equation 正是 prefix norm 的 terminal 重写。

不能重复计费。

真正新信息来自 denominator matrix quotient \(R_2\)。

---

### 87. 再重复 fixed-target Subspace Theorem

terminal 三坐标系统正好达到

\[
3h(P)
\]

临界常数。

重复同类型 fixed-target theorem 不会产生严格线性余量。

下一步必须使用 moving orientation / same-prime algebra。

---

## 第二十六部分：当前最值得继续的证明路线

### 88. 路线 A：完成一般 projective denominator / 5-adic allocation

这是最“全局”的结构路线。

目前已经有：

\[
h
\le
2v_p(Z_0)+v_p(\Xi),
\]

\[
v_p(Z_0)
=
\max(0,r_p+\omega_p-\alpha_p),
\]

以及

\[
\omega_2\in\{0,1\}.
\]

五进则有

\[
\omega_5>0
\Longrightarrow
v_5(U_{12}^{\rm prim})=0.
\]

下一步应分别处理：

#### A1. common-scale branch

若 \(v_5(L)\) 的线性部分由

\[
2v_5(c),\quad v_5(Q_1),\quad2v_5(\Omega)
\]

支付，则把这些 common-scale depth 送进：

- denominator overlap；
- primitive carry；
- reducedness；
- \(F_-/E\) 双边 factor allocation。

目标是证明它们无法同时承担正比例高度。

#### A2. angular branch

若正线性五进高度进入

\[
\omega_5=v_5(X_1^2+Y_1^2),
\]

则 bottom edge \(\theta_{12}\) 不携带这份深度。

结合 tetrahedron ultrametric，其他两条边必须承担传播的 \(m_3\)-deep contact。

再用无 \(E_D\) eliminant 把 simultaneous contact 压到

\[
M/\eta
\quad\text{或}\quad
R/\eta
\]

单一 tail factor。

这一分支很可能能形成

\[
0<|\Theta|<\text{forced divisor}\le|\Theta|
\]

型直接矛盾。

---

### 89. 路线 B：same-prime Gaussian resultant

terminal frontier 已经把全部 exponential entropy 转移到

\[
(C_L,\Pi).
\]

而 \(\Pi\) 的每个 prime-power orientation 同时出现在：

- pair-max condition；
- secondary Gaussian congruence；
- carrier/projective angular structure；
- decimal prefix determinant。

最有价值的下一步是：

> 对同一个 \(p^h\Vert C_L\)，把 pair-max Hensel orientation 与 decimal/carry residual 写在同一个 \(\mathbf Z[i]/(\pi_p^h)\) 系统里，消去 moving numerator/quotient，构造一个只依赖 denominator mode 与 subexponential coefficient 的 same-prime resultant。

如果得到一个 nonzero resultant \(\Theta_p\)，且

\[
\pi_p^h\mid\Theta_p
\]

对总共 \(C_L=10^{S+o(S)}\) 的 prime mass 成立，而

\[
|\Theta|=10^{o(S)}
\]

或严格小于 \(C_L\)，则 frontier 会直接关闭。

这是当前最贴近最终矛盾的路线。

---

### 90. 路线 C：把 terminal Gaussian orientation 接回一般 carrier tetrahedron

terminal 线目前把 \(C_L\) 看成 moving pair-max core；

一般结构线已经有：

- \(\theta_{12},\theta_{13},\theta_{23}\) 的 ultrametric；
- projective \(Z_0\) depth；
- angular/bottom exclusion；
- carrier-circle eliminant。

很可能可以证明：

> 一个占 \(S+o(S)\) 高度的 pair-max Gaussian core若在 terminal secondary congruence 中选择 orientation，那么同一 orientation 会强迫 tetrahedron 两条独立 residual 同时发生过深接触；而 5-adic angular/bottom exclusion 阻止这份深度在 bottom edge 中循环，因此必须落到单侧 tail factor。该 tail factor与 \(C_L\) 的 asymptotic coprimality 再产生矛盾。

这条路线可以把 terminal 的特殊变量重新翻译成全局 projective invariant，理论上更有希望得到真正的 DD closure。

---

### 91. 路线 D：absolute \(S\) bound 之后再有限证书

一旦解析结构给出

\[
S\le S_0
\]

且 \(S_0\) 实用，已有证书框架可以继续：

- denominator-tail exact generation；
- valuation-state exact Hensel；
- CRT；
- modular-square filter；
- exact multiprecision discriminant square test。

现在没有必要提前对未知巨大 \(S_0\) 做逐层枚举。

---

## 第二十七部分：后续本地 Agent 应采用的工作状态

建议把当前 DD 状态写成下面这组“不可丢失”的事实。

### 92. 全局严格/解析事实

\[
n_3=8S-1
\quad\text{整层为空},
\]

\[
n_3\le8S-2,
\]

\[
n_3<
\frac{31}{4}S+\frac{6581}{960},
\]

\[
\limsup\frac{m_3}{S}\le5,
\]

\[
\boxed{
\limsup_{\rm DD}\frac{n_3}{S}
\le
6.308883577618\ldots
}
\]

（后两项中的渐近常数依赖 Schmidt Subspace Theorem，阈值非有效）。

同时：

\[
\text{surplus modes}\le11.
\]

---

### 93. tail / local arithmetic

\[
QG<\kappa\le10QG,
\]

\[
\frac{Q^2}{11}<\kappa<10Q^2,
\]

\[
10^m\mid\kappa^2(\kappa+2G),
\]

\[
v_p(F_-)=
v_p(E)+v_p(\kappa)+v_p(\kappa+2G)
-v_p(\kappa+G)-v_p(Q).
\]

reduced tail：

\[
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
\]

\[
Q<\frac uv\le10Q.
\]

---

### 94. primitive exact-lift skeleton

\[
D=(H,q),
\qquad
D\mid g_*,
\]

\[
\alpha=CH_0,
\qquad
\beta=Cq_0,
\qquad
(C,10)=1,
\]

\[
A_{12}10^dq_0-QH_0=E',
\]

\[
b_3H_0-a_3q_0=10^mE',
\]

\[
DE'=\tau a.
\]

---

### 95. scale-free system

\[
v\omega A_{12}10^d-a_3Q_1=wa_0,
\]

以及

\[
L c^4\lambda^2r^2w(LQ_1+2v)x^2
-2L c^4\lambda^2r^2v(LQ_1+v)A_{12}10^d x
+\eta^2\mathcal N_{12}Q_1w
=0,
\]

\[
x=a_0/\omega.
\]

并有

\[
\boxed{
L\mid\mathcal N_{12}Q_1\Omega^2.
}
\]

---

### 96. determinant/projective system

\[
\theta_{12},
\quad
\theta_{13},
\quad
\theta_{23}
\]

满足每个 \(p\) 处两个最小 valuation 相等。

nested carry：

\[
CC_P\varepsilon_P
=
g_2\theta_{23}
+
10^{m_2}g_1\theta_{13},
\]

\[
CC_{23}\varepsilon_1
=
\theta_{13}
+
10^{m_3}g_2\theta_{12}.
\]

stereographic circle：

\[
|R_0z-\mathcal C|^2=LE_D.
\]

无 \(E_D\) eliminant：

\[
\Xi
=
(LQ+\tau)^2(LQ+2\tau)^2
(10^{2k}+10^{2d}).
\]

projective depth：

\[
v_p(Z_0)
=
\max(0,r_p+\omega_p-\alpha_p).
\]

五进 angle/bottom exclusion：

\[
\boxed{
\omega_5>0
\Longrightarrow
v_5(U_{12}^{\rm prim})=0.
}
\]

---

### 97. terminal frontier system

只在假想 \(n/S\to6.308883\ldots\) 序列上使用：

\[
5^TU+V=2^HZ,
\]

\[
C_L=10^{S+o(S)},
\]

\[
q_c=10^{0.3088835776S+o(S)},
\]

\[
(C_L,q_c)=1,
\]

\[
(C_L,L)=10^{o(S)}.
\]

oriented Gaussian core：

\[
N(\Pi)=C_L.
\]

secondary congruence：

\[
\Pi
\mid
A_*2^{m-2}q_c-iB_*5^{2T-m}.
\]

真正 denominator quotient：

\[
R_2
=
\frac{5^T\widetilde r+s q_c\theta}{2^{m_2}},
\]

\[
\operatorname{core}_{10}(R_2)
=
10^{1.007853581954S+o(S)}.
\]

source residue：

\[
s\theta q_c
\equiv
-5^T\widetilde r
\pmod{2^{m_2}}.
\]

最后 entropy margin：

\[
\delta_*
=
0.007853581954\ldots.
\]

固定 \((C_L,\Pi)\) 后，Gaussian residue 将最后的 \(q_c/R_2\) lift 压到至多一个。

---

## 第二十八部分：推荐的下一次证明任务

后续本地继续时，不建议再从头重跑所有 valuation states。更合适的单次目标是：

### 98. 首选目标

**证明 moving pair-max Gaussian core 的 uniform same-prime incompatibility。**

可尝试以下具体形式：

> 对任意假想 frontier sequence，取 \(p^h\Vert C_L\) 的 oriented Gaussian prime \(\pi^h\Vert\Pi\)。利用 pair-max Gaussian condition、secondary residue、carrier tetrahedron 与 decimal carry，构造 \(\Theta_p\in\mathbf Z[i]\)，使
>
> \[
> \pi^h\mid\Theta_p,
> \]
>
> 而在抽去所有 decimal/projective/common-scale baseline 后，
>
> \[
> N(\Theta_p)=p^{o(h)}
> \]
>
> 或全局乘积满足
>
> \[
> 0<N(\Theta)<C_L\le N(\Theta).
> \]
>
> 若能做到，即可关闭 \(6.308883\ldots\) frontier。

### 99. 第二目标

若首选路线暂时卡住，则先完成一般 DD 的：

\[
\boxed{
\text{projective denominator/common-scale allocation lemma}
}
\]

把 §27.45–27.46 的 \(Z_0\) 槽彻底支付掉。

特别是分别关闭：

- common-scale branch；
- 5-adic angular branch。

只要证明任何 positive-linear carrier excess 都必须进入一个单侧 tail factor，而该 factor 又不能与 moving Gaussian core 共享线性高度，就可以从结构上得到 \(S\le S_0\)。

### 100. 暂不优先

以下方向目前边际收益较低：

- 继续手工降低 \(6.308883\) 的小数；
- 对单个奇素数再做更深 Hensel；
- 重复 quadratic character；
- 再做一轮 fixed-target Subspace；
- 在尚无绝对 \(S_0\) 时大规模 finite enumeration。

---
