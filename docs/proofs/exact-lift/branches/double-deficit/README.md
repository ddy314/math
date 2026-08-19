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
   \limsup n/S\le6.215109404735\ldots
   \]
   （仅为该 conditional sector，不是新全局 DD bound）。
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
   并由 tail-root 得到 exact `2-short / 2-balanced` 二分；同时恢复 `Subspace-defect` 与 `Subspace-Final5` height budget。
30. [`pure-common-five-squareclass-nogo.md`](pure-common-five-squareclass-nogo.md)：pure common-scale 的深 `5^{2g}` Hensel 最终只剩
   \[
   UV\in((\mathbf Z/5^{2g}\mathbf Z)^\times)^2,
   \]
   等价于一个模 5 quadratic-character bit；继续 same-prime 5-adic lifting没有线性高度收益。
31. [`high-funnel-qz-gcd-allocation.md`](high-funnel-qz-gcd-allocation.md)：从 `u(u+2v)|F_-Q` 抽出
   \[
   L_Z=\frac{2^{H+2}5^TZ}{(2^{H+2}5^TZ,q)}\mid F_-,
   \]
   并证明
   \[
   \gcd(q,Z)^2\mid\gamma(R_3^{\rm den})^2.
   \]
32. [`high-funnel-qz-projective-allocation.md`](high-funnel-qz-projective-allocation.md)：用 projective denominator exact formula继续消去 `R_3^{den}`，得到当前最干净的 rough-gcd payer theorem
   \[
   \boxed{\gcd(q,Z)^2\mid\gamma Z_0^2a^2.}
   \]

## 当前严格状态

DD **全局仍为 `待证`**；没有有效绝对 `S` 上界，也没有证明 DD 全体为空。

此前依赖经典 Schmidt Subspace Theorem 有

\[
\limsup_{\rm DD}\frac{n_3}{S}
\le6.308883577618\ldots.
\]

第 23 项已经严格排除任何无界 sequence 满足

\[
\frac{n_3}{S}\to6.308883577618\ldots,
\]

因此当前最强全局渐近表述是

\[
\boxed{
\text{若 DD solutions 在 }S\text{ 上无界，则}
\quad
\limsup_{\rm DD}\frac{n_3}{S}
<6.308883577618\ldots.
}
\]

这个 strict gap 仍是**非有效**的；本 continuation 中出现的 `6.215109...`、`6.361730...`、`6.611730...` 都是明确写了作用域的 conditional sector bounds，不能替代上述 global strict limsup。

### 当前新的 high-funnel 核

在 canonical `t_2=1` double-resonant funnel 中，5-adic 与 2-adic 账本已经分别压成：

\[
\boxed{
B_5=q_5+2g_5,
\quad
m=2q_5+4g_5+n_5,
\quad
v_5(a)=q_5,
}
\]

以及

\[
\boxed{v_2(H_{\rm sph}-y_3)=1,}
\]

再加

\[
\boxed{
 d\le m+2\mathfrak q+\mathfrak n+\mathfrak g-1
}
\]
或

\[
\boxed{
2\mathfrak g=m+\mathfrak q+\ell-2.
}
\]

pure common-scale endpoint在 5-adic quadratic 上没有继续 Hensel 收益，因此当前真正值得攻击的是 rough-factor compatibility。

### 当前 rough-factor payer theorem

令 `Q=Uq`、`5^TU+V=2^HZ`。现已证明

\[
\boxed{
L_Z:=
\frac{2^{H+2}5^TZ}{\gcd(2^{H+2}5^TZ,q)}
\mid F_-.
}
\]

而

\[
\boxed{
\gcd(q,Z)^2\mid\gamma Z_0^2a^2.
}
\]

所以 `q-Z` common rough height 不再是一个未命名自由池：它只能由

1. denominator overlap `gamma`；
2. stereographic projective denominator `Z_0`；
3. sphere-gap quotient `a`

支付。

下一步应把这一三 payer theorem 与无 `E_D` carrier-circle eliminant / primitive determinant ladder 联立。当前尚缺的关键 propagation lemma 是：从 `q-Z` common prime 推出两条**独立** carrier residual 的同步深接触；在没有该引理前不能直接套用 eliminant。

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

以及此前的 `check_dd_good_*` / `check_dd_genuine_*` / `check_dd_pairmax_*` 账本脚本。

这些脚本只认证正文声明的有限代数、valuation ledger 与常数计算，不承担 DD 全局空性证明。