# A2 `B_W / D_W` source parity suppliers 的 collision gate

> **依赖：** `source-discriminant.md`、`spontaneous-height-content-oversaturation.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**`B_W` 与 positive source discriminant `D_W/2` 都是 odd-inert parity suppliers。本文证明二者若复用同一 genuine prime，则该 prime必须进入固定 linear sheet `18K-55=0`；该 sheet与 additive residual overlap的 central factor `2K-9` 在 `3 mod 4` support上完全分离，并且与 omega-height target quadratic `P=6K^2-36K+55` 的共同 odd prime只能来自 `3,5,11`。因此 source parity若由一枚共同 moving inert prime承担，该 prime必是 noncentral、non-omega-target 的新 label。本文仍允许该 linear sheet本身存在，故不关闭 A2。

---

## 1. exact square collision identity

沿用

\[
\mathscr D_W:=55z^2-49c_u^2,
\]

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.
\]

直接计算：

\[
\begin{aligned}
55\mathscr B_W-K^2\mathscr D_W
={}&55c_u^2(5K^2-36K+55)\\
&+55z^2K^2-K^2(55z^2-49c_u^2)\\
={}&c_u^2\left[55(5K^2-36K+55)+49K^2\right].
\end{aligned}
\]

而括号恰为

\[
324K^2-1980K+3025=(18K-55)^2.
\]

所以得到 exact identity

\[
\boxed{
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2.}
\tag{1.1}
\]

这不是 resultant only；它是整数平方恒等式。

---

## 2. common genuine prime must hit the linear sheet

令 odd prime `r` 满足

\[
r\mid\mathscr B_W,
\qquad
r\mid\mathscr D_W,
\qquad
r\nmid c_u.
\]

由 (1.1)：

\[
r\mid c_u^2(18K-55)^2.
\]

所以

\[
\boxed{r\mid18K-55.}
\tag{2.1}
\]

反过来若

\[
r\mid\mathscr D_W,
\qquad
r\mid18K-55,
\qquad
r\nmid55,
\]
则 (1.1) 给 `r|B_W`。因此在与 `55c_u` 分离的 genuine sector：

\[
\boxed{
r\mid\mathscr B_W,\mathscr D_W
\Longleftrightarrow
r\mid\mathscr D_W,\ 18K-55.}
\tag{2.2}
\]

所以两份 source parity的 moving overlap只有一张 fixed linear sheet。

---

## 3. collision sheet is disjoint from additive central overlap on inert support

additive residual parity doubling theorem证明，height-free additive companions若再次共享 odd prime，只能回到

\[
(2K-9)\omega.
\]

先比较两个 linear factors：

\[
(18K-55)-9(2K-9)=26.
\tag{3.1}
\]

因此

\[
\boxed{\gcd(18K-55,2K-9)\mid26.}
\tag{3.2}
\]

若 odd prime `r` 同时整除二者，则

\[
r=13.
\]
但

\[
13\equiv1\pmod4.
\]
所以对 inert prime：

\[
\boxed{
r\equiv3\pmod4,\ r\mid18K-55
\Longrightarrow
r\nmid2K-9.}
\tag{3.3}
\]

因此 source parity collision prime不可能再使用 additive central sheet。

---

## 4. collision prime is non-content

`source-discriminant.md` 已证明

\[
\boxed{\gcd(\mathscr D_W,\omega)\mid6.}
\tag{4.1}
\]

所以任意 non-`3` odd divisor of `D_W` 都满足

\[
\boxed{r\nmid\omega.}
\tag{4.2}
\]

特别地，任何 genuine non-`3` source parity collision prime同时具有

\[
\boxed{r\nmid(2K-9)\omega.}
\tag{4.3}
\]

结合 residual parity doubling：若这样一枚 prime恰进入某一个 additive height-free residual，它不可能同时进入另一个 residual；additive pair不能用它复用两份 parity。

注意本文不声称 collision prime必进入 additive residual pair中的任意一个。

---

## 5. collision sheet versus omega-height target quadratic

omega-height target quadratic为

\[
P_{\omega H}(K)=6K^2-36K+55.
\]

将 linear root `18K-55=0` 代入并清分母：

\[
18^2P_{\omega H}(55/18)=330.
\]
等价地 polynomial resultant 为

\[
\boxed{
\operatorname{Res}_K(P_{\omega H},18K-55)=330
=2\cdot3\cdot5\cdot11.}
\tag{5.1}
\]

因此任何 odd prime同时满足

\[
r\mid P_{\omega H}(K),
\qquad
r\mid18K-55
\]
必有

\[
\boxed{r\in\{3,5,11\}.}
\tag{5.2}
\]

在 genuine non-`3,5` height target sector只剩 fixed `11`。

而真正 serial/equal-depth target还满足 `r|omega`；由 (4.1)，non-`3` 的 `D_W` divisor不能同时整除 `omega`。所以 source parity collision sheet与 genuine serial target pool本身完全分离。

---

## 6. parity supplier dichotomy

`source-discriminant.md` 给两份 global odd-inert parity：

\[
\mathscr B_W\equiv7\pmod8,
\]

\[
\mathscr D_W/2\equiv3\pmod4.
\]

因此各自都必须含 `3 mod 4` prime到奇次。

现在两份 parity的 allocation只有两种可能：

1. **separate suppliers**：存在至少两枚不同 inert primes，分别承担 `B_W` 与 `D_W/2` 的奇 parity；
2. **reused supplier**：某枚 inert prime同时整除 `B_W,D_W`，此时由 §2 它必须满足
   \[
   \boxed{18K-55\equiv0\pmod r.}
   \]

而 reused supplier在 genuine non-`3` sector还自动满足

\[
r\nmid\omega,
\qquad
r\nmid2K-9,
\]
并且不能是 moving omega-height target。

这给 source parity一个严格的“两枚 prime product surcharge / 单枚 fixed linear sheet”二分。

---

## 7. current interface to residual parity doubling

若 source parity走 separate-supplier branch，则已经产生至少两枚不同 inert primes；后续可直接结合 natural representative高度做 product budget。

若走 reused-supplier branch，则唯一 reusable prime被压入

\[
18K-55=0
\]
且是 noncentral、noncontent。由 additive residual parity doubling theorem，这样的 prime不能同时承担 height-free additive actual/companion两份 parity。

所以后续最值得继续审计的是 linear sheet `18K-55` 与 angle pair common support

\[
AQ_0c_Q
\]
以及 additive individual residual supports的 cross-overlap。

A2 仍为 `待证`。
