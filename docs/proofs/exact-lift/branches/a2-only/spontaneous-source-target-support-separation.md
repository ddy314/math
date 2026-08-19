# A2 source common gcd 与 equal-depth target pool 的 support separation

> **依赖：** `spontaneous-source-parity-common-gcd.md`、`spontaneous-source-parity-decimal-square-gate.md`、`spontaneous-height-equal-depth-target-ladder.md`。
>
> **严格状态：**source common gcd的每个 genuine moving prime都必须进入 linear sheet `18K-55`；equal-depth omega-height target baseline则必须进入 fixed quadratic `P=6K^2-36K+55`。两者 resultant仅为 `330`，所以除 fixed `3,5,11` 外两套 moving support完全分离。于是 source common-depth budget与 equal-depth target/serial budgets可以全局相乘而不重复计算 moving prime。本文是 support allocation lemma，不证明任一 pool为空，因此不关闭 A2。

---

## 1. source common support enters the linear sheet

fully-decimal source common depth reader为

\[
G_{\rm free}
=G_{\rm dec}/\gcd(G_{\rm dec},b_3^2).
\]

对任何与 fixed `5,11` 分离的 genuine odd common prime `r`：

\[
v_r(G_{\rm free})=v_r(G_S)>0.
\]

source square-root theorem给

\[
v_r(18K-55)
\ge\left\lceil\frac{v_r(G_{\rm free})}{2}\right\rceil\ge1.
\]

所以

\[
\boxed{r\mid G_{\rm free}\Longrightarrow r\mid18K-55}
\tag{1.1}

在 genuine moving common sector成立。

---

## 2. equal-depth target baseline enters `P`

所有 genuine equal-depth omega-height target primes满足

\[
\boxed{r\mid P(K),}
\qquad
P(K):=6K^2-36K+55.
\tag{2.1}

更强地 target-ladder已有

\[
v_r(P)=h_r.
\]

所以 `P` 是整个 target baseline pool的 short carrier。

---

## 3. exact resultant

直接计算

\[
\boxed{
\operatorname{Res}_K(P(K),18K-55)=330.}
\tag{3.1}

即

\[
330=2\cdot3\cdot5\cdot11.
\]

因此任何 odd prime同时满足

\[
r\mid P(K),
\qquad
r\mid18K-55
\]
都必须属于

\[
\boxed{r\in\{3,5,11\}.}
\tag{3.2}

---

## 4. moving support separation

结合 §§1--3：

\[
\boxed{
\operatorname{Supp}_{\rm mov}(G_{\rm free})
\cap
\operatorname{Supp}_{\rm mov}(P)
=\varnothing}
\tag{4.1}

在 genuine non-`3,5,11` sector严格成立。

特别地，所有 genuine target subclasses均与 source common moving pool分离：

\[
\boxed{
E_{\rm first},\ E_{\rm second},\ E_{\rm double}
\quad\text{均不与 }G_{\rm free}\text{ 复用 moving prime}.}
\tag{4.2}

fixed `11` 需要单独 bookkeeping；它不是 moving overlap。

---

## 5. independent height budgets

source common generic depth有

\[
\boxed{H_S^{gen}\mid18K-55<180N.}
\tag{5.1}

而 equal-depth target baseline product

\[
G_{\rm tar}:=\prod p^{h_p}
\]
满足 dual-short carrier bound

\[
\boxed{G_{\rm tar}<98T^2.}
\tag{5.2}

由于 moving supports按 (4.1) 分离，二者可直接形成不重复计数的 product budget：

\[
\boxed{
H_S^{gen}G_{\rm tar}<17640\,NT^2.}
\tag{5.3}

这本身是上界而非矛盾；严格作用是后续任何 lower-bound/product-parity argument都可以同时收费 source-common 与 target baseline，而无需担心同一 moving prime被算两次。

---

## 6. double-serial combination

double-serial target还有更强

\[
G_{\rm dbl}^3R_{\rm dbl}^2<1053TN^3.
\]

由于 `E_dbl` 同样属于 `P` support，(4.1) 给

\[
\boxed{
\gcd_{\rm mov}(G_{\rm free},G_{\rm dbl})=1.}
\tag{6.1}

所以 source square-root cost与 double-serial weighted surcharge也是完全独立的两个 moving sectors。

---

## 7. current role

A2 的主要 moving prime结构现在至少分成两套互斥 pools：

1. source common / parity reuse：线性 carrier `18K-55`；
2. equal-depth target / serial resonance：quadratic carrier `P(K)`。

它们除 fixed `11` 外不相交。后续 global parity若被迫同时调用两边，就会真正增加 distinct support与 product cost，而不是同一 prime在不同 ledger中重复出现。

A2 仍为 `待证`。
