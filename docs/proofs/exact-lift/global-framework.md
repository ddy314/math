# 全局统一框架

本文件对应原总稿 §§3–11，记录整数球面提升、primitive recovery、统一前两块对象、第三块尾部正规化、统一判别式、primitive tail quadratic、denominator prime graph，以及高斯整数结构的边界。

> 迁移说明：以下正文由原始总稿机械拆分，公式和证明状态不作数学改写。
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

