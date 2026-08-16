# A1 safe 2-adic max dichotomy — 2026-08-16

本文只使用整数球面、denominator recovery 与安全 gap

\[
U=H-y_3=LA
\]

分析素数 `2`。结论给出一个覆盖整个 A1 的二进分流：

- 若二进最大 denominator 在前两块，则第三分母必须吸收完整 `2^\ell`；
- 若第三分母没有吸收完整 `2^\ell`，则第三块必须是唯一二进最大，并得到显式 `\ell` 上界。

本文结论均为 **已严格完成**。

---

## 1. 球面奇偶性

令

\[
e_i=v_2(b_i),
\qquad
E=\max(e_1,e_2,e_3).
\]

整数球面满足

\[
y_1^2+y_2^2+y_3^2=H^2.
\]

全局模 `4` 分析已经严格给出：

\[
\boxed{H\text{ 为奇数},}
\]

并且

\[
\boxed{y_1,y_2,y_3\text{ 中恰有一个奇数}.}
\]

这等价于

\[
\boxed{E\text{ 在 }e_1,e_2,e_3\text{ 中唯一取得}.}
\tag{1}
\]

而取得最大 denominator exponent 的那一坐标恰好是奇的 `y_i`。

---

## 2. 若前缀 denominator 取得二进最大，则 `e_3\ge\ell`

假设唯一最大值在第一或第二块。

那么

\[
\boxed{y_3\equiv0\pmod2.}
\]

因为 `H` 为奇数：

\[
\boxed{U=H-y_3\text{ 为奇数}.}
\tag{2}
\]

安全 gap 分解为

\[
U=LA,
\]

其中

\[
L=\frac{10^\ell}{\gcd(10^\ell,b_3)}.
\]

所以

\[
\boxed{
v_2(L)=\max(\ell-e_3,0).
}
\tag{3}
\]

由 (2)，`L` 必为奇数，因此

\[
\boxed{e_3\ge\ell.}
\tag{4}
\]

也就是说：

\[
\boxed{
\max(e_1,e_2)>e_3
\Longrightarrow
v_2(b_3)\ge\ell.
}
\tag{5}
\]

这是一条纯安全球面结论。

---

## 3. 若 `e_3<\ell`，第三块必为唯一二进最大

(5) 的逆否命题立刻给出：

若

\[
\boxed{e_3<\ell,}
\]

则二进最大值不能在前缀。

由 (1)，最大值又必须唯一，所以

\[
\boxed{e_3>e_1,e_2.}
\tag{6}
\]

此时

\[
y_3,H
\]

都是奇数，而 `y_1,y_2` 都是偶数。

记

\[
\alpha_2=v_2(y_1)=e_3-e_1,
\qquad
\beta_2=v_2(y_2)=e_3-e_2.
\]

两者均至少为 `1`。

---

## 4. 二平方和的精确二进赋值

由

\[
U(H+y_3)=y_1^2+y_2^2
\tag{7}
\]

分析右侧。

### 4.1 `e_1\ne e_2`

此时

\[
\alpha_2\ne\beta_2.
\]

两个平方的二进赋值不同，所以无 cancellation：

\[
\boxed{
v_2(y_1^2+y_2^2)
=2\min(\alpha_2,\beta_2).
}
\]

令

\[
M=\max(e_1,e_2).
\]

则

\[
\min(\alpha_2,\beta_2)=e_3-M,
\]

所以

\[
\boxed{
v_2(y_1^2+y_2^2)=2(e_3-M).}
\tag{8}
\]

### 4.2 `e_1=e_2`

此时

\[
\alpha_2=\beta_2=r:=e_3-e_1.
\]

约去 `2^{2r}` 后是两个奇数平方之和；任意奇数平方模 `8` 都为 `1`，所以和模 `8` 为 `2`。

因此

\[
\boxed{
v_2(y_1^2+y_2^2)=2r+1
=2(e_3-M)+1.}
\tag{9}
\]

---

## 5. `U` 与 `H+y_3` 中恰有一个只有一个因子 2

`H,y_3` 都是奇数，所以

\[
U=H-y_3,
\qquad
H+y_3
\]

都是偶数。

并且它们的和为

\[
2H\equiv2\pmod4.
\]

所以二者中恰有一个满足二进赋值 `1`，另一个承担右侧剩余的全部二进深度。

因此由 (7)：

\[
\boxed{
v_2(U)\le
v_2(y_1^2+y_2^2)-1.
}
\tag{10}
\]

另一方面由 `U=LA`：

\[
v_2(U)\ge v_2(L)=\ell-e_3
\]

（当前正处于 `e_3<\ell`）。

于是

\[
\boxed{
\ell-e_3
\le
v_2(y_1^2+y_2^2)-1.
}
\tag{11}
\]

---

## 6. 显式尾长界

### 若 `e_1\ne e_2`

由 (8)、(11)：

\[
\ell-e_3
\le2(e_3-M)-1.
\]

所以

\[
\boxed{
\ell\le3e_3-2M-1.
}
\tag{12}
\]

### 若 `e_1=e_2`

由 (9)、(11)：

\[
\ell-e_3
\le2(e_3-M).
\]

因此

\[
\boxed{
\ell\le3e_3-2M.
}
\tag{13}
\]

---

## 7. 二进通道的最终二选一

令

\[
e_3=v_2(b_3),
\qquad M=\max(v_2(b_1),v_2(b_2)).
\]

A1 任意候选必须满足以下之一：

### 2-saturated side

\[
\boxed{e_3\ge\ell.}
\]

特别地，若二进最大 denominator 位于前两块，则只能落在这一侧。

### third-unique-max side

\[
\boxed{e_3<\ell,
\qquad e_3>M,}
\]

并且

\[
\boxed{
\ell\le
\begin{cases}
3e_3-2M-1,&e_1\ne e_2,\\
3e_3-2M,&e_1=e_2.
\end{cases}}
\]

这把整个 A1 的二进尾部压成一个明确的 saturated / unique-max 二分，而无需调用旧 primitive tail quadratic。