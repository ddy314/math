# A2 terminal descendant overdepth 的 fixed `-26` fourth-power character

> **依赖：** `spontaneous-crt-descendant-quartic-tail-hierarchy.md`、`spontaneous-crt-descendant-balance-tail.md`。
>
> **严格状态：**finite quartic hierarchy 已证明 exact remainder在四阶终止。本文审计 fully saturated generic equal-parent branch的 terminal coefficient。quartic homogeneous form精确化成 `26[27(X+Y)]^4+[55Y]^4`。因此若前三层已使 lower block严格深于 `4h`，而 actual remainder仍越过 `4h`，则 `-26` 必须是模 `p` 的第四次幂。对 genuine inert prime `p=3 mod4`，第四次幂集合与平方集合相同，故必要条件等价于 `(26/p)=-1`。这给 terminal overdepth一个固定 quadratic-character filter，不依赖尚未完全分解的 degree-192 ordinary resultant。本文没有排除满足该 character的 primes，因此不关闭 A2。

---

## 1. terminal quartic form

finite hierarchy给

\[
M^{(4)}
=s_L^4
\frac{65536\,\mathcal H_4(X,Y)}{5^4 11^4},
\]

其中

\[
\boxed{
\mathcal H_4(X,Y)
=2\cdot3^{12}\cdot13(X+Y)^4
+5^4 11^4Y^4.}
\tag{1.1}
\]

利用

\[
3^{12}=27^4,
\qquad
5^411^4=55^4,
\qquad
2\cdot13=26,
\]
得到 exact compact form

\[
\boxed{
\mathcal H_4(X,Y)
=26[27(X+Y)]^4+[55Y]^4.}
\tag{1.2}
\]

---

## 2. local terminal baseline

固定 genuine same-prime common label，记

\[
h=v_p(G_\Delta)\ge1.
\]

在 generic moving equal-parent branch写

\[
X=p^hX_0,
\qquad
Y=p^hY_0,
\qquad
p\nmid X_0Y_0.
\tag{2.1}
\]

finite hierarchy中前三层若已全部 saturated到使

\[
v_p(M^{(1)}+M^{(2)}+M^{(3)})>4h,
\tag{2.2}
\]
则 quartic block normally独占 `4h` 层。

因此若 actual remainder还满足

\[
\boxed{v_p(M)>4h,}
\tag{2.3}
\]
必要地

\[
\boxed{
\mathcal H_4(X_0,Y_0)\equiv0\pmod p.}
\tag{2.4}
\]

注意若 `X_0+Y_0=0 mod p`，(1.2) 只剩 `[55Y_0]^4`，为 unit，故 (2.4) 不可能。因此 terminal overdepth本身自动排除 parent cancellation `chi=-1`。

---

## 3. `-26` must be a fourth power

由 (1.2),(2.4)，且 `p` 与 `3,5,11,13,Y_0,X_0+Y_0` 分离：

\[
26[27(X_0+Y_0)]^4
\equiv-[55Y_0]^4\pmod p.
\]

所以

\[
\boxed{
\left(
\frac{55Y_0}{27(X_0+Y_0)}
\right)^4
\equiv-26\pmod p.}
\tag{3.1}
\]

因此

\[
\boxed{-26\text{ 是模 }p\text{ 的第四次幂}.}
\tag{3.2}
\]

---

## 4. inert primes: fourth powers equal squares

当前 genuine parity carrier只关心

\[
\boxed{p\equiv3\pmod4.}
\tag{4.1}
\]

此时

\[
p-1=2m_p
\]
且 `m_p` 为奇数。平方子群 `QR_p` 的阶就是奇数 `m_p`。映射

\[
x\mapsto x^2
\]
在奇阶群 `QR_p` 上是 automorphism，所以每个平方都唯一地是某个平方的平方。故

\[
\boxed{
(\mathbf F_p^\times)^4
=(\mathbf F_p^\times)^2.}
\tag{4.2}
\]

因此 (3.2) 等价于

\[
\boxed{
\left(\frac{-26}{p}\right)=1.}
\tag{4.3}
\]

又 `(−1/p)=-1`，于是

\[
\boxed{
\left(\frac{26}{p}\right)=-1.}
\tag{4.4}
\]

这就是 terminal overdepth 的 fixed character filter。

---

## 5. residue classes

`(26/p)` 对 genuine `p\nmid26` 只依赖 `p mod 104`。在 `p=3 mod4` 的 classes中，(4.4) 精确留下

\[
\boxed{
p\equiv
3,7,15,27,31,35,43,47,51,63,71,75
\pmod{104}.}
\tag{5.1}
\]

这里 (5.1) 仅是 character bookkeeping；它不声称这些 classes都实际出现 descendant roots。

---

## 6. role in the finite hierarchy

finite quartic hierarchy已经保证没有 fifth-order transport项。因此 terminal branch只有两种机制：

1. quartic coefficient为 unit：actual depth精确停在 `4h`；
2. quartic coefficient发生 p-adic cancellation：其全部额外 terminal depth由 `C_63^(4)` 读取，并且 prime首先必须满足 fixed character (4.4)。

所以 terminal overdepth已经没有新的 normalized parent ratio自由；它只剩 ordinary terminal tail与 fixed `-26` character。

下一步最值得做的是把该 character与 descendant-only external 的 projective carrier / prime-source character交叉，或者审计 `C_63^(4)` 与 `G_Delta` 的 common gcd高度。

A2 仍为 `待证`。
