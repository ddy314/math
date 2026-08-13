# 原问题与 carrier 几何

本文件对应原总稿 §§1–2，记录问题定义、统一符号、十进制拼接的正权平均表达，以及三个异常分支的穷尽。后续整数球面和尾部正规化见 [global-framework.md](global-framework.md)。

> 迁移说明：以下正文由原始总稿机械拆分，公式和证明状态不作数学改写。
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

