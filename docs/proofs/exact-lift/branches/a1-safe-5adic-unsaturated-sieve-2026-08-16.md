# A1 safe 5-adic unsaturated sieve — 2026-08-16

本文分析第三块没有吸收完整 `5^\ell` 的情形。

令

\[
e_i=v_5(b_i).
\]

若

\[
\boxed{e_3<\ell,}
\]

则安全 gap 中 `5\mid L`，所以 `5\mid U=H-y_3`。把这一事实与 odd-prime denominator graph 联立，可排除大部分五进最大赋值形状。

核心结论：五进 unsaturated 时，只剩

1. 第三块 unique max；
2. 三块指数全相等；
3. 第一、第二块 pair-max。

任何涉及第三块与恰好一个前缀块 pair-max 的形状都为空，前缀 unique-max 也为空。

本文结论均为 **已严格完成**。

---

## 1. Unsaturated 强迫 `5\mid U`

安全 gap 为

\[
U=LA,
\qquad
L=\frac{10^\ell}{\gcd(10^\ell,b_3)}.
\]

所以

\[
\boxed{
v_5(L)=\ell-e_3>0.}
\]

因此

\[
\boxed{5\mid U=H-y_3.}
\tag{1}
\]

即

\[
\boxed{H\equiv y_3\pmod5.}
\tag{2}
\]

---

## 2. 前缀 unique-max 不可能

假设第一块 unique max：

\[
e_1=E>e_2=e_3=e.
\]

则整数球面坐标满足

\[
y_1\text{ 是 5 进单位},
\qquad
5\mid y_2,y_3.
\]

球面模 `5`：

\[
H^2\equiv y_1^2\not\equiv0\pmod5,
\]

所以 `H` 是 5 进单位。

但 `5\mid y_3`，于是

\[
U=H-y_3
\]

也是 5 进单位，与 (1) 矛盾。

因此第一块 unique max 为空。

第二块 unique max 完全同理。

所以：

\[
\boxed{
 e_3<\ell
\Longrightarrow
\text{五进 unique max 若存在，只能在第三块}.}
\tag{3}
\]

---

## 3. `b_1,b_3` pair-max 不可能

设

\[
e_1=e_3=E>e_2.
\]

则

\[
y_1,y_3
\]

都是 5 进单位，而

\[
5\mid y_2.
\]

由 (2)：

\[
H\equiv y_3\pmod5.
\]

所以

\[
H^2\equiv y_3^2\pmod5.
\]

另一方面球面模 `5`：

\[
H^2
\equiv y_1^2+y_3^2
\pmod5.
\]

比较得到

\[
y_1^2\equiv0\pmod5,
\]

与 `y_1` 是 5 进单位矛盾。

因此

\[
\boxed{
 e_1=e_3>e_2,\ e_3<\ell
\text{ 为空}.}
\tag{4}
\]

同理

\[
\boxed{
 e_2=e_3>e_1,\ e_3<\ell
\text{ 为空}.}
\tag{5}
\]

---

## 4. 五进 unsaturated 的全部剩余最大形状

odd denominator graph 允许的形状包括：

- unique max；
- pair-max（`5\equiv1 mod4`，所以允许）；
- 三块全相等。

由 §§2–3，若 `e_3<\ell`，只剩：

### (I) 第三块 unique max

\[
\boxed{e_3=E>e_1=e_2.}
\]

### (II) 三块全相等

\[
\boxed{e_1=e_2=e_3=E.}
\]

### (III) 第一、第二块 pair-max

\[
\boxed{e_1=e_2=E>e_3.}
\]

没有其他五进赋值形状。

---

# 5. 前缀 pair-max 自动产生深 Hensel `-1` 锁

考虑情形 (III)：

\[
e_1=e_2=E>e_3=e,
\qquad
 d=E-e>0.
\]

则

\[
y_1,y_2\text{ 是 5 进单位},
\qquad
v_5(y_3)=d.
\]

记

\[
\boxed{L_0=\ell-e_3>0.}
\]

由 `U=LA`：

\[
\boxed{v_5(U)\ge L_0.}
\tag{6}
\]

又

\[
H=y_3+U,
\]

所以

\[
v_5(H)\ge\min(d,L_0).
\]

同样

\[
H+y_3=2y_3+U
\]

满足

\[
\boxed{
v_5(H+y_3)\ge\min(d,L_0).
}
\tag{7}
\]

球面 gap：

\[
y_1^2+y_2^2=U(H+y_3).
\]

由 (6)–(7)：

\[
\boxed{
v_5(y_1^2+y_2^2)
\ge L_0+\min(d,L_0).}
\tag{8}
\]

因为 `y_1,y_2` 都是 5 进单位，可以除以 `y_2^2`，得到

\[
\boxed{
\left(\frac{y_1}{y_2}\right)^2
\equiv-1
\pmod{5^{L_0+\min(d,L_0)}}.
}
\tag{9}
\]

所以 prefix pair-max 的五进 unsaturated 通道必须实现一个随 `\ell-e_3` 增长的深 Hensel root `\sqrt{-1}`。

---

# 6. 三块全相等也产生 Hensel 锁

若

\[
e_1=e_2=e_3=E<\ell,
\]

则 `y_1,y_2,y_3` 都是 5 进单位。

由 `v_5(U)\ge L_0=\ell-E>0`：

\[
H\equiv y_3\not\equiv0\pmod5.
\]

因此

\[
H+y_3
\]

是 5 进单位。

所以

\[
v_5(y_1^2+y_2^2)
=v_5(U)
\ge L_0.
\]

从而

\[
\boxed{
\left(\frac{y_1}{y_2}\right)^2
\equiv-1
\pmod{5^{\ell-E}}.
}
\tag{10}
\]

---

# 7. 第三块 unique-max

若

\[
e_3=E>e_1=e_2=e,
\qquad E<\ell,
\]

则 `y_3,H` 都是 5 进单位，而 `y_1,y_2` 都含至少一个因子 `5`。

由 `5\mid U`：

\[
H\equiv y_3\pmod5,
\]

所以

\[
H+y_3
\]

是 5 进单位。

因此

\[
\boxed{
v_5(U)=v_5(y_1^2+y_2^2).}
\tag{11}
\]

并且

\[
\boxed{
v_5(y_1^2+y_2^2)\ge\ell-E.}
\tag{12}
\]

写

\[
r=\min(v_5(y_1),v_5(y_2)),
\]

则若 `\ell-E>2r`，约去共同的 `5^{2r}` 后，剩余 unit pair 还必须满足一个额外深度

\[
\boxed{5^{\ell-E-2r}}
\]

的 `-1` Hensel congruence。

---

# 8. 五进通道的最终安全分流

A1 任意候选在素数 `5` 上满足：

### 5-saturated

\[
\boxed{e_3\ge\ell.}
\]

或

### 5-unsaturated

\[
\boxed{e_3<\ell,}
\]

且最大赋值形状只能是：

\[
\boxed{
\text{third unique max},
\quad
\text{triple tie},
\quad
\text{prefix pair-max}.}
\]

其中后两种自动携带 (9)、(10) 的深 `\sqrt{-1}` Hensel 锁，第三 unique-max 在 excess 足够大时也携带相应锁。

这与二进 dichotomy 一起，把第三尾的两个十进制素数通道都改写成安全整数球面语言。