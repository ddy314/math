# A1 top-layer edge closure and slope-4 gap — 2026-08-16

本文继续 `a1-top-layer-repunit-edge-gap-2026-08-16.md`。

核心进展：

1. 第一条 `m_1=2k` repunit 边缘现已**整条关闭**；
2. 第二条 `n_2=2k` repunit 边缘进一步从 `m_1\ge3k+1` 推到
   \[
   \boxed{m_1\ge4k+1},
   \]
   并且新的取等边界只有常数个十进制偏移。

本文结论均为 **已严格完成**。

---

# 1. 第一 repunit 边缘完整关闭

前文已经把 `m_1=2k` 唯一可能边缘压成

\[
\boxed{
 g=0,
\quad
 b_1=10^{2k}-1,
\quad
 a_1=10^{2k+1},
\quad
 n_2\ge3k+1.
}
\tag{1}
\]

记

\[
a=10^{-2k}.
\]

则

\[
r_1
=\frac{10^{2k+1}}{10^{2k}-1}
=\frac{10}{1-a}.
\]

令

\[
A_0=10^k r_1,
\qquad
t=\frac{r_2}{A_0},
\qquad
z=\frac{r_3}{A_0}.
\]

最高层四端点乘积中，`b_1` 因子等于 `1-a`，其余因子都不超过 `1`，故

\[
\boxed{t\le1-a.}
\tag{2}
\]

另一方面 `g=0` 且 `r_3<10`，所以

\[
\boxed{z^2<a(1-a)^2.}
\tag{3}
\]

---

## 1.1 `\lambda` 与 contact correction 已降到二阶

由此前最高层边缘估计：

\[
\boxed{\lambda<\frac a9.}
\tag{4}
\]

又因 `g=0`，

\[
n_2=m_2+k.
\]

由 (1)：

\[
m_2\ge2k+1.
\]

所以

\[
b_2\ge10^{m_2-1}\ge10^{2k}=a^{-1}.
\]

记

\[
h=\frac1Q.
\]

因为

\[
h=\frac\lambda{b_2},
\]

由 (4)：

\[
\boxed{h<\frac{a^2}{9}.}
\tag{5}
\]

于是

\[
c_Q=2h+h^2<\frac14a^2.
\tag{6}
\]

并且

\[
a+t^2+z^2<1+2a<\frac{51}{50}.
\]

所以 contact correction 满足

\[
\boxed{
 c_Q(a+t^2+z^2)
<\frac{51}{200}a^2.
}
\tag{7}
\]

---

## 1.2 Prefix defect 比最大第三坐标仍多出固定二阶量

因为 `g=0`：

\[
u=1-\lambda(1-t).
\]

写

\[
d=1-t.
\]

由 (2)：

\[
d\ge a.
\]

同时最高层已有 `d<5a`，所以 `d<1/(1+\lambda)`，以下关于 `d` 的二次式在该区间递增。

prefix defect

\[
F=u^2-t^2-a
\]

精确写成

\[
F
=2(1-\lambda)d-(1-\lambda^2)d^2-a.
\]

因此在 `d\ge a` 上

\[
F
\ge
2(1-\lambda)a-(1-\lambda^2)a^2-a.
\]

由 (4)：

\[
\boxed{
F>a-\frac{11}{9}a^2.
}
\tag{8}
\]

而 (3) 给出

\[
z^2<a-2a^2+a^3.
\]

所以

\[
F-z^2
>
\left(\frac79-a\right)a^2.
\]

因为 `a\le1/100`：

\[
\boxed{F-z^2>\frac34a^2.}
\tag{9}
\]

但 rational contact 必须满足

\[
F<z^2+c_Q(a+t^2+z^2),
\]

由 (7)：

\[
F-z^2<\frac{51}{200}a^2.
\]

这与 (9) 冲突，因为

\[
\frac34>\frac{51}{200}.
\]

因此

\[
\boxed{
 m_1=2k
\text{ 的最高层 repunit 边缘完全为空}.}
\tag{10}
\]

---

# 2. 第二 repunit 边缘重新参数化

现在只剩另一条取等边缘：

\[
\boxed{
 g=0,
\quad
 n_2=2k,
\quad
 a_2=10^{2k}-1,
\quad
 b_2=10^{k-1},
}
\tag{11}
\]

前文已证明

\[
m_1\ge3k+1.
\]

写第一块 normal form：

\[
b_1=10^{m_1}(1-D),
\qquad
D=\frac{d_1}{10^{m_1}}>0,
\]

\[
a_1=10^{n_1-1}(1+E),
\qquad
E=\frac{e_1}{10^{n_1-1}}\ge0.
\]

最高层 `g=0,s_1=2` 给出

\[
n_1-1=m_1+1.
\]

定义

\[
\boxed{
w=\frac{1-D}{1+E},
\qquad
x=1-w.}
\tag{12}
\]

则

\[
\boxed{t=(1-a)w=(1-a)(1-x),}
\tag{13}
\]

并且

\[
r_1=\frac{10}{w}.
\]

因为 `r_3<10`：

\[
\boxed{z^2<a w^2.}
\tag{14}
\]

---

# 3. `x` 与 `\lambda` 的直接比较

最高层已有

\[
1-t<5a.
\]

由 (13)：

\[
1-t=a+(1-a)x<5a,
\]

所以

\[
\boxed{x<\frac{4a}{1-a}<\frac4{99}.}
\tag{15}
\]

normal form 还给出

\[
0\le E<\frac{5a}{1-5a}<\frac1{19},
\qquad
0<D<\frac1{19}.
\]

由

\[
x=\frac{D+E}{1+E},
\]

可得

\[
D<(1+E)x<\frac{20}{19}x.
\tag{16}
\]

本边缘上

\[
\lambda=\frac1{10b_1+1}.
\]

又 `d_1\ge1`，故

\[
D\ge10^{-m_1}.
\]

因此

\[
\lambda
<
\frac{10^{-m_1}}{10(1-D)}
\le
\frac{D}{10(1-D)}.
\]

用 `D<1/19` 与 (16)：

\[
\boxed{\lambda<\frac{x}{9}.}
\tag{17}
\]

另外

\[
\frac1Q=\frac\lambda{b_2}\le\lambda,
\]

故由 (15)、(17)：

\[
\boxed{c_Q<\frac{x}{4}.}
\tag{18}
\]

---

# 4. Contact 把 `x` 压到 `O(a^2)`

由

\[
u=1-\lambda(1-t)
\]

有

\[
u^2>1-2\lambda(1-t).
\]

利用 (13)：

\[
F
=u^2-(1-a)^2w^2-a.
\]

再减去第三坐标最大值 `aw^2`：

\[
F-aw^2
>
(1-a)-(1-a+a^2)w^2
-2\lambda(1-t).
\]

记

\[
B=1-a+a^2>\frac{99}{100}.
\]

因为 `w=1-x`：

\[
(1-a)-Bw^2
=-a^2+B(2x-x^2).
\]

所以

\[
F-aw^2
>
-a^2+B(2x-x^2)-2\lambda(1-t).
\tag{19}
\]

由 (15)：

\[
2x-x^2>\frac{39}{20}x.
\]

故

\[
B(2x-x^2)>
\frac{3861}{2000}x.
\tag{20}
\]

又由 (17) 与 `1-t<5a`：

\[
2\lambda(1-t)
<\frac{10a}{9}x
\le\frac1{90}x.
\tag{21}
\]

contact 给出

\[
F-aw^2
<c_Q(a+t^2+z^2).
\]

而由 (18)：

\[
c_Q(a+t^2+z^2)
<\frac{x}{4}\frac{51}{50}
=\frac{51}{200}x.
\tag{22}
\]

综合 (19)–(22)：

\[
\frac{3861}{2000}x
<
a^2+rac1{90}x+rac{51}{200}x.
\]

因此

\[
\boxed{x<\frac{61}{100}a^2.}
\tag{23}
\]

这里使用了一个略松但方便的有理常数 `61/100`。

---

# 5. 整数颗粒度把斜率推到 4

由 (16)、(23)：

\[
D<\frac{20}{19}\frac{61}{100}a^2
<\frac{13}{20}a^2.
\tag{24}
\]

但

\[
D=\frac{d_1}{10^{m_1}},
\qquad d_1\ge1,
\]

所以

\[
10^{-m_1}\le D<\frac{13}{20}10^{-4k}.
\]

若 `m_1\le4k`，左侧至少为 `10^{-4k}`，矛盾。

因此

\[
\boxed{
 m_1\ge4k+1.
}
\tag{25}

这把前文 `m_1\ge3k+1` 再推进整整一个斜率层。

---

# 6. 新边界 `m_1=4k+1` 只有常数偏移

若

\[
\boxed{m_1=4k+1,}
\]

则由 (24)：

\[
d_1
=D10^{m_1}
<\frac{13}{20}10^{-4k}10^{4k+1}
=\frac{13}{2}.
\]

因此

\[
\boxed{d_1\in\{1,2,3,4,5,6\}.}
\tag{26}
\]

即

\[
\boxed{
 b_1=10^{4k+1}-d_1,
\qquad d_1\in\{1,\dots,6\}.
}
\]

同时由 `x<61a^2/100` 和

\[
E=\frac{x-D}{1-x}<\frac{x}{1-x}
\]

可得一个绝对常数级上界

\[
e_1=E10^{n_1-1}<61.
\]

所以该新取等边界已经退化成有限个 `(d_1,e_1)` 常数偏移类型；它仍是关于 `k` 的无界族，但其十进制局部形状已经完全有限化。

---

# 7. 当前最高层边缘状态

最高层 `s_1=g+2` 的边缘现在变成：

- `m_1=2k`：**整条为空**；
- `n_2=2k`：只能是
  \[
  g=0,
  \quad a_2=10^{2k}-1,
  \quad b_2=10^{k-1},
  \quad m_1\ge4k+1;
  \]
- 新边界 `m_1=4k+1`：`b_1` 只剩六个常数 deficit，`a_1` 只剩常数级 lower-end excess。

所以最高层真正的边缘核已经被压成一个 slope-4 的极窄 repunit/Hensel 型族。