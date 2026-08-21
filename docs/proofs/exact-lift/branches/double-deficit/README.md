# `double-deficit`（DD）分支

这是 DD 的**当前权威状态入口**。

2026-08-22 的 discriminant-root audit 发现：unified integer discriminant root 与 §18 的 reduced root `L Xi` 之间存在真实 normalization factor；此前把二者直接认同后得到的一批 5-adic high-funnel 状态必须降级。

历史账本与 `frontier.md` 保留原来源块、原状态与 no-go 记录用于审计。若旧来源块中的状态与本 README 或 2026-08-22 correction notes 冲突，以本 README / correction notes 为准。

## 1. 当前安全主结论

DD 尚未证明为空，也没有 effective absolute height bound。

当前安全的全局渐近结论为

\[
\boxed{
\limsup_{\rm DD}\frac{n_3}{S_{12}}
\le 6.308883577618\ldots
}
\]

该阈值使用 Schmidt Subspace Theorem，因此非有效。

2026-08-22 已对 corrected canonical `t_2=1` double-resonant high funnel 独立重证同一常数。令

\[
a=\log_{10}2,
\]

则

\[
\boxed{
\limsup\frac nS
\le
\frac{8+7a}{1+2a}
=6.308883577618031\ldots
}
\]

而 equality closure 强迫

\[
Q_5,G_5,N_5,R\to0,
\qquad
\frac mS\to2.808883577618\ldots,
\qquad
\frac dS\to\frac72.
\]

所以旧 `6.308883...` terminal geometry 仍是真正的 extremal geometry；当前没有正确证明把 `<=` 升级为严格 `<`。

主修正文：

- [`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md)：错误 normalization 的依赖审计与撤销表。
- [`dd-corrected-high-funnel-schmidt-2026-08-22.md`](dd-corrected-high-funnel-schmidt-2026-08-22.md)：corrected high-funnel 的独立 Schmidt + exact-small-factor 证明，恢复 `6.308883...`。
- [`frontier.md`](frontier.md)：terminal odd moving-core、full rational Good、Gaussian/projective 与 slot-capacity 的规范研究账本。
- [`dd-z0-charged-first-2026-08-21.md`](dd-z0-charged-first-2026-08-21.md)：post-tail `X_Q` charged-first local allocation；继续使用前必须按 discriminant-root audit 检查依赖。

## 2. 2026-08-22 后撤销 / 降级的旧结论

以下旧结论不得再作为覆盖整个 canonical funnel 的 theorem 引用：

1. `frontier-five-adic-closure` 通过旧 valuation mismatch 关闭 equality frontier；旧
   \[
   \limsup n/S<6.308883577618\ldots
   \]
   当前撤销，退回 `<=`。

2. `high-funnel-five-adic-dichotomy` 的 exhaustive
   \[
   \text{Defect-heavy}\cup\text{Tail-short}
   \]
   partition。

3. 旧
   \[
   3v_5(\Xi)=5q_5+4g_5+n_5-m
   \]
   (`Xi-slack`)。

4. 从该链推出的 generic `denominator-max-lock`：
   \[
   b_3\text{ 非 5-adic maximum}\Longrightarrow n<6S+O(1),
   \]
   以及把所有 remaining states强制到
   \[
   B_5=q_5+2g_5,
   \qquad
   m=2q_5+4g_5+n_5.
   \]

5. `high-funnel-tail-short-schmidt-upgrade.md` 中依赖上述 branch exhaustion 的 whole-funnel `<=6` 合并结论。其 LP 在额外 Tail-short 条件成立时仍可作为条件计算读取。

6. `Final-5` 仍可作为额外条件 sheet；不得再描述为 remaining high funnel 的必然终态。

## 3. corrected 5-adic local ledger

令

\[
E_5:=\max_i v_5(b_i),
\qquad
B_5:=v_5(b_3),
\qquad
q_5:=v_5(Q).
\]

在相应 `B_5<m` high-funnel discriminant-separation region，正确的 depth 为

\[
\boxed{
v_5(\Xi)=q_5+E_5-B_5.
}
\]

若 `b_3` 是 5-adic maximum，则

\[
\boxed{v_5(\Xi)=q_5.}
\]

结合

\[
\Xi=|\mathcal M-C_0a|,
\qquad
C_0=QL+2\tau,
\]

及 decimal depth，在对应作用域内有

\[
\boxed{
v_5(a)=q_5+E_5-B_5,
}
\]

从而

\[
\boxed{
v_5(H-y_3)=T+(E_5-B_5).
}
\]

另一方面

\[
\widehat g=\gamma/c_3
\]

满足

\[
v_5(\widehat g)=g_5-(E_5-B_5).
\]

所以 denominator-max deficit 在 actual small factor 中精确抵消：

\[
\boxed{
v_5\bigl((H-y_3)\widehat g\bigr)=T+g_5.
}
\]

## 4. corrected canonical high-funnel Schmidt proof

canonical `t_2=1` phase保留

\[
\kappa=2\gamma5^TU,
\qquad
\kappa+2G=2\gamma2^HZ,
\qquad
2^HZ-5^TU=V.
\]

fixed-target Schmidt 给

\[
\log U+\log Z\ge S-o(S).
\]

结合 decimal pinning 与 resonance，独立得到

\[
\boxed{
\frac{2(1+2a)}3M
+2aQ_2+aN_2
+\frac{1-a}{3}(2Q_5+4G_5+N_5)
+2R
\le3.
}
\]

同时 exact

\[
F_-=2^{H+1}Z(H-y_3)\widehat g
\]

和上一节的 corrected 5-adic cancellation 给 whole-funnel small-factor inequality。两式具有直接 dual certificate：

\[
\boxed{
\limsup\frac nS
\le
\frac{8+7\log_{10}2}{1+2\log_{10}2}.
}
\]

后续 strict-gap 工作以这套 corrected inequalities 为 baseline，不再调用旧 `Five-dichotomy / Xi-slack / Final-5 exhaustion`。

## 5. equality terminal 的安全结构

若存在 sequence 满足

\[
\frac nS\to6.308883577618\ldots,
\]

corrected dual equality强迫系统回到旧 terminal ratios。真正剩余的正线性 entropy 是 odd split-prime moving core

\[
V=C_Lv_0,
\qquad
\log C_L=S+o(S),
\qquad
\log v_0=o(S).
\]

因此 `frontier.md` 中 odd moving core、Gaussian orientation、sign-Farey、Lorentz cofactor、hidden-square/no-double-pay 等**条件恒等式**继续可用。

其中任何依赖旧 5-adic mismatch 来宣称 equality 已被排除的历史文字均由本 README supersede。

## 6. full rational-contact：Bad 已关闭，当前只研究 Good

旧分解写

\[
C_L=D_+D_-C_G\cdot10^{o(S)}.
\]

full rational-contact 指

\[
D_+D_-=C_L^{1-o(1)}.
\]

`frontier.md` 的后续 continuation 已证明 Bad repeat 不能承载正线性质量：

\[
\boxed{
\log(B_+B_-)=o(S).
}
\]

selected / conjugate orientation 在 `Delta_U` 中的重复总质量也只有 `o(S)`。因此 full rational-contact 在 leading order 上是 **Good**。

当前 Good 的关键 exact / local 结构包括：

- cofactor Lorentz system `(CF1)`--`(CF5)`；
- `Good-cofactor-unit`
  \[
  \boxed{
  \log\gcd\bigl(C_L,d^2N_c+R_0^2H_J\bigr)=o(S);
  }
  \]
- `next-R / next-J / axis-carrier / radius-overlap / pure-radius` 五类 local slots；
- `next-J` 与 `next-R`、axis-repeat 的逐素数互斥；
- pair-max orientation 可由 derivative gcd 唯一重构；
- second-order Newton、near-square `2/5` CRT、三 Gaussian quotient projective determinant等路线已经证明退化或精确临界；
- full rational moving-core 的 orientation entropy 已压到 `10^{o(S)}`。

因此以后不得再把 Bad 当作开放 frontier，也不应继续重做 Bad-CF / `Nc-elim` closure。

## 7. 当前 full rational Good frontier

删去 `o(S)` exceptional core 后，main prime-power 只能进入有限 local network：

1. `next-R`：`p | H_R`；
2. `next-J`：`p | H_J`；
3. `axis/carrier`：`p | N_c`，且只能使用 selected orientation 的 conjugate Gaussian orientation；
4. `radius overlap`：由 `min(v_p(H_R),v_p(N_c))` 自动支付；
5. `pure-radius`：抽掉 equal-depth baseline 后，`Nc1-elim` 的 unit-unit cancellation；该条件等价于 `p | alpha`。

其中

\[
\boxed{
\text{next-J 与 next-R / axis-repeat 逐素数互斥。}
}
\]

Good 目前可以进一步压成

\[
\boxed{
\text{cofactor slots}
\;\cup\;
\text{equal-depth residual}
\;\cup\;
\text{pure numerator-shell contact }(C_L,\alpha).
}
\]

另有 exact bridge

\[
\boxed{
g_0\alpha=(2^HZ+5^TU)A_0.
}
\tag{Concat-radius}
\]

因此当前 full rational Good 的首选目标是 **primitive digit-shell lemma**：证明在 rational sign contact 与 `Good-cofactor-unit` 已成立后，main pair-max modulus不能再以正线性高度进入 `alpha` 或 equal-depth residual。

如果该尝试只再次恢复 `Concat-radius`、hidden square 或 `(CF1)`--`(CF5)`，则应视为 full rational Good 的 local algebra 已闭包，停止继续制造 local resultant。

## 8. genuine-Gaussian branch

若

\[
C_G=10^{\varepsilon S+o(S)}
\]

对某个 `epsilon>0`，main primes 不满足 rational sign contact `A congruent +/- b`。这一支仍需 genuine split-prime / projective / digit-shell compatibility。

旧 first-order rational resultant在这些 primes处为 unit，因此不能复用 full-rational closure。

## 9. post-tail / non-canonical dominant line

细粒度历史研究保存在：

- [`tail-allocation-ledger.md`](tail-allocation-ledger.md)
- [`high-funnel-ledger.md`](high-funnel-ledger.md)
- [`good-genuine-ledger.md`](good-genuine-ledger.md)

内部来源块保留当时状态。涉及 unified discriminant root、`W=LXi`、5-adic mismatch、Five-dichotomy、Xi-slack、denominator-max exhaustion 的任何结论，都必须先经过 [`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md)。

post-tail charged-first 仍提供 denominator-source factor allocation视角；喂回 global slope 前要逐项确认其 local transfer 不通过失效的 discriminant-root chain。

## 10. 已判死 / 不应重开的 terminal 路线

- standalone tangent / blow-up；
- cross-resultant 与 near-axis norm 直接 gcd；
- U/Z side same-prime norm resultants；
- Bad branch 作为正线性 frontier；
- Bad 直接桥接 bottom determinant；
- `t_p+b_p<=h_p`；
- 单靠 `C_0` 与 digital norm gcd；
- 模 `A_0` 的 small-gcd argument；
- generic first-order GCD / Subspace / Ridout closure；
- first-order hyperbolic `2x2` determinant mining；
- second-order Newton/Hensel 继续迭代；
- near-square 小 CRT root 当作新 phase；
- 三 Gaussian quotients继续做普通 projective determinant。

这些方向要么精确回到 hidden square / existing norm / source channels，要么 leading-order product-formula budget恰好临界。

## 11. 当前优先任务

1. full rational Good：证明 primitive digit-shell lemma，优先处理 `(C_L,alpha)` 与 equal-depth residual。
2. 将 Good 的 `next-R / next-J / axis-carrier / pure-radius` local network做全局容量统计，寻找不能同时饱和的 slot。
3. 若 digit-shell 再次回到 `Concat-radius` / hidden square / Lorentz critical system，则停止 full-rational local eliminant，转 genuine-Gaussian branch。
4. genuine-Gaussian：寻找真正的 split-prime / projective / digit-shell compatibility，不再使用 rational sign-contact resultant。
5. 得到 strict-gap terminal结论后，再反馈 post-tail / non-canonical global branch partition。
