# A1 direct 2/5-adic tail collapse — 2026-08-16

本文给出一个比此前 `resonance / double-nonresonance / cross-corridor` 分类更短的 fixed-prefix finite 证明。

核心输入只有：

1. 原始 exact lift 的平方恒等式；
2. `T=10^\ell`；
3. 第三分数既约性 `gcd(a_3,b_3)=1`。

结论是：第三分母相对 `T` 的二进、五进**正偏移**分别有一个只依赖前缀的显式上界。结合 decade window 后，负偏移也自动有下界，因此 `(h,x,y)` 直接落入显式有限矩形。

本文结论均为 **已严格完成**。

---

## 1. 原始平方恒等式

沿用

\[
T=10^\ell,
\qquad
C=a_1 10^{n_2}+a_2,
\qquad
D=10^gQ,
\]

\[
G=b_1b_2,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2.
\]

exact lift 写成

\[
\frac{TC+a_3}{TD+b_3}
=
\sqrt{\frac N{G^2}+\frac{a_3^2}{b_3^2}}.
\]

平方并清分母：

\[
\boxed{
G^2b_3^2(TC+a_3)^2
=
(TD+b_3)^2
\left(Nb_3^2+G^2a_3^2\right).
}
\tag{1}
\]

这条恒等式完全直接来自原问题，不使用旧 `a_3/\delta_3` 正规化。

展开成关于 `T` 的二次式还得到

\[
\begin{aligned}
0={}&
\left(b_3^2K-D^2G^2a_3^2\right)T^2\\
&+2b_3\left[
G^2a_3(Cb_3-Da_3)-DNb_3^2
\right]T
-Nb_3^4,
\end{aligned}
\tag{2}
\]

其中

\[
K=G^2C^2-D^2N.
\]

特别地，(2) 模 `T` 立刻给出

\[
\boxed{T\mid Nb_3^4.}
\tag{3}
\]

所以若 `p\in\{2,5\}` 且 `p\nmid b_3`，则

\[
\boxed{\ell\le v_p(N).}
\tag{4}
\]

这已经说明：固定前缀下，若第三分母缺少 `2` 或 `5` 中任意一个，则尾长直接有前缀上界。

---

## 2. 当 `p\mid b_3` 时的精确赋值方程

固定

\[
p\in\{2,5\}.
\]

记

\[
e=v_p(b_3)>0,
\qquad
\gamma=v_p(G),
\qquad
d=v_p(D),
\qquad
n=v_p(N).
\]

由于

\[
\gcd(a_3,b_3)=1,
\]

有

\[
\boxed{v_p(a_3)=0.}
\tag{5}
\]

又因为 `\ell\ge1`，`T` 被 `p` 整除，所以

\[
TC+a_3
\]

是 `p`-进单位：

\[
\boxed{v_p(TC+a_3)=0.}
\tag{6}
\]

对 (1) 两边取 `p`-进赋值，得到精确等式

\[
\boxed{
2e+2\gamma
=
2v_p(TD+b_3)
+
v_p(Nb_3^2+G^2a_3^2).
}
\tag{7}
\]

---

## 3. 正偏移的 universal upper bound

假设反面

\[
e>\max(\ell+d,\gamma).
\tag{8}
\]

因为

\[
v_p(TD)=\ell+d<e=v_p(b_3),
\]

两项赋值不同，所以

\[
\boxed{v_p(TD+b_3)=\ell+d.}
\tag{9}
\]

另一方面，由 `e>\gamma` 与 `n\ge0`：

\[
n+2e>2\gamma.
\]

在

\[
Nb_3^2+G^2a_3^2
\]

中，两项赋值分别为

\[
n+2e
\quad\text{与}\quad
2\gamma,
\]

严格不同，故

\[
\boxed{
v_p(Nb_3^2+G^2a_3^2)=2\gamma.
}
\tag{10}
\]

把 (9)–(10) 代回 (7)：

\[
2e+2\gamma
=2(\ell+d)+2\gamma,
\]

即

\[
e=\ell+d,
\]

与 (8) 矛盾。

因此：

\[
\boxed{
v_p(b_3)
\le
\max\bigl(\ell+v_p(D),\ v_p(G)\bigr),
\qquad p=2,5.
}
\tag{11}
\]

这是整个 A1 的 universal `2/5` tail valuation cap。

---

## 4. 低侧状态还有必要下界

若

\[
e<\ell+d,
\tag{12}
\]

则

\[
v_p(TD+b_3)=e.
\]

由 (7) 得

\[
v_p(Nb_3^2+G^2a_3^2)=2\gamma.
\tag{13}
\]

若

\[
n+2e<2\gamma,
\]

则和式左侧的赋值应为 `n+2e`，与 (13) 矛盾。因此低侧必满足

\[
\boxed{
n+2e\ge2\gamma.}
\tag{14}
\]

即

\[
\boxed{
e\ge
\left\lceil\frac{2v_p(G)-v_p(N)}2\right\rceil
}
\quad\text{只要 }e<\ell+v_p(D).
\tag{15}
\]

等号赋值时还需避免额外 `p`-进抵消；本文只保留 (15) 作为必要条件。

---

## 5. 归一化偏移的前缀上界

写

\[
b_3=h2^u5^v,
\qquad
\gcd(h,10)=1,
\qquad
h\mid Q^2G
\]

（最后一条来自 universal denominator certificate）。定义

\[
\boxed{x=u-\ell,\qquad y=v-\ell.}
\]

如果 `x>0`，则 `u>0`，可对 `p=2` 使用 (11)：

\[
\ell+x
\le
\max\left(\ell+v_2(D),v_2(G)\right).
\]

因为 `\ell\ge1`，得到

\[
\boxed{
x\le X_+
:=\max\left(v_2(D),v_2(G)-1\right).}
\tag{16}
\]

对 `x\le0` 该上界自动成立，因为 `X_+\ge0`。所以实际上所有候选统一满足

\[
\boxed{x\le X_+.}
\tag{17}
\]

完全同理，

\[
\boxed{y\le Y_+
:=\max\left(v_5(D),v_5(G)-1\right).}
\tag{18}
\]

注意

\[
D=10^gQ,
\]

所以

\[
v_2(D)=g+v_2(Q),
\qquad
v_5(D)=g+v_5(Q).
\]

`X_+,Y_+` 都是纯前缀常数。

---

## 6. decade window 自动给出负偏移下界

归一化第三分母为

\[
\rho=\frac{b_3}{T}=h2^x5^y.
\]

A1 位数窗等价于

\[
\boxed{10^{g-1}\le h2^x5^y<10^g.}
\tag{19}
\]

由 `y\le Y_+` 与 (19) 左端：

\[
2^x
\ge
\frac{10^{g-1}}{h5^{Y_+}},
\]

故

\[
\boxed{
x\ge X_-
:=
\left\lceil
\log_2\frac{10^{g-1}}{h5^{Y_+}}
\right\rceil.}
\tag{20}
\]

同理由 `x\le X_+`：

\[
\boxed{
y\ge Y_-
:=
\left\lceil
\log_5\frac{10^{g-1}}{h2^{X_+}}
\right\rceil.}
\tag{21}
\]

因此对每个固定的 `h\mid Q^2G`：

\[
\boxed{
X_-\le x\le X_+,
\qquad
Y_-\le y\le Y_+.
}
\tag{22}
\]

这是一个显式有限整数矩形。

---

## 7. Fixed-prefix finite 的短证明

固定前两块后：

1. `g` 已有有限前缀范围；
2. `h\mid Q^2G`，所以 `h` 有有限多个选择；
3. 对每个 `h`，(22) 把 `(x,y)` 放入显式有限矩形；
4. 因而
   \[
   \rho=h2^x5^y
   \]
   只有有限多个值；
5. 固定 `\rho` 后，rational-contact quadratic 对 `r_3` 至多给出两个固定有理根；
6. 原问题要求该根的**既约分母**恰为
   \[
   b_3=T\rho=10^\ell\rho,
   \]
   因而每个固定根至多实现一个 `\ell`。

于是得到：

\[
\boxed{
\text{对任意固定前两块，A1 第三块候选集合有限。}
}
\tag{23}
\]

这个证明不再需要逐个讨论 resonance、`++/--` 象限和两条 cross corridors。

---

## 8. 与旧 tail 文件的关系

此前的

- `a1-resonance-collapse-2026-08-16.md`；
- `a1-cross-corridor-reduction-2026-08-16.md`；
- `a1-cross-corridor-primitive-collapse-2026-08-16.md`

仍然是正确且更细的局部结构分析，可用于以后需要精确枚举 offset 时使用。

但在“证明 fixed-prefix finite”这一目标上，本文 (11)、(17)–(23) 已提供更短、更统一的主证明。因此 A1 后续主线可以直接引用本文，把 resonance/corridor 分类降级为可选细化，而把研究精力集中到 moving-prefix 四层 `h=-1,0,1,2`。
