# A2 fixed `31/179` target/descent overlap 的 exact depth squeeze

> **依赖：** `spontaneous-crt-target-descent-overlap.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**前一文件把 equal-depth target/descent reuse压成 fixed `31/179`，并证明 baseline `h>=2` 时 `v_p(Dhat_63)=1`。本文使用 original additive carrier的 target depth与 fully primitive positive descent，进一步证明同样 `v_p(Rstar_63)=1`。因此任意高 baseline target `p^h,h>=2` 在两个 descended carriers中都只留下 first-layer shadow；无界 target depth不能随 descent reuse传播。唯一可能继续发生 second-layer cancellation的只剩 fixed `31/179,h=1`。本文不排除这两个低 baseline templates，因此不关闭 A2。

---

## 1. original target depth

height-free additive identity之前给

\[
\widehat{\mathcal T}_2
=5^m\widehat{\mathcal J}_H
-2^{m+1}B_0^2(2K-9)\alpha,
\tag{1.1}
\]

其中 `B_0=c_ug`。

真正 equal-depth oversaturation target满足

\[
v_p(\widehat{\mathcal J}_H)\ge h+1,
\]

\[
v_p(\alpha)=2h.
\]

所以

\[
\boxed{
v_p(\widehat{\mathcal T}_2)
\ge\min(h+1,2h)=h+1.}
\tag{1.2}
\]

这里允许两项进一步 cancellation；本文只需要 lower bound。

---

## 2. descended quotient depth for high baseline

前一 target-overlap theorem已经证明：若

\[
p\in\{31,179\},
\qquad h\ge2,
\]
则

\[
\boxed{v_p(\widehat{\mathscr D}_{63})=1.}
\tag{2.1}
\]

这些 primes与 `2\cdot5g` 分离，所以

\[
\boxed{
v_p(g2^m\widehat{\mathscr D}_{63})=1.}
\tag{2.2}
\]

---

## 3. positive descent forces the short remainder to the same first layer

fully primitive descent为

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.}
\tag{3.1}
\]

由 (1.2)，当 `h>=2`：

\[
v_p(\widehat{\mathcal T}_2)\ge h+1\ge3.
\tag{3.2}
\]

而 (2.2) 的第二项精确只有一层。

如果第一项深度大于 `1`，右边和的唯一最浅项就是第二项，整个右边只能有 depth `1`，与 (3.2) 矛盾。

如果第一项不被 `p` 整除，右边则为 unit，也矛盾。

所以第一项必须精确同深：

\[
\boxed{
v_p(5^\lambda\mathscr R_{63}^\star)=1.}
\tag{3.3}
\]

`p\ne5`，故

\[
\boxed{
v_p(\mathscr R_{63}^\star)=1.}
\tag{3.4}
\]

---

## 4. complete high-baseline depth profile

结合 target baseline

\[
v_p(P)=h
\]
和前一 theorem：

\[
\boxed{
\begin{array}{c|c}
\text{carrier}&p\text{-depth}\\ \hline
P(K)&h\\
\widehat{\mathcal T}_2&\ge h+1\\
\widehat{\mathscr D}_{63}&1\\
\mathscr R_{63}^\star&1
\end{array}
\qquad
(p=31,179,\ h\ge2).}
\tag{4.1}
\]

所以 target baseline可以随 `h` 增长，但 descent overlap完全停留在 first layer。

特别地：

\[
\boxed{
\text{unbounded equal-depth target resonance cannot propagate into the height-descent pair}.}
\tag{4.2}
\]

---

## 5. only low-baseline fixed templates remain

真正尚未由本链精确锁死的 target/descent reuse只有

\[
\boxed{
(p,h)=(31,1),\quad(179,1).}
\tag{5.1}
\]

此时 target-overlap identity中 main term与 `H_0` error都只有一层，`Dhat_63` 可能发生 next-digit cancellation；positive descent也允许 `Rstar_63` 同步继续一层。

因此若要彻底删除 target reuse，只需对两个 fixed roots

\[
K\equiv9\pmod{31},
\qquad
K\equiv71\pmod{179}
\]
做一次 mod-`p^2` normalized audit。没有任何 moving prime或 high-depth Hensel family需要继续处理。

A2 仍为 `待证`。
