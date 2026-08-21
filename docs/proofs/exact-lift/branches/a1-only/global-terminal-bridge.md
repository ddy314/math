# A1 global terminal bridge: full tail divisor, integer contact weight, and recovery modulus

> 日期：2026-08-21。本文只使用原 exact-lift 平方恒等式、A1 safe common-quotient normalization 与 primitive reducedness。目标是把此前主要服务于 minimal diagonal 的 deep 分析接回 **整个 A1 四层**
> \[
> d=s_1-g\in\{-1,0,1,2\}.
> \]
> 本文不使用早期预印本中未完成的 “far gap / second gap incompatibility” 论证。

状态：**本文各结论均已严格完成；A1 全局空性仍待最后 terminal incompatibility。**

---

## 1. 记号

A1 中写

\[
g=-s_3\ge0,
\qquad
k=s_2+s_3\ge1,
\qquad
n=m_3-g=n_3.
\]

前两分母对象为

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2.
\]

第三尾公共商正规化写成

\[
\omega=\gcd(b_3,10^n),
\qquad
L=\frac{10^n}{\omega},
\qquad
M=\frac{b_3}{\omega},
\]

于是

\[
\gcd(L,M)=1,
\qquad
10^n=\omega L,
\qquad
b_3=\omega M.
\]

沿用 safe integer-gap recovery：

\[
U=H-y_3=La,
\qquad
\mathcal T=Ma
\]

对唯一正整数 `a`，且

\[
10^{g-1}\le \frac ML<10^g.
\tag{1}
\]

---

## 2. 第三分母的全局尾模整除

### 定理 A1-T1

任意 A1 exact-lift candidate 都满足

\[
\boxed{b_3\mid 10^{m_3}QG.}
\tag{2}
\]

因此正规化后的整个第三分母余部满足

\[
\boxed{M\mid10^gQG.}
\tag{3}
\]

注意 (3) 控制的是完整 `M`，包括 `2,5` 部分；它强于只控制第三分母 non-decimal part 的旧 denominator funnel。

### 证明

令

\[
N=(a_1b_2)^2+(a_2b_1)^2.
\]

原 exact lift 平方并清去三个分母后有

\[
\alpha^2G^2b_3^2
=
\beta^2\bigl(Nb_3^2+G^2a_3^2\bigr).
\tag{4}
\]

模 `b_3^2` 得

\[
b_3^2\mid \beta^2G^2a_3^2.
\]

逐素数取赋值，推出

\[
b_3\mid \beta G a_3.
\]

由于原第三分数既约，

\[
\gcd(a_3,b_3)=1,
\]

故

\[
b_3\mid\beta G.
\]

又

\[
\beta=10^{m_3}Q+b_3,
\]

所以

\[
b_3\mid10^{m_3}QG,
\]

即 (2)。

A1 中

\[
10^{m_3}=10^g10^n=10^g\omega L,
\qquad
b_3=\omega M.
\]

代入 (2) 并约去 `omega`：

\[
M\mid10^gLQG.
\]

再由 `(L,M)=1` 欧几里得约去 `L`，得到 (3)。证毕。

---

## 3. contact 参数离散化为一个前缀整数

### 定理 A1-T2

定义

\[
\boxed{
\kappa:=\frac{10^gLQG}{M}.
}
\tag{5}
\]

则

\[
\boxed{\kappa\in\mathbf Z_{>0}}
\]

且精确落在一个十倍窗口

\[
\boxed{QG<\kappa\le10QG.}
\tag{6}
\]

更重要的是，rational-contact 权重

\[
\theta=\frac{b_3}{10^{m_3}Q}
\]

满足

\[
\boxed{\theta=\frac G\kappa.}
\tag{7}
\]

因此整个 A1 contact 可以写成离散形式

\[
\boxed{
R=\frac{\kappa P+Gr_3}{\kappa+G},
}
\tag{8}
\]

其中

\[
P=\frac{C}{10^gQ},
\qquad
C=a_1 10^{n_2}+a_2.
\]

等价地

\[
\boxed{
\frac{P-R}{R-r_3}=\frac G\kappa,
\qquad
QG<\kappa\le10QG.
}
\tag{9}
\]

### 证明

(3) 直接保证 (5) 为正整数。

由 safe tail slope (1)：

\[
10^{g-1}\le\frac ML<10^g.
\]

取倒数并乘 `10^gQG`：

\[
QG<\frac{10^gLQG}{M}\le10QG,
\]

得到 (6)。

另一方面

\[
\theta
=\frac{\omega M}{10^g\omega LQ}
=\frac{M}{10^gLQ}
=\frac G\kappa,
\]

即 (7)。把它代回原 rational contact

\[
R=\frac{P+\theta r_3}{1+\theta}
\]

即得 (8)-(9)。证毕。

---

## 4. 同一个 `kappa` 强制 recovery gap 整除

令

\[
A=10^{m_2}b_1,
\qquad
B=b_2,
\qquad
Q=A+B.
\]

A1 safe gap identity 可写成

\[
\mathcal T
=10^gQ\Delta-B(10^{g+k}y_1-y_2),
\tag{10}
\]

其中

\[
H=10^ky_1-\Delta,
\qquad \Delta\in\mathbf Z_{>0}.
\]

### 定理 A1-T3

任意 A1 candidate 满足

\[
\boxed{
Q\mid \kappa A(10^{g+k}y_1-y_2).
}
\tag{11}
\]

定义

\[
\boxed{
Q_0:=\frac{Q}{\gcd(Q,\kappa A)}.
}
\tag{12}
\]

则

\[
\boxed{
Q_0\mid10^{g+k}y_1-y_2.
}
\tag{13}
\]

因此旧 terminal picture 中的 recovery gap 不再携带一个独立、任意的 cyclotomic modulus；其强制模数由同一个 contact integer `kappa` 决定。

### 证明

由 `U=La, T=Ma` 与 (5)：

\[
\kappa\mathcal T
=\kappa Ma
=10^gQG\,La
=10^gQG(H-y_3).
\]

故

\[
Q\mid\kappa\mathcal T.
\tag{14}
\]

由 (10) 模 `Q`：

\[
\mathcal T
\equiv-B(10^{g+k}y_1-y_2)
\equiv A(10^{g+k}y_1-y_2)
\pmod Q,
\]

其中使用 `B=-A mod Q`。与 (14) 联立得到 (11)。按 (12) 约去 `gcd(Q,kappa A)` 即得 (13)。证毕。

---

## 5. 整个 decimal tail 的同时 `2/5` 整除证书

### 定理 A1-T4

任意 A1 candidate 满足

\[
\boxed{
L\mid N\omega^2,
}
\tag{15}
\]

以及

\[
\boxed{
\omega\mid
G^2 10^gLQ(10^gLQ+2M).
}
\tag{16}
\]

因此

\[
\boxed{
10^n
\mid
G^2 10^gL^2Q(10^gLQ+2M).
}
\tag{17}
\]

特别地 saturated `L=1` 时

\[
\boxed{
10^n\mid G^2 10^gQ(10^gQ+2M),
\qquad
M\mid10^gQG.
}
\tag{18}
\]

所以统一有精确尾长界

\[
\boxed{
n\le
\min_{p\in\{2,5\}}
v_p\!\left(G^2 10^gL^2Q(10^gLQ+2M)\right).
}
\tag{19}
\]

### 证明

A1 中

\[
\alpha=\omega L A_{12}+a_3,
\qquad
\beta=\omega(10^gLQ+M)
\]

对某个正整数 `A_12`。把 `b_3=omega M` 代入 (4) 并约去 `omega^2`：

\[
\alpha^2G^2M^2
=(10^gLQ+M)^2
\bigl(N\omega^2M^2+G^2a_3^2\bigr).
\tag{20}
\]

模 `L`：

\[
\alpha\equiv a_3,
\qquad
10^gLQ+M\equiv M,
\]

故两边的 `G^2 a_3^2 M^2` 消去，得到

\[
L\mid N\omega^2M^4.
\]

由 `(L,M)=1` 得 (15)。

模 `omega`：

\[
\alpha\equiv a_3,
\]

且含 `N omega^2` 的项消失，所以

\[
\omega\mid
G^2a_3^2\bigl((10^gLQ+M)^2-M^2\bigr).
\]

右侧差平方等于

\[
G^2a_3^2 10^gLQ(10^gLQ+2M).
\]

因为 `omega|b_3` 且 `(a_3,b_3)=1`，有 `(a_3,omega)=1`，从而可约去 `a_3^2`，得到 (16)。

再由 `10^n=omega L`，将 (16) 两边额外乘以 `L` 即得 (17)。`L=1` 给 (18)，而 (19) 是 (17) 分别取 `v_2,v_5` 的直接结果。证毕。

---

## 6. 对当前 A1 前沿的意义

本文把四个全局位数层共同置于以下 terminal bridge：

\[
\boxed{
\begin{gathered}
M\mid10^gQG,\\
QG<\kappa\le10QG,\\
\theta=G/\kappa,\\
Q_0\mid10^{g+k}y_1-y_2,\\
10^n\mid G^2 10^gL^2Q(10^gLQ+2M).
\end{gathered}}
\tag{20}
\]

这里 `kappa` 同时控制：

- rational contact 的实权；
- recovery gap 的有效模数 `Q0`；
- third-tail quotient `M/L`。

所以后续 terminal closure 不应再把 `U=H-y3` 与 recovery gap 当成两个独立自由 gap。真正需要证明的是：在四层 digit constraint 下，(20) 的同一个 `kappa` 无法同时满足 contact、recovery 和 decimal-tail valuation。

下一步优先分 `g=0` 与 `g>=1`：

- `g=0` 没有 saturated `L=1`，且 recovery gap 为 `10^k y1-y2`，与 carrier bottom gap 同尺度；
- `g>=1` 允许 saturated，但 (18) 把整个 `10^n` 同时压到显式的 `2/5` 前缀整式上，可与四层 digit bounds 联用。
