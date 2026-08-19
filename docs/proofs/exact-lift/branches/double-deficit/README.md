# `double-deficit`（DD）分支

这是 DD 分支的规范编辑入口。主干与 frontier 后续分开保存；新增 continuation 均按依赖单独记录，并严格区分 `已严格完成`、`有限/计数结论`、`待证` 与 `失效/降级`。

## 阅读顺序

1. [`core.md`](core.md)：DD 统一正规化、有限证书、相对界与全局未闭合核心。
2. [`frontier.md`](frontier.md)：假想 `n_3/S -> 6.308883577618...` frontier 的 one-channel、rational contact、5-adic allocation、decimal remainder、Good/Bad 与旧 no-go 审计。
3. [`good-radius-excess.md`](good-radius-excess.md)：full-rational Good 的 baseline/excess 正规化与 `G_exc`。
4. [`good-axis-normalization.md`](good-axis-normalization.md)：证明 `epsilon_p=max(v_p(alpha)-v_p(N_c),0)`，构造三条 canonical excess reader。
5. [`good-excess-gcd-ladder.md`](good-excess-gcd-ladder.md)：`C_N^k` gcd ladder、stable tail、deficit/overflow separation。
6. [`good-short-residue-audit.md`](good-short-residue-audit.md)：审计 local second-short-residue 候选；carry / `N(Delta_1)` / axis baseline 均不可重复收费。
7. [`good-prefix-polarization.md`](good-prefix-polarization.md)：`(n_1,m_1,n_2,m_2)=(S,0,0,S)+o(S)`，prefix 正线性 entropy 全在 `a_1`。
8. [`good-prefix-crt-location-audit.md`](good-prefix-crt-location-audit.md)：full-rational Q/G natural representatives精确退回 reconstruction / clean source；给 uniqueness，不给 emptiness。
9. [`genuine-discriminant-carrier.md`](genuine-discriminant-carrier.md)：由 unified discriminant构造 `W^2+Omega^2` square-depth carrier。
10. [`genuine-discriminant-cross-audit.md`](genuine-discriminant-cross-audit.md)：`Omega y_2/(Wy_3)=10^{-9S+o(S)}`；raw cross determinant无 Archimedean saving。
11. [`genuine-denominator-cleared-carrier.md`](genuine-denominator-cleared-carrier.md)：ghost cross 清回 original integers，得到 cube-depth digit carrier。
12. [`genuine-full-concat-carrier.md`](genuine-full-concat-carrier.md)：识别 `beta=Q10^{m_3}+b_3`，得到 `C_sigma^2 | Q a_2^2b_1^2 beta ± W a_3`。
13. [`genuine-full-concat-hensel.md`](genuine-full-concat-hensel.md)：把 square-depth 分成 exact first lift + unit-unit second lift。
14. [`genuine-tail-root-orientation-lock.md`](genuine-tail-root-orientation-lock.md)：primitive tail quadratic 判别式线性化；global tail-root sign `eta` 锁死 genuine `same/opp` relative orientation。
15. [`genuine-elliptic-collapse.md`](genuine-elliptic-collapse.md)：surviving elliptic second lift经 W-free `Theta` 精确退回 original sphere square-depth；same-prime discriminant route只剩 orientation reader。
16. [`genuine-a12-second-order-crt.md`](genuine-a12-second-order-crt.md)：从 surviving square-depth读取模 `C_G` 的 moving-W `A_12` residue。
17. [`genuine-a12-fixed-crt.md`](genuine-a12-fixed-crt.md)：用 carry-square消去 `W,a_3`，得到 fixed 模 `C_G` linear `A_12` CRT。
18. [`genuine-large-core-crt.md`](genuine-large-core-crt.md)：曾得到 `log C_G/S>0.382232844764...` 时 fixed-fiber uniqueness；该 threshold 现已被第 20 项的 split-independent 结果全面覆盖，保留作中间证书。
19. [`mixed-rational-good-extension.md`](mixed-rational-good-extension.md)：证明 Bad closure 不要求 full rational contact；任意 mixed split 中 partial rational main mass仍几乎全是 Good，Good slot/excess ladder可把 `C_L` 替换为 `E=D_+D_-`。
20. [`pairmax-fixed-a12-crt.md`](pairmax-fixed-a12-crt.md)：**当前最强 prefix 结论。** `Sphere-pay-identity` 实际完全不依赖 rational/genuine split，故对整个 one-channel main core有
   \[
   C_L^2\mid\Theta,
   \qquad
   \Theta=(\kappa+G)Q(a_2b_1)^2\beta+\mathscr T a_3^2.
   \]
   carry-square 因而给 split-independent fixed congruence
   \[
   2\mathscr T g_0B10^d v_0\Sigma R_0A_{12}
   \equiv M_{L,0}\pmod{C_L}.
   \]
   与 fixed `q_c^2` residue 联立，联合 period 高度恒为
   \[
   1.617767155236\ldots S+o(S),
   \]
   所以任意 terminal frontier fixed fiber 中 `A_12` / `a_1` 至多一个，不再需要 rational/genuine 分支或 genuine-mass threshold。

## 当前严格状态

DD 全局仍为 `待证`。当前最强全局渐近界仍是

\[
\limsup_{\rm DD}\frac{n_3}{S}
\le 6.308883577618\ldots,
\]

其阈值使用经典 Schmidt Subspace Theorem，非有效。上述 continuation 的新结论都只在假想 frontier sequence 上成立，不能推出 DD 全局空性或有效绝对高度界。

### 1. pair-max prefix 已统一，不再依赖 rational/genuine split

one-channel main core满足

\[
V=C_Lv_0,
\qquad
\log C_L=S+o(S),
\qquad
(q_c,C_L)=10^{o(S)}.
\]

新的 split-independent W-free carrier为

\[
\boxed{
C_L^2\mid
\Theta=(\kappa+G)Q(a_2b_1)^2\beta+\mathscr T a_3^2.
}
\]

其 square-depth完全由 original sphere carrier支付，故不能重复当 local height；但把 exact carry平方后，可以读取一个 fixed whole-`C_L` decimal period：

\[
\boxed{
2\mathscr T g_0B10^d v_0\Sigma R_0A_{12}
\equiv M_{L,0}\pmod{C_L}.
}
\]

clean source同时给 fixed Q-side：

\[
\boxed{
g_0B10^dVA_{12}\equiv XR_0\pmod{q_c^2}.}
\]

两 period渐近互素，因此

\[
\boxed{
\log(C_Lq_c^2)
=1.617767155236\ldots S+o(S)>\log A_{12}=S+o(S).
}
\]

所以：

\[
\boxed{
\#\{A_{12}\text{ in any fixed terminal frontier fiber}\}\le1,
\qquad
\#\{a_1\}\le1.
}
\]

这是 `有限/计数结论`，还不是 emptiness。

### 2. full/partial rational Good 仍有独立 cofactor 问题

Bad closure已经扩展到任意 mixed split：

\[
\boxed{\log(B_+B_-)=o(S)}.
\]

因此 partial rational-contact main core `E=D_+D_-` 几乎全进入 Good。对其可定义

\[
E_N=E/(E,N_c),
\qquad
A_N=\alpha/(\alpha,N_c),
\]

\[
G_{\rm exc}^{(R)}=(E_N,A_N),
\qquad
D_k^{(R)}=(E_N^k,A_N),
\]

并继续使用 slot / excess ledger。这个 cofactor 问题与 universal prefix uniqueness并不等价；后者只锁 decimal prefix candidate，前者仍可能用于 eventual emptiness。

### 3. discriminant same-prime route 已基本闭包

primitive tail quadratic给 exact global sign `eta`，genuine relative orientation被锁死；wrong hyperbolic sign无 main mass。surviving W-free second lift满足 `Sphere-pay-identity`，其 square-depth完全由原 sphere carrier支付。

因此继续从

\[
W,\ \Omega,\ K_\sigma
\]

构造同素数 higher resultant / short representative属于 `失效/降级`。这些对象目前只保留 orientation / CRT reader 价值。

### 4. 现在真正剩余的 terminal frontier

prefix entropy已经压到“每个 fixed fiber至多一个”。要继续接近 closure，需要至少完成其一：

- 对 split-independent residue
  \[
  A_{12}\pmod{C_Lq_c^2}
  \]
  的唯一 lift做真正独立的 Archimedean digit-window exclusion；
- 找到不由 sphere / carry / clean-source / hidden-square parents重构的第三 fixed residue；
- 或利用 partial-rational Good cofactor ledger证明任何合法 fixed fiber本身为空。

## 可复核脚本

DD 的机械证书位于 [`scripts/exact-lift/double-deficit/`](../../../../../scripts/exact-lift/double-deficit/)。主要包括：

- `check_dd_good_radius_excess.py`
- `check_dd_good_axis_normalization.py`
- `check_dd_good_excess_gcd_ladder.py`
- `check_dd_good_short_residue_audit.py`
- `check_dd_good_prefix_polarization.py`
- `check_dd_good_prefix_crt_location_audit.py`
- `check_dd_genuine_discriminant_carrier.py`
- `check_dd_genuine_discriminant_cross_audit.py`
- `check_dd_genuine_denominator_cleared_carrier.py`
- `check_dd_genuine_full_concat_hensel.py`
- `check_dd_genuine_tail_root_orientation_lock.py`
- `check_dd_genuine_elliptic_collapse.py`
- `check_dd_genuine_a12_fixed_crt.py`
- `check_dd_genuine_large_core_crt.py`
- `check_dd_mixed_rational_good_extension.py`
- `check_dd_pairmax_fixed_a12_crt.py`

这些脚本只认证正文声明的有限赋值逻辑、常数账本与 exact identities，不承担 DD emptiness 的证明。