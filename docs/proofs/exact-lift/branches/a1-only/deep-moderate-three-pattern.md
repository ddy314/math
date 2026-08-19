# A1 minimal diagonal: moderate double-deep three-pattern collapse

> 日期：2026-08-20。依赖 `deep-moderate-factorization.md` 与 `deep-balanced-collapse.md`。当前范围 `k=g>=31`。

`deep-moderate-factorization.md` 已在

\[
A,B>0,
\qquad
A,B\le2k+3
\]

中构造绝对有限整数

\[
196000<r<15214000,
\]

以及 factor pair

\[
X_1=sa,
\qquad
X_2=qb,
\qquad
ab=Dr,
\]

其中

\[
X_1=10\gamma T-wDN_0,
\]

\[
X_2=100\gamma T-(10w-1)DN_0.
\]

并且

\[
v_2(r)\le23,
\qquad
v_5(r)\le10.
\]

本文证明此前暂留的 2-adic / 5-adic transition strips 实际在 `k>=31` 全部为空。于是 moderate double-deep 只剩三个显式模板：low-low、low-high、high-low。

状态：**已严格完成。**

---

## 1. 5-adic transition `B+nu5=k+1` 不可能

记

\[
\nu_5=v_5(N_0),
\qquad
Y=B+\nu_5.
\]

若

\[
Y=k+1,
\]

则在 `X_1` 中两项的 5-adic valuation 都等于 `k+1`，因此

\[
v_5(X_1)\ge k+1.
\]

在 `X_2` 中两项赋值分别为 `k+2` 与 `k+1`，所以严格由后者承担：

\[
v_5(X_2)=k+1.
\]

由 `ab=Dr` 且 `q,s` 与 5 互素：

\[
v_5(X_1)+v_5(X_2)=B+v_5(r).
\]

因此

\[
B+v_5(r)\ge2k+2.
\]

但

\[
B=k+1-\nu_5,
\qquad
v_5(r)\le10,
\]

故右侧又满足

\[
B+v_5(r)\le k+11.
\]

当前 `k>=31` 时

\[
2k+2>k+11,
\]

矛盾。所以

\[
\boxed{B+\nu_5\ne k+1.}
\tag{1}
\]

---

## 2. 5-adic transition `B+nu5=k+2` 也不可能

若

\[
Y=k+2,
\]

则 `X_1` 中两项赋值为 `k+1` 与 `k+2`，故

\[
v_5(X_1)=k+1.
\]

而 `X_2` 两项均为 `k+2`，所以

\[
v_5(X_2)\ge k+2.
\]

于是

\[
B+v_5(r)\ge2k+3.
\]

另一方面

\[
B=k+2-\nu_5,
\]

故

\[
B+v_5(r)\le k+12.
\]

对 `k>=31`：

\[
2k+3>k+12,
\]

矛盾。因此

\[
\boxed{B+\nu_5\ne k+2.}
\tag{2}
\]

所以 5-adic transition strip 完全消失。

---

## 3. 2-adic transition strip整体不可能

记

\[
\nu_2=v_2(N_0),
\qquad
X=A+\nu_2,
\qquad
e=v_2(w)\in\{0,1,2\}.
\]

此前 transition strip 为

\[
\boxed{k+1-e\le X\le k+2.}
\tag{3}
\]

在 `X_1` 中两项赋值为

\[
k+1,\qquad X+e.
\]

由 (3)，二者最小值至少为 `k+1`，所以

\[
v_2(X_1)\ge k+1.
\]

在 `X_2` 中两项赋值为

\[
k+2,\qquad X,
\]

故

\[
v_2(X_2)\ge X\ge k+1-e.
\]

于是

\[
v_2(X_1)+v_2(X_2)
\ge2k+2-e.
\tag{4}
\]

但 `ab=Dr` 给

\[
v_2(X_1)+v_2(X_2)
=A+v_2(r).
\]

而 transition 中 `A<=X<=k+2`，再用 `v_2(r)<=23`：

\[
A+v_2(r)\le k+25.
\tag{5}
\]

对 `k>=31`、`e<=2`：

\[
2k+2-e\ge2k
>k+25.
\]

(4)-(5) 矛盾。因此

\[
\boxed{
 k+1-e\le A+\nu_2\le k+2
 \Longrightarrow\bot.
}
\tag{6}

所以 2-adic transition strip 也完全消失。

---

## 4. 两个素数侧现在都只有 low / high 两态

由 `deep-moderate-factorization.md` 的 valuation dichotomy，再结合 §§1–3：

### 2-adic low

\[
\boxed{
A+2\nu_2+e=v_2(r)\le23.
}
\tag{7}

### 2-adic high

\[
\boxed{
A=2k+3-v_2(r).
}
\tag{8}

### 5-adic low

\[
\boxed{
B+2\nu_5=v_5(r)\le10.
}
\tag{9}

### 5-adic high

\[
\boxed{
B=2k+3-v_5(r).
}
\tag{10}

不存在第三种 transition 状态。

---

## 5. high-high 被 fully-balanced collapse 排除

若 2、5 两侧同时 high，则由 (8)、(10)：

\[
A+e+\nu_2>k,
\qquad
B+\nu_5>k.
\]

这正落入 `deep-balanced-collapse.md` 已排除的 fully-balanced double-deep 区域。因此

\[
\boxed{\text{high-high impossible}.}
\tag{11}

所以 moderate double-deep 只剩三种模板。

---

## 6. 最终 three-pattern normal form

任意 moderate double-deep candidate 必须属于且只可能属于以下三类之一。

### LL: low-low

\[
\boxed{
A+2\nu_2+e=v_2(r),
\qquad
B+2\nu_5=v_5(r).
}
\tag{12}

特别地

\[
A\le23,
\qquad B\le10.
\]

### LH: 2-low / 5-high

\[
\boxed{
A+2\nu_2+e=v_2(r),
\qquad
B=2k+3-v_5(r).
}
\tag{13}

因此 `A<=23`，而 `B` 被 `k` 与有限参数 `v_5(r)` 精确锁定。

### HL: 2-high / 5-low

\[
\boxed{
A=2k+3-v_2(r),
\qquad
B+2\nu_5=v_5(r).
}
\tag{14}

因此 `B<=10`，而 `A` 被 `k` 与有限参数 `v_2(r)` 精确锁定。

综上：

\[
\boxed{
\text{moderate double-deep}
=\text{LL}\cup\text{LH}\cup\text{HL},
}
\tag{15}

其中

\[
196000<r<15214000.
\]

原来的二维 `(A,B)` 自由度已经完全消失。

---

## 7. high branch 上 factor pair 的巨大素数幂被精确分配

这个 three-pattern 还有一个直接可用的加强。

### LH

由 `B=2k+3-v_5(r)`，总 5-adic exponent 为

\[
B+v_5(r)=2k+3.
\]

而 high branch 中

\[
v_5(X_1)=k+1,
\qquad
v_5(X_2)=k+2.
\]

所以若写

\[
r=5^{v_5(r)}r_5,
\qquad 5\nmid r_5,
\]

则

\[
\boxed{
a=5^{k+1}a_0,}
\qquad
\boxed{b=5^{k+2}b_0,}
\]

并且

\[
\boxed{a_0b_0=2^A r_5.}
\tag{16}

右侧是绝对有界对象，因为 `A<=23`、`r<15214000`。

### HL

完全对称。写

\[
r=2^{v_2(r)}r_2,
\qquad 2\nmid r_2.
\]

则

\[
\boxed{a=2^{k+1}a_0,}
\qquad
\boxed{b=2^{k+2}b_0,}
\]

且

\[
\boxed{a_0b_0=5^B r_2.}
\tag{17}

这里 `B<=10`，所以右侧同样绝对有界。

这意味着 LH / HL 并不只是“一侧指数线性锁定”：除去显式的 `5^{k+1},5^{k+2}` 或 `2^{k+1},2^{k+2}` 后，两个 factor 的剩余 quotient 已经来自绝对有限 divisor set。

下一步应优先利用 (16)-(17) 与 `s|b_1,q|Q` 做 resultant / modular exhaustion。