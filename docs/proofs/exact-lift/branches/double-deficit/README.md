# `double-deficit`（DD）分支

这是 DD 的规范编辑入口。正文与 continuation 严格区分 `已严格完成`、`有限证书`、`待证` 与 `失效/降级`；历史 equality-frontier 文件保留为条件结构定理与 no-go 记录，不再把已关闭的 frontier 当作可实现候选层。

## 1. 基础与旧 frontier

1. [`core.md`](core.md)：DD 统一正规化、relative bounds、gcd-normal form、primitive determinant / carrier、Schmidt tail collapse 与旧 extremal geometry。
2. [`frontier.md`](frontier.md)：假想 `n_3/S -> 6.308883577618...` 的 terminal geometry、rational/genuine contact、Gaussian/projective allocation 与历史 no-go。
3. [`frontier-five-adic-closure.md`](frontier-five-adic-closure.md)：**严格关闭旧 `6.308883577618...` equality frontier**。因此若 DD solutions 在 `S` 上无界，
   \[
   \boxed{\limsup_{\rm DD} n_3/S<6.308883577618\ldots}
   \]
   但 gap 仍非有效。

## 2. equality-frontier 内的结构 continuation（历史条件工具）

这些文件仍严格，但共同的 extremal equality hypothesis 已被第 3 项排除；其作用是保留可迁移机制。

- [`good-radius-excess.md`](good-radius-excess.md)
- [`good-axis-normalization.md`](good-axis-normalization.md)
- [`good-excess-gcd-ladder.md`](good-excess-gcd-ladder.md)
- [`good-short-residue-audit.md`](good-short-residue-audit.md)
- [`good-prefix-polarization.md`](good-prefix-polarization.md)
- [`good-prefix-crt-location-audit.md`](good-prefix-crt-location-audit.md)
- [`mixed-rational-good-extension.md`](mixed-rational-good-extension.md)
- [`genuine-discriminant-carrier.md`](genuine-discriminant-carrier.md)
- [`genuine-discriminant-cross-audit.md`](genuine-discriminant-cross-audit.md)
- [`genuine-denominator-cleared-carrier.md`](genuine-denominator-cleared-carrier.md)
- [`genuine-full-concat-carrier.md`](genuine-full-concat-carrier.md)
- [`genuine-full-concat-hensel.md`](genuine-full-concat-hensel.md)
- [`genuine-tail-root-orientation-lock.md`](genuine-tail-root-orientation-lock.md)
- [`genuine-elliptic-collapse.md`](genuine-elliptic-collapse.md)
- [`genuine-a12-second-order-crt.md`](genuine-a12-second-order-crt.md)
- [`genuine-a12-fixed-crt.md`](genuine-a12-fixed-crt.md)
- [`genuine-large-core-crt.md`](genuine-large-core-crt.md)
- [`pairmax-fixed-a12-crt.md`](pairmax-fixed-a12-crt.md)

## 3. canonical `t_2=1` double-resonant funnel

这一条线已经从旧 `6.308883...` equality analysis 推广为 finite-height / sector-level lemmas。

- [`high-funnel-five-adic-dichotomy.md`](high-funnel-five-adic-dichotomy.md)：exact 5-adic dichotomy
  \[
  m\le5q_5+4g_5+n_5
  \quad\text{or}\quad
  3d\le m+4q_5+5g_5+2n_5.
  \]
- [`high-funnel-defect-optimization.md`](high-funnel-defect-optimization.md)：第一次 defect-aware LP；历史 `Tail-short <= 6.215109404735...`。
- [`high-funnel-xi-depth.md`](high-funnel-xi-depth.md)、[`high-funnel-gap-depth.md`](high-funnel-gap-depth.md)、[`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md)：把 `Defect-heavy` 压到 `Final-5` rigid sheet。
- [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md)：强制 `v_2(H-y_3)=1`，并给 `2-short / 2-balanced` 二分。
- [`high-funnel-two-balanced-collapse.md`](high-funnel-two-balanced-collapse.md)：历史 sector improvement。
- [`high-funnel-exact-small-factor-normalization.md`](high-funnel-exact-small-factor-normalization.md)：
  \[
  F_-=
  \frac{2^{H+2}5^TZ}{s}\,a\frac{g_*}{V},
  \qquad Z\mid F_-.
  \]
- [`high-funnel-final-five-collapse.md`](high-funnel-final-five-collapse.md)：`Final-5`
  \[
  \boxed{\limsup n/S\le5.805865360520\ldots.}
  \]
- [`high-funnel-tail-short-schmidt-upgrade.md`](high-funnel-tail-short-schmidt-upgrade.md)：把 Tail-short 从旧 `6.215109...` 再压到
  \[
  \boxed{\limsup n/S\le\frac6{1+\log_{10}2}=4.611730721041\ldots.}
  \]
  与其余 sheets 合并后得到当前严格 funnel-level 结论
  \[
  \boxed{\limsup_{\rm canonical\ t_2=1\ double\text{-}resonant} n/S\le6.}
  \]
- [`high-funnel-625-rigidity.md`](high-funnel-625-rigidity.md)、[`high-funnel-final5-two-adic-optimization.md`](high-funnel-final5-two-adic-optimization.md)、[`high-funnel-final5-sphere-c3-collapse.md`](high-funnel-final5-sphere-c3-collapse.md)：进一步记录 `6.25` 邻域、二进与 sphere common-scale 的 rigidification。

### gap / recovery square line

- [`high-funnel-gap-square-core.md`](high-funnel-gap-square-core.md)：
  \[
  5^Ta_0G_0=s\varepsilon\mu^2.
  \]
- [`high-funnel-gap-epsilon-allocation.md`](high-funnel-gap-epsilon-allocation.md)：common epsilon depth 分配。
- [`high-funnel-recovery-squarefree-lock.md`](high-funnel-recovery-squarefree-lock.md)：
  \[
  h^2G_0=2\varepsilon^3Lc^4r_*^2a_0,
  \qquad
  \operatorname{sqf}(G_0)=\operatorname{sqf}(2\varepsilon La_0).
  \]
- [`high-funnel-square-identities-audit.md`](high-funnel-square-identities-audit.md)：审计上述 square identities，避免把同一 recovery algebra重复收费。
- [`pure-common-five-squareclass-nogo.md`](pure-common-five-squareclass-nogo.md)：pure common 的深 5-adic Hensel 只剩一个 mod-5 square-class bit，没有线性高度收益。

### `q-Z` 历史路线

[`high-funnel-qz-gcd-allocation.md`](high-funnel-qz-gcd-allocation.md)、[`high-funnel-qz-projective-allocation.md`](high-funnel-qz-projective-allocation.md)、[`high-funnel-qz-two-sheet-split.md`](high-funnel-qz-two-sheet-split.md)、[`high-funnel-qz-sheet-reader-collapse.md`](high-funnel-qz-sheet-reader-collapse.md)、[`high-funnel-qz-bottom-orientation-correction.md`](high-funnel-qz-bottom-orientation-correction.md) 均保留为严格中间账本；但 exact small-factor normalization 已证明 canonical funnel 中 `Z|F_-`，因此 `gcd(q,Z)` 不再是当前 height bottleneck。

## 4. post-tail / non-canonical dominant branch reoptimization（当前主线）

目标：把 global tail collapse `limsup m/S<=5` 与第二次 fixed-target Schmidt rough product重新喂回其它 dominant states，决定能否把全 DD 的 explicit asymptotic bound升级到 `<=6`。

### 4.1 denominator rough source 被压成 `X_Q`

- [`gcd-normal-exact-small-factor.md`](gcd-normal-exact-small-factor.md)：对整个 gcd-normal tail
  \[
  F_-=r(u+2v)\,a(g_*/v).
  \]
- [`tail-rough-d0-allocation.md`](tail-rough-d0-allocation.md)：第二次 Schmidt 的 `d_0` rough height除 actual small-factor payer外，只剩 primitive denominator-concat cancellation。
- [`tail-rough-cq-excess.md`](tail-rough-cq-excess.md)：对 `p|core_{10}(d_0)`，写
  \[
  v_p(b_1)=v_p(b_2)=E,\quad v_p(b_3)=j,\quad c=v_p(C_Q),
  \]
  canonical unpaid depth为
  \[
  \boxed{x_p=\max(c-j-\min(E,j),0).}
  \]
  并定义 `X_Q=prod p^{x_p}`。第二次 Schmidt 的唯一 hard loss是 `log X_Q`。
- [`tail-pure-cancellation-three-sheet.md`](tail-pure-cancellation-three-sheet.md)、[`tail-pure-cancellation-hensel-nogo.md`](tail-pure-cancellation-hensel-nogo.md)、[`tail-hard-source-derivative-sheet.md`](tail-hard-source-derivative-sheet.md)、[`tail-source-cancellation-transfer.md`](tail-source-cancellation-transfer.md)：baseline-free / hard local sheets及历史 no-go。

### 4.2 general source transfer：`X_Q` 离开 denominator 世界

[`tail-rough-general-transfer.md`](tail-rough-general-transfer.md) 对任意 denominator baseline严格证明
\[
\boxed{
 x_p\le
 \max\!\left(
 v_p(C),
 v_p(N_0),
 v_p(R_3^{\rm den})
 \right),
}
\]
其中
\[
N_0=\frac{\mathcal N_{12}}{(b_1,b_2)^2},
\qquad
R_3^{\rm den}=\frac{b_3}{(b_3,\operatorname{lcm}(b_1,b_2))}.
\]
因此 denominator source overflow全部转移到 numerator / Gaussian / projective payer。

### 4.3 Gaussian payer 去 denominator 化

[`tail-rough-gaussian-payer-split.md`](tail-rough-gaussian-payer-split.md) 写
\[
g_n=(a_1,a_2),
\qquad
N_{\rm ang}=\frac{N_0}{g_n^2}.
\]
`N_ang` 是 primitive sum of two squares，因此所有 odd rough prime均 `1 mod 4`；`3 mod 4` rough mass只能回流到 common numerator或 projective/gap。

[`tail-rough-angular-source-transfer.md`](tail-rough-angular-source-transfer.md) 定义纯 numerator Gaussian integer
\[
Z_{\rm num}=-\bar a_1 10^{m_2}+i\bar a_2,
\qquad
N_{\rm num}=N(Z_{\rm num}),
\]
并由 exact identity
\[
Z_{\rm ang}-B_1Z_{\rm num}=\bar a_1C_Q
\]
把 split orientation转移到 `N_num`。还得到 cyclotomic overlap
\[
\boxed{
\operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
\mid10^{2|s_2|}+1.
}
\]

### 4.4 canonical payer layers

[`tail-rough-canonical-payer-decomposition.md`](tail-rough-canonical-payer-decomposition.md) 对每个 `p^x||X_Q` 按 exponent layer定义
\[
e_3+e_B+e_G+e_A=x
\]
并全局得到
\[
\boxed{X_Q=X_3X_BX_GX_A,}
\]
with canonical readers
\[
X_3\mid Z_0a,
\qquad
X_B\mid C_{12}\mid R_{12},
\qquad
X_G\mid(a_1,a_2),
\qquad
X_A\mid N_{\rm num}.
\]
这里 `R_12` 是 orientation-uniform bottom determinant reader。

[`tail-rough-third-angular-absorption.md`](tail-rough-third-angular-absorption.md) 进一步证明：若
\[
r=v_p(R_3^{\rm den})>0,
\qquad
\omega=v_p(N_{\rm ang}),
\]
则 integer sphere 强制
\[
\boxed{v_p(Z_0a)\ge r+\omega.}
\]
因此同一 prime上的 third-exclusive 与 Gaussian-angular layers不是两个独立 payer。写
\[
X_A=X_{A,3}X_{A,0},
\]
其中 `X_{A,3}` 支撑在 `R_3^{den}` 非单位 primes，则
\[
\boxed{X_3X_{A,3}\mid Z_0a.}
\]
真正独立的 Gaussian remainder `X_{A,0}` **只支撑在 `R_3^{den}` 为 p-unit 的 primes上**。

当前 post-tail rough loss因此可读成三类机制：

1. projective/gap combined layer `X_P:=X_3X_{A,3}|Z_0a`；
2. bottom/common numerator layers `X_B|R_12`, `X_G|(a_1,a_2)`；
3. residual split-Gaussian `X_{A,0}|N_num`，且其 support上没有 third-exclusive denominator depth。

这已经是当前 **branch reoptimization frontier**；不要再把 `C_Q` 或整个 `X_Q` 当作匿名 gcd loss。

## 5. 当前严格状态

DD **全局仍为 `待证`**：尚无有效绝对 `S` 上界，也未证明 DD 全体为空。

当前最强全局 asymptotic statement仍是经典 Schmidt 下的非有效严格加强：
\[
\boxed{
\text{若 DD solutions 在 }S\text{ 上无界，则}
\limsup_{\rm DD}\frac{n_3}{S}<6.308883577618\ldots.
}
\]

但 canonical `t_2=1` double-resonant funnel现在已经**显式**达到
\[
\boxed{\limsup n/S\le6.}
\]
而不是旧 README 中的 `6.215109...`。

尚不能把 `<=6` 宣布成全 DD bound：其它 post-tail dominant side branches的完整定量 reoptimization尚未完成。当前最直接目标是对上述 projective / bottom-common / residual-Gaussian payer layers建立 simultaneous height bound，并把它代回第二次 Schmidt inequality。

## 6. 可复核脚本

机械证书位于 [`scripts/exact-lift/double-deficit/`](../../../../../scripts/exact-lift/double-deficit/)。本 continuation 的关键新脚本包括：

- `check_dd_frontier_five_adic_closure.py`
- `check_dd_high_funnel_five_adic_dichotomy.py`
- `check_dd_high_funnel_defect_optimization.py`
- `check_dd_high_funnel_xi_depth.py`
- `check_dd_high_funnel_gap_depth.py`
- `check_dd_high_funnel_denominator_max_lock.py`
- `check_dd_high_funnel_two_adic_balance.py`
- `check_dd_pure_common_five_squareclass.py`
- `check_dd_high_funnel_qz_gcd_allocation.py`
- `check_dd_high_funnel_qz_projective_allocation.py`
- `check_dd_high_funnel_qz_two_sheet_split.py`
- `check_dd_high_funnel_exact_small_factor_normalization.py`
- `check_dd_high_funnel_two_balanced_collapse.py`
- `check_dd_high_funnel_final_five_collapse.py`
- `check_dd_high_funnel_gap_square_core.py`
- `check_dd_high_funnel_gap_epsilon_allocation.py`
- `check_dd_tail_rough_general_transfer.py`
- `check_dd_tail_rough_gaussian_payer_split.py`
- `check_dd_tail_rough_angular_source_transfer.py`
- `check_dd_tail_rough_canonical_payer_decomposition.py`
- `check_dd_tail_rough_third_angular_absorption.py`

以及此前的 `check_dd_good_*` / `check_dd_genuine_*` / `check_dd_pairmax_*` 账本脚本。

这些脚本只认证正文声明的有限代数、valuation ledger 与常数计算；无界覆盖来自正文证明，不把有限枚举误作全局证明。
