# A1 second-repunit minimal-third 5-adic closure — 2026-08-16

本文继续 `a1-repunit-minimal-third-25-sieve-2026-08-16.md`。

前文把 second-repunit edge 的最小第三尾边界压成

\[
\ell=2k+1,
\qquad
b_3=10^{2k},
\qquad
 a_3=10^{2k+1}-h,
\]

其中

\[
h\in\{1,3,7,9,11\},
\]

并且若

\[
b_1=10^{m_1}-d,
\]

则

\[
\boxed{v_5(d)=k-1.}
\]

本文证明这一整层实际上为空：

\[
\boxed{\ell=2k+1\text{ 无 exact lift}.}
\]

因此 second-repunit edge 上进一步有

\[
\boxed{\ell\ge2k+2.}
\]

证明是一个精确的 5-adic monomial uniqueness certificate，不枚举 `k` 或 `m_1`。

---

## 1. 参数化

令

\[
\boxed{x=10^k,}
\qquad
\boxed{R=10^{m_1-4k}.}
\]

因为此前已经证明 `m_1\ge4k+1`，所以

\[
R\in10\mathbf Z_{>0},
\qquad
v_5(R)\ge1.
\]

第一块写成

\[
\boxed{b_1=Rx^4-d,}
\qquad
\boxed{a_1=10Rx^4+e,}
\]

其中

\[
d\ge1,
\qquad e\ge0.
\]

second-repunit 与最小第三尾数据为

\[
b_2=\frac{x}{10},
\qquad
 a_2=x^2-1,
\]

\[
b_3=x^2,
\qquad
 a_3=10x^2-h,
\]

其中

\[
h\in\{1,3,7,9,11\}.
\]

前文的安全五进 sieve 给出

\[
\boxed{v_5(d)=k-1.}
\tag{1}
\]

---

## 2. exact-lift 清分母多项式

令

\[
C=a_1x^2+a_2,
\qquad
Q=b_1x+b_2,
\qquad
T=10x^2.
\]

于是

\[
\alpha=TC+a_3,
\qquad
\beta=TQ+b_3.
\]

将 exact lift 平方并清掉所有分母：

\[
\Phi_h(x,R,d,e)=0,
\tag{2}
\]

其中 `\Phi_h` 是整数多项式。

我们不需要展开它的全部系数，只需要对每个 monomial 做 5-adic 赋值账本。

---

## 3. 唯一最浅 monomial

在五个允许的 `h` 中，`\Phi_h` 都含有 monomial

\[
\boxed{x^7d^2.}
\]

其系数分别为某个非零整数，并且统一满足

\[
\boxed{v_5([x^7d^2]\Phi_h)=4.}
\tag{3}
\]

利用

\[
v_5(x)=k,
\qquad
v_5(d)=k-1,
\]

这一项的总赋值恰为

\[
7k+2(k-1)+4
=
\boxed{9k+2.}
\tag{4}
\]

---

## 4. 所有其他 monomial 至少深一个完整 `k`

任取另一个 monomial

\[
c\,x^{a_x}R^{a_R}d^{a_d}e^{a_e}.
\]

在只使用

\[
v_5(R)\ge1,
\qquad
v_5(e)\ge0
\]

的前提下，其 5-adic 赋值至少为

\[
(a_x+a_d)k
+a_R
+v_5(c)-a_d.
\tag{5}
\]

对五个

\[
h\in\{1,3,7,9,11\}
\]

的符号多项式逐 monomial 精确审计得到：除 `x^7d^2` 外，**每一项**都满足

\[
\boxed{a_x+a_d\ge10,}
\tag{6}
\]

\[
\boxed{a_R\ge0,}
\tag{7}
\]

以及

\[
\boxed{v_5(c)-a_d\ge2.}
\tag{8}
\]

所以所有其他项的赋值都至少为

\[
10k+2.
\tag{9}
\]

因为

\[
k\ge1,
\]

有

\[
10k+2>9k+2.
\]

因此 `x^7d^2` 是整个多项式中**唯一**取得最小 5-adic 赋值的 monomial。

---

## 5. 唯一最小赋值不可能相消

若整数和为零，那么其中最小 `p`-进赋值必须至少由两项共同取得；否则约去最小公因子后，模 `p` 会只剩一个非零项。

但 (4)、(9) 表明 `\Phi_h` 中只有 `x^7d^2` 具有赋值 `9k+2`，其余全部严格更深。

所以

\[
\Phi_h(x,R,d,e)\ne0.
\]

这对每个

\[
h\in\{1,3,7,9,11\}
\]

以及所有

\[
k\ge1,
\quad m_1\ge4k+1
\]

成立。

因此

\[
\boxed{\ell=2k+1\text{ 整层为空}.}
\tag{10}
\]

结合前文 `\ell\ge2k+1`：

\[
\boxed{\ell\ge2k+2.}
\tag{11}
\]

---

## 6. 有限符号证书

脚本：

`scripts/check_a1_minimal_third_5adic.py`

脚本只验证有限的符号事实：

1. 五个允许 `h`；
2. `x^7d^2` 系数的 `v_5=4`；
3. 其余每个 monomial 都满足 (6)–(8)。

无界参数 `k,m_1` 始终保留在赋值公式中，没有被有限枚举替代。

---

## 7. Second-repunit edge 的最新形状

当前这条最高层特殊边缘已经满足

\[
\boxed{
 m_1\ge4k+1,
\qquad
\ell\ge2k+2,
}
\]

并且此前的整体 escape cone 仍成立：

\[
\boxed{
 m_1\ge5k-3
\quad\text{或}\quad
\ell\ge3k-3.
}
\]

所以最接近端点的第三尾层已经完全消失；任何剩余族必须继续向更深第三尾或更长第一分母方向逃逸。