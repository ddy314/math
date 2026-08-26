# A1 minimal diagonal: coefficient-sensitive complement source minima

> 日期：2026-08-26。依赖 `deep-2high-normalized-complement-shell.md` 中的 cross-coprimality，以及 strict-2 Q-side orientation。当前统一 frontier 为 `k>=32`。
>
> 本文适用于全部 surviving double-deep 2-high / 5-low master states；其中 `w=2` 的 `u`-side sharpen 也只用 master whole-block selector，因此同样覆盖 moderate HL 与原 2-extreme `E_2`。

最新 normalized complement shell 给出

\[
\boxed{\gcd(\alpha,u)=1,\qquad \gcd(\beta,v)=1.}
\tag{1}
\]

另一方面 strict-2 orientation 对全部 surviving 2-high master 给出

\[
\boxed{v\equiv3\pmod4.}
\tag{2}
\]

本文把 (1)-(2) 与 decimal source prime 的短周期结构联立。核心效果是：如果一个小的 `3 mod 4` source prime 已经进入 coefficient `beta`，它就不能再承担 `v` 的负模四来源；于是 `v` 必须跳到下一个可由 `Q` 提供的 source prime。`w=2` 的 `u` 侧也有完全平行的现象。

状态：**严格完成；得到 coefficient-sensitive complement minima 与 denominator caps，但本结果本身不关闭 full 2-high master。**

---

## 1. Q-side source prime 集

记

\[
Q_w(k)=10^{2k+2}-(10w-1).
\]

对固定 `w` 定义

\[
\boxed{
\mathcal P_Q(w):=
\left\{
 p:\ p\text{ prime},\ p\equiv3\pmod4,\ p\nmid10,
\ \exists k\ge0\text{ 使 }p\mid Q_w(k)
\right\}.}
\tag{3}
\]

对任意 odd prime `p`，条件 `p|Q_w(k)` 只依赖

\[
k\pmod{\operatorname{ord}_p(10)},
\]

所以 membership in `P_Q(w)` 是一个有限 residue-cycle 检查。

直接逐 prime 检查得到各类型最前面的 source primes：

\[
\boxed{
\begin{array}{c|l}
w&\mathcal P_Q(w)\text{ 的起始部分}\\ \hline
1&7,19,23,31,43,47,59,67,71,83,103,107,\ldots\\
2&3,31,59,67,71,107,127,151,167,179,211,223,\ldots\\
3&7,23,59,67,71,83,107,151,167,179,199,223,\ldots\\
4&7,19,23,31,67,107,131,151,163,179,191,223,\ldots
\end{array}}
\tag{4}
\]

附带脚本 `check_a1_deep_2high_coefficient_source_minima.py` 对这些起始段做 exact residue-cycle audit。

---

## 2. cross-coprimality 强迫 coefficient-sensitive `v` 下界

由于 `Q` 为奇数，`v|Q` 也是奇数。由 (2)，`v` 的 prime-power factorization 中必存在某个

\[
p\equiv3\pmod4
\]

以奇指数出现。

该 `p` 满足

\[
p\mid v\mid Q_w(k),
\]

所以

\[
p\in\mathcal P_Q(w).
\]

又由 (1)：

\[
p\nmid\beta.
\]

因此定义

\[
\boxed{
P_Q(w,\beta)
:=\min\{p\in\mathcal P_Q(w):p\nmid\beta\}.}
\tag{5}
\]

对任意实际 candidate，集合非空，因为上面从 `v` 本身已经构造出至少一个元素。于是

\[
\boxed{v\ge P_Q(w,\beta).}
\tag{6}
\]

这是一个真正依赖 finite coefficient `beta` 的 complement lower bound。

特别地：

\[
\boxed{w=2,\ 3\mid\beta\Longrightarrow v\ge31.}
\tag{7}
\]

因为 `w=2` 时最小 Q-source 是 3，而下一个已经是 31。相比旧 structural bound `v>=3`，这里一次跳过了 `7,11,19,23`。

其余立即例子：

\[
\boxed{w=3,\ 7\mid\beta\Longrightarrow v\ge23,}
\tag{8}
\]

\[
\boxed{w=4,\ 7\mid\beta\Longrightarrow v\ge19,}
\tag{9}
\]

\[
\boxed{w=4,\ 7\cdot19\mid\beta\Longrightarrow v\ge23.}
\tag{10}
\]

对 `w=1`：

\[
\boxed{7\cdot19\cdot23\mid\beta\Longrightarrow v\ge31.}
\tag{11}
\]

---

## 3. `w=2` 的 u-side source prime 集

`w=2` 时

\[
b_1(k)=10^{2k+1}-2.
\]

已有

\[
v_2(b_1)=1,
\qquad s\equiv1\pmod4,
\]

而 `s` 只由 odd `1 mod 4` whole blocks 构成。因此

\[
v_2(u)=1,
\qquad
\frac u2\equiv3\pmod4.
\tag{12}
\]

所以 `u/2` 中至少有一个 `3 mod 4` prime 以奇指数出现。

定义

\[
\boxed{
\mathcal P_b(2):=
\left\{
 p:\ p\text{ prime},\ p\equiv3\pmod4,\ p\nmid10,
\ \exists k\ge0\text{ 使 }p\mid b_1(k)
\right\}.}
\tag{13}
\]

exact residue-cycle 检查给

\[
\boxed{
\mathcal P_b(2)=
19,31,59,71,131,151,179,191,199,251,311,359,\ldots}
\tag{14}
\]

的起始部分。

由 `gcd(alpha,u)=1`，承担 (12) 的 prime 不能整除 `alpha`。定义

\[
\boxed{
P_b(\alpha):=
\min\{p\in\mathcal P_b(2):p\nmid\alpha\}.}
\tag{15}
\]

则

\[
\boxed{w=2:\quad u\ge2P_b(\alpha).}
\tag{16}
\]

特别地：

\[
\boxed{19\mid\alpha\Longrightarrow u\ge62.}
\tag{17}
\]

若 `19*31|alpha`，则进一步有

\[
\boxed{u\ge118.}
\tag{18}
\]

---

## 4. coefficient-sensitive complement product

记

\[
M=uv.
\]

结合已有的 `w=1` joint minimum `M>=621` 与 mandatory `u` minima，可统一写成：

\[
\boxed{
M\ge
\begin{cases}
\max\{621,\ 27P_Q(1,\beta)\},&w=1,\\[2mm]
2P_b(\alpha)P_Q(2,\beta),&w=2,\\[2mm]
P_Q(3,\beta),&w=3,\\[2mm]
12P_Q(4,\beta),&w=4.
\end{cases}}
\tag{19}
\]

这里每一项都只依赖 finite coefficient `(alpha,beta)` 与固定 decimal type `w`。

因此 complement height

\[
\mu=\frac{MD}{T^2}<10001
\]

立即给出 signature-dependent denominator cap

\[
\boxed{
\frac D{T^2}<\frac{10001}{M_{\min}(w,\alpha,\beta)}.}
\tag{20}
\]

这比只按 `w` 使用一个统一常数更精细。

---

## 5. 几个强的显式子族

### 5.1 `w=2, 3|beta`

由 (7) 与 baseline `P_b>=19`：

\[
M\ge2\cdot19\cdot31=1178.
\]

所以

\[
\boxed{
\frac D{T^2}<\frac{10001}{1178}<9.}
\tag{21}
\]

这是 `w=2` 中一个很大的 coefficient subfamily：一旦 3-primary block 分到 `beta`，旧 `M>=114` 立即提高十倍以上。

### 5.2 `w=2, 19|alpha`

由 (17) 与 `v>=3`：

\[
M\ge62\cdot3=186,
\]

故

\[
\boxed{
\frac D{T^2}<\frac{10001}{186}<54.}
\tag{22}
\]

若同时 `3|beta`：

\[
M\ge62\cdot31=1922,
\]

从而

\[
\boxed{
\frac D{T^2}<\frac{10001}{1922}<6.}
\tag{23}
\]

### 5.3 `w=3, 7|beta`

\[
M\ge23,
\qquad
\boxed{D/T^2<10001/23<435.}
\tag{24}
\]

### 5.4 `w=4, 7|beta`

\[
M\ge12\cdot19=228,
\qquad
\boxed{D/T^2<10001/228<44.}
\tag{25}
\]

若 `7*19|beta`：

\[
M\ge12\cdot23=276,
\qquad
\boxed{D/T^2<10001/276<37.}
\tag{26}
\]

### 5.5 `w=1, 7*19*23|beta`

由 (11)：

\[
27P_Q(1,\beta)\ge27\cdot31=837>621,
\]

所以

\[
\boxed{M\ge837,\qquad D/T^2<10001/837<12.}
\tag{27}
\]

---

## 6. 与 normalized R-shell 的接口

normalized shell 已把任何 candidate 写成

\[
R\equiv x_{\alpha,\beta}5^d\pmod{4r_{10}},
\qquad
3780<\frac R{5^d}<78015,
\]

并在 moderate HL 中把 `(w,Y,alpha,beta)` 化成 finite coefficient data。

本文说明：在进入 `(d,R)` periodic cover 前，可以先从同一 `(alpha,beta)` 读出一个更强的 `M_min`，再通过 (20) 收紧允许的 denominator/excess 区域。尤其 `w=2` 的 `3|beta`、`19|alpha` 两类会得到数量级明显更强的 pure-2 extreme cap。

因此后续 certificate 推荐按

\[
\boxed{(w,Y,\alpha,\beta,M_{\min},m)}
\]

组织，而不只按 `(w,Y,alpha,beta,m)`；`M_min` 可由很短的 source-prime list 精确计算。

---

## 7. 依赖审计

本文没有把 source-prime 条件当成独立于 cross-coprimality 的第二个随机筛。逻辑链只有：

1. strict-2 orientation 强迫 `v=3 mod 4`；
2. whole-block orientation 在 `w=2` 强迫 `u/2=3 mod 4`；
3. normalized shell 的 cross-coprimality 禁止 coefficient prime 再进入对应 complement；
4. decimal congruence只负责列出“某个 prime 是否可能成为该侧 source”。

所以 (19)-(27) 都是现有 master skeleton 的严格推论，没有重复计数 Hensel/contact-square obstruction。