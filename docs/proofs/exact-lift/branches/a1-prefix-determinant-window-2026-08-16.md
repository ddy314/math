# A1 cross-layer prefix determinant window — 2026-08-16

本文开始统一处理最高层以外的三个 `s_1-g` 层。

定义 carrier determinant

\[
\boxed{
J:=10^k a_1b_2-a_2b_1.
}
\]

由第一坐标严格承担 carrier：

\[
10^k r_1>r_2,
\]

所以

\[
\boxed{J\in\mathbf Z_{>0}.}
\]

本文证明，在除少数低 `g` chamber 外、且 `m_1` 不短时，`J` 被压入一个宽度常数的 `10^{-2k}` 窗；特别地得到新的 moving-prefix 线性锥和 `J\in\{1,2\}` 边界核。

本文结论均为 **已严格完成**。

---

## 1. 四层统一参数

记

\[
\boxed{d=s_1-g\in\{-1,0,1,2\}.}
\]

仍令

\[
a=10^{-2k},
\qquad
A_0=10^k r_1,
\qquad
 t=\frac{r_2}{A_0},
\qquad
 z=\frac{r_3}{A_0}.
\]

prefix contact 记为

\[
u=\frac{P}{A_0}
=(1-\lambda)+\lambda10^{-g}t,
\qquad
\lambda=\frac{b_2}{Q}.
\]

有

\[
0<t<1,
\qquad
0<u<1.
\]

并且

\[
\boxed{
1-t
=\frac{J}{10^ka_1b_2}.}
\tag{1}
\]

---

## 2. 一个无条件的 lower gap

rational contact 给出

\[
P>R.
\]

所以

\[
u^2>\frac{R^2}{A_0^2}
=a+t^2+z^2.
\]

又 `u<1`，故

\[
t^2<1-a.
\]

于是

\[
1-t
>1-\sqrt{1-a}
=\frac{a}{1+\sqrt{1-a}}
>\frac a2.
\]

因此整个 A1 无条件满足

\[
\boxed{
1-t>\frac12\,10^{-2k}.}
\tag{2}

---

## 3. 第三坐标在 generic chamber 中不超过 `a`

A1 第三分数满足

\[
r_3<10^{1-g}.
\]

另一方面

\[
s_1=g+d,
\]

所以

\[
r_1>10^{s_1-1}=10^{g+d-1}.
\]

从而

\[
A_0=10^k r_1>10^{k+g+d-1}.
\]

因此

\[
z
<10^{2-k-2g-d},
\]

即

\[
z^2
<10^{4-4g-2d}\,a.
\tag{3}
\]

若

\[
\boxed{2g+d\ge2,}
\tag{4}
\]

则

\[
\boxed{z^2<a.}
\tag{5}

对四个位数层，(4) 只排除以下低尺度 chamber：

\[
(d,g)=(1,0),(0,0),(-1,0),(-1,1).
\]

最高层 `d=2` 没有例外。

---

## 4. `m_1\ge2k+2` 时 prefix weight 也进入 `a` 级

因为

\[
Q=b_1 10^{m_2}+b_2,
\]

有粗界

\[
\lambda=\frac{b_2}{Q}<10^{1-m_1}.
\]

若

\[
\boxed{m_1\ge2k+2,}
\tag{6}
\]

则

\[
\boxed{
\lambda<10^{-2k-1}=\frac a{10}.}
\tag{7}

---

## 5. Contact 给出 upper gap

定义

\[
\Delta
:=u^2-t^2-a-z^2
=\frac{P^2-R^2}{A_0^2}>0.
\]

已有 rational-contact 上界

\[
\Delta
<c_Q(a+t^2+z^2),
\]

其中

\[
c_Q=\frac{2+1/Q}{Q}.
\]

因为

\[
\frac1Q\le\lambda<1,
\]

有

\[
\boxed{c_Q<3\lambda.}
\tag{8}

同时

\[
1-u
=\lambda(1-10^{-g}t)
<\lambda,
\]

所以

\[
\boxed{1-u^2<2\lambda.}
\tag{9}

由

\[
1-t^2
=a+z^2+(1-u^2)+\Delta
\]

和 `a+t^2+z^2<u^2<1`，得到

\[
1-t^2
<a+z^2+2\lambda+3\lambda.
\]

在 (4)、(6) 下，使用 (5)、(7)：

\[
1-t^2
<2a+\frac a2
=\frac52a.
\]

因此

\[
\boxed{
1-t<\frac52\,10^{-2k}.}
\tag{10}

结合 (2)：

\[
\boxed{
\frac12\,10^{-2k}
<1-t<
\frac52\,10^{-2k}.}
\tag{11}

---

# 6. Carrier determinant 窗

由 (1)、(11)：

\[
\boxed{
\frac{a_1b_2}{2\,10^k}
<J<
\frac{5a_1b_2}{2\,10^k}.}
\tag{12}

这是一个跨四个位数层的整数窗口。

---

## 7. 新 moving-prefix 线性锥

若

\[
n_1+m_2\le k-1,
\]

则

\[
a_1b_2<10^{n_1+m_2}\le10^{k-1}.
\]

由 (12)：

\[
J<\frac52\cdot10^{-1}<1,
\]

与

\[
J\in\mathbf Z_{>0}
\]

矛盾。

所以在 (4)、(6) 的 generic chamber 中：

\[
\boxed{n_1+m_2\ge k.}
\tag{13}

由于

\[
n_1=m_1+g+d,
\]

也可写成

\[
\boxed{
 m_1+m_2+g+d\ge k.}
\tag{14}

---

# 8. 取等边界只有两个 determinant 常数核

若

\[
\boxed{n_1+m_2=k,}
\tag{15}

则

\[
a_1b_2<10^k.
\]

由 (12)：

\[
0<J<\frac52.
\]

所以

\[
\boxed{J\in\{1,2\}.}
\tag{16}

即边界 (15) 被精确压成两个 Bézout 型方程：

\[
\boxed{
10^k a_1b_2-a_2b_1=1
}
\]

或

\[
\boxed{
10^k a_1b_2-a_2b_1=2.
}
\]

这为三个较低位数层提供了第一个真正的整数边界核。

---

# 9. 后续分工

因此对

\[
d\in\{-1,0,1\}
\]

可以分成：

1. 四个低 `g` chamber：
   \[
   (1,0),(0,0),(-1,0),(-1,1);
   \]
2. `m_1\le2k+1` 的短第一分母锥；
3. `m_1\ge2k+2` 的 generic determinant cone，其中
   \[
   n_1+m_2\ge k;
   \]
4. 取等层 `n_1+m_2=k` 只剩 `J=1,2`。

下一步应优先关闭 `J=1,2`，再处理严格层 `n_1+m_2>k`。