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

旧 extremal frontier closure 与新 high-funnel continuation：

21. [`tail-root-kappa-plus-g-crt-nogo.md`](tail-root-kappa-plus-g-crt-nogo.md)：证明看似巨大的 `kappa+G` 第三 prefix period 精确退化。
22. [`tail-root-decimal-phase-lock.md`](tail-root-decimal-phase-lock.md)：tail-root 与 decimal phase 的 2-adic audit；在旧 extremal model 上重新推出 `H=2m+o(S)` 与 `log Z=log q_c+o(S)`。
23. [`frontier-five-adic-closure.md`](frontier-five-adic-closure.md)：**关闭旧 `6.308883577618...` equality frontier**，并严格得到无界 DD 若存在则 `limsup n_3/S < 6.308883577618...`，但 gap 非有效。
24. [`high-funnel-five-adic-dichotomy.md`](high-funnel-five-adic-dichotomy.md)：在 canonical `t_2=1` double-resonant S-unit funnel 中得到 exact 5-adic 二分
   \[
   m\le5q_5+4g_5+n_5
   \quad\text{or}\quad
   3d\le m+4q_5+5g_5+2n_5.
   \]
25. [`high-funnel-defect-optimization.md`](high-funnel-defect-optimization.md)：恢复 defect-aware `F_-` height；`Tail-short` sector 得到
   \[
   \limsup n/S\le6.215109404735\ldots.
   \]
26. [`high-funnel-xi-depth.md`](high-funnel-xi-depth.md)：`Defect-heavy` slack 精确集中到单一判别 quotient：
   \[
   3v_5(\Xi)=5q_5+4g_5+n_5-m.
   \]
27. [`high-funnel-gap-depth.md`](high-funnel-gap-depth.md)：恢复 `C_0=QL+2tau` 并证明 `v_5(a)=v_5(Xi)`；defect slack就是 sphere-gap quotient `a` 的额外 5-depth。
28. [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md)：若 `b_3` 不是 5-adic maximum，则 sector 只有 slope `<=6`；剩余 `Final-5-lock` 满足
   \[
   B_5=q_5+2g_5,
   \quad m=2q_5+4g_5+n_5,
   \quad v_5(a)=q_5,
   \quad T=m-2g_5.
   \]
29. [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md)：scale-free quadratic 强制
   \[
   v_2(H_{\rm sph}-y_3)=1,
   \]
   并得到 exact `2-short / 2-balanced` 二分与 `Final-5` Schmidt height budget。
30. [`pure-common-five-squareclass-nogo.md`](pure-common-five-squareclass-nogo.md)：pure common-scale 的深 `5^{2g}` Hensel 只剩一个模 5 quadratic-character bit；继续 same-prime lifting没有线性高度收益。

历史 `q-Z` allocation（严格但已被更强 normalization 覆盖）：

31. [`high-funnel-qz-gcd-allocation.md`](high-funnel-qz-gcd-allocation.md)：证明 `gcd(q,Z)` 可分配到 denominator overlap / third-exclusive common scale。
32. [`high-funnel-qz-projective-allocation.md`](high-funnel-qz-projective-allocation.md)：继续把 third-exclusive payer送入 projective denominator / sphere gap。
33. [`high-funnel-qz-two-sheet-split.md`](high-funnel-qz-two-sheet-split.md)：把 residual `q-Z` overlap分为 gap / complementary 两 sheets，并证明“common prime 自动制造两条独立 carrier residual”是错误预期。

最新 exact small-factor / gap-square continuation：

34. [`high-funnel-exact-small-factor-normalization.md`](high-funnel-exact-small-factor-normalization.md)：严格区分 gcd-normal `q_red` 与 `Q=Uq` 的 source `q`。令
   \[
   s=(2\cdot5^T,q),
   \]
   则
   \[
   L=\frac{2\cdot5^T}{s},
   \qquad q_{\rm red}=q/s,
   \qquad \tau=q_{\rm red}V,
   \]
   且 `q_red|E`。最终得到
   \[
   \boxed{
   F_-=
   \frac{2^{H+2}5^TZ}{s}
   \;a\frac{g_*}{V},
   }
   \]
   特别地
   \[
   \boxed{Z\mid F_-.}
   \]
   所以第 31–33 项中的 `gcd(q,Z)` height loss在 canonical `t_2=1` 主恒等式中实际上完全消失；这些文件保留为正确中间账本，但不再是当前 bottleneck。
35. [`high-funnel-two-balanced-collapse.md`](high-funnel-two-balanced-collapse.md)：曾用 `2-balanced` 得到 sector `<=6.152932680260...`；该结论仍正确，但已被第 36 项覆盖。
36. [`high-funnel-final-five-collapse.md`](high-funnel-final-five-collapse.md)：保留 exact small factor 中此前漏掉的完整二进 overlap
   \[
   v_2\!\left(a(g_*/V)/s\right)=\mathfrak g.
   \]
   与 `U-height` 联立后 `mathfrak g log 2` 精确抵消，整个 `Final-5-lock` 得到
   \[
   \boxed{
   \limsup n/S\le5.805865360520\ldots.
   }
   \]
   因而 canonical double-resonant `t_2=1` funnel 中 `Defect-heavy` 的 `>6.215109...` remaining sheet为空；结合 `Tail-short`，该 funnel整体满足
   \[
   \boxed{
   \limsup n/S\le
   \frac{28}{3+5\log_{10}2}
   =6.215109404735\ldots.
   }
   \]
   **这是 funnel-level 显式 bound，目前尚未无条件升级为全 DD numerical limsup。**
37. [`high-funnel-gap-square-core.md`](high-funnel-gap-square-core.md)：将 exact small factor 与
   \[
   F_-=2(\kappa+2G)\mu^2/G_0
   \]
   对齐，得到
   \[
   \boxed{5^Ta_0G_0=s\varepsilon\mu^2.}
   \]
   pure common 中化为 `a_0G_0=epsilon*(square)`。
38. [`high-funnel-gap-epsilon-allocation.md`](high-funnel-gap-epsilon-allocation.md)：对 `p` 不整除 10 证明
   \[
   \min(v_p(a_0),v_p(\varepsilon))\le v_p(\lambda).
   \]
   pure common 中若 `d=(a_0,epsilon)`, `a_0=dA`, `epsilon=dE`，则
   \[
   d\mid\lambda,
   \qquad E\mid G_0,
   \qquad A(G_0/E)=\mu_0^2.
   \]
39. [`high-funnel-recovery-squarefree-lock.md`](high-funnel-recovery-squarefree-lock.md)：显式恢复
   \[
   \frac\mu\nu
   =\frac{\varepsilon Lc^2r_*a_0}{q_0}
   \]
   的最低项。若
   \[
   h=(\varepsilon Lc^2r_*a_0,q_0),
   \]
   则
   \[
   \boxed{h^2G_0=2\varepsilon^3Lc^4r_*^2a_0,}
   \]
   因而
   \[
   \boxed{\operatorname{sqf}(G_0)=\operatorname{sqf}(2\varepsilon La_0).}
   \]
   pure common 中进一步为
   \[
   \boxed{\operatorname{sqf}(G_0)=\operatorname{sqf}(\varepsilon a_0).}
   \]
   所以 recovery gcd已无自由 squarefree support；剩余自由在 square depth / Archimedean height。

## 当前严格状态

DD **全局仍为 `待证`**；没有有效绝对 `S` 上界，也没有证明 DD 全体为空。

此前依赖经典 Schmidt Subspace Theorem 有

\[
\limsup_{\rm DD}\frac{n_3}{S}
\le6.308883577618\ldots.
\]

第 23 项严格关闭旧 equality frontier，所以当前最强**全局**渐近表述仍是

\[
\boxed{
\text{若 DD solutions 在 }S\text{ 上无界，则}
\quad
\limsup_{\rm DD}\frac{n_3}{S}
<6.308883577618\ldots.
}
\]

这个 strict gap 仍是非有效的。

另一方面，第 36 项已经把 canonical double-resonant `t_2=1` S-unit funnel **显式**压到

\[
\boxed{6.215109404735\ldots.}
\]

最初 merged DD handoff 的依赖图明确记录：旧全局 `6.308883...` 的顶端来自

\[
\text{unique }2/5\text{-resonant S-unit funnel}
+\text{tail slope collapse}.
\]

但是 canonical 文档没有保留 post-tail 之后其它 dominant side branches 的完整定量系数表。因此在重新核完这些旁支之前，不能仅凭 funnel 改进就把 `6.215109...` 宣布成新的全 DD explicit limsup。

### 当前真正的两个任务

1. **branch reoptimization**：把全局 `m/S<=5` tail collapse重新代回非-funnel dominant states，证明它们的 post-tail slope都不超过 `6.215109...`（或找出真正的新最大旁支）。
2. **absolute-height line**：在 canonical funnel 内，`q-Z` gcd 已不再是 bottleneck；gap/recovery 已压成
   \[
   5^Ta_0G_0=s\varepsilon\mu^2,
   \qquad
   h^2G_0=2\varepsilon^3Lc^4r_*^2a_0.
   \]
   下一自由度是 `h` 与 `G_0` 的 square depth / height，而不是新的 radical support。

## 可复核脚本

DD 的机械证书位于 [`scripts/exact-lift/double-deficit/`](../../../../../scripts/exact-lift/double-deficit/)。本 continuation 的新增/关键脚本包括：

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

以及此前的 `check_dd_good_*` / `check_dd_genuine_*` / `check_dd_pairmax_*` 账本脚本。

这些脚本只认证正文声明的有限代数、valuation ledger 与常数计算，不承担 DD 全局空性证明。