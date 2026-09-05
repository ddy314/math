# 十进制拼接平方和问题：严格层第一轮

## 0. 本轮范围与结论

本轮只研究

\[
\delta_2+\delta_3\ge 1.
\]

接受 `proved_results_report_v2.md` 中 T1–T18，不重新审计这些定理，不研究临界层，
也不使用 E1–E7 的有限计算支持任何全局结论。

上传区实际只提供了 `proved_results_report_v2.md`；本轮使用该报告中的 T1–T18、
依赖表及第 4.2、6、9.2 节的完整严格层分支。没有假称读取未出现在上传区的
`proved_results_index_v2.md`。

本轮得到三个结果。

1. 建立了统一覆盖唯一最大、两坐标共同最大和三坐标共同最大的主导坐标恒等式。
2. 把整个严格层双向等价地压入四个固定的十进制 \(S\)-整数超曲面
   \(\mathcal H_k\)，其中
   \[
   k=\Delta-m\in\{-1,0,1,2\}.
   \]
   这实现了“有限多个固定丢番图方程”意义下的全严格层压缩，但尚未求出这些
   超曲面的全部允许点。
3. 对类 D，即第二、第三坐标共同最大类，给出四个显式固定方程
   \(\mathcal D_k\)，并把无界参数 \(m\) 隔离成单个十进制 \(S\)-单位
   \(\tau=10^{-m}\)。每个 \(\mathcal D_k\) 都是关于 \(\tau\) 的固定六次
   提升方程。这完整覆盖 D 的四条无界射线，不是固定 \(m\) 的切片。

没有证明严格层无解，也没有找到严格层原题解。

---

## 1. 完整严格层分支树

沿用

\[
\Delta=\delta_1+\delta_2+\delta_3,\qquad
m=\max_i\delta_i.
\]

严格层的完整分支如下。

### A. 第一坐标达到最大值

当 \(m=1\) 时：

\[
(1,1,0),\qquad (1,0,1),\qquad (1,1,1).
\]

当 \(m\ge2\) 时，由 T17：

\[
(m,m,1-m),\qquad (m,1-m,m),
\]

\[
(m,m-1,2-m),\qquad (m,2-m,m-1),
\]

\[
(m,m,2-m),\qquad (m,2-m,m).
\]

### B. 第二坐标唯一最大

\[
(\delta_1,\delta_2,\delta_3)=(k-r,m,r),
\]

其中

\[
k\in\{-1,0,1,2\},\qquad
m>\max(r,k-r),\qquad
m+r\ge1.
\]

### C. 第三坐标唯一最大

\[
(\delta_1,\delta_2,\delta_3)=(k-r,r,m),
\]

其中限制同样为

\[
k\in\{-1,0,1,2\},\qquad
m>\max(r,k-r),\qquad
m+r\ge1.
\]

### D. 第二、第三坐标共同最大，第一坐标不是最大

\[
(k-m,m,m),\qquad k\in\{-1,0,1,2\},
\]

即

\[
(-m-1,m,m),\quad(-m,m,m),\quad(1-m,m,m),\quad(2-m,m,m).
\]

其中 \(k=2,m=1\) 给出 \((1,1,1)\)，应归入 A，故从 D 删除。

这四类互不遗漏。下文的统一坐标会把它们识别为同四个固定超曲面上的不同
“最大坐标面”。

---

## 2. 统一主导坐标框架

### 2.1 拼接加权平均与球面方向

记

\[
W_1=b_1\,10^{\beta_2+\beta_3},\qquad
W_2=b_2\,10^{\beta_3},\qquad
W_3=b_3,
\]

\[
\lambda_i=\frac{W_i}{B}.
\]

于是

\[
\lambda_i>0,\qquad \lambda_1+\lambda_2+\lambda_3=1,
\]

并且拼接比有精确表示

\[
R
=
\lambda_1\,10^{\delta_2+\delta_3}q_1
+\lambda_2\,10^{\delta_3}q_2
+\lambda_3q_3.
\tag{2.1}
\]

令

\[
u_i=\frac{q_i}{R},
\qquad
\mathbf u=(u_1,u_2,u_3).
\]

由球面方程，

\[
\|\mathbf u\|_2=1.
\]

再定义

\[
\mathbf v=
\left(
\lambda_1\,10^{\delta_2+\delta_3},
\lambda_2\,10^{\delta_3},
\lambda_3
\right).
\]

式 (2.1) 等价于

\[
\mathbf v\cdot\mathbf u=1.
\tag{2.2}
\]

### 定理 T19：统一主导坐标恒等式

对原题任意严格层解，

\[
\boxed{\|\mathbf v-\mathbf u\|_2^2=\|\mathbf v\|_2^2-1}.
\tag{2.3}
\]

特别地，

\[
\boxed{\|\mathbf v\|_2\ge1}.
\tag{2.4}
\]

若

\[
I=\{i:\delta_i=m\}
\]

是所有达到最大位数差的坐标集合，则对每个 \(i\in I\)，

\[
\boxed{u_i>\frac1{100\sqrt3}},
\tag{2.5}
\]

从而

\[
\boxed{v_i<100\sqrt3}.
\tag{2.6}
\]

该结论同时适用于：

- \(|I|=1\)：唯一最大坐标；
- \(|I|=2\)：两个坐标共同最大；
- \(|I|=3\)：三个坐标共同最大。

#### 证明

由 (2.2) 及 \(\|\mathbf u\|_2=1\)，

\[
\|\mathbf v-\mathbf u\|_2^2
=\|\mathbf v\|_2^2+\|\mathbf u\|_2^2
-2\mathbf v\cdot\mathbf u
=\|\mathbf v\|_2^2-1.
\]

这证明 (2.3)–(2.4)。

若 \(i\in I\)，则

\[
q_i>10^{m-1}.
\]

另一方面，每个 \(q_j<10^{m+1}\)，所以

\[
R<\sqrt3\,10^{m+1}.
\]

故

\[
u_i=\frac{q_i}{R}>\frac1{100\sqrt3}.
\]

又因 (2.2) 的三个加项严格为正，每个 \(v_i u_i<1\)，结合 (2.5) 即得
(2.6)。证毕。

#### 与 T16–T17 的关系

若第一坐标达到最大值，则

\[
v_1=\lambda_1\,10^{\delta_2+\delta_3}.
\]

而

\[
\lambda_1>\frac{b_1}{b_1+1}\ge\frac12.
\]

由 (2.6)，

\[
10^{\delta_2+\delta_3}<200\sqrt3,
\]

所以整数 \(\delta_2+\delta_3\le2\)。这与 T17 中第一最大分支只出现
后两块总差 \(1,2\) 相容。

T19 的作用不是替代 T16，而是给出一个不预设最大坐标位置的统一球面—加权平均
恒等式。

---

## 3. 四个固定十进制 \(S\)-整数超曲面

本节把全部无界位数差统一改写为十进制 \(S\)-单位变量。

### 3.1 归一化变量

定义数字块的十进制尾尺度

\[
P_i=10^{-\alpha_i},\qquad Q_i=10^{-\beta_i},
\]

以及块首尾归一化量

\[
\widehat a_i=a_iP_i,\qquad
\widehat b_i=b_iQ_i.
\]

于是

\[
\frac1{10}\le\widehat a_i<1,\qquad
\frac1{10}\le\widehat b_i<1,
\tag{3.1}
\]

\[
a_i=\frac{\widehat a_i}{P_i}\in\mathbb Z_{>0},\qquad
b_i=\frac{\widehat b_i}{Q_i}\in\mathbb Z_{>0}.
\tag{3.2}

\]

再令

\[
z_i=\frac{\widehat a_i}{\widehat b_i}
=\frac{q_i}{10^{\delta_i}}.
\tag{3.3}
\]

严格层必有 \(m\ge1\)。定义

\[
\tau=10^{-m},
\qquad
\varepsilon_i=10^{\delta_i-m}.
\tag{3.4}
\]

于是

\[
\tau\in\{10^{-n}:n\ge1\},
\qquad
\varepsilon_i\in\{10^{-g}:g\ge0\}.
\tag{3.5}
\]

\[
0<\varepsilon_i\le1,\qquad
\max_i\varepsilon_i=1.
\tag{3.6}
\]

由定义直接得到三个尺度兼容式

\[
\boxed{\varepsilon_iP_i=\tau Q_i\qquad(i=1,2,3)}.
\tag{3.7}
\]

记

\[
k=\Delta-m.
\]

由 T5，

\[
k\in\{-1,0,1,2\}.
\tag{3.8}
\]

把 (3.7) 相乘，并使用 \(\Delta=m+k\)，得到

\[
\boxed{\varepsilon_1\varepsilon_2\varepsilon_3
=10^k\tau^2}.
\tag{3.9}
\]

严格层条件等价于

\[
\boxed{\varepsilon_2\varepsilon_3\ge10\tau^2}.
\tag{3.10}
\]

最后定义两个完整拼接数的归一化首数：

\[
\mathcal A
=\widehat a_1+P_1\widehat a_2+P_1P_2\widehat a_3,
\tag{3.11}
\]

\[
\mathcal B
=\widehat b_1+Q_1\widehat b_2+Q_1Q_2\widehat b_3.
\tag{3.12}
\]

它们满足

\[
A=10^{\alpha_1+\alpha_2+\alpha_3}\mathcal A,
\qquad
B=10^{\beta_1+\beta_2+\beta_3}\mathcal B.
\tag{3.13}
\]

### 定理 T20：严格层的四超曲面双向等价

原题的严格层解与下列允许数据双向等价。

1. 选择
   \[
   k\in\{-1,0,1,2\}.
   \]
2. 选择
   \[
   P_i,Q_i,\tau\in\{10^{-n}:n\ge1\},
   \qquad
   \varepsilon_i\in\{10^{-g}:g\ge0\}.
   \]
3. 满足 (3.1)–(3.2)、逐项既约条件
   \[
   \gcd\!\left(\frac{\widehat a_i}{P_i},
               \frac{\widehat b_i}{Q_i}\right)=1,
   \tag{3.14}
   \]
   以及 (3.6)–(3.10)。
4. 满足固定方程
   \[
   \boxed{
   \mathcal B^2
   \left(
   \varepsilon_1^2z_1^2+
   \varepsilon_2^2z_2^2+
   \varepsilon_3^2z_3^2
   \right)
   =
   10^{2k}\mathcal A^2
   }.
   \tag{\(\mathcal H_k\)}
   \]

由于所有量均为正，\((\mathcal H_k)\) 等价于未平方式

\[
\boxed{
\mathcal B
\sqrt{\varepsilon_1^2z_1^2+
      \varepsilon_2^2z_2^2+
      \varepsilon_3^2z_3^2}
=10^k\mathcal A
}.
\tag{3.15}
\]

清去 \(z_i\) 的分母后，\((\mathcal H_k)\) 是固定的
\(\mathbb Z[1/10]\)-多项式方程：

\[
\boxed{
\begin{aligned}
\mathcal B^2\bigl[
&\varepsilon_1^2
 (\widehat a_1\widehat b_2\widehat b_3)^2\\
&+\varepsilon_2^2
 (\widehat a_2\widehat b_1\widehat b_3)^2\\
&+\varepsilon_3^2
 (\widehat a_3\widehat b_1\widehat b_2)^2
\bigr]
=
10^{2k}\mathcal A^2
(\widehat b_1\widehat b_2\widehat b_3)^2.
\end{aligned}
}
\tag{3.16}
\]

当 \(k=-1\) 时，把 (3.16) 乘以 \(100\) 即可清去固定系数 \(10^{-2}\)。
因此整个严格层确实落在四个固定的十进制 \(S\)-整数超曲面

\[
\mathcal H_{-1},\quad
\mathcal H_0,\quad
\mathcal H_1,\quad
\mathcal H_2
\]

上，而不是落在随 \(m,r\) 改变的无限个不同方程上。

#### 正向证明

由 (3.7)，

\[
\frac{Q_i}{P_i}=\frac{\varepsilon_i}{\tau}.
\]

所以

\[
q_i
=\frac{\widehat a_i/P_i}{\widehat b_i/Q_i}
=\frac{\varepsilon_i}{\tau}z_i.
\]

从而

\[
R
=\frac1{\tau}
\sqrt{\varepsilon_1^2z_1^2+
      \varepsilon_2^2z_2^2+
      \varepsilon_3^2z_3^2}.
\tag{3.17}
\]

另一方面，由 (3.13) 及 \(\Delta=m+k\)，

\[
\frac AB
=10^{m+k}\frac{\mathcal A}{\mathcal B}
=\frac{10^k}{\tau}\frac{\mathcal A}{\mathcal B}.
\tag{3.18}
\]

令 (3.17) 与 (3.18) 相等，即得 (3.15)，平方后为
\((\mathcal H_k)\)。

#### 反向证明

由 \(P_i,Q_i,\tau,\varepsilon_i\) 的取值集合，可唯一写成

\[
P_i=10^{-\alpha_i},\quad
Q_i=10^{-\beta_i},\quad
\tau=10^{-m},\quad
\varepsilon_i=10^{-g_i},
\]

其中

\[
\alpha_i,\beta_i,m\ge1,\qquad g_i\ge0.
\]

由 (3.7)，

\[
g_i+\alpha_i=m+\beta_i,
\]

故

\[
\delta_i=\alpha_i-\beta_i=m-g_i.
\tag{3.19}
\]

由 \(\max_i\varepsilon_i=1\)，至少一个 \(g_i=0\)，所以

\[
\max_i\delta_i=m.
\]

由 (3.9)，

\[
g_1+g_2+g_3=2m-k.
\]

结合 (3.19)，

\[
\Delta=3m-(g_1+g_2+g_3)=m+k.
\]

而 (3.10) 正好给出

\[
\delta_2+\delta_3\ge1.
\]

式 (3.1)–(3.2) 保证 \(\alpha_i,\beta_i\) 是重构整数块的实际位数，
(3.14) 保证逐项既约。最后，\((\mathcal H_k)\) 因两边为正可开正平方根，
再逆用 (3.17)–(3.18)，得到

\[
\frac AB=\sqrt{q_1^2+q_2^2+q_3^2}.
\]

故重构数据是原题严格层解。证毕。

---

## 4. 四大类在统一超曲面中的位置

令

\[
I=\{i:\varepsilon_i=1\}.
\]

由 (3.19)，这恰好是达到最大位数差 \(m\) 的坐标集合。

| 原分支 | 在 \(\mathcal H_k\) 中的最大坐标面 |
|---|---|
| A：第一坐标达到最大 | \(\varepsilon_1=1\) |
| B：第二坐标唯一最大 | \(\varepsilon_2=1,\ \varepsilon_1,\varepsilon_3\le10^{-1}\) |
| C：第三坐标唯一最大 | \(\varepsilon_3=1,\ \varepsilon_1,\varepsilon_2\le10^{-1}\) |
| D：第二、第三共同最大 | \(\varepsilon_2=\varepsilon_3=1,\ \varepsilon_1\le10^{-1}\) |

三坐标共同最大对应

\[
\varepsilon_1=\varepsilon_2=\varepsilon_3=1.
\]

此时 (3.9) 给出

\[
1=10^k\tau^2.
\]

结合 \(k\le2\) 和 \(m\ge1\)，只能有

\[
k=2,\qquad \tau=10^{-1},
\]

即

\[
(\delta_1,\delta_2,\delta_3)=(1,1,1).
\]

因此唯一最大、两坐标共同最大和三坐标共同最大不再需要三套互不关联的
归一化估计；它们只是同四个 \(\mathcal H_k\) 上不同的坐标面。

在这个意义下，B、C、D 原有的十二个无界位数族已经被合并为四个固定方程上的
三个面型，而不是十二组随参数变化的代数方程。

---

## 5. 类 D 的完整固定方程压缩

本节完整处理

\[
D:\qquad
(\delta_1,\delta_2,\delta_3)=(k-m,m,m),
\qquad
k\in\{-1,0,1,2\}.
\]

不固定 \(m\)。

### 定理 T21：类 D 的四个固定六次 \(S\)-单位提升方程

类 D 原题解与四个系统 \(\mathcal D_k\) 的允许点双向等价，其中

\[
k\in\{-1,0,1,2\}.
\]

在 D 面上，

\[
\varepsilon_2=\varepsilon_3=1.
\]

由 (3.9)，

\[
\boxed{\varepsilon_1=10^k\tau^2}.
\tag{5.1}
\]

尺度兼容式 (3.7) 化为

\[
\boxed{
Q_1=10^k\tau P_1,\qquad
P_2=\tau Q_2,\qquad
P_3=\tau Q_3
}.
\tag{5.2}
\]

D 中第一坐标不是最大，等价于

\[
\boxed{10^k\tau^2\le10^{-1}}.
\tag{5.3}
\]

特别地，\(k=2,m=1\) 时左边等于 \(1\)，自动不满足 (5.3)，所以
\((1,1,1)\) 的重复边界已经被删除。

将 (5.1)–(5.2) 代入 (3.15)，得到固定方程

\[
\boxed{
\begin{aligned}
&\left[
\widehat b_1+
10^k\tau P_1
(\widehat b_2+Q_2\widehat b_3)
\right]\\
&\quad\cdot
\sqrt{
z_2^2+z_3^2+
10^{2k}\tau^4z_1^2
}\\
&=
10^k
\left[
\widehat a_1+
P_1\widehat a_2+
\tau P_1Q_2\widehat a_3
\right].
\end{aligned}
}
\tag{\(\mathcal D_k\)}
\]

这里仍须满足 T20 的数字格点、实际位数及逐项既约条件，以及 (5.2)。

令

\[
D_0=\widehat b_1,
\qquad
D_1=10^kP_1(\widehat b_2+Q_2\widehat b_3),
\]

\[
S_0=z_2^2+z_3^2,
\qquad
S_4=10^{2k}z_1^2,
\]

\[
A_0=\widehat a_1+P_1\widehat a_2,
\qquad
A_1=P_1Q_2\widehat a_3.
\]

则 \(\mathcal D_k\) 平方后为

\[
\boxed{
(D_0+\tau D_1)^2(S_0+\tau^4S_4)
=10^{2k}(A_0+\tau A_1)^2
}.
\tag{5.4}
\]

展开为关于单个十进制 \(S\)-单位 \(\tau=10^{-m}\) 的六次方程：

\[
\boxed{
\begin{aligned}
0={}&
\bigl(D_0^2S_0-10^{2k}A_0^2\bigr)\\
&+2\tau
\bigl(D_0D_1S_0-10^{2k}A_0A_1\bigr)\\
&+\tau^2
\bigl(D_1^2S_0-10^{2k}A_1^2\bigr)\\
&+\tau^4D_0^2S_4
+2\tau^5D_0D_1S_4
+\tau^6D_1^2S_4.
\end{aligned}
}
\tag{5.5}
\]

清去 \(\widehat b_i\) 和全部十进制 \(S\)-整数的分母后，(5.5) 是固定整数
多项式—\(S\)-单位方程。它没有随 \(m\) 增长的次数或项数。

#### 覆盖性证明

若原位数模式属于 D，则

\[
\delta_2=\delta_3=m,\qquad \delta_1=k-m.
\]

因此

\[
\varepsilon_2=\varepsilon_3=1,\qquad
\varepsilon_1=10^{\delta_1-m}=10^{k-2m}=10^k\tau^2,
\]

从而 (5.1)–(5.2) 成立。把这些等式代入 T20 即得到
\(\mathcal D_k\)。

反向地，给定 \(\mathcal D_k\) 的允许点，T20 已重构

\[
\delta_i=m-g_i.
\]

由 \(\varepsilon_2=\varepsilon_3=1\) 得

\[
\delta_2=\delta_3=m.
\]

由 \(\varepsilon_1=10^k\tau^2\) 得

\[
\delta_1-m=k-2m,
\]

即

\[
\delta_1=k-m.
\]

(5.3) 保证 \(\delta_1<m\)。故重构解恰落在 D，而不是 A、B 或 C。
证毕。

### 本节完成了什么

本节没有排除 D，但完成了用户要求的第三种“完整处理”：

- D 的四条无界射线全部被覆盖；
- 没有固定 \(m\)；
- 四条射线被压成四个固定方程 \(\mathcal D_k\)；
- 无界层参数只以纯 \(10\) 次幂根 \(\tau=10^{-m}\) 出现；
- 每个方程关于 \(\tau\) 的次数统一不超过 \(6\)。

---

## 6. 全局不变量路线的检验

### 6.1 纯实球面间隙不能统一排除严格层

考虑 \(\mathcal D_0\) 的实数松弛闭包：允许

\[
\tau,P_i,Q_i\to0
\]

并暂时只保留归一化方程与实数块区间。

取

\[
\tau=0,\qquad
(\varepsilon_1,\varepsilon_2,\varepsilon_3)=(0,1,1),
\]

\[
P_i=Q_i=0,
\]

\[
(\widehat a_1,\widehat a_2,\widehat a_3)
=
\left(\frac12,\frac3{10},\frac25\right),
\]

\[
(\widehat b_1,\widehat b_2,\widehat b_3)
=
\left(\frac12,\frac12,\frac12\right).
\]

此时

\[
(z_1,z_2,z_3)=\left(1,\frac35,\frac45\right),
\]

\[
\sqrt{\varepsilon_1^2z_1^2+
      \varepsilon_2^2z_2^2+
      \varepsilon_3^2z_3^2}
=1,
\]

\[
\mathcal A=\mathcal B=\frac12.
\]

故 \(\mathcal H_0\) 精确成立。

若把未平方式左减右记为 \(F\)，则在该点

\[
\frac{\partial F}{\partial\widehat a_1}=-1.
\]

因此这个交点不是高阶偶然接触；在实数松弛问题中，它是横截交点。

结论是：

> “最大坐标的球面方向与拼接加权平均之间存在统一正间隙”这一机制对整个严格层
> 不成立。

这不产生原题解，因为该闭包点没有保留离散十进制格点和逐项既约条件；它证明的是，
纯阿基米德紧致性不能单独关闭无界参数。若要排除严格层，必须使用离散的
\(2,5\)-进信息、逐项既约性或 T9 分母核。

### 6.2 T9 与最大位数差位置尚无直接冲突

在 T20 的坐标中，

\[
a_i=\frac{\widehat a_i}{P_i},\qquad
b_i=\frac{\widehat b_i}{Q_i}.
\]

最大位数差位置由 \(\varepsilon_i\) 是否等于 \(1\) 决定，而 T9 中
\(v_p(b_i)\) 的最大位置由整数

\[
\frac{\widehat b_i}{Q_i}
\]

的素因子结构决定。

尺度关系

\[
\varepsilon_iP_i=\tau Q_i
\]

只约束十进制位数，不决定 \(p\ne2,5\) 的赋值。因此目前不能从
“\(\delta_i\) 最大”推出“\(v_p(b_i)\) 最大”，也不能反推。

所以 T9 仍是可能的下一步算术输入，但需要一条新的耦合引理；不能直接把 T9 的
最大赋值位置结论外推为严格层矛盾。

### 6.3 二进赋值同样没有由位数面自动决定

T8 限制最大 \(v_2(b_i)\) 恰在一个分母取得，但 A、B、C、D 的面型只记录
\(\alpha_i-\beta_i\)。同一面型内可以改变块的末位而不改变任何
\(\delta_i\)。

故 T8 不能仅凭最大坐标面关闭 B、C 或 D；必须把 \(\mathcal H_k\) 清分母后
的最低 \(2\)-进项与 T8 同时分析。

---

## 7. 对第一坐标最大六射线与 T18 的重新评估

### 7.1 两个精确的实闭包交点

T18 的四条非双最大射线分别对应后两块总差 \(k=1\) 和 \(k=2\)。

对

\[
(m,m-1,2-m),
\]

有

\[
(\varepsilon_1,\varepsilon_2,\varepsilon_3)
\longrightarrow
\left(1,\frac1{10},0\right).
\]

在 \(\mathcal H_1\) 的实闭包中取

\[
\widehat a_1=\frac1{10},\qquad
\widehat b_1=1,
\]

\[
\widehat a_2=1,\qquad
\widehat b_2=\frac1{\sqrt{99}},
\]

并令其他归一化尾项消失。此时

\[
z_1=\frac1{10},\qquad z_2=\sqrt{99},
\]

所以

\[
\sqrt{z_1^2+\frac1{100}z_2^2}=1
=10\widehat a_1.
\]

故 \(\mathcal H_1\) 在

\[
\widehat b_1=1
\]

的边界精确相交。

对

\[
(m,m,2-m),
\]

有

\[
(\varepsilon_1,\varepsilon_2,\varepsilon_3)
\longrightarrow(1,1,0).
\]

在 \(\mathcal H_2\) 的实闭包中取

\[
\widehat a_1=\frac1{10},\qquad
\widehat b_1=1,
\]

\[
\widehat a_2=1,\qquad
\widehat b_2=\frac1{\sqrt{99.99}}.
\]

则

\[
\sqrt{z_1^2+z_2^2}=10
=100\widehat a_1.
\]

交换第二、第三坐标给出另外两条 T18 射线的同类闭包交点。

这些点使用了归一化区间的闭端点，不是原题解；它们说明 T18 中的边缘现象是
真实的极限几何，而不是粗估计偶然造成的假象。

### 7.2 为什么停止继续优化 \(49/50\)、\(99/100\)

T18 当前给出的信息本质上是

\[
\frac{b_1}{10^{\beta_1}}>c
\]

一类归一化边缘约束。即便把固定常数 \(c<1\) 任意提高，仍有无限多整数

\[
b_1=10^{\beta_1}-1
\]

满足该形状。

要从整数性得到终止，至少需要把绝对数字亏损

\[
d_1=10^{\beta_1}-b_1\in\mathbb Z_{>0}
\]

压到

\[
d_1<1,
\]

或得到与逐项既约、T7–T9、某个固定素数赋值相冲突的条件。T18 的证明链只控制
\(d_1/10^{\beta_1}\)，没有产生这种绝对亏损界。

上节两个实闭包交点进一步表明：只用同一组欧氏范数与加权平均不等式，
其最优常数会把变量推向

\[
\widehat b_1=1,\qquad
\widehat a_1=\frac1{10}
\]

等边界，而不会形成统一正间隙。

因此本轮明确停止沿 T18 的同类不等式链继续优化常数。尚未发现：

- \(\beta_1\) 的统一有限上界；
- 与逐项既约性的直接矛盾；
- 与 T7–T9 的直接矛盾；
- 可执行的无限下降。

---

## 8. 未解决分支是否真正减少

### 8.1 已经发生的减少

在“固定代数对象”的意义下，未解决结构已经减少：

1. 全部 A、B、C、D 不再需要随 \(m,r\) 改变的无限组方程；
2. 整个严格层只需研究
   \[
   \mathcal H_{-1},\mathcal H_0,\mathcal H_1,\mathcal H_2
   \]
   四个固定超曲面的允许十进制 \(S\)-整数点；
3. B、C、D 原有十二个外部参数族成为这四个超曲面上的三个最大坐标面；
4. D 更进一步成为四个固定六次提升方程 \(\mathcal D_k\)。

所以本轮达到“把整个严格层压成有限多个固定丢番图方程”的目标。

### 8.2 尚未发生的减少

没有任何 A、B、C、D 分支被证明为空。四个 \(\mathcal H_k\) 仍是高维
\(S\)-整数问题，不是已经求解的有限曲线清单。

因此不能把本轮结果表述为：

- 严格层无解；
- D 无解；
- 未解决位数模式已经被删除；
- 已经有可终止的枚举算法。

本轮的推进是“无限参数方程族 \(\to\) 四个固定 \(S\)-整数超曲面”，不是
“无限解候选 \(\to\) 有限候选点”。

---

## 9. 下一轮唯一推荐主线

下一轮应只研究 D 的四个固定方程 (5.5)，不再优化 T18 的阿基米德常数。

具体目标是建立下面的“十进制提升障碍”：

> 清去 (5.5) 的全部十进制分母后，比较
> \(\tau^0,\tau^1,\tau^2,\tau^4,\tau^5,\tau^6\)
> 六组项的最低 \(2\)-进与 \(5\)-进赋值，结合
> \(\gcd(a_i,b_i)=1\)、T8 和 T9，证明某一最低赋值只能唯一取得，
> 或把它强制降为一个固定的本原二平方方程。

其首要对象是 \(\tau=0\) 的主面方程

\[
\boxed{
D_0^2S_0=10^{2k}A_0^2
},
\tag{9.1}
\]

即

\[
\boxed{
\widehat b_1^2
\left[
\left(\frac{\widehat a_2}{\widehat b_2}\right)^2+
\left(\frac{\widehat a_3}{\widehat b_3}\right)^2
\right]
=
10^{2k}
(\widehat a_1+P_1\widehat a_2)^2
}.
\tag{9.2}
\]

实数上 (9.2) 有交点，所以必须研究“哪些主面有理点能够提升为
\(\tau=10^{-m}\) 的逐项既约十进制格点”。这正是 (5.5) 隔离出的离散问题。

如果能够证明所有四个 \(k\) 均无提升，则整个 D 被排除；如果只能证明主面数据
落在有限多个本原二平方参数族，也会把 D 从四个高维超曲面继续压成有限曲线族。

这是一条单一、可检验、直接承接本轮新方程的主线。

---

## 10. 本轮最终状态

- 完整严格层分支树：已列出。
- 统一主导坐标框架：T19。
- 覆盖整个严格层的新双向定理：T20。
- 完整覆盖一个无限大类的新定理：T21 覆盖 D。
- 整个严格层固定方程压缩：四个 \(\mathcal H_k\)。
- D 的进一步压缩：四个固定六次 \(\mathcal D_k\)。
- 合法严格层解：未找到。
- 严格层无解证明：未完成。
- 下一轮唯一主线：D 类六次提升方程的同步 \(2,5\)-进分析。
