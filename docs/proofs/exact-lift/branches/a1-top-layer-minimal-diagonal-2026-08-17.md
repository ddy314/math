# A1 top-layer minimal-surplus diagonal kernel — 2026-08-17

本文研究最高层最小双 surplus

\[
r=s=1,
\qquad g\ge1
\]

中的 diagonal 区域

\[
\boxed{k=g.}
\]

在这一条线上，自然 carrier-gap 尺度恰好退化成常数 `10`。结合 half-gap shell，可把真实 rational gap 的整数部分完全锁死为 `5`，进而得到一个新的十进制余量参数 `j`。

核心结论（`k\ge2`）：

\[
\boxed{
U_1=(5-z)10^{k+1}+j,
\qquad
0\le j<\frac{17}{5}10^k,
}
\]

以及

\[
\boxed{
x=(5-z-w)10^{k+1}+j.}
\]

本文结论均为 **已严格完成**；`k=g=1` 保留为明确有限的小尺度例外。

---

## 1. diagonal 基本形状

`r=s=1` 已给出

\[
b_1=10^{2k+1}-w,
\]

\[
a_2=10^{2k+1}-z,
\]

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

当

\[
g=k
\]

时

\[
m_2=k-g+1=1,
\]

故

\[
\boxed{b_2=1.}
\tag{1}
\]

共同十进制中心为

\[
\boxed{M=10^{2k+1}.}
\]

自然 gap 尺度变成

\[
\boxed{
H_0=10^{g+1-k}=10.
}
\tag{2}
\]

---

## 2. half-gap shell 直接锁死 gap 的整数部分

令

\[
D_0=10^kr_1-r_2.
\]

half-gap sharpening 给出

\[
\frac12
<\frac{D_0}{10}
<\frac{267}{500}.
\]

所以

\[
\boxed{
5<D_0<\frac{267}{50}=5.34.
}
\tag{3}
\]

由于 `b_2=1`，residue kernel 给出

\[
D_0
=10^k\frac{U_1}{b_1}+U_2.
\]

而 `s=1,y=0` 时

\[
U_2=z.
\]

故

\[
\boxed{
D_0
=10^k\frac{U_1}{b_1}+z.
}
\tag{4}
\]

又 determinant

\[
\Delta=10^kb_2U_1+b_1U_2
\]

在这里化为

\[
\boxed{
\Delta=10^kU_1+b_1z.
}
\tag{5}
\]

并且

\[
D_0=\frac\Delta{b_1}.
\]

由 (3)：

\[
5b_1<\Delta<\frac{267}{50}b_1.
\]

因此存在唯一正整数 `J` 使

\[
\boxed{
\Delta=5b_1+J,
\qquad
0<J<\frac{17}{50}b_1.
}
\tag{6}
\]

---

## 3. `J` 的十进制同余

把 (5) 代入 (6)：

\[
10^kU_1+b_1z
=5b_1+J.
\]

于是

\[
\boxed{
J=10^kU_1-(5-z)b_1.
}
\tag{7}
\]

令

\[
c=5-z.
\]

因为

\[
z\in\{1,3\},
\]

所以

\[
\boxed{c\in\{4,2\}.}
\tag{8}
\]

再代入

\[
b_1=10^{2k+1}-w:
\]

\[
J
=10^kU_1-c10^{2k+1}+cw.
\]

因此

\[
\boxed{
J=cw+10^k
\left(U_1-c10^{k+1}\right).
}
\tag{9}
\]

---

## 4. `k\ge2` 时得到新的非负整数 `j`

定义

\[
\boxed{
j=U_1-c10^{k+1}.}
\tag{10}
\]

则 (9) 为

\[
\boxed{J=cw+10^kj.}
\tag{11}
\]

六类型中

\[
cw\le4\cdot4=16.
\]

若

\[
k\ge2,
\]

则

\[
cw<10^k.
\]

因为 `J>0` 且 `J\equiv cw\pmod{10^k}`，其最小正代表就是 `cw`，所以

\[
\boxed{j\ge0.}
\tag{12}
\]

由 (6)：

\[
10^kj
<J
<\frac{17}{50}b_1
<\frac{17}{50}10^{2k+1}.
\]

故

\[
\boxed{
0\le j<\frac{17}{5}10^k.
}
\tag{13}
\]

所以

\[
\boxed{
U_1=c10^{k+1}+j
=(5-z)10^{k+1}+j.
}
\tag{14}
\]

---

## 5. 第一分子 offset `x` 也得到块分解

在 diagonal 中 `g=k`，且 `r=1`，所以

\[
U_1=x+10^{k+1}w.
\]

结合 (14)：

\[
x+10^{k+1}w
=(5-z)10^{k+1}+j.
\]

因此

\[
\boxed{
 x=(5-z-w)10^{k+1}+j.
}
\tag{15}
\]

六类型中 `5-z-w` 总是非负：

| `z` | `w` | `5-z-w` |
|---:|---:|---:|
| 1 | 1 | 3 |
| 1 | 2 | 2 |
| 1 | 3 | 1 |
| 1 | 4 | 0 |
| 3 | 1 | 1 |
| 3 | 2 | 0 |

所以 diagonal 第一分子 offset 只允许六个固定主块，外加

\[
0\le j<0.34\cdot10^{k+1}.
\]

---

## 6. 原四整数在 diagonal 中的最终形状

对 `k=g\ge2`、`r=s=1`，六类型统一写成

\[
\boxed{
b_1=10^{2k+1}-w,}
\]

\[
\boxed{b_2=1,}
\]

\[
\boxed{a_2=10^{2k+1}-z,}
\]

\[
\boxed{
 a_1
=10^{3k+2}
+(5-z-w)10^{k+1}
+j,
}
\]

其中

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\},
\]

\[
\boxed{0\le j<\frac{17}{5}10^k.}
\]

因此 diagonal 边界已经从两个长整数自由度降为：

- 一个整数 `k\ge2`；
- 6 个绝对类型；
- 一个只有 `k+1` 位尺度、且前 `~70%` 区间被删除的余量 `j`。

---

## 7. `k=g=1` 小尺度例外

当

\[
k=g=1,
\]

有

\[
10^k=10,
\]

而某些类型的 `cw` 可达到 `12` 或 `16`，因此从 `J>0` 不能自动推出本文定义的 `j\ge0`。

这是一个**明确有限的单个 `(k,g)` 切片**，应单独做精确有限检查；它不影响 `k=g\ge2` 的无界 diagonal reduction。

---

## 8. 后续接口

在 diagonal 中第三分母正规化还有额外简化。令

\[
\sigma=\frac{b_3}{10^{m_3}}
\in[0.1,1).
\]

因为 `g=k`，有

\[
\boxed{
\frac\theta\lambda
=\frac\rho{10^k}
=\sigma.
}
\]

所以 positive excess decomposition 中 prefix-contact 与 third-contact 两个 source 只差一个第三分母 significand `sigma`。

下一步应把 `(k;z,w;j;\sigma)` 代回 excess decomposition 与 safe integer-gap identity，优先关闭 `k\ge2` diagonal；`k=1` 则作为有限切片独立核验。
