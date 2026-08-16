# A1 odd prime-power routing classification — 2026-08-16

本文把 `a1-inert-prime-power-routing-2026-08-16.md` 推广到全部奇素数 `p\ne5`。

核心结论：若 `p\mid b_3` 且第三分母中的完整 `p`-幂没有进入 `Q`，那么这只能是一个 Gaussian split prime 的 pair-max 异常：

\[
\boxed{
v_p(b_3)>v_p(Q)
\Longrightarrow
p\equiv1\pmod4,
}
\]

并且必有恰好一种

\[
\boxed{
v_p(b_3)=v_p(b_1)>v_p(b_2),}
\]

或

\[
\boxed{
v_p(b_3)=v_p(b_2)>v_p(b_1).}
\]

本文结论均为 **已严格完成**。

---

## 1. 记号与 denominator prime graph

固定奇素数

\[
p\ne5,
\qquad p\mid b_3.
\]

记

\[
e_i=v_p(b_i),
\qquad E=\max(e_1,e_2,e_3).
\]

全局 denominator prime graph 给出：

1. unique max 时，另外两块的指数相等；
2. pair-max 只可能由 `p\equiv1\pmod4` 承担。

另外，前文已经独立证明：若第三块是 unique max，

\[
e_3=E>e_1=e_2,
\]

则安全 contact gap 强迫

\[
\boxed{p^E\mid Q.}
\tag{1}
\]

该证明实际上不使用 `p\equiv3\pmod4`，只需 `p\ne2,5`。

---

## 2. 非 pair-max 情形全部满足 `e_3\le v_p(Q)`

### 2.1 三块全相等

若

\[
e_1=e_2=e_3=E,
\]

则 `p^E` 同时整除 `b_1,b_2`，故

\[
\boxed{v_p(Q)\ge E=e_3.}
\tag{2}
\]

### 2.2 第一块 unique max

若

\[
e_1=E>e_2=e_3=e,
\]

则 `Q=b_1 10^{m_2}+b_2` 两项赋值分别为 `E,e`，所以

\[
\boxed{v_p(Q)=e=e_3.}
\tag{3}
\]

### 2.3 第二块 unique max

同理

\[
e_2=E>e_1=e_3=e
\]

给出

\[
\boxed{v_p(Q)=e=e_3.}
\tag{4}
\]

### 2.4 第三块 unique max

由安全 gap 证明 (1)：

\[
\boxed{v_p(Q)\ge E=e_3.}
\tag{5}
\]

因此，只要不是 pair-max，就必有

\[
\boxed{e_3\le v_p(Q).}
\tag{6}
\]

---

## 3. Pair-max 的三种位置

pair-max 只可能有 `p\equiv1\pmod4`。

### 3.1 第一、第二块 pair-max

若

\[
e_1=e_2=E>e_3,
\]

则 `Q` 的两项都被 `p^E` 整除，所以

\[
\boxed{v_p(Q)\ge E>e_3.}
\tag{7}
\]

这一 pair-max 也不会造成 routing deficit。

### 3.2 第一、第三块 pair-max

若

\[
\boxed{e_1=e_3=E>e_2=e,}
\tag{8}
\]

则 `Q` 两项赋值分别为 `E,e`，所以

\[
\boxed{v_p(Q)=e<E=e_3.}
\tag{9}
\]

这是第一种真正的 prime-power routing 异常。

### 3.3 第二、第三块 pair-max

若

\[
\boxed{e_2=e_3=E>e_1=e,}
\tag{10}
\]

同理

\[
\boxed{v_p(Q)=e<E=e_3.}
\tag{11}
\]

这是第二种异常。

---

## 4. 完整分类

综上，对任意奇素数 `p\ne5` 且 `p\mid b_3`：

\[
\boxed{
 v_p(b_3)\le v_p(Q)
}
\]

除非同时满足

\[
\boxed{p\equiv1\pmod4}
\]

并且 `p` 的 denominator exponent pattern 是

\[
\boxed{
(e_1,e_2,e_3)=(E,e,E),\quad e<E,
}
\]

或

\[
\boxed{
(e_1,e_2,e_3)=(e,E,E),\quad e<E.
}
\]

因此可写成一句结构性结论：

\[
\boxed{
\text{第三分母中未被 }Q\text{ 完整吸收的 odd prime-power，}
\text{只能来自 }p\equiv1\pmod4\text{ 的 prefix--third pair-max。}
}
\tag{12}
\]

---

## 5. 与 inert routing 的关系

若

\[
p\equiv3\pmod4,
\]

pair-max 本身被 denominator prime graph 禁止，所以 (12) 自动退化为

\[
\boxed{v_p(b_3)\le v_p(Q),}
\]

恰好恢复 `a1-inert-prime-power-routing-2026-08-16.md`。

所以 inert theorem 是本文完整 odd-prime 分类的无异常特例。

---

## 6. 后续核心

结合 universal denominator certificate

\[
b_3\mid10^{2m_3}Q^2G,
\]

第三分母的 odd part 现在只剩两类来源：

1. **Q-routed part**：完整 prime-power 已整除 `Q`；
2. **split pair-max part**：`p\equiv1\pmod4`，且第三块与恰好一个前缀 denominator 并列取得最大指数。

因此后续 Gaussian / square analysis 已无需再处理任意 odd prime-flow 图；只需研究第二类 split pair-max 异常是否能与 safe gap

\[
LA(H+y_3)=y_1^2+y_2^2
\]

及整数平方证书同时存在。