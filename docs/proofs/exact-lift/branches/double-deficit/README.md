# `double-deficit`（DD）分支

这是 DD 分支的规范编辑入口。新增 continuation 按依赖单独记录，并严格区分 `已严格完成`、`有限/计数结论`、`待证` 与 `失效/降级`。

## 阅读顺序

基础部分：

1. [`core.md`](core.md)：DD 统一正规化、有限证书、相对界、Schmidt 渐近界与原 extremal frontier。
2. [`frontier.md`](frontier.md)：假想 `n_3/S -> 6.308883577618...` terminal geometry、rational/genuine contact、5-adic allocation、decimal remainder、Good/Bad 与历史 no-go 审计。

full-rational / mixed Good continuation：

3. [`good-radius-excess.md`](good-radius-excess.md)：Good baseline/excess 正规化与 `G_exc`。
4. [`good-axis-normalization.md`](good-axis-normalization.md)：`epsilon_p=max(v_p(alpha)-v_p(N_c),0)` 与三条 canonical excess reader。
5. [`good-excess-gcd-ladder.md`](good-excess-gcd-ladder.md)：`C_N^k` gcd ladder、stable tail、deficit/overflow separation。
6. [`good-short-residue-audit.md`](good-short-residue-audit.md)：local second-short-residue no-go 审计。
7. [`good-prefix-polarization.md`](good-prefix-polarization.md)：`(n_1,m_1,n_2,m_2)=(S,0,0,S)+o(S)`。
8. [`good-prefix-crt-location-audit.md`](good-prefix-crt-location-audit.md)：旧 Q/G unique prefix lift 的 natural-representative no-go。
9. [`mixed-rational-good-extension.md`](mixed-rational-good-extension.md)：Bad closure 扩展到任意 mixed split；partial rational main mass几乎全为 Good。

genuine / pair-max continuation：

10. [`genuine-discriminant-carrier.md`](genuine-discriminant-carrier.md)：unified discriminant 的第二 square-depth Gaussian carrier。
11. [`genuine-discriminant-cross-audit.md`](genuine-discriminant-cross-audit.md)：raw cross determinant 无 Archimedean saving。
12. [`genuine-denominator-cleared-carrier.md`](genuine-denominator-cleared-carrier.md)：ghost carrier 清回 original integers。
13. [`genuine-full-concat-carrier.md`](genuine-full-concat-carrier.md)：`C_sigma^2 | Q a_2^2b_1^2 beta ± W a_3`。
14. [`genuine-full-concat-hensel.md`](genuine-full-concat-hensel.md)：two-level Hensel ledger。
15. [`genuine-tail-root-orientation-lock.md`](genuine-tail-root-orientation-lock.md)：tail quadratic 判别式线性化并锁死 relative Gaussian orientation。
16. [`genuine-elliptic-collapse.md`](genuine-elliptic-collapse.md)：surviving elliptic second lift完全由 sphere square-depth支付。
17. [`genuine-a12-second-order-crt.md`](genuine-a12-second-order-crt.md)：moving-W genuine `A_12` residue。
18. [`genuine-a12-fixed-crt.md`](genuine-a12-fixed-crt.md)：W-free fixed genuine `A_12` residue。
19. [`genuine-large-core-crt.md`](genuine-large-core-crt.md)：历史 intermediate threshold `log C_G/S>0.382232844764...`；已被下一项覆盖。
20. [`pairmax-fixed-a12-crt.md`](pairmax-fixed-a12-crt.md)：将 W-free square-depth 全局化到整个 one-channel `C_L`，与 `q_c^2` 联立得到 universal fixed-fiber prefix uniqueness。

最新 tail-root / 5-adic closure：

21. [`tail-root-kappa-plus-g-crt-nogo.md`](tail-root-kappa-plus-g-crt-nogo.md)：证明看似巨大的 `kappa+G` 第三 prefix period 精确退化，因为
   \[
   \kappa+G=\gamma\Sigma,
   \qquad
   \mathscr T BV-U\kappa G^2=U\kappa G(\kappa+G).
   \]
22. [`tail-root-decimal-phase-lock.md`](tail-root-decimal-phase-lock.md)：tail-root 与 decimal phase 的 2-adic audit，重新推出 extremal model 的
   \[
   H=2m+o(S),
   \qquad
   \log Z=\log q_c+o(S).
   \]
23. [`frontier-five-adic-closure.md`](frontier-five-adic-closure.md)：**关闭旧 `6.308883577618...` equality frontier。** 利用同一个 unified discriminant root 的 DD 强化 `W=L Xi`，得到 tail-root 两项的 5-adic 深度分别为 `T/2+o(S)` 与至少 `T+o(S)`，无法满足模 `5^d`，其中 `d=3.5S+o(S)`。
24. [`high-funnel-five-adic-dichotomy.md`](high-funnel-five-adic-dichotomy.md)：把上述矛盾推广到整个 slope `>7` 的唯一 S-unit funnel，得到 exact finite-height 二分
   \[
   \boxed{m\le5q_5+4g_5+n_5}
   \quad\text{or}\quad
   \boxed{3d\le m+4q_5+5g_5+2n_5}.
   \]
   下一步应把它与 stability defect重新做线性优化。

## 当前严格状态

DD **全局仍为 `待证`**；没有有效绝对 `S` 上界，也没有证明 DD 全体为空。

但旧的 extremal asymptotic equality frontier 已经关闭。此前依赖经典 Schmidt Subspace Theorem 有

\[
\limsup_{\rm DD}\frac{n_3}{S}
\le6.308883577618\ldots.
\]

最新 5-adic contradiction证明：不存在无界 DD sequence 满足

\[
\frac{n_3}{S}\to6.308883577618\ldots.
\]

因此严格更新为：

\[
\boxed{
\text{若 DD solutions 在 }S\text{ 上无界，则}
\quad
\limsup_{\rm DD}\frac{n_3}{S}
<6.308883577618\ldots.
}
\]

这个 strict gap 目前仍是**非有效**的：尚未恢复一个显式新的 numerical slope。

### 1. 为什么 equality frontier 会矛盾

DD §18 对统一判别根有

\[
W=L\Xi.
\]

extremal frontier 的 5-adic baseline给

\[
v_5(L)=T+o(S).
\]

另一方面

\[
\mathscr T=\frac{\kappa^2(\kappa+2G)}{10^m}
\]

只有

\[
v_5(\mathscr T)=\frac T2+o(S).
\]

tail-root 模 `5^d` 要求两个不同深度的整数相消到

\[
d=3.5S+o(S),
\]

但其和只能保持较浅的 `T/2+o(S)=0.9362945...S+o(S)` 深度，矛盾。

### 2. 更一般的 high-funnel 二分

在旧证明已经严格压出的 slope `>7` unique funnel 中，记

\[
B_5=v_5(b_3),\quad q_5=v_5(Q),\quad g_5=v_5(G),\quad n_5=v_5(\mathcal N_{12}).
\]

新的 exact lemma迫使每个候选满足：

\[
\boxed{m\le5q_5+4g_5+n_5}
\]

或

\[
\boxed{3d\le m+4q_5+5g_5+2n_5}.
\]

所以任何继续维持大 `m,d` 的候选必须让 `q_5,g_5,n_5` 至少一个承担正线性 defect。当前最直接的下一任务是重建旧 stability inequality中这些 defect 的显式惩罚系数，并求一个新的 LP optimum。

### 3. equality-frontier continuation 的新定位

`good-*`、`genuine-*`、`pairmax-fixed-a12-crt.md` 等文件仍是严格的**条件结构定理 / no-go 审计**，但其共同假设的 `6.308883...` equality frontier 已被第 23 项排除。

其中尤其有可迁移机制：

\[
C_L^2\mid
\Theta=(\kappa+G)Q(a_2b_1)^2\beta+\mathscr T a_3^2,
\]

以及 fixed whole-`C_L` prefix period；这些可能在新的较低 frontier 中继续使用，但不能无条件外推到所有 DD。

## 可复核脚本

DD 的机械证书位于 [`scripts/exact-lift/double-deficit/`](../../../../../scripts/exact-lift/double-deficit/)。本轮新增/关键脚本包括：

- `check_dd_genuine_tail_root_orientation_lock.py`
- `check_dd_genuine_elliptic_collapse.py`
- `check_dd_genuine_a12_fixed_crt.py`
- `check_dd_genuine_large_core_crt.py`
- `check_dd_mixed_rational_good_extension.py`
- `check_dd_pairmax_fixed_a12_crt.py`
- `check_dd_tail_root_kappa_plus_g_crt_nogo.py`
- `check_dd_tail_root_decimal_phase_lock.py`
- `check_dd_frontier_five_adic_closure.py`
- `check_dd_high_funnel_five_adic_dichotomy.py`

以及此前的 `check_dd_good_*` / `check_dd_genuine_*` 账本脚本。

这些脚本只认证正文声明的有限代数、valuation ledger 与常数计算，不承担 DD 全局空性证明。