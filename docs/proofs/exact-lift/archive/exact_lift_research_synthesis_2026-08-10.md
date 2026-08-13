# 三块十进制拼接 Exact Lift 问题：研究综述、统一符号与当前证明路线

> **整理日期：2026-08-11**  
> **文档性质：研究综述 / 证明状态总汇 / 后续攻关基准稿**  
> **当前严格状态：主不存在性命题尚未完成证明。**  
> 本文只把已经有完整论证支持的结论标为“已证”；有限枚举仅视为有限切片证书；曾经提出但后来发现有逻辑缺口、退化为恒等式或不能保持十进制结构的路线，统一列入“失效或降级路线”，不得继续作为已证结论使用。

---

## 摘要

给定三组正的既约有理数

\[
r_i=\frac{a_i}{b_i},\qquad \gcd(a_i,b_i)=1,\qquad i=1,2,3,
\]

把三个分子按十进制顺序拼接为整数 \(\alpha\)，把三个分母按同样顺序拼接为整数 \(\beta\)。研究目标是判断是否可能存在

\[
\frac{\alpha}{\beta}
=
\sqrt{r_1^2+r_2^2+r_3^2}.
\]

整个研究的核心困难来自两套算术结构的耦合：左侧由十进制位数、\(2\)-进和 \(5\)-进结构控制；右侧由有理球面、平方判别式、二平方和与高斯整数分解控制。经过多轮归约，目前已经形成一套比较完整的统一框架：

1. 把拼接比值改写成三个经过十进制放大的坐标的正权平均，由 carrier 条件排除正常位数区域，并把所有候选分成 \(A_2\)-only、double-deficit 与 \(A_1\)-only 三个异常分支；
2. 把有理球面提升为整数球面
   \[
   y_1^2+y_2^2+y_3^2=H^2
   \]
   与整数平面
   \[
   q\alpha=H\beta,
   \]
   同时得到精确的 primitive recovery
   \[
   \gcd(q,y_i)=q/b_i;
   \]
3. 对三个分支统一提出第三分母与十进制尾幂的公共因子，建立尾商 \(L\)、尾权 \(\kappa\)、平方判别式、第三块本原二次式和逐素数 denominator prime graph；
4. 在高斯整数环中分析
   \[
   y_1^2+y_2^2=(H-y_3)(H+y_3),
   \]
   得到完整的共轭因子匹配与局部素数分配规律；
5. 证明高斯翻面虽然严格改变球面因子的尺度，但通常离开原来的十进制系数平面，因此不能直接形成传统无限下降；
6. 对 \(A_2\) 分支，已经压缩到唯一 deep-even 终端通道，并进一步发展出 source split、\(2\)-进 Hensel 锁、\(5\)-进同步、平方单边分配、Gaussian rectangle、prefix defect、odd inert excess 与双 Hensel 接触系统；
7. 对 double-deficit 分支，已经把原本高维的无界参数空间压缩到若干显式线性锥；先由“拼接行列式 gap 的赋值恒等式 + 阿基米德高度上界”排除 \(2/5\)-进双 resonance 顶部，再由二进主导项与球面差分排除整个单五进 resonance 中高层，并把全局相对界降到 \(n_3\le9S_{12}+1\)；
8. 对 \(A_1\)-only 的 saturated 支 \(L=1\)，已经证明自由尾长受 denominator-only 上界控制，但 decimal shift \(g\) 仍然可能无界。

当前最有价值的 DD 策略已经从“继续逐素数追同余”转向“把十进制 gap 的精确 \(p\)-进深度、球面主导项与全局高度预算直接比较”。这一方法现已关闭所有 \(n_3\ge9S_{12}+2\) 的 DD 候选。DD 仍剩下随 \(S_{12}\) 增长的中低层无界锥，特别是五进 resonance 阈值以下的 \(d_3\)-dominant 区域；随后还需回到 \(A_2\) 的双 Hensel / ellipse 系统，并为 \(A_1\) saturated 支寻找保持十进制 coefficient plane 的新不变量。

---

# 1. 原问题与统一符号

## 1.1 基本数据

对 \(i=1,2,3\)，令

\[
r_i=\frac{a_i}{b_i}>0,
\qquad
\gcd(a_i,b_i)=1,
\]

其中 \(a_i,b_i\) 均为无前导零的正整数。

统一记

\[
n_i=\operatorname{digits}(a_i),
\qquad
m_i=\operatorname{digits}(b_i),
\]

以及分子、分母位数差

\[
\boxed{s_i=n_i-m_i.}
\]

三个分子与三个分母的十进制拼接分别为

\[
\boxed{
\alpha
=
a_1 10^{n_2+n_3}
+a_2 10^{n_3}
+a_3,
}
\]

\[
\boxed{
\beta
=
b_1 10^{m_2+m_3}
+b_2 10^{m_3}
+b_3.
}
\]

目标命题是

\[
\boxed{
\text{不存在正既约有理数三元组使 }
\frac{\alpha}{\beta}
=
\sqrt{r_1^2+r_2^2+r_3^2}.
}
\]

本文把右侧欧氏长度统一记为

\[
\boxed{
\mathcal R
:=
\sqrt{r_1^2+r_2^2+r_3^2}.
}
\]

---

## 1.2 十进制权重与 carrier 放大因子

定义三个分母位置权重

\[
B_1=10^{m_2+m_3},
\qquad
B_2=10^{m_3},
\qquad
B_3=1,
\]

以及正权

\[
w_i=B_i b_i.
\]

定义十进制放大因子

\[
\Lambda_1=10^{s_2+s_3},
\qquad
\Lambda_2=10^{s_3},
\qquad
\Lambda_3=1.
\]

则拼接式恒等地写成

\[
\alpha
=
\sum_{i=1}^3 w_i\Lambda_i r_i,
\qquad
\beta
=
\sum_{i=1}^3w_i.
\]

因此 exact lift 等式等价于

\[
\boxed{
\mathcal R
=
\frac{
w_1\Lambda_1r_1
+w_2\Lambda_2r_2
+w_3r_3
}{
w_1+w_2+w_3
}.
}
\]

右端是三个数

\[
\Lambda_1r_1,\qquad
\Lambda_2r_2,\qquad
r_3
\]

的严格正权平均。

由于

\[
\mathcal R>r_i
\]

对所有 \(i\) 都成立，第三坐标

\[
\Lambda_3r_3=r_3
\]

永远不可能达到 \(\mathcal R\)。因此若 exact lift 存在，第一、第二坐标至少有一个必须满足

\[
\Lambda_i r_i\ge \mathcal R.
\]

这就是整个分支理论的 carrier 原理。

---

# 2. Carrier 几何与三个异常分支

如果

\[
s_3\le0,
\qquad
s_2+s_3\le0,
\]

则

\[
\Lambda_1\le1,
\qquad
\Lambda_2\le1.
\]

于是

\[
\Lambda_1r_1<\mathcal R,\qquad
\Lambda_2r_2<\mathcal R,\qquad
r_3<\mathcal R,
\]

三个正权平均项全部小于 \(\mathcal R\)，矛盾。

因此正常位数区域被严格排除。

所有可能候选恰好处于以下三个异常 chamber：

| 分支 | 位数条件 | 可能承担 carrier 的坐标 |
|---|---|---|
| \(A_2\)-only | \(s_3>0,\ s_2+s_3\le0\) | 第二坐标 |
| double-deficit（DD） | \(s_3>0,\ s_2+s_3>0\) | 第一、第二坐标 |
| \(A_1\)-only | \(s_3\le0,\ s_2+s_3>0\) | 第一坐标 |

所以主命题已经严格化为：

\[
\boxed{
\text{分别证明 }A_2\text{-only、DD、}A_1\text{-only 三个分支均为空。}
}
\]

---

# 3. 整数球面提升与 primitive recovery

令

\[
\boxed{
q=\operatorname{lcm}(b_1,b_2,b_3),
}
\]

并定义

\[
\boxed{
y_i=\frac{a_iq}{b_i}.
}
\]

若 exact lift 成立，则

\[
q\mathcal R
=
\sqrt{y_1^2+y_2^2+y_3^2}.
\]

另一方面

\[
\mathcal R=\frac{\alpha}{\beta},
\]

所以

\[
q\mathcal R=\frac{q\alpha}{\beta}
\]

是有理数。一个整数的平方根若为有理数，则必为整数。于是存在正整数 \(H\) 满足

\[
\boxed{
y_1^2+y_2^2+y_3^2=H^2,
}
\]

并且

\[
\boxed{
q\alpha=H\beta.
}
\]

这是原问题最关键的算术提升：十进制拼接问题被嵌入“整数球面 + 整数线性平面”的交。

需要强调：\(q=\operatorname{lcm}(b_i)\) 本身并不能自动保证四元组
\((y_1,y_2,y_3,H)\) 整体本原。因此本文避免把它无条件称为“本原四元组”；真正无条件成立的是下面的逐坐标恢复恒等式。

对每个 \(i\)，

\[
\boxed{
\gcd(q,y_i)=\frac{q}{b_i}.
}
\]

逐素数看，若

\[
E=v_p(q),
\qquad
e_i=v_p(b_i),
\]

则

\[
v_p(\gcd(q,y_i))=E-e_i.
\]

因此分母中每个素数的赋值模式，都会精确映射到球面坐标中对应的消失深度。这是后续 denominator prime graph 的基础。

---

# 4. 全局统一的前两块对象

为了减少三个分支之间重复记号，统一定义

\[
\boxed{
Q=b_1 10^{m_2}+b_2,
}
\]

\[
\boxed{
G=b_1b_2,
}
\]

以及前两块的二平方型

\[
\boxed{
\mathcal N_{12}
=
(a_1b_2)^2+(a_2b_1)^2.
}
\]

其中 \(Q\) 是前两分母的普通十进制拼接，\(G\) 是两个分母的乘积，\(\mathcal N_{12}\) 则是

\[
G^2(r_1^2+r_2^2).
\]

后续很多统一判别式都由这三个对象控制。

对三个分支，还可引入统一的 coefficient pair \((C,D)\)：

\[
(C,D)=
\begin{cases}
\left(a_1 10^{m_2}+10a_2,\ Q\right),
& A_2,\\[0.6em]
\left(10^{m_2+k_{12}}a_1+10^{d_3}a_2,\ Q\right),
& DD,\\[0.6em]
\left(10^{g+k_{12}+m_2}a_1+a_2,\ 10^gQ\right),
& A_1,
\end{cases}
\]

其中在 DD 中统一记

\[
d_3=s_3>0,
\qquad
k_{12}=s_2+s_3>0,
\]

而在 \(A_1\) 中记

\[
g=-s_3\ge0,
\qquad
k_{12}=s_2+s_3\ge1.
\]

---

# 5. 第三块尾部的统一正规化

三个异常分支都存在一个“第三块十进制尾幂与第三分母公共部分”的正规化。

统一定义有效尾长

\[
\ell=
\begin{cases}
m_3,&A_2,\ DD,\\
m_3-g,&A_1.
\end{cases}
\]

再令

\[
\boxed{
\delta_3=\gcd(10^\ell,b_3),
}
\]

\[
\boxed{
L=\frac{10^\ell}{\delta_3},
\qquad
\tau=\frac{b_3}{\delta_3}.
}
\]

于是

\[
\gcd(L,\tau)=1.
\]

第三分子的对应本原化记为

\[
\boxed{
z_3=\frac{a_3}{\delta_3}.
}
\]

该正规化的核心含义是：十进制尾部中强制出现的 \(2\)-、\(5\)-因子全部被剥出，剩余的 \(L\) 是真正参与高斯因子转移和平方判别的“尾商”。

对 \(A_2\) 与 DD，必有 \(L>1\)。  
对 \(A_1\)，只有一种特殊情形可能出现

\[
L=1,
\]

即 decimal-saturated 支。这一支后来被证明是整个 \(A_1\) 中最特殊的难点。

---

# 6. 统一尾权 \(\kappa\)

三个分支中看似不同的第三块实参数，实际上都可以压入同一个整数 \(\kappa\)。

统一结论为

\[
\boxed{
QG<\kappa\le10QG.
}
\]

对 \(A_2\) 和 DD，

\[
\boxed{
\kappa
=
\frac{10^{m_3}QG}{b_3}
=
\frac{LQG}{\tau}
\in\mathbf Z.
}
\]

因而

\[
\frac{\tau}{L}
=
\frac{QG}{\kappa}.
\]

对 \(A_1\) 则有相应的带 \(10^g\) 形式：

\[
\boxed{
\kappa
=
\frac{10^gLQG}{\tau}
\in\mathbf Z,
}
\]

这个整数区间

\[
QG<\kappa\le10QG
\]

非常重要：第三块尾部虽然位数可以变长，但它的核心斜率只能由前两块尺度 \(QG\) 的一个固定十倍窗口控制。

---

# 7. 统一二次式、判别平方与 primitive recovery

令球面 gap 的统一有理参数满足

\[
G(\mathcal R-r_3)=\frac{\mu}{\nu},
\qquad
\gcd(\mu,\nu)=1.
\]

三个异常分支都可以化成

\[
\boxed{
D(\kappa+2G)\mu^2
-2G\kappa C\,\mu\nu
+\kappa D\mathcal N_{12}\nu^2
=0.
}
\]

由本原性立刻得到

\[
\boxed{
\nu\mid D(\kappa+2G),
\qquad
\mu\mid \kappa D\mathcal N_{12}.
}
\]

定义统一判别核

\[
\boxed{
K_{C,D}
=
G^2C^2-D^2\mathcal N_{12}.
}
\]

则有理解存在的必要条件是

\[
\boxed{
\kappa
\left(
\kappa K_{C,D}
-2GD^2\mathcal N_{12}
\right)
=
W^2
}
\]

对某个整数 \(W\)。

这条“统一判别平方”目前是三个分支最重要的公共算术约束之一。

进一步定义

\[
G_0
=
\gcd(
\mathcal N_{12}\nu^2-\mu^2,\,
2G\mu\nu
).
\]

第三块的 primitive recovery 可以写成

\[
\boxed{
10^{m_3}QG_0
=
2\kappa\mu\nu
}
\]

（在 \(A_1\) 中按有效尾长做相应替换）。

一个后来得到的重要全局结论是

\[
\boxed{
G_0\mid2G\mathcal N_{12}.
}
\]

因此 \(G_0\) 不能作为新的无界素数储存池。第三块恢复过程中所有额外 gcd 的素因子，仍然被前两块对象控制。

---

# 8. 三分支统一的 primitive tail quadratic

利用

\[
10^\ell=\delta_3L,
\qquad
b_3=\delta_3\tau,
\qquad
a_3=\delta_3z_3,
\]

三个分支共同满足一个关于 \(z_3\) 的本原二次方程：

\[
\boxed{
-\kappa(\kappa+2G)z_3^2
+2G^2LC\,z_3
+\mathcal C_3
=0,
}
\]

其中

\[
\boxed{
\mathcal C_3
=
G^2L^2C^2
-\mathcal N_{12}(LD+\tau)^2.
}
\]

由有理根定理得到

\[
\boxed{
\delta_3\mid\kappa(\kappa+2G),
}
\]

\[
\boxed{
a_3\mid\mathcal C_3.
}
\]

又因为 \(L\mid\kappa\)，所以

\[
\boxed{
10^\ell
\mid
\kappa^2(\kappa+2G).
}
\]

这是目前最干净的三分支统一 denominator-tail certificate。

它直接导致一个粗但完全前缀一致的尾长锥：

若记

\[
S_{12}=m_1+m_2,
\]

则

\[
Q,G<10^{S_{12}},
\]

从而

\[
\boxed{
\ell\le6S_{12}+3.
}
\]

即

\[
\boxed{
m_3\le6S_{12}+3
}
\]

对 \(A_2\)、DD 成立，而 \(A_1\) 有

\[
\boxed{
m_3-g\le6S_{12}+3.
}
\]

这个结果第一次把第三块无界尾长整体压入“前两分母位数的线性锥”。

---

# 9. Primitive Vieta 对与第三分子的 prime flow

定义

\[
\boxed{
\delta_3^\vee
=
\frac{\kappa(\kappa+2G)}{\delta_3},
}
\]

\[
\boxed{
a_3^\vee
=
\frac{\mathcal C_3}{a_3}.
}
\]

则二次式可以精确分解为

\[
\boxed{
\kappa(\kappa+2G)X^2
-2G^2LCX
-\mathcal C_3
=
(\delta_3X-a_3)
(\delta_3^\vee X+a_3^\vee).
}
\]

因而

\[
\delta_3\delta_3^\vee
=
\kappa(\kappa+2G),
\]

\[
a_3a_3^\vee
=
\mathcal C_3,
\]

并有交叉差

\[
\boxed{
a_3\delta_3^\vee
-\delta_3a_3^\vee
=
2G^2LC.
}
\]

若某个素数满足

\[
p\nmid2GLC,
\qquad
p\mid a_3,
\]

则

\[
p\nmid a_3^\vee,
\qquad
p\nmid\delta_3,
\]

并且

\[
\boxed{
v_p(a_3)=v_p(\mathcal C_3).
}
\]

同时有

\[
\boxed{
\mathcal N_{12}
\equiv
\left(
\frac{GLC}{LD+\tau}
\right)^2
\pmod{p^{v_p(a_3)}}.
}
\]

因此第三分子的“自由素数”并不自由：它们必须以完整 prime-power 深度满足一个 \(\mathbf Q(\sqrt{\mathcal N_{12}})\) 中的分裂条件。

这条结果保留了 Vieta 结构的算术价值，但它本身不能形成正整数解之间的无限下降；后面会解释原因。

---

# 10. Denominator prime graph

对任意素数 \(p\)，记

\[
e_i=v_p(b_i),
\qquad
E=\max(e_1,e_2,e_3).
\]

## 10.1 奇素数 \(p\neq2,5\)

如果最大赋值只在一块出现，例如

\[
e_1=E>e_2,e_3,
\]

则 complementary denominator concatenation 强迫

\[
p^E\mid b_2 10^{m_3}+b_3.
\]

由于 \(p\nmid10\)，若 \(e_2\ne e_3\)，右侧赋值只能等于

\[
\min(e_2,e_3)<E,
\]

矛盾。因此

\[
\boxed{
\text{unique max}
\Longrightarrow
\text{另外两块的 }p\text{-进指数相等}.
}
\]

如果最大值由恰好两块取得，则球面方程模 \(p\) 强迫

\[
y_i^2+y_j^2\equiv0\pmod p.
\]

若 \(p\equiv3\pmod4\)，这只有在两项都被 \(p\) 整除时才能发生，从 recovery 再追溯会与 pair-max 结构冲突。因此 pair-max 只能由

\[
\boxed{
p\equiv1\pmod4
}
\]

的奇素数承担。

## 10.2 素数 \(2\)

整数球面模 \(4\) 给出

\[
\boxed{
H\text{ 为奇数},
}
\]

并且

\[
\boxed{
y_1,y_2,y_3
\text{ 中恰有一个奇数}.
}
\]

由 primitive recovery 可推出

\[
\boxed{
\max_i v_2(b_i)
\text{ 必须唯一取得}.
}
\]

因此 denominator prime graph 的全局 skeleton 为

\[
\boxed{
\begin{array}{c|c}
p=2 & \text{最大指数必须唯一}\\
p\equiv3\pmod4,\ p\neq5
& \text{不能 pair-max}\\
p\equiv1\pmod4
& \text{允许 pair-max}
\end{array}
}
\]

这组结构对三个异常分支同时有效。

---

# 11. 高斯整数结构：成功之处与边界

整数球面给出

\[
y_1^2+y_2^2
=
(H-y_3)(H+y_3).
\]

在 \(\mathbf Z[i]\) 中，

\[
y_1^2+y_2^2
=
(y_1+iy_2)(y_1-iy_2).
\]

把第三块尾商 \(L\) 从

\[
H-y_3
\]

中剥出，可以构造正规化高斯因子，并得到形如

\[
N(h_0)=E_0a,
\]

\[
N(k_0)=LE_0(H+y_3),
\]

\[
h_0k_0
=
-E_0\overline{(y_1+iy_2)}
\]

的双范数系统。

通过逐素数分析，可以建立完整的 conjugate-factor matching：所有与 \(a\) 互素的高斯素因子都能够在共轭两侧严格匹配；潜在失配只可能出现在

\[
p\mid\gcd(E_0,a)
\]

的局部容量不足位置。

这一步后来进一步得到惰性异常素数的全局定位：

- 在 \(A_2\) 相邻边界区中，\(p\equiv3\pmod4\) 的异常核为空；
- 在 DD 与 \(A_1\) 中，若 \(p\equiv3\pmod4\) 真正进入异常核，则必须有
  \[
  e_1=e_2=e<e_3=E,
  \]
  并且
  \[
  p^E\mid A+B,
  \]
  同时
  \[
  v_p(a)=2(E-e).
  \]

因此局部高斯因子匹配本身已经相当完整。

然而，最重要的负面结论是：

\[
\boxed{
\text{高斯 flip 不保持原十进制 coefficient plane。}
}
\]

翻面会把球面因子大致从

\[
(La,\ H+y_3)
\]

转移为

\[
(a,\ L(H+y_3)).
\]

球面尺度确实严格变化，但原本的十进制平面关系会出现额外因子 \(L\)。例如在 DD 中，原有

\[
A+B=c
\]

类型的系数关系，翻面后变成

\[
A'+B'=Lc',
\]

因此离开原来的 exact-lift 系数族。

所以：

\[
\boxed{
\text{Gaussian descent 是有效的局部因子归约，但目前无法充当可迭代的全局下降。}
}
\]

---

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

与两个非 \(d_3\)-dominant 扇区的 \(n_3\le7S_{12}+4\) 合并，得到当前 DD 的统一相对界

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

## 27.9 这一结论的逻辑边界

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

---

# 28. \(A_1\)-only 分支

\(A_1\)-only 满足

\[
s_3\le0,
\qquad
s_2+s_3>0.
\]

统一记

\[
\boxed{
g=-s_3\ge0,
}
\]

\[
\boxed{
k_{12}=s_2+s_3\ge1.
}
\]

有效第三尾长为

\[
\boxed{
\ell=m_3-g.
}
\]

定义

\[
U=H-y_3,
\qquad
\mathcal S_{12}=y_1^2+y_2^2.
\]

经过第三块正规化，同样有

\[
\boxed{
U=La,
\qquad
La\mid\mathcal S_{12}.
}
\]

并且

\[
H
=
\frac12
\left(
La+\frac{\mathcal S_{12}}{La}
\right),
\]

\[
y_3
=
\frac12
\left(
\frac{\mathcal S_{12}}{La}
-La
\right).
\]

---

## 28.1 薄环约束

由第一坐标 carrier 及球面条件可得到 \(La\) 必须处在一个很薄的实数区间：

\[
\boxed{
10^{k_{12}}y_1
-
\sqrt{
(10^{2k_{12}}-1)y_1^2-y_2^2
}
<
La
<
\sqrt{\mathcal S_{12}}.
}
\]

这说明 tail gap 并非可以任意选取二平方和的除数，并且必须同时处在一个很窄的几何环带中。

---

## 28.2 尾商斜率锁

第三分母正规化进一步给出

\[
\boxed{
10^{g-1}
\le
\frac{\tau}{L}
<
10^g.
}
\]

因此 \(g\) 直接锁定 normalized denominator quotient 的数量级。

---

# 29. \(A_1\) 的 saturated 支 \(L=1\)

当

\[
L>1
\]

时，高斯因子转移至少存在严格尺度变化。

真正特殊的是

\[
\boxed{
L=1.
}
\]

这等价于有效尾幂

\[
10^\ell
\]

已经全部被第三分母吸收。

旧思路曾希望在这里继续 Gaussian descent，但后来严格检查发现：

\[
\boxed{
L=1
\text{ 时 Gaussian flip 只是 projective identity}.
}
\]

约掉整体尺度后，球面点与线性平面都回到原对象，没有任何严格变小的高度。

所以 saturated 支必须采用独立于 Gaussian descent 的机制。

---

# 30. \(A_1\) saturated 的 denominator-only 尾长界

对整个 saturated 支，可以不再分别处理旧稿中的若干高侧二进/五进子分支，而直接得到

\[
\boxed{
\ell
\le
\left\lfloor
\log_5((10Q+2)G)
\right\rfloor.
}
\]

粗化为

\[
\boxed{
\ell
\le
3(m_1+m_2)+1.
}
\]

这是一个重要进展：saturated 支原本看似可以任意增长的“有效第三尾长”已经被前两分母位数线性控制。

因此 \(A_1\) 中真正还可能独立无界的量主要变成了 decimal shift

\[
\boxed{
g.
}
\]

---

# 31. \(A_1\) saturated 的奇素数约束

令

\[
d_*=\gcd(\tau,10^gQ),
\]

\[
h=\frac{\tau}{d_*}.
\]

可证明

\[
\boxed{
\gcd(U,h)=1,
}
\]

并且

\[
\boxed{
h\mid G.
}
\]

更强地，\(h\) 的所有奇素因子满足

\[
\boxed{
p\equiv1\pmod4.
}
\]

还有

\[
\boxed{
h
\mid
\frac{
b_1b_2
}{
\gcd(b_1,b_2)^2
}.
}
\]

所以 saturated 第三分母中所有非十进制“新奇素数”都必须来自前两分母的不共享部分，而且只能是 \(1\bmod4\) 素数。

这大幅限制了 denominator prime supply，却仍没有直接给出 \(g\) 的统一上界。

---

# 32. 早期“完整证明”为什么不能作为最终证明

研究过程中曾经形成过一版形式上已经把三个分支全部“关闭”的预印本框架。严格审计后发现，其中承担全局不存在性作用的若干步骤没有真正建立。

这些问题已经明确撤回，不能继续作为证明依据。

## 32.1 “完全共享分母结构已关闭”曾被无证明引用

如果每个素数在三个分母中的最高赋值都至少出现两次，可以严格得到

\[
b_1=q_0c_2c_3,
\]

\[
b_2=q_0c_1c_3,
\]

\[
b_3=q_0c_1c_2,
\]

其中 \(c_1,c_2,c_3\) 两两互素。

这个分解本身正确。

错误在于曾经从这里直接跳到“完全共享分母分支已经排除”。  
分解定理只描述结构，并没有自动导出与 exact balance 的矛盾。

后续研究通过更细 denominator prime graph、局部高斯匹配和分支正规化替代了这个未经证明的“总关闭”。

---

## 32.2 有限证书不能替代无界下降

早期 \(A_2\) 证明中曾经存在这样的逻辑：

1. 用计算排除一个有限盒子；
2. 宣称更高位候选会“下降”回该盒子；
3. 因而全局排除。

问题在于第 2 步没有给出保持以下所有性质的严格映射：

- 正性；
- 既约性；
- exact balance；
- 整数球面；
- 十进制位数；
- 同一 carrier 分支。

后续真正证明的 Gaussian flip 又不保持原十进制 coefficient plane，因此无法补上这条缺口。

现在有限证书只被用于已经先有严格参数上界的有限切片。

---

## 32.3 DD 中“素数同时进入 gap 与二平方和所以矛盾”不成立

曾经尝试认为某个独占最高素幂同时进入

\[
H-y_3
\]

和

\[
y_1^2+y_2^2
\]

会与二平方定理冲突。

这是错误的。

二平方定理对

\[
p\equiv3\pmod4
\]

只要求它在二平方和中的总赋值为偶数，并不禁止它同时整除一个因子 \(H-y_3\)。

因此 DD 后来必须转向更精细的：

- unique-max denominator graph；
- \(e_1=e_2<e_3\)；
- exact \(p\)-adic capacity；
- near-square；
- resonance；
- near-\(S\)-unit。

---

## 32.4 \(A_1\) 中“两个 gap 尺度不相容”的文字论证不够

早期 \(A_1\) 终端论证曾使用：

- 远 gap；
- 第二个独立 gap；
- cyclotomic kernel；
- 尺度不相容；

但没有给出一个可以逐行核验的矛盾，例如

\[
v_p(X)\ge A
\quad\text{且}\quad
v_p(X)\le A-1,
\]

或

\[
0<T<M\le T.
\]

因此该“terminal incompatibility”没有成立。

后续真正可靠的结果是薄环、尾商斜率、统一 tail quadratic、saturated tail bound 与 denominator-only 奇素数锁。

---

# 33. 后来被严格判死或降级的证明路线

## 33.1 \(A_2\to A_1\) 的 Vieta jumping

关于第三坐标的二次方程确实有 companion root。

但在相邻 \(A_2\) 中可以证明 companion 第三坐标全局为负。

做符号反射后虽然得到更小的正坐标

\[
\widehat r_3<r_3,
\]

甚至有精确差值

\[
r_3-\widehat r_3
=
\frac{
20GP
}{
Q(\kappa+2G)
},
\]

但反射后的点不再满足原十进制 coefficient plane。

所以没有合法的

\[
\text{正根}\to\text{更小正根}
\]

Vieta jumping。

---

## 33.2 反复 Gaussian flip

对 \(L>1\)，flip 确实把球面因子中的 \(L\) 从一侧移到另一侧。

然而十进制平面系数会多出 \(L\)，因此一次 flip 后就离开原族。

对 saturated \(L=1\)，flip 又退化为 projective identity。

所以两个极端都无法形成传统无限下降。

---

## 33.3 Source-only Legendre/Jacobi 全局乘积

曾经尝试把所有 source prime 的二次剩余条件相乘，希望得到全局 \(-1\)。

严格整理后发现各项之间存在结构性抵消，最终只得到

\[
\boxed{
1=1.
}
\]

这说明 source-only quadratic character 没有利用到真正关键的十进制相位信息。

---

## 33.4 Generic \(u_0,c_u,\rho\) 二次剩余追逐

大量模素数条件在已知 Gaussian norm / source split 下自动满足。

继续逐个做 Legendre symbol 只会重复已有局部 norm 条件，不能控制十进制 coefficient plane。

因此该路线被降级。

---

## 33.5 “模数大于区间”只给唯一性，不给空性

如果一个变量 \(R\) 满足 CRT 且

\[
0<R<D,
\]

而模数 \(M>D\)，只能推出区间内至多有一个候选。

这只是

\[
\boxed{
\text{at most one},
}
\]

因此无法推出

\[
\boxed{
\text{zero}.
}
\]

真正还需要证明唯一代表不能满足 Gaussian divisor、窄实数窗口或平方条件。

---

## 33.6 普通 class group / genus / Hasse norm

外部系数本身已经满足大量全局 norm 条件。

单独使用 genus theory 或普通 Hasse norm obstruction 没有直接抓住十进制 coefficient plane。

class group 中某个小 ideal class 也可能被 source-side prime 补偿。

因此这些工具目前只可能作为辅助，不适合做主路线。

---

## 33.7 Scalar descent

曾经构造过一个线性变换 \(\mathcal M\)，但它满足

\[
\mathcal M^2=-\mathfrak d I.
\]

也就是说两步变换只回到原向量的标量倍数。

这种结构属于有限阶/projective 对称，无法形成无限下降。

---

## 33.8 错误的 odd-inert 推断

曾一度从

\[
E_1+\mathcal K
=
R_*(A_0^2+C_0^2)
\]

以及某个 \(p\equiv3\pmod4\) 在 \(E_1\) 中奇次出现，直接推断

\[
p\mid a_1.
\]

这是无效的，因为赋值可能出现类似

\[
3+1=4
\]

的普通加法抵消。

因此曾经由此得到的“某些 core 已全局关闭”“所有 odd inert prime 必来自固定 core”等说法已经撤回。

真正留下来的结构是 odd inert excess 三分法与 source 双 Hensel 接触。

---

# 34. 有限计算在完整证明中的正确角色

有限计算目前有三种用途。

### 34.1 验证严格有界切片

例如 \(A_2\) deep-even 中

\[
m_2\le10
\]

已经可以用纯整数模平方证书排除。

只要候选范围本身先由严格数学推导得到，这类计算可以成为证明的一部分。

### 34.2 诊断无界参数空间的实际稀疏程度

例如更高 \(m_2\) 层的 denominator recovery 过滤，可以告诉我们哪些理论约束最有杀伤力，从而决定下一步该证明哪个统一引理。

这类结果是研究导航，不应写成全局定理。

### 34.3 为最终有限余项提供证书

最理想的全局证明不一定需要纯手工排除所有小参数。

如果能够先证明

\[
S_{12}\le S_0
\]

或

\[
m_2\le M_0,
\]

那么剩余有限范围完全可以由可复核的整数程序关闭。

因此目标不应执着于“完全不用计算”，而应要求：

\[
\boxed{
\text{无限族必须先被理论上统一压成有限族。}
}
\]

---

# 35. “固定前缀有限”与“全局空”之间的逻辑门槛

这是整个项目中最重要的方法论教训之一。

在 \(A_2\) 中，固定前两块后第三块可以被平方判别和 recovery 压成有限集合。

在 DD 中，固定 ghost \((y_1,y_2)\) 后

\[
La\mid y_1^2+y_2^2
\]

使第三坐标只有有限候选。

在 \(A_1\) 中也存在相同的逐纤维有限化。

但如果前缀参数

\[
m_2,\ a_2,\ b_2
\]

或 ghost

\[
y_1,y_2
\]

仍然无界，那么

\[
\bigcup_{\text{所有前缀}}
\text{有限候选集}
\]

仍可能是无限集合。

因此以下推理是无效的：

\[
\forall P,\quad
\#F(P)<\infty
\quad\Longrightarrow\quad
\bigcup_PF(P)
\text{ 有限}.
\]

真正需要的是某种 **prefix-uniform** 结论：

\[
\boxed{
\text{统一高度上界、统一矛盾、或保持原问题族的严格下降。}
}
\]

目前主定理仍开放，正是因为这最后一层还没有完全建立。

---

# 36. 当前严格证明状态

截至本文整理时，可以可靠写成以下状态。

## 36.1 已严格完成

1. exact lift 的十进制正权平均重写；
2. carrier 原理；
3. 正常位数区域排除；
4. 三异常分支穷尽；
5. 整数球面提升；
6. primitive recovery；
7. denominator prime graph 的主要全局结构；
8. 第三块公共尾商正规化；
9. 统一整数尾权 \(\kappa\)；
10. 统一二次式和平方判别式；
11. primitive tail quadratic；
12. \(10^\ell\mid\kappa^2(\kappa+2G)\)；
13. 三分支线性 denominator-tail cone；
14. 完整高斯共轭匹配的局部结构；
15. 高斯 flip 不保持十进制 coefficient plane；
16. \(A_2\) 相邻边界区
    \[
    (s_2,s_3)=(-1,1);
    \]
17. \(A_2\) deep-even 终端通道；
18. \(a_1=3\) 全局排除；
19. \(A_2\) 的 source split、Hensel 商、五进同步与 factor allocation；
20. \(A_2\) 的 prefix defect、odd inert excess 与 source 双 Hensel 系统；
21. \(A_2\) 的有限切片
    \[
    m_2\le10
    \]
    排除；
22. DD 的公共商正规化；
23. DD 的 surplus simplex；
24. DD 的 near-square gap；
25. DD 的
    \[
    d_3\le5S_{12};
    \]
26. DD 顶部 \(2/5\)-adic 双 resonance；
27. DD near-\(S\)-unit 化；
28. DD 极端 denominator 不对称；
29. DD 最大 denominator-tail 层排除；
30. DD 拼接行列式 gap 的精确赋值恒等式；
31. DD 双 resonance 终端尖角
    \[
    10S_{12}+11\le n_3\le11S_{12}+3
    \]
    的全排除；
32. DD 的五进正规形先给出中间上界
    \[
    n_3
    <
    \left(5+3\log_5 10\right)S_{12}
    +\frac32\log_5 10;
    \]
33. DD 中高层的奇偶锁 \(10\mid b_3\)、唯一五进正规形与超深五进单位抵消；
34. DD 中高层的二进非 resonance 锁 \(\Delta_2>0\) 与三条二进正规形；
35. DD 二进主导项锁
    \[
    v_2(\kappa)=v_2(G)+1
    \]
    及整个单五进 resonance 中高层的排除；
36. DD 当前全局相对界
    \[
    n_3\le9S_{12}+1;
    \]
37. DD 阈值以下的上层
    \[
    n_3\ge(5+2\log_5 10)S_{12}+\log_5 10
    \]
    被压成唯一五进 resonance 正规形或 \(\Delta_5>0\)；
38. \(A_1\) saturated 支的 denominator-only 尾长界；
39. \(A_1\) saturated 非十进制奇素数只能来自 \(G\) 且为 \(1\bmod4\)。

---

## 36.2 尚未完成

\[
\boxed{
A_2\text{-only 尚未全局关闭}.
}
\]

\[
\boxed{
DD 尚未全局关闭.
}
\]

\[
\boxed{
A_1\text{-only 尚未全局关闭.
}
\]

因此

\[
\boxed{
\text{主不存在性定理尚未完成证明}.
}
\]

---

# 37. 三个分支的剩余核心

## 37.1 \(A_2\)

真正开放的是

\[
\boxed{
m_2\ge11
}
\]

下 deep-even 终端系统的统一空性。

局部素数追逐已经基本耗尽，继续方向应集中在：

\[
\boxed{
\text{source 双 Hensel}
+
\text{十进制窄窗口}
}
\]

以及

\[
\boxed{
\text{Gaussian ellipse}
+
\text{真实 }2/5\text{-adic phase}.
}
\]

---

## 37.2 DD

原先的双 resonance 顶部

\[
10S_{12}+11
\le n_3\le
11S_{12}+3
\]

已经排除；其下方原本可能只发生五进 resonance 的整个中高层

\[
d_3=\max(s_1,s_2,d_3),
\qquad
n_3\ge9S_{12}+2
\]

也已由二进主导项与球面差分排除。当前严格上界是

\[
\boxed{
n_3\le9S_{12}+1.
}
\]

但 DD 仍未全局关闭：\(d_3\) 非 dominant 扇区与五进 resonance 阈值下的 dominant 扇区仍可随 \(S_{12}\) 无界增长。后一区域的上层

\[
n_3\ge
(5+2\log_5 10)S_{12}
+\log_5 10
\]

已进一步只剩唯一五进 resonance 正规形或 \(\Delta_5>0\)。

下一个精确目标是：在 \(n_3\le9S_{12}+1\) 内分别处理 \(p=5\) 的 resonance 及两条非 resonance 恒等式，并寻找仍可送入

\[
(\mathcal R-r_3)(\mathcal R+r_3)
=
\frac{\mathcal N_{12}}{G^2}
\]

的唯一主导项；目标仍是绝对高度界或直接矛盾。

---

## 37.3 \(A_1\)

有效尾长已经受

\[
\ell\le3(m_1+m_2)+1
\]

控制。

真正最危险的是 saturated \(L=1\) 中可能继续无界的 decimal shift

\[
\boxed{
g.
}
\]

Gaussian descent 在这里完全失效。

需要寻找一个新的 coefficient-plane invariant 或直接的 decimal-shift 高度界。

---

# 38. 推荐的全局攻关顺序

## 第一优先级：关闭五进 resonance 阈值以下的 DD

第 27 节已经关闭双 resonance 顶部及其下方整个单五进 resonance 带。下一步只需面对

\[
n_3\le9S_{12}+1
\]

内的两个区域：非 \(d_3\)-dominant 扇区，以及尚未达到五进 resonance 强制阈值的 \(d_3\)-dominant 扇区；后一区域仍可能自发发生 resonance。

建议把全部力量放在

\[
\mathcal N_{12}
=
X_0^2+\varepsilon^2
\]

的 near-square 结构与

\[
\kappa(
\kappa K_{C,D}
-
2GQ^2\mathcal N_{12}
)
=
W^2
\]

之间。

具体应尝试：

1. 对 \(p=5\) 的 resonance、\(\Delta_5>0\) 与 \(\Delta_5<0\) 三种状态分别做 \(\kappa\) 相对 \(G\) 的超距分类；
2. 把每一类中 \(\mathcal R-r_3\) 与 \(2r_3\) 的赋值差写成显式线性式，寻找像第 27.5 节那样唯一主导的球面因子；
3. 在接近 \(9S_{12}+1\) 的上层继续利用短 numerator block，给出
   \[
   |\varepsilon|/X_0
   \]
   的指数级上界；
4. 把判别核围绕 \(\mathcal N_{12}=X_0^2\) 展开，并寻找最近的候选整数平方中心 \(W_0^2\)；
5. 证明真实值与 \(W_0^2\) 的非零偏差小于相邻平方间距；
6. 如果最终只得到
   \[
   S_{12}\le S_0,
   \]
   则用有限证书关闭剩余层。

near-square 路线仍可用来给 \(E\) 或 \(F_-\) 提供绝对值上界，但不应再以已排除的 resonance 带为目标。新的主线是用

\[
\frac{\mu}{\nu}
=
\frac{E\kappa^2}{10^{m_3}Q^2(\kappa+G)}
\]

控制非 resonance 时 \(F_-\) 与 \(F_+\) 的赋值差，并每次与

\[
\kappa^3(\kappa+2G)<10^{8S_{12}+4}
\]

的统一高度上界重新比较。

---

## 第二优先级：\(A_2\) 的 resultant / Hensel 接触

对

\[
\Phi(x,z)
=
(99x-4)z-2x-4
\]

和

\[
\Psi_{a_1}(y,z)
=
400a_1(z+1)^2
-y(99z-2)^2
\]

计算

\[
\operatorname{Res}_z(\Phi,\Psi_{a_1}).
\]

由于 \(\Phi\) 对 \(z\) 线性，可以直接代入

\[
z=\frac{2x+4}{99x-4}
\]

得到显式的

\[
\Theta_{a_1}(x,y).
\]

合法 source odd excess 要求某个 inert prime 同时满足

\[
p^{2h}\mid\Phi,
\qquad
p^h\mid\Psi_{a_1}.
\]

预期可转化为

\[
p^h
\mid
\Theta_{a_1}(x,y).
\]

下一步应研究：

- \(\Theta_{a_1}\) 的因子分解；
- repeated-root/discriminant；
- 与固定 core \(a_1\) 的 gcd；
- 是否只有有限小素数允许高阶 Hensel 接触；
- \(p^{2h}\) 与十进制区间长度之间的 rational reconstruction 矛盾。

如果能证明所有高阶接触都来自固定有限素数集，\(A_2\) 就可能进一步压成有限状态。

---

## 第三优先级：\(A_1\) saturated 的 coefficient-plane invariant

这里不应继续尝试 Gaussian flip。

更合理的方向是找一个直接依赖

\[
10^g
\]

与前两块系数的整数对象，例如：

- determinant；
- cross-ratio 型有理不变量；
- 二次型 discriminant；
- 两个线性平面之间的格指数；
- 对 \(2,5\)-进高度同时敏感的 resultant。

目标是证明当 \(g\) 变大时，该对象一方面必须被 \(10^g\) 深度整除，另一方面绝对值增长速度又小于 \(10^g\)，从而出现

\[
0<|X|<10^g
\quad\text{且}\quad
10^g\mid X
\]

的直接矛盾。

这会比在 saturated 支中继续寻找“下降”自然得多。

---

# 39. 最终主定理需要的最小新成果集合

目前不需要重新发明前面所有局部代数。

一个完整证明最少需要以下三类新结果。

### Lemma DD — 中低层的统一高度界

双 resonance 顶部已排除。剩余需证明的是：对单 resonance 和非 resonance 区域建立

\[
S_{12}\le S_0,
\]

或者直接得到与 gap-valuation 恒等式不相容的赋值/高度矛盾。

### Lemma A2 — deep-even uniform obstruction

证明

\[
m_2\ge11
\]

时 source Hensel / Gaussian ellipse / decimal window 无法兼容，或者得到统一 \(m_2\) 上界。

### Lemma A1 — saturated decimal-shift bound

证明 saturated \(L=1\) 中

\[
g\le g_0(m_1,m_2)
\]

并最终与现有 tail bound 合并成全局有限性，或者直接产生矛盾。

若三条都得到统一有限上界，最后的有限区域可以由严格整数证书完全关闭。

---

# 40. 统一符号表

本文有意消除了旧工作稿中同一字母被多次复用的问题。

| 统一符号 | 含义 |
|---|---|
| \(a_i,b_i\) | 第 \(i\) 个既约有理数的分子、分母 |
| \(n_i,m_i\) | \(a_i,b_i\) 的十进制位数 |
| \(s_i=n_i-m_i\) | 第 \(i\) 块位数差 |
| \(\alpha,\beta\) | 三分子、三分母的十进制拼接 |
| \(\mathcal R\) | \(\sqrt{r_1^2+r_2^2+r_3^2}\) |
| \(B_i,w_i,\Lambda_i\) | 拼接位置权重、正权、carrier 放大因子 |
| \(q\) | \(\operatorname{lcm}(b_1,b_2,b_3)\) |
| \(y_i,H\) | 整数球面坐标与半径 |
| \(Q\) | \(b_1 10^{m_2}+b_2\) |
| \(G\) | \(b_1b_2\) |
| \(\mathcal N_{12}\) | \((a_1b_2)^2+(a_2b_1)^2\) |
| \(C,D\) | 三分支统一 coefficient pair |
| \(\ell\) | 有效第三尾长 |
| \(\delta_3\) | \(\gcd(10^\ell,b_3)\) |
| \(L\) | \(10^\ell/\delta_3\) |
| \(\tau\) | \(b_3/\delta_3\) |
| \(z_3\) | \(a_3/\delta_3\) |
| \(\kappa\) | 统一整数尾权 |
| \(K_{C,D}\) | 统一判别核 |
| \(W\) | 统一判别平方根 |
| \(G_0\) | primitive recovery gcd |
| \(S_{12}\) | \(m_1+m_2\)，前两分母位数尺度 |
| \(\mathcal S_{12}\) | \(y_1^2+y_2^2\)，前两 ghost 平方和 |
| \(d_3\) | DD 中 \(s_3\) |
| \(k_{12}\) | DD/A1 中 \(s_2+s_3\) |
| \(g\) | \(A_1\) 中 \(-s_3\) |
| \(A_{12}\) | \(a_1 10^{n_2}+a_2\) |
| \(\sigma_5\) | \(A_2\) deep-even 中 \(v_5(u)\) |
| \(E_5\) | \(\lambda+\sigma_5\) |
| \(Q_0,\mathcal N_0\) | \(A_2\) 去二后的前缀量 |
| \(c_Q,c_u,\rho\) | \(A_2\) source split |
| \(\Delta_{\rm pref}\) | \(A_2\) prefix defect |
| \(\Phi,\Psi_{a_1}\) | \(A_2\) source 双 Hensel 多项式 |

---

# 41. 旧记号到统一记号的主要对应

为了阅读此前工作稿，下面给出最容易冲突的旧记号对应。正文不再使用这些歧义写法。

| 旧用法 | 本文统一写法 |
|---|---|
| \(M=m_2,\ m=m_3\) | 直接使用 \(m_2,m_3\) |
| \(S=y_1^2+y_2^2\) | \(\mathcal S_{12}\) |
| \(S=m_1+m_2\) | \(S_{12}\) |
| DD 中 \(d=s_3\) | \(d_3\) |
| 多处 \(D\) 表 gcd / divisor / coefficient | gcd 用 \(\delta_3,d_*\)，统一系数保留 \(D\) |
| 第三分子本原根 \(z\) | \(z_3\) |
| \(A_2\) 判别平方根 \(z\) | \(Z\) |
| source normalized \(z\) | 只在 Hensel 小节局部使用 \(z\) |
| \(q\) 同时表示 lcm 与 source quotient | 全局 lcm 保留 \(q\)，source quotient 改为 \(q_Q\) |
| \(G\) 同时表示 gap / \(b_1b_2\) | 全局 \(G=b_1b_2\)，gap 改用 \(\mathcal G\) |
| \(N\) 的多个二平方范数 | 全局 \(\mathcal N_{12}\)，A2 去二后 \(\mathcal N_0\) |
| A1 saturated 的尾长 \(n\) | \(\ell=m_3-g\) |
| \(s=v_5(u)\) | \(\sigma_5\) |
| \(E=\lambda+s\) | \(E_5=\lambda+\sigma_5\) |

---

# 42. 关键公式依赖图

可以把当前全部证明压缩成下面的逻辑网络：

\[
\boxed{
\text{exact lift}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{positive weighted average}
}
\]

\[
\Downarrow
\]

\[
\boxed{
A_2\ \cup\ DD\ \cup\ A_1
}
\]

同时

\[
\boxed{
\text{exact lift}
}
\]

\[
\Downarrow
\]

\[
\boxed{
y_1^2+y_2^2+y_3^2=H^2,
\quad
q\alpha=H\beta
}
\]

\[
\Downarrow
\]

\[
\boxed{
\gcd(q,y_i)=q/b_i
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{denominator prime graph}
}
\]

三个分支分别做第三尾正规化：

\[
\boxed{
(\delta_3,L,\tau)
}
\]

\[
\Downarrow
\]

\[
\boxed{
QG<\kappa\le10QG
}
\]

\[
\Downarrow
\]

\[
\boxed{
\kappa(
\kappa K_{C,D}
-2GD^2\mathcal N_{12}
)
=W^2
}
\]

以及

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G)
}
\]

\[
\Downarrow
\]

\[
\boxed{
\ell\le6S_{12}+3
}
\]

随后：

\[
A_2
\Longrightarrow
\boxed{
\text{deep-even}
+
\text{source split}
+
\text{odd inert excess}
+
\text{double Hensel}
}
\]

\[
DD
\Longrightarrow
\boxed{
\text{surplus simplex}
+
\text{near-square}
+
2/5\text{ resonance}
+
\text{near-}S\text{-unit}
}
\]

\[
A_1
\Longrightarrow
\boxed{
\text{thin annulus}
+
\text{slope lock}
+
\text{saturated tail bound}
}
\]

最终都汇入同一个尚未完全解决的问题：

\[
\boxed{
\text{如何对无界前缀得到 prefix-uniform contradiction?}
}
\]

---

# 43. 研究结论

这道题目前已经不再是“一个巨大的、无结构的十进制拼接丢番图方程”。

它已经被压缩成三个相当具体的终端问题。

\(A_2\) 的难点是：

\[
\boxed{
\text{高阶 source Hensel 接触能否与真实十进制窗口长期共存？}
}
\]

DD 的难点是：

\[
\boxed{
\text{所有强制五进 resonance 的高层消失后，
阈值以下的 resonance/non-resonance 锥能否仍随前缀高度无界增长？}
}
\]

\(A_1\) 的难点是：

\[
\boxed{
\text{在 Gaussian descent 完全失效的 saturated 平面中，
decimal shift }g\text{ 能否无界？}
}
\]

现阶段最值得优先攻击 DD。

其优先级来自这样一个事实：第 27 节已经首次把局部 resonance 数据转成了 prefix-uniform 的全局高度矛盾。原顶部的结构是

\[
\text{极端不对称}
+
\text{短 numerator block}
+
\text{near-square}
+
\text{双 Hensel resonance}
+
\text{near-}2,5\text{-smooth}.
\]

这个最顶层及其下方的单五进 resonance 带现已全部排除，并得到新的全局相对界

\[
n_3\le9S_{12}+1.
\]

但这仍然不是 DD 全局空性；接下来必须在五进 resonance 阈值以下，对自发 resonance 与两条 non-resonance 支分别建立同样的主导项或高度矛盾。这一 gap-valuation / dominant-term / height 思维也有可能被移植到 \(A_2\) 和 \(A_1\) 的剩余核中。

在那之前，严格的最终状态仍然是：

\[
\boxed{
\text{主不存在性命题高度受限、结构非常刚性，但尚未完成证明。}
}
\]
