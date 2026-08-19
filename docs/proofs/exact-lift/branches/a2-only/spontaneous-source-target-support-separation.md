# A2 source common gcd 与 equal-depth target pool 的 complete support separation

> **依赖：** `spontaneous-source-parity-common-gcd.md`、`spontaneous-source-parity-decimal-square-gate.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-content-oversaturation.md`。
>
> **严格状态：**source common gcd 的 genuine prime必须进入 linear sheet `18K-55`；equal-depth omega-height target baseline必须进入 quadratic `P=6K^2-36K+55`。二者 resultant 为 `330`，此前只把 moving support分离并保留 fixed `11` bookkeeping。本文补齐该 fixed case：共同 root `mod 11` 唯一强迫 `K=0 mod11`，但 genuine height target已有 `p∤K`。因此 source-common genuine support与整个 equal-depth target/serial genuine support完全不相交，不再保留 fixed `11` exception。本文是 support allocation lemma，不证明任一 pool为空，因此不关闭 A2。

---

## 1. source common support enters the linear sheet

fully-decimal source common depth reader为

\[
G_{\rm free}
:=\frac{G_{\rm dec}}{\gcd(G_{\rm dec},b_3^2)}.
\]

对任意 genuine odd source-common prime `r`，固定 small-prime bookkeeping除外，source square-root theorem给

\[
v_r(18K-55)
\ge\left\lceil\frac{v_r(G_{\rm free})}{2}\right\rceil\ge1.
\]

所以

\[
\boxed{
r\mid G_{\rm free}
\Longrightarrow
r\mid18K-55.}
\tag{1.1}
\]

---

## 2. equal-depth target baseline enters `P`

所有 genuine equal-depth omega-height target primes满足

\[
\boxed{r\mid P(K),}
\qquad
P(K):=6K^2-36K+55,
\tag{2.1}
\]

并且 target-ladder 给精确 baseline depth

\[
\boxed{v_r(P)=h_r.}
\tag{2.2}
\]

同一 genuine height sector此前还严格证明

\[
\boxed{r\nmid K.}
\tag{2.3}
\]

理由是 `TK+a_3=\omega W_q≡0 mod r`，而 primitive reduction 给 `r∤a_3T`；若 `r|K` 就会强迫 `r|a_3`，矛盾。

---

## 3. exact resultant leaves only `3,5,11`

直接计算

\[
\boxed{
\operatorname{Res}_K(P(K),18K-55)=330
=2\cdot3\cdot5\cdot11.}
\tag{3.1}
\]

所以任何 odd prime同时满足

\[
r\mid P(K),
\qquad
r\mid18K-55
\]
都必须属于

\[
\boxed{r\in\{3,5,11\}.}
\tag{3.2}
\]

`3,5` 已不属于当前 genuine non-`3,5` height target sector。此前唯一尚未清掉的是 `11`。

---

## 4. fixed `11` root is nongenuine

模 `11`，linear sheet化为

\[
18K-55\equiv7K\pmod{11}.
\]

因此

\[
11\mid18K-55
\Longrightarrow
\boxed{K\equiv0\pmod{11}.}
\tag{4.1}
\]

而

\[
P(0)=55\equiv0\pmod{11},
\]

所以这正是 resultant 中 fixed `11` collision 的唯一 root。

但 genuine target必须满足 (2.3)：

\[
11\nmid K.
\]

故 fixed `11` collision不能属于 genuine equal-depth target：

\[
\boxed{
11\mid P(K),\quad
11\mid18K-55
\Longrightarrow
\text{nongenuine target state}.}
\tag{4.2}
\]

因此 `11` 不再需要作为 source/target overlap exception保留。

---

## 5. complete genuine support separation

综合 §§1--4，在 genuine non-`3,5` height sector严格得到

\[
\boxed{
\operatorname{Supp}_{\rm gen}(G_{\rm free})
\cap
\operatorname{Supp}_{\rm gen}(P)
=\varnothing.}
\tag{5.1}
\]

特别地，所有 equal-depth target subclasses都与 source-common genuine support分离：

\[
\boxed{
E_{\rm first},\ E_{\rm second},\ E_{\rm double}
\quad\text{均不能与 }G_{\rm free}
\text{ 复用 genuine prime}.}
\tag{5.2}
\]

这比旧版本的 moving-support separation更强：现在没有 fixed `11` 尾项。

---

## 6. independent height budgets

source common generic square-root depth满足

\[
\boxed{H_S^{\rm gen}\mid18K-55<180N.}
\tag{6.1}
\]

而 equal-depth target baseline product

\[
G_{\rm tar}:=\prod p^{h_p}
\]
满足 dual-short carrier bound

\[
\boxed{G_{\rm tar}<98T^2.}
\tag{6.2}
\]

由于 (5.1) 是 genuine support完全分离，二者可无条件形成不重复计数的 product budget：

\[
\boxed{
H_S^{\rm gen}G_{\rm tar}
<17640\,NT^2.}
\tag{6.3}
\]

这仍只是上界，不是矛盾；作用是任何后续 lower-bound / parity allocation都可以同时向两池收费。

对 double-serial pool同样有

\[
\boxed{
\gcd_{\rm gen}(G_{\rm free},G_{\rm dbl})=1,}
\tag{6.4}
\]

所以 source square-root cost与

\[
G_{\rm dbl}^3R_{\rm dbl}^2<1053TN^3
\]
也是完全独立的两套 genuine support budget。

---

## 7. current role

A2 当前最重要的两套 moving/genuine prime池现在严格 disjoint：

1. source common / source parity reuse：linear carrier
   \[
   18K-55;
   \]
2. equal-depth target / serial resonance：quadratic carrier
   \[
   P(K)=6K^2-36K+55.
   \]

不存在 fixed `11` genuine bridge。

因此后续若 global parity被迫同时调用 source-common sector和 equal-depth target sector，就会真正增加 distinct prime support与 multiplicative cost；不可能再由同一 genuine prime在两个 ledger中重复承担。

A2 仍为 `待证`。
