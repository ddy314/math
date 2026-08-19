# A1 minimal diagonal: extreme height collapse

> 日期：2026-08-20。依赖 `deep-extreme-classification.md` 与 `deep-complement-height.md`。当前范围 `k=g>=31`。

`deep-extreme-classification.md` 已证明 extreme double-deep 只能是一侧 extreme、另一侧 shallow-low。本文把 complement-height inequality 代入，得到：

\[
\boxed{\text{5-extreme 完全为空}.}
\]

因此 double-deep 的 extreme 部分只剩 2-extreme；其 5-adic shallow height 还满足统一线性上界

\[
\boxed{B+\nu_5<7+0.570k.}
\]

状态：**已严格完成。**

---

## 1. 5-extreme 的结构

若 5-extreme，则

\[
B\ge2k+4.
\]

由 `deep-extreme-classification.md`，balanced collapse 强迫

\[
\boxed{A+e+\nu_2<k,}
\tag{1}

其中

\[
e=v_2(w),
\qquad\nu_2=v_2(N_0).
\]

同时 `deep-complement-height.md` 已证明

\[
B+\nu_5<3k,
\]

所以两个 cancellation exponents 都未达到 `3k`，可以直接使用未饱和 height inequality：

\[
\boxed{
2^{A+e+\nu_2}5^{B+\nu_5}
<390100\,10^k.
}
\tag{2}

---

## 2. 5-extreme 立即与 height inequality 矛盾

左侧最小也满足

\[
2^{A+e+\nu_2}5^{B+\nu_5}
\ge5^{2k+4}.
\]

因此 (2) 要求

\[
5^{2k+4}
<390100\,2^k5^k.
\]

约去 `5^k`：

\[
625\left(\frac52\right)^k<390100.
\tag{3}

但在 `k=31` 已有

\[
625(5/2)^{31}>10^{15}>390100,
\]

以后只会更大。矛盾。

故

\[
\boxed{
B\ge2k+4
\Longrightarrow\bot.
}
\tag{4}

所以 5-extreme double-deep 完全为空。

---

## 3. 2-extreme 的 5-side 统一高度界

现在唯一可能的 extreme branch 是

\[
A=2k+3+E,
\qquad E\ge1.
\]

balanced collapse 强迫

\[
\boxed{Y:=B+\nu_5<k.}
\tag{5}

### 3.1 若 2-side 未达到 `3k`

设

\[
A+e+\nu_2<3k.
\]

height inequality 为

\[
2^{2k+3+E+e+\nu_2}5^Y
<390100\,2^k5^k.
\]

所以

\[
5^Y
<390100\,
\frac{5^k}{2^{k+3+E+e+\nu_2}}.
\]

因为

\[
390100<5^8,
\qquad
2>5^{0.430},
\]

得到安全粗化

\[
Y
<k+8-0.430(k+3+E+e+\nu_2)
<7+0.570k.
\tag{6}

### 3.2 若 2-side 达到 `3k`

若

\[
A+e+\nu_2\ge3k,
\]

`deep-complement-height.md` 已给更强结论

\[
\boxed{Y<8+0.139k.}
\tag{7}

对 `k>=31`，(7) 显然蕴含更弱统一界 (6)。

所以全部 2-extreme candidate 都满足

\[
\boxed{
B+\nu_5<7+0.570k.
}
\tag{8}

---

## 4. 2-extreme 的 factor valuation

`deep-extreme-classification.md` 还给

\[
v_2(t)=2k+3,
\]

而 5-side shallow-low 给

\[
v_5(t)=2B+2\nu_5.
\]

因此可写

\[
\boxed{
t=
2^{2k+3}
5^{2B+2\nu_5}
r_{10},
\qquad\gcd(r_{10},10)=1.}
\tag{9}

又

\[
D=2^{2k+3+E}5^B,
\]

所以 renormalized bounded parameter 为

\[
\boxed{
\frac tD
=
\frac{5^{B+2\nu_5}r_{10}}{2^E},
}
\tag{10}

且始终满足

\[
\boxed{
196000
<\frac{5^{B+2\nu_5}r_{10}}{2^E}
<15214000.
}
\tag{11}

因此剩余 extreme branch 已严格变成一个 pure-2 denominator problem；5-side height 由 (8) 控制，而所有非 `2,5` 自由度集中在 odd integer `r_{10}`。

---

## 5. 当前 double-deep 分类进一步缩短

moderate three-pattern 仍为

\[
LL,\quad LH,\quad HL.
\]

extreme 原有 `E_2,E_5` 两支，现在 `E_5` 已由本文排除。因此

\[
\boxed{
\text{double-deep}
=LL\cup LH\cup HL\cup E_2,
}
\tag{12}

其中 `E_2` 是 one-sided 2-extreme / 5-low branch。

下一步对 extreme 只需研究 (10)-(11) 的 pure-2 denominator descent，不再需要 5-extreme 分支。