# A2 fixed `31/179` triple-deep target 的 serial dichotomy

> **依赖：** 历史 `spontaneous-crt-target-descent-fixed-h1.md`、`spontaneous-crt-target-descent-fixed-h1-third.md`；`height-ledger.md` 中 `spontaneous-height-equal-depth-tropical-balance.md`、`spontaneous-height-equal-depth-serial-tropical-bridge.md`、`spontaneous-height-equal-depth-serial-conjugates.md` 与 `spontaneous-height-equal-depth-serial-parity-neutrality.md`。
>
> **严格状态：**历史 fixed-target audit 已把 `(p,h)=(31,1),(179,1)` 的 target/descent triple-deep overlap 各压成唯一一个模 `p^3` 点。本文不再继续机械提升 `(K,d)`，而把这两个点送入 canonical serial depth system。两点都满足 `r_+=2` **精确成立**。因此 serial system 只有两种可能：`rho_p=1` 时第二节点必 strict-extra，并有 `c_p=1`；`rho_p>1` 时第一节点必 strict-extra，且 `r_B=1`、`c_p>1`、`min(c_p,rho_p)=2`。后一类中 fixed target prime 在 source carrier `B_W` 的 exponent 恰为 `2`，故对 `B_W` 的 inert parity 完全中性，并强迫另一枚 serial-first pool 外的 inert supplier。本文没有排除前一种 second-node strict regime，因此仍不宣称 A2 关闭。

---

## 1. 两个历史 triple-deep 点的 actual depth 是精确 `3`

沿用 target quadratic

\[
P(K)=6K^2-36K+55,
\]

以及 projective coordinate

\[
d:=D/N,
\qquad
U/N=dK-1.
\]

actual target companion 为

\[
\frac{R_+}{N}
=dP-K(dK-1).
\tag{1.1}
\]

历史 h=1 audit 已得到唯一 triple-deep states：

\[
\boxed{
\begin{array}{c|c|c}
p&K\pmod{p^3}&d\pmod{p^3}\\ \hline
31&17307&22110\\
179&5430752&890583
\end{array}}
\tag{1.2}
\]

直接代入 (1.1) 得两点统一满足

\[
\boxed{
v_p(P)=1,\qquad v_p(dK-1)=1,\qquad v_p(R_+/N)=3.}
\tag{1.3}
\]

由于 baseline target depth

\[
h=1,
\]
定义

\[
r_+:=v_p(R_+)-h
\]
后，两点实际上不是仅有 `r_+>=2`，而是

\[
\boxed{r_+=2.}
\tag{1.4}
\]

这一步很重要：后续 serial second node 的 minimum 不只受到下界，而受到一个精确 upper cutoff。

---

## 2. serial depth notation

沿用 `height-ledger.md`：

\[
v_p(\mathscr B_W)=h+r_B,
\tag{2.1}
\]

\[
v_p(\Lambda_{\rm dec})=2h+\rho_p,
\tag{2.2}
\]

定义 middle residual

\[
C_{BE}=F_{\rm dec}P-2K^2\beta,
\qquad
c_p:=v_p(C_{BE})-h.
\tag{2.3}
\]

当前 `h=1`。历史 tropical theorem 在 triple-deep point 已给

\[
\boxed{\min\{r_B,\rho_p\}=1.}
\tag{2.4}
\]

first serial node 的 valuation law 为

\[
\boxed{
c_p\ge\min\{r_B,1\},}
\tag{2.5}
\]

且当 `r_B\ne1` 时 minimum 唯一，因此

\[
\boxed{c_p=\min\{r_B,1\}=1.}
\tag{2.6}
\]

second serial node 来自 exact identity

\[
F_{\rm dec}E_+
=K\Lambda_{\rm dec}+\beta C_{BE}.
\tag{2.7}
\]

其 valuation law 是

\[
\boxed{r_+\ge\min\{\rho_p,c_p\},}
\tag{2.8}
\]

且若 `rho_p\ne c_p`，minimum 唯一，故

\[
\boxed{r_+=\min\{\rho_p,c_p\}.}
\tag{2.9}
\]

现在把精确值 (1.4) 代入。

---

## 3. `rho_p=1`：第二 serial node 必 strict-extra

先设

\[
\boxed{\rho_p=1.}
\tag{3.1}
\]

若 `c_p>1`，则 second node (2.7) 的两个 RHS terms 中 `rho_p=1` 是唯一 minimum。由 (2.9) 必有

\[
r_+=1,
\]

与 (1.4) 的 `r_+=2` 矛盾。

因此

\[
\boxed{c_p=1.}
\tag{3.2}
\]

于是

\[
\boxed{c_p=\rho_p=1<r_+=2.}
\tag{3.3}
\]

这正是 canonical **second-node strict cancellation**。

serial-conjugate theorem 对

\[
D_E:=\beta C_{BE}-K\Lambda_{\rm dec}
\]
给出：当 actual sum sheet strict-extra 时，conjugate sheet 精确停在 common baseline。因此

\[
\boxed{v_p(D_E)=2h+c_p=3.}
\tag{3.4}
\]

所以这一 regime 虽仍存在，但它已经从“继续自由 Hensel 提升”改写成：

\[
\boxed{
\rho_p=c_p=1,\quad r_+=2,\quad v_p(D_E)=3.
}
\tag{3.5}
\]

后续若要关闭它，应审计这个 exact third-layer conjugate，而不是再次提升 `(K,d)`。

---

## 4. `rho_p>1`：第一 serial node 必 strict-extra

现在设

\[
\boxed{\rho_p>1.}
\tag{4.1}
\]

由 tropical identity (2.4)，立刻得到

\[
\boxed{r_B=1.}
\tag{4.2}
\]

若 `c_p=1`，那么 second node 中 `c_p=1<rho_p` 是唯一 minimum，故 (2.9) 再次强迫

\[
r_+=1,
\]

与 (1.4) 矛盾。因此

\[
\boxed{c_p>1.}
\tag{4.3}
\]

结合 (4.2)：

\[
\boxed{r_B=h=1<c_p,\qquad \rho_p>h.}
\tag{4.4}
\]

这正是 canonical **first-node strict cancellation** (`Sigma_first`)。

还有一个此前没有显式抽出的精确 squeeze。由 (2.8) 与 `r_+=2`：

\[
2\ge\min\{c_p,\rho_p\}.
\]

而 (4.1),(4.3) 又说明二者都至少为 `2`，故

\[
\boxed{\min\{c_p,\rho_p\}=2.}
\tag{4.5}
\]

所以这一 regime 的全部 depth profile 为

\[
\boxed{
r_B=1,\quad c_p>1,\quad\rho_p>1,\quad
\min\{c_p,\rho_p\}=2,\quad r_+=2.}
\tag{4.6}
\]

first-node conjugate sheet相应精确停在 baseline；不存在两张 middle sheets同时继续深化的可能。

---

## 5. `rho_p>1` regime 对 source inert parity 完全中性

source carrier `B_W` 在 target prime上的 exponent 是

\[
v_p(\mathscr B_W)=h+r_B.
\]

由 (4.2) 和 `h=1`：

\[
\boxed{v_p(\mathscr B_W)=2.}
\tag{5.1}
\]

而 `31,179` 都满足

\[
p\equiv3\pmod4.
\]

所以它们在本 regime 对 `B_W` 的 global inert parity贡献为偶数。

历史 serial-parity theorem 已证明

\[
\mathscr B_W\equiv7\pmod8,
\]
故其所有 `3 mod4` prime exponents 的总 parity 为奇。整个 `Sigma_first` pool 的每枚 prime都以 `2h` 偶深度进入 `B_W`，不能承担这份全局奇 parity。

因此若 fixed `31/179` triple-deep point 落入 (4.6)，则必存在至少一枚

\[
\boxed{r\equiv3\pmod4}
\]

在 `B_W` 中以奇次出现，并且

\[
\boxed{r\notin\Sigma_{\rm first}.}
\tag{5.2}
\]

换句话说，first-node fixed-target escape不是免费的：它自动产生一份额外的 inert support surcharge。

---

## 6. canonical frontier

两个 fixed target/descent triple-deep states不再是两个未组织的 p-adic 点。它们统一满足 exact dichotomy

\[
\boxed{
\begin{cases}
\rho_p=1:\quad c_p=1<r_+=2,
&\text{second-node strict},\\[1mm]
\rho_p>1:\quad r_B=1<c_p,\ \min(c_p,\rho_p)=2,
&\text{first-node strict}.
\end{cases}}
\tag{6.1}
\]

其中第二行还必产生一枚 `Sigma_first` 外的 global inert parity supplier。

因此后续对 fixed `31/179` 不应继续机械提升 `K,d`。真正剩余的两个接口是：

1. second-node regime 的 exact conjugate depth `v_p(D_E)=3`；
2. first-node regime 强迫出的 external source-parity complement。

本文没有证明第一行为空，也没有证明第二行的 complement 与所有其它 supplier 必然独立，所以 A2 仍为 `待证`。

---

## 7. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_fixed_target_serial_dichotomy.py
```
