# A1 resonance collapse — 2026-08-16

本文继续：

- `a1-rational-contact-framework-2026-08-16.md`；
- `a1-denominator-funnel-2026-08-16.md`。

目标是把 A1 denominator funnel 中所有至少含一个 `2`/`5` resonance 的尾部彻底压成固定前缀下的有限状态，并精确说明为什么这些状态不能承载 `\ell\to\infty`。

除最后的“剩余核心”外，本文结论均为 **已严格完成**。

---

## 1. 统一偏移坐标

由 denominator funnel，写

\[
\boxed{b_3=h2^u5^v},
\qquad
\gcd(h,10)=1,
\qquad
h\mid Q^2G.
\]

同时

\[
T=10^\ell=2^\ell5^\ell,
\qquad
m_3=g+\ell.
\]

定义两个尾赋值偏移

\[
\boxed{x=u-\ell},
\qquad
\boxed{y=v-\ell}.
\]

于是

\[
\boxed{
\frac{b_3}{T}=h2^x5^y.
}
\]

而 `b_3` 恰有 `m_3=g+\ell` 位，因此

\[
10^{g+\ell-1}\le b_3<10^{g+\ell}.
\]

除以 `T=10^\ell`，得到整个 A1 的统一 decade window：

\[
\boxed{
10^{g-1}
\le h2^x5^y
<10^g.
}
\tag{1}
\]

这是后面把 resonance 从一条无限直线压成有限整数点的关键。

---

## 2. 二进 resonance 精确锁定 `x`

沿用 denominator funnel 的记号

\[
K=G^2C^2-D^2N,
\qquad
D=10^gQ.
\]

二进 resonance 条件为

\[
\ell+v_2(K)
=
1+u+g+v_2(Q)+v_2(N).
\]

代入 `u=\ell+x`，消去 `\ell`：

\[
\boxed{
x=x_2^*}
\]

其中

\[
\boxed{
 x_2^*
=
v_2(K)-1-g-v_2(Q)-v_2(N).
}
\tag{2}
\]

所以二进 resonance 不只是控制赋值的增长率，而是把 `u-\ell` 精确固定成前缀常数。

把 (2) 代回 decade window (1)：

\[
10^{g-1}
\le h2^{x_2^*}5^y
<10^g.
\]

取对数可得

\[
\frac{(g-1)\log10-\log h-x_2^*\log2}{\log5}
\le y
<
\frac{g\log10-\log h-x_2^*\log2}{\log5}.
\]

这个实区间的长度恰为

\[
\frac{\log10}{\log5}
=1+\frac{\log2}{\log5}
<2.
\]

因此：

\[
\boxed{
\text{固定前缀与 }h\text{ 后，二进 resonance 至多留下两个整数 }y.
}
\tag{3}
\]

---

## 3. 五进 resonance 精确锁定 `y`

五进 resonance 条件为

\[
\ell+v_5(K)
=
v+g+v_5(Q)+v_5(N).
\]

代入 `v=\ell+y`，消去 `\ell`：

\[
\boxed{y=y_5^*}
\]

其中

\[
\boxed{
 y_5^*
=
v_5(K)-g-v_5(Q)-v_5(N).
}
\tag{4}
\]

代回 decade window：

\[
10^{g-1}
\le h2^x5^{y_5^*}
<10^g.
\]

于是

\[
\frac{(g-1)\log10-\log h-y_5^*\log5}{\log2}
\le x
<
\frac{g\log10-\log h-y_5^*\log5}{\log2}.
\]

区间长度为

\[
\frac{\log10}{\log2}
=1+\frac{\log5}{\log2}
<4.
\]

因此：

\[
\boxed{
\text{固定前缀与 }h\text{ 后，五进 resonance 至多留下四个整数 }x.
}
\tag{5}
\]

---

## 4. 双 resonance 更强：偏移唯一

若二进、五进同时 resonance，则

\[
\boxed{(x,y)=(x_2^*,y_5^*)}
\]

完全由前缀唯一确定。

此时只需检查一次 decade window

\[
10^{g-1}
\le h2^{x_2^*}5^{y_5^*}<10^g.
\]

若不成立，整个双 resonance 状态立即为空。

若成立，定义

\[
\boxed{\rho=h2^{x_2^*}5^{y_5^*}}.
\]

则

\[
\boxed{b_3=T\rho}.
\]

尽管 `\rho` 未必是整数，它是一个由前缀唯一确定的正有理数。

---

## 5. 任意单 resonance 都把 `b_3/T` 压成有限集合

二进 resonance 时，由 §2，`x=x_2^*`，而 `y` 至多两个可能值；因此

\[
\boxed{
\rho:=\frac{b_3}{T}=h2^x5^y
}
\]

只可能落在一个至多两元素集合中。

五进 resonance 时同理，`y=y_5^*`，`x` 至多四个可能值，因此 `\rho` 至多有四个值。

双 resonance 则至多一个值。

所以：

\[
\boxed{
\text{任意至少含一个 resonance 的 A1 状态，固定前缀与 }h\text{ 后，}
\rho=b_3/T\text{ 只有有限多个值。}
}
\tag{6}
\]

注意这一步没有使用任何有限枚举；有限性直接来自 resonance 等式和十进制位数窗。

---

## 6. 固定 `\rho` 后 `r_3` 也被固定

A1 rational-contact 参数为

\[
\theta=\frac{b_3}{TD}.
\]

若

\[
b_3=T\rho,
\]

则

\[
\boxed{\theta=\frac\rho D}
\]

与 `\ell` 无关。

而前缀 `P=C/D`、`S=N/G^2` 也均固定。故判别平方

\[
P^2-(1+2\theta)S=z^2
\]

若成立，则二次根公式给出的

\[
 r_3
=
\frac{\theta P\pm(1+\theta)z}{1+2\theta}
\]

也是固定有理数，至多两个符号候选。

写其既约形式为

\[
\boxed{r_3=\frac pq},
\qquad
\gcd(p,q)=1.
\]

原问题本身规定 `r_3=a_3/b_3` 已经既约，因此必须有

\[
\boxed{b_3=q}.
\tag{7}
\]

但另一方面

\[
b_3=T\rho=10^\ell\rho.
\]

把 `\rho=A/B` 写成既约正有理数，(7) 变成

\[
10^\ell\frac AB=q.
\]

所以

\[
\boxed{
10^\ell=\frac{qB}{A}.
}
\tag{8}
\]

右端是固定有理数。

因此每个固定 `(prefix,h,\rho,\pm)` 状态至多存在一个 `\ell`，并且只有当右端恰为十的非负整数幂时才可能存在。

于是得到本文核心结论：

\[
\boxed{
\text{A1 中所有至少含一个 }2/5\text{ resonance 的尾部，固定前缀后均无无界 }\ell\text{ 族。}
}
\tag{9}
\]

这比“固定前缀有限”更精确：对每一个 resonance offset 状态与根号符号，`\ell` 至多一个。

---

## 7. resonance 扇区的严格状态

综合 denominator funnel 中 `h\mid Q^2G`：

1. `h` 取自固定前缀的有限因子集；
2. 二进 resonance：每个 `h` 至多两个 `y`；
3. 五进 resonance：每个 `h` 至多四个 `x`；
4. 双 resonance：每个 `h` 至多一个 `(x,y)`；
5. 每个 offset 状态至多两个 `r_3` 根；
6. 每个根至多一个 `\ell`。

所以：

\[
\boxed{
\text{含 resonance 的全部 A1 扇区已经归约为显式、可审计的 fixed-prefix finite certificate。}
}
\]

这里仍不能推出所有前缀的并集有限；该结论的用途是严格证明：任何真正的 A1 无界尾族都只能藏在**二进、五进同时非 resonance**的区域。

---

## 8. 新的唯一无界尾核心

因此 A1 尾部的真正无限核心已经缩为

\[
\boxed{
\text{double-nonresonant sector}
}
\]

即同时满足

\[
\ell+v_2(K)
\ne
1+u+g+v_2(Q)+v_2(N),
\]

\[
\ell+v_5(K)
\ne
v+g+v_5(Q)+v_5(N),
\]

以及

\[
b_3=h2^u5^v,
\qquad h\mid Q^2G,
\]

\[
10^{g-1}\le h2^{u-\ell}5^{v-\ell}<10^g,
\]

\[
W^2=T^2K-2Tb_3DN.
\]

下一步不应再同时处理四个赋值扇区；只需专攻这个 double-nonresonant core。
