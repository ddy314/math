# A1 top-layer third-block edge — 2026-08-16

本文继续第二 repunit / slope-4 边缘：

\[
\boxed{
 g=0,
\quad n_2=2k,
\quad a_2=10^{2k}-1,
\quad b_2=10^{k-1},
\quad m_1\ge4k+1.
}
\]

前文已把第一块压到极端端点。本文证明第三分数也必须逼近上端点 `10`，从而得到新的第三尾斜率：

\[
\boxed{\ell\ge2k+1.}
\]

并把新取等层 `\ell=2k+1` 压成常数偏移核。

本文结论均为 **已严格完成**。

---

## 1. 复用的 slope-4 参数

记

\[
a=10^{-2k}.
\]

第一块写成

\[
b_1=10^{m_1}(1-D),
\qquad
 a_1=10^{n_1-1}(1+E),
\]

并定义

\[
w=\frac{1-D}{1+E},
\qquad
x=1-w.
\]

前文已经严格得到

\[
\boxed{x<\frac{61}{100}a^2.}
\tag{1}
\]

以及

\[
\boxed{t=(1-a)w.}
\tag{2}
\]

最高层还有

\[
1-t<5a.
\tag{3}
\]

本边缘 `g=0`，所以

\[
u=1-\lambda(1-t).
\]

并且由 `\lambda<x/9`：

\[
\boxed{\lambda<\frac{61}{900}a^2.}
\tag{4}
\]

contact correction 仍满足

\[
\boxed{
c_Q(a+t^2+z^2)<\frac{16}{100}a^2.}
\tag{5}
\]

这里使用 `c_Q<x/4` 与 `a+t^2+z^2<51/50` 的已有估计。

---

## 2. 第三坐标必须吃掉 prefix defect 的主阶

由

\[
u^2>1-2\lambda(1-t)
\]

和 (2)：

\[
F=u^2-t^2-a
>
1-2\lambda(1-t)-(1-a)^2-a.
\]

由 (3)、(4)：

\[
2\lambda(1-t)
<10a\lambda
<\frac{61}{90}a^3.
\]

所以

\[
\boxed{
F>a-a^2-\frac{61}{90}a^3.
}
\tag{6}
\]

rational contact 给出

\[
F<z^2+c_Q(a+t^2+z^2).
\]

结合 (5)、(6)：

\[
z^2
>
a-rac{29}{25}a^2
\]

（右侧常数 `29/25` 是对 `a\le1/100` 的安全粗化）。因此

\[
\boxed{
z^2>a\left(1-\frac65a\right).}
\tag{7}
\]

---

## 3. `r_3` 被压到 10 的上端点

本边缘

\[
r_1=\frac{10}{w},
\]

所以

\[
A_0=10^k r_1
=\frac{10^{k+1}}w.
\]

于是

\[
r_3=zA_0
=10\frac{z/\sqrt a}{w}.
\]

由 `w<1` 与 (7)：

\[
\frac{z}{\sqrt a}
>
\sqrt{1-\frac65a}
>1-\frac65a.
\]

因此

\[
\boxed{
 r_3
>10\left(1-\frac65a\right).
}
\tag{8}
\]

即

\[
\boxed{
10-r_3<12\cdot10^{-2k}.}
\]

---

## 4. 第三块十进制端点正规形

这里 `g=0`，所以

\[
m_3=\ell=n_3.
\]

令

\[
T=10^\ell,
\qquad
\eta=\frac{a_3}{T},
\qquad
\rho=\frac{b_3}{T}.
\]

有

\[
\frac1{10}\le\eta,\rho<1,
\qquad
r_3=\frac\eta\rho.
\]

由 `\rho\ge1/10` 与 (8)：

\[
\eta=r_3\rho
>1-\frac65a.
\]

所以正整数 deficit

\[
\boxed{d_3:=T-a_3\ge1}
\]

满足

\[
\boxed{
1\le d_3<\frac65aT
=\frac65\,10^{\ell-2k}.}
\tag{9}
\]

另一方面 `\eta<1` 与 (8) 给出

\[
\rho<\frac1{10(1-6a/5)}.
\]

定义

\[
\boxed{e_3:=b_3-10^{\ell-1}\ge0.}
\]

则

\[
\boxed{
0\le e_3
<
\frac{3a}{25(1-6a/5)}T
<\frac18\,10^{\ell-2k}.}
\tag{10}
\]

---

## 5. 整数颗粒度先给出 `\ell\ge2k`

由 (9)，`d_3\ge1`。

若

\[
\ell\le2k-1,
\]

则

\[
\frac65 10^{\ell-2k}
\le\frac{6}{50}<1,
\]

与 (9) 矛盾。

所以

\[
\boxed{\ell\ge2k.}
\tag{11}
\]

---

# 6. 取等层 `\ell=2k` 被唯一确定

若

\[
\boxed{\ell=2k,}
\]

则 (9)：

\[
1\le d_3<\frac65,
\]

所以

\[
\boxed{d_3=1.}
\]

而 (10)：

\[
0\le e_3<\frac18,
\]

所以

\[
\boxed{e_3=0.}
\]

因此唯一可能第三块为

\[
\boxed{
 a_3=10^{2k}-1,
\qquad
 b_3=10^{2k-1}.
}
\tag{12}

此时

\[
\boxed{r_3=10(1-a).}
\tag{13}
\]

又本边缘

\[
\frac{r_2}{10^k}=10(1-a),
\]

所以

\[
r_3=\frac{r_2}{10^k}.
\]

进而

\[
\boxed{z^2=a t^2.}
\tag{14}
\]

---

# 7. `\ell=2k` 与 contact correction 冲突

由 (14)：

\[
F-z^2
=u^2-(1+a)t^2-a.
\]

使用

\[
u^2>1-2\lambda(1-t),
\qquad
t\le1-a,
\]

得到

\[
F-z^2
>
1-2\lambda(1-t)
-(1+a)(1-a)^2-a.
\]

而

\[
(1+a)(1-a)^2
=1-a-a^2+a^3.
\]

所以

\[
F-z^2
>a^2-a^3-2\lambda(1-t).
\]

由 (3)、(4)：

\[
2\lambda(1-t)<\frac{61}{90}a^3.
\]

因此

\[
\boxed{
F-z^2>\frac{49}{50}a^2.
}
\tag{15}
\]

另一方面 `m_1\ge4k+1` 与 normal form 给出

\[
b_1>(1-5a)10^{4k+1},
\]

所以

\[
\lambda=\frac1{10b_1+1}<\frac{a^2}{90}.
\]

本边缘 `b_2=10^{k-1}`，故

\[
\frac1Q=\frac\lambda{b_2}\le\lambda<\frac{a^2}{90}.
\]

从而

\[
c_Q<\frac{a^2}{40}.
\]

因此 contact 必须给出

\[
F-z^2
<c_Q(a+t^2+z^2)
<\frac{51}{2000}a^2.
\tag{16}
\]

(15) 与 (16) 矛盾。

所以

\[
\boxed{\ell=2k\text{ 整层为空}.}
\tag{17}
\]

结合 (11)：

\[
\boxed{\ell\ge2k+1.}
\tag{18}
\]

---

# 8. 新边界 `\ell=2k+1` 是第三块常数核

若

\[
\boxed{\ell=2k+1,}
\]

则由 (9)：

\[
1\le d_3<12,
\]

所以

\[
\boxed{d_3\in\{1,2,\dots,11\}.}
\tag{19}
\]

由 (10)：

\[
0\le e_3<\frac{10}{8},
\]

所以

\[
\boxed{e_3\in\{0,1\}.}
\tag{20}
\]

即新边界只有

\[
\boxed{
 a_3=10^{2k+1}-d_3,
\quad1\le d_3\le11,
}
\]

\[
\boxed{
 b_3=10^{2k}+e_3,
\quad e_3\in\{0,1\}.
}
\]

若 `e_3=0`，既约性进一步要求 `d_3` 与 `10` 互素；若 `e_3=1`，则

\[
10b_3-a_3=10+d_3
\]

把既约性化成一个模数不超过 `21` 的固定 gcd 条件。

所以第二 repunit 边缘现在同时具有：

- 第一块 slope-4 constant core；
- 第三块 slope-2+1 constant core。

这已经把该边缘压成两个有限常数偏移系统与无界参数 `k` 的组合。