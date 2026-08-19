# A2 target baseline 与 height-descent pair 的 fixed squarefree common gcd

> **依赖：** `spontaneous-crt-target-descent-overlap.md`、`spontaneous-crt-target-descent-depth-squeeze.md`、`spontaneous-crt-target-descent-fixed-h1.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`。
>
> **严格状态：**此前逐 prime 证明 equal-depth target 若与 fully primitive height-descent pair复用 prime，则只能是 fixed `31,179`；高 baseline `h>=2` 时两个 descended carriers在该 prime上都精确只有一层，而 `h=1` 时 target baseline自身只有一层。本文把这些局部结论合成为一个 global gcd identity：target product `G_tar` 与 `Rstar_63,Dhat_63` 的 common part完全相同，是 `31*179` 的 squarefree divisor。除去该固定 common part后，两个 descended carriers都与全部 target baseline support互素。结合 primitive mod-4 orientation，在 `Z=1 mod4` 分支中，若 fixed overlap的数量为偶数，则两个 target-free residual carriers仍各自为 `3 mod4`，因此各自必须产生 target-disjoint inert parity。本文不证明这两份新 parity彼此也不复用，因此不关闭 A2。

---

## 1. target baseline product

令 `E_tar` 为当前所有 genuine deep equal-depth omega-height target primes，并写

\[
h_p:=v_p(\omega)=v_p(W_q)\ge1.
\]

定义 baseline product

\[
\boxed{
G_{\rm tar}:=\prod_{p\in E_{\rm tar}}p^{h_p}.}
\tag{1.1}
\]

已有 target ladder 给

\[
G_{\rm tar}\mid P(K),
\]
并且对每个 target prime

\[
\boxed{v_p(P)=h_p.}
\tag{1.2}
\]

fully primitive height descent为

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.}
\tag{1.3}
\]

其中

\[
\boxed{
\mathscr R_{63}^\star>0,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4,
\qquad
\gcd(\mathscr R_{63}^\star,10g)=1.}
\tag{1.4}
\]

---

## 2. target overlap support is only `31,179`

`spontaneous-crt-target-descent-overlap.md` 已证明：若 genuine target prime `p` 还满足

\[
p\mid\widehat{\mathscr D}_{63}
\]
或

\[
p\mid\mathscr R_{63}^\star,
\]
则

\[
\boxed{p\in\{31,179\}.}
\tag{2.1}
\]

更精确地，对应的 target root必须分别落在

\[
\boxed{
K\equiv9\pmod{31},
\qquad
K\equiv71\pmod{179}.}
\tag{2.2}
\]

另一个 `P(K)` root并不属于 descent overlap sheet。

所以 moving target support 与整个 descended pair已经完全分离。

---

## 3. within the target pool, the two descended carriers have identical support

固定 `p\in E_tar`。target oversaturation给

\[
\boxed{v_p(\widehat{\mathcal T}_2)\ge h_p+1\ge2.}
\tag{3.1}
\]

且 genuine target 与 `5g2` 分离。

由 descent identity (1.3)：

- 若 `p|Dhat_63` 而 `p∤Rstar_63`，右边第一项为 unit，故 `That_2` 为 unit，矛盾；
- 若 `p|Rstar_63` 而 `p∤Dhat_63`，同理右边第二项为 unit，仍矛盾。

因此

\[
\boxed{
 p\in E_{\rm tar}
\Longrightarrow
\bigl[p\mid\widehat{\mathscr D}_{63}
\iff p\mid\mathscr R_{63}^\star\bigr].}
\tag{3.2}
\]

结合 §2，两者在 target pool内的 common support完全相同，而且至多是 `31,179`。

---

## 4. common target depth is always exactly one layer

现在审计 gcd 中的 exponent。

### high baseline `h_p>=2`

`spontaneous-crt-target-descent-depth-squeeze.md` 已证明，对 fixed overlap primes `31,179`：

\[
\boxed{
v_p(\widehat{\mathscr D}_{63})
=v_p(\mathscr R_{63}^\star)=1.}
\tag{4.1}
\]

因此与 `G_tar` 的 common exponent为

\[
\min(h_p,1)=1.
\]

### low baseline `h_p=1`

即使 descended carrier继续 Hensel加深，`G_tar` 在该 prime上本身只有一层：

\[
v_p(G_{\rm tar})=1.
\]

所以 gcd exponent仍然只能是

\[
\boxed{1.}
\tag{4.2}
\]

因此 target/descent common factor在所有 baseline depth下都 squarefree。

---

## 5. canonical global common factor

定义

\[
\boxed{
G_{TD}
:=\gcd(G_{\rm tar},\mathscr R_{63}^\star).}
\tag{5.1}
\]

由 §§2--4：

\[
\boxed{
G_{TD}\mid31\cdot179,
\qquad G_{TD}\text{ squarefree}.}
\tag{5.2}
\]

而 (3.2) 与相同的 depth audit给

\[
\boxed{
G_{TD}
=\gcd(G_{\rm tar},\widehat{\mathscr D}_{63}).}
\tag{5.3}
\]

因此

\[
\boxed{
G_{TD}\in\{1,31,179,31\cdot179\}.}
\tag{5.4}
\]

它是 entire target baseline 与 descended pair之间唯一可能的 common bookkeeping factor。

定义 target-free quotients

\[
\boxed{
R_{TD}^\circ:=\frac{\mathscr R_{63}^\star}{G_{TD}},
\qquad
D_{TD}^\circ:=\frac{\widehat{\mathscr D}_{63}}{G_{TD}}.}
\tag{5.5}
\]

则严格有

\[
\boxed{
\gcd(R_{TD}^\circ,G_{\rm tar})
=\gcd(D_{TD}^\circ,G_{\rm tar})=1.}
\tag{5.6}
\]

所以除去最多 `5549` 的 fixed factor以后，两个 descended carriers都与全部 target baseline support真正分离。

---

## 6. mod-4 parity after removing target overlap

因为

\[
31\equiv179\equiv3\pmod4,
\]
所以

\[
\boxed{
G_{TD}\equiv
\begin{cases}
1\pmod4,&G_{TD}=1\text{ or }31\cdot179,\\
3\pmod4,&G_{TD}=31\text{ or }179.
\end{cases}}
\tag{6.1}
\]

而

\[
\mathscr R_{63}^\star\equiv3\pmod4.
\]
故

\[
\boxed{
R_{TD}^\circ\equiv
\begin{cases}
3\pmod4,&G_{TD}\equiv1\pmod4,\\
1\pmod4,&G_{TD}\equiv3\pmod4.
\end{cases}}
\tag{6.2}
\]

因此若 fixed target overlap数量为偶数（`G_TD=1` 或 `31*179`），则 positive target-free integer `R_TD^circ` 仍为 `3 mod4`，必含至少一枚 odd inert prime到奇次；由 (5.6)，这枚 prime不属于任何 equal-depth target baseline support：

\[
\boxed{
G_{TD}\equiv1\pmod4
\Longrightarrow
R_{TD}^\circ\text{ 强迫一份 target-disjoint inert parity}.}
\tag{6.3}
\]

---

## 7. dangerous `Z=1 mod4` branch duplicates the target-free parity

`spontaneous-crt-descended-quotient-orientation.md` 已证明

\[
\boxed{
\widehat{\mathscr D}_{63}\equiv3Z\pmod4.}
\tag{7.1}
\]

在最危险 orientation

\[
\boxed{Z\equiv1\pmod4,}
\tag{7.2}
\]
有

\[
\widehat{\mathscr D}_{63}\equiv3\pmod4.
\]

所以和 (6.2) 完全同型：若 `G_TD≡1 mod4`，则

\[
\boxed{D_{TD}^\circ\equiv3\pmod4.}
\tag{7.3}
\]

结合 (5.6)：

\[
\boxed{
Z\equiv1\pmod4,\quad
G_{TD}\equiv1\pmod4
\Longrightarrow
R_{TD}^\circ,D_{TD}^\circ
\text{ 各自都需要 target-disjoint inert parity}.}
\tag{7.4}
\]

本文尚未证明这两份 parity彼此不能由同一个 generic non-target prime复用；该 cross-descendant overlap正是下一层应审计的对象。

---

## 8. revised global frontier

height descent与 equal-depth target之间现在只剩一个绝对有界的接口：

\[
\boxed{G_{TD}\mid5549.}
\]

因此后续 global parity/product arguments可以先无损除去 `G_TD`，再把 descended pair视为 target-free carriers。

特别地：

- `G_TD=1` 或 `31*179`：`Rstar_63` 的 odd-inert parity不能由 target pool支付；在 `Z=1` 中 `Dhat_63` 同样如此；
- `G_TD=31` 或 `179`：恰有一个 fixed target prime可以支付 descended parity，是唯一 target-reuse escape channel。

所以 target/descent reuse已经从任意 moving support压成一个四值 squarefree bookkeeping variable，而不再是 unbounded prime-allocation问题。

A2 仍为 `待证`。
