# A2 source odd-parity reuse 的 linear half-depth surcharge

> **依赖：** `spontaneous-source-parity-collision-gate.md`。
>
> **严格状态：**若同一 genuine inert prime要同时承担 `B_W` 与 `D_W/2` 两份 odd parity，则它在两个 source carriers中的赋值都为奇数。利用 exact square collision identity，本文证明这两个奇赋值必须相等；随后 common linear sheet `18K-55` 至少承担 `(e+1)/2` 层该 prime。把所有 odd/odd reused primes聚合后得到一个仅 `O(N)` 的全局 height budget `H_reuse | 18K-55 < 180N`。因此 source parity要节省 prime support，就必须支付极短 linear depth。本文仍允许这样的 linear divisors存在，因此不关闭 A2。

---

## 1. exact collision identity

已有

\[
\boxed{
55\mathscr B_W-K^2\mathscr D_W
=c_u^2L_S^2,}
\qquad
\boxed{L_S:=18K-55.}
\tag{1.1}
\]

固定 genuine odd prime `r`，假设

\[
r\mid\mathscr B_W,
\qquad
r\mid\mathscr D_W,
\]

以及 unit separation

\[
r\nmid55Kc_u.
\tag{1.2}
\]

记

\[
\boxed{a:=v_r(\mathscr B_W),}
\qquad
\boxed{d:=v_r(\mathscr D_W),}
\qquad
\boxed{\ell:=v_r(L_S).}
\tag{1.3}
\]

由 (1.1)：

\[
\boxed{
v_r(55\mathscr B_W-K^2\mathscr D_W)=2\ell.}
\tag{1.4}
\]

---

## 2. odd/odd reuse forces equal depth

现在假设同一 prime真的同时承担两份 source odd parity，即

\[
\boxed{a\equiv d\equiv1\pmod2.}
\tag{2.1}
\]

若

\[
a\ne d,
\]
则 (1.2) 下两个 LHS summands赋值不同，非阿基米德赋值给

\[
v_r(55\mathscr B_W-K^2\mathscr D_W)
=\min(a,d).
\]

右边由 (1.4) 为偶数，而 `min(a,d)` 是奇数，矛盾。

所以必须

\[
\boxed{a=d=:e,}
\tag{2.2}
\]

并且

\[
\boxed{e\text{ 为奇数}.}
\tag{2.3}
\]

这说明 two-source parity reuse本身已经强迫一个新的 equal-depth collision。

---

## 3. linear sheet pays at least half the odd depth

在 (2.2) 下，LHS 两项均有精确赋值 `e`。

如果它们没有额外 cancellation，则 (1.4) 会给

\[
2\ell=e,
\]
但左边为偶数、右边为奇数，不可能。

因此 LHS 必至少再加深一层：

\[
2\ell\ge e+1.
\]

所以

\[
\boxed{
\ell=v_r(18K-55)
\ge\frac{e+1}{2}.}
\tag{3.1}
\]

因为 `e` 为奇数，右边是整数。

等价地：

\[
\boxed{
r^{(e+1)/2}\mid18K-55.}
\tag{3.2}
\]

所以复用两份 odd parity的 depth不能只藏在两个高次 source forms中；至少一半必须显式出现在固定 linear prefix integer里。

---

## 4. short Archimedean height

endpoint 有

\[
0<K<10N.
\]

当前 `K` 巨大且正，因此 `18K-55>0`；粗界足够：

\[
\boxed{0<18K-55<180N.}
\tag{4.1}
\]

于是单个 reused prime满足

\[
\boxed{
r^{(e+1)/2}<180N.}
\tag{4.2}
\]

这把两个 source carriers中的奇赋值深度压回一个只有 `M+3` 位量级的 linear integer。

---

## 5. global reused-prime product

令 `E_reuse` 为所有满足以下条件的 genuine primes：

\[
r\equiv3\pmod4,
\]

\[
a_r:=v_r(\mathscr B_W)\text{ odd},
\qquad
d_r:=v_r(\mathscr D_W)\text{ odd}.
\]

§2 已证明

\[
a_r=d_r=:e_r.
\]

定义 weighted reuse product

\[
\boxed{
H_{\rm reuse}
:=\prod_{r\in E_{\rm reuse}}
r^{(e_r+1)/2}.}
\tag{5.1}
\]

逐 prime由 (3.2) 且 primes互素：

\[
\boxed{H_{\rm reuse}\mid18K-55.}
\tag{5.2}
\]

因此

\[
\boxed{H_{\rm reuse}<180N.}
\tag{5.3}
\]

写

\[
G_{\rm reuse}:=\prod r^{e_r},
\qquad
R_{\rm reuse}:=\prod r,
\]
则

\[
H_{\rm reuse}^2=G_{\rm reuse}R_{\rm reuse}.
\]
所以还得到

\[
\boxed{
G_{\rm reuse}R_{\rm reuse}
<(180N)^2.}
\tag{5.4}
\]

---

## 6. parity allocation dichotomy with depth cost

source side的两份 odd parity现在有严格二分：

### separate support

若 `B_W` 与 `D_W/2` 的 odd parity不能全部由共同 odd/odd primes承担，则至少需要 distinct inert support；这直接产生 prime-count/product surcharge。

### reused support

任何真正同时承担两边奇 parity的 prime都进入 `E_reuse`，并支付

\[
\boxed{r^{(e+1)/2}\mid18K-55.}
\]

所有这种 reuse的总成本受

\[
\boxed{H_{\rm reuse}<180N}
\]
控制。

所以“省 prime”与“省 linear depth”不能同时发生。

---

## 7. relation to serial pool

source parity collision gate 已证明 non-`3` reused prime满足

\[
r\nmid\omega,
\qquad
r\nmid2K-9,
\]
且不属于 genuine omega-height serial target pool。

所以 `H_reuse` 与 `Sigma_first/Sigma_double` 是 support-separated 的新 source object。后续可以把

\[
G_{\rm dbl}^3R_{\rm dbl}^2<1053TN^3
\]
和

\[
H_{\rm reuse}<180N
\]
同时计入 product budget，而不会重复计算同一 genuine moving prime。

本文仍不证明这些 independent supports的 combined lower bound足以超过 decimal height；A2 仍为 `待证`。
