# A1 top-layer boundary closure — 2026-08-16

本文继续 `a1-top-layer-decimal-normal-form-2026-08-16.md`，攻击最高层

\[
s_1=g+2
\]

的两个最外整数边界

\[
m_1=2k,
\qquad
n_2=2k.
\]

核心结果：

\[
\boxed{m_1=n_2=2k\text{ 为空},}
\]

并且任意单边取等都只能发生在 `g=0` 的唯一 `10^{2k}-1` 常数偏移族。

本文结论均为 **已严格完成**。

---

## 1. 复用的 contact 估计

沿用最高层记号

\[
a=10^{-2k},
\qquad
A_0=10^kr_1,
\qquad
t=\frac{r_2}{A_0},
\qquad
z=\frac{r_3}{A_0},
\]

\[
\lambda=\frac{b_2}{Q},
\qquad
u=\frac{P}{A_0}
=(1-\lambda)+\lambda10^{-g}t.
\]

prefix defect 为

\[
F=u^2-t^2-a.
\tag{1}
\]

且

\[
\boxed{
F<z^2+c_Q(a+t^2+z^2),
\qquad
c_Q=\frac{2+1/Q}{Q}.
}
\tag{2}
\]

最高层还给出

\[
\boxed{z^2<a\,10^{-4g}\le a.}
\tag{3}
\]

并且前文已证明

\[
\boxed{m_1\ge2k,\qquad n_2\ge2k.}
\tag{4}
\]

---

## 2. 双边界的精确常数偏移

假设

\[
\boxed{m_1=n_2=2k.}
\tag{5}
\]

由 decimal normal form：

\[
\boxed{
b_1=10^{2k}-j,
\qquad j\in\{1,2,3,4\},}
\tag{6}
\]

\[
\boxed{
a_2=10^{2k}-h,
\qquad h\in\{1,2,3,4\}.}
\tag{7}
\]

又因 `n_2=m_2+k+g`，

\[
m_2=k-g,
\]

且前文已证明此边界上

\[
\boxed{b_2=10^{m_2-1}=10^{k-g-1}.}
\tag{8}
\]

于是

\[
Q
=(10^{2k}-j)10^{m_2}+10^{m_2-1}
=10^{m_2-1}(10^{2k+1}-10j+1),
\]

所以

\[
\boxed{
\lambda
=\frac1{10^{2k+1}-10j+1}.
}
\tag{9}
\]

因为 `k\ge1`、`j\le4`，

\[
10^{2k}>10j-1,
\]

故

\[
\boxed{\lambda<\frac a9.}
\tag{10}
\]

---

## 3. 双边界强迫 `t` 下降过多

最高层有

\[
n_1-1=m_1+g+1=2k+g+1,
\]

所以

\[
a_1\ge10^{2k+g+1}.
\]

利用 (6)–(8)：

\[
t
=\frac{a_2b_1}{b_2 10^k a_1}
\le
\frac{(10^{2k}-h)(10^{2k}-j)}{10^{4k}}.
\]

因此

\[
t
\le
1-(h+j)a+hj a^2.
\]

因为 `h+j\ge2`、`hj\le16`、`a\le1/100`：

\[
\boxed{t<1-\frac95a.}
\tag{11}
\]

进一步

\[
\boxed{t^2<1-\frac72a.}
\tag{12}
\]

另一方面 `u>1-\lambda`，由 (10)：

\[
u^2>(1-\lambda)^2>1-2\lambda>1-\frac29a.
\]

代入 (1)、(12)：

\[
F
>
\left(1-\frac29a\right)
-\left(1-\frac72a\right)-a
=
\boxed{\frac{41}{18}a.}
\tag{13}
\]

---

## 4. contact 上界与 (13) 冲突

由 `b_2\ge1`，

\[
\frac1Q=\frac\lambda{b_2}\le\lambda<\frac a9.
\]

所以

\[
c_Q
<\frac{2a}{9}+\frac{a^2}{81}
<\frac a4.
\tag{14}
\]

又由 `t<1`、(3)：

\[
a+t^2+z^2<1+2a<\frac{51}{50}.
\]

从 (2)、(3)、(14)：

\[
F
<
a+rac a4\frac{51}{50}
=
\boxed{\frac{251}{200}a.}
\tag{15}
\]

但

\[
\frac{41}{18}>\frac{251}{200}.
\]

与 (13) 矛盾。

故

\[
\boxed{m_1=n_2=2k\text{ 整个双边界为空}.}
\tag{16}
\]

---

# 5. 单边 `m_1=2k`：四个 `j` 只剩 `g=0,j=1`

现在只假设

\[
\boxed{m_1=2k.}
\]

由 normal form：

\[
b_1=10^{2k}-j,
\qquad
j\in\{1,2,3,4\}.
\tag{17}
\]

又由最高层端点条带，若写

\[
x=\frac{b_2}{10^{m_2}},
\]

则

\[
x<\frac1{10(1-5a)}.
\]

所以

\[
\lambda=\frac{x}{b_1+x}
<\frac{x}{b_1}
<
\frac{a}{10(1-5a)(1-4a)}.
\]

由于 `a\le1/100`，分母严格大于 `9`，故

\[
\boxed{\lambda<\frac a9.}
\tag{18}
\]

四端点乘积中

\[
\frac{b_1}{10^{m_1}}=1-ja,
\]

其余三个因子均不超过 `1`，因此

\[
\boxed{t\le1-ja.}
\tag{19}
\]

由 (1)、`u>1-\lambda`、(18)、(19)：

\[
F
>
\left(1-\frac29a\right)
-(1-ja)^2-a.
\tag{20}
\]

### 5.1 `j\ge2` 全部为空

若 `j\ge2`，最弱情况是 `j=2`。由 `a\le1/100`，(20) 给出

\[
F>\frac{27}{10}a.
\tag{21}
\]

另一方面 (18) 与 §4 同样给出

\[
F<\frac{251}{200}a.
\]

矛盾。

所以

\[
\boxed{j\in\{2,3,4\}\text{ 全空}.}
\tag{22}
\]

### 5.2 `j=1` 在 `g\ge1` 时也为空

若 `j=1`，由 (20)：

\[
F
>
\left(\frac79-a\right)a
>\frac34a.
\tag{23}
\]

如果 `g\ge1`，则由 (3)

\[
z^2<10^{-4}a.
\]

并仍有 `c_Q<a/4`，故

\[
F
<10^{-4}a+rac{51}{200}a
<\frac{13}{50}a.
\tag{24}
\]

与 (23) 矛盾。

因此

\[
\boxed{
m_1=2k
\Longrightarrow
 g=0,
\quad b_1=10^{2k}-1.
}
\tag{25}
\]

再结合双边界 (16)，此时必有

\[
\boxed{n_2\ge2k+1.}
\tag{26}
\]

---

# 6. 单边 `n_2=2k`：只剩 `g=0,h=1`

现在假设

\[
\boxed{n_2=2k.}
\]

由 normal form：

\[
a_2=10^{2k}-h,
\qquad
h\in\{1,2,3,4\},
\tag{27}
\]

并且

\[
\boxed{b_2=10^{m_2-1},
\qquad m_2=k-g.}
\tag{28}
\]

于是

\[
\boxed{
\lambda
=\frac1{10b_1+1}.
}
\tag{29}
\]

由双边界已经为空，而 (4) 给出 `m_1\ge2k`，所以现在必有

\[
\boxed{m_1\ge2k+1.}
\tag{30}
\]

最高层端点正规形还给出

\[
b_1>(1-5a)10^{m_1}.
\]

结合 (30)、`a\le1/100`：

\[
b_1
>(1-5a)10^{2k+1}
>\frac{19}{2}10^{2k}.
\]

所以由 (29)：

\[
\boxed{\lambda<\frac a{95}.}
\tag{31}
\]

并且

\[
\frac1Q=\frac\lambda{b_2}\le\lambda,
\]

从而

\[
\boxed{c_Q<\frac a{40}.}
\tag{32}
\]

四端点乘积中

\[
\frac{a_2}{10^{n_2}}=1-ha,
\]

所以

\[
\boxed{t\le1-ha.}
\tag{33}
\]

由 (1)、`u>1-\lambda`：

\[
F
>
(1-2\lambda)-(1-ha)^2-a.
\tag{34}
\]

### 6.1 `h\ge2` 全空

若 `h\ge2`，最弱取 `h=2`。由 (31)、`a\le1/100`，(34) 给出

\[
F>\frac{29}{10}a.
\tag{35}
\]

另一方面由 (2)、(3)、(32)：

\[
F
<a+rac a{40}\frac{51}{50}
<\frac{103}{100}a.
\tag{36}
\]

矛盾。

故

\[
\boxed{h\in\{2,3,4\}\text{ 全空}.}
\tag{37}
\]

### 6.2 `h=1` 强迫 `g=0`

若 `h=1`，由 (31)、(34)：

\[
F
>
\left(1-a-\frac2{95}\right)a
>\frac{24}{25}a.
\tag{38}
\]

如果 `g\ge1`，则

\[
z^2<10^{-4}a.
\]

由 (2)、(32)：

\[
F
<10^{-4}a+rac{51}{2000}a
<\frac3{100}a.
\tag{39}
\]

矛盾。

因此

\[
\boxed{
n_2=2k
\Longrightarrow
 g=0,
\quad a_2=10^{2k}-1,
\quad b_2=10^{k-1}.
}
\tag{40}
\]

再由双边界为空：

\[
\boxed{m_1\ge2k+1.}
\tag{41}
\]

---

# 7. 最高层边界的最终分类

最高层

\[
s_1=g+2
\]

已经满足

\[
m_1\ge2k,
\qquad
n_2\ge2k.
\]

本文进一步证明：

### 若 `g\ge1`

两个边界都不可能取等，因此

\[
\boxed{
 g\ge1
\Longrightarrow
m_1\ge2k+1,
\qquad
n_2\ge2k+1.
}
\tag{42}
\]

### 若 `g=0`

只有三类：

1. 内部锥
   \[
   m_1\ge2k+1,
   \qquad
   n_2\ge2k+1;
   \]
2. 第一边界唯一族
   \[
   \boxed{
   m_1=2k,
   \quad b_1=10^{2k}-1,
   \quad n_2\ge2k+1;
   }
   \]
3. 第二边界唯一族
   \[
   \boxed{
   n_2=2k,
   \quad a_2=10^{2k}-1,
   \quad b_2=10^{k-1},
   \quad m_1\ge2k+1.
   }
   \]

且两个边界不能同时发生。

因此最高层已经从二维边界面压成：一个严格内部锥，加上 `g=0` 时两条单独的 repunit 型边缘族。