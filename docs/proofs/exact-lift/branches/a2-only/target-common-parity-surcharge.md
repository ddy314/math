# A2 fixed target/descent common parity 的 unavoidable surcharge

> **依赖：** `primitive-reduction.md` §8；历史 `spontaneous-crt-target-descent-overlap.md`、`spontaneous-crt-target-descent-global-gcd.md`；`height-ledger.md` 中 `spontaneous-height-equal-depth-mod24-parity.md`；`fixed-target-serial-dichotomy.md`。
>
> **严格状态：**target/descent common support 已被历史审计压成 squarefree `G_TD | 31*179`。本文证明若 `G_TD = 31` 或 `179`，即恰有一个 fixed target label 试图承担 descendant common 的 `3 mod 4` parity，则无论该 target baseline depth `h` 奇偶如何，都必强迫另一枚不同的 non-`3` inert prime。`h` 奇时 surcharge 来自 reduced numerator `W_q^prim ≡ 1 mod 4`；`h` 偶时来自 short prefix carrier `P/5 ≡ 11 mod 24`。特别地，历史尚存的 `(31,1),(179,1)` second-node strict regime 也自动带一枚额外 non-`3` height supplier，因此 fixed target old pool 不能单独吸收 common parity。本文尚未证明这枚 surcharge supplier 与 source/external common pool 完全分离，因此仍不宣称 A2 关闭。

---

## 1. fixed target/descent common bookkeeping

历史 target/descent overlap 已证明：任何 genuine equal-depth target prime 若同时进入 fully primitive descendant common support，则

\[
\boxed{p\in\{31,179\}.}
\tag{1.1}
\]

而 global-gcd audit 进一步证明 descendant common 中的 target contribution 只有一层，因此

\[
\boxed{G_{TD}\mid31\cdot179,\qquad G_{TD}\text{ squarefree}.}
\tag{1.2}
\]

两枚 fixed primes 都是 inert：

\[
31\equiv179\equiv3\pmod4,
\qquad31\cdot179\equiv1\pmod4.
\tag{1.3}
\]

所以 fixed target old pool 自身能够给 `G_Delta` 提供 odd inert parity 当且仅当

\[
\boxed{G_{TD}=p_0\in\{31,179\}.}
\tag{1.4}
\]

即两枚中恰有一枚进入 target/descent common overlap。

固定这枚 `p_0`。真正 equal-depth target 的 baseline depth满足

\[
\boxed{
v_{p_0}(P)=v_{p_0}(\omega)=v_{p_0}(W_q)=h\ge1,}
\tag{1.5}
\]

其中

\[
P(K)=6K^2-36K+55.
\tag{1.6}
\]

下面按 `h` 奇偶分裂。

---

## 2. odd baseline: reduced numerator forces a second height prime

`primitive-reduction.md` 已证明

\[
W_q^{\rm prim}:=\frac{W_q}{3^\delta}\equiv1\pmod4,
\tag{2.1}
\]

并且 balanced `3` 已被完整约去，所以

\[
3\nmid W_q^{\rm prim}.
\tag{2.2}
\]

设

\[
h\equiv1\pmod2.
\tag{2.3}
\]

由 (1.5)，`p_0^h` 在 `W_q^prim` 中仍以 exact odd exponent出现，因为 `p_0 != 3`。写

\[
W_q^{\rm prim}=p_0^h W_1.
\tag{2.4}
\]

由 `p_0 = 3 mod 4` 与 `h` 奇：

\[
p_0^h\equiv3\pmod4.
\]

结合 (2.1)：

\[
\boxed{W_1\equiv3\pmod4.}
\tag{2.5}
\]

因此 `W_1` 必含至少一枚 prime

\[
\boxed{r\equiv3\pmod4}
\tag{2.6}
\]

到奇数次。由 (2.2)，`r != 3`；由已约去 `p_0` 的 exact odd contribution，必可选

\[
\boxed{r\ne p_0.}
\tag{2.7}
\]

所以 odd baseline 强迫一枚不同的 non-`3` inert height supplier：

\[
\boxed{
h\text{ odd}\Longrightarrow
\exists r\ne3,p_0:\ r\equiv3\pmod4,\quad v_r(W_q)\text{ odd}.}
\tag{2.8}
\]

特别地，历史 fixed-target triple-deep points 都有 `h=1`，所以 `fixed-target-serial-dichotomy.md` 尚保留的 `rho_p=1` second-node strict regime 也自动满足 (2.8)。该 regime 不能由 `31` 或 `179` 单独承担全部 non-`3` height parity。

---

## 3. even baseline: short prefix carrier forces a second inert prime

现在设

\[
h\equiv0\pmod2.
\tag{3.1}
\]

`height-ledger.md` 的 dual-short mod-24 theorem 已证明

\[
\boxed{\frac{P}{5}\equiv11\pmod{24}.}
\tag{3.2}
\]

这里也可直接从 decimal structure 看出。写 `K=10s`，则

\[
\frac P5
=120s^2-72s+11
\equiv11\pmod{24}.
\tag{3.3}
\]

又由 (1.5)，`v_{p_0}(P)=h` exact。定义

\[
P_1:=\frac{P}{5p_0^h}.
\tag{3.4}
\]

因为 `h` 偶而 `p_0 = 3 mod4`：

\[
p_0^h\equiv1\pmod4.
\]

所以由 (3.2)：

\[
\boxed{P_1\equiv3\pmod4.}
\tag{3.5}
\]

因此 `P_1` 必含某枚

\[
r\equiv3\pmod4
\]
到奇数次。它不能等于 `p_0`，因为 `p_0` 的完整 exact depth `h` 已在 (3.4) 中约尽。

还要排除 `r=3`。但

\[
P(K)=6K^2-36K+55\equiv1\pmod3,
\tag{3.6}
\]

故 `3` 根本不整除 `P`。因此

\[
\boxed{
h\text{ even}\Longrightarrow
\exists r\ne3,p_0:\ r\equiv3\pmod4,\quad v_r(P_1)\text{ odd}.}
\tag{3.7}
\]

所以 even baseline 也必须额外产生一枚 distinct non-`3` inert prefix supplier。

---

## 4. unified target surcharge theorem

合并 §§2–3：

\[
\boxed{
G_{TD}=p_0\in\{31,179\}
\Longrightarrow
\exists r\ne3,p_0,\ r\equiv3\pmod4,
}
\tag{4.1}
\]

其中：

- `h` 奇时 `r` 由 `W_q^prim` 的 reduced-numerator parity 强迫；
- `h` 偶时 `r` 由 `P/(5p_0^h)` 的 prefix parity 强迫。

因此 target/descent common factor 的 odd orientation从来不是免费的：

\[
\boxed{
G_{TD}\equiv3\pmod4
\Longrightarrow
\text{至少再出现一枚 }G_{TD}\text{ 外的 non-3 inert prime}.}
\tag{4.2}
\]

这里“`G_TD` 外”是严格的：在危险 case (1.4) 中 `G_TD=p_0`，而 surcharge prime `r != p_0`。

---

## 5. consequence for descendant common parity

历史 common-parity dichotomy 在 `Z=1 mod4, G_Delta=3 mod4` 时允许 common gcd 自身吸收两边 parent parity。旧 source classification把这种 common odd parity的 old-pool来源分成：

1. fixed target `31/179`；
2. source-common overlap；
3. fixed height/denominator shadows；
4. genuine external common kernel。

本文说明第 1 项不能再被视为“单独解释 parity”的终止叶子：若它以 odd orientation出现，自动向其外部输出另一枚 non-`3` inert prime。

因此新的逻辑边界是：

\[
\boxed{
\text{fixed target odd common parity}
\Longrightarrow
\text{source/height/external side还必须承担一份 independent inert support}.}
\tag{5.1}
\]

这与 `fixed-target-serial-dichotomy.md` 的 first-node surcharge互补，并且覆盖其尚未关闭的 second-node strict regime。

尚需继续证明 surcharge prime不能被 source-common / fixed-height / generic external common pool无代价回收。A2 因此仍为 `待证`，但 fixed target 已从 possible terminal absorber 降级为 mandatory parity exporter。

---

## 6. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_target_common_parity_surcharge.py
```

checker 验证 `P/5 mod 24`、`P mod 3`、`31/179` 的 mod-4 classes 以及 odd/even baseline parity ledger。