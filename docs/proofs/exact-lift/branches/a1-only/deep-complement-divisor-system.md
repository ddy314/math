# A1 minimal diagonal: complementary quadratic-divisor system

> 日期：2026-08-20。依赖 `deep-four-factor-frame.md`。当前范围 `k=g>=31`。

本文把 complementary linear relation

\[
\bar s b-\bar q a=10\lambda T
\]

与

\[
\bar s\mid b_1,
\qquad
\bar q\mid Q
\]

直接联立，得到一对互相嵌套的二次整除条件。

在 double-deep 中 `lambda=1`，它尤其适合 moderate LL：此时 `a,b` 来自绝对有限集合，因此问题变成 fixed-coefficient simultaneous quadratic-divisor system。

状态：**整除正规形严格完成；Vieta-jumping / descent 方向仍待证。**

---

## 1. 记号

令

\[
\boxed{u:=\bar s=b_1/s,}
\qquad
\boxed{v:=\bar q=Q/q.}
\]

four-factor frame 给

\[
\boxed{bu-av=10\lambda T.}
\tag{1}

又

\[
b_1=10T^2-w,
\qquad
Q=100T^2-(10w-1).
\tag{2}

---

## 2. `u` 侧二次整除

由 (1)：

\[
100\lambda^2T^2=(bu-av)^2.
\]

把 `10b_1=100T^2-10w` 乘上 `lambda^2`：

\[
10\lambda^2b_1
=(bu-av)^2-10w\lambda^2.
\]

因为

\[
u\mid b_1,
\]

左侧被 `u` 整除。右侧模 `u` 只剩

\[
a^2v^2-10w\lambda^2.
\]

因此

\[
\boxed{
u\mid a^2v^2-10w\lambda^2.}
\tag{3}

---

## 3. `v` 侧二次整除

由 (1)：

\[
100\lambda^2T^2=(bu-av)^2.
\]

而

\[
\lambda^2Q
=100\lambda^2T^2-(10w-1)\lambda^2.
\]

所以

\[
\lambda^2Q
=(bu-av)^2-(10w-1)\lambda^2.
\]

因为

\[
v\mid Q,
\]

模 `v` 得

\[
\boxed{
v\mid b^2u^2-(10w-1)\lambda^2.}
\tag{4}

---

## 4. double-deep 专门化

在 double-deep 中

\[
\lambda=1.
\]

于是 (1),(3),(4) 变成

\[
\boxed{bu-av=10T,}
\tag{5}

\[
\boxed{
u\mid a^2v^2-10w,}
\tag{6}

\[
\boxed{
v\mid b^2u^2-(10w-1).}
\tag{7}

这已经完全不含 `N_0,gamma,D`。

所以所有 double-deep candidate 都必须在 complementary divisor plane `(u,v)` 上满足一对固定形状的 quadratic divisibilities；`D,N_0,gamma` 只在其他方程中负责进一步筛选。

---

## 5. moderate LL 的 fixed-coefficient 版本

LL 中

\[
A\le23,
\qquad
B\le10,
\qquad
196000<r<15214000,
\]

而 `deep-moderate-factor-quotients.md` 给出

\[
\alpha\beta=r_{10}
\]

以及显式 `a,b`。因此对每个固定

\[
(w,r,A,B,\nu_2,\nu_5,\alpha,\beta)
\]

，`a,b` 都是固定正整数。

此时 LL 剩余的 unbounded `k` 必须产生正整数 `u,v` 满足

\[
\boxed{
\begin{aligned}
&bu-av=10^{k+1},\\
&u\mid a^2v^2-10w,\\
&v\mid b^2u^2-(10w-1).
\end{aligned}}
\tag{8}

这是一套 fixed-coefficient simultaneous quadratic-divisor system。

它已经与原来的 `Q,b_1` 完整 factorization 解耦：不需要先 factor `10^{2k+2}-(10w-1)` 或 `10^{2k+1}-w` 才能陈述必要条件。

---

## 6. quotient variables

可进一步定义整数

\[
\boxed{m:=\frac{a^2v^2-10w}{u},}
\]

\[
\boxed{n:=\frac{b^2u^2-(10w-1)}{v}.}
\]

由 (8)，`u,v,m,n` 全为正整数（当前 `u,v` 巨大，所以 numerator 为正）。

后续可能的 Vieta-jumping / descent 目标是研究 `(u,v)` 与 `(m,n)` 的 size direction 和 involution；本文暂不把该方向误写成已经证明的无限下降。

---

## 7. 当前用途

这套 system 对 LL 最直接，因为 `a,b` 固定；对 LH/HL 虽然 `a,b` 含显式 `2^k/5^k`，仍可先除去 `deep-moderate-factor-quotients.md` 中已知的大 prime powers，再得到相应的 scaled quadratic divisibility。

因此后续可以并行尝试：

1. LL：Vieta-jumping / minimal-solution descent；
2. LH/HL：先 strip 大 `2/5` powers，再做 periodic congruence；
3. 与 `deep-moderate-root-normal-form.md` 的 square-root branch 同时使用。