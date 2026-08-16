# A1 top-layer uniform cone — 2026-08-16

本文强化 `a1-global-digit-band-and-top-layer-cone-2026-08-16.md` 的最高层分析。

旧文件 §§5–6 已经对泛型区域推出分情况的 `(m_1,k)` 锥；这里利用最高层 `s_1=g+2` 自身提供的更强第三坐标估计，把所有 `g\ge0, k\ge1`（包括 `(g,k)=(0,1),(0,2)`）统一成一条结论：

\[
\boxed{
s_1=g+2\Longrightarrow m_1\ge2k.
}
\]

本文结论均为 **已严格完成**。

---

## 1. 最高层的端点不等式

沿用

\[
A_0=10^k r_1,
\qquad
t=\frac{r_2}{A_0},
\qquad
z=\frac{r_3}{A_0},
\]

\[
\lambda=\frac{b_2}{Q},
\qquad
Q=b_1 10^{m_2}+b_2,
\]

\[
u=\frac{P}{A_0}
=(1-\lambda)+\lambda10^{-g}t,
\]

以及

\[
a=10^{-2k}.
\]

无量纲 prefix defect 为

\[
F=u^2-t^2-a.
\tag{1}
\]

由 rational contact：

\[
\boxed{
F<z^2+c_Q(a+t^2+z^2),
\qquad
c_Q=\frac{2+1/Q}{Q}.
}
\tag{2}
\]

最高层

\[
s_1=g+2
\]

已经在前文严格推出十进制端点损失

\[
\boxed{
t<\frac{1-\lambda}{1+9\lambda}.}
\tag{3}
\]

---

## 2. 最高层专属的第三坐标绝对界

由

\[
s_1=g+2
\]

和位数窗，

\[
r_1>10^{s_1-1}=10^{g+1}.
\]

因此

\[
A_0=10^k r_1>10^{k+g+1}.
\]

另一方面 `s_3=-g`，所以

\[
r_3<10^{s_3+1}=10^{1-g}.
\]

于是

\[
\boxed{
z<10^{-k-2g}.}
\tag{4}
\]

记

\[
\boxed{\zeta=10^{-k-2g},}
\qquad
\zeta^2=10^{-2k-4g}.
\]

则 `z^2<\zeta^2`。

这一步只使用最高层位数，不需要 `k+2g\ge3`，所以两个旧低尺度角落同样覆盖。

---

## 3. 一个统一 contact 下界

因为

\[
u>1-\lambda,
\]

由 (1)、(2)、`z^2<\zeta^2`：

\[
(1-\lambda)^2-t^2-a
<
\zeta^2+c_Q(a+t^2+\zeta^2).
\]

因此

\[
\boxed{
(1-\lambda)^2
<
(1+c_Q)(t^2+a+\zeta^2).
}
\tag{5}
\]

令

\[
h=\frac1Q.
\]

和前文一样，

\[
h\le1-2\lambda,
\]

所以

\[
1+c_Q=(1+h)^2\le4(1-\lambda)^2.
\]

代回 (5)：

\[
1<4(t^2+a+\zeta^2).
\]

故

\[
\boxed{
t^2>\frac14-a-\zeta^2.}
\tag{6}
\]

最坏情形是 `k=1,g=0`，此时

\[
a=\zeta^2=\frac1{100}.
\]

所以整个最高层统一满足

\[
\boxed{
t^2>\frac{23}{100}.}
\tag{7}
\]

而

\[
\frac{23}{100}>\left(\frac9{19}\right)^2.
\]

所以

\[
t>\frac9{19}.
\]

如果 `\lambda\ge1/10`，则由 (3)

\[
t<\frac{1-1/10}{1+9/10}=\frac9{19},
\]

矛盾。因此最高层无条件有

\[
\boxed{\lambda<\frac1{10}.}
\tag{8}
\]

---

## 4. 统一的 `\lambda` 指数锥

将端点上界 (3) 代入 (5)：

\[
(1-\lambda)^2
<
(1+c_Q)
\left(
\frac{(1-\lambda)^2}{(1+9\lambda)^2}
+a+\zeta^2
\right).
\]

约去 `(1-\lambda)^2`：

\[
\frac1{1+c_Q}
<
\frac1{(1+9\lambda)^2}
+
\frac{a+\zeta^2}{(1-\lambda)^2}.
\tag{9}
\]

又因为 `b_2\ge1`，

\[
\frac1Q\le\lambda,
\]

故

\[
1+c_Q=\left(1+\frac1Q\right)^2
\le(1+\lambda)^2.
\]

所以 (9) 强迫

\[
\frac1{(1+\lambda)^2}
-
\frac1{(1+9\lambda)^2}
<
\frac{a+\zeta^2}{(1-\lambda)^2}.
\tag{10}
\]

左侧精确为

\[
\frac{16\lambda(1+5\lambda)}
{(1+\lambda)^2(1+9\lambda)^2}.
\]

由 (8)，`0<\lambda<1/10`；在该区间

\[
\frac{16(1+5\lambda)}
{(1+\lambda)^2(1+9\lambda)^2}
>\frac72.
\]

同时

\[
\frac1{(1-\lambda)^2}<\frac{100}{81}.
\]

因此由 (10)：

\[
\frac72\lambda
<
\frac{100}{81}(a+\zeta^2).
\]

即

\[
\boxed{
\lambda
<
\frac{200}{567}
\left(10^{-2k}+10^{-2k-4g}\right).
}
\tag{11}
\]

提取 `10^{-2k}`：

\[
\boxed{
\lambda
<
\frac{200}{567}
10^{-2k}(1+10^{-4g}).
}
\tag{12}
\]

由于 `g\ge0`，

\[
1+10^{-4g}\le2,
\]

所以得到简单统一粗化：

\[
\boxed{
\lambda
<
\frac{400}{567}10^{-2k}
<
\frac34 10^{-2k}.
}
\tag{13}
\]

---

## 5. 第一分母位数锥 `m_1\ge2k`

写

\[
x=\frac{b_2}{10^{m_2}}\ge\frac1{10}.
\]

由

\[
\lambda=\frac{x}{b_1+x},
\]

有

\[
b_1=x\frac{1-\lambda}{\lambda}.
\]

而 (8) 给出 `1-\lambda>9/10`，故

\[
b_1>\frac9{100\lambda}.
\]

再由 (13)：

\[
\boxed{
 b_1>\frac3{25}10^{2k}.
}
\tag{14}
\]

另一方面 `b_1` 是 `m_1` 位正整数，所以

\[
b_1<10^{m_1}.
\]

因此

\[
10^{m_1}>\frac3{25}10^{2k}.
\]

因为

\[
\frac3{25}>10^{-1},
\]

而 `m_1` 为整数，立即得到

\[
\boxed{m_1\ge2k.}
\tag{15}
\]

所以：

\[
\boxed{
s_1=g+2,\quad m_1<2k}
\]

在整个 A1 中为空，包括此前的两个低尺度 `(g,k)` 角落。

---

## 6. 当前最高层核心

结合全局四层带，A1 现为

\[
s_1-g\in\{-1,0,1,2\}.
\]

最高层 `s_1-g=2` 还额外满足

\[
\boxed{
\lambda
<
\frac{200}{567}10^{-2k}(1+10^{-4g})
}
\]

以及

\[
\boxed{m_1\ge2k.}
\]

因此最高层已经被压进一个非常薄的 moving-prefix cone：第二块在前两分母拼接中的权重随 `k` 至少按 `10^{-2k}` 衰减，而第一分母位数至少以斜率 `2` 跟随 `k` 增长。

该结果仍不等于最高层全空；剩余任务是利用 normalized square / integer gap / 十进制端点离散性继续攻击 `m_1\ge2k` 的极端边界锥。