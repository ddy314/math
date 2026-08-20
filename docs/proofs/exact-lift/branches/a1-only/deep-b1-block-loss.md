# A1 minimal diagonal: strict 2-deep `b_1` block loss

> 日期：2026-08-19。依赖 `deep-q-side-proper-divisor.md` 与 minimal-diagonal odd-prime supply theorem。

strict 2-adic low-side 已知

\[
h=qs,
\qquad q\mid Q,
\]

其中 `s` 只能选择 `b_1` 中 `1 mod 4` 的完整 odd prime-power blocks。

`deep-q-side-proper-divisor.md` 已证明 Q-side 永久损失：

\[
q\le Q/7\quad(w=1,3,4),
\qquad q\le Q/3\quad(w=2).
\]

本文补上 `b_1` 侧的 prefix-uniform block loss，并把两侧合并。

状态：**已严格完成。**

---

## 1. `B_+` 记号

写

\[
b_1=10^{2k+1}-w,
\]

并令

\[
B_+
=
\prod_{p\equiv1(4),\ p^e\Vert b_1}p^e.
\]

odd-prime supply 中

\[
s\le B_+.
\]

任何 `2` 次幂以及所有 `p=3 mod4` prime-power blocks 都不可能进入 `B_+`。

---

## 2. `w=1`：固定因子 `3` 永久丢失

因为

\[
10\equiv1\pmod3,
\]

有

\[
b_1=10^{2k+1}-1\equiv0\pmod3.
\]

而

\[
3\equiv3\pmod4,
\]

所以整个 `3`-power block 都不能进入 `B_+`。至少损失一个因子 `3`：

\[
\boxed{B_+\le b_1/3.}
\tag{1}
\]

---

## 3. `w=2`：`2` 加上至少一个 `>=7` 的 `3 mod 4` odd block

这里

\[
b_1=10^{2k+1}-2.
\]

由于高十进制幂被 `8` 整除，

\[
b_1\equiv6\pmod8,
\]

故

\[
\boxed{v_2(b_1)=1.}
\tag{2}
\]

写 odd part

\[
b_1=2m.
\]

则

\[
m\equiv3\pmod4.
\]

所以 `m` 的素因子分解中至少有一个 `p=3 mod4` 的 prime-power block 以奇次数贡献；否则所有 blocks 的乘积只能是 `1 mod4`。

另一方面

\[
b_1\equiv1-2\equiv2\pmod3,
\]

故 `3` 不整除 `b_1`。因此这个被迫存在的 `3 mod4` odd prime 至少为 `7`。

`B_+` 同时不能使用 factor `2` 与该 odd block，所以

\[
\boxed{B_+\le b_1/(2\cdot7)=b_1/14.}
\tag{3}
\]

---

## 4. `w=3`：本文不虚构额外 loss

此时 `b_1` 为奇数且

\[
b_1\equiv1\pmod4.
\]

这个 residue 本身允许所有 odd prime-power blocks 都来自 `1 mod4` primes，因此没有一个仅凭绝对小模即可强迫的 `3 mod4` block。

所以保留安全粗界

\[
\boxed{B_+\le b_1.}
\tag{4}
\]

---

## 5. `w=4`：固定 `2^2` 与 `3` block 同时丢失

现在

\[
b_1=10^{2k+1}-4.
\]

高十进制幂被 `16` 整除，所以

\[
b_1\equiv12\pmod{16},
\]

从而

\[
\boxed{v_2(b_1)=2.}
\tag{5}
\]

同时模 `3`：

\[
b_1\equiv1-4\equiv0\pmod3.
\]

因此 `B_+` 既不能使用 `2^2`，也不能使用 `3 mod4` 的 factor `3`：

\[
\boxed{B_+\le b_1/(4\cdot3)=b_1/12.}
\tag{6}
\]

---

## 6. 与 Q-side proper-divisor cap 合并

strict 2-deep 中

\[
h=qs,
\qquad s\le B_+.
\]

结合已有

\[
q\le
\begin{cases}
Q/7,&w=1,3,4,\\
Q/3,&w=2,
\end{cases}
\]

得到新的统一表：

\[
\boxed{
\begin{array}{c|c}
w&h\text{ upper bound in strict 2-deep}\\ \hline
1&Qb_1/21\\
2&Qb_1/42\\
3&Qb_1/7\\
4&Qb_1/84
\end{array}}
\tag{7}
\]

这些损失全部来自永久局部结构，与 `k`、具体 factorization、`ell` 无关。

---

## 7. 当前用途

(7) 仍只是常数因子收缩，单独不足以证明 deep sector 为空；但 fixed-layer exponent box 与任何统一 decade estimate 都不应再使用 `QB_+` 或 `Qb_1` 作为 strict 2-deep 的极值。

特别地 even-`w` 的供给损失已经很显著：

\[
w=2:\quad h\le Qb_1/42,
\]

\[
w=4:\quad h\le Qb_1/84.
\]

后续 deep 证明应把这些界与 `A` 的奇偶/resonance、Q-side orientation、5-adic Legendre lock 同时使用。