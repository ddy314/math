# A2 additive carrier 与 descendant pair 的 exact gcd interface

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`、`spontaneous-crt-descendant-common-parity.md`。
>
> **严格状态：**fully primitive descent 已有 `\widehat{\mathcal T}_2=5^\lambda\mathscr R_{63}^\star+g2^m\widehat{\mathscr D}_{63}`，并且 `\gcd(\mathscr R_{63}^\star,10g)=1`、`5\nmid\widehat{\mathscr D}_{63}`。本文抽出一个此前未显式记录的全局 gcd identity：original additive carrier 与任意一个 descendant parent 的公共部分都**恰好**等于两个 descendant parents 的 common gcd `G_\Delta`。因此一枚 additive prime 若复用任意一个 descendant parent，就自动进入两边的 common pool；不存在只复用单边的第三种 support channel。本文不排除 `G_\Delta` 本身的 external common parity，因此不关闭 A2。

---

## 1. fully primitive descent

沿用

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.}
\tag{1.1}
\]

历史 primitive reduction 已证明

\[
\boxed{
\gcd(\mathscr R_{63}^\star,10g)=1,}
\tag{1.2}
\]

而 descended quotient audit 给

\[
\boxed{5\nmid\widehat{\mathscr D}_{63}.}
\tag{1.3}
\]

定义

\[
\boxed{
G_\Delta
:=\gcd(\mathscr R_{63}^\star,
          \widehat{\mathscr D}_{63}).}
\tag{1.4}
\]

---

## 2. additive / short-remainder gcd

由 (1.1)：

\[
\begin{aligned}
\gcd(\widehat{\mathcal T}_2,\mathscr R_{63}^\star)
&=\gcd(g2^m\widehat{\mathscr D}_{63},\mathscr R_{63}^\star).
\end{aligned}
\]

由 (1.2)，`g2^m` 与 `Rstar` 互素，因此

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,\mathscr R_{63}^\star)
=G_\Delta.}
\tag{2.1}
\]

---

## 3. additive / descended-quotient gcd

同理由 (1.1)：

\[
\gcd(\widehat{\mathcal T}_2,\widehat{\mathscr D}_{63})
=\gcd(5^\lambda\mathscr R_{63}^\star,
      \widehat{\mathscr D}_{63}).
\]

由 (1.3)，`5^lambda` 与 `Dhat` 互素，所以

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,\widehat{\mathscr D}_{63})
=G_\Delta.}
\tag{3.1}
\]

合并 (2.1),(3.1)：

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,\mathscr R_{63}^\star)
=
\gcd(\widehat{\mathcal T}_2,\widehat{\mathscr D}_{63})
=
\gcd(\mathscr R_{63}^\star,\widehat{\mathscr D}_{63})
=G_\Delta.}
\tag{3.2}
\]

---

## 4. prime-support consequence

固定任意奇素数 `p`。若

\[
p\mid\widehat{\mathcal T}_2
\]

并且它还满足

\[
p\mid\mathscr R_{63}^\star
\quad\text{或}\quad
p\mid\widehat{\mathscr D}_{63},
\]

那么由 (3.2) 自动有

\[
\boxed{
p\mid G_\Delta,}
\tag{4.1}
\]

即同时

\[
\boxed{
p\mid\mathscr R_{63}^\star,
\qquad
p\mid\widehat{\mathscr D}_{63}.}
\tag{4.2}
\]

因此 additive supplier 的 descendant reuse 只有严格二分：

1. `p\nmid G_Delta`：它完全不进入两个 descendant parents；
2. `p\mid G_Delta`：它同时进入两个 parents 的 common pool。

不存在“只复用 `Rstar`”或“只复用 `Dhat`”的中间 channel。

---

## 5. role in the dangerous `Z=1 mod4` orientation

在 `Z\equiv1\pmod4` 中，endpoint fixed-`3` audit 已给

\[
3\nmid\widehat{\mathcal T}_2,
\]

而 additive primitive carrier 为 positive `3 mod4`。所以必存在某枚

\[
q\equiv3\pmod4,
\qquad q\ne3,
\]

在 `\widehat{\mathcal T}_2` 中以奇次出现。

(3.2) 说明这枚 mandatory non-`3` inert supplier 若想复用 descendant support，就必须进入 `G_Delta`。因此后续 global support audit 可严格分成：

\[
\boxed{
\text{additive-external supplier}
\quad\text{or}\quad
\text{descendant-common supplier in }G_\Delta.}
\tag{5.1}
\]

第二种情形可以直接接入现有 `descendant-common-parity` 的 old-pool/external-kernel 分类；无需再分别审计 additive-vs-`Rstar` 与 additive-vs-`Dhat` 两张 overlap 表。

A2 仍为 `待证`。

---

## 6. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_additive_descendant_gcd_interface.py
```
