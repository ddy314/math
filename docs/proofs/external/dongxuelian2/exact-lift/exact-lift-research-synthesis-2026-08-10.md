# 三块十进制拼接 Exact Lift 问题：研究综述、统一符号与当前证明路线

> **整理日期：2026-08-10**  
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
7. 对 double-deficit 分支，已经把原本高维的无界参数空间压缩到一个极端不对称、同时发生 \(2\)-进与 \(5\)-进 resonance、并且 \(\kappa,\kappa+2G\) 接近 \(2,5\)-smooth 的尖角；
8. 对 \(A_1\)-only 的 saturated 支 \(L=1\)，已经证明自由尾长受 denominator-only 上界控制，但 decimal shift \(g\) 仍然可能无界。

当前最有价值的总策略已经从“继续逐素数追同余”转向“利用极端十进制不对称产生 near-square，再与整数判别平方的离散间距冲突”。优先目标是关闭 double-deficit 的最后尖角；随后回到 \(A_2\) 的双 Hensel / ellipse 系统；最后为 \(A_1\) saturated 支寻找保持十进制 coefficient plane 的新不变量。

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
\boxed{y_i=\frac{a_iq}{b_i}.}
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
\boxed{y_1^2+y_2^2+y_3^2=H^2,}
\]

并且

\[
\boxed{q\alpha=H\beta.}
\]

这是原问题最关键的算术提升：十进制拼接问题被嵌入“整数球面 + 整数线性平面”的交。

需要强调：\(q=\operatorname{lcm}(b_i)\) 本身并不能自动保证四元组 \((y_1,y_2,y_3,H)\) 整体本原。因此本文避免把它无条件称为“本原四元组”；真正无条件成立的是下面的逐坐标恢复恒等式。

对每个 \(i\)，

\[
\boxed{\gcd(q,y_i)=\frac{q}{b_i}.}
\]

逐素数看，若

\[
E=v_p(q),
\qquad e_i=v_p(b_i),
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
\boxed{Q=b_1 10^{m_2}+b_2,}
\]

\[
\boxed{G=b_1b_2,}
\]

以及前两块的二平方型

\[
\boxed{\mathcal N_{12}=(a_1b_2)^2+(a_2b_1)^2.}
\]

其中 \(Q\) 是前两分母的普通十进制拼接，\(G\) 是两个分母的乘积，\(\mathcal N_{12}\) 则是 \(G^2(r_1^2+r_2^2)\)。

对三个分支，还可引入统一的 coefficient pair \((C,D)\)：

\[
(C,D)=
\begin{cases}
\left(a_1 10^{m_2}+10a_2,\ Q\right),& A_2,\\[0.6em]
\left(10^{m_2+k_{12}}a_1+10^{d_3}a_2,\ Q\right),& DD,\\[0.6em]
\left(10^{g+k_{12}+m_2}a_1+a_2,\ 10^gQ\right),& A_1,
\end{cases}
\]

其中在 DD 中统一记 \(d_3=s_3>0, k_{12}=s_2+s_3>0\)，而在 \(A_1\) 中记 \(g=-s_3\ge0, k_{12}=s_2+s_3\ge1\)。

---

# 5. 第三块尾部的统一正规化

三个异常分支都存在一个“第三块十进制尾幂与第三分母公共部分”的正规化。

统一定义有效尾长

\[
\ell=\begin{cases}m_3,&A_2,\ DD,\\m_3-g,&A_1.\end{cases}
\]

再令

\[
\boxed{\delta_3=\gcd(10^\ell,b_3),}
\]

\[
\boxed{L=\frac{10^\ell}{\delta_3},\qquad\tau=\frac{b_3}{\delta_3}.}
\]

于是 \(\gcd(L,\tau)=1\)。第三分子的对应本原化记为

\[
\boxed{z_3=\frac{a_3}{\delta_3}.}
\]

该正规化的核心含义是：十进制尾部中强制出现的 \(2\)-、\(5\)-因子全部被剥出，剩余的 \(L\) 是真正参与高斯因子转移和平方判别的“尾商”。

对 \(A_2\) 与 DD，必有 \(L>1\)。对 \(A_1\)，只有一种特殊情形可能出现 \(L=1\)，即 decimal-saturated 支。这一支后来被证明是整个 \(A_1\) 中最特殊的难点。

---

# 6. 统一尾权 \(\kappa\)

三个分支中看似不同的第三块实参数，实际上都可以压入同一个整数 \(\kappa\)。统一结论为

\[
\boxed{QG<\kappa\le10QG.}
\]

对 \(A_2\) 和 DD，

\[
\boxed{\kappa=\frac{10^{m_3}QG}{b_3}=\frac{LQG}{\tau}\in\mathbf Z.}
\]

因而 \(\tau/L=QG/\kappa\)。对 \(A_1\) 则有相应的带 \(10^g\) 形式：

\[
\boxed{\kappa=\frac{10^gLQG}{\tau}\in\mathbf Z.}
\]

这个整数区间非常重要：第三块尾部虽然位数可以变长，但它的核心斜率只能由前两块尺度 \(QG\) 的一个固定十倍窗口控制。

---

# 7. 统一二次式、判别平方与 primitive recovery

令球面 gap 的统一有理参数满足

\[
G(\mathcal R-r_3)=\frac{\mu}{\nu},\qquad\gcd(\mu,\nu)=1.
\]

三个异常分支都可以化成

\[
\boxed{D(\kappa+2G)\mu^2-2G\kappa C\,\mu\nu+\kappa D\mathcal N_{12}\nu^2=0.}
\]

由本原性立刻得到

\[
\boxed{\nu\mid D(\kappa+2G),\qquad\mu\mid \kappa D\mathcal N_{12}.}
\]

定义统一判别核

\[
\boxed{K_{C,D}=G^2C^2-D^2\mathcal N_{12}.}
\]

则有理解存在的必要条件是

\[
\boxed{\kappa\left(\kappa K_{C,D}-2GD^2\mathcal N_{12}\right)=W^2}
\]

对某个整数 \(W\)。进一步定义

\[
G_0=\gcd(\mathcal N_{12}\nu^2-\mu^2,2G\mu\nu).
\]

第三块的 primitive recovery 可以写成

\[
\boxed{10^{m_3}QG_0=2\kappa\mu\nu}
\]

（在 \(A_1\) 中按有效尾长做相应替换）。一个后来得到的重要全局结论是

\[
\boxed{G_0\mid2G\mathcal N_{12}.}
\]

因此 \(G_0\) 不能作为新的无界素数储存池。

---

# 8. 三分支统一的 primitive tail quadratic

利用 \(10^\ell=\delta_3L,b_3=\delta_3\tau,a_3=\delta_3z_3\)，三个分支共同满足

\[
\boxed{-\kappa(\kappa+2G)z_3^2+2G^2LC\,z_3+\mathcal C_3=0,}
\]

其中

\[
\boxed{\mathcal C_3=G^2L^2C^2-\mathcal N_{12}(LD+\tau)^2.}
\]

由有理根定理得到

\[
\boxed{\delta_3\mid\kappa(\kappa+2G),\qquad a_3\mid\mathcal C_3.}
\]

又因为 \(L\mid\kappa\)，所以

\[
\boxed{10^\ell\mid\kappa^2(\kappa+2G).}
\]

这是目前最干净的三分支统一 denominator-tail certificate。若记 \(S_{12}=m_1+m_2\)，则得到粗但前缀一致的尾长锥

\[
\boxed{\ell\le6S_{12}+3.}
\]

即 \(m_3\le6S_{12}+3\) 对 \(A_2\)、DD 成立，而 \(A_1\) 有 \(m_3-g\le6S_{12}+3\)。

---

# 9. Primitive Vieta 对与第三分子的 prime flow

定义

\[
\boxed{\delta_3^\vee=\frac{\kappa(\kappa+2G)}{\delta_3},\qquad a_3^\vee=\frac{\mathcal C_3}{a_3}.}
\]

则二次式精确分解为

\[
\boxed{\kappa(\kappa+2G)X^2-2G^2LCX-\mathcal C_3=(\delta_3X-a_3)(\delta_3^\vee X+a_3^\vee).}
\]

因而

\[
\delta_3\delta_3^\vee=\kappa(\kappa+2G),\quad a_3a_3^\vee=\mathcal C_3,
\]

并有交叉差

\[
\boxed{a_3\delta_3^\vee-\delta_3a_3^\vee=2G^2LC.}
\]

若某个素数 \(p\nmid2GLC\) 且 \(p\mid a_3\)，则 \(p\nmid a_3^\vee,p\nmid\delta_3\)，并且

\[
\boxed{v_p(a_3)=v_p(\mathcal C_3).}
\]

同时有

\[
\boxed{\mathcal N_{12}\equiv\left(\frac{GLC}{LD+\tau}\right)^2\pmod{p^{v_p(a_3)}}.}
\]

因此第三分子的“自由素数”必须以完整 prime-power 深度满足一个 \(\mathbf Q(\sqrt{\mathcal N_{12}})\) 中的分裂条件。

---

# 10. Denominator prime graph

对任意素数 \(p\)，记 \(e_i=v_p(b_i),E=\max(e_1,e_2,e_3)\)。

若奇素数 \(p\neq2,5\) 的最大赋值只在一块出现，则另外两块的 \(p\)-进指数相等。若最大值恰由两块取得，pair-max 只能由 \(p\equiv1\pmod4\) 的奇素数承担。

对 \(p=2\)，整数球面模 \(4\) 给出 \(H\) 为奇数，\(y_1,y_2,y_3\) 中恰有一个奇数，由 primitive recovery 推出

\[
\boxed{\max_i v_2(b_i)\text{ 必须唯一取得}.}
\]

因此 denominator prime graph 的 skeleton 为

\[
\boxed{\begin{array}{c|c}p=2&\text{最大指数必须唯一}\\p\equiv3\pmod4,\ p\neq5&\text{不能 pair-max}\\p\equiv1\pmod4&\text{允许 pair-max}\end{array}}
\]

这组结构对三个异常分支同时有效。

---

# 11. 高斯整数结构：成功之处与边界

整数球面给出

\[
y_1^2+y_2^2=(H-y_3)(H+y_3).
\]

在 \(\mathbf Z[i]\) 中分析共轭因子后，可以建立完整的 conjugate-factor matching；潜在失配只可能出现在 \(p\mid\gcd(E_0,a)\) 的局部容量不足位置。进一步得到惰性异常素数的全局定位：在 \(A_2\) 相邻边界区中，\(p\equiv3\pmod4\) 的异常核为空；在 DD 与 \(A_1\) 中，若这种素数真正进入异常核，则必须有 \(e_1=e_2=e<e_3=E\)，并且 \(p^E\mid A+B\)，同时 \(v_p(a)=2(E-e)\)。

最重要的负面结论是

\[
\boxed{\text{高斯 flip 不保持原十进制 coefficient plane}.}
\]

翻面会把球面因子从约 \((La,H+y_3)\) 转移为 \((a,L(H+y_3))\)，但十进制平面关系出现额外因子 \(L\)，离开原 exact-lift 系数族。因此 Gaussian descent 是有效的局部因子归约，却目前无法作为可迭代的全局下降。

---

# 12. \(A_2\)-only 分支

## 12.1 相邻边界区已严格固定

\(A_2\)-only 满足 \(s_3>0,s_2+s_3\le0\)。令 \(k=s_3\ge1\)。carrier 条件结合三块十进制窗口可严格推出

\[
\boxed{s_3=1,\qquad s_2=-1.}
\]

因此第二分子比分母少一位，第三分子比分母多一位。

## 12.2 第一块 core 压缩

真正无界的危险通道只剩

\[
\boxed{b_1=2.}
\]

第一分子最终只剩

\[
\boxed{a_1\in\{5,7,9,11,13\}.}
\]

其中 \(a_1=3\) 已经通过实数函数 \(F_3(x,y)<1\) 在整个合法区域全局排除。

## 12.3 Deep-even 终端通道

危险通道具有

\[
\boxed{b_2=2^{m_2+m_3+t}u,\qquad b_3=2^{m_2+m_3+1}b_{3,0},}
\]

其中 \(u,b_{3,0}\) 均为奇数且 \(t\ge3\)。前两分母拼接

\[
Q=2^{m_2+1}Q_0,
\qquad Q_0=5^{m_2}+2^{m_3+t-1}u.
\]

第三块正规化尾商被强迫为纯五次幂

\[
\boxed{L=5^\lambda,\qquad5^\lambda>2^{m_2+1}.}
\]

进一步去二后写 \(b'=2^{m_2+1}c\)，其中 \(c\) 奇且位于十倍窗口。

## 12.4 二进 Hensel 锁

\[
\boxed{t=1+v_2(5^{m_2+\lambda}+c).}
\]

由 \(t\ge3\) 得 \(c\equiv3\pmod4\)，从而 \(c\ge3\)，并加强为

\[
\boxed{5^\lambda>3\cdot2^{m_2+1}.}
\]

## 12.5 source split

存在唯一互素分解

\[
\boxed{c=c_Qc_u,}
\]

并写成

\[
Q_0=5^{\sigma_5}c_Qq_Q,
\qquad u=5^{\sigma_5}c_u\rho,
\]

其中 \(c_u\) 的素因子均为 \(1\bmod4\)，故 \(c_u\equiv1\pmod4\)，从 \(c\equiv3\pmod4\) 得

\[
\boxed{c_Q\equiv3\pmod4.}
\]

## 12.6 五进统一参数

定义 \(E_5=\lambda+\sigma_5\)。合法候选只能处于三条五进通道：

- \(\sigma_5>0\)：\(m_3=\tfrac32E_5\)，且 \(E_5\) 偶；
- reflection：\(\sigma_5=0,\lambda<m_3\le\tfrac32\lambda\)；
- balance：\(\sigma_5=0,\lambda=m_3\)。

因此 \(m_3,\lambda,v_5(u)\) 不能独立增长。

## 12.7 Hensel 商与 \(\rho\) 恢复

定义 \(f=5^{E_5}q_Q+2c_u\)，存在奇整数 \(\omega,\theta\) 使

\[
5^{E_5}q_Q+c_u=2^{t-1}\rho\omega,
\]
\[
5^{m_2+\lambda}+c=2^{t-1}\rho\theta,
\]

且 \(\gcd(\omega,\theta)=1\)。于是

\[
\boxed{\rho=\frac{\gcd(5^{E_5}q_Q+c_u,5^{m_2+\lambda}+c)}{2^{t-1}}.}
\]

所以 \(\rho\) 也失去独立自由度。

## 12.8 去二平方判别与 factor allocation

定义去二范数 \(\mathcal N_0=C_0^2+a_2^2\)，判别平方可写成

\[
\boxed{5^\lambda(5^\lambda K_0-2cQ_0\mathcal N_0)=Z^2.}
\]

等价于差平方系统

\[
\boxed{\mathcal A^2-Z^2=5^\lambda Q_0\mathcal N_0(5^\lambda Q_0+2c).}
\]

从而差平方的完整 prime-power 分配只能单边进入两因子，特别是 \(c_Q\) 存在唯一互素分解 \(c_Q=c_-c_+\) 使相应部分以平方形态分配到两侧。

## 12.9 十进制实窗口与 Gaussian rectangle

对每个 core \(a_1\) 已有严格的 \(x=b_2/10^{m_2}\)、\(y=a_2/10^{m_2-1}\)、\(w=b_3/10^{m_3}\) 窄窗口。整体形态是：第二分子接近上端、第二分母接近下端、第三分母接近上端、第三分子接近下端。

定义 source-side Gaussian rectangle 的正交误差 \(L_0\) 与 \(M_0\)，有

\[
\boxed{L_0+iM_0=(U_5+10iH_s)(a_2+iC_0),}
\]

并引入纯前缀整数

\[
\boxed{\Delta_{\rm pref}=A_0^2+C_0^2-P^2,}
\]

满足 \(\Delta_{\rm pref}\equiv7\pmod8\)。denominator-side 对第二层 surplus 的接触被 \(\Delta_{\rm pref}\) 控制。

## 12.10 odd inert excess 与双 Hensel

第二层必出现某个 \(p\equiv3\pmod4\) 的正奇 extra valuation。其来源分 denominator-prefix、source、spontaneous angle 三类。对 source inert prime，定义

\[
\Phi(x,z)=(99x-4)z-2x-4,
\]

\[
\Psi_{a_1}(y,z)=400a_1(z+1)^2-y(99z-2)^2.
\]

若 \(p^{2h}\Vert\sigma\)，则必须满足

\[
\boxed{v_p(\Phi)=2h,\qquad v_p(\Psi_{a_1})\ge h.}
\]

这是一个 \(2h:h\) 的双 Hensel 接触系统，同时受窄十进制窗口约束。

## 12.11 有限证书与开放核

严格有限计算已关闭 \(m_2\le10\) 的 deep-even 终端切片。更高层诊断显示很稀疏，但不能替代无界证明。当前真正任务是

\[
\boxed{m_2\ge11\Longrightarrow\text{终端系统无解}.}
\]

最值得保留的方法是 source linear Hensel + decimal rigidity，以及 Gaussian ellipse + 真实 \(2/5\)-adic phase。

---

# 17. Double-deficit 分支

DD 令 \(d_3=s_3>0,k_{12}=s_2+s_3>0\)，定义球面 gap \(e=H-y_3>0\) 与 ghost 平方和 \(\mathcal S_{12}=y_1^2+y_2^2\)。exact balance 可化为

\[
T\mathcal G=b_3e.
\]

正规化后存在唯一正整数 \(a\) 使

\[
\boxed{e=La,\qquad\mathcal G=\tau a,\qquad La\mid\mathcal S_{12}.}
\]

因此固定 ghost \((y_1,y_2)\) 与正规化参数后，第三坐标只可能来自 \(\mathcal S_{12}\) 的有限除数，真正无界性来自前两 ghost。

---

# 18. DD 判别平方与斜率锁

恢复方程可整理成 \(LJ=W^2\)，实际根进一步满足 \(W=L\Xi,J=L\Xi^2\)。同时

\[
\boxed{\frac1{10}\le\frac\tau L<1.}
\]

说明 DD 尾 gap 与尾分母始终处于固定十倍窗口。

---

# 19. DD surplus simplex

定义 \(S_{12}=m_1+m_2\)。尺度比较给出

\[
\boxed{s_1+s_2+d_3-\max(s_1,s_2,d_3)\le2.}
\]

因此 DD 被切成三个薄扇区。两个非 \(d_3\)-dominant 扇区都满足

\[
\boxed{n_3\le7S_{12}+4.}
\]

所以当 \(n_3>7S_{12}+4\) 时必须进入 \(d_3=\max(s_1,s_2,d_3)\) 的第三分子 surplus 主导扇区。

---

# 20. DD near-square 与 squarefree gap

判别平方可写成

\[
\boxed{Y^2=X^2-\mathcal N_{12}10^{m_3}Q(10^{m_3}Q+2b_3),}
\]

其中 \(X=GA_{12}10^{n_3}\)。整数平方间距给出粗上界，进一步利用 \(\kappa\) 的平方部分加强为

\[
\boxed{d_3\le3S_{12}+|s_1-s_2|+2.}
\]

在 \(d_3\)-dominant 扇区中

\[
\boxed{d_3\le5S_{12}.}
\]

结合 denominator-tail cone 得

\[
\boxed{n_3\le11S_{12}+3.}
\]

---

# 22. DD 的 \(2\)-进与 \(5\)-进双 resonance

near-square 两正因子 \(F_-,F_+\) 的和为 \(2GA_{12}10^{n_3}\)。若两因子的某个 \(p\)-进赋值不同，则和的赋值只能是较小者。因此足够大的 \(n_3\) 必须发生 resonance：

\[
\boxed{f_p+2r_p=k_p+n_p+2s_p.}
\]

已得到

\[
\boxed{d_3=\max,\ n_3\ge9S_{12}+2\Longrightarrow5\text{-adic resonance},}
\]

\[
\boxed{d_3=\max,\ n_3\ge10S_{12}+11\Longrightarrow2\text{-adic resonance}.}
\]

所以顶部区域 \(n_3\ge10S_{12}+11\) 同时发生 2/5 resonance，并留下深 Hensel 相位。

---

# 23. DD near-\(S\)-unit 化

顶部区域中定义

\[
\boxed{\mathscr T=\frac{\kappa^2(\kappa+2G)}{10^{m_3}}\in\mathbf Z_{>0}.}
\]

统一尾权区间给出

\[
\boxed{1\le\mathscr T<10^{S_{12}-7}.}
\]

因此 \(\kappa\) 与 \(\kappa+2G\) 去掉 \(2,5\) 后的奇部分都非常小，即二者同时接近 \(2,5\)-smooth。

---

# 24. DD 极端不对称

平方部分上下界夹逼给出

\[
\boxed{n_3<8.533128S_{12}+|s_1-s_2|+6.173325.}
\]

若仍处于顶部 \(n_3\ge10S_{12}+11\)，则

\[
\boxed{|s_1-s_2|>1.466872S_{12}+4.826675,}
\]

并进一步

\[
\boxed{|m_1-m_2|>0.466872S_{12}+4.826675.}
\]

所以一个前两分母块占总位数约 73.3% 以上，另一个低于约 26.7%；相应短 numerator block 也有显式上界。

---

# 25. DD 最大 denominator-tail 层已排除

若 \(m_3=6S_{12}+3\)，则 \(\mathscr T=1\)，迫使 \(\kappa,\kappa+2G\) 仅含 \(2,5\) 素因子。利用有理 \(2,5\)-单位距离 1 的最小间距与尾权区间可得矛盾（\(S_{12}\ge5\)）。因此

\[
\boxed{m_3\le6S_{12}+2.}
\]

---

# 26. DD 当前终端尖角

真正还可能逃向无穷的 DD 候选必须处在

\[
\boxed{10S_{12}+11\le n_3\le11S_{12}+3,}
\]

并同时满足 \(d_3=\max\)、\(d_3\le5S_{12}\)、\(m_3\le6S_{12}+2\)、2/5 双 resonance，以及上述极端不对称。

---

# 27. DD 最有希望的机制：near-square + integer spacing

顶部不对称意味着

\[
\mathcal N_{12}=X_0^2+\varepsilon^2,\qquad|\varepsilon|\ll X_0.
\]

应把它直接代入统一判别平方，围绕某个整数平方中心展开，争取证明真实偏差非零且小于相邻平方间距，从而直接矛盾或得到前缀统一上界 \(S_{12}\le S_0\)。这是当前优先级最高路线。

---

# 28. \(A_1\)-only 分支

\(A_1\) 令 \(g=-s_3\ge0,k_{12}=s_2+s_3\ge1\)，有效尾长 \(\ell=m_3-g\)。第三块正规化同样给出 \(U=La,La\mid\mathcal S_{12}\)。

## 28.1 薄环约束

\[
\boxed{10^{k_{12}}y_1-\sqrt{(10^{2k_{12}}-1)y_1^2-y_2^2}<La<\sqrt{\mathcal S_{12}}.}
\]

## 28.2 尾商斜率锁

\[
\boxed{10^{g-1}\le\frac\tau L<10^g.}
\]

---

# 29. \(A_1\) saturated 支 \(L=1\)

真正特殊的是 \(L=1\)。严格检查表明此时 Gaussian flip 只是 projective identity，约掉整体尺度后回到原对象，没有严格下降，因此必须寻找独立机制。

---

# 30. \(A_1\) saturated denominator-only 尾长界

整个 saturated 支有

\[
\boxed{\ell\le\left\lfloor\log_5((10Q+2)G)\right\rfloor\le3(m_1+m_2)+1.}
\]

因此有效第三尾长受前两分母位数线性控制，真正还可能独立无界的量主要是 decimal shift \(g\)。

---

# 31. \(A_1\) saturated 奇素数约束

令 \(d_*=\gcd(\tau,10^gQ),h=\tau/d_*\)。可证明

\[
\boxed{\gcd(U,h)=1,\qquad h\mid G,}
\]

且 \(h\) 的所有奇素因子都满足 \(p\equiv1\pmod4\)，更强地

\[
\boxed{h\mid\frac{b_1b_2}{\gcd(b_1,b_2)^2}.}
\]

所以 saturated 第三分母中所有非十进制“新奇素数”必须来自前两分母的不共享部分，而且只能是 \(1\bmod4\) 素数。

---

# 32. 早期“完整证明”中撤回的步骤

已经明确撤回且不能再作为证明依据的包括：把完全共享分母分解直接当成该分支无解；用有限证书替代无界下降；在 DD 中把素数同时进入 gap 与二平方和误当成矛盾；在 A1 中用未量化的“两 gap 尺度不相容”充当 terminal contradiction。

---

# 33. 被严格判死或降级的证明路线

以下路线已经证明不能承担全局终止：

- \(A_2\to A_1\) Vieta jumping：companion root 为负，反射正根不保持 coefficient plane；
- 反复 Gaussian flip：\(L>1\) 离开原族，\(L=1\) 退化为 projective identity；
- source-only Legendre/Jacobi 全局乘积：退化为 \(1=1\)；
- generic 二次剩余追逐：多数条件在已有 Gaussian norm/source split 下自动满足；
- “模数大于区间”：只给 at most one，不给 zero；
- 普通 class group/genus/Hasse norm：没有直接抓住 decimal coefficient plane；
- scalar descent：两步只回到标量倍数；
- 错误 odd-inert 推断：加法赋值抵消使“odd excess \(\Rightarrow p\mid a_1\)”无效。

真正保留的是 odd inert excess 三分法与 source 双 Hensel 接触。

---

# 34. 有限计算的正确角色

有限计算只在三种场景使用：验证已有严格上界的有限切片；诊断无界空间稀疏程度；为最终有限余项提供证书。核心原则是

\[
\boxed{\text{无限族必须先被理论上统一压成有限族}.}
\]

---

# 35. 固定前缀有限与全局空的门槛

逐前缀/逐 ghost 的有限化不能推出全局有限或全局空。真正需要的是 prefix-uniform 高度上界、统一矛盾，或保持原问题族的严格下降。这是主定理仍开放的根本原因。

---

# 36. 当前严格证明状态

已严格完成的核心包括：weighted-average/carrier；三异常分支；整数球面与 primitive recovery；denominator prime graph；尾正规化、\(\kappa\)、统一二次式、判别平方、primitive tail quadratic、tail cone；高斯局部结构与 flip 边界；A2 相邻边界、deep-even、source split、Hensel、五进同步、factor allocation、prefix defect、odd inert excess、双 Hensel、\(m_2\le10\) finite closure；DD 公共商、surplus simplex、near-square、\(d_3\le5S_{12}\)、双 resonance、near-S-unit、极端不对称、最大 tail 层排除；A1 saturated tail bound 与奇素数锁。

尚未全局关闭：A2-only、DD、A1-only，因此主不存在性定理仍未完成。

---

# 37. 三个分支的剩余核心

## A2
\[
\boxed{m_2\ge11}
\]
下 deep-even 终端系统的统一空性。重点是 source 双 Hensel + 十进制窄窗口，以及 Gaussian ellipse + 真实 2/5-adic phase。

## DD
\[
\boxed{10S_{12}+11\le n_3\le11S_{12}+3}
\]
的顶部尖角，同时具备极端不对称、双 resonance、near-S-unit。它最接近“一个核心引理即可关闭无界部分”。

## A1
有效尾长受 \(\ell\le3(m_1+m_2)+1\) 控制，最危险的是 saturated \(L=1\) 中可能无界的 decimal shift \(g\)。需要新的 coefficient-plane invariant 或直接高度界。

---

# 38. 推荐攻关顺序

1. **DD 最后尖角**：利用 near-square 与 integer discriminant square 的离散间距，并用 2/5 resonance 排除偏差恰零；
2. **A2 resultant / Hensel**：研究 \(\operatorname{Res}_z(\Phi,\Psi_{a_1})\) 或代入线性根，寻找固定有限素数/高阶接触障碍；
3. **A1 saturated coefficient-plane invariant**：寻找被 \(10^g\) 深度整除但绝对值增长小于 \(10^g\) 的非零整数对象，制造直接矛盾。

---

# 39. 最小新成果集合

完整证明至少还需要三类新结果：DD 极端尖角排除或统一 \(S_{12}\) 上界；A2 deep-even uniform obstruction 或统一 \(m_2\) 上界；A1 saturated decimal-shift bound 或直接矛盾。若都得到统一有限上界，最后有限区域可由严格整数证书关闭。

---

# 40. 统一符号摘要

全局使用 \(a_i,b_i,n_i,m_i,s_i,\alpha,\beta,\mathcal R,q,y_i,H,Q,G,\mathcal N_{12},C,D,\ell,\delta_3,L,\tau,z_3,\kappa,K_{C,D},W,G_0,S_{12},\mathcal S_{12},d_3,k_{12},g,A_{12}\)。A2 局部使用 \(\sigma_5,E_5,Q_0,\mathcal N_0,c_Q,c_u,\rho,\Delta_{\rm pref},\Phi,\Psi_{a_1}\)。

---

# 41. 旧记号兼容原则

旧稿中 \(M,m,S,D,z,q,G,N,s,E\) 多次复用。整合时应优先采用本文统一记号：分母位数直接用 \(m_2,m_3\)，\(S_{12}=m_1+m_2\)，\(\mathcal S_{12}=y_1^2+y_2^2\)，全局 lcm 用 \(q\)，前两分母积用 \(G\)，全局二平方型用 \(\mathcal N_{12}\)，A2 五进量用 \(\sigma_5,E_5\)。

---

# 42. 依赖图

exact lift 一方面经 positive weighted average 进入 A2/DD/A1 三 chamber；另一方面经 integer sphere + exact recovery 进入 denominator prime graph。三 chamber 统一经过 \((\delta_3,L,\tau)\)、\(QG<\kappa\le10QG\)、统一 discriminant square 与 \(10^\ell\mid\kappa^2(\kappa+2G)\)。随后 A2 进入 deep-even/source split/double-Hensel；DD 进入 surplus/near-square/resonance/near-S-unit；A1 进入 thin-annulus/slope-lock/saturated-tail-bound。最终都汇入 prefix-uniform contradiction 问题。

---

# 43. 研究结论

当前问题已经从一个无结构的十进制拼接丢番图方程压缩为三个具体终端问题。A2 的难点是高阶 source Hensel 接触能否与真实十进制窗口长期共存；DD 的难点是极端不对称产生的 near-square 能否仍满足统一整数判别平方；A1 的难点是在 Gaussian descent 完全失效的 saturated 平面中 decimal shift \(g\) 能否无界。

现阶段最值得优先攻击 DD，因为它已同时具备极端不对称、短 numerator block、near-square、双 Hensel resonance 和 near-2,5-smooth，这种形状最有希望通过整数平方的离散间距产生真正的全局矛盾。

严格最终状态仍然是

\[
\boxed{\text{主不存在性命题高度受限、结构非常刚性，但尚未完成证明}.}
\]
