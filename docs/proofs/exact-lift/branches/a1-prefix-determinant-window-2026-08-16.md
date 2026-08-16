# A1 cross-layer prefix determinant window — 2026-08-16

本文开始统一处理最高层以外的三个 `s_1-g` 层。

定义 carrier determinant

\[
\boxed{J:=10^k a_1b_2-a_2b_1.}
\]

由第一坐标严格承担 carrier：

\[
10^k r_1>r_2,
\]

所以

\[
\boxed{J\in\mathbf Z_{>0}.}
\]

本文证明：在除少数低 `g` chamber 外、且 `m_1` 足够长时，前两分数的相对 gap 被压到 `10^{-2k}` 尺度；等价地，`J` 落入一个常数宽度的高精度 determinant 窗。

> 审计修正：旧版末尾曾把形式条件 `n_1+m_2=k` 产生的 `J\in\{1,2\}` 描述成后续实际边界核。但本文 determinant 窗同时假设 `m_1\ge2k+2`，在三个 generic 低层中该取等条件根本不可达。相关形式推论已删除；后续只把 `J` 窗作为高精度有理逼近与局部赋值接口使用。

本文其余结论均为 **已严格完成**。

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
\boxed{1-t=\frac{J}{10^ka_1b_2}.}
\tag{1}
\]

---

## 2. 无条件 lower gap

rational contact 给出 `P>R`，所以

\[
u^2>\frac{R^2}{A_0^2}=a+t^2+z^2.
\]

又 `u<1`，故

\[
t^2<1-a.
\]

于是

\[
1-t>1-\sqrt{1-a}
=\frac{a}{1+\sqrt{1-a}}
>\frac a2.
\]

因此整个 A1 无条件满足

\[
\boxed{1-t>\frac12\,10^{-2k}.}
\tag{2}
\]

---

## 3. Generic chamber 中第三坐标不超过 `a`

A1 有

\[
r_3<10^{1-g},
\qquad
r_1>10^{g+d-1}.
\]

所以

\[
z<10^{2-k-2g-d},
\]

即

\[
z^2<10^{4-4g-2d}a.
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
\]

对四个位数层，(4) 只排除低尺度 chamber

\[
(d,g)=(1,0),(0,0),(-1,0),(-1,1).
\]

---

## 4. 长第一分母使 prefix weight 进入 `a` 级

因为

\[
\lambda=\frac{b_2}{Q}<10^{1-m_1},
\]

若

\[
\boxed{m_1\ge2k+2,}
\tag{6}
\]

则

\[
\boxed{\lambda<\frac a{10}.}
\tag{7}
\]

---

## 5. Contact 给出 upper gap

定义

\[
\Delta:=u^2-t^2-a-z^2>0.
\]

rational contact 给出

\[
\Delta<c_Q(a+t^2+z^2),
\qquad
c_Q=\frac{2+1/Q}{Q}.
\]

由于 `1/Q\le\lambda`：

\[
\boxed{c_Q<3\lambda.}
\tag{8}
\]

又

\[
1-u=\lambda(1-10^{-g}t)<\lambda,
\]

故

\[
\boxed{1-u^2<2\lambda.}
\tag{9}
\]

由

\[
1-t^2=a+z^2+(1-u^2)+\Delta
\]

和 `a+t^2+z^2<u^2<1`，在 (4)、(6) 下得到

\[
1-t^2<a+a+2\lambda+3\lambda
<\frac52a.
\]

因此

\[
\boxed{1-t<\frac52\,10^{-2k}.}
\tag{10}
\]

结合 (2)：

\[
\boxed{
\frac12\,10^{-2k}
<1-t<
\frac52\,10^{-2k}.}
\tag{11}
\]

---

## 6. Carrier determinant 窗

由 (1)、(11)：

\[
\boxed{
\frac{a_1b_2}{2\,10^k}
<J<
\frac{5a_1b_2}{2\,10^k}.}
\tag{12}
\]

这是一条跨四个位数层的高精度整数窗口。

等价地，正整数

\[
J=10^ka_1b_2-a_2b_1
\]

必须与尺度 `a_1b_2/10^k` 同阶；因此前两既约分数满足

\[
\frac{r_2}{10^kr_1}=1+O(10^{-2k})
\]

且误差常数已经由 (11) 显式固定。

---

## 7. 对旧 `J\in\{1,2\}` 边界的修正

从 (12) 单独看，如果形式上再假设

\[
n_1+m_2=k,
\]

确实会推出 `J\in\{1,2\}`。

但本文同时使用

\[
m_1\ge2k+2.
\]

在三个 generic 低层 `d\in\{-1,0,1\}` 中，

\[
n_1=m_1+g+d.
\]

结合 `2g+d\ge2` 可知：

- `d=1` 时 `g\ge1`，故 `n_1\ge2k+4`；
- `d=0` 时 `g\ge1`，故 `n_1\ge2k+3`；
- `d=-1` 时 `g\ge2`，故 `n_1\ge2k+3`。

所以一律有

\[
\boxed{n_1>k,}
\]

从而

\[
\boxed{n_1+m_2=k}
\]

在当前 generic determinant cone 中不可发生。

因此 `J=1,2` 不应列为实际开放边界。

---

## 8. 当前正确用途

对三个较低位数层

\[
d\in\{-1,0,1\}
\]

后续分工应为：

1. 单独处理四个低 `g` chamber
   \[
   (1,0),(0,0),(-1,0),(-1,1);
   \]
2. 处理短第一分母区域 `m_1\le2k+1`；
3. 在 `m_1\ge2k+2` 的 generic 区域使用 (11)–(12) 作为高精度 determinant / p-adic 输入，研究
   \[
   J=10^ka_1b_2-a_2b_1
   \]
   的素因子、赋值与十进制末端结构。

当前不再把任何不可达的形式取等条件当作实际 frontier。