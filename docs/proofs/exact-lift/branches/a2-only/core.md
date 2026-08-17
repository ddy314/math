# `A_2`-only 分支

本文件对应原总稿 §§12–16。它包含相邻边界、第一块 core、deep-even 终端通道、二进 Hensel 锁、source split、五进参数、Gaussian rectangle、prefix defect、odd inert excess、双 Hensel 系统、有限证书和当前开放核。

> 迁移说明：以下正文由原始总稿机械拆分，公式和证明状态不作数学改写。
# 12. \(A_2\)-only 分支

## 12.1 相邻边界区已经严格固定

\(A_2\)-only 满足

\[
s_3>0,
\qquad
s_2+s_3\le0.
\]

令

\[
k=s_3\ge1.
\]

carrier 条件给出

\[
(10^{2k}-1)r_2^2
\ge
r_1^2+r_3^2.
\]

把三块十进制位数窗口逐项代入并处理端点，可以严格推出

\[
\boxed{
s_3=1,
\qquad
s_2=-1.
}
\]

这一步早期曾经只被口头称为“carrier cap + digit window”，后来已经补成可审计的端点证明。

因此 \(A_2\) 唯一可能的位数形态是：

- 第二分子比分母少一位；
- 第三分子比分母多一位。

---

## 12.2 第一块 core 的压缩

在相邻边界区中，实数几何和 ordered Cauchy 先给出第一分母的有限上界，后续继续结合十进制窗口、局部素数结构和 deep-even 分支，最终真正无界的危险通道只剩

\[
\boxed{
b_1=2.
}
\]

第一分子一度剩下

\[
a_1\in\{3,5,7,9,11,13\}.
\]

进一步定义

\[
x=\frac{b_2}{10^{m_2}},
\qquad
y=\frac{a_2}{10^{m_2-1}},
\]

并利用

\[
F_{a_1}(x,y)
=
\left(
\frac{a_1+y}{2+x}
\right)^2
-\frac{a_1^2}{4}
-\frac{y^2}{100x^2},
\]

exact lift 必须满足

\[
F_{a_1}(x,y)>1.
\]

对 \(a_1=3\) 可以在整个合法区域严格证明

\[
F_3(x,y)<1.
\]

因此

\[
\boxed{
a_1=3
\text{ 已全局排除}.
}
\]

最终 core 只剩

\[
\boxed{
a_1\in\{5,7,9,11,13\}.
}
\]

---

## 12.3 Deep-even 终端通道

从这里开始仍统一使用全局位数 \(m_2,m_3\)，避免旧稿中 \(M,m\) 的重复记号。

最后危险通道具有

\[
\boxed{
b_2
=
2^{m_2+m_3+t}u,
}
\]

\[
\boxed{
b_3
=
2^{m_2+m_3+1}b_{3,0},
}
\]

其中

\[
u,\ b_{3,0}
\]

均为奇数，且

\[
\boxed{
t\ge3.
}
\]

前两分母拼接满足

\[
Q
=
2\cdot10^{m_2}+b_2
=
2^{m_2+1}Q_0,
\]

其中

\[
\boxed{
Q_0
=
5^{m_2}
+
2^{m_3+t-1}u.
}
\]

第三块正规化尾商被强迫为纯五次幂

\[
\boxed{
L=5^\lambda,
}
\]

并且

\[
\boxed{
5^\lambda>2^{m_2+1}.
}
\]

将

\[
b_3=\delta_3 b'
\]

进一步去二后写成

\[
\boxed{
b'=2^{m_2+1}c.
}
\]

于是 \(c\) 为奇数，并处在十倍窗口

\[
\boxed{
\frac{5^\lambda}{10\cdot2^{m_2+1}}
\le c
<
\frac{5^\lambda}{2^{m_2+1}}.
}
\]

---

## 12.4 二进 Hensel 锁

deep-even 通道中的二进抵消深度没有独立自由度，其值由

\[
5^{m_2+\lambda}+c
\]

唯一决定：

\[
\boxed{
t
=
1+
v_2(5^{m_2+\lambda}+c).
}
\]

因为 \(t\ge3\)，得到

\[
5^{m_2+\lambda}+c
\equiv0\pmod4.
\]

而

\[
5^k\equiv1\pmod4,
\]

所以

\[
\boxed{
c\equiv3\pmod4.
}
\]

于是 \(c\ge3\)，并可把尾商下界加强为

\[
\boxed{
5^\lambda>3\cdot2^{m_2+1}.
}
\]

这一结果把二进深度与五进尾商精确耦合起来。

---

## 12.5 \(c=c_Qc_u\) 的来源分解

统一记

\[
\sigma_5=v_5(u).
\]

按 \(c\) 的素因子究竟来自前缀 \(Q_0\) 还是来自 \(u\)，存在唯一互素分解

\[
\boxed{
c=c_Qc_u,
}
\]

并进一步写成

\[
\boxed{
Q_0
=
5^{\sigma_5}c_Qq_Q,
}
\]

\[
\boxed{
u
=
5^{\sigma_5}c_u\rho.
}
\]

满足

\[
\gcd(c_Qq_Q,c_u\rho)=1,
\]

\[
\gcd(c_Q,c_u)=1,
\]

\[
\gcd(c_u,\rho)=1.
\]

由二平方局部条件，

\[
p\mid c_u
\Longrightarrow
p\equiv1\pmod4.
\]

因此

\[
c_u\equiv1\pmod4.
\]

结合

\[
c\equiv3\pmod4
\]

得到

\[
\boxed{
c_Q\equiv3\pmod4.
}
\]

这一步把原先混杂的“尾分母素数”分成两个来源完全不同的算术库：

- \(c_Q\)：来自 denominator-prefix；
- \(c_u\)：来自 source \(u\)，且只含 \(1\bmod4\) 奇素数。

---

## 12.6 五进统一参数与三条通道

定义

\[
\boxed{
E_5=\lambda+\sigma_5.
}
\]

为了描述 \(5\)-进同步，统一使用

\[
d_5=m_3-E_5,
\]

\[
r_5=2E_5-m_3,
\]

\[
\nu_5=3E_5-2m_3.
\]

满足

\[
2d_5+\nu_5=E_5,
\]

\[
r_5+d_5=E_5,
\]

\[
E_5+\nu_5=2r_5.
\]

合法候选只能处于三条五进通道：

### 通道 I：\(\sigma_5>0\)

\[
\boxed{
m_3=\frac32E_5,
}
\]

并且 \(E_5\) 必须为偶数。

### 通道 II：reflection

\[
\sigma_5=0,
\qquad
\lambda<m_3\le\frac32\lambda.
\]

此时

\[
\boxed{
\nu_5=3\lambda-2m_3.
}
\]

### 通道 III：balance

\[
\sigma_5=0,
\qquad
\lambda=m_3.
\]

该支中 \(5\)-进范数至少达到尾长深度，并存在更细的 gap 分类。

这三条通道说明 \(m_3,\lambda,v_5(u)\) 不能独立增长。

---

## 12.7 Hensel 商与 \(\rho\) 的恢复

定义

\[
\boxed{
f=5^{E_5}q_Q+2c_u.
}
\]

存在奇整数 \(\omega,\theta\) 使

\[
\boxed{
5^{E_5}q_Q+c_u
=
2^{t-1}\rho\omega,
}
\]

\[
\boxed{
5^{m_2+\lambda}+c
=
2^{t-1}\rho\theta.
}
\]

二式相减整理得到

\[
\boxed{
c_Q\omega-\theta
=
2^{m_3}5^{E_5}c_u.
}
\]

并且

\[
\boxed{
\gcd(\omega,\theta)=1.
}
\]

于是

\[
\boxed{
2^{t-1}\rho
=
\gcd(
5^{E_5}q_Q+c_u,\,
5^{m_2+\lambda}+c
).
}
\]

因此

\[
\boxed{
\rho
=
\frac{
\gcd(
5^{E_5}q_Q+c_u,\,
5^{m_2+\lambda}+c
)
}{
2^{t-1}
}.
}
\]

也就是说 \(\rho\) 同样失去了独立自由度。

---

## 12.8 完全去二的平方判别式

定义

\[
A_0=a_1 10^{m_2-1},
\qquad
P=A_0+a_2,
\]

以及

\[
C_0=\frac{a_1b_2}{2}.
\]

定义 deep-even 前两块奇范数

\[
\boxed{
\mathcal N_0=C_0^2+a_2^2.
}
\]

它与全局 \(\mathcal N_{12}\) 的关系是

\[
\mathcal N_{12}=4\mathcal N_0
\]

因为此时 \(b_1=2\)。

定义

\[
K_0
=
25\cdot2^{2(m_3+t)}u^2P^2
-
Q_0^2\mathcal N_0.
\]

判别平方可写成

\[
\boxed{
5^\lambda
\left(
5^\lambda K_0
-
2cQ_0\mathcal N_0
\right)
=
Z^2.
}
\]

再令

\[
\boxed{
\mathcal A
=
5^{\lambda+1}2^{m_3+t}uP,
}
\]

则完全等价于差平方系统

\[
\boxed{
\mathcal A^2-Z^2
=
5^\lambda Q_0\mathcal N_0
\left(
5^\lambda Q_0+2c
\right).
}
\]

所以存在正奇数因子 \(U_-,U_+\) 满足

\[
\boxed{
U_-U_+
=
5^\lambda Q_0\mathcal N_0
(5^\lambda Q_0+2c),
}
\]

\[
\boxed{
U_-+U_+
=
2\mathcal A.
}
\]

这把 \(A_2\) 的无界问题从混合二进/五进/高斯结构压成了一个纯奇数的“乘积已知 + 和已知”的差平方因子分配问题。

---

## 12.9 实数十进制窗口

定义

\[
x=\frac{b_2}{10^{m_2}},
\qquad
y=\frac{a_2}{10^{m_2-1}},
\qquad
w=\frac{b_3}{10^{m_3}}.
\]

已经得到 core-specific 的严格窗口：

\[
\boxed{
\begin{array}{c|c}
a_1&x\\ \hline
5&27/250<x<3/16\\
7&1/10\le x<7/40\\
9&1/10\le x<3/20\\
11&1/10\le x<1/8\\
13&1/10\le x<11/100
\end{array}
}
\]

第二分子被压在其十进制区间顶部：

\[
\boxed{
\begin{array}{c|c}
a_1&y\\ \hline
5&y>0.93\\
7&y>0.84\\
9&y>0.83\\
11&y>0.88\\
13&y>0.95
\end{array}
}
\]

第三分母被压在其位数区间顶部：

\[
\boxed{
\begin{array}{c|c}
a_1&w\\ \hline
5&w>20/21\\
7&w>7/8\\
9&w>5/6\\
11&w>5/6\\
13&w>10/11
\end{array}
}
\]

而第三分子则被压在其位数区间底部。

这种“第二分子接近上端、第二分母接近下端、第三分母接近上端、第三分子接近下端”的反向挤压，是 \(A_2\) 终端系统中非常重要的实几何刚性。

---

# 13. \(A_2\) 的 factor allocation

对差平方两因子做最简分母恢复后，可写

\[
U_-=f\xi,
\qquad
U_+=q_Q\upsilon,
\]

并有

\[
\boxed{
\xi\upsilon
=
5^{E_5}c_Q^2\mathcal N_0.
}
\]

同时

\[
\boxed{
\upsilon-5^{E_5}\xi
=
2^t5^{2E_5-m_3}\rho a_3.
}
\]

若

\[
p^e\Vert c_Q,
\]

则该完整素数幂不能分散到两边，必须全部进入 \(\xi\) 或全部进入 \(\upsilon\)。

因此存在唯一互素分解

\[
\boxed{
c_Q=c_-c_+,
\qquad
\gcd(c_-,c_+)=1,
}
\]

使去掉共同五进部分后

\[
\boxed{
\xi=c_-^2X,
\qquad
\upsilon=c_+^2Y.
}
\]

这叫做 \(c_Q\) 的 square-side allocation。

同类分析也可以对 \(\rho\) 做平方单边分配。

于是原本每个素数幂都有很多组合方式的 factor allocation，被压缩为每个完整 prime power 的二元选择。

---

# 14. \(A_2\) 的 Gaussian rectangle 与 prefix defect

这一阶段的目的，是进一步研究差平方终端式中必然出现的 \(3\bmod4\) 奇素数。

定义 source-side 量

\[
U_5=5^{m_2-\sigma_5},
\]

以及

\[
D_0=2^{m_3+t-1}\rho,
\]

\[
H_s=D_0c_u.
\]

由 source split 有

\[
\boxed{
c_Qq_Q=U_5+H_s.
}
\]

固定十进制斜率满足

\[
\boxed{
U_5C_0=10H_sA_0.
}
\]

定义正交误差

\[
\boxed{
L_0
=
U_5a_2-10H_sC_0.
}
\]

实数窗口可以严格证明

\[
\boxed{
L_0<0.
}
\]

同时

\[
\boxed{
\gcd(L_0,a_2)
=
\gcd(a_2,5a_1).
}
\]

所以能够同时进入 \(L_0\) 与 \(a_2\) 的 \(3\bmod4\) 素数只能来自固定 core 的小素数。

再定义

\[
M_0=U_5C_0+10H_sa_2.
\]

由固定斜率，

\[
\boxed{
M_0=10H_sP.
}
\]

于是有 Gaussian 乘法恒等式

\[
\boxed{
L_0+iM_0
=
(U_5+10iH_s)(a_2+iC_0).
}
\]

因此

\[
\boxed{
L_0^2+M_0^2
=
(U_5^2+100H_s^2)\mathcal N_0.
}
\]

这一结构把“十进制固定斜率”直接嵌入高斯整数乘法。

---

## 14.1 Prefix defect

定义

\[
\boxed{
\Delta_{\rm pref}
=
A_0^2+C_0^2-P^2.
}
\]

展开为

\[
\Delta_{\rm pref}
=
C_0^2-2A_0a_2-a_2^2.
\]

这是纯粹由第一、第二块决定的整数。

第二层 surplus \(E_1\) 可以精确写成

\[
\boxed{
E_1
=
R_*\Delta_{\rm pref}
+
\Sigma a_2^2,
}
\]

其中

\[
R_*=100\,5^{E_5}H_s^2
\]

而 \(\Sigma\) 是 denominator/source 乘积因子。

关键 gcd 关系是

\[
\boxed{
\gcd(q_Qf,E_1)
=
\gcd(q_Qf,\Delta_{\rm pref}).
}
\]

这意味着所有 denominator-side 对 \(E_1\) 的接触，都被同一个纯前缀整数 \(\Delta_{\rm pref}\) 控制。

还得到

\[
\boxed{
\Delta_{\rm pref}\equiv7\pmod8.
}
\]

对

\[
a_1=9,11,13
\]

可以进一步证明

\[
\boxed{
\Delta_{\rm pref}>0.
}
\]

---

## 14.2 Odd inert excess

第二层结构给出

\[
E_1\equiv3\pmod4.
\]

另一方面，相关 source norm 与 \(\mathcal N_0\) 中 \(3\bmod4\) 素数的赋值受到二平方和奇偶约束。

因此必然存在某个

\[
p\equiv3\pmod4
\]

使第二层产生一个正奇数的“额外赋值”。

统一称其为

\[
\boxed{
\text{odd inert excess}.
}
\]

这里描述的是一类机制，并不指定某个固定素数：某个 inert prime 在第二层乘积中比基础二平方赋值多出奇数深度。

当前分析把它分成三类来源：

### I. Denominator-prefix excess

\[
p\mid q_Qf.
\]

这类接触完全受

\[
\Delta_{\rm pref}
\]

控制。

### II. Source excess

\[
p\mid \mathfrak n
\]

其中 \(\mathfrak n\) 是 source-side 二平方尺度。

这类 prime 与 denominator 已经证明完全分离：

\[
p\nmid q_Qfc_Qu_0.
\]

它们的 odd excess 只能通过一种高阶 Hensel 角接触产生。

### III. Spontaneous angle excess

\[
p\nmid \mathfrak n q_Qf\mathcal N_0,
\qquad
p\mid E_1.
\]

这类 prime 原先不属于 source 或 denominator，只在第二层角度条件中自发出现，目前最难统一排除。

---

# 15. \(A_2\) 的 source 双 Hensel 系统

对 source inert prime，可以把原来的复杂二次表达式线性化。

定义

\[
L_+=5^{E_5}D_0+c_Q,
\]

\[
L_-=99\,5^{E_5}D_0-2c_Q.
\]

source 参数 \(\sigma\) 满足

\[
\boxed{
2\sigma
=
c_uD_0L_-
-
2U_5L_+.
}
\]

因此 \(\sigma\) 对纯五次幂

\[
U_5=5^{m_2-\sigma_5}
\]

是线性的。

若

\[
p^{2h}\Vert\sigma,
\qquad
p\equiv3\pmod4,
\]

则 \(U_5\) 必须以精确深度 \(2h\) 贴近一个显式有理 Hensel 根。

为了与十进制窗口结合，引入归一化变量

\[
x=\frac{b_2}{10^{m_2}},
\qquad
y=\frac{a_2}{10^{m_2-1}},
\]

以及一个 source-normalized 变量

\[
z=\frac{5^{E_5}D_0}{c_Q}.
\]

其实际实数意义可化为

\[
z=\frac{b_2}{w},
\]

而 \(w=b_3/10^{m_3}\) 已经被压在接近 \(1\) 的窄窗口中。

定义第一个 Hensel 多项式

\[
\boxed{
\Phi(x,z)
=
(99x-4)z-2x-4.
}
\]

若

\[
p^{2h}\Vert\sigma,
\]

则

\[
\boxed{
v_p(\Phi(x,z))=2h.
}
\]

于是

\[
z
\equiv
\frac{2x+4}{99x-4}
\pmod{p^{2h}}.
\]

再定义第二个 Hensel 多项式

\[
\boxed{
\Psi_{a_1}(y,z)
=
400a_1(z+1)^2
-y(99z-2)^2.
}
\]

source odd excess 若存在，还必须满足

\[
\boxed{
v_p(\Psi_{a_1}(y,z))\ge h.
}
\]

因此 source odd excess 被压缩为非常特殊的

\[
\boxed{
2h:h
}
\]

双 Hensel 接触：

\[
\boxed{
v_p(\Phi)=2h,
\qquad
v_p(\Psi_{a_1})\ge h.
}
\]

而 \(x,y,z\) 同时受到窄十进制实数窗口约束。

这已经远强于普通的 Legendre/Jacobi 二次剩余条件。

---

# 16. \(A_2\) 的有限证书与当前开放核

严格有限计算已经关闭

\[
\boxed{
m_2\le10
}
\]

的 deep-even 终端切片。

后来使用 denominator recovery 与实数 core window 对

\[
m_2=11,12,13
\]

进行了更强诊断，没有看到 denominator/core 幸存者，\(m_2=14,15\) 也极为稀疏；但这些更高层结果目前应视为结构诊断，不能替代无界证明。

当前 \(A_2\) 的真正任务是：

\[
\boxed{
m_2\ge11
\Longrightarrow
\text{终端系统无解}.
}
\]

现阶段最值得保留的两类方法是：

1. **source linear Hensel + decimal rigidity**：研究
   \[
   \operatorname{Res}_z(\Phi,\Psi_{a_1}),
   \]
   或将
   \[
   z=\frac{2x+4}{99x-4}
   \]
   代回 \(\Psi_{a_1}\)，把高阶 \(p\)-进接触压成仅含 \(x,y,a_1\) 的显式多项式；
2. **二维 ellipse / Gaussian rectangle + 真实十进制 phase**：停止 generic quadratic-character chasing，改为利用 ellipse 的连续几何窗口与 \(2\)-进、\(5\)-进相位的离散性直接制造冲突。

---

