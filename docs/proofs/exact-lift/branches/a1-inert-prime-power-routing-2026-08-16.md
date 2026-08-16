# A1 inert-prime-power routing — 2026-08-16

本文强化 `a1-inert-prime-routing-2026-08-16.md`。

前文只证明第三分母中每个 `p\equiv3\pmod4` 的**素数本身**必须整除 `Q`。现在结合 denominator prime graph 与安全 integer-gap，证明完整指数都必须由 `Q` 承担：

\[
\boxed{
 p\equiv3\pmod4
\Longrightarrow
v_p(b_3)\le v_p(Q).
}
\]

因此第三分母的 Gaussian inert prime-power 部分整体整除 `Q`。

本文结论为 **已严格完成**。

---

## 1. Denominator prime graph 的形状

固定奇素数

\[
p\equiv3\pmod4.
\]

记

\[
e_i=v_p(b_i),
\qquad
E=\max(e_1,e_2,e_3).
\]

全局 denominator prime graph 已严格给出：

1. 若最大赋值唯一取得，则另外两块的 `p`-进指数相等；
2. 对 `p\equiv3\pmod4`，pair-max 不可能。

现在假设

\[
p\mid b_3,
\qquad e_3>0.
\]

因此所有可能赋值形状只有：

### (I) 三块全相等

\[
e_1=e_2=e_3=E;
\]

### (II) 第三块唯一最大

\[
e_3=E>e_1=e_2=e;
\]

### (III) 第一块唯一最大

\[
e_1=E>e_2=e_3=e>0;
\]

### (IV) 第二块唯一最大

\[
e_2=E>e_1=e_3=e>0.
\]

没有其他情况。

---

## 2. 三块全相等

若

\[
e_1=e_2=e_3=E,
\]

则

\[
p^E\mid b_1,
\qquad
p^E\mid b_2.
\]

所以

\[
Q=b_1 10^{m_2}+b_2
\]

两项都被 `p^E` 整除，直接得到

\[
\boxed{v_p(Q)\ge E=e_3.}
\tag{1}
\]

---

## 3. 第一或第二块唯一最大

### 3.1 第一块唯一最大

若

\[
e_1=E>e_2=e_3=e,
\]

由于 `p\nmid10`，`Q` 的两项赋值分别为

\[
v_p(b_1 10^{m_2})=E,
\qquad
v_p(b_2)=e.
\]

二者不同，所以和的赋值等于较小者：

\[
\boxed{v_p(Q)=e=e_3.}
\tag{2}
\]

### 3.2 第二块唯一最大

同理若

\[
e_2=E>e_1=e_3=e,
\]

则

\[
v_p(b_1 10^{m_2})=e,
\qquad
v_p(b_2)=E,
\]

故

\[
\boxed{v_p(Q)=e=e_3.}
\tag{3}
\]

所以只有“第三块唯一最大”需要额外证明。

---

## 4. 第三块唯一最大：`H` 是 `p`-进单位

现在设

\[
\boxed{e_3=E>e_1=e_2=e.}
\tag{4}
\]

令

\[
q=\operatorname{lcm}(b_1,b_2,b_3).
\]

则

\[
v_p(q)=E.
\]

第三整数球面坐标为

\[
y_3=\frac{qa_3}{b_3}.
\]

因为

\[
\gcd(a_3,b_3)=1,
\]

有

\[
p\nmid a_3.
\]

所以

\[
\boxed{v_p(y_3)=E-e_3=0.}
\tag{5}
\]

即 `y_3` 是 `p`-进单位。

而

\[
H^2=y_1^2+y_2^2+y_3^2.
\]

由于 `e_1=e_2=e<E`，前两坐标至少都含 `p^{E-e}`，因此

\[
y_1\equiv y_2\equiv0\pmod p.
\]

模 `p`：

\[
H^2\equiv y_3^2\not\equiv0\pmod p.
\]

故

\[
\boxed{v_p(H)=0.}
\tag{6}
\]

---

## 5. 安全 contact gap 强迫 `p^E\mid Q`

A1 安全 integer-gap 定义

\[
\mathcal E=Cq-DH,
\]

并严格证明

\[
\boxed{\mathcal E=\tau A,}
\tag{7}
\]

其中

\[
\tau=\frac{b_3}{\gcd(10^\ell,b_3)}.
\]

因为 `p\ne2,5`，`10^\ell` 不含 `p`，所以

\[
\boxed{v_p(\tau)=v_p(b_3)=E.}
\tag{8}
\]

由 (7)：

\[
v_p(\mathcal E)\ge E.
\tag{9}
\]

另一方面 `v_p(q)=E`，所以

\[
p^E\mid Cq.
\]

而

\[
\mathcal E=Cq-DH
\]

也被 `p^E` 整除，因此

\[
p^E\mid DH.
\]

由 (6)，`H` 是 `p`-进单位，于是

\[
\boxed{p^E\mid D.}
\tag{10}
\]

A1 中

\[
D=10^gQ.
\]

因为 `p\nmid10`：

\[
\boxed{p^E\mid Q.}
\tag{11}
\]

所以第三块唯一最大时同样有

\[
\boxed{v_p(Q)\ge E=e_3.}
\]

---

## 6. 统一 prime-power routing

四种允许赋值形状全部处理完毕，因此：

\[
\boxed{
 p\equiv3\pmod4,\ p\mid b_3
\Longrightarrow
v_p(Q)\ge v_p(b_3).
}
\tag{12}
\]

定义第三分母的 inert prime-power part

\[
\boxed{
(b_3)_{3(4)}
:=
\prod_{\substack{p\mid b_3\\p\equiv3(4)}}
 p^{v_p(b_3)}.
}
\]

则

\[
\boxed{
(b_3)_{3(4)}\mid Q.
}
\tag{13}
\]

这严格强化了 denominator funnel 的

\[
b_3\mid10^{2m_3}Q^2G.
\]

对 `3 mod 4` 素数而言，`G` 不再提供任何额外 prime-power 容量：第三分母中的完整 inert 部分必须直接塞进 `Q`。

---

## 7. 后续意义

A1 第三分母现在可按奇素数类型分解：

- `p\equiv3\pmod4`：完整指数受 `Q` 控制；
- `p\equiv1\pmod4`：仍可能从 `Q^2G` 获得容量；
- `2,5`：由此前 resonance / cross-corridor 分析控制。

因此 fixed-prefix funnel 中真正尚有较大自由度的 odd part 已经只剩 Gaussian split primes `p\equiv1\pmod4`。

这为下一步把 safe sum-of-two-squares gap

\[
LA(H+y_3)=y_1^2+y_2^2
\]

与第三分母 prime supply 联立提供了更锋利的局部入口。